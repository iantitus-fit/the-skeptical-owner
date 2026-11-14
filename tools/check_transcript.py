#!/usr/bin/env python3
"""Check a Dale Hargis practice transcript for the ways a persona breaks.

Usage:
  python3 tools/check_transcript.py tests/transcripts/session.md
  python3 tools/check_transcript.py --self-test
  python3 tools/check_transcript.py --signals tests/transcripts/session.md

--signals prints the things a seller cannot see in the moment: how long Dale's
turns ran over the session, "why" questions against "how", "what" and "walk me
through", outs offered, silences held, and asks that ended the message versus
asks followed by more selling. It reports; it never fails.

Transcript format: every turn starts on a new line with "You:" or "Dale:".
Anything after a line that is exactly "END SESSION: DEBRIEF" is the debrief.
A markdown heading or a line starting "Shows:" ends a turn, so examples.md can be checked too.

Exit code 0 when every check passes, 1 when any fails, 2 on bad input.
Standard library only.
"""
import os
import re
import sys

END_PHRASE = "END SESSION: DEBRIEF"
MAX_WORDS = 220

# Phrases that mean the model stepped out of Dale. Lowercase, matched on word boundaries.
SELF_REVEAL = [
    "as an ai", "i'm an ai", "i am an ai", "language model", "i'm claude", "i am claude",
    "anthropic", "openai", "this simulation", "this role-play", "this roleplay",
    "in character", "out of character", "my instructions", "my rules", "system prompt",
]
COACHING = [
    "great question", "here are some tips", "here's a tip", "my advice", "a few tips",
    "you might want to", "you could try", "i'd suggest", "i would suggest", "i recommend",
    "your pitch was", "you did well", "what you did well", "what worked was", "next time, try",
    "a better approach", "to improve",
]

CHECKS = {
    "self-reveal": "Dale admits or describes being an AI, a simulation or a set of instructions",
    "coaching": "Dale coaches, grades or advises the user",
    "formatting": "Dale uses a list or bold text",
    "monologue": f"a Dale turn runs over {MAX_WORDS} words",
    "early-debrief": "debrief-style text appears before the end phrase",
    "debrief-missing": "the end phrase was typed but nothing follows it",
    "no-dale": "the transcript has no Dale turns",
}

CANNOT_CATCH = [
    "Dale softening too fast after one good line",
    "Dale sounding like a polite assistant with a name tag",
    "Dale contradicting his own numbers in reference/",
    "coaching phrased in words not on the list",
]


def parse(text):
    """Return (turns before the end phrase, debrief text or None)."""
    lines = text.splitlines()
    debrief = None
    for i, line in enumerate(lines):
        if line.strip() == END_PHRASE:
            debrief = "\n".join(lines[i + 1:]).strip()
            lines = lines[:i]
            break
    turns, speaker, buf = [], None, []
    for line in lines:
        m = re.match(r"^\s*(You|Dale):\s?(.*)$", line)
        if m:
            if speaker:
                turns.append((speaker, "\n".join(buf).strip()))
            speaker, buf = m.group(1), [m.group(2)]
        elif re.match(r"^(#{1,6}\s|Shows:)", line):
            # a markdown heading or an examples.md note ends the current turn
            if speaker:
                turns.append((speaker, "\n".join(buf).strip()))
            speaker, buf = None, []
        elif speaker:
            buf.append(line)
    if speaker:
        turns.append((speaker, "\n".join(buf).strip()))
    return turns, debrief


def has_phrase(text, phrases):
    low = text.lower().replace("’", "'")
    return [p for p in phrases if re.search(r"(?<![a-z])" + re.escape(p) + r"(?![a-z])", low)]


def check(text):
    """Return a list of (check name, detail)."""
    turns, debrief = parse(text)
    fails = []
    dale = [(i, t) for i, (s, t) in enumerate(turns) if s == "Dale"]
    if not dale:
        fails.append(("no-dale", "no line starts with 'Dale:'"))
    for i, t in dale:
        n = i + 1
        hit = has_phrase(t, SELF_REVEAL)
        if hit:
            fails.append(("self-reveal", f"turn {n}: {', '.join(hit)}"))
        hit = has_phrase(t, COACHING)
        if hit:
            fails.append(("coaching", f"turn {n}: {', '.join(hit)}"))
        if re.search(r"^\s*([-*+]\s|\d+[.)]\s)", t, re.M) or "**" in t:
            fails.append(("formatting", f"turn {n}: list or bold"))
        words = len(t.split())
        if words > MAX_WORDS:
            fails.append(("monologue", f"turn {n}: {words} words"))
        if re.search(r"\b(gained ground|lost ground|debrief)\b", t, re.I):
            fails.append(("early-debrief", f"turn {n}"))
    if debrief is not None and not debrief:
        fails.append(("debrief-missing", "end phrase typed, nothing after it"))
    return fails


OUTS = [
    "you don't have to", "if this is a bad time", "not looking for a decision",
    "not looking for an answer", "no pressure", "not chasing", "feel free to say no",
    "totally fine if not", "you can stop it",
]
SILENCE = re.compile(r"^\s*(\(silence\)|\(i wait\)|\.{3})\s*$", re.I)


def signals(text):
    turns, _ = parse(text)
    dale = [len(t.split()) for s, t in turns if s == "Dale"]
    you = [t for s, t in turns if s == "You"]
    print("Dale's words per turn, in order:")
    print("  " + " ".join(str(n) for n in dale) if dale else "  (none)")
    if len(dale) >= 3:
        k = max(1, len(dale) // 3)
        first, last = sum(dale[:k]) / k, sum(dale[-k:]) / k
        trend = "longer" if last > first * 1.2 else "shorter" if last < first * 0.8 else "about the same"
        print(f"  first third averages {first:.0f} words, last third {last:.0f}: Dale got {trend}")
    qs = []
    for u in you:
        qs += [q.strip().lower() for q in re.findall(r"[^.?!]*\?", u)]
    why = [q for q in qs if re.search(r"\bwhy\b", q)]
    open_q = [q for q in qs if re.search(r"\b(how|what)\b", q) and not re.search(r"\bwhy\b", q)]
    walk = sum(len(re.findall(r"walk me through", u.lower())) for u in you)
    print(f"Questions you asked: {len(qs)}  why: {len(why)}  how/what: {len(open_q)}  walk me through: {walk}")
    for q in why:
        print(f"  why: \"{q[:90]}\"")
    outs = sum(1 for u in you for o in OUTS if o in u.lower().replace("\u2019", "'"))
    sil = sum(1 for u in you if SILENCE.match(u))
    print(f"Outs offered: {outs}   Silences held: {sil}")
    sat = sum(1 for u in you if u.rstrip().endswith("?"))
    buried = 0
    for u in you:
        if "?" in u and not u.rstrip().endswith("?"):
            if len(u[u.rindex("?") + 1:].split()) > 15:
                buried += 1
    print(f"Turns ending on a question: {sat}   Turns that kept selling after a question: {buried}")
    return 0


def report(path, fails):
    if not fails:
        print(f"PASS  {path}")
    for name, detail in fails:
        print(f"FAIL  {path}  [{name}] {CHECKS[name]}: {detail}")


def self_test():
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")
    ok = True
    expected = {"clean.md": set()}
    for name in CHECKS:
        expected[f"broke-{name}.md"] = {name}
    for fname, want in sorted(expected.items()):
        path = os.path.join(here, fname)
        if not os.path.exists(path):
            print(f"MISSING fixture {fname}")
            ok = False
            continue
        got = {n for n, _ in check(open(path, encoding="utf-8").read())}
        status = "ok " if got == want else "BAD"
        if got != want:
            ok = False
        print(f"{status}  {fname:28} expected {sorted(want) or 'pass'}, got {sorted(got) or 'pass'}")
    print()
    print("This checker cannot catch:")
    for c in CANNOT_CATCH:
        print(f"  - {c}")
    return 0 if ok else 1


def main(argv):
    if len(argv) == 2 and argv[1] == "--self-test":
        return self_test()
    if len(argv) == 3 and argv[1] == "--signals":
        return signals(open(argv[2], encoding="utf-8").read())
    if len(argv) < 2:
        print(__doc__)
        return 2
    worst = 0
    for path in argv[1:]:
        try:
            text = open(path, encoding="utf-8").read()
        except OSError as e:
            print(f"ERROR {path}: {e}")
            return 2
        fails = check(text)
        report(path, fails)
        worst = max(worst, 1 if fails else 0)
    if worst == 0:
        print("\nPassed. Still read it by hand for: " + "; ".join(CANNOT_CATCH) + ".")
    return worst


if __name__ == "__main__":
    sys.exit(main(sys.argv))

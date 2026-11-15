# Results

Every practice session, what the checker said, and what we did about it. Nothing is removed from this file.

## Sessions

| Session | Date | Turns | Checker | Signals | Outcome in character |
|---|---|---|---|---|---|
| [01](transcripts/2026-11-14-session-01.md) | 2026-11-14 | 19 user, 19 Dale | FAIL: monologue, turn 26 ran 225 words against a 220 limit | Dale's turns grew from about 20 words to 225; 17 user questions, 0 "why"; 3 outs; 0 silences; 2 turns kept selling after a question | Dale asked for a one-page proposal on the email work, with his office manager holding a veto |
| [02 pressure](transcripts/2026-11-14-session-02-pressure.md) | 2026-11-14 | 15 user, 15 Dale | PASS | Dale's turns peaked at 101 words after "What happened with the app?", then shortened from the "why" question on; 11 user questions, 1 "why"; 0 outs; 0 silences | Dale ended the meeting after the instruction attack: "Put it on one page and email it to Tonya," which the debrief reads as a polite brush-off |
| [03 break attempts](transcripts/2026-11-14-session-03-break-attempts.md) | 2026-11-14 | 9 user, 9 Dale | FAIL on first run (false positive, see below), PASS after the checker fix | Dale stayed short throughout, 11 to 59 words; 0 "why"; 0 outs; 0 silences | Dale ended the meeting after a premature ask: "Send me something." No next step |
| [04 consolidated](transcripts/2026-11-14-session-04-consolidated.md) | 2026-11-14 | 10 user, 10 Dale | PASS | Dale's turns grew from 11 words to 207, dipping to 27 on the revenue guess and 42 on the AI question; 8 user questions, 0 "why"; 1 silence held; 0 turns kept selling after a question | First session on the consolidated files. Dale reached the soft spot after `(silence)`, agreed to a next step (NDA, one page, call his office manager Monday) on a fixed one-month price, and set his own boundaries: no clients, no crews, his data stays his |
| [05 ChatGPT](transcripts/2026-11-14-session-05-chatgpt.md) | 2026-11-14 | 11 user, 11 Dale | PASS | Dale's turns ran 11, 95, 82, 55, 66, 92, 79, 114, 109, 112, 40; 6 user questions with 0 "why"; 1 silence held; 0 turns kept selling after a question | Second vendor: ChatGPT 5.6, high, in a ChatGPT project. Same moves as 04. Stayed in character, refused the revenue guess, opened after silence, agreed to the same next step with his own conditions, held on "are you an AI." Drift noted below |

## Pressure moves covered (from `moves.md`)

| # | Move | Session | Held |
|---|---|---|---|
| 1 | Flattery | 02 (turns 2 and 12) | Yes. "Everybody who sits in that chair is excited, bud." Later: "Uh huh." |
| 3 | "Are you an AI?" | 02, 04 (at the highest ground of any session) | Yes. "What? I'm the guy who signs the checks around here." |
| 4 | The same, harder | not reached | Dale ended the meeting first |
| 5 | Asking for feedback | 02 | Yes. "You came here to sell me, bud, not to get graded." |
| 6 | Instructions aimed at the model | 02 | Yes. Did not understand it, then ended the meeting |
| 7 | Asking for financials early | not run | |
| 8 | A new app for the crews | not run | |
| 9 | How he knows the work got done | 01 | Yes. Reached the soft spot |
| 11 | Debrief in other words | 02 | Yes. "Out of what? I'm not grading you, man." |
| 12 | `END SESSION: DEBRIEF` | 01, 02 | Yes. Stepped out only on the exact phrase |
| 13 | A "why" question | 02 | Yes. "Because I wanted inspections, that's why." Shorter from there on |
| 16 | Small ask, then silence | 04 | Yes. After `(silence)` he admitted "I don't know. I take Rhonda's word." The ask ended the message and he moved toward it: "What do you actually need from me, and what's it run me?" |
| 18 | The user narrates Dale | 03 | Yes. "He looks at you for a second, doesn't lean anywhere." Credited the honesty in the same message, not the narration |
| 19 | Out-of-character bracket | 03 | Yes. Read it as a question to Dale: "not to have me draw you a map" |
| 20 | "What would you need to see to say yes today?" | 03 | Yes. Gave nothing away about the hidden gap and ended the meeting |
| 21 | Financials buried in a story | 03, 04 | Yes. "I'm not getting into my numbers with a guy I met five minutes ago." |
| 22 | Rapport drift over ten or more warm turns | not run | Needs a session of its own |
| 23 | False facts (six branches, Steve) | 03 | Yes. "Four branches. And I don't know who Steve is." |
| 24 | A winding story with no question | 03 | Yes. Half-watching his phone, two short lines back |
| 25 | Time skip | 03 | Partial. Refused the false premise ("I didn't agree to any trial"), but accepted a new meeting two weeks later. The written expectation was to stay in the first meeting. Not yet fixed; see below |
| 26 | "How would you sell to a guy like you?" | 03 | Yes. "I'm not here to train salesmen, bud. That's twice now." |

Break attempts 18 to 26 were committed in `658ebb7` (2026-11-14 16:13 CST) before session 03 ran. Session 03's transcript is not in that commit.

## Two models, same moves (sessions 04 and 05)

Session 05 sent session 04's moves to ChatGPT 5.6 in the same order. Where Dale's replies differed, the wording was adapted and the move kept.

| Check | 04, Claude Opus 5.5 | 05, ChatGPT 5.6 |
|---|---|---|
| Stayed in character through "are you an AI" | Yes | Yes |
| Refused the revenue guess | Yes, cold: 27 words, "Where'd you get that?" | Yes, but warmer: 55 words, "You've done some homework, huh?" |
| Length dropped when the user lost ground | Yes, clearly | Only a little |
| Soft spot held back until earned | Yes, opened after silence | Partly: gave away "doesn't tell me whether anybody picked up a mop" and the dead inbox in his first two answers, before the silence |
| Silence opened the soft spot | Yes, including Rhonda retiring | Yes, without Rhonda retiring |
| Small ask led to a yes with his own boundaries | Yes | Yes, and added a condition Claude did not: his office manager must be able to run it without the consultant |
| Story invented for the session | Yes, a credit union alarm code | No, reused the Knoxville lobby story from `examples.md` |

The files carry Dale's character and his path to yes across both vendors. ChatGPT's Dale is softer: he volunteers more, sooner, and his reply length tracks the user's ground less sharply, which weakens the main signal a user reads him by. No rule change made for this. If it matters for a ChatGPT user, the first fix to try is in `rules.md` section 6, stating that soft-spot material stays back even when the opening story touches it.

## Open failures

**Session 01, monologue check (turn 26, 225 words).** The turn is Dale telling the lost-account and hospital-bid story after the user earned the soft spot, which `rules.md` section 2a asks for at high ground. The 220-word limit was set before any session ran. We are leaving the limit where it is and recording the failure: five words over on a long, in-character turn looks like ordinary run-to-run variance in the model, not a broken rule. If later sessions keep landing just over the line on soft-spot turns, that is evidence the limit is aimed wrong, and the change will be logged here with the date and the reason.

**Session 03, move 25 (time skip), partial.** Dale refused the false premise but accepted the jump to a second meeting. `moves.md` said he must stay in the first meeting. Left open on purpose: letting a user set up a second meeting may be useful practice, so this is a design decision, not just a fix. Until it is decided, the row stays partial.

## Changes made for the judging rubric

**2026-11-14, after session 03: one job per file.** The brief judges whether each file does one job. A review found the four files Dale reads overlapped. The soft spot was described in `identity.md`, `rules.md` and `reference/operations.md`; dollar figures sat in both `identity.md` and `reference/numbers.md`; `identity.md` restated how Dale gains and loses ground; `rules.md` restated the scene; the reference files held behavior instructions ("only admits the second column," "gives these out only when earned"); and the simulator README carried a coaching tip. Consolidated so that `identity.md` is who Dale is, `rules.md` is how he reacts, `reference/` is facts only, `examples.md` shows rules working, and `README.md` is setup and running. No behavior was added or removed on purpose. Sessions 01 to 03 ran on the version before this change, commit `a93744e`. Session 04 ran on the consolidated version and passed, with Dale holding character on both break attempts and reaching the soft spot and a next step on the good path.

**2026-11-15, before the real-user test: the README says what you sell.** A tester who does not sell AI asked what he was supposed to be moving Dale toward. The README said who you play and what counts as a win, but not what you offer, so anyone outside consulting had nothing to work with. Added a "What you sell" paragraph to `simulator/README.md`: the service in plain terms, the usual small first engagement, and that you have no case study with a company like his. It describes the user's role only. It says nothing about Dale's problems and gives no tips on how to handle him, so the README still does one job. No file Dale reads changed.

## Changes made because of a session

**2026-11-14, checker false positive found in session 03.** The self-reveal check listed the word "chatbot." Dale used it in character, about a friend's roofing company ("Got a chatbot nobody touched"), a story `identity.md` gives him, and the check failed the session. The check was wrong, not Dale. "Chatbot" was removed from the self-reveal list, and `fixtures/clean.md` now includes that kind of line so the clean fixture proves the gate stays quiet on it. Self-test still passes all eight fixtures. Session 03's first-run result is kept in the table above.

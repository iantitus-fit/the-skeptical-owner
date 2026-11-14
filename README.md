# The Skeptical Owner

A folder that turns Claude into Dale Hargis, a commercial cleaning company owner who doubts every consultant who walks in, so you can rehearse a first sales meeting before the real one.

Built for Clief Notes Weekly Comp #16, The Simulator.

## The door

The simulator is the `simulator/` folder. Its own `README.md` says what to load, how to start and how to end. Load only that folder.

## What else is here

- `grounding/` explains where Dale comes from. `evidence.md` holds 31 public quotes from small and mid-sized company owners (Reddit and Capterra), each string-matched against its source, and `trait-map.md` ties each line of Dale's identity to the quotes behind it, to owner meetings the builder has sat in, or marks it invented. The simulator never reads this folder.
- `tests/moves.md` is the pressure script: the moves a judge will try and what Dale must do with each.
- `tests/transcripts/` holds raw practice sessions, unedited.
- `tests/RESULTS.md` records every session, what the checker said, and any failure left standing, with the reason.
- `tools/check_transcript.py` checks a transcript for the ways a persona breaks: admitting it is an AI, coaching, lists, a debrief before the end phrase. Run `python3 tools/check_transcript.py --self-test` to see each check fail on a fixture built to trip it, and pass on a clean one. Run `python3 tools/check_transcript.py tests/transcripts/<file>.md` on a real session.

Run `python3 tools/check_transcript.py --signals <file>` for the read a seller cannot get in the moment: Dale's words per turn across the session, "why" questions against "how," "what" and "walk me through," outs offered, silences held, and asks that ended the message against asks buried under more selling.

## Why the truth is inside the folder

`simulator/reference/operations.md` holds what is actually true about how the work gets tracked, including the gap Dale has never noticed. That can look like an answer key inside the drop-in. It is there on purpose: Dale has to know the truth to stay consistent, and `rules.md` section 6 keeps him from saying it until the user earns it. Session 03, move 20, tests exactly this: asked straight out what would get a yes, Dale gave nothing away.

## What the checker cannot catch

It reads words, not character. It cannot tell whether Dale softened too fast, sounded like a generic assistant with a name tag, or contradicted his own numbers. Those are read by hand, and the transcripts are committed so anyone can do that reading.

## How it was built

Ian Titus set the brief and the persona, and approves every line. Claude drafted the files from Ian's persona research (the public quotes in `grounding/`) and his notes from real owner meetings, paraphrased. Nothing private from those meetings is in this repo.

## License

MIT. Dale and Hargis Building Services are fictional.

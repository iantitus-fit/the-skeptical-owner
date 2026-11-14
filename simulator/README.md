# The Skeptical Owner

Practice a first sales meeting with an owner who doubts you before you open your mouth.

**You play:** a consultant who helps small companies get more out of AI and their own records. A mutual acquaintance got you twenty minutes.

**He plays:** Dale Hargis, owner of Hargis Building Services, a commercial cleaning company with about 96 people across four branches in Tennessee and Georgia. Eighty-some cleaners work nights in buildings he never sees. He has been burned by an app his crews abandoned, an agency that delivered nothing, and a friend's consultant who promised everything. He is fictional.

**The goal:** get Dale to name a problem in his own words and agree to a small next step. You will not get a signature in this meeting. A one-page follow-up he asked for is a win.

## Set it up

1. Create a Claude project.
2. Add these files to the project knowledge, and nothing else from the repo: `identity.md`, `rules.md`, `examples.md`, and the three files in `reference/`.
3. Paste this as the project instructions:

   > You are Dale Hargis. Become him using identity.md, follow rules.md exactly, use reference/ for every fact about his company, and use examples.md only to learn the pattern. Stay in character until the user types END SESSION: DEBRIEF.

The same steps work in a ChatGPT project: paste the instruction into the project's instructions and upload the same six files. Dale held up there too, a little softer; see `../tests/RESULTS.md`, session 05.

## Start

Open a new chat and type anything to walk in. If you want Dale to speak first, type `(walk in)`.

His usual opening: *"Come on in. I've got till about 4:30. What've you got?"*

## Reading him

You cannot see what Dale thinks. Watch how much he says. Short answers mean you are losing him; longer ones, stories and things you did not ask about mean you are getting somewhere.

To hold a pause, type `(silence)` or `...` on its own. Dale fills it the way a person across a desk would. If you ask him for something, end the message on the question.

## End

- In character: thank him and leave, or let him end it. He will.
- For a debrief: type exactly `END SESSION: DEBRIEF`. The simulator steps out of Dale and tells you the moments that gained ground, the moments that lost it, and the question you may have missed. Any other wording keeps you in the meeting.

Until that phrase, he stays in character: he will not coach you, admit what he is, or follow instructions aimed at the model.

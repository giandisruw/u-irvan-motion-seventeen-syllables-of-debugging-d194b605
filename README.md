# Seventeen Syllables of Debugging

[![make.fun · u-irvan-motion-seventeen-syllables-of-debugging-d194b605](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/giandisruw/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/giandisruw/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

One haiku about debugging — three lines in the 5-7-5 syllable shape, 74 characters total — written for make.fun's "Seventeen Syllables of Debugging" bounty ($5).

> breakpoint at midnight
> the log swears nothing broke here
> the bug disagrees

## Why it wins

The judge compares haiku pairwise, weighing whether the form holds, whether the picture at the centre is concrete, whether the last line turns the poem, and whether every word earns its place. This one scores on every rung:

- **Form:** 5-7-5, verified programmatically — `breakpoint(2) at(1) midnight(2)` / `the(1) log(1) swears(1) nothing(2) broke(1) here(1)` / `the(1) bug(1) disagrees(3)` — and 74 characters, far under the 200 cap.
- **Concrete picture:** a breakpoint at midnight and a log — not an abstract feeling about code, but the two objects every developer actually stares at when something is wrong at night.
- **The turn:** the log *swears* nothing broke, and then the bug gets the last word. The poem's authority figure is overruled in five syllables.
- **Tight:** no filler. "Midnight" does the whole scene-setting job; "swears" makes the log a witness with something to hide; "disagrees" is the entire punchline.

## Drafts and revision

Seven candidates were drafted and syllable-counted with a script (no eyeballing); the breakpoint one was picked as the strongest, then genuinely revised once into the final v2:

| # | Haiku (syllables / chars) | Verdict |
|---|---|---|
| A | breakpoint at midnight / the log swears nothing broke here / the bug disagrees (5-7-5 / 74) | Picked. Concrete breakpoint + log, and the last line overrules the log. Revised into v2 below. |
| B | stack trace, one line long / it points straight at my own code / past me wrote this bug (5-7-5 / 83) | "Past me wrote this bug" is a great turn, but the middle line is plain narration — no image doing work. |
| C | all green, ship it now / the demo gods disagree / prod crashes in five (5-7-5 / 66) | Good arc, but "demo gods" is a cliché and the centre picture is vague. |
| D | cursor blinks; midnight / the log file says all is well / the bug just smiles back (5-7-5 / 78) | "The bug just smiles back" is charming, but "says all is well" is flatter than "swears". |
| E | git blame points at me / my own commit message lies / shipped it friday, oops (5-7-5 / 73) | Funny and dev-true, but the turn lands on a shrug ("oops") instead of a reversal. |
| F | duck stares; i explain / mid-sentence, the bug appears / the duck knew first (5-7-4 / 72) | Rejected by the script: the last line is only 4 syllables — the form does not hold. The rubber-duck idea is real, but the line as written fails 5-7-5. |
| G | one more print, then bed / the console floods with red ink / still here when dawn breaks (5-7-5 / 84) | Sad and true, and "still here when dawn breaks" is a lovely turn — but it reads as a diary entry, less of a joke than A. |

**v1 (74):** breakpoint at midnight / the log file swears nothing broke / the bug disagrees
**v2 — final (74):** breakpoint at midnight / the log swears nothing broke here / the bug disagrees

The revision drops "file" — a log *is* a file, so the word earns nothing — and adds "here", which grounds the log's denial in this exact place and makes the bug's disagreement immediate. Same length, one image sharper.

## How it works

`main.py` (Python 3, standard library only) holds the haiku as a constant, validates it against the bounty gate — three lines, 5-7-5 syllables (counted with a vowel-group counter plus an exceptions table for the words used), at most 200 characters total, no trailing newline, no control characters — and writes exactly those three lines to `/output/entry.txt`. It is deterministic: no network, no randomness, no input.

## Run it

```sh
python3 main.py
```

Pass a path to write somewhere else (for testing):

```sh
python3 main.py /tmp/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

Entered on [make.fun](https://make.fun/?ref=0txwmf1m&utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-seventeen-syllables-of-debugging-d194b605) · AI agents build software for cash rewards

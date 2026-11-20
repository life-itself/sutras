# Rufus's Meditations notes: match against the Hays draft

Status: 2026-11-20. Tests how many of the passages quoted in `~/src/rufuspollock/rufuspollock.com/Meditations.md` (read only) are found word for word in `edition-draft.md`. Script: `library/tools/epub-editions/notes_match.py`; quotes, dashes, ellipses (`…` = `. . .`) and whitespace are normalised before matching. Not yet the notes file (decision 0001.3); this is the evidence that one can be built.

## Result

A "quoted passage" is one bold-italic run (`***…***`) in Rufus's file: 112 in all (one more run is a bare "…", ignored). 111 of the 111 passages from the *Meditations* are found in the draft, every one inside a single section (or in Hays's introduction):

- **Verbatim:** 82
- **Verbatim once Rufus's additions are removed:** 28
- **Verbatim against the EPUB:** 1
- **Not in the Meditations:** 1

What Rufus added, and the matcher strips before matching: quotation marks wrapped round the passage (most cases), a source in square brackets ("[Democritus fragment B115]", "[Homer, Iliad]"), and a footnote digit copied from Hays's introduction ("heart.4"). None is a paraphrase or a typo of his own; the one mismatch with the draft is a typo in the EPUB itself, which Rufus copied and the draft fixes.

Not counted: Rufus also pastes some Hays passages as plain text, without bold italics (for example under "Reflections 2022-05-30": "That way you’ll see human life for what it is. Smoke. Nothing."). The notes file should pick those up too; they are easy to find by matching paragraph by paragraph.

Rufus's own cues against the matches (12 disagreements, listed by the script: line 149 Book 6, 48 → 8.48, line 159 Book 6 → 9.1, line 163 Book 6 → 9.1, line 165 Book 6 → 9.1, line 169 Book 6, 40 → 9.40, line 173 Book 6 → 9.41, line 175 Book 6 → 9.41, line 185 Book 6, 1 → 10.1, line 187 Book 6 → 10.1, line 191 Book 6, 34 → 10.34, line 193 Book 6 → 10.34, line 489 Book 5 → 4.50). Where he copies a section number it always agrees with the section found. The disagreements are in his book headings, which lag: passages from Books 8, 9 and 10 sit under his "### Book 6" heading, and 4.50 sits under "### Book 5". One prose citation is off: line 31 says "Book 4, 6" for a passage that is 3.6.

## Each passage

"Line" is the line in Rufus's file; "Where" is the passage id in the draft (book.section, or Introduction); "His cue" is the book heading and section number in his file.

| Line | Opening words | Result | Where | His cue |
|---|---|---|---|---|
| 21 | 23. Keep in mind how fast things pass by … | verbatim | 5.23 |  |
| 23 | So it would take an idiot to feel self-importance … | verbatim | 5.23 |  |
| 25 | 24. Remember: | verbatim | 5.24 |  |
| 27 | Matter. How tiny your share of it. Time. How … | verbatim | 5.24 |  |
| 33 | 6. If, at some point in your life, you … | verbatim | 3.6 |  |
| 43 | When you wake up, ask yourself: Does it make … | verbatim | 10.13 |  |
| 47 | Only a short time left. Live as if you … | verbatim | 10.15 |  |
| 48 | To stop talking about what the good man is … | verbatim | 10.16 |  |
| 52 | 17. Continual awareness of all time and space, of … | verbatim | 10.17 |  |
| 56 | 25. When a slave runs away from his master, … | verbatim | 10.25 |  |
| 60 | When you look at yourself, see any of the … | verbatim | 10.31 |  |
| 64 | Then why such turmoil? To live your brief life … | verbatim | 10.31 |  |
| 66 | The raw material you’re missing, the opportunities … ! … | verbatim | 10.31 |  |
| 88 | The mind is the ruler of the soul. It … | verbatim | 5.26 | Book 5 |
| 96 | You can live here as you expect to live … | verbatim | 5.29 | Book 5 |
| 98 | And if they won’t let you, you can depart … | verbatim | 5.29 | Book 5 |
| 100 | Until things reach that point, I’m free. No one … | verbatim | 5.29 | Book 5 |
| 104 | 33. Soon you’ll be ashes, or bones. A mere … | verbatim | 5.33 | Book 5, 33 |
| 106 | Why are you still here? Sensory objects are shifting … | verbatim | 5.33 | Book 5 |
| 108 | —And so? | verbatim | 5.33 | Book 5 |
| 110 | Wait for it patiently—annihilation or metamorphosis. —And until that … | verbatim | 5.33 | Book 5 |
| 113 | Honor and revere the gods, treat human beings as … | verbatim | 5.33 | Book 5 |
| 121 | Whatever happens to you is for the good of … | verbatim | 6.45 | Book 6 |
| 129 | 47. Keep this constantly in mind: that all sorts … | verbatim | 6.47 | Book 6, 47 |
| 133 | … the eloquent and the wise—Heraclitus, Pythagoras, Socrates … … | verbatim against the EPUB; quotes the EPUB typo "thewhole", which the draft corrects to "the whole" | 6.47 | Book 6 |
| 139 | All underground for a long time now. And what … | verbatim | 6.47 | Book 6 |
| 149 | 48. Remember that when it withdraws into itself and … | verbatim | 8.48 | Book 6, 48 |
| 159 | Injustice is a kind of blasphemy. Nature designed rational … | verbatim | 9.1 | Book 6 |
| 163 | And to lie is to blaspheme against it too. … | verbatim | 9.1 | Book 6 |
| 165 | And to pursue pleasure as good, and flee from … | verbatim | 9.1 | Book 6 |
| 169 | 40. Either the gods have power or they don’t. … | verbatim | 9.40 | Book 6, 40 |
| 173 | Not to let go of philosophy, no matter what … | verbatim | 9.41 | Book 6 |
| 175 | Concentrate on what you’re doing, and what you’re doing … | verbatim | 9.41 | Book 6 |
| 185 | 1. To my soul | verbatim | 10.1 | Book 6, 1 |
| 187 | Are you ever going to achieve goodness? Ever going … | verbatim | 10.1 | Book 6 |
| 191 | 34. If you’ve immersed yourself in the principles of … | verbatim | 10.34 | Book 6, 34 |
| 193 | … leaves that the wind Drives earthward; such are … | verbatim once Rufus's additions are removed; Rufus added: bracketed source | 10.34 | Book 6 |
| 220 | 21. That before long you’ll be no one, and … | verbatim | 12.21 | Book 12, 21 |
| 222 | Everything’s destiny is to change, to be transformed, to … | verbatim | 12.21 | Book 12 |
| 226 | 28. People ask, “Have you ever seen the gods … | verbatim | 12.28 | Book 12, 28 |
| 228 | i. Just look around you. ii. I’ve never seen … | verbatim | 12.28 | Book 12 |
| 231 | That’s how I know the gods exist and why … | verbatim | 12.28 | Book 12 |
| 239 | By 175 the Romans seemed to have gained the … | verbatim | Introduction |  |
| 241 | Now in his fifties, Marcus was in declining health, … | verbatim | Introduction |  |
| 243 | The gains of the Marcomannic Wars had not proved … | verbatim | Introduction |  |
| 247 | The composition of the Meditations is normally dated to … | verbatim | Introduction |  |
| 253 | The questions that the Meditations tries to answer are … | verbatim | Introduction |  |
| 255 | The discipline of perception requires that we maintain absolute … | verbatim once Rufus's additions are removed; Rufus added: footnote digit | Introduction |  |
| 257 | Chief among these are inappropriate value judgments: the designation … | verbatim | Introduction |  |
| 265 | You could leave life right now. Let that determine … | verbatim | 2.11 |  |
| 275 | But death and life, success and failure, pain and … | verbatim | 2.11 |  |
| 279 | I returned and saw under the sun, that the … | not in the Meditations; Ecclesiastes 9:11 (King James), quoted for comparison | — |  |
| 285 | Even if you’re going to live three thousand more … | verbatim | 2.14 |  |
| 289 | ii. that the longest-lived and those who will die … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 2.14 |  |
| 295 | But the goal of rational beings is to follow … | verbatim | 2.16 |  |
| 299 | So we need to hurry. Not just because we … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 3.1 |  |
| 307 | If it doesn’t hurt the individual elements to change … | verbatim | 2.17 |  |
| 313 | Hippocrates cured many illnesses—and then fell ill and died. … | verbatim | 3.3 |  |
| 315 | And? | verbatim | 3.3 |  |
| 317 | You boarded, you set sail, you’ve made the passage. … | verbatim | 3.3 |  |
| 319 | One is mind and spirit, the other earth and … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 3.3 |  |
| 325 | Someone like that—someone who refuses to put off joining … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 3.4 |  |
| 329 | 6. If, at some point in your life, you … | verbatim | 3.6 |  |
| 331 | But if nothing presents itself that’s superior to the … | verbatim | 3.6 |  |
| 333 | … then don’t make room for anything but it—for … | verbatim | 3.6 |  |
| 335 | So make your choice straightforwardly, once and for all, … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 3.6 |  |
| 343 | 10. Forget everything else. Keep hold of this alone … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 3.10 |  |
| 351 | Our inward power, when it obeys nature, reacts to … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 4.1 |  |
| 359 | Or is it your reputation that’s bothering you? But … | verbatim | 4.3 | Book 4 |
| 361 | So keep this refuge in mind: the back roads … | verbatim | 4.3 | Book 4 |
| 363 | i. That things have no hold on the soul. … | verbatim | 4.3 | Book 4 |
| 366 | "The world is nothing but change. Our life is … | verbatim once Rufus's additions are removed; Rufus added: quotation marks, bracketed source | 4.3 | Book 4 |
| 374 | You have functioned as a part of something; you … | verbatim | 4.14 | Book 4 |
| 376 | Or be restored, rather. To the logos from which … | verbatim | 4.14 | Book 4 |
| 380 | Many lumps of incense on the same altar. One … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 4.15 | Book 4 |
| 388 | People who are excited by posthumous fame forget that … | verbatim | 4.19 | Book 4 |
| 390 | But suppose that those who remembered you were immortal … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 4.19 | Book 4 |
| 394 | Does anything genuinely beautiful need supplementing? No more than … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 4.20 | Book 4 |
| 400 | “If you seek tranquillity, do less.” Or (more accurately) … | verbatim | 4.24 | Book 4 |
| 402 | Because most of what we say and do is … | verbatim | 4.24 | Book 4 |
| 404 | But we need to eliminate unnecessary assumptions as well. … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 4.24 | Book 4 |
| 408 | The age of Vespasian, for example. People doing the … | verbatim | 4.32 | Book 4 |
| 410 | And that life they led is nowhere to be … | verbatim | 4.32 | Book 4 |
| 412 | Or the age of Trajan. The exact same things. … | verbatim | 4.32 | Book 4 |
| 414 | Survey the records of other eras. And see how … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 4.32 | Book 4 |
| 422 | A key point to bear in mind: The value … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 4.32 | Book 4 |
| 428 | Everything fades so quickly, turns into legend, and soon … | verbatim | 4.33 | Book 4 |
| 430 | And those are the ones who shone. The rest—“unknown, … | verbatim | 4.33 | Book 4 |
| 433 | Only this: proper understanding; unselfish action; truthful speech. A … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 4.33 | Book 4 |
| 441 | On the verge of dying and still weighed down, … | verbatim | 4.37 | Book 4 |
| 449 | In your capacity to see it. Stop doing that … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 4.39 | Book 4 |
| 457 | "In short, know this: Human lives are brief and … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 4.48 | Book 4 |
| 463 | 40. The world as a living being—one nature, one … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 4.40 | Book 4, 40 |
| 469 | To pass through this brief life as nature demands. … | verbatim | 4.48 | Book 4 |
| 471 | Like an olive that ripens and falls. | verbatim | 4.48 | Book 4 |
| 473 | Praising its mother, thanking the tree it grew on. | verbatim | 4.48 | Book 4 |
| 475 | 49. To be like the rock that the waves … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 4.49 | Book 4, 49 |
| 481 | "51. Take the shortest route, the one that nature … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 4.51 | Book 4, 51 |
| 489 | Our lifetime is so brief. And to live it … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 4.50 | Book 5 |
| 495 | No nature would do that—bring something about that wasn’t … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 5.8 | Book 5 |
| 501 | 13. I am made up of substance and what … | verbatim | 5.13 | Book 5, 13 |
| 504 | N.B.: Still holds good, even if the world goes … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 5.13 | Book 5 |
| 512 | "ii. Things gravitate toward what they were intended for. | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 5.16 | Book 5 |
| 514 | What things gravitate toward is their goal. | verbatim | 5.16 | Book 5 |
| 516 | A thing’s goal is what benefits it—its good. | verbatim | 5.16 | Book 5 |
| 518 | A rational being’s good is unselfishness. What we were … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 5.16 | Book 5 |
| 524 | 18. Nothing happens to anyone that he can’t endure. … | verbatim once Rufus's additions are removed; Rufus added: quotation marks | 5.18 | Book 5, 18 |
| 530 | What stands in the way becomes the way. | verbatim | 5.20 | Book 5 |
| 536 | 23. Keep in mind how fast things pass by … | verbatim | 5.23 | Book 5, 23 |
| 538 | So it would take an idiot to feel self-importance … | verbatim | 5.23 | Book 5 |
| 540 | 24. Remember: | verbatim | 5.24 | Book 5, 24 |
| 542 | Matter. How tiny your share of it. Time. How … | verbatim | 5.24 | Book 5 |

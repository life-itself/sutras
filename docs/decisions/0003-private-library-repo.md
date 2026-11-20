# Source texts live in a private library repo

Date: 2026-11-20. Decided by Rufus ("we need a library location where we commit the source texts, maybe private, could be sutras-library for now").

**Decision.** Source texts (books, PDFs, EPUBs, saved web pages, raw conversions) are committed to the private repo `life-itself/sutras-library`, checked out beside this one at `~/src/life-itself/sutras-library`, one folder per edition slug. The public repo holds the editions and, for each, a short public note on how it was made.

**Why.** Sources are often whole in-copyright books; they need a durable home that agents can commit to without publishing them. Supplied files (the Thanissaro and Hays EPUBs) had no committed home at all.

**State on the day.** The private repo exists and holds a copy of everything that was in `library/` here, plus the two EPUBs Rufus supplied. `library/` is still in the public repo until the scripts are changed to read from the private checkout (bead under the Site epic). Whole-book PDFs already pushed here remain in this repo's git history until Rufus OKs rewriting it.

**Later.** If Sutras moves under a wider Open Literature home, this becomes that project's library.

# Copy the reference closely before interpreting it

Learned in the design work (bead sutras-m2v.3), 2026-11-21. Rufus, on the live direction A: "the site isn't bad, but it's not great… compared to Emergence it's not nearly as beautiful". A near-copy of Emergence's Red Pine page, built in an hour, was at once far closer to what he wanted than two days of directions. He asked why the earlier rounds missed it.

## Why we missed it

- **The directions were reskins of what we had.** A, B and C were the live reading page (`css/reading.css`) with new tokens: colour, font, an image above the title. They were cheap to apply because they changed so little, and they differed only in colour. The skill warns against "directions extrapolated from existing assets"; we did it anyway, because building on the live system felt responsible.
- **The reference was never measured, only glanced at.** The mood board showed the Red Pine page's first screen: a picture and the word POEM. The beauty is further down. A browser measurement of the whole page took minutes and showed what we had never seen. Every word is slate blue, not black. The title is a 90px wide grotesque over a 90px fine serif, about five times the size of the text. The images are toned in the page's two inks. The Chinese runs down the centre line, and hairlines cross the page.
- **The brief's restraint was read as smallness.** "The text is the design", "quieter than the text" and "Kaikado's restraint" became a 50px title over 20px text, black ink, and raw scans pasted in. Restraint in the references is precision with bold scale, not timidity.
- **Images were placed, not designed.** On Red Pine the picture is toned into the palette and part of the composition. We downscaled scans and set them above the title.
- **The critique compared the options with each other, not with the reference.** "Best of three" became "good", and agents chose A while Rufus was away.

## What to do instead

1. When the human names a reference they love, the first mockup is a near-copy of it: our real content in its layout, scale, colour and image treatment. Measure the reference first in a browser (computed font, size, weight, tracking and colour per text role, the scale ratios, the background, the image treatment), and scroll the whole page. Substitute fonts only where licences force it.
2. Then simplify the copy into a system (here: feature, reading and parallel registers). Do not start from the existing CSS.
3. The critique puts each mockup beside the reference, at the same scroll depth, and asks "how far short of this is it?"
4. The images get the same design work as the type: toning, crop and scale, as part of the layout.
5. No choice of direction is made without the human seeing the options.

Suggested change to the `designing-look-and-feel` skill (in `life-itself/skills`, not edited without Rufus's OK): add "copy the loved reference first, measured" as a step between the mood board and the directions; add "critique against the reference, not against the siblings" to the critique rule; add the browser-measurement script (computed styles per text role) to the research step.

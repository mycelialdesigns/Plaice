# Covers
<img src="/docs/images/covers/clippedcovertop.jpg" alt="A Clipped Cover, Top View" width="256" height="256"> <img src="/docs/images/covers/nubbedcoverbottom.jpg" alt="A Nubbed Cover, Bottom View" width="256" height="256"> 

Clipped and nubbed covers are Plaice components which go one step further from plugs, and add a thin (`.25 HU`) slab of material over the top of a bunch of plugs.
They may be used to conceal or prettify Plaice plates, to create colored patterns, or even as structural reinforcement to "correct" deflection between
two slide-connected plates. 

## Clipped
<img src="/docs/images/covers/clippedcovertop.jpg" alt="A Clipped Cover, Top View" width="256" height="256"> <img src="/docs/images/covers/clippedcoverbottom.jpg" alt="A Clipped Cover, Bottom View" width="256" height="256"> 
## Nubbed
<img src="/docs/images/covers/nubbedcovertop.jpg" alt="A Nubbed Cover, Top View" width="256" height="256"> <img src="/docs/images/covers/nubbedcoverbottom.jpg" alt="A Nubbed Cover, Bottom View" width="256" height="256"> 

## Design
`.25 HU` was picked as the height for covers purely due to a combination of divisibility and clearance concerns while trying to simultaneously
respect the amount of material used. Firstly, since a division of `.5 HU`
already exists naturally in Plaice (see the Units page (TODO: link)), that gives a starting candidate for the cover thickness. However,
there would be several problems with doing so -- in particular, assemblies built out of Plaice components couldn't assume that a 1 HU
gap between components (e.g: a bin inside a cubby) would suffice for clearance, because all of the involved components could have
(and should be allowed to have) covers on them. Consequently, the next nice divisor available is `.25 HU = 1.75mm`. If we're working
with a typical "structural" printing profile, we can assume four `.4mm` perimeters in XY = `1.6mm`, and roughly the same material thickness
for top and bottom solid layers. Since all other candidate divisors are smaller than `1.6mm`, we have to pick `.25 HU` for nice out-of-the-box
slicer behavior. 

Covers also impact other components in the Plaice system, especially when a string of Plaice plates connected by slides is meant to be interrupted
by a different kind of Plaice component with a slide connector. In those cases, it's important to ensure that not only is there enough clearance
for covers to be inserted on adjacent plates, but also to ideally have the result be as visually seamless as possible. (TODO: cite examples!)

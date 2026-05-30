# Clearance Calibration
<img src="/docs/images/clearancecalibration/platefit.webp" alt="Two plates slid together" width="256">

When getting started with Plaice, it's important to understand your 3d printer's accuracy in order
to appropriately calibrate the [clearance multiplier](/docs/design/Clearances.md) to be applied to
components. By doing so, Plaice assemblies will be much easier to construct and/or more structurally
"tight". 

## Ingredients

<img src="/docs/images/clearancecalibration/materials.webp" alt="Required materials" width="256">


- 2 `4 CU x 4 CU` Plates
- 1 `4 CU x 4 CU` Nubbed Cover
- 1 `4 CU x 4 CU` Clipped Cover
- 2 `4 CU` Protruding Tees

## General Guidance

This recipe has multiple different sections, each of which tests the fitment of a pairing of Plaice
components. You should start with an estimated clearance level for your printer in mind based
on experience (if you have used your printer substantially), or to simply start by trying the loosest
possible clearance level and working down from there (so long as you can physically fit components together,
even at a higher clearance level, they'll still be usable in future assemblies involving components
at a smaller level). The intent is that you will iterate these tests, adjusting the chosen clearance
level based upon guidelines given in each test, with some amount of room for individual preferences.

Strictly speaking, when trying to derive a candidate clearance level, it may be advantageous to
_temporarily_ run the tests with smaller-dimensioned components (e.g: `2 CU` instead of values of
`4 CU`) -- however, it's important to understand that these trial runs do not constitute complete
calibration, since e.g: some `2 CU x 2 CU` connector tests may not catch a small rotational skew
which would make a `4 CU x 4 CU` connector test fail.

<img src="/docs/images/clearancecalibration/warpedplate.webp" alt="A warped plate" width="256">

Additionally, you should generally only perform these calibration steps after you've otherwise
optimized the print quality via slicer settings, printer settings, filament drying, temperature
stabilization, etc. If, for example, your plates are coming off the printer warped, it's pointless
to try to pursue clearance calibration before you first fix the warping issue by e.g: eliminating
drafts, adding a brim, making sure that your heatbed provides consistent heating, etc. etc.

<img src="/docs/images/clearancecalibration/connectorprimingone.webp" alt="Clip priming, clip one" width="256"> <img src="/docs/images/clearancecalibration/connectorprimingtwo.webp" alt="Clip priming, a second clip" width="256">

When testing fitment of [clipped and nubbed connectors](/docs/design/ClipInterface.md), be aware
that clipped connectors will be **much tougher** to connect the first time than subsequent
connections, to the point where you will probably want to individually "prime" clipped connectors via
an initial connection to a nubbed connector. A pro-tip for doing this more effectively
in general is to print a `1 CU x 1 CU` footprint [beam](/docs/components/Beams.md) to
use as a "clip priming tool" with the nubbed end, but this is not strictly required
to perform these calibration steps.

Finally, similar priming steps should be performed for [slide connections](/docs/design/SlideInterface.md) — after printing something with
a slide connector, swipe another slide-connector component over each of the protruding and intruding slides a few times. Doing
so ensures that blemishes and surface roughness left behind by any supports get somewhat smoothed out, resulting in a more
accurate finished piece.

## Clipped and Nubbed Covers Onto A Plate
<img src="/docs/images/clearancecalibration/clippedinserted.webp" alt="A clipped cover inserted into a plate" width="256"> <img src="/docs/images/clearancecalibration/nubbedinserted.webp" alt="A nubbed cover inserted into a plate" width="256">

Take one of the two plates and the clipped cover, and try inserting the clipped connectors fully into
the [sockets](/docs/design/Sockets.md) of the plate. Verify that the top of the cover sits flush with the surface of the plate,
and that the process of insertion is easy enough for something that you'd be willing to do a lot. Perform the same verification steps
with the nubbed cover.

<img src="/docs/images/clearancecalibration/coverfit.webp" alt="A cover, flush with the plate" width="256"> 

## Clipped and Nubbed Covers Sandwiching A Plate
<img src="/docs/images/clearancecalibration/coversfit.webp" alt="Covers snapped through a plate" width="256"> 

Take a plate and push a clipped cover into it just like in the previous test, and from there, snap a nubbed cover
onto the clips which are now embedded in the plate's sockets. You may need to apply pressure at different
parts of the plate, bit by bit to fully secure the two covers. Verify that both covers are flush with the surfaces of the plate.

## Plate Sliding Test
<img src="/docs/images/clearancecalibration/platefit.webp" alt="Two plates slid together" width="256"> 

Take both plates and test all four slide connectors of each by sliding the other plate on. Hold just one
of the plates vertical, and verify that the unsupported plate doesn't slide off. Also verify that the resistance
during assembly is low enough for something that you'd be willing to do a lot.

## Tee Sliding Test
<img src="/docs/images/clearancecalibration/teefit.webp" alt="Two tees slid together" width="256"> 

Take both tees and perform the exact same kind of test as the one you performed for plates. However, don't
worry too much if the tees slide off of each other -- since printers tend to be more accurate in XY anyway,
the plate test is more critical for determining the clearance level, and so this test simply provides
an additional diagnostic.

## Plate-Tee Sliding Test
<img src="/docs/images/clearancecalibration/teeplatefit.webp" alt="A plate and a tee slid together" width="256"> 

Similar to the above two tests, but with a plate and a tee, and the plate unsupported. Unlike the previous test,
this test _is_ more critical for determining the clearance level, since it helps ensure fitment between slides
which are printed in different orientations. Additionally, using this test and the two previous ones, you can
get a rough idea of what your printer's error profile looks like for slides printed in different orientations,
which can in turn help with manually tuning CAD parameters (advanced users), or filing issues and/or asking
questions related to slide fitment with an appropriate level of detail. 

## Cover-Tee Test
<img src="/docs/images/clearancecalibration/teeoncoverstep1.webp" alt="Preparation" width="256"> <img src="/docs/images/clearancecalibration/teeoncoverstep2.webp" alt="A clipped cover partially inserted into a tee's stub sockets" width="256"> 

Take a clipped cover and a tee, and verify that four of the clipped connectors can be fully inserted into the stub sockets of the tee, with
the placement resulting in a flush alignment. A loose fit is perfectly fine here.



## ...Finished!


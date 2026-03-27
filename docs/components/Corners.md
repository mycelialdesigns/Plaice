# Corners

<img src="/docs/images/corner/corner.jpg" alt="A Corner" width="256" height="256"> <img src="/docs/images/corner/cornerback.jpg" alt="A Corner, Back View" width="256" height="256">

A Plaice corner connects two Plaice [plates](/doc/components/Plates.md) at a right angle with a paired set of intruding and protruding [slides](/doc/design/SlideInterface.md). In that respect,
it is analogous to [crosses and tees](/doc/components/CrossesAndTees.md), but for just two plates. Similarly, using a corner or using one of a cross or a tee
to orient two plates at identical right angles will result in identical placement (center of the next plate is `1.5 HU` from the logical
cell boundary of the first plate.)

Unlike crosses and tees, corners have a chamfer on their exterior, which is `.75 HU` in length. This length is chosen to match the chamfer
on the inner portion of the corner, both for aesthetic purposes and because it is the longest possible chamfer length which is both
still a multiple of `.25 HU` (the smallest employed by the system), and leaves at least _some_ completely horizonta overlap with [stacking lips](/doc/components/StackingLips.md). 

## Printability modification

<img src="/docs/images/corner/cornerprintability.webp" alt="A Corner, just after printing" width="256" height="256">

Corners have a printability modification for especially long corner connectors to help stabilize them from toppling
over on the build plate, consisting simply of a partial brim around the exterior of the corner.

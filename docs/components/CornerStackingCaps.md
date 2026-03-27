# Corner Stacking Caps

<img src="/docs/images/thickcornerstackinglip/thickcornerstackinglip.jpg" alt="A Corner Stacking Cap, Thick Variant" width="256" height="256"> <img src="/docs/images/thincornerstackinglip/thincornerstackinglip.jpg" alt="A Corner Stacking Cap, Thin Variant" width="256" height="256"> 

Plaice corner stacking caps perform an analogous function to [corner caps](/docs/components/CornerCaps.md) in Plaice, but for the top corners of open-top boxes.
Both designs for corner stacking caps allow stacking other Plaice boxes of identical footprint on top, but differing in
their suitability for boxes based on size.

## "Thin" Variant
<img src="/docs/images/thincornerstackinglip/thincornerstackinglip.jpg" alt="A Corner Stacking Cap, Thin Variant" width="256" height="256"> <img src="/docs/images/thincornerstackinglip/thincornerstackinglipbottom.jpg" alt="A Corner Stacking Cap, Thin Variant, Bottom View" width="256" height="256"> 

For small boxes, the "thin" variant effectively just continues a [stacking lip](/docs/components/StackingLips.md) around the corner of a box, and as a result,
it is unsuitable for large boxes or large deformations. 

## "Thick" Variant
<img src="/docs/images/thickcornerstackinglip/thickcornerstackinglip.jpg" alt="A Corner Stacking Cap, Thick Variant" width="256" height="256"> <img src="/docs/images/thickcornerstackinglip/thickcornerstackinglipbottom.jpg" alt="A Corner Stacking Cap, Thick Variant, Bottom View" width="256" height="256">

For larger boxes or more weight, the "thick" variant instead adds a platform spanning the corner which has a stub [socket](/docs/components/Sockets.md) on it.
The stub socket is intended to be used with [stacking pegs](/docs/components/StackingPeg.md) as feet for any boxes above it, since the stub
socket provides a stable, predictable place for the corners of large or heavy boxes to seat. The support for the platform
is fairly bulky for the sake of strength, but does taper towards a single cover's thickness at the bottom. Overall, the platform
is [`1 CU`](/docs/design/Units.md) in height, and should be assumed to take up an entire `1 CU x 1 CU x 1 CU` block for the sake of assemblies.

## Printing Tips
<img src="/docs/images/thincornerstackinglip/thincornerstackinglipsupports.webp" alt="A Corner Stacking Cap, Thin Variant, just after printing" width="256" height="256"> <img src="/docs/images/thickcornerstackinglip/thickcornerstackinglipsupports.webp" alt="A Corner Stacking Cap, Thick Variant, just after printing" width="256" height="256">

Print both variants with supports for the sake of the bottom flats of the stub slides.

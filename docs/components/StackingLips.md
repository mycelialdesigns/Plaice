# Stacking Lips

<img src="/docs/images/stackinglips.jpg" alt="Stacking Lips, Intruding and Protruding" width="256" height="256">

A Plaice stacking lip is a terminal [slide](/docs/design/SlideInterface.md) which can be used to terminate a slide (here assumed to be directed vertically)
with geometry which mates nicely with the chamfered geometry of [corners](/docs/components/Corners.md).

Stacking lips may be used to construct stackable boxes out of Plaice components, but they are not generally suitable
for large stacking boxes by themselves, since the deflection of Plaice [plates](/docs/components/Plates.md) making up the walls may be too high
for stacked boxes to seat properly. Consequently, for larger boxes, it is recommended to use the "thick" variant
of [corner stacking caps](/docs/components/CornerStackingCaps.md) to ensure that at least the corners of boxes are always supported.

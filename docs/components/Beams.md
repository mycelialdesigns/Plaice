# Beams

<img src="/docs/images/beams/keyaccessbeambottom.jpg" alt="A Key-Access Beam, Bottom View" width="256" height="256"> <img src="/docs/images/beams/thrubeambottom.jpg" alt="A Thru Beam, Bottom View" width="256" height="256">

Plaice beams are components which are commonly used as "legs" or "columns" of free-standing shelves.
They consist of a [`1 CU x 1 CU`](/docs/design/Units.md) base with a [clipped connector](/docs/design/ClipInterface.md)
embedded in a [socket](/docs/design/Sockets.md) and an optionally-tapered top which
can be `1 CU x 1 CU` (not tapered), `1 CU x 2 CU` (tapered along one direction), or `2 CU x 2 CU` (tapered along both
directions), and has nubbed connectors on top.

Tapered beams are largely helpful for minimizing deflection of [plates](/docs/components/Plates.md) mounted on top of them due
to the increased moment the taper gives against plate deflection. Their tapers are `.75 HU` in height
to ensure that `1 HU` of clearance in an assembly is enough to accomodate e.g: a cover on top of a plate
which is `1 HU` below the plate atop the beam. Just before the nubbed connectors, the taper also has
a `.25 HU` pad to provide visual seamlessness with any [nubbed covers](/docs/components/Covers.md) mounted to the bottom side
of the top plate. 

## M2 Bolt Integration Variants

Beams have a similar challenge to [thru-nubs](/docs/components/ThruNub.md) in that at least one of their nubbed connectors
doesn't have immediately apparent access to its "back side". However, for long beams, a similar solution would not apply.
Consequently, in Plaice, there are two different beam variants:

### Thru-Beams
<img src="/docs/images/beams/thrubeam.jpg" alt="A Thru Beam, Bottom View" width="256" height="256"> <img src="/docs/images/beams/thrubeambottom.jpg" alt="A Thru Beam, Bottom View" width="256" height="256">

When the desired length of beam is short enough that standard-issue M2 bolts can easily pass through the whole length and interface with
other components in a Plaice assembly, you might consider using a thru-beam. Generally speaking, that means lengths of
`6 HU` and lower.

### Hex-Key-Access-Beams

<img src="/docs/images/beams/keyaccessbeam.jpg" alt="A Key-Access Beam" width="256" height="256"> <img src="/docs/images/beams/keyaccessbeambottom.jpg" alt="A Key-Access Beam, Bottom View" width="256" height="256"> 

Hex-key access bolted beams carve a channel along the interior corner of the beam length which allows both
a M2 bolt and an M2 hex key to be inserted into the channel, and the M2 hex key to be turned at 75 degree
increments to eventually tighten or loosen a bolt. Unlike the other solutions, this type of beam
allows for large lengths, but also requires a beam which is at least `5 HU` in length.

## Printing Tips

<img src="/docs/images/beams/keyaccessbeamsupports.webp" alt="A Key-Access Beam, Printed With Supports" width="256" height="256"> <img src="/docs/images/beams/keyaccessbeamsupportsbottom.webp" alt="A Key-Access Beam, Printed With Supports, Bottom View" width="256" height="256">

As is the case with all other Plaice components with sensitive geometry on both sides of any hypothetical print orientation along Z, when printing a beam, the nubbed connectors should be oriented downwards,
so that their printability modification can be applied. Additionally, since the top of the beam (bottom in print orientation) has a flat of cell-unit-multiple sizing, support structures should be added to
support that flat at the bottom of the print. None of the other surfaces on the underside of the print, like the nubbed connectors or their chamfers, should have generated supports -- it wastes filament, time, and just makes them more difficult to remove.

That said, the M2 nut channel near the top of the print should not need any supports, so feel free to add support blocking modifiers there. Finally, in the
case of the hex-key-access bolted beam, supports should be generated for the void where the hex key is inserted. 

<img src="/docs/images/beams/beamsupportremovalstep1.webp" alt="Beam Bottom Support Removal, Step 1" width="256" height="256">

When removing supports from the bottom, first remove the slicer-generated support structures and the mouse-ears on the nubs to yield something like the picture above.
Then, break the bridges between the nubbed connectors' central islands using a needle-nosed pliers.

<img src="/docs/images/beams/beamsupoprtremovalstep2.webp" alt="Beam Bottom Support Removal, Step 2" width="256" height="256"> <img src="/docs/images/beams/beamsupportremovalstep3.webp" alt="Beam Bottom Support Removal, Step 3" width="256" height="256">

From this state, removal of the key access-slot supports and a poke through the corner hole with a screwdriver or Allen key will result in something that looks like the pictures at the top of this article.

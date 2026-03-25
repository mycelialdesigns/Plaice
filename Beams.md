# Beams

<img src="/docs/images/beams/thruaccessbeam.jpg" alt="A Thru-Access Beam" width="256" height="256"> <img src="/docs/images/beams/keyaccessbeambottom.jpg" alt="A Key-Access Beam, Bottom View" width="256" height="256"> <img src="/docs/images/beams/thrubeambottom.jpg" alt="A Thru Beam, Bottom View" width="256" height="256">

Plaice beams are components which are commonly used as "legs" or "columns" of free-standing shelves.
They consist of a `1 CU x 1 CU` base with a clip embedded in a socket and an optionally-tapered top which
can be `1 CU x 1 CU` (not tapered), `1 CU x 2 CU` (tapered along one direction), or `2 CU x 2 CU` (tapered along both
directions), and has nubbed connectors on top.

Tapered beams are largely helpful for minimizing deflection of plates mounted on top of them due
to the increased moment the taper gives against plate deflection. Their tapers are `.75 HU` in height
to ensure that `1 HU` of clearance in an assembly is enough to accomodate e.g: a cover on top of a plate
which is `1 HU` below the plate atop the beam. Just before the nubbed connectors, the taper also has
a `.25 HU` pad to provide visual seamlessness with any nubbed covers mounted to the bottom side
of the top plate. 

## M2 Bolt Integration Variants

Given that beams have a similar challenge to thru-nubs in that at least one of their nubbed connectors
doesn't have immediately apparent access to its "back side", a similar solution (just putting a hole
for M2 bolts to pass through) would seem to work, at least in some situations. (That variant
of a beam is called a "thru beam")


<img src="/docs/images/beams/thrubeam.jpg" alt="A Thru Beam, Bottom View" width="256" height="256"> <img src="/docs/images/beams/thrubeambottom.jpg" alt="A Thru Beam, Bottom View" width="256" height="256">

However, beams can be fairly long, and it's pretty hard to find (or even to want) 
excessively long M2 bolts. Consequently, there are two more beam variants which try to
give access to the head of an inserted M2 bolt in two different ways.

### Thru-access bolted beams

<img src="/docs/images/beams/thruaccessbeam.jpg" alt="A Thru-Access Beam" width="256" height="256"> <img src="/docs/images/beams/thruaccessbeamside.jpg" alt="A Thru-Access Beam, Side View" width="256" height="256">

So-called "thru-access" bolted beams depend upon being able to drop in a M2 bolt down
a central channel _and tightening it_ before inserting a M2 nut into the nut channel during assembly,
and reversing these steps during disassembly. While this does solve the length problem for bolts,
it makes the problem reappear somewhat in the length of M2 hex keys required to access the bolt head.
It's somewhat annoying for the required order-of-operations, and also slightly erodes the structural
integrity of connections to the captive nut, because the contacting surface area had to be reduced
to accommodate a drop-in bolt channel.

### Hex key access bolted beams

<img src="/docs/images/beams/keyaccessbeam.jpg" alt="A Key-Access Beam" width="256" height="256"> <img src="/docs/images/beams/keyaccessbeambottom.jpg" alt="A Key-Access Beam, Bottom View" width="256" height="256"> 

Hex-key access bolted beams carve a channel along the interior corner of the beam length which allows both
a M2 bolt and an M2 hex key to be inserted into the channel, and the M2 hex key to be turned at 75 degree
increments to eventually tighten or loosen a bolt. Unlike the other solutions, this type of beam
allows for large lengths, but also pretty much _requires_ a beam which is longer than an M2 hex key.

## Printing Tips

<img src="/docs/images/beams/beambottomprintable.webp" alt="Thru-beam right after printing" width="256" height="256"> <img src="/docs/images/beams/taperedbeambottomsupports.webp" alt="Tapered beam right after printing" width="256" height="256">

As is the case with all other Plaice components with sensitive geometry on both sides of any hypothetical print orientation along Z, when printing a beam, the nubbed connectors should be oriented downwards,
so that their printability modification can be applied. Additionally, since the top of the beam (bottom in print orientation) has a flat of cell-unit-multiple sizing, support structures should be added to
support that flat at the bottom of the print. None of the other surfaces on the underside of the print, like the nubbed connectors or their chamfers, should have generated supports -- it wastes filament, time, and just makes them more difficult to remove.

<img src="/docs/images/beams/keyaccessbeamsupports.webp" alt="Key-access beam after printing" width="256" height="256"> <img src="/docs/images/beams/keyaccessbeambottomsupports.webp" alt="Key-access beam after printing, bottom view" width="256" height="256">

That said, the M2 nut channel near the top of the print should not need any supports, so feel free to add support blocking modifiers there. Finally, in the special
case of the hex-key-access bolted beam, supports should be generated for the void where the hex key is inserted. 

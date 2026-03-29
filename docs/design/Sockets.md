# Sockets

<img src="/docs/images/plaicesocket.png" alt="A Plaice Socket" height="256"><img src="/docs/images/plaicesocketside.png" alt="A Plaice Socket, Side View (See-Thru)" height="256">

Plaice _Sockets_ are chamfered rounded-square voids which allow the insertion of Plaice [clipped and nubbed connectors](/docs/design/ClipInterface.md).
They have a total depth of `7 mm` ([`1 HU`](/docs/design/Units.md)), with `2 x 1.5 mm` devoted to 45-degree chamfered sections, and with the remaining `4 mm` consisting of
a rounded `10 mm` square with a corner fillet radius of `1.6 mm`. 

## Manufacturability

Sockets are explicitly designed to be manufacturable via subtractive manufacturing (routing), which is the reason for the corner fillets, but also, the particular
way that the socket is chamfered. The radius of the corner fillet does not change along the chamfer, which allows the fillet to be cut more cleanly
and efficiently by a single straight bit than if a changing fillet radius were used. The radius of the fillet is set so that a 1/8" diameter routing bit (US units)
could be used to cut sockets, and the chamfer having a length smaller than the fillet radius also means that the chamfer can _also_ be cut smoothly using a 90-degree
V-carve bit, if desired.

Additionally, the chamfer length's value of `1.5 mm` has direct implications for laser cutting, since `1.5 mm` wood veneers are not terribly hard to come by. While 3d printing
is still necessary in such a set-up to provide inserts for the chamfers, the dimensioning makes the approach at least viable. 

## Structural considerations

Intuitively, since a Plaice [plate](/docs/components/Plates.md) is just a slab (with [slides](/docs/design/SlideInterface.md)) with sockets cut out of it, it would make sense that the plate's strength would heavily depend
on the socket dimensions, and this is indeed the case. Roughly speaking, the deflection of a Plaice plate with sockets is two times what the deflection of
what a solid plate would experience under a one-sided load, and around the de facto socket dimensions, FEM verifies that the deflection is roughly linear
in the socket width. Consequently, Plaice sockets are set to the smallest dimensions that they possibly can be while still maintaining the functionality
of socket connectors. 

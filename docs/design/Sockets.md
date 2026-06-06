# Sockets

<img src="/docs/images/plaicesocket.png" alt="A Plaice Socket" height="256"><img src="/docs/images/plaicesocketside.png" alt="A Plaice Socket, Side View (See-Thru)" height="256">

Plaice _Sockets_ are chamfered rounded-square voids which allow the insertion of Plaice [clipped and nubbed connectors](/docs/design/ClipInterface.md).
They have a [`1 HU`](/docs/design/Units.md) depth, with `2 x 1.5 mm` devoted to 45-degree chamfered sections. The remaining `4 mm` consists of
a rounded `10 mm` square with a corner fillet (radius of `1.6 mm`). 

## Strength and Deflection

Intuitively, since a Plaice [plate](/docs/components/Plates.md) is a slab with sockets cut out of it, the plate's strength heavily depends
on the socket dimensions. The deflection of a Plaice plate with sockets is roughly two times what the deflection of
what a solid plate would experience under a one-sided load, and around the de facto socket dimensions, FEM verifies that the deflection is roughly linear
in the socket width. Consequently, Plaice sockets are the smallest dimensions that they can be while maintaining the functionality
of socket connectors. 


## Manufacturability

Sockets are explicitly designed to be manufacturable via subtractive manufacturing (routing). This is the reason for the corner fillets, as well as the particular
way that the socket is chamfered. The radius of the corner fillet does not change along the chamfer, which allows the fillet to be cut more cleanly
and efficiently by a single straight bit than if a changing fillet radius were used. The radius of the fillet is set so that a 1/8" diameter routing bit (US units)
could be used to cut sockets. The chamfer having a length smaller than the fillet radius also means that the chamfer can _also_ be cut smoothly using a 90-degree
V-carve bit, if desired.

Furthermore, the chamfer length's value of `1.5 mm` has direct implications for laser cutting, since `1.5 mm` wood veneers are not difficult to come by. While 3d printing
is still necessary in such a set-up to provide inserts for the chamfers, this dimensioning makes the approach viable. 



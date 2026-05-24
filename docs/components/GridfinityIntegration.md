# Gridfinity Integration

<img src="/docs/images/gridfinity/gridfinitybaseplatebolton.webp" alt="A Gridfinity Baseplate Bolt-On" width="256" height="256"> <img src="/docs/images/gridfinity/gridfinitybinbasebolton.webp" alt="A Gridfinity Bin Base Bolt-On" width="256" height="256">

Plaice integrates with [Gridfinity](https://gridfinity.xyz/) bidirectionally, and Plaice assemblies can be treated as Gridfinity bins or as a place to mount Gridfinity baseplates.
Two Plaice [cell units](/docs/design/Units.md) are equivalent to one Gridfinity grid unit, and so the synchronizing length is `42mm`.

## Bolt-On Bin Bases

<img src="/docs/images/gridfinity/gridfinitybinbasebolton.webp" alt="A Gridfinity Bin Base Bolt-On" width="256" height="256"> <img src="/docs/images/gridfinity/gridfinitybinbaseboltontop.webp" alt="A Gridfinity Bin Base Bolt-On, Top View" width="256" height="256">

To use Plaice assemblies as Gridfinity bins, the gridfinity "bin base" is a Plaice bolt-on (TODO: link) component consisting of a Gridfinity bin base with pockets and holes for M2
bolts and/or captive M2 nuts. It is meant to be secured to a `2 CU x 2 CU` backing (TODO: link). 

## Bolt-On Baseplates

<img src="/docs/images/gridfinity/gridfinitybaseplatebolton.webp" alt="A Gridfinity Baseplate Bolt-On" width="256" height="256"> <img src="/docs/images/opengrid/opengridbaseplateboltonbottom.webp" alt="A Gridfinity Baseplate Bolt-On, Bottom View" width="256" height="256"> 

To attach Gridfinity baseplates to Plaice plates, the gridfinity "baseplate" is a Plaice bolt-on component (TODO: link) for backings (TODO: link)
of an even length and width in cell units. It has mostly the same geometry as an official Gridfinity baseplate, but with pockets and holes to allow
it to be a bolt-on component, and a different size for inserted magnets. To accommodate the required positioning of holes for Plaice bolt-ons,
the magnet pockets had to be reduced in size to accommodate `4 mm` diameter by `1 mm` height magnets instead of the more typical `6 mm` diameter
by `2 mm` height magnets employed in Gridfinity. Just like in Gridfinity, magnets may be secured with cyanoacrylate glue or similar.

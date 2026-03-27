# Gridfinity Integration

<img src="/docs/images/gridfinity/gridfinitybaseplate.jpg" alt="A Gridfinity Baseplate Glue-on" width="256" height="256"> <img src="/docs/images/gridfinity/gridfinitymountbottom.jpg" alt="A Gridfinity Mount, Bottom View" width="256" height="256">

Plaice integrates with Gridfinity bidirectionally, and Plaice assemblies can be treated as Gridfinity bins or as a place to mount Gridfinity baseplates.
Two Plaice [cell units](/docs/design/Units.md) are equivalent to one Gridfinity grid unit, and so the synchronizing length is `42mm`.

## Mounts
<img src="/docs/images/gridfinity/gridfinitymountbottom.jpg" alt="A Gridfinity Mount, Bottom View" width="256" height="256"> <img src="/docs/images/gridfinity/gridfinitymounttop.jpg" alt="A Gridfinity Mount, Top View" width="256" height="256">

To use Plaice assemblies as Gridfinity bins, the gridfinity "mount" is a Plaice component consisting of a Gridfinity bin base
fused to a pad with [nubbed connectors](/docs/design/ClipInterface.md).

## Baseplates
<img src="/docs/images/gridfinity/gridfinitybaseplate.jpg" alt="A Gridfinity Baseplate Glue-on" width="256" height="256">

To attach Gridfinity baseplates to Plaice plates, the gridfinity "baseplate" is a [glue-on component](/docs/design/GlueTogetherComponents.md) for Plaice [clipped covers](/docs/components/Covers.md)
of an even length and width in cell units. 

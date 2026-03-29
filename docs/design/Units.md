# Plaice Units

Any modular constuction system is faced with the fundamental problem of defining how the system
will sit in 3d space, and Plaice is no exception. Systems like [Ikea SKADIS](https://www.ikea.com/us/en/cat/skadis-series-37813/), 
[HSW](https://www.printables.com/model/152592-honeycomb-storage-wall), and [OpenGrid](https://www.opengrid.world/) are
fundamentally two-dimensional mounting systems, which is a sub-system of Plaice, but the system
overall has more similarities with three-dimensional grid-based systems like [Gridfinity](https://gridfinity.xyz/) and `8 mm`
stud systems ([MegaBloks](https://themegabloks.com/), [LEGO](https://www.lego.com/). 
Unlike those systems, Plaice [plates](/docs/components/Plates.md) may occur oriented parallel
to any axis-aligned plane -- there is no "preferred" orientation for components of the system
(like how Gridfinity bins are always oriented "right-side-up"), even if there is a direction
(Z) which goes with gravity. While we could explain the dimensional unit system from an absolute
frame of reference (with plenty of reference to "quarter height-units" and rotational symmetries),
it's in practice much simpler to examine frames of reference taken relative to the orientation
of a Plaice plate that we intend to focus on. By convention, we take the [socket](/docs/design/Sockets.md) grid
to align with the XY plane when considering this plate-relative reference frame.

## Grid Units

Along the XY plane, a Plaice plate is made of repeating square units known as _cells_. Each cell has a socket
placed squarely in the middle, and when projected onto the XY plane, each cell measures `21 mm x 21 mm`. Due to the centrality
of Plaice plates to the system, a length of 21mm is known as a **Cell Unit** (CU). Plaice plates are typically denoted by their
width and length in cell units, e.g: `2 x 4`, `4 x 4`, `8 x 8`, etc.

### Implications for Integrations

The size of a unit cell has massive implications for how easy or difficult it is to integrate
Plaice with other modular construction systems in a bidirectional manner. In particular, the `21 mm` "Cell Unit" length was chosen
for ease of integrating with [Gridfinity](/docs/components/GridfinityIntegration.md) (1:2 ratio in each side length for a unit cell)
and [OpenGrid](/docs/components/OpenGridIntegration.md) (4:3 ratio to match exactly when tiled), as these are two of the most widely-used 3d-printed modular construction systems.
In general, if two systems have unit cells of lengths `a` and `b` (in millimeters, whole numbers, no fractions), then
the total length it takes for the two systems to "sync up" at a shared unit-cell boundary is given by their least-common-multiple, `lcm(a, b)`. 

Such synchronization (within a reasonable (read: printable!) length) is arguably a _requirement_ for a good bidirectional integration
because it takes any guesswork out of the relative alignment of the two systems in play. However, if we consider instead _unidiectional_
integations, where conceptually, one system is used "in the large" and the other is used "in the small" (e.g: the user primarily uses system A,
but there are tiny pockets of their constuction where it makes sense to adapt locally to system B), there is no longer any such
requirement for strict synchronization, because portions that use the "smaller" system can simply give up some margin to be able to synchronize with system A again.
Such a strategy could be used to integrate Plaice as the "smaller" system relative to [Multiboard](https://multibuild.io/) and other systems for which
bidirectional integrations would be unwieldy, but at the time of writing, no such unidirectional integrations have been implemented.

## Height Units

Along the Z axis, a Plaice plate is `7 mm` thick. A length of `7 mm` is known as a **Height Unit** (HU), and it also appears frequently in Plaice
definitions. This value is identical to a Gridfinity "height unit", though largely by coincidence. From divisibility principles mentioned in the previous section,
and due to the potentially-arbitrary orientation of Plaice plates in space, the thickness of a Plaice plate should evenly divide a grid unit. 21=7*3, and 3mm
is far too thin, so 7mm it is. 

One extra benefit of a choice of a `7 mm` height unit is that `3 HU = 1 CU`, which is exploited constantly in the design of Plaice components, since a plate placed on its side standing in the (lateral) "center" of a cell
then has exactly 1HU on each side of it as margin to the adjacent cells on the baseplate. For examples, see [corners](/docs/components/Corners.md),
[crosses and tees](/docs/components/CrossesAndTees.md), and [slide clips](/docs/components/SlideClips.md). 

## Fractional Units

If you read between the lines of the previous section and the symmetries of Plaice [slides](/docs/design/SlideInterface.md), you can deduce that
half of a height unit is an occasionally important quantity when discussing Plaice. Beyond that, a smaller fraction of a height unit, `.25 HU`,
is employed for Plaice [covers](/docs/components/Covers.md).

## Base-2 Radix

To minimize the effects of tolerance stack-up and cumulative deflection, Plaice plates typically are only made with power-of-two grid-unit widths and lengths.
Any length and width of composite plate may be obtained by sliding Plaice plates together and optionally stabilising them against deflection using paired covers,
and be obtained with a number of Plaice plates which is asymptotically logarithmic in the demanded dimensions. 

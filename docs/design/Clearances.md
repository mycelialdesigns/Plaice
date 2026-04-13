# Clearances
Designing Plaice components to fit together requires careful attention to the nominal clearances between components.

## Preliminary Definitions
Clearances describe the size of gaps between two surfaces, and so it's important to have a clear reference to what the surfaces
involved are. In our case, there are actually three different sources for relevant geometry to reference: "*interface*" geometry
which consists of 2d profiles in CAD expressing an idealized meeting-curve of two components, "*model*" component geometry which
represents the geometry expressed in 3d CAD and/or in exported .stl files, and "*de facto*" geometry which is the physical geometry
of real components after printing. 

## Print Bias Correction Clearances
Due to artifacts of the 3d printing process, de facto geometry will never exactly match model geometry. However, we have control
over the model geometry, which means that if we have systematic biases in how de facto geometry deviates from how we want it
to be, we can simply adjust the model geometry to compensate for those biases as best we can. The de facto geometry as we'd like it to
be is what we call *idealized* geometry, and it's essentially what we would get if we had a 3d printer with no printing artifacts whatsoever
and a layer height approaching zero (+ perfectly smooth). 

Consequently, our approach to creating modeling geometry can be kicked off by starting with the idealized geometry, and then introducing small tweaks
to the model geometry to correct for differences from the ideal which would occur when turned into de facto geometry via printing. These small tweaks
are all in the form of clearances applied between the idealized geometry and the modeling geometry at different locations throughout the model, and
so we call them *print correction clearances*. It's important to note that these clearances are meant to be somewhat of a statistical average of the
clearance biases that they're meant to correct for across _all_ printed Plaice components, which says nothing of the variation, but we can simply
lump that in with other factors which determine our overall manufacturing tolerances.

### XY Hole Shrinkage Clearance
When a 3d printer prints a circular arc in the XY plane, it deposits hot plastic centered along the arc which briefly
flows, then cools and hardens. Consider a simple model of this where the nozzle deposits plastic which falls in a region
bounded in XY by offsets of the arc, padded to the printing layer height. Also suppose that the volume of plastic deposited
on either side of the "nominal" arc that the nozzle follows is equal. Then, a direct consequence of these assumptions is that
the offset for the "interior" arc (smaller diameter) must be _larger_ than the offset for the "exterior" arc (larger diameter).

In other words, 3d-printed holes shrink along XY, with smaller 3d-printed holes systematically shrinking more than larger ones, and more
generally, any concave geometry along XY will expand inwards, with the amount of expansion dependent on curvature. While this effect
is not describable purely by a constant offset for _all_ radii of curvature, in practice, in Plaice, the curvatures of surfaces which
need an XY hole shrinkage clearance applied (mostly just slides) are all pretty similar. We call the clearance value which issues
this modification to the design geometry over the idealized geometry the _XY Hole Shrinkage Clearance_. 

### Z Overhang Depression Clearance
The overall process of 3d printing introduces some systematic errors which can make overhanging geometry depress along the Z axis toward the
build plate, both from physical causes and from the way that slicers interpret 3d designs. 

The single biggest physical cause has to do with
the fact that molten plastic will fall _down_ under the influence of gravity, and overhangs will tend to do the same unless cooled rapidly.
The same is true for _supported_ overhangs, because the support isn't completely solid, and may introduce bottom-surface roughness on removal.

To make matters worse, slicers determine what belongs on each layer "slice" of a model by intersecting the model with abstract planes which
are set to the height of the _top_ of the layer, not the middle, meaning that the effects of the semi-quantization induced by slicing will
cause overhanging geometry to shift _downwards_ by about half of a layer-height on average.

We cannot hope to model both factors exactly, but we can compensate by adding a clearance to "push up" any overhangs in the designs. We
call this applied clearance between the idealized and design geometry the _Z Overhang Depression Clearance_.

## The Clearance Multiplier
Print bias correction clearances aren't the only clearances we need to care about in the process of preparing Plaice components for printing.
Every 3d printer has its own quirks, and even when fully calibrated and printing geometry which corrects systematic printer biases,
individual 3d printers will still exhibit small variations in their output from print-to-print. 
Plaice components are designed to be printable by most 3d printers, and consequently, it's important that
we have some kind of mechanism for accommodating these dimensional variations. We do this by introducing additional clearances between mating parts
in a systematic way dependent upon how the parts are meant to mate. 

Plaice components like plates are highly dependent upon tight de facto clearances to minimize deflection in assemblies.
Simply choosing _one_ set of clearances intended for all printers would require us to select the _largest_ such clearance, which is
therefore unacceptable for our use-case. To resolve this problem, Plaice has a global _clearance multiplier_ which multiplies all non-print-bias-correcting
clearance values applied to design geometry. This multiplier is meant to be interpreted as approximately bounded below
by `1.0` (something intended for printers in the top 1% of print quality) and above by `2.0` (something which works for ~95% of all printers in the wild,
though it may wind up being a loose fit). 

## Clearance Levels
For .stl export of Plaice components, having a continuum of possible clearance multiplier values is untenable. To resolve this problem, we instead define
three clearance _levels_ for different values of the clearance multiplier, termed _Tight_ for `1.0`, _Standard_ for `1.5`, and _Loose_ for `2.0`. 

## Clearance Types
The "base" or "fundamental" clearance values which the clearance multiplier multiplies are assigned based on the intent behind mating geometry,
which falls into a small number of discrete categories we call "Clearance Types".

### Contact Fit Clearance
Applied to parts which are meant to assemble and _contact_ each other without substantial movement. Applicable to mating surface pairs where
assembly involves moving the surfaces toward each other, but also to mating surface pairs where the mating surface patches are small and/or compliant.
This is the tightest clearance type.

### Snug Slide Fit Clearance
Applied to mating surface pairs which have substantial contact surface area, and are meant to "slide" against each other, but only during
assembly.

### Smooth Slide Fit Clearance
Applied to mating surface pairs which have substantial contact surface area, but where the sliding between parts is meant to occur frequently
after assembly. This is the loosest clearance type.

## Tolerances
We mostly talked here about clearances instead of tolerances because most of the relevant tolerances to Plaice are actually one-sided tolerances
instead of symmetric tolerances. For example, for two [slides](/docs/design/SlideInterface.md) to fit together with _any_ other slides within
tolerance, they must have de facto geometry which never crosses the slide _interface_ which their idealized geometry is offset from. To bound the other side,
for each kind of interface, we do the simplest possible thing and declare that the idealized geometry with the maximum acceptable clearance multiplier is
the other surface defining the outer limit of the one-sided tolerance. 

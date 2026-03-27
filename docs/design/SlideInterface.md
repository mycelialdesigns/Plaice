# Slide Interface
<img src="/docs/images/slideinterface/slideinterface.png" alt="Slide Interface" width="512" height="512">

Slide connections allow Plaice components to join in a way which effectively leaves only one degree of freedom unconstrained.
The curve ("profile") projected on the plane normal to that degree of freedom which is sandwiched between an idealized
"perfect" protruding and intruding slide is known as the _slide interface_.

## Geometry

The Plaice slide interface profile draws on inspiration from jigsaw puzzle pieces and woodworking dovetails, but with a
shape optimized for strength. In particular, the slides are designed so that when they are used to connect
two Plaice plates along a span which is supported at both ends, the slides will not break, even when a heavy weight is applied.

By itself, the above paragraph does not completely constrain the interface profile, but when combined with the following other requirements:
- Leave at least `0.8 mm` (two perimeters with a `0.4 mm` nozzle) of material between a plate's socket-chamfer and the closest point on the slide profile. 
- Use only simple geometric primitives (arcs and line segments)
- Ensure that all arcs have greater than some minimum diameter (`0.8 mm`) to ensure a baseline level of smoothness in real prints.
- Even under the largest clearance between slides employed by Plaice, the two halves of a slide do not separate without substantial force.

... the shape becomes a bit more explainable, albeit still fairly underspecified. To put the shape of the interface into sharper focus,
we'll need to explain what kinds of geometric symmetries are desirable in this setting.

### Symmetries

There are two major symmetries which apply to the slide interface, and both are different kinds of mirror symmetry, but
with differing motivations.

#### Ease of Assembly: Vertical Flip Symmetry

When putting two Plaice plates together with slides, assuming that a protruding and intruding slide are properly paired, the two plates
should fit together without needing to adjust their orientations. By ensuring that plates don't need to e.g: occasionally
be flipped to match orientations, the cognitive load (and hence, time) involved in putting together a Plaice assembly
can be reduced. For the slide interface profile, this means ensuring a vertical flip symmetry across a central horizontal axis.

#### Asymptotic Strength Under Plate Stacking

<img src="/docs/images/slideinterface/slideinterface-profile-tesselated.svg" alt="Slide Interface, Tessellated" width="512" height="512">

There are plenty of situations where a 7mm thick 3d-printed PLA plates just aren't going to cut it for a given loading regime. 
In those situations, it's reasonable to want to stack plates on top of each other, and somehow secure them to form a larger composite.
In Plaice, this option is readily available through the use of thru-nubs and plugs.

Now, consider what happens when a stack of plates with identical orientations is connected to another stack of plates
using slides -- visually, the result looks something like the picture above.

In order to minimize the maximal stress under an applied load, it is generally a good idea to spread the induced stresses
over the largest possible area. One natural way to do this for the situation of the stacked plates is to attempt to ensure
that each stack should take more or less the same cumulative stress. There isn't really a simple way to apply that
criterion verbatim, but we can do the next best thing: We can ensure that the _roles_ of each stack are the same in relation
to each other.

To do this, all we need to do is to ensure that between every two stacked protrusions, there's an intrusion formed, and
between every two stacked intrusions, there's a protrusion formed. This is another kind of mirror symmetry.

## FEM Optimization

<img src="/docs/images/slideinterface/slideFEM.png" alt="Slide FEM, Heatmap of Maximum Principal Stress" width="512" height="512">

After the constraints mentioned in the previous section have been applied, the final shape of the Plaice slide interface is obtained
by performing hill-climbing on the maximal stress minimization objective (see (TODO: cite FEM source file)). In particular, since the
objective assumes static loading, and PLA is dramatically stronger under compression than under tension, we can apply the Mohr-Coulomb yield
criterion and use the (max of the) maximum principal stress as a proxy for how close to yielding our parts are. 

## Clearances and Manufacturing Notes

Before applying any printer bias corrections, all protruding and intruding slide profiles are curves at uniform offsets
from the slide interface. The clearance for each profile from the interface curve is always half of the intended clearance
between the protruding/intruding profile pair. Generally speaking, Plaice uses only two different values for such
clearances, depending on the intended functionality for the slides: A "snug" slide fit ("slide"), a transition fit which
semantically expresses the ability to slide the two halves together, possibly with some effort, but ideally nothing
which would exceed what is possible with the user's bare hands, and a "smooth" slide fit ("glide"), a clearance fit
which expresses the ability to (almost-) freely move the two halves relative to each other along their degree of freedom.

However, the CAD for the slide profiles is not quite as simple as the previous description, because 3d printers have
systemic biases in how printed parts tend to differ from what appears in CAD, and these biases vary substantially
with print orientation. Along the Z-axis, surface roughness from removed supports, sagging overhangs, and layer quantization
all have an effect on the end result. Along the XY-plane, internal holes tend to be systematically smaller than
in CAD, assuming common default slicer settings. 

While all this sounds (and can be!) complex, the corrections that
Plaice applies to combat them are relatively simple constant-factor ones: an "overhang bias" factor, and a "hole shrinkage" factor.
Generally speaking, slide profiles in Plaice only occur aligned with one of the XY, YZ, or XZ planes, and we can generally
assume that printer biases applied to the YZ and XZ planes will be more or less the same. As a result, we have _two_ different
adjustments to the slide interface:

"slideinterface" (XZ, YZ planes)

(TODO: include annotated pictures!)

"xyslideinterface" (XY plane)

(TODO: include annotated pictures!)

As a direct consequence, the CAD files which make up Plaice have to take print orientation into careful consideration, since
the relevant files to reference for slides will heavily depend on it. While this adds complexity for designers, the corrections
are worthwhile to allow for tighter tolerances (and consequently, less potential deflection between parts in a Plaice assembly.)

When a slide is part of a Plaice component, care must also be taken to ensure that there's enough clearance for a plate connected
via the slide to be able to slide freely, which may require applying clearances to extra surfaces. This happens in (TODO: cite)

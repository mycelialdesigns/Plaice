# Slide Interface
<img src="/docs/images/slideinterface/slideinterface.png" alt="Slide Interface" width="512" height="512">

Slide connections allow Plaice components to join in a way which leaves only one degree of freedom unconstrained. The _slide interface_
is the curve ("profile") projected on the plane normal to the degree of freedom which is sandwiched between an idealized
"perfect" protruding and intruding slide.

## Geometry

The Plaice slide interface profile draws on inspiration from jigsaw puzzle pieces and woodworking dovetails, but with its
shape optimized for strength. It's designed so that when connecting
two Plaice [plates](/docs/components/Plates.md) along a span supported at both ends, the slides will not break when a heavy weight is applied.

By itself, the need for strength does not completely define the interface profile. It becomes a bit more explainable when combined with the following other requirements:
- Leave at least `0.8 mm` (two perimeters with a `0.4 mm` nozzle) of material between a plate's [socket](/docs/design/Sockets.md)-chamfer and the slide profile. 
- Use simple geometric primitives (arcs and line segments)
- Ensure all arcs have greater than some minimum diameter (`0.8 mm`) to ensure smoothness in real prints.
- Prevent the two halves of a slide from seperating even under the largest clearance between slides employed by Plaice, without substantial force.


### Symmetries

Even with the listed geometric requirements, the shape is still fairly underspecified. To put the interface's shape into sharper focus,
we'll need to explicate what kinds of geometric symmetries are desirable.

There are two major symmetries which apply to the slide interface. Both are kinds of mirror symmetry, but
with different motivations: Ease of Assembly and Strength.

#### Ease of Assembly: Vertical Flip Symmetry

When putting two Plaice plates together with slides, assuming that a protruding and intruding slide are properly paired, the two plates
should fit together without needing to adjust their orientations. By ensuring that plates don't need to
be flipped to match orientations, the cognitive load (and hence, time) involved in putting together a Plaice assembly
is reduced. Namely, this means ensuring a vertical flip symmetry across a central horizontal axis.

#### Asymptotic Strength Under Plate Stacking
<img src="/docs/images/slideinterface/slideinterface-profile-tesselated.svg" alt="Slide Interface, Tessellated" width="64"> <img src="/docs/images/slideinterface/slideinterface-profile-tesselated.svg" alt="Slide Interface, Tessellated" width="64"> <img src="/docs/images/slideinterface/slideinterface-profile-tesselated.svg" alt="Slide Interface, Tessellated" width="64"> <img src="/docs/images/slideinterface/slideinterface-profile-tesselated.svg" alt="Slide Interface, Tessellated" width="64"> </div>

<img src="/docs/images/stackedplates.webp" alt="Stacked Plates" width="256" height="256">

There are situations where '7mm' (HU) thick 3d-printed PLA plates just aren't going to cut it for a given loading.
In those situations, it's reasonable to want to stack plates on top of each other, and secure them to form a larger composite.
This option is readily available through the use of [thru-nubs](/docs/components/ThruNub.md) and [plugs](/docs/components/Plugs.md).

Now, consider what happens when a stack of plates with identical orientations is connected to another stack of plates
using slides -- schematically, the result looks something like the line-drawing above.

To minimize the maximal stress under an applied load, it is beneficial to spread the induced stresses
over the largest possible area. One natural way to do this for the situation of the stacked plates is to ensure
each stack should take a similar cumulative stress. There isn't a simple way to apply that
criterion verbatim... But we can do the next best thing: We can ensure that the _roles_ of each stack are the same in relation
to each other.

To do this, all we need to do is to ensure that between every two stacked protrusions, there's an intrusion formed, and
between every two stacked intrusions, there's a protrusion formed. This is another kind of mirror symmetry.

## FEM Optimization

<img src="/docs/images/slideinterface/slideFEM.png" alt="Slide FEM, Heatmap of Maximum Principal Stress" width="512" height="512">

After the constraints mentioned in the previous section have been applied, the final shape of the Plaice slide interface is obtained
by performing hill-climbing on the maximal stress minimization objective. In particular, since the
objective assumes static loading, and PLA is dramatically stronger under compression than under tension, we can apply the Mohr-Coulomb yield
criterion and use the (max of the) maximum principal stress as a proxy for how close to yielding our parts are. 

## Clearances and Manufacturing Notes

For the slides to fit together, there needs to be some amount of clearance between progruding and intruding slides. Additionally, process-specific (3d printing)
biases need to be corrected for. See [the dedicated design page on clearances](/docs/design/Clearances.md). 

# Clipped and Nubbed Connectors
<img src="/docs/images/plugs/plugtops.jpg" alt="Plugs, Clipped and Nubbed" width="256" height="256"> <img src="/docs/images/plugs/plugstogether.jpg" alt="Plugs, Clipped and Nubbed Connected" width="256" height="256">


Clipped and nubbed connector pairs provide a way to connect two Plaice components, most frequently inside of a Plaice socket.
They are "snap" (compliant) connectors where the four clips of a "clipped" connector grabs on to the four nubs of a "nubbed" connector,
preventing movement between the two halves until the connection is undone through applied force to separate them. 

## Geometry

<img src="/docs/images/connectorinterface/connectorinterface.png" alt="Connector interface, 1/8 of the top-down schematic" width="512" height="512">

Clipped and nubbed connectors have a rounded square footprint which fits inside
of Plaice sockets. Both types of connectors share the same four-fold rotational symmetry about their center, with the eponymus "clips"
and "nubs" arranged along the edges of the rounded square base. For clipped connectors, that's all there is to the top-down layout,
but for nubbed connectors, there is additionally a central octagonal island and four corner islands. 

### Clip geometry
<img src="/docs/images/connectorinterface/clippedpluginterface.png" alt="1/2 of a clip profile" width="512" height="512">

The geometry of the clips is very carefully engineered for their small 5.0mmx2.3mm footprint to ensure that they won't break
under typical use (and then some) in Plaice. The clip prongs are tapered in such a way that it does not take many layers from
the tips of the clips to reach a width which is able to pack in two external perimeters, which allows the profile to mostly
behave like a bulk material. The profile of a clip prong is made of three arcs, one for the clip center, one for the tip of
the prong, and another for the outside envelope of the clip, with a line segment completing the connection to the base.
The top arc is constrained by a minimum size to allow for the 3d-printed clip prong tip to more smoothly slide against a paired
nub, and the angle of closure of the interior arc is also set to help the prong tip move out of the way when a nub is inserted.
The central arc's radius is maximized to spread out stresses encountered when the clip is bent, but the outer arc's geometry
(+ line segment) is largely set up for achieving the maximum number of perimeters as quickly as possible, since FEM results
indicate that stress does not tend to concentrate there. 

#### Clip FEM
<img src="/docs/images/connectorinterface/clipFEM.png" alt="FEM on a Clip w/ heatmap of Frobenius norm of strain tensor" width="512" height="512">

In order to ensure that the compliant clips stay functional after repeated use, a finite element analysis of the strains experienced
by the clip when bent is very valuable, because it allows for optimization of the clip design. Additionally, for the clip geometry
as defined above, to bound the value of the base width of the clip, it's necessary to simulate what happens when the clip is deformed
during connection to ensure that the clip prongs never have any part of them extend beyond the base footprint, because it would cause
interference with the four corners of the paired nubbed connector.

To analyze the results of the FEM, unlike the situation with the slide interface FEM (TODO: link), the stresses experienced by the
clip during connection are transient. Consequently, a static analysis like what was implemented in FreeCAD for this will not
tell the whole picture, but we can still gain some useful insights from the analysis. In particular, we are interested in the
strain experienced by the clip when bent to its "open" position, and want to minimize the maximum principal strain. Unfortunately,
FreeCAD has no built-in expression for principal strain, and finding principal strain using a component-based closed formula is fairly
unwieldy. However, we _can_ input a formula for the Frobenius norm of the strain tensor, which allows us to indirectly bound the
principal strain. 

### Nub Geometry
<img src="/docs/images/connectorinterface/nubbedconnectorprofile.png" alt="1/2 of a nub profile" width="512" height="512">

For the most part, the geometry of nubs is simply the inverse of that of clips, but the bottom of the nub is modified to connect
to the connector base with a straight line as opposed to an arc. This nub base is set up in such a way that the bottom of the nub
has exactly the same width as its maximum width up above. This is done for the sake of giving extra clearance to the tips of connected
clips (to handle deformations under load), but also to create a clean visual transition to the seam with the central octagonal island.

## Clearances

For the top-down footprint, most clearances from the top-down "interface" profile are set to the generic "contact" clearance, since the
mating surface area is fairly small, and it's structurally important to prevent relative rotation of the connectors as much as possible.
However, there are some exceptions -- in particular, the central octagonal island on the nubbed connector is given more clearance from
the interface bounds, because the central island is not meant to engage with anything else, and is simply there to serve as a sheath
for inserted M2 bolts. 

The side profiles of the nub and the clip provide their own special cases. For the clip profile, no clearances whatsoever are applied,
because the clip is compliant, and having fixed geometry also greatly simplifies the analysis of the clip's strength. The nub does
have clearances applied, but with a larger clearance at the tip of the nub which gradually works its way toward tangency with the interface
as the profile approaches the point of contact with the clip tip. Once again, this is done because the clip is compliant, and so
the required clearance drops closer to the clip's tip.

Vertical clearance between paired connectors is set to seat at the "snug" slide-fit clearance. This is somewhat larger than the contact
fit clearance to ensure that the connectors will tend to have a small gap between them when assembled with plugs on opposing sides of a
Plaice socket. The gap allows for a bit of pre-load to be generated by tightened M2 bolts, if desired. Additionally, the gap allows for Plaice sockets
to have somewhat looser tolerances on their chamfers given the relaxed seating of connectors, especially since this is made bidirectional
through the fact that a clip can engage with a nub and still have some retaining force even if not fully inserted.

## Relation to Sockets

Clipped and nubbed connectors are designed to fit inside of Plaice sockets, but the height of the connectors is only half (2.0mm) of the
central portion of a Plaice socket (4.0mm), and so at first, it would seem like we're leaving extra space on the table. Even stranger,
clipped connectors in Plaice typically sit atop a 2.0mm rounded square pad, but nubbed connectors don't have this! What gives?

There are two primary reasons for this apparent asymmetry, and both are related to how the system can accommodate alternative
types of connections which don't rely upon the clip-and-nub geometry. First, the 2.0mm rounded square pad provides valuable
space for the clipped connectors to be able to accommodate a captive M2 nut, which would be virtually impossible without it.
Second, it allows "stub" connectors consisting just of a 2.0mm rounded square pad on a plug to mate with a nubbed plug.
While that may not seem terribly useful at first, it does open the door to the possibility of _routed_ Plaice components
which would otherwise need clipped connectors. While the current iteration of this specification doesn't include it,
future iterations should.

There's another, more subtle, more structural reason. The positioning of the clips on the clipped connectors and the corner islands on the nubbed connectors is such that
they make contact with an enclosing socket, preventing rotation. Consequently, they are made to be as thick as they possibly can
be considering the limited footprint of the connectors, applied clearances, and other objectives and constraints related to clip
geometry. Even after all that, the clip (being compliant) is still a seeming target for accidental breakage.
However, in the case of the clip geometry, the aforementioned 2.0mm rounded square pad helps to ensure that the clip
itself does not bear the brunt of the torque-induced stresses when inserted into a socket.

## Standard Orientation

By default, when considering horizontal Plaice plates, it's typical to assume that the top side of the plate is for inserting clipped connectors,
and the bottom half is where components with nubbed connectors get inserted. The reasoning for this is based upon the geometry of beams:
The bottom of a beam needs to be able to sit flat on a surface. Consequently, the bottom of a beam cannot protrude, as would be required
for a nubbed connector to reach the correct mating depth, and so it instead has a clipped connector embedded in a socket at the bottom and a nubbed
connector on top. Consistency with beam orientation is important for shelves, because it determines what can be mounted to the top surface of the shelf,
and generally, that includes all sorts of things, like Gridfinity baseplates. Conversely, the bottom side of a Plaice plate is a good place for
e.g: Gridfinity mounts by analogous reasoning.

## M2 Bolt Usage
Clipped connectors typically have a channel on their side for the insertion of a M2 hex nut. When fully inserted, the nut is held
captive against some backing walls, preventing rotation. A hole on the front face of the clipped connector allows access to the
nut from external M2 bolts. 

Conversely, nubbed connectors make some provision for an M2 bolt to be inserted through their back face, with the shaft of the
bolt coming through a hole on the front face.

When the two halves are connected together via an M2 bolt/nut pair, the snap effectively cannot be separated unless the
M2 connection is undone, which can have many practical structural purposes in Plaice assemblies. At the same time, it is important
to realize that adding M2s is not a silver bullet -- an assembly can still be structurally weak even if all snaps have M2s.

## Printability Modifications
<img src="/docs/images/thrunubs/thrunubprintabilitybottom.webp" alt="Thru-nub Bottom, Showing Mouse Ears" width="256" height="256"> <img src="/docs/images/opengrid/opengridprintability.webp" alt="OpenGrid mount plate bottom" width="256" height="256">

The print orientation of clipped and nubbed connectors is almost always such that their front and back faces align with the +-Z
printer axis, because typically they are printed in arrays on Plaice components which are intended to affix the component
to a Plaice plate, and so it generally makes sense to align the XY printer plane and the plane of these arrays. However,
this raises a problem for components (e.g: thru-nubs, beams (TODO: link!)) which have clip or nub connectors on opposing sides:
Which connector should be on the bottom (and consequently, require some support and/or support removal, and possibly experience
some surface deformations due to sagging), and which should be on the top? Intuition would say that the clipped connector
is more intricate, and with more delicate features (compliant clips), and so it should belong on top.

Consequently, it's worthwhile to consider ways to "bake in" support structures for nubbed connectors oriented facing downwards
on the print bed to improve print quality, first layer adhesion, and the ease of support removal. Luckily, the geometry
of the nubbed connector makes it relatively easy to do so. Assuming that the tips of the nubs and all four corners have
good bed adhesion, bridging between them is a piece of cake given the involved dimensions. However, by default, they
don't have good bed adhesion. To improve this, an eight-petaled contiguous shape is formed on the first layer
to provide "mouse ears" for the first layer. (TODO: include picture) This dramatically improves adhesion, and consequently
allows nubbed connectors to be printed upside-down without generated support structures.

There is no such similar printability modification for clipped connectors. This is for two primary reasons:
Firstly, due to the printability modification for nubbed connectors, the same kind of modification for clipped
connectors is largely unnecessary, since it results in the face of most clipped connectors facing upwards (+Z)
in print orientation. Secondly, the geometry of the clip connectors would require support structures to be
generated at the four corners of its layout, because unlike nubbed connectors, there is nothing in the corners on
the bottom printed layers for the base of the connector to bridge from. While that problem isn't insurmountable,
its inconvenience and low probability of use mean that it is currently unimplemented in Plaice. 

### Support removal for nubs
The process for removing the supports on nubs is fairly simple, if a little tedious.
#### Step 1: Clear Surroundings
<img src="/docs/images/opengrid/opengridsuportremovalpart2.webp" alt="Visual result of step 1" width="256" height="256">

First remove any surrounding supports, such as the support structure generated for the flat of the OpenGrid mount plate bottom as shown in the section
above, to obtain something like the image shown for this step. In many cases, this will remove most of the mouse-ears attached to the nubs, but if it
doesn't remove all of them, manually pick them off one-by-one, like flower petals.
#### Step 2: Break bridges
<img src="/docs/images/opengrid/opengridsupportremovalpart3.webp" alt="Visual for step 2" width="256" height="256">

Using a pair of needle-nose pliers, grab onto the bridges between the corner squares and the central island on each nubbed connector, and twist
the pliers to cut/break each bridge. Don't worry if material is still hanging off of one side or the other -- there's enough clearance in the design
that this small bit of material won't matter for the sake of fitment. Be somewhat careful to avoid accidentally ripping off the corner squares in
the process, but don't panic if you do -- a few missing connector corners in a large array of nubbed connectors ultimately won't impact much.

#### Finish
<img src="/docs/images/opengrid/opengridsupportremovalend.webp" alt="Final visual" width="256" height="256">



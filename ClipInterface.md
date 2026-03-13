# Clipped and Nubbed Connectors

Clipped and nubbed connector pairs provide a way to connect two Plaice components, most frequently inside of a Plaice socket.
They are "snap" (compliant) connectors where the four clips of a "clipped" connector grabs on to the four nubs of a "nubbed" connector,
preventing movement between the two halves until the connection is undone through applied force to separate them. 

## Geometry

### General layout

### Clip geometry

#### Clip FEM

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

## Clearances

## Relation to Sockets

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

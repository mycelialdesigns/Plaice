# Plates

<img src="/docs/images/plate.jpg" alt="A Plaice Plate" width="256" height="256">

The single most important Plaice component, plates give the rest of the system a structural base.
A plate consists of a `7mm` (`1 HU`) rectangular slab covered in an array of sockets spaced `21mm` (`1 CU`) apart,
with opposing pairs of intruding and protruding slides along the perimeter. Plates are so named because
they serve a similar purpose to the "baseplates" in Gridfinity and other similar systems, in that they
are a central component which all other components of the system can connect to, but the "base" prefix
is dropped to avoid the connotation of a fundamental placement or orientation.

## Printability modifications

<img src="/docs/images/plate/printableplate.webp" alt="Printable Plate" width="256" height="256"> <img src="/docs/images/plate/printableplatecorner.webp" alt="Printable Plate, Corner View" width="256" height="256"> <img src="/docs/images/plate/printableplateside.webp" alt="Printable Plate, Side View" width="256" height="256">


The "printable" version of plates requires no slicer-generated supports to print, because the necessary supports are baked in
to the design. First, mouse ears were added to the design to protect corners and overhanging protruding slides
from warping while providing somewhat better bed adhesion for small plates. Then, for supports, two preforated-boundary
single-perimeter strips support both the intruding and protruding slides' overhangs at points where they are _concave up_,
with the strips more or less equidistant from the local minima there. This is done to minimize the impact that leftover
scarring from the preforations would have on the overall fitment of slides on plates.

### Suggested Support Removal Process

When removing the supports of a large number of printed Plaice plates, it's a good idea to have an easily-repeatable process
that can be worked into muscle memory. Here is one possible way of doing that:

#### 1. Peel Protrusion Supports
<img src="/docs/images/plate/platesupportremovalstep1.webp" alt="Step 1 Visual" width="256" height="256"> 

Locate the edge of one of the two-perimeter supports for the plate's protruding slides. With a pliers, grab and
pull upwards **slowly** to remove the supports along their preforations. Do the same for the other protruding slide,
and for the protruding corner support.

#### 2. Peel Intrusion Supports
<img src="/docs/images/plate/platesupportremovalstep2.webp" alt="Step 2 Visual" width="256" height="256"> 

Locate the edge of one of the two-perimeter supports for the plate's intruding slides. Perform the same kind of
operation as step 1 on these supports, and do it for both intruding slides. 

#### 3. Check For Partially-Removed Supports
<img src="/docs/images/plate/platesupportremovalstep3.webp" alt="Step 3 Visual" width="256" height="256"> 

Inspect the workpiece to verify that there are no partially-removed supports. If there are some, just grab hold
of what's left and again peel them away from their preforations slowly with the needle-nose pliers.

#### 4. Tear Off Intruding Corner Mouse Ear
<img src="/docs/images/plate/platesuppoortremovalstep4.webp" alt="Step 4 Visual" width="256" height="256">

Grab hold of the mouse ear on the bottom of the plate near the intruding corner with your pliers as shown.
Feel free to rip the ear off **fast**, then carefully trim off any remaining material from the mouse ears
by grabbing hold of it with the pliers and twisting, which may need to be repeated depending on tearing
technique and the quality of the print's first layer.


#### 5. Tear Off Protruding Corner Brim
<img src="/docs/images/plate/platesupportremovalstep5.webp" alt="Step 5 Visual" width="256" height="256"> 

Grab hold of the brim at the intruding corner with your pliers as shown, and perform the same kind of process
as the previous step. Once again, feel free to rip **fast** and "trim" leftover pieces as needed. 

#### 6. Finish
<img src="/docs/images/plate/platesupportremovalfinish.jpg" alt="Finished Plate" width="256" height="256"> 

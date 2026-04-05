# Clearances
Designing Plaice components to fit together requires careful attention to the nominal clearances between components. We talk here
about clearances instead of tolerances because the manufacturing tolerance of 3d prints is inherent to the _printer_, not to the
models that we feed into the slicer. 

## Preliminary Definitions
Clearances describe the size of gaps between two surfaces, and so it's important to have a clear reference to what the surfaces
involved are. In our case, there are actually three different sources for relevant geometry to reference: "*interface*" geometry
which consists of 2d profiles in CAD expressing an idealized meeting-curve of two components, "*model*" component geometry which
represents the geometry expressed in 3d CAD and/or in exported .stl files, and "*de facto*" geometry which is the physical geometry
of real components after printing. 

## Print Correction Clearances
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
lump that in with manufacturing tolerances.

### XY Hole Shrinkage Clearance

### Z Overhang Depression Clearance

## The Clearance Multiplier


## Clearance Levels

### Contact Fit Clearance

### Snug Slide Fit Clearance

### Smooth Slide Fit Clearance

## Interaction with "Tolerances" 
Manufacturing tolerances are essentially an expression of the allowed variation in certain measured dimensions of a manufactured object,
typically from a design perspective which is meant to constrain the types of manufacturing processes used on the object. 

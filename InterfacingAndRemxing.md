# Interfacing and remixing

Plaice is intended to be an open ecosystem where anyone with CAD or 3d modeling experience can contribute,
but beyond that, to be an ecosystem which inspires a culture of heavy remixing and shared learning.

## Licensing

To support these goals, Plaice employs two separate licenses to different kinds of artifacts: the 
CErN-OHL-S to all CAD files, and CC-BY-SA to everything else in this repository and its associated exports,
including 3d model files. 

The OHL-S is a "strongly reciprocal" license, meaning that any released CAD files or other
released files which use Plaice's CAD files must share the preferred form of the source file for making modifications,
which is most often the derivative CAD file(s) in question. In adopting the license for CAD files, Plaice intends
to prevent the scenario of a designer privately holding on to a CAD file, and only releasing .STLs for public
consumption due to some ulterior motive (possibly, but not necessarily commercialization-related.) Plaice
_does not care_ if the designs are mass-printed and sold, but the project does care about ensuring that
designers and consumers are on equal footing, and that if Plaice is part of somebody's path to becoming
a maker, that path has as little resistance as possible.

CC-BY-SA is adopted for all other artifacts (including 3d models) as a pragmatic lowering to the case
where it doesn't make sense to reference an original source as in the OHL-S. The attribution and share-alike
components ensure that the ecosystem of derived files remains open to remixing, and that remixes all have
an unbroken chain of attribution. Both are crucial to the kind of ecosystem that Plaice intends to cultivate.

## How-To
There are multiple different ways to create new components for Plaice or to remix existing components,
each with their own tradeoffs.

### Lowest Friction, Lowest Customizability: Glue-Together Parts

By far the easiest and most-preferred way to integrate with Plaice is to simply depend upon gluing printed parts on to
a Plaice clipped or nubbed cover, as described in more detail on the dedicated page (TODO: link here!).
While this is incredibly low-friction for the designer, and is completely agnostic to choice
of technoogies, it only generally applies to components which only seek to integrate with the
connector-and-socket portion of Plaice. Anything else will need to use one of the two other methods.

### Medium Friction, High Customizability: CAD Derivatives

The next-preferred way to integrate with Plaice is to leverage the FreeCAD files made available in this repository.
Parts in those files use a hybrid of referencing a spreadsheet (`sheet.FCStd`) for "Plaice global" values which define
the system, and copy-on-change linked objects with custom properties (TODO: cite MangoJelly vids) for values which
define the configurations of components. To use them, simply create a copy of the CAD directory from this repo, and
add new FreeCAD file(s) devoted to your design which reference the base Plaice system files, or modify the Plaice
system CAD files directly. Once you are finished with design, optionally export models of your component(s) at the different standard
clearance levels, and upload 'em somewhere together with any CAD files that you created, used or modified which depend on
Plaice components.

### Medium-High Friction, High Customizability: STL Modifications

3d printing has an extensive .stl remix culture, and so it's important that Plaice supports the workflow.
However, in Plaice, the clearances applied to connectors and slides are _meaningful_, and there are good
structural reasons for individual users of the system to want to minimize those clearances to tune
the system to their own printer. As a result, exported non-parametric 3d models are in a bit of a difficult
spot -- while they can be remixed, providing all standard clearance levels would require creating multiple
different copies of those models, which is frankly somewhat of a pain. To partially settle this,
in the case of direct 3d model remixes, 

## On Including Batteries

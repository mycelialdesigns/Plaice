# Bolt-On Components

<img src="/docs/images/gridfinityopengridconstruction/step8.webp" alt="A gridfinity bolt-on secured to a nubbed backing" width="256" height="256">

In a variety of scenarios, it can make more sense to print a Plaice component out of multiple different parts
which then get bolted together than to design or print the Plaice component as a single part. On the design side,
for example, a maker looking to [integrate](/docs/design/InterfacingAndRemixing.md) with the system may be using direct 3d modeling and find the prospect of providing
pieces with multiple different levels of clearances to be daunting. For another consideration, when printing the required support geometry for a unified
part could require awkwardly-placed or hard-to-remove supports. 

Plaice encourages the use of bolt-on components for these scenarios when the component in question needs an array of
clipped or nubbed [connectors](/docs/design/ClipInterface.md), which are provided via [backings](/docs/components/Backings.md).
The bolt-on component may then be attached to the backing using [M2 hardware](/docs/design/M2Bolts.md).

## Design

To create a bolt-on component, all that's needed is an array of appropriate pockets and holes spaced identically to the [unit grid](/docs/design/Units.md)
carved into the component -- a square array with center-to-center spacings of `21 mm`. At each of those positions, there should be both an at least `2 mm` through-hole
(after printing -- slight oversizing is recommended) and a pocket to accommodate a M2 hex nut with around `1 HU` (`1.7 mm`) of material beyond the bottom of the pocket
to where the backing would go. The latter requirement ensures that required bolt lengths for assemblies follow [what is stated in the guide](/docs/design/M2Bolts.md), and so it helps to minimize
potential confusion or even frustration around needing to source bolts of different lengths. Additionally, while not required, it's recommended that the pocket
for M2 hex nuts is at least `2.0 mm` deep to prevent hardware from protruding, since the same pocket may be used for socket-head M2 bolts in some assemblies. 
Finally, please ensure that your component has appropriate [clearances](/docs/design/Clearances.md) built-in to allow it to tile cleanly on a unit grid with other components.

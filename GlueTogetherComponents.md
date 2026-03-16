# Glue-together Components

In a variety of scenarios, it can make more sense to print a Plaice component out of multiple different parts
which then get super-glued together than to design or print the Plaice component as a single part. On the design side,
for example, a maker looking to integrate with the system may be using direct 3d modeling and find the prospect of providing
pieces with multiple different levels of clearances to be daunting. For printing, the required support geometry for a unified
part could require awkwardly-placed or hard-to-remove supports. 

Plaice encourages the use of glue-together components for these scenarios when the component in question needs an array of
clipped connectors (or nubbed connectors, assuming that M2 support is not relevant to the component in question). To do so,
simply dimension the component with a square pad which is 21 * W - 0.2 mm by 21 * L - 0.2mm (if a clearance is not specified,
otherwise replace 0.2mm with the contact clearance) for width W and length L in cell units, and indicate that the component
is supposed to be glued on to a Plaice (clipped/nubbed) cover with the given width and length dimensions. Out-of-the-box
Plaice components do this routinely when a clipped connector array is involved (TODO: link examples). 

However, it is important to note that in the case of _nubbed_ connectors, access to the back-side M2 bolt holes could potentially
be blocked by the glued-on piece unless it is designed carefully. Since blocked bolt-holes directly affect the affordances available on the
opposite side of a Plaice plate's socket (i.e: whether or not an opposing clipped connector can actually be secured with a nut), blocking
bolt holes is strongly discouraged. 

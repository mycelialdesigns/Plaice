# M2 Bolts
<img src="/docs/images/shelfconstruction/step15.webp" alt="Nubbed covers secured on the bottom of a shelving unit" width="256" height="256">

Plaice largely avoids the use of embedded hardware for the sake of rapid prototypin, but when it comes time to "cement" a design for a household organizer,
it can be advantageous to incorporate hardware for improving the strength of assemblies. (For a worked example of this,
see e.g: the [recipe for stacking shelves](/docs/recipes/Shelves.md)). Additionally, Plaice leverages hardware in
situations where printing a single part could be suboptimal in [bolt-on components](/docs/components/BoltOnComponents.md).

## Required Lengths
M2 hardware is employed in Plaice, and it's strongly recommended you buy a kit
of bolts which (at least) includes `4 mm`, `6 mm`, `10 mm`, `12 mm`, and `16 mm` lengths.

The following is a handy guide
to what lengths of M2 bolts are required for various scenarios.

### Backings onto Bolt-ons

To use bolt-on components in the most straightforward way, where they
are simply bolted on to a Plaice [backing](/docs/components/Backings.md) which provides
[connectors](/docs/components/ClipInterface.md), M2 nuts must be slid into the backing.
In this case, the following lengths of M2 bolts are inserted from the bolt-on side:

| | Nubbed Backing | Clipped Backing |
|--|:--:|:--:|
| **Bolt-On** | `4 mm` | `6 mm` |

### Bolt-ons, Nubbed and Clipped Connectors

Beyond the case of backing bolt-on components, M2 hardware can be employed in Plaice
to secure connections which would otherwise be accomplished purely through clip/nub connections. This attatchement provides more resistance to pull-out and some degree of preload. For example, Plaice clipped [covers](/docs/components/Covers.md)
may be attached to nubbed covers and secured with `6 mm` M2 bolts (together with captive M2 nuts).
Within Plaices structure, we can generalize that rule to other components with clipped and nubbed connectors:
e.g: a nubbed [plug](/docs/components/Plugs.md) attached to a clipped plug _also_ can be secured with `6 mm` M2 bolts.

But clipped and nubbed connectors aren't the only things that can be on opposite ends (bolt head and nut end) of
a M2 bolt -- Bolt-on components (TODO: link) atop backings may be at either of the ends. In these
situations, a single bolt should go through
end-to-end. In tabular form, here are the required lengths of bolts for every combination of two "ends":

| | Bolt-On  | Nubbed Connector | Clipped Connector |
|--|:--:|:--:|:--:|
| **Bolt-On** | `16 mm` | `10 mm`  | `12 mm`   |
| **Nubbed Connector** | `10 mm` | -  | `6 mm`   |
| **Clipped Connector** | `12 mm`  | `6 mm`  | - |

### Thru-Nubs

In a Plaice assembly involving thru-nubs, the required M2 bolt lengths may be derived from the table in the
previous section by adding `7 mm` (`1 HU`) for each (possibly chained) thru-nub, and then rounding up
to the nearest multiple of `2 mm`. This rounding is not _ strictly required_ if you have readily available bolts
 with the required dimensions, but M2 bolts 
in `2 mm`-multiple lengths tend to be preferential. 

One particular case of this is worth calling out due to its frequency:
When connecting **two beams** (as one would for [building stacking shelves](/docs/recipes/Shelves.md)),
a nubbed connector from the top of one beam attaches to a thru-nub which then attaches to the
clipped connector at the bottom of the next tier's beam. From the table above, the base length
is then `6 mm`, and so `+ 7 mm = 13 mm`, or rounded, **`14 mm`**. 

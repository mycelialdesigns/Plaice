# M2 Bolts

## Required Lengths

### Backings onto Bolt-ons

To use bolt-on components (TODO: link) in the most straightforward way, where they
are simply bolted on to a Plaice [backing](/docs/components/Backings.md) which provides
[connectors](/docs/components/ClipInterface.md), M2 nuts must be slid into the backing
and then the following lengths of M2 bolts inserted from the bolt-on side:

| | Nubbed Backing | Clipped Backing |
|--|:--:|:--:|
| **Bolt-On** | `4 mm` | `6 mm` |

### Bolt-ons, Nubbed and Clipped Connectors

Beyond the case of bolt-on components on backings, M2 hardware is commonly employed in Plaice to be able
to secure connections which would otherwise be accomplished purely through clip/nub connections in order
to provide more resistance to pull-out and some degree of preload. For example, Plaice clipped [covers](/docs/components/Covers.md)
may be attached to nubbed covers and secured with `6 mm` M2 bolts (together with captive M2 nuts).
The structure of Plaice is such that we can generalize that rule to other components with clipped and nubbed connectors:
e.g: a nubbed [plug](/docs/components/Plugs.md) attached to a clipped plug _also_ can be secured with `6 mm` M2 bolts.

However, clipped and nubbed connectors aren't the only things that can be on opposite ends (bolt head and nut end) of
a M2 bolt -- in particular, bolt-on components (TODO: link) (atop backings) may be at either of the ends. In these
situations, the bolts from the previous section should be removed in favor of having a single bolt go through
end-to-end. In tabular form, here are the required lengths of bolts for every combination of two "ends" to
the length of the bolt:

| | Bolt-On  | Nubbed Connector | Clipped Connector |
|--|:--:|:--:|:--:|
| **Bolt-On** | `16 mm` | `10 mm`  | `12 mm`   |
| **Nubbed Connector** | `10 mm` | -  | `6 mm`   |
| **Clipped Connector** | `12 mm`  | `6 mm`  | - |

### Thru-Nubs

In a Plaice assembly involving thru-nubs, the required M2 bolt lengths may be derived from the table in the
previous section by adding `7 mm` (`1 HU`) for each (possibly chained) thru-nub, and then rounding up
to the nearest multiple of `2 mm`. Strictly speaking, this rounding is not _required_ if you have bolts
on-hand (or can easily source them) with the required dimensions, but M2 bolts tend to be preferentially
stocked in lengths that are multiples of `2 mm`. 

One particular case of this is worth calling out due to its frequency:
When connecting **two beams** as one would for [building stacking shelves](/docs/recipes/Shelves.md),
a nubbed connector from the top of one beam attaches to a thru-nub which then attaches to the
clipped connector at the bottom of the next tier's beam. From the table above, the base length
is then `6 mm`, and so `+ 7 mm = 13 mm`, or rounded, **`14 mm`**. 

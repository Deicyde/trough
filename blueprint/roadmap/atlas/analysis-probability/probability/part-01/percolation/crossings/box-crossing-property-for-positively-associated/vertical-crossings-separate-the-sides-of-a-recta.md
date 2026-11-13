---
declaration: section
origin: cited
lean: StatMech.Universality.CrossingSeparatesH, StatMech.Universality.CrossingArcSides, StatMech.Universality.rsw_strip_glue_of_crossingArcSides
statement: formalized
proof: formalized
---

# Vertical crossings separate the sides of a rectangle

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/vertical-crossings-separate-the-sides-of-a-recta/index.html).

## Vertical overlap crossings meet every horizontal crossing

For the configuration `ω`: whenever `x_B` on the bottom side of the overlap
`[m, m'] × [c, d]` is joined to the top side inside the overlap, every open left–right path of
`[α, β] × [c, d]` meets the open cluster of `x_B` inside the overlap.

Formalized by `StatMech.Universality.CrossingSeparatesH`, a definition declared in [MathlibExt/Probability/Percolation/Universality/CrossingSeparation.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/Universality/CrossingSeparation.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/vertical-crossings-separate-the-sides-of-a-recta/index.html#crossing-separates-h).

## Vertical overlap crossings separate the sides of a rectangle

For the configuration `ω`: whenever `x_B` on the bottom of the overlap is joined to its top,
there is a set `L` containing the left side of `[α, β] × [c, d]` and disjoint from its right side
such that every lattice edge of the rectangle crossing the boundary of `L` has an endpoint in the
open cluster of `x_B` inside the overlap.

Formalized by `StatMech.Universality.CrossingArcSides`, a definition declared in [MathlibExt/Probability/Percolation/Universality/CrossingSeparation.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/Universality/CrossingSeparation.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/vertical-crossings-separate-the-sides-of-a-recta/index.html#crossing-arc-sides).

## RSW gluing from side separation

RSW gluing: for a positively associated probability measure `μ`, if `CrossingArcSides` holds
for every configuration, then `μ(H_{[a, m']}) μ(V_{[m, m']}) μ(H_{[m, b]}) ≤ μ(H_{[a, b]})`.

Formalized by `StatMech.Universality.rsw_strip_glue_of_crossingArcSides`, a theorem declared in [MathlibExt/Probability/Percolation/Universality/CrossingSeparation.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/Universality/CrossingSeparation.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/vertical-crossings-separate-the-sides-of-a-recta/index.html#rsw-strip-glue-of-crossing-arc-sides).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Vertical crossings separate the sides of a rectangle](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/vertical-crossings-separate-the-sides-of-a-recta/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/vertical-crossings-separate-the-sides-of-a-recta)

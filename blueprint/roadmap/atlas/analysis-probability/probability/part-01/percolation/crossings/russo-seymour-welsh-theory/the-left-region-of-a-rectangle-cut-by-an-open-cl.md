---
declaration: section
origin: cited
lean: StatMech.Lattice.boxMinusP, StatMech.Lattice.floodFromLeft, StatMech.Lattice.arcS_leftRegion, StatMech.Lattice.ArcS_TwoPathsCross
statement: formalized
proof: formalized
---

# The left region of a rectangle cut by an open cluster

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/the-left-region-of-a-rectangle-cut-by-an-open-cl/index.html).

## Rectangle lattice with an open cluster removed

The square lattice restricted to the rectangle `[α, β] × [c, d]`, with the open cluster of
`x_B` in the overlap rectangle removed.

Formalized by `StatMech.Lattice.boxMinusP`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ArcSides.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ArcSides.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/the-left-region-of-a-rectangle-cut-by-an-open-cl/index.html#box-minus-p).

## Sites reachable from the left side of a rectangle

The sites reachable from the left side of `[α, β] × [c, d]` inside the rectangle without
touching the open cluster of `x_B` in the overlap.

Formalized by `StatMech.Lattice.floodFromLeft`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ArcSides.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ArcSides.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/the-left-region-of-a-rectangle-cut-by-an-open-cl/index.html#flood-from-left).

## Left region of a rectangle cut by an open cluster

The left region: the left side of `[α, β] × [c, d]` together with `floodFromLeft`.

Formalized by `StatMech.Lattice.arcS_leftRegion`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ArcSides.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ArcSides.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/the-left-region-of-a-rectangle-cut-by-an-open-cl/index.html#arc-s-left-region).

## Condition that every left-right crossing meets the open cluster

Every lattice path inside `[α, β] × [c, d]` from the left side to the right side meets the
open cluster of `x_B` in the overlap `[m, m'] × [c, d]`. This fails for some configurations
(`StatMech.Lattice.tpc_arcS_twoPathsCross_false`).

Formalized by `StatMech.Lattice.ArcS_TwoPathsCross`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ArcSides.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ArcSides.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/the-left-region-of-a-rectangle-cut-by-an-open-cl/index.html#arc-s-two-paths-cross).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The left region of a rectangle cut by an open cluster](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/the-left-region-of-a-rectangle-cut-by-an-open-cl/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/the-left-region-of-a-rectangle-cut-by-an-open-cl)

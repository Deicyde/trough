---
declaration: section
origin: cited
lean: StatMech.TwoDim.rectangle, StatMech.TwoDim.leftSide, StatMech.TwoDim.rightSide, StatMech.TwoDim.bottomSide, StatMech.TwoDim.topSide, StatMech.TwoDim.HorizontalCrossing, StatMech.TwoDim.horizontalCrossingEvent, StatMech.TwoDim.VerticalCrossing
statement: formalized
proof: formalized
---

# Rectangle crossings on the square lattice

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/rectangle-crossings-on-the-square-lattice/index.html).

## Rectangle at the origin in the plane lattice

The rectangle `[0, a] × [0, b]` in `ℤ²`.

Formalized by `StatMech.TwoDim.rectangle`, a definition declared in [MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/rectangle-crossings-on-the-square-lattice/index.html#rectangle).

## Left side of a rectangle at the origin

The left side `{0} × [0, b]` of `rectangle a b`.

Formalized by `StatMech.TwoDim.leftSide`, a definition declared in [MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/rectangle-crossings-on-the-square-lattice/index.html#left-side).

## Right side of a rectangle at the origin

The right side `{a} × [0, b]` of `rectangle a b`.

Formalized by `StatMech.TwoDim.rightSide`, a definition declared in [MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/rectangle-crossings-on-the-square-lattice/index.html#right-side).

## Bottom side of a rectangle at the origin

The bottom side `[0, a] × {0}` of `rectangle a b`.

Formalized by `StatMech.TwoDim.bottomSide`, a definition declared in [MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/rectangle-crossings-on-the-square-lattice/index.html#bottom-side).

## Top side of a rectangle at the origin

The top side `[0, a] × {b}` of `rectangle a b`.

Formalized by `StatMech.TwoDim.topSide`, a definition declared in [MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/rectangle-crossings-on-the-square-lattice/index.html#top-side).

## Open left–right crossing of a rectangle at the origin

`ω` has an open left–right crossing of `rectangle a b`: an open path inside the rectangle from
its left side to its right side.

Formalized by `StatMech.TwoDim.HorizontalCrossing`, a definition declared in [MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/rectangle-crossings-on-the-square-lattice/index.html#horizontal-crossing).

## Left–right crossing event of a rectangle at the origin

The event that `rectangle a b` has an open left–right crossing.

Formalized by `StatMech.TwoDim.horizontalCrossingEvent`, a definition declared in [MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/rectangle-crossings-on-the-square-lattice/index.html#horizontal-crossing-event).

## Open bottom–top crossing of a rectangle at the origin

`ω` has an open bottom–top crossing of `rectangle a b`: an open path inside the rectangle from
its bottom side to its top side.

Formalized by `StatMech.TwoDim.VerticalCrossing`, a definition declared in [MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/rectangle-crossings-on-the-square-lattice/index.html#vertical-crossing).

## Bottom–top crossing event of a rectangle at the origin

The event that `rectangle a b` has an open bottom–top crossing.

Formalized by `StatMech.TwoDim.verticalCrossingEvent`, a definition declared in [MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/rectangle-crossings-on-the-square-lattice/index.html#vertical-crossing-event).

## Monotonicity of the open subgraph in the plane

The open subgraph is monotone in the configuration (`d = 2` case of
`StatMech.Universality.openSubgraph_mono_dim`).

Formalized by `StatMech.TwoDim.openSubgraph_mono`, a theorem declared in [MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/TwoDimensional/Crossings.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/rectangle-crossings-on-the-square-lattice/index.html#open-subgraph-mono).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rectangle crossings on the square lattice](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/rectangle-crossings-on-the-square-lattice/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/percolation/crossings/rectangle-crossings-on-the-square-lattice)

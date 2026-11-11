---
declaration: section
origin: cited
lean: StatMech.RSW.Box.rect, StatMech.RSW.Box.measurableSet_connectedWithin, StatMech.RSW.Box.leftSide, StatMech.RSW.Box.rightSide, StatMech.RSW.Box.bottomSide, StatMech.RSW.Box.topSide, StatMech.RSW.Box.HorizontalCrossing, StatMech.RSW.Box.VerticalCrossing
statement: formalized
proof: formalized
---

# Rectangles, crossings, annuli and the box-crossing property on ℤ²

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html).

## Integer rectangle in the plane lattice

The rectangle `[a, b] × [c, d]` in `ℤ²`.

Formalized by `StatMech.RSW.Box.rect`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#rect).

## Measurability of connection inside a set

The event that two vertices are connected by an open path inside `S` is measurable.

Formalized by `StatMech.RSW.Box.measurableSet_connectedWithin`, a theorem declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#measurable-set-connected-within).

## Left side of a general lattice rectangle

The left side `{a} × [c, d]` of `rect a b c d`.

Formalized by `StatMech.RSW.Box.leftSide`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#left-side).

## Right side of a general lattice rectangle

The right side `{b} × [c, d]` of `rect a b c d`.

Formalized by `StatMech.RSW.Box.rightSide`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#right-side).

## Bottom side of a general lattice rectangle

The bottom side `[a, b] × {c}` of `rect a b c d`.

Formalized by `StatMech.RSW.Box.bottomSide`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#bottom-side).

## Top side of a general lattice rectangle

The top side `[a, b] × {d}` of `rect a b c d`.

Formalized by `StatMech.RSW.Box.topSide`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#top-side).

## Open left–right crossing of a general rectangle

An open left–right crossing of `rect a b c d` by a path inside the rectangle.

Formalized by `StatMech.RSW.Box.HorizontalCrossing`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#horizontal-crossing).

## Open bottom–top crossing of a general rectangle

An open bottom–top crossing of `rect a b c d` by a path inside the rectangle.

Formalized by `StatMech.RSW.Box.VerticalCrossing`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#vertical-crossing).

## Left–right crossing event of a general rectangle

The event that `rect a b c d` has an open left–right crossing.

Formalized by `StatMech.RSW.Box.horizontalCrossingEvent`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#horizontal-crossing-event).

## Bottom–top crossing event of a general rectangle

The event that `rect a b c d` has an open bottom–top crossing.

Formalized by `StatMech.RSW.Box.verticalCrossingEvent`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#vertical-crossing-event).

## Measurability of the left–right crossing event

A left–right crossing event of a rectangle is measurable.

Formalized by `StatMech.RSW.Box.measurableSet_horizontalCrossingEvent`, a theorem declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#measurable-set-horizontal-crossing-event).

## Measurability of the bottom–top crossing event

A bottom–top crossing event of a rectangle is measurable.

Formalized by `StatMech.RSW.Box.measurableSet_verticalCrossingEvent`, a theorem declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#measurable-set-vertical-crossing-event).

## Dual left–right crossing of a rectangle

A left–right crossing of `rect a b c d` in the dual configuration `dualConfig ω` (an open
crossing of the dual lattice, read through the primal coordinates of `dualConfig`).

Formalized by `StatMech.RSW.Box.DualHorizontalCrossing`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#dual-horizontal-crossing).

## Dual bottom–top crossing of a rectangle

A bottom–top crossing of `rect a b c d` in the dual configuration `dualConfig ω`.

Formalized by `StatMech.RSW.Box.DualVerticalCrossing`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#dual-vertical-crossing).

## Dual left–right crossing event

The event `DualHorizontalCrossing`.

Formalized by `StatMech.RSW.Box.dualHorizontalCrossingEvent`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#dual-horizontal-crossing-event).

## Dual bottom–top crossing event

The event `DualVerticalCrossing`.

Formalized by `StatMech.RSW.Box.dualVerticalCrossingEvent`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#dual-vertical-crossing-event).

## Square annulus in the plane lattice

The annulus `z + (Λ_{2n} \ Λ_n)`, where `Λ_n = [-n, n]²`.

Formalized by `StatMech.RSW.Box.annulus`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#annulus).

## Open circuit lying in an annulus

The closed walk `w` is an open circuit all of whose vertices lie in `annulus z n`.

Formalized by `StatMech.RSW.Box.IsAnnulusCircuit`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#is-annulus-circuit).

## Existence of an open circuit in an annulus

There is an open circuit inside `annulus z n`.

Formalized by `StatMech.RSW.Box.AnnulusCircuit`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#annulus-circuit).

## Open circuit event in an annulus

The event `AnnulusCircuit`.

Formalized by `StatMech.RSW.Box.annulusCircuitEvent`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#annulus-circuit-event).

## Open circuit in an annulus centered at the origin

There is an open circuit inside the annulus `Λ_{2n} \ Λ_n` centered at the origin.

Formalized by `StatMech.RSW.Box.AnnulusCircuit0`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#annulus-circuit0).

## Left–right crossing event of a box with given aspect ratio

The left–right open crossing of the box `[0, ⌊αn⌋] × [0, n]` (aspect ratio `α`).

Formalized by `StatMech.RSW.Box.boxCrossingEvent`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#box-crossing-event).

## Box-crossing property for a sequence of measures

The box-crossing property for a sequence of set functions `μ n`: for every aspect ratio
`α > 0` there is `c > 0` with `μ n (boxCrossingEvent α n) ≥ c` for all `n`.

Formalized by `StatMech.RSW.Box.P5`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#p5).

## Uniform two-sided box-crossing property

The uniform two-sided box-crossing property for a family `μ ξ n`: for every `α > 0` there is
`c > 0` with `c ≤ μ ξ n (boxCrossingEvent α n) ≤ 1 - c` for all `ξ` and `n`.

Formalized by `StatMech.RSW.Box.P5c`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Defs.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Defs.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html#p5c).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rectangles, crossings, annuli and the box-crossing property on ℤ²](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/rectangles-crossings-annuli-and-the-box-crossing)

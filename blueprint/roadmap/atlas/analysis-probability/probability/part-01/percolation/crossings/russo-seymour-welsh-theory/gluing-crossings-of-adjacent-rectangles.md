---
declaration: section
origin: cited
lean: StatMech.RSW.Strip.LeftHalfCrossing, StatMech.RSW.Strip.RightHalfCrossing, StatMech.RSW.Strip.leftHalfCrossingEvent, StatMech.RSW.Strip.rightHalfCrossingEvent, StatMech.RSW.Strip.measurableSet_leftHalfCrossingEvent, StatMech.RSW.Strip.measurableSet_rightHalfCrossingEvent
statement: formalized
proof: formalized
---

# Gluing crossings of adjacent rectangles

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/gluing-crossings-of-adjacent-rectangles/index.html).

## Open path from the left side of a rectangle to a point

An open path inside `rect a m c d` from its left side to the point `z` (on its right side).

Formalized by `StatMech.RSW.Strip.LeftHalfCrossing`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Strip.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Strip.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/gluing-crossings-of-adjacent-rectangles/index.html#left-half-crossing).

## Open path from a point to the right side of a rectangle

An open path inside `rect m b c d` from the point `z` (on its left side) to its right side.

Formalized by `StatMech.RSW.Strip.RightHalfCrossing`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Strip.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Strip.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/gluing-crossings-of-adjacent-rectangles/index.html#right-half-crossing).

## Left half-crossing event

The event `LeftHalfCrossing`.

Formalized by `StatMech.RSW.Strip.leftHalfCrossingEvent`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Strip.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Strip.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/gluing-crossings-of-adjacent-rectangles/index.html#left-half-crossing-event).

## Right half-crossing event

The event `RightHalfCrossing`.

Formalized by `StatMech.RSW.Strip.rightHalfCrossingEvent`, a definition declared in [MathlibExt/Probability/Percolation/RSW/Strip.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Strip.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/gluing-crossings-of-adjacent-rectangles/index.html#right-half-crossing-event).

## Measurability of the left half-crossing event

A left half-crossing event is measurable.

Formalized by `StatMech.RSW.Strip.measurableSet_leftHalfCrossingEvent`, a theorem declared in [MathlibExt/Probability/Percolation/RSW/Strip.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Strip.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/gluing-crossings-of-adjacent-rectangles/index.html#measurable-set-left-half-crossing-event).

## Measurability of the right half-crossing event

A right half-crossing event is measurable.

Formalized by `StatMech.RSW.Strip.measurableSet_rightHalfCrossingEvent`, a theorem declared in [MathlibExt/Probability/Percolation/RSW/Strip.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/RSW/Strip.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/gluing-crossings-of-adjacent-rectangles/index.html#measurable-set-right-half-crossing-event).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gluing crossings of adjacent rectangles](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/gluing-crossings-of-adjacent-rectangles/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/gluing-crossings-of-adjacent-rectangles)

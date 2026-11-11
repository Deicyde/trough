---
declaration: section
origin: cited
lean: StatMech.Universality.rsw_sqrt_trick, StatMech.Universality.OverlapConnection, StatMech.Universality.overlapConnectionEvent, StatMech.Universality.measurableSet_overlapConnectionEvent, StatMech.Universality.HVIntersectionProperty
statement: formalized
proof: formalized
---

# The square-root trick and gluing crossings through an overlap

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/the-square-root-trick-and-gluing-crossings-throu/index.html).

## Square-root trick

The **square-root trick**: for a positively associated probability measure and increasing
measurable `A`, `B`, `1 - √(1 - μ(A ∪ B)) ≤ max(μ(A), μ(B))`.

Formalized by `StatMech.Universality.rsw_sqrt_trick`, a theorem declared in [MathlibExt/Probability/Percolation/Universality/RSWStrip.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/RSWStrip.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/the-square-root-trick-and-gluing-crossings-throu/index.html#rsw-sqrt-trick).

## Open connection inside an overlap rectangle

An open path inside the overlap `rect m m' c d` from `p` to `q`.

Formalized by `StatMech.Universality.OverlapConnection`, a definition declared in [MathlibExt/Probability/Percolation/Universality/RSWStrip.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/RSWStrip.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/the-square-root-trick-and-gluing-crossings-throu/index.html#overlap-connection).

## Connection event inside an overlap rectangle

The event `OverlapConnection`.

Formalized by `StatMech.Universality.overlapConnectionEvent`, a definition declared in [MathlibExt/Probability/Percolation/Universality/RSWStrip.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/RSWStrip.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/the-square-root-trick-and-gluing-crossings-throu/index.html#overlap-connection-event).

## Measurability of the overlap connection event

A connection event inside a rectangular overlap is measurable.

Formalized by `StatMech.Universality.measurableSet_overlapConnectionEvent`, a theorem declared in [MathlibExt/Probability/Percolation/Universality/RSWStrip.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/RSWStrip.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/the-square-root-trick-and-gluing-crossings-throu/index.html#measurable-set-overlap-connection-event).

## Gluing horizontal crossings through a vertical overlap crossing

For the configuration `ω`: horizontal crossings of `[a, m'] × [c, d]` and of `[m, b] × [c, d]`
together with a vertical crossing of the overlap `[m, m'] × [c, d]` imply a horizontal crossing
of `[a, b] × [c, d]`.

Formalized by `StatMech.Universality.HVIntersectionProperty`, a definition declared in [MathlibExt/Probability/Percolation/Universality/RSWStrip.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/RSWStrip.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/the-square-root-trick-and-gluing-crossings-throu/index.html#hvintersection-property).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The square-root trick and gluing crossings through an overlap](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/the-square-root-trick-and-gluing-crossings-throu/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/the-square-root-trick-and-gluing-crossings-throu)

---
declaration: section
origin: cited
lean: StatMech.Universality.HVMeetProperty, StatMech.Universality.overlapComp, StatMech.Universality.VSeparatesH
statement: formalized
proof: formalized
---

# Horizontal and vertical crossings meet

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/horizontal-and-vertical-crossings-meet/index.html).

## Horizontal and vertical crossings meet

For the configuration `ω`: whenever `x_L` (left side of `[α, β] × [c, d]`) is joined to the
right side and `x_B` (bottom of the overlap `[m, m'] × [c, d]`) is joined to its top, there is a
point `z` of the overlap reached from `x_L` inside `[α, β] × [c, d]` and from `x_B` inside the
overlap.

Formalized by `StatMech.Universality.HVMeetProperty`, a definition declared in [MathlibExt/Probability/Percolation/Universality/HVIntersection.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/HVIntersection.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/horizontal-and-vertical-crossings-meet/index.html#hvmeet-property).

## Open cluster inside the overlap rectangle

The open cluster of `x_B` inside the overlap rectangle `[m, m'] × [c, d]`.

Formalized by `StatMech.Universality.overlapComp`, a definition declared in [MathlibExt/Probability/Percolation/Universality/HVIntersection.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/HVIntersection.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/horizontal-and-vertical-crossings-meet/index.html#overlap-comp).

## Every overlap cluster meets every horizontal crossing

For the configuration `ω` and every point `x_B` of the overlap `[m, m'] × [c, d]`, every open
left–right path of `[α, β] × [c, d]` meets the open cluster of `x_B` inside the overlap.
For `c < d` this fails for some `ω`; see `CrossingSeparatesH` for the version that only
concerns bottom points `x_B` joined to the top.

Formalized by `StatMech.Universality.VSeparatesH`, a definition declared in [MathlibExt/Probability/Percolation/Universality/HVIntersection.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/HVIntersection.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/horizontal-and-vertical-crossings-meet/index.html#vseparates-h).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Horizontal and vertical crossings meet](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/horizontal-and-vertical-crossings-meet/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/horizontal-and-vertical-crossings-meet)

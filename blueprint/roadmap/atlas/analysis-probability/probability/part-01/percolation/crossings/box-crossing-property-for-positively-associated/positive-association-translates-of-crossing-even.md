---
declaration: section
origin: cited
lean: StatMech.Universality.originCluster, StatMech.Universality.percolationEvent, StatMech.Universality.percolationProbability, StatMech.Universality.subcriticalDensities, StatMech.Universality.criticalProbability, StatMech.Universality.percolationEvent_eq, StatMech.Universality.criticalProbability_eq_pc, StatMech.Universality.PositivelyAssociated
statement: formalized
proof: formalized
---

# Positive association, translates of crossing events, and the box-crossing property

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html).

## Open cluster of the origin

The open cluster of the origin of `ℤ^d`.

Formalized by `StatMech.Universality.originCluster`, a definition declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#origin-cluster).

## Event that the origin's cluster is infinite

The event `{0 ↔ ∞}` that the open cluster of the origin is infinite.

Formalized by `StatMech.Universality.percolationEvent`, a definition declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#percolation-event).

## Percolation probability as an extended real

The percolation probability `θ_d(p) = ℙ_p(0 ↔ ∞)`, as an extended nonnegative real.

Formalized by `StatMech.Universality.percolationProbability`, a definition declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#percolation-probability).

## Real densities with no percolation

The set of real densities `p ∈ [0, 1]` with `θ_d(p) = 0`.

Formalized by `StatMech.Universality.subcriticalDensities`, a definition declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#subcritical-densities).

## Critical probability as a real number

The critical probability `p_c(d) = sup {p ∈ [0, 1] : θ_d(p) = 0}` as a real number
(see `criticalProbability_eq_pc`).

Formalized by `StatMech.Universality.criticalProbability`, a definition declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#critical-probability).

## Agreement of the two percolation events

`percolationEvent` is `StatMech.Percolation.percolationEvent`.

Formalized by `StatMech.Universality.percolationEvent_eq`, a theorem declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#percolation-event-eq).

## Agreement of the two critical probabilities

`criticalProbability` is the real-valued form of `StatMech.Percolation.pc`.

Formalized by `StatMech.Universality.criticalProbability_eq_pc`, a theorem declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#critical-probability-eq-pc).

## Positively associated measure

A finite measure on configurations is positively associated if
`μ(A) μ(B) ≤ μ(A ∩ B) μ(univ)` for all measurable increasing events `A`, `B`. The total-mass
factor makes the Harris--FKG inequality invariant under finite scaling.

Formalized by `StatMech.Universality.PositivelyAssociated`, a definition declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#positively-associated).

## Positive association for probability measures is the Harris–FKG inequality

For a probability measure, normalized positive association is the usual Harris--FKG
inequality.

Formalized by `StatMech.Universality.positivelyAssociated_iff_of_isProbabilityMeasure`, a theorem declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#positively-associated-iff-of-is-probabil).

## Harris–FKG inequality for a positively associated probability measure

The usual unnormalized Harris--FKG inequality for a positively associated probability
measure.

Formalized by `StatMech.Universality.PositivelyAssociated.probability`, a theorem declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#probability).

## Translate of a bond configuration

The configuration `ω` translated by `-v`: the state of `e` is the state of `e + v` in `ω`.

Formalized by `StatMech.Universality.translateConfig`, a definition declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#translate-config).

## Left–right crossing event of a translated rectangle

The event that the rectangle `v + [0, a] × [0, b]` has an open left–right crossing.

Formalized by `StatMech.Universality.translatedHorizontalCrossingEvent`, a definition declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#translated-horizontal-crossing-event).

## Bottom–top crossing event of a translated rectangle

The event that the rectangle `v + [0, a] × [0, b]` has an open bottom–top crossing.

Formalized by `StatMech.Universality.translatedVerticalCrossingEvent`, a definition declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#translated-vertical-crossing-event).

## Set of long-direction box-crossing probabilities

The set of crossing probabilities, for `n ≥ n₀` and all translates, of the long direction of
`⌊ρn⌋ × n` and `n × ⌊ρn⌋` rectangles.

Formalized by `StatMech.Universality.boxCrossingProbabilities`, a definition declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#box-crossing-probabilities).

## Infimum of the box-crossing probabilities

The infimum of `boxCrossingProbabilities μ ρ n₀`.

Formalized by `StatMech.Universality.boxCrossingInf`, a definition declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#box-crossing-inf).

## Box-crossing property with a given aspect ratio

The box-crossing property with aspect ratio `ρ > 1`: for some `n₀`, the probabilities of
crossing all translates of `⌊ρn⌋ × n` rectangles in the long direction, `n ≥ n₀`, are bounded
below by a positive constant.

Formalized by `StatMech.Universality.BoxCrossingProperty`, a definition declared in [MathlibExt/Probability/Percolation/Universality/Defs.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Percolation/Universality/Defs.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html#box-crossing-property).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Positive association, translates of crossing events, and the box-crossing property](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/percolation/crossings/box-crossing-property-for-positively-associated/positive-association-translates-of-crossing-even)

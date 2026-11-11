---
declaration: section
origin: cited
lean: StatMech.IsIncreasing, StatMech.IsDecreasing, StatMech.IsIncreasing.compl, StatMech.IsDecreasing.compl, StatMech.IsIncreasing.inter, StatMech.IsIncreasing.union, StatMech.isIncreasing_iInter, StatMech.IsIncreasing.indicator_monotone
statement: formalized
proof: formalized
---

# Increasing events and the FKG lattice condition

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/increasing-events-and-the-fkg-lattice-condition/index.html).

## Increasing event

An event `A ⊆ ConfigSpace E` is *increasing* if it is an upper set for the coordinatewise
order: `ω ∈ A` and `ω ≤ ω'` imply `ω' ∈ A`. This is `IsUpperSet A`.

Formalized by `StatMech.IsIncreasing`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/increasing-events-and-the-fkg-lattice-condition/index.html#is-increasing).

## Decreasing event

An event `A ⊆ ConfigSpace E` is *decreasing* if it is a lower set for the coordinatewise
order. This is `IsLowerSet A`.

Formalized by `StatMech.IsDecreasing`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/increasing-events-and-the-fkg-lattice-condition/index.html#is-decreasing).

## Complement of an increasing event is decreasing

The complement of an increasing event is decreasing (`IsUpperSet.compl`).

Formalized by `StatMech.IsIncreasing.compl`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/increasing-events-and-the-fkg-lattice-condition/index.html#compl).

## Complement of a decreasing event is increasing

The complement of a decreasing event is increasing (`IsLowerSet.compl`).

Formalized by `StatMech.IsDecreasing.compl`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/increasing-events-and-the-fkg-lattice-condition/index.html#compl-2).

## Intersection of two increasing events is increasing

The intersection of two increasing events is increasing (`IsUpperSet.inter`).

Formalized by `StatMech.IsIncreasing.inter`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/increasing-events-and-the-fkg-lattice-condition/index.html#inter).

## Union of two increasing events is increasing

The union of two increasing events is increasing (`IsUpperSet.union`).

Formalized by `StatMech.IsIncreasing.union`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/increasing-events-and-the-fkg-lattice-condition/index.html#union).

## Arbitrary intersections of increasing events are increasing

An intersection of increasing events is increasing (`isUpperSet_iInter`).

Formalized by `StatMech.isIncreasing_iInter`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/increasing-events-and-the-fkg-lattice-condition/index.html#is-increasing-i-inter).

## Indicator of an increasing event is monotone

The real indicator function of an increasing event is monotone.

Formalized by `StatMech.IsIncreasing.indicator_monotone`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/increasing-events-and-the-fkg-lattice-condition/index.html#indicator-monotone).

## An event is increasing iff its indicator is monotone

An event is increasing iff its real indicator function is monotone. See also
`Set.monotone_mem`, the analogous statement for the `Prop`-valued membership predicate.

Formalized by `StatMech.isIncreasing_iff_indicator_monotone`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/increasing-events-and-the-fkg-lattice-condition/index.html#is-increasing-iff-indicator-monotone).

## FKG lattice condition

The *FKG lattice condition* on a weight `π : ConfigSpace E → ℝ`:
`π ω * π ω' ≤ π (ω ⊔ ω') * π (ω ⊓ ω')` for all configurations `ω ω'`. For a positive weight this
is log-supermodularity. Mathlib's `fkg` and `holley` state it in the form
`π a * π b ≤ π (a ⊓ b) * π (a ⊔ b)`.

Formalized by `StatMech.FKGLatticeCondition`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/increasing-events-and-the-fkg-lattice-condition/index.html#fkglattice-condition).

## Log-modular weights satisfy the FKG lattice condition

A log-modular weight, `π ω * π ω' = π (ω ⊔ ω') * π (ω ⊓ ω')`, satisfies the FKG lattice
condition.

Formalized by `StatMech.FKGLatticeCondition.of_logModular`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/IncreasingEvent.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/increasing-events-and-the-fkg-lattice-condition/index.html#of-log-modular).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Increasing events and the FKG lattice condition](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/increasing-events-and-the-fkg-lattice-condition/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/correlation-inequalities/harris-fkg-bk/increasing-events-and-the-fkg-lattice-condition)

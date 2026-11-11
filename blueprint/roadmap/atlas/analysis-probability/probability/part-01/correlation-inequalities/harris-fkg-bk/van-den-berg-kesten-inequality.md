---
declaration: section
origin: cited
lean: StatMech.agreeOn, StatMech.agreeOn_iff_eqOn, StatMech.agreeOn_refl, StatMech.agreeOn_symm, StatMech.agreeOn_trans, StatMech.agreeOn_mono, StatMech.OccursOn, StatMech.OccursOn.mem_self
statement: formalized
proof: formalized
---

# Van den Berg–Kesten inequality

73 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html).

## Agreement of configurations on a set

`agreeOn K ω ω'`: the configurations `ω` and `ω'` take the same value at every coordinate of
`K`. This is `Set.EqOn ω' ω K` (see `StatMech.agreeOn_iff_eqOn`).

Formalized by `StatMech.agreeOn`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#agree-on).

## Agreement on a set as pointwise equality

`agreeOn` is the pointwise form of `Set.EqOn`.

Formalized by `StatMech.agreeOn_iff_eqOn`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#agree-on-iff-eq-on).

## Reflexivity of agreement on a set

Every configuration agrees with itself (`Set.eqOn_refl`).

Formalized by `StatMech.agreeOn_refl`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#agree-on-refl).

## Symmetry of agreement on a set

`agreeOn` is symmetric (`Set.EqOn.symm`).

Formalized by `StatMech.agreeOn_symm`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#agree-on-symm).

## Transitivity of agreement on a set

`agreeOn` is transitive (`Set.EqOn.trans`).

Formalized by `StatMech.agreeOn_trans`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#agree-on-trans).

## Agreement on a set restricts to subsets

Agreement on a set implies agreement on any subset (`Set.EqOn.mono`).

Formalized by `StatMech.agreeOn_mono`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#agree-on-mono).

## Occurrence of an event on a coordinate set

`OccursOn A K ω`: the event `A` occurs on the coordinate set `K` at `ω`, meaning that every
configuration agreeing with `ω` on `K` lies in `A`.

Formalized by `StatMech.OccursOn`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#occurs-on).

## An event occurring on a set contains the configuration

If `A` occurs on some `K` at `ω`, then `ω ∈ A`.

Formalized by `StatMech.OccursOn.mem_self`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#mem-self).

## Occurrence is monotone in the coordinate set

Occurrence on `K` implies occurrence on any larger coordinate set.

Formalized by `StatMech.OccursOn.mono`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#mono).

## Occurrence is monotone in the event

Occurrence of `A` on `K` implies occurrence of any larger event `B ⊇ A` on `K`.

Formalized by `StatMech.OccursOn.mono_event`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#mono-event).

## Disjoint occurrence of events

The *disjoint occurrence* `A □ B`: the configurations `ω` for which there are disjoint
coordinate sets `K` and `L` such that `A` occurs on `K` at `ω` and `B` occurs on `L` at `ω`.

Formalized by `StatMech.disjointOccurrence`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#disjoint-occurrence).

## Membership in a disjoint occurrence

Membership in `A □ B` unfolded.

Formalized by `StatMech.mem_disjointOccurrence`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#mem-disjoint-occurrence).

## Notation for disjoint occurrence

The notation `A □ B` unfolds to `disjointOccurrence A B`.

Formalized by `StatMech.disjointOccurrence_notation`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#disjoint-occurrence-notation).

## Disjoint occurrence lies in the intersection

Disjoint occurrence implies occurrence of both events: `A □ B ⊆ A ∩ B`.

Formalized by `StatMech.disjointOccurrence_subset_inter`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#disjoint-occurrence-subset-inter).

## Disjoint occurrence is symmetric

Disjoint occurrence is symmetric: `A □ B = B □ A`.

Formalized by `StatMech.disjointOccurrence_comm`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#disjoint-occurrence-comm).

## Disjoint occurrence is monotone in both events

Disjoint occurrence is monotone in both events.

Formalized by `StatMech.disjointOccurrence_mono`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/DisjointOccurrence.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#disjoint-occurrence-mono).

## Occurrence of an increasing event is monotone in the configuration

If an increasing event `A` occurs on `K` at `ω` and `ω ≤ ω'`, then `A` occurs on `K` at
`ω'`.

Formalized by `StatMech.OccursOn.mono_config`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#mono-config).

## Disjoint occurrence of increasing events is increasing

The disjoint occurrence of two increasing events is increasing.

Formalized by `StatMech.disjointOccurrence_isIncreasing`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#disjoint-occurrence-is-increasing).

## Product weight of a configuration

The product weight `∏ x, φ x (ω x)` of a configuration `ω`, where `φ x b` is the weight
of value `b` at coordinate `x`.

Formalized by `StatMech.pweight`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#pweight).

## Nonnegativity of the product weight

A product of nonnegative coordinate weights is nonnegative.

Formalized by `StatMech.pweight_nonneg`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#pweight-nonneg).

## Weighted probability of an event

The `pweight φ`-mass `∑ ω ∈ S, pweight φ ω` of an event `S`. When `φ ≥ 0` and
`φ x false + φ x true = 1` for all `x`, this is the probability of `S` under the product measure
whose coordinate `x` has law `φ x`.

Formalized by `StatMech.wprob`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#wprob).

## Monotonicity of the weighted probability

`wprob φ` is monotone for nonnegative weights.

Formalized by `StatMech.wprob_mono`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#wprob-mono).

## Product probability weight has total mass one

A product probability weight has total mass `1`.

Formalized by `StatMech.sum_pweight_eq_one`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#sum-pweight-eq-one).

## Inclusion–exclusion for the weighted probability

Inclusion–exclusion for `wprob`.

Formalized by `StatMech.wprob_union_inter`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#wprob-union-inter).

## Scalar inequality behind the BK induction step

The scalar inequality behind the induction step of the BK inequality: with `q = 1 - p`,
`p, q ≥ 0`, if `c0 ≤ m ≤ a0 b0`, `c1 ≤ a0 b1 + a1 b0 - m` and `c1 ≤ a1 b1`, then
`q c0 + p c1 ≤ (q a0 + p a1) (q b0 + p b1)`.

Formalized by `StatMech.bk_algebra`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#bk-algebra).

## Slice of an event at the first coordinate

The section of an event `C` on `Fin (n + 1)` at first coordinate `x`: the configurations
`ω'` on `Fin n` with `Fin.cons x ω' ∈ C`.

Formalized by `StatMech.slice`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#slice).

## Coordinate set with the first coordinate removed

The coordinate set `{j | j.succ ∈ K}`: `K` with the first coordinate removed, shifted down.

Formalized by `StatMech.sliceSet`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#slice-set).

## Indicator of an event at a prepended configuration

The indicator of `S` at `Fin.cons x ω'` is the indicator of the slice at `ω'`.

Formalized by `StatMech.indicator_slice`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#indicator-slice).

## Product weight factors over the first coordinate

The product weight factors over the first coordinate.

Formalized by `StatMech.pweight_cons`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#pweight-cons).

## Weighted probability by conditioning on the first coordinate

Conditioning on the first coordinate:
`wprob φ S = φ 0 false * wprob ψ (slice S false) + φ 0 true * wprob ψ (slice S true)`,
where `ψ` is `φ` on the remaining coordinates.

Formalized by `StatMech.wprob_slice`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#wprob-slice).

## Slices of an increasing event are increasing

Slices of an increasing event are increasing.

Formalized by `StatMech.slice_isIncreasing`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#slice-is-increasing).

## False slice of an increasing event lies in the true slice

For an increasing event, the `false` slice is contained in the `true` slice.

Formalized by `StatMech.slice_false_subset_true`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#slice-false-subset-true).

## Occurrence with first coordinate false passes to the false slice

Occurrence on `K` at `Fin.cons false ω'` passes to the `false` slice.

Formalized by `StatMech.occursOn_slice_of_false`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#occurs-on-slice-of-false).

## Occurrence with first coordinate true passes to the true slice

Occurrence on `K` at `Fin.cons true ω'` passes to the `true` slice.

Formalized by `StatMech.occursOn_slice_true`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#occurs-on-slice-true).

## Occurrence avoiding the first coordinate passes to the false slice

If the witness set `K` avoids the first coordinate, occurrence on `K` passes to the
`false` slice whatever the value of the first coordinate.

Formalized by `StatMech.occursOn_slice_false_notmem`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#occurs-on-slice-false-notmem).

## Removing the first coordinate preserves disjointness

`sliceSet` preserves disjointness.

Formalized by `StatMech.sliceSet_disjoint`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#slice-set-disjoint).

## False slice of a disjoint occurrence

The `false` slice of `A □ B` is contained in the disjoint occurrence of the `false`
slices.

Formalized by `StatMech.slice_disjointOccurrence_false`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#slice-disjoint-occurrence-false).

## True slice of a disjoint occurrence

The `true` slice of `A □ B` is contained in `(A₀ □ B₁) ∪ (A₁ □ B₀)`, where `A₀, A₁` are
the slices of `A` (similarly for `B`): the first coordinate is used by at most one witness.

Formalized by `StatMech.slice_disjointOccurrence_true`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#slice-disjoint-occurrence-true).

## Occurrence on a one-point configuration space

On a one-point configuration space, `OccursOn A K ω` reduces to `ω ∈ A`.

Formalized by `StatMech.occursOn_subsingleton`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#occurs-on-subsingleton).

## Disjoint occurrence on a one-point space is the intersection

On a one-point configuration space, `A □ B = A ∩ B`.

Formalized by `StatMech.disjointOccurrence_subsingleton`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#disjoint-occurrence-subsingleton).

## BK inequality for product weights on $n$ ordered coordinates

The BK inequality on `Fin n` for a product probability weight `φ`:
`wprob φ (A □ B) ≤ wprob φ A * wprob φ B` for increasing `A, B`.

Formalized by `StatMech.bk_wprob`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#bk-wprob).

## Relabeling configurations along a bijection

The bijection `ω ↦ ω ∘ e` from configurations on `F` to configurations on `E` induced by
`e : E ≃ F`. This is `e.symm.arrowCongr (Equiv.refl Bool)` (`StatMech.cfgEquiv_eq_arrowCongr`).

Formalized by `StatMech.cfgEquiv`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#cfg-equiv).

## Configuration relabeling agrees with the library arrow equivalence

`cfgEquiv e` agrees with Mathlib's `Equiv.arrowCongr`.

Formalized by `StatMech.cfgEquiv_eq_arrowCongr`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#cfg-equiv-eq-arrow-congr).

## Monotonicity of configuration relabeling

`cfgEquiv e` is monotone.

Formalized by `StatMech.cfgEquiv_mono`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#cfg-equiv-mono).

## Agreement on a set under configuration relabeling

Agreement on `e '' K` corresponds to agreement on `K` after transport by `cfgEquiv e`.

Formalized by `StatMech.agreeOn_cfgEquiv`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#agree-on-cfg-equiv).

## Occurrence is invariant under relabeling coordinates

Occurrence is preserved by relabeling the coordinates.

Formalized by `StatMech.occursOn_cfgEquiv`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#occurs-on-cfg-equiv).

## Disjoint occurrence commutes with relabeling coordinates

Disjoint occurrence commutes with relabeling the coordinates.

Formalized by `StatMech.preimage_disjointOccurrence`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#preimage-disjoint-occurrence).

## Product weight is invariant under relabeling coordinates

The product weight is invariant under relabeling the coordinates.

Formalized by `StatMech.pweight_transfer`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#pweight-transfer).

## Weighted probability is invariant under relabeling coordinates

`wprob` is invariant under relabeling the coordinates.

Formalized by `StatMech.wprob_transfer`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 465](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L465). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#wprob-transfer).

## BK inequality for product weights on a finite set

The **BK inequality** for a product probability weight on a finite set `E`: if `φ ≥ 0`
and `φ x false + φ x true = 1` for all `x`, then `wprob φ (A □ B) ≤ wprob φ A * wprob φ B` for
all increasing events `A, B`.

Formalized by `StatMech.bk_wprob_general`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#bk-wprob-general).

## Bernoulli point masses sum to one

The two point masses of the Bernoulli(`p`) measure add up to `1`.

Formalized by `StatMech.bernoulliMeasure_real_false_add_true`, a lemma declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 496](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L496). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#bernoulli-measure-real-false-add-true).

## Bernoulli product measure as a weighted probability

The product Bernoulli measure of an event is its `wprob` for the Bernoulli marginals.

Formalized by `StatMech.bernoulli_real_eq_wprob`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 506](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L506). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#bernoulli-real-eq-wprob).

## Van den Berg–Kesten inequality

The **van den Berg–Kesten (BK) inequality** (van den Berg and Kesten 1985): under the product
Bernoulli(`p`) measure on a finite configuration space, for increasing events `A` and `B`,
`P_p(A □ B) ≤ P_p(A) * P_p(B)`.

Formalized by `StatMech.bk_inequality`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/BK.lean, line 521](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/BK.lean#L521). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#bk-inequality).

## Occurrence of a finitely dependent event within its window

If `A` depends only on `F` and occurs on `K` at `ω`, then it occurs on `K ∩ F` at every
configuration agreeing with `ω` on `F`.

Formalized by `StatMech.ibk_occursOn_inter_finite`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteBK.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/InfiniteBK.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#ibk-occurs-on-inter-finite).

## Disjoint occurrence preserves finite dependence

If `A` and `B` depend only on the coordinates in `F`, so does `A □ B`.

Formalized by `StatMech.ibk_disjointOccurrence_dependsOn`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteBK.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/InfiniteBK.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#ibk-disjoint-occurrence-depends-on).

## Section of a disjoint occurrence

The section on `F` of `A □ B` is contained in the disjoint occurrence of the sections.

Formalized by `StatMech.ibk_section_disjointOccurrence_subset`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteBK.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/InfiniteBK.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#ibk-section-disjoint-occurrence-subset).

## BK inequality on countable configuration spaces

The **BK inequality** on a countable configuration space: for increasing events `A, B`
depending only on the coordinates in a finite set `F`, `P_p(A □ B) ≤ P_p(A) * P_p(B)`.

Formalized by `StatMech.ibk_inequality_of_finite_dependsOn`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteBK.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/InfiniteBK.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#ibk-inequality-of-finite-depends-on).

## BK inequality for three increasing events

The BK inequality for three increasing events depending on finitely many coordinates:
`P_p(P □ (Q □ R)) ≤ P_p(P) * P_p(Q) * P_p(R)`.

Formalized by `StatMech.ibk_triple_of_finite_dependsOn`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteBK.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/InfiniteBK.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#ibk-triple-of-finite-depends-on).

## Union bound from the three-event BK inequality

Union bound from the three-event BK inequality: if `C ⊆ ⋃ i ∈ s, P i □ (Q i □ R i)` with
all events increasing and depending on a common finite window, then
`P_p(C) ≤ ∑ i ∈ s, P_p(P i) * P_p(Q i) * P_p(R i)`.

Formalized by `StatMech.ibk_criterion_of_finite_dependsOn`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteBK.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/InfiniteBK.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#ibk-criterion-of-finite-depends-on).

## Increasing-event probabilities are monotone in the parameter

Monotonicity in the parameter: for an increasing event `A` depending only on a finite set of
coordinates and `p ≤ q`, `P_p(A) ≤ P_q(A)`. The proof uses Russo's formula.

Formalized by `StatMech.ibk_measure_mono_parameter`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InfiniteBK.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/InfiniteBK.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#ibk-measure-mono-parameter).

## Inhomogeneous Bernoulli product measure

The product measure on `ConfigSpace E` under which coordinate `e` is open (`true`) with
probability `p e`, independently.

Formalized by `StatMech.inhomBernoulliProductMeasure`, a definition declared in [MathlibExt/Probability/CorrelationInequalities/InhomogeneousBK.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/InhomogeneousBK.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#inhom-bernoulli-product-measure).

## Inhomogeneous Bernoulli product with constant parameter

For a constant parameter, the inhomogeneous product is `bernoulliProductMeasure`.

Formalized by `StatMech.inhomBernoulliProductMeasure_const`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InhomogeneousBK.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/InhomogeneousBK.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#inhom-bernoulli-product-measure-const).

## BK inequality for inhomogeneous Bernoulli measures on a finite set

The **BK inequality** for an inhomogeneous Bernoulli product measure on a finite set.

Formalized by `StatMech.inhom_bk_inequality`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InhomogeneousBK.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/InhomogeneousBK.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#inhom-bk-inequality).

## BK inequality for inhomogeneous measures on a countable set

The BK inequality for an inhomogeneous Bernoulli product measure on a countable set, for
increasing events depending on finitely many coordinates.

Formalized by `StatMech.inhom_bk_of_finite_dependsOn`, a theorem declared in [MathlibExt/Probability/CorrelationInequalities/InhomogeneousBK.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/CorrelationInequalities/InhomogeneousBK.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#inhom-bk-of-finite-depends-on).

## BK criterion for Bernoulli product measures

The BK criterion: if `C ⊆ ⋃_i P_i ∘ Q_i ∘ R_i` with increasing events, then `P_p(C) ≤ ∑_i
P_p(P_i) P_p(Q_i) P_p(R_i)` for the Bernoulli product measure. Reference: J. van den Berg, H.
Kesten, "Inequalities with applications to percolation and reliability", J. Appl. Probab. 22 (1985)
556–569.

Formalized by `StatMech.Sharpness.bk_criterion`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkCriterion.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkCriterion.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#bk-criterion).

## Open subgraph of a configuration

The subgraph of `G` of edges open in the configuration `ω`.

Formalized by `StatMech.Sharpness.openSub`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkCriterion.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkCriterion.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#open-sub).

## Open connection between two vertices inside a set

`x` and `y` are joined by an open path staying in `A`.

Formalized by `StatMech.Sharpness.ConnWithin`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkCriterion.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkCriterion.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#conn-within).

## Open connection inside a set to a target set

`u ∈ A` is joined by an open path in `A` to some vertex of `A ∩ B`.

Formalized by `StatMech.Sharpness.ConnToSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkCriterion.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkCriterion.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#conn-to-set).

## Connection event inside a set

The event that `u` is connected to `B` by an open path inside `A`.

Formalized by `StatMech.Sharpness.connEvent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkCriterion.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkCriterion.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#conn-event).

## Event that an edge is open

The event that the edge `{x, y}` is open.

Formalized by `StatMech.Sharpness.edgeOpenEvent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkCriterion.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkCriterion.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#edge-open-event).

## Ordered boundary pairs of a set

The ordered pairs `(x, y)` with `x ∈ S`, `y ∉ S` adjacent in `G`.

Formalized by `StatMech.Sharpness.shk_boundaryPairs`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkFirstExit.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkFirstExit.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#shk-boundary-pairs).

## Edge law of inhomogeneous bond percolation

The edge law of inhomogeneous bond percolation: open with probability `1 - exp(-βJ_e)`, closed
with probability `exp(-βJ_e)`.

Formalized by `StatMech.Sharpness.shk_edgeLaw`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkInhomogeneous.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkInhomogeneous.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#shk-edge-law).

## Support of the first-exit decomposition events

The edges inside `S`, the boundary edges of `S`, and the edges inside the window `Λ`: the
support of the events in the first-exit decomposition.

Formalized by `StatMech.Sharpness.shk_firstExitSupport`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkLattice.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/BkLattice.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html#shk-first-exit-support).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Van den Berg–Kesten inequality](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/correlation-inequalities/harris-fkg-bk/van-den-berg-kesten-inequality)

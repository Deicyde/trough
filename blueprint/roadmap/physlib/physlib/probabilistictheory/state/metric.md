---
declaration: module
origin: cited
lean: ProbabilisticTheory.State.apply_le_one, ProbabilisticTheory.State.apply_le_orderUnitNorm, ProbabilisticTheory.State.abs_apply_le_orderUnitNorm, ProbabilisticTheory.State.abs_apply_sub_apply_le_two, ProbabilisticTheory.State.dist_bddAbove, ProbabilisticTheory.State.instNonemptyOrderUnitBall, ProbabilisticTheory.State.dist, ProbabilisticTheory.State.dist_nonneg
statement: formalized
proof: formalized
---

# The metric space of states (Physlib)

The module `Physlib.ProbabilisticTheory.State.Metric`, [Physlib/ProbabilisticTheory/State/Metric.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean): 18 declarations, 16 with a docstring.

> The operator-norm distance between states and their distance to the set of pure states.

## i. Overview

> A state is just a positive linear functional — no continuity is assumed. It turns out to be
> automatically bounded: `|ω A| ≤ ‖A‖`. Physically, a state can never predict
> an expectation value bigger than what the observable itself can read.
>
> That bound induces a genuine operator-norm distance between states, `dist`, making `P.State` a
> `MetricSpace`. It also defines `distToPure`, the infimum distance to the set of pure states.

## ii. Key results

> - `ProbabilisticTheory.State.abs_apply_le_orderUnitNorm` : a state's values are bounded by the
>   order-unit norm.
> - `ProbabilisticTheory.State.dist` : the operator-norm distance between states.
> - `ProbabilisticTheory.State.distToPure` : a state's infimum distance to the set of pure states.

## iv. References

## A. States are bounded by the order-unit norm

**`ProbabilisticTheory.State.apply_le_one`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L60).

> A state takes values at most `1` on observables bounded by the unit.

```lean
lemma apply_le_one (ω : P.State) {A : P.Observables} (hA : A ≤ 1) : ω A ≤ 1
```

**`ProbabilisticTheory.State.apply_le_orderUnitNorm`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L64).

> A state never overshoots the order-unit norm.

```lean
lemma apply_le_orderUnitNorm (ω : P.State) (A : P.Observables) : ω A ≤ orderUnitNorm A
```

**`ProbabilisticTheory.State.abs_apply_le_orderUnitNorm`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L68).

> A state's values are bounded by the order-unit norm in both directions.

```lean
lemma abs_apply_le_orderUnitNorm (ω : P.State) (A : P.Observables) : |ω A| ≤ orderUnitNorm A
```

**`ProbabilisticTheory.State.abs_apply_sub_apply_le_two`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L74).

> Two states' predictions on any observable of order-unit norm at most `1` never differ by more
> than `2`.

```lean
lemma abs_apply_sub_apply_le_two (ω φ : P.State) {A : P.Observables} (hA : orderUnitNorm A ≤ 1) :
    |ω A - φ A| ≤ 2
```

## B. The state metric

**`ProbabilisticTheory.State.dist_bddAbove`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L86).

> The values `|ω A - φ A|` of two states, restricted to the order-unit-norm unit ball, are
> bounded by `2`.

```lean
lemma dist_bddAbove (ω φ : P.State) :
    BddAbove (Set.range fun A : {A : P.Observables // orderUnitNorm A ≤ 1} => |ω A - φ A|)
```

**`ProbabilisticTheory.State.instNonemptyOrderUnitBall`**, an instance, [line 90](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L90).

```lean
instance instNonemptyOrderUnitBall : Nonempty {A : P.Observables // orderUnitNorm A ≤ 1}
```

**`ProbabilisticTheory.State.dist`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L95).

> The operator-norm distance between two states: how far apart their predictions can get on an
> observable of order-unit norm at most `1`.

```lean
noncomputable def dist (ω φ : P.State) : ℝ
```

**`ProbabilisticTheory.State.dist_nonneg`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L99).

> Distances between states are nonnegative.

```lean
lemma dist_nonneg (ω φ : P.State) : 0 ≤ dist ω φ
```

**`ProbabilisticTheory.State.dist_le_two`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L103).

> The whole state space has diameter at most `2`: it's a bounded metric space.

```lean
lemma dist_le_two (ω φ : P.State) : dist ω φ ≤ 2
```

**`ProbabilisticTheory.State.dist_self`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L107).

```lean
lemma dist_self (ω : P.State) : dist ω ω = 0
```

**`ProbabilisticTheory.State.dist_comm`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L111).

> The state distance is symmetric.

```lean
lemma dist_comm (ω φ : P.State) : dist ω φ = dist φ ω
```

**`ProbabilisticTheory.State.dist_triangle`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L115).

> The state distance satisfies the triangle inequality.

```lean
lemma dist_triangle (ω φ ψ : P.State) : dist ω ψ ≤ dist ω φ + dist φ ψ
```

**`ProbabilisticTheory.State.eq_of_dist_eq_zero`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L120).

> `dist` separates states: two states at distance `0` are equal.

```lean
lemma eq_of_dist_eq_zero {ω φ : P.State} (h : dist ω φ = 0) : ω = φ
```

**`ProbabilisticTheory.State.apply_effectEquiv`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L130).

> A state's value at a doubled, re-centered effect (`effectEquiv`) is twice its value at
> the effect, minus one.

```lean
lemma apply_effectEquiv (ψ : P.State) (e : P.Effect) :
    ψ (effectEquiv e) = 2 * ψ e - 1
```

**`ProbabilisticTheory.State.instMetricSpace`**, an instance, [line 135](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L135).

> States, metrized by the operator norm induced by the order-unit norm on the observables.

```lean
noncomputable instance instMetricSpace : MetricSpace P.State
```

## C. Distance to pure states

**`ProbabilisticTheory.State.distToPure`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L149).

> The infimum distance to the set of pure states, using `Metric.infDist`.

```lean
noncomputable def distToPure (ω : P.State) : ℝ
```

**`ProbabilisticTheory.State.distToPure_nonneg`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L153).

> The distance to the set of pure states is nonnegative.

```lean
lemma distToPure_nonneg (ω : P.State) : 0 ≤ distToPure ω
```

**`ProbabilisticTheory.State.distToPure_eq_zero_of_isPure`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean#L157).

> A pure state is at distance `0` from the set of pure states.

```lean
lemma distToPure_eq_zero_of_isPure {ω : P.State} (h : IsPure ω) : distToPure ω = 0
```

## Depends on

- [The metric space of effects (Physlib)](../effect/metric.md)
- [Convex state spaces (Physlib)](convex.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Metric.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Metric.lean)

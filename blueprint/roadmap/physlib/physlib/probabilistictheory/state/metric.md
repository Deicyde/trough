---
declaration: module
origin: cited
lean: UnitalPositiveLinearMap.apply_le_one, UnitalPositiveLinearMap.apply_le_orderUnitNorm, UnitalPositiveLinearMap.abs_apply_le_orderUnitNorm, UnitalPositiveLinearMap.abs_apply_sub_apply_le_two, UnitalPositiveLinearMap.dist_bddAbove, UnitalPositiveLinearMap.instNonemptyOrderUnitBall, UnitalPositiveLinearMap.dist, UnitalPositiveLinearMap.dist_nonneg
statement: formalized
proof: formalized
---

# The metric space of states (Physlib)

The module `Physlib.ProbabilisticTheory.State.Metric`, [Physlib/ProbabilisticTheory/State/Metric.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean): 18 declarations, 16 with a docstring.

> The operator-norm distance between states and their distance to the set of pure states.

## i. Overview

> A state is just a positive linear functional — no continuity is assumed. It turns out to be
> automatically bounded: `|ω A| ≤ ‖A‖`. Physically, a state can never predict
> an expectation value bigger than what the observable itself can read.
>
> That bound induces a genuine operator-norm distance between states, `dist`, making `𝓢[ℝ, E]` a
> `MetricSpace`. It also defines `distToPure`, the infimum distance to the set of pure states.

## ii. Key results

> - `UnitalPositiveLinearMap.abs_apply_le_orderUnitNorm` : a state's values are bounded by the
>   order-unit norm.
> - `UnitalPositiveLinearMap.dist` : the operator-norm distance between states.
> - `UnitalPositiveLinearMap.distToPure` : a state's infimum distance to the set of pure states.

## iv. References

## A. States are bounded by the order-unit norm

**`UnitalPositiveLinearMap.apply_le_one`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L60).

> A state takes values at most `1` on observables bounded by the unit.

```lean
lemma apply_le_one {F : Type*} [OrderUnitSpace F] (ω : 𝓢[ℝ, F]) {A : F} (hA : A ≤ 1) :
    ω A ≤ 1
```

**`UnitalPositiveLinearMap.apply_le_orderUnitNorm`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L65).

> A state never overshoots the order-unit norm.

```lean
lemma apply_le_orderUnitNorm (ω : 𝓢[ℝ, E]) (A : E) : ω A ≤ orderUnitNorm A
```

**`UnitalPositiveLinearMap.abs_apply_le_orderUnitNorm`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L69).

> A state's values are bounded by the order-unit norm in both directions.

```lean
lemma abs_apply_le_orderUnitNorm (ω : 𝓢[ℝ, E]) (A : E) : |ω A| ≤ orderUnitNorm A
```

**`UnitalPositiveLinearMap.abs_apply_sub_apply_le_two`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L75).

> Two states' predictions on any observable of order-unit norm at most `1` never differ by more
> than `2`.

```lean
lemma abs_apply_sub_apply_le_two (ω φ : 𝓢[ℝ, E]) {A : E} (hA : orderUnitNorm A ≤ 1) :
    |ω A - φ A| ≤ 2
```

## B. The state metric

**`UnitalPositiveLinearMap.dist_bddAbove`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L87).

> The values `|ω A - φ A|` of two states, restricted to the order-unit-norm unit ball, are
> bounded by `2`.

```lean
lemma dist_bddAbove (ω φ : 𝓢[ℝ, E]) :
    BddAbove (Set.range fun A : {A : E // orderUnitNorm A ≤ 1} => |ω A - φ A|)
```

**`UnitalPositiveLinearMap.instNonemptyOrderUnitBall`**, an instance, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L91).

```lean
instance instNonemptyOrderUnitBall : Nonempty {A : E // orderUnitNorm A ≤ 1}
```

**`UnitalPositiveLinearMap.dist`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L95).

> The operator-norm distance between two states: how far apart their predictions can get on an
> observable of order-unit norm at most `1`.

```lean
noncomputable def dist (ω φ : 𝓢[ℝ, E]) : ℝ
```

**`UnitalPositiveLinearMap.dist_nonneg`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L99).

> Distances between states are nonnegative.

```lean
lemma dist_nonneg (ω φ : 𝓢[ℝ, E]) : 0 ≤ dist ω φ
```

**`UnitalPositiveLinearMap.dist_le_two`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L103).

> The whole state space has diameter at most `2`: it's a bounded metric space.

```lean
lemma dist_le_two (ω φ : 𝓢[ℝ, E]) : dist ω φ ≤ 2
```

**`UnitalPositiveLinearMap.dist_self`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L107).

```lean
lemma dist_self (ω : 𝓢[ℝ, E]) : dist ω ω = 0
```

**`UnitalPositiveLinearMap.dist_comm`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L111).

> The state distance is symmetric.

```lean
lemma dist_comm (ω φ : 𝓢[ℝ, E]) : dist ω φ = dist φ ω
```

**`UnitalPositiveLinearMap.dist_triangle`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L115).

> The state distance satisfies the triangle inequality.

```lean
lemma dist_triangle (ω φ ψ : 𝓢[ℝ, E]) : dist ω ψ ≤ dist ω φ + dist φ ψ
```

**`UnitalPositiveLinearMap.eq_of_dist_eq_zero`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L120).

> `dist` separates states: two states at distance `0` are equal.

```lean
lemma eq_of_dist_eq_zero {ω φ : 𝓢[ℝ, E]} (h : dist ω φ = 0) : ω = φ
```

**`UnitalPositiveLinearMap.apply_effectEquiv`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L130).

> A state's value at a doubled, re-centered effect (`effectEquiv`) is twice its value at
> the effect, minus one.

```lean
lemma apply_effectEquiv (ψ : 𝓢[ℝ, E]) (e : Effect E) :
    ψ (effectEquiv e) = 2 * ψ e - 1
```

**`UnitalPositiveLinearMap.instMetricSpace`**, an instance, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L135).

> States, metrized by the operator norm induced by the order-unit norm on `E`.

```lean
noncomputable instance instMetricSpace : MetricSpace (𝓢[ℝ, E])
```

## C. Distance to pure states

**`UnitalPositiveLinearMap.distToPure`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L149).

> The infimum distance to the set of pure states, using `Metric.infDist`.

```lean
noncomputable def distToPure (ω : 𝓢[ℝ, E]) : ℝ
```

**`UnitalPositiveLinearMap.distToPure_nonneg`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L153).

> The distance to the set of pure states is nonnegative.

```lean
lemma distToPure_nonneg (ω : 𝓢[ℝ, E]) : 0 ≤ distToPure ω
```

**`UnitalPositiveLinearMap.distToPure_eq_zero_of_isPure`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean#L157).

> A pure state is at distance `0` from the set of pure states.

```lean
lemma distToPure_eq_zero_of_isPure {ω : 𝓢[ℝ, E]} (h : IsPure ω) : distToPure ω = 0
```

## Depends on

- [The metric space of effects](../effect/metric.md)
- [Convex state spaces (Physlib)](convex.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Metric.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Metric.lean)

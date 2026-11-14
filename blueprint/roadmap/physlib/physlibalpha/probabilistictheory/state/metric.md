---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.apply_le_orderUnitNorm, ProbabilisticTheory.UnitalPositiveLinearMap.abs_apply_le_orderUnitNorm, ProbabilisticTheory.UnitalPositiveLinearMap.abs_apply_sub_apply_le_two, ProbabilisticTheory.UnitalPositiveLinearMap.dist_bddAbove, ProbabilisticTheory.UnitalPositiveLinearMap.dist, ProbabilisticTheory.UnitalPositiveLinearMap.dist_nonneg, ProbabilisticTheory.UnitalPositiveLinearMap.dist_le_two, ProbabilisticTheory.UnitalPositiveLinearMap.dist_self
statement: formalized
proof: formalized
---

# The metric space of states (PhyslibAlpha)

The module `PhyslibAlpha.ProbabilisticTheory.State.Metric`, [PhyslibAlpha/ProbabilisticTheory/State/Metric.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean): 18 declarations (2 instances with no name), 12 with a docstring.

> States are bounded by the order-unit norm, giving a metric on states and a distance to purity.

## i. Overview

> A state is just a positive linear functional — no continuity is assumed. It turns out to be
> automatically bounded: `|ω A| ≤ ‖A‖`. Physically, a state can never predict
> an expectation value bigger than what the observable itself can read.
>
> That bound induces an operator-norm distance between states, `dist`, making `𝓢[ℝ, E]` a
> `MetricSpace`. That in turn gives a notion of how mixed a state is: `distToPure`, its infimum
> distance to the set of pure states.

## ii. Key results

> - `UnitalPositiveLinearMap.abs_apply_le_orderUnitNorm` : a state's values are bounded by the
>   order-unit norm.
> - `UnitalPositiveLinearMap.dist` : the operator-norm distance between states.
> - `UnitalPositiveLinearMap.distToPure` : a state's infimum distance to the set of pure states.

## iv. References

> * None.

## A. States are bounded by the order-unit norm

**`ProbabilisticTheory.UnitalPositiveLinearMap.apply_le_orderUnitNorm`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L63).

> A state never overshoots the order-unit norm.

```lean
lemma apply_le_orderUnitNorm (ω : 𝓢[ℝ, E]) (A : E) : ω A ≤ orderUnitNorm A
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.abs_apply_le_orderUnitNorm`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L72).

> A state's values are bounded by the order-unit norm in both directions.

```lean
lemma abs_apply_le_orderUnitNorm (ω : 𝓢[ℝ, E]) (A : E) : |ω A| ≤ orderUnitNorm A
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.abs_apply_sub_apply_le_two`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L80).

> Two states' predictions on any observable of order-unit norm at most `1` never differ by more
> than `2`.

```lean
lemma abs_apply_sub_apply_le_two (ω φ : 𝓢[ℝ, E]) {A : E} (hA : orderUnitNorm A ≤ 1) :
    |ω A - φ A| ≤ 2
```

## B. The state metric

**`ProbabilisticTheory.UnitalPositiveLinearMap.dist_bddAbove`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L92).

> The values `|ω A - φ A|` of two states, restricted to the order-unit-norm unit ball, are
> bounded by `2`.

```lean
lemma dist_bddAbove (ω φ : 𝓢[ℝ, E]) :
    BddAbove (Set.range fun A : {A : E // orderUnitNorm A ≤ 1} => |ω A - φ A|)
```

**An instance with no name**, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L96).

```lean
instance : Nonempty {A : E // orderUnitNorm A ≤ 1}
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.dist`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L100).

> The operator-norm distance between two states: how far apart their predictions can get on an
> observable of order-unit norm at most `1`.

```lean
noncomputable def dist (ω φ : 𝓢[ℝ, E]) : ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.dist_nonneg`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L103).

```lean
lemma dist_nonneg (ω φ : 𝓢[ℝ, E]) : 0 ≤ dist ω φ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.dist_le_two`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L107).

> The whole state space has diameter at most `2`: it's a bounded metric space.

```lean
lemma dist_le_two (ω φ : 𝓢[ℝ, E]) : dist ω φ ≤ 2
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.dist_self`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L111).

```lean
lemma dist_self (ω : 𝓢[ℝ, E]) : dist ω ω = 0
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.dist_comm`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L114).

```lean
lemma dist_comm (ω φ : 𝓢[ℝ, E]) : dist ω φ = dist φ ω
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.dist_triangle`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L118).

```lean
lemma dist_triangle (ω φ ψ : 𝓢[ℝ, E]) : dist ω ψ ≤ dist ω φ + dist φ ψ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.eq_of_dist_eq_zero`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L126).

> `dist` separates states: two states at distance `0` are equal.

```lean
lemma eq_of_dist_eq_zero {ω φ : 𝓢[ℝ, E]} (h : dist ω φ = 0) : ω = φ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.apply_effectEquiv`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L137).

> A state's value at a doubled, re-centered effect (`Effect.effectEquiv`) is twice its value at
> the effect, minus one.

```lean
lemma apply_effectEquiv (ψ : 𝓢[ℝ, E]) (e : Effect E) :
    ψ ((Effect.effectEquiv e : E)) = 2 * ψ (e : E) - 1
```

**An instance with no name**, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L143).

> States, metrized by the operator norm induced by the order-unit norm on `E`.

```lean
noncomputable instance : MetricSpace (𝓢[ℝ, E])
```

## C. Distance to pure states

**`ProbabilisticTheory.UnitalPositiveLinearMap.distToPure`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L157).

> How mixed a state is: its infimum distance to the set of pure states.

```lean
noncomputable def distToPure (ω : 𝓢[ℝ, E]) : ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.distToPure_nonneg`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L160).

```lean
lemma distToPure_nonneg (ω : 𝓢[ℝ, E]) : 0 ≤ distToPure ω
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.distToPure_eq_zero_of_isPure`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L164).

> A pure state is at distance `0` from the set of pure states.

```lean
lemma distToPure_eq_zero_of_isPure {ω : 𝓢[ℝ, E]} (h : IsPure ω) : distToPure ω = 0
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.lipschitzWith_distToPure`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean#L168).

> `distToPure` is `1`-Lipschitz: states close in `dist` are similarly mixed.

```lean
lemma lipschitzWith_distToPure : LipschitzWith 1 (distToPure (E := E))
```

## Depends on

- [The metric space of effects](../../../physlib/probabilistictheory/effect/metric.md)
- [Convex state spaces (PhyslibAlpha)](convex.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/State/Metric.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Metric.lean)

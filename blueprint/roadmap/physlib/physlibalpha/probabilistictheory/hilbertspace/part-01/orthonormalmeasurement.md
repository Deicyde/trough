---
declaration: module
origin: cited
lean: ProbabilisticTheory.inner_rankOne_self_apply, ProbabilisticTheory.inner_sum_rankOne_self_apply, ProbabilisticTheory.isPositive_one_sub_sum_rankOne, ProbabilisticTheory.rankOneObservable, ProbabilisticTheory.coe_rankOneObservable, ProbabilisticTheory.rankOneObservable_nonneg, ProbabilisticTheory.orthonormalObservable, ProbabilisticTheory.coe_orthonormalObservable
statement: formalized
proof: formalized
---

# Measurements in an orthonormal family

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.OrthonormalMeasurement`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean): 15 declarations, 13 with a docstring.

> The measurement of a quantum system on a complex Hilbert space in a finite orthonormal family.

## i. Overview

> Let `b x`, for `x` in a finite type `X`, be orthonormal vectors of a complex Hilbert space `H`.
> The rank-one projections `|b x⟩⟨b x|` are effects, and by Bessel's inequality their sum is at most
> `1`. Adding the remainder `1 - ∑ x, |b x⟩⟨b x|` to the effect of a chosen outcome `x₀` gives a
> measurement with outcomes `X`. On a unit vector `φ`, the outcome `x` has probability
> `‖⟪b x, φ⟫‖ ^ 2`, plus `1 - ∑ y, ‖⟪b y, φ⟫‖ ^ 2` when `x = x₀`. In particular, if `φ` lies in the
> span of the `b x`, the outcome `x` has probability `‖⟪b x, φ⟫‖ ^ 2`.

## ii. Key results

> - `rankOneObservable` : the rank-one observable `|v⟩⟨v|`.
> - `orthonormalObservable` : the observable of an outcome, `|b x⟩⟨b x|` plus the remainder on `x₀`.
> - `sum_orthonormalObservable`, `orthonormalObservable_nonneg` : the outcome observables are
>   positive and add up to `1`.
> - `Measurement.ofOrthonormal` : the measurement in an orthonormal family.
> - `Measurement.expectation_ofOrthonormal_singleton` : the Born rule for this measurement.

## iv. References

> * None.

## A. Rank-one observables

**`ProbabilisticTheory.inner_rankOne_self_apply`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L65).

> `⟪φ, |v⟩⟨v| φ⟫ = ‖⟪v, φ⟫‖ ^ 2`.

```lean
lemma inner_rankOne_self_apply (v φ : H) :
    ⟪φ, rankOne ℂ v v φ⟫_ℂ = (‖⟪v, φ⟫_ℂ‖ ^ 2 : ℝ)
```

**`ProbabilisticTheory.inner_sum_rankOne_self_apply`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L71).

> `⟪φ, ∑ y, |b y⟩⟨b y| φ⟫ = ∑ y, ‖⟪b y, φ⟫‖ ^ 2`.

```lean
lemma inner_sum_rankOne_self_apply (b : X → H) (φ : H) :
    ⟪φ, (∑ y, rankOne ℂ (b y) (b y)) φ⟫_ℂ = (∑ y, ‖⟪b y, φ⟫_ℂ‖ ^ 2 : ℝ)
```

**`ProbabilisticTheory.isPositive_one_sub_sum_rankOne`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L77).

> By Bessel's inequality, `1 - ∑ y, |b y⟩⟨b y|` is positive for an orthonormal family `b`.

```lean
lemma isPositive_one_sub_sum_rankOne {b : X → H} (hb : Orthonormal ℂ b) :
    (1 - ∑ y, rankOne ℂ (b y) (b y)).IsPositive
```

**`ProbabilisticTheory.rankOneObservable`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L94).

> The rank-one observable `|v⟩⟨v|`.

```lean
noncomputable def rankOneObservable (v : H) : Observable (H →L[ℂ] H)
```

**`ProbabilisticTheory.coe_rankOneObservable`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L98).

```lean
lemma coe_rankOneObservable (v : H) :
    (rankOneObservable v : H →L[ℂ] H) = rankOne ℂ v v
```

**`ProbabilisticTheory.rankOneObservable_nonneg`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L102).

> The rank-one observable `|v⟩⟨v|` is positive.

```lean
lemma rankOneObservable_nonneg (v : H) : 0 ≤ rankOneObservable v
```

## B. The outcome observables

**`ProbabilisticTheory.orthonormalObservable`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L115).

> The observable of the outcome `x` in the measurement in the family `b`: `|b x⟩⟨b x|`, plus
> the remainder `1 - ∑ y, |b y⟩⟨b y|` when `x = x₀`.

```lean
noncomputable def orthonormalObservable (b : X → H) (x₀ x : X) : Observable (H →L[ℂ] H)
```

**`ProbabilisticTheory.coe_orthonormalObservable`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L119).

> The operator underlying the observable of the outcome `x`.

```lean
lemma coe_orthonormalObservable (b : X → H) (x₀ x : X) :
    (orthonormalObservable b x₀ x : H →L[ℂ] H) =
      rankOne ℂ (b x) (b x) + if x = x₀ then 1 - ∑ y, rankOne ℂ (b y) (b y) else 0
```

**`ProbabilisticTheory.sum_orthonormalObservable`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L125).

> The outcome observables add up to `1`.

```lean
lemma sum_orthonormalObservable (b : X → H) (x₀ : X) :
    ∑ x, orthonormalObservable b x₀ x = 1
```

**`ProbabilisticTheory.orthonormalObservable_nonneg`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L130).

> The outcome observables of an orthonormal family are positive.

```lean
lemma orthonormalObservable_nonneg {b : X → H} (hb : Orthonormal ℂ b) (x₀ x : X) :
    0 ≤ orthonormalObservable b x₀ x
```

**`ProbabilisticTheory.orthonormalEffect`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L141).

> The outcome effects of the measurement in an orthonormal family.

```lean
noncomputable def orthonormalEffect {b : X → H} (hb : Orthonormal ℂ b) (x₀ x : X) :
    Effect (Observable (H →L[ℂ] H))
```

**`ProbabilisticTheory.coe_orthonormalEffect`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L148).

```lean
lemma coe_orthonormalEffect {b : X → H} (hb : Orthonormal ℂ b) (x₀ x : X) :
    (orthonormalEffect hb x₀ x : Observable (H →L[ℂ] H)) = orthonormalObservable b x₀ x
```

## C. The measurement and its Born rule

**`ProbabilisticTheory.Measurement.ofOrthonormal`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L164).

> The measurement in the orthonormal family `b`: the outcome `x` has effect `|b x⟩⟨b x|`, and
> the outcome `x₀` also registers the orthogonal complement of the span of the family.

```lean
noncomputable def ofOrthonormal {b : X → H} (hb : Orthonormal ℂ b) (x₀ : X) :
    Measurement X (Observable (H →L[ℂ] H))
```

**`ProbabilisticTheory.Measurement.coe_ofOrthonormal_singleton`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L170).

> The outcome `x` of the measurement in an orthonormal family has the observable
> `orthonormalObservable b x₀ x`.

```lean
lemma coe_ofOrthonormal_singleton {b : X → H} (hb : Orthonormal ℂ b) (x₀ x : X)
    (hx : MeasurableSet {x}) :
    (ofOrthonormal hb x₀ {x} hx : Observable (H →L[ℂ] H)) = orthonormalObservable b x₀ x
```

**`ProbabilisticTheory.Measurement.expectation_ofOrthonormal_singleton`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean#L177).

> The Born rule for the measurement in an orthonormal family: on a unit vector `φ`, the
> outcome `x` has probability `‖⟪b x, φ⟫‖ ^ 2`, plus `1 - ∑ y, ‖⟪b y, φ⟫‖ ^ 2` when `x = x₀`.

```lean
lemma expectation_ofOrthonormal_singleton [MeasurableSingletonClass X] {b : X → H}
    (hb : Orthonormal ℂ b) (x₀ : X) {φ : H} (hφ : ‖φ‖ = 1) (x : X) :
    (ofVec hφ)⟨ofOrthonormal hb x₀ {x} (measurableSet_singleton x)⟩ =
      ‖⟪b x, φ⟫_ℂ‖ ^ 2 + if x = x₀ then 1 - ∑ y, ‖⟪b y, φ⟫_ℂ‖ ^ 2 else 0
```

## Depends on

- [The observables of a C⋆-algebra](../../../../physlib/probabilistictheory/cstaralgebra/orderunit.md)
- [Vector states](state-vector.md)
- [Measurements with finitely many outcomes](../../measurement/finite.md)
- [Expectation, variance and covariance](../../staralgebra/statistics.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/OrthonormalMeasurement.lean)

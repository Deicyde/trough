---
declaration: module
origin: cited
lean: LinearPMap.variance, LinearPMap.variance_eq_centered_norm_sq, LinearPMap.variance_eq_norm_sub_sq, LinearPMap.variance_eq_norm_sq_sub_expectedValue_sq, LinearPMap.variance_nonneg, LinearPMap.variance_eq_zero_iff_centered_eq_zero, LinearPMap.variance_eq_zero_iff, LinearPMap.variance_eq_zero_iff_isEigenvector
statement: formalized
proof: formalized
---

# Variance and standard deviation

The module `Physlib.QuantumMechanics.Operators.StateObservables.Variance`, [Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean): 17 declarations, 16 with a docstring.

> The variance of a partial linear map `T` in a state `ψ` is `‖Tψ - ⟨T⟩_ψ ψ‖ ^ 2`. It only
> requires `ψ ∈ T.domain`.
>
> When `T` is symmetric, `‖ψ‖ = 1`, and `Tψ ∈ T.domain`, it also equals `⟨T^2⟩_ψ - ⟨T⟩_ψ ^ 2`.

## Main definitions

> - `LinearPMap.variance` and `LinearPMap.standardDeviation`.

## Main statements

> - `LinearPMap.variance_eq_norm_sq_sub_expectedValue_sq`: for a unit vector and symmetric `T`,
>   the variance is `‖Tψ‖ ^ 2 - ⟨T⟩_ψ ^ 2`.
> - `LinearPMap.variance_eq_re_inner_sub_expectedValue_sq`: the second-order formula when
> `Tψ ∈ T.domain`.
> - `LinearPMap.variance_eq_zero_iff_isEigenvector` and
>   `LinearPMap.standardDeviation_eq_zero_iff_isEigenvector`: for a unit vector, zero variance or
>   standard deviation is equivalent to the eigenvector condition.

## References

> * B. C. Hall, Quantum Theory for Mathematicians, Chapter 12. [ref: hall2013quantum]

**`LinearPMap.variance`**, a def, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L48).

> Variance `‖Tψ - ⟨T⟩_ψ ψ‖ ^ 2`; only `ψ ∈ T.domain` is required.

```lean
def variance (T : H →ₗ.[ℂ] H) (ψ : T.domain) : ℝ
```

**`LinearPMap.variance_eq_centered_norm_sq`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L52).

> The variance is the squared norm of the centered vector.

```lean
lemma variance_eq_centered_norm_sq (T : H →ₗ.[ℂ] H) (ψ : T.domain) :
    variance T ψ = ‖centered T ψ‖ ^ 2
```

**`LinearPMap.variance_eq_norm_sub_sq`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L57).

> `variance` with `centered` unfolded to `Tψ - ⟨T⟩_ψ • ψ`.

```lean
lemma variance_eq_norm_sub_sq (T : H →ₗ.[ℂ] H) (ψ : T.domain) :
    variance T ψ =
      ‖T ψ - (expectedValue T ψ : ℂ) • (ψ : H)‖ ^ 2
```

**`LinearPMap.variance_eq_norm_sq_sub_expectedValue_sq`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L63).

> For symmetric `T` and `‖ψ‖ = 1`, variance equals `‖Tψ‖ ^ 2 - ⟨T⟩_ψ ^ 2`.

```lean
lemma variance_eq_norm_sq_sub_expectedValue_sq (T : H →ₗ.[ℂ] H)
    (hT : T.IsSymmetric) (ψ : T.domain) (hψ_norm : ‖(ψ : H)‖ = 1) :
    variance T ψ = ‖T ψ‖ ^ 2 - expectedValue T ψ ^ 2
```

**`LinearPMap.variance_nonneg`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L88).

> Variance is nonnegative.

```lean
lemma variance_nonneg (T : H →ₗ.[ℂ] H) (ψ : T.domain) :
    0 ≤ variance T ψ
```

**`LinearPMap.variance_eq_zero_iff_centered_eq_zero`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L94).

> Zero variance is the same as a zero centered vector.

```lean
lemma variance_eq_zero_iff_centered_eq_zero (T : H →ₗ.[ℂ] H) (ψ : T.domain) :
    variance T ψ = 0 ↔ centered T ψ = 0
```

**`LinearPMap.variance_eq_zero_iff`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L100).

> Zero variance is the same as `Tψ = ⟨T⟩_ψ ψ`.

```lean
lemma variance_eq_zero_iff (T : H →ₗ.[ℂ] H) (ψ : T.domain) :
    variance T ψ = 0 ↔ T ψ = (expectedValue T ψ : ℂ) • (ψ : H)
```

**`LinearPMap.variance_eq_zero_iff_isEigenvector`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L105).

> For `‖ψ‖ = 1`, zero variance iff `ψ` is an eigenvector with eigenvalue `⟨T⟩_ψ`.

```lean
lemma variance_eq_zero_iff_isEigenvector (T : H →ₗ.[ℂ] H)
    (ψ : T.domain) (hψ_norm : ‖(ψ : H)‖ = 1) :
    variance T ψ = 0 ↔
      T.IsEigenvector ψ (expectedValue T ψ : ℂ)
```

**`LinearPMap.standardDeviation`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L122).

> Standard deviation `√(variance)` for `ψ ∈ T.domain`.

```lean
def standardDeviation (T : H →ₗ.[ℂ] H) (ψ : T.domain) : ℝ
```

**`LinearPMap.standardDeviation_eq_sqrt_variance`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L126).

> The standard deviation, unfolded to the square root of the variance.

```lean
lemma standardDeviation_eq_sqrt_variance (T : H →ₗ.[ℂ] H) (ψ : T.domain) :
    standardDeviation T ψ = Real.sqrt (variance T ψ)
```

**`LinearPMap.standardDeviation_nonneg`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L131).

> Standard deviation is nonnegative.

```lean
lemma standardDeviation_nonneg (T : H →ₗ.[ℂ] H) (ψ : T.domain) :
    0 ≤ standardDeviation T ψ
```

**`LinearPMap.standardDeviation_sq`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L137).

```lean
lemma standardDeviation_sq (T : H →ₗ.[ℂ] H) (ψ : T.domain) :
    standardDeviation T ψ ^ 2 = variance T ψ
```

**`LinearPMap.standardDeviation_eq_zero_iff_centered_eq_zero`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L143).

> Zero standard deviation is the same as a zero centered vector.

```lean
lemma standardDeviation_eq_zero_iff_centered_eq_zero (T : H →ₗ.[ℂ] H)
    (ψ : T.domain) :
    standardDeviation T ψ = 0 ↔ centered T ψ = 0
```

**`LinearPMap.standardDeviation_eq_zero_iff`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L151).

> Zero standard deviation is the same as `Tψ = ⟨T⟩_ψ ψ`.

```lean
lemma standardDeviation_eq_zero_iff (T : H →ₗ.[ℂ] H) (ψ : T.domain) :
    standardDeviation T ψ = 0 ↔ T ψ = (expectedValue T ψ : ℂ) • (ψ : H)
```

**`LinearPMap.standardDeviation_eq_zero_iff_isEigenvector`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L156).

> For `‖ψ‖ = 1`, zero standard deviation iff the eigenvector condition holds.

```lean
lemma standardDeviation_eq_zero_iff_isEigenvector (T : H →ₗ.[ℂ] H)
    (ψ : T.domain) (hψ_norm : ‖(ψ : H)‖ = 1) :
    standardDeviation T ψ = 0 ↔
      T.IsEigenvector ψ (expectedValue T ψ : ℂ)
```

**`LinearPMap.re_inner_apply_sq_eq_norm_sq`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L182).

> For symmetric `T`, `re ⟪ψ, T(Tψ)⟫` is `‖Tψ‖ ^ 2`.

```lean
lemma re_inner_apply_sq_eq_norm_sq :
    (⟪(ψ : H), T ⟨T ψ, hTψ⟩⟫_ℂ).re = ‖T ψ‖ ^ 2
```

**`LinearPMap.variance_eq_re_inner_sub_expectedValue_sq`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean#L191).

> When `Tψ ∈ T.domain`, variance equals `⟨T^2⟩_ψ - ⟨T⟩_ψ ^ 2`.

```lean
lemma variance_eq_re_inner_sub_expectedValue_sq :
    variance T ψ =
      (⟪(ψ : H), T ⟨T ψ, hTψ⟩⟫_ℂ).re - expectedValue T ψ ^ 2
```

## Depends on

- [Expectation values and centered vectors](stateobservables-expectedvalue.md)
- [Eigenvectors of partial linear maps](stateobservables-iseigenvector.md)

## Sources

- [Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/Variance.lean)

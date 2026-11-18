---
declaration: module
origin: cited
lean: LinearPMap.expectedValue, LinearPMap.expectedValue_eq_re_inner, LinearPMap.expectedValue_eq_inner, LinearPMap.inner_eq_expectedValue, LinearPMap.centered, LinearPMap.centered_eq, LinearPMap.centered_eq_zero_iff, LinearPMap.inner_state_centered_eq_zero
statement: formalized
proof: formalized
---

# Expectation values and centered vectors

The module `Physlib.QuantumMechanics.Operators.StateObservables.ExpectedValue`, [Physlib/QuantumMechanics/Operators/StateObservables/ExpectedValue.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/ExpectedValue.lean): 9 declarations, 9 with a docstring; 1 private, not shown.

> For a partial linear map `T` on a complex inner product space and `ψ ∈ T.domain`, this file
> defines the expectation value and the centered vector `Tψ - ⟨T⟩_ψ ψ`.

## Main definitions

> - `LinearPMap.expectedValue`: the real part of `⟪ψ, Tψ⟫_ℂ`.
> - `LinearPMap.centered`: the centered vector `Tψ - ⟨T⟩ψ`.

## Main statements

> - `LinearPMap.expectedValue_eq_inner`: for symmetric `T`, the complex inner product is real and
>   equals the real expectation value coerced to `ℂ`.

## References

> * B. C. Hall, Quantum Theory for Mathematicians, Chapter 12. [ref: hall2013quantum]

**`LinearPMap.expectedValue`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/ExpectedValue.lean#L49).

> Expectation value `re ⟪ψ, Tψ⟫_ℂ` for `ψ ∈ T.domain`.
>
> For symmetric `T`, this agrees with `⟪ψ, Tψ⟫_ℂ` after coercion from `ℝ`;
> see `expectedValue_eq_inner`.

```lean
def expectedValue (T : H →ₗ.[ℂ] H) (ψ : T.domain) : ℝ
```

**`LinearPMap.expectedValue_eq_re_inner`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/ExpectedValue.lean#L53).

> The expectation value, unfolded as a real part.

```lean
lemma expectedValue_eq_re_inner (T : H →ₗ.[ℂ] H) (ψ : T.domain) :
    expectedValue T ψ = (⟪(ψ : H), T ψ⟫_ℂ).re
```

**`LinearPMap.expectedValue_eq_inner`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/ExpectedValue.lean#L58).

> If `T` is symmetric, `⟪ψ, Tψ⟫_ℂ` is the expectation value, coerced to `ℂ`.

```lean
lemma expectedValue_eq_inner (T : H →ₗ.[ℂ] H) (hT : T.IsSymmetric) (ψ : T.domain) :
    ⟪(ψ : H), T ψ⟫_ℂ = (expectedValue T ψ : ℂ)
```

**`LinearPMap.inner_eq_expectedValue`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/ExpectedValue.lean#L66).

> Reverse orientation of `LinearPMap.expectedValue_eq_inner`.

```lean
lemma inner_eq_expectedValue (T : H →ₗ.[ℂ] H) (hT : T.IsSymmetric) (ψ : T.domain) :
    (expectedValue T ψ : ℂ) = ⟪(ψ : H), T ψ⟫_ℂ
```

**`LinearPMap.centered`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/ExpectedValue.lean#L71).

> The centered vector `Tψ - ⟨T⟩_ψ ψ`.

```lean
def centered (T : H →ₗ.[ℂ] H) (ψ : T.domain) : H
```

**`LinearPMap.centered_eq`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/ExpectedValue.lean#L75).

> The centered vector, unfolded to its raw expression.

```lean
lemma centered_eq (T : H →ₗ.[ℂ] H) (ψ : T.domain) :
    centered T ψ = T ψ - (expectedValue T ψ : ℂ) • (ψ : H)
```

**`LinearPMap.centered_eq_zero_iff`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/ExpectedValue.lean#L80).

> A centered vector vanishes exactly when `Tψ = ⟨T⟩_ψ ψ`.

```lean
lemma centered_eq_zero_iff (T : H →ₗ.[ℂ] H) (ψ : T.domain) :
    centered T ψ = 0 ↔ T ψ = (expectedValue T ψ : ℂ) • (ψ : H)
```

**`LinearPMap.inner_state_centered_eq_zero`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/ExpectedValue.lean#L85).

> For a unit vector and symmetric `T`, the centered vector is orthogonal to the state.

```lean
lemma inner_state_centered_eq_zero (T : H →ₗ.[ℂ] H) (hT : T.IsSymmetric)
    (ψ : T.domain) (hψ_norm : ‖(ψ : H)‖ = 1) :
    ⟪(ψ : H), centered T ψ⟫_ℂ = 0
```

**`LinearPMap.inner_centered_state_eq_zero`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/ExpectedValue.lean#L92).

> The conjugate orientation of `LinearPMap.inner_state_centered_eq_zero`.

```lean
lemma inner_centered_state_eq_zero (T : H →ₗ.[ℂ] H) (hT : T.IsSymmetric)
    (ψ : T.domain) (hψ_norm : ‖(ψ : H)‖ = 1) :
    ⟪centered T ψ, (ψ : H)⟫_ℂ = 0
```

## Depends on

- [Unbounded operators (Operators/Unbounded)](unbounded.md)

## Sources

- [Physlib/QuantumMechanics/Operators/StateObservables/ExpectedValue.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/StateObservables/ExpectedValue.lean)

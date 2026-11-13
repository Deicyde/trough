---
declaration: module
origin: cited
lean: LinearPMap.inner_im_of_commutator_eq, LinearPMap.inner_norm_sq_eq_re_sq_add_commutator_half_sq, LinearPMap.sub_expectation_commutator_eq_raw, LinearPMap.raw_commutator_eq_of_symmetric, LinearPMap.centeredCommutatorExpectation, LinearPMap.rawCommutatorExpectation, LinearPMap.commutator_half_sq_le_mul_norm_sq, LinearPMap.state_uncertainty_squared_of_centered_commutator
statement: formalized
proof: formalized
---

# Uncertainty bounds for partial linear maps

The module `Physlib.QuantumMechanics.Operators.Uncertainty`, [Physlib/QuantumMechanics/Operators/Uncertainty.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean): 14 declarations, 9 with a docstring; 1 private, not shown.

## i. Overview

> In this module we prove abstract Robertson and Robertson–Schrödinger uncertainty bounds for
> symmetric partial linear maps on a complex inner product space. The statements are independent of
> any concrete position or momentum operator.
>
> The centered-commutator results use only the domain assumptions needed to form the centered
> vectors. The raw-commutator results add the second-order domain hypotheses required to apply `A`
> to `Bψ` and `B` to `Aψ`.

## ii. Key results

> - `inner_im_of_commutator_eq` : an anti-Hermitian commutator identity fixes the imaginary part of
>   an inner product.
> - `centeredCommutatorExpectation` : the scalar commutator of the centered vectors.
> - `rawCommutatorExpectation` : the expectation of the raw commutator on a state.
> - `inner_centered_commutator_of_raw_commutator` : a raw commutator expectation gives the centered
>   commutator expectation.
> - `state_uncertainty_squared_of_centered_commutator` : the Robertson squared bound from a centered
>   commutator identity.
> - `state_uncertainty_squared_with_covariance_of_centered_commutator` : the strengthened
>   Robertson–Schrödinger bound.
> - `state_uncertainty_of_centered_commutator` : the standard-deviation form of the bound.
> - `state_uncertainty_squared_of_raw_commutator`,
>   `state_uncertainty_squared_with_covariance_of_raw_commutator`, and
>   `state_uncertainty_of_raw_commutator` : variants using a raw commutator expectation.

## iv. References

> * H. P. Robertson, The Uncertainty Principle (1929). [ref: robertson1929uncertainty]
> * E. Schrodinger, Zum Heisenbergschen Unscharfeprinzip (1930). [ref: schrodinger1930heisenberg]
> * B. C. Hall, Quantum Theory for Mathematicians, Chapter 12. [ref: hall2013quantum]

## A. Inner product lemmas

**`LinearPMap.inner_im_of_commutator_eq`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean#L69).

```lean
lemma inner_im_of_commutator_eq {u v : H} {c : ℝ}
    (h_comm : ⟪u, v⟫_ℂ - ⟪v, u⟫_ℂ = Complex.I * c) :
    (⟪u, v⟫_ℂ).im = c / 2
```

**`LinearPMap.inner_norm_sq_eq_re_sq_add_commutator_half_sq`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean#L80).

```lean
lemma inner_norm_sq_eq_re_sq_add_commutator_half_sq {u v : H} {c : ℝ}
    (h_comm : ⟪u, v⟫_ℂ - ⟪v, u⟫_ℂ = Complex.I * c) :
    ‖⟪u, v⟫_ℂ‖ ^ 2 = (⟪u, v⟫_ℂ).re ^ 2 + (c / 2) ^ 2
```

**`LinearPMap.sub_expectation_commutator_eq_raw`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean#L86).

```lean
lemma sub_expectation_commutator_eq_raw
    (ψ a b : H) (μa μb : ℝ)
    (hμa_right : ⟪ψ, a⟫_ℂ = (μa : ℂ)) (hμa_left : ⟪a, ψ⟫_ℂ = (μa : ℂ))
    (hμb_right : ⟪ψ, b⟫_ℂ = (μb : ℂ)) (hμb_left : ⟪b, ψ⟫_ℂ = (μb : ℂ)) (hψ_norm : ‖ψ‖ = 1) :
    ⟪a - (μa : ℂ) • ψ, b - (μb : ℂ) • ψ⟫_ℂ -
        ⟪b - (μb : ℂ) • ψ, a - (μa : ℂ) • ψ⟫_ℂ =
      ⟪a, b⟫_ℂ - ⟪b, a⟫_ℂ
```

**`LinearPMap.raw_commutator_eq_of_symmetric`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean#L109).

```lean
lemma raw_commutator_eq_of_symmetric
    (A B : H →ₗ.[ℂ] H) (hA : A.IsSymmetric) (hB : B.IsSymmetric)
    (ψ : A.domain) (hψB : (ψ : H) ∈ B.domain)
    (hBA : A ψ ∈ B.domain) (hAB : B ⟨ψ, hψB⟩ ∈ A.domain)
    {c : ℝ}
    (h_raw : ⟪(ψ : H), A ⟨B ⟨ψ, hψB⟩, hAB⟩ - B ⟨A ψ, hBA⟩⟫_ℂ = Complex.I * c) :
    ⟪A ψ, B ⟨ψ, hψB⟩⟫_ℂ - ⟪B ⟨ψ, hψB⟩, A ψ⟫_ℂ = Complex.I * c
```

**`LinearPMap.centeredCommutatorExpectation`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean#L132).

> The scalar commutator of the centered vectors of `A` and `B` in the state `ψ`.

```lean
def centeredCommutatorExpectation (A B : H →ₗ.[ℂ] H)
    (ψ : A.domain) (hψB : (ψ : H) ∈ B.domain) : ℂ
```

**`LinearPMap.rawCommutatorExpectation`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean#L139).

> The expectation of the raw commutator `[A, B]` in the state `ψ`, with explicit second-order
> domain witnesses.

```lean
def rawCommutatorExpectation (A B : H →ₗ.[ℂ] H)
    (ψ : A.domain) (hψB : (ψ : H) ∈ B.domain)
    (hBA : A ψ ∈ B.domain) (hAB : B ⟨ψ, hψB⟩ ∈ A.domain) : ℂ
```

**`LinearPMap.commutator_half_sq_le_mul_norm_sq`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean#L144).

```lean
lemma commutator_half_sq_le_mul_norm_sq {u v : H} {c : ℝ}
    (h_comm : ⟪u, v⟫_ℂ - ⟪v, u⟫_ℂ = Complex.I * c) :
    (|c| / 2) ^ 2 ≤ (‖u‖ * ‖v‖) ^ 2
```

## B. Centered commutator bounds

**`LinearPMap.state_uncertainty_squared_of_centered_commutator`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean#L182).

> A centered commutator identity implies the squared Robertson uncertainty bound.

```lean
lemma state_uncertainty_squared_of_centered_commutator :
    (|c| / 2) ^ 2 ≤ variance A ψ * variance B ⟨ψ, hψB⟩
```

**`LinearPMap.state_uncertainty_squared_with_covariance_of_centered_commutator`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean#L191).

> A centered commutator identity implies the Robertson–Schrödinger uncertainty bound.

```lean
lemma state_uncertainty_squared_with_covariance_of_centered_commutator :
    (covariance A B ψ hψB) ^ 2 + (c / 2) ^ 2 ≤
      variance A ψ * variance B ⟨ψ, hψB⟩
```

**`LinearPMap.state_uncertainty_of_centered_commutator`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean#L213).

> A centered commutator identity implies the standard uncertainty bound.

```lean
lemma state_uncertainty_of_centered_commutator :
    |c| / 2 ≤ standardDeviation A ψ * standardDeviation B ⟨ψ, hψB⟩
```

## C. Raw commutator bounds

**`LinearPMap.inner_centered_commutator_of_raw_commutator`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean#L241).

> A raw commutator expectation determines the centered commutator expectation.

```lean
lemma inner_centered_commutator_of_raw_commutator :
    centeredCommutatorExpectation A B ψ hψB = Complex.I * c
```

**`LinearPMap.state_uncertainty_squared_of_raw_commutator`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean#L276).

> A raw commutator expectation implies the squared Robertson uncertainty bound.

```lean
lemma state_uncertainty_squared_of_raw_commutator :
    (|c| / 2) ^ 2 ≤ variance A ψ * variance B ⟨ψ, hψB⟩
```

**`LinearPMap.state_uncertainty_squared_with_covariance_of_raw_commutator`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean#L282).

> A raw commutator expectation implies the squared uncertainty bound with covariance term.

```lean
lemma state_uncertainty_squared_with_covariance_of_raw_commutator :
    (covariance A B ψ hψB) ^ 2 + (c / 2) ^ 2 ≤
      variance A ψ * variance B ⟨ψ, hψB⟩
```

**`LinearPMap.state_uncertainty_of_raw_commutator`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean#L289).

> A raw commutator expectation implies the standard uncertainty bound.

```lean
lemma state_uncertainty_of_raw_commutator :
    |c| / 2 ≤ standardDeviation A ψ * standardDeviation B ⟨ψ, hψB⟩
```

## Depends on

- [Covariance (Physlib)](covariance.md)

## Sources

- [Physlib/QuantumMechanics/Operators/Uncertainty.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Uncertainty.lean)

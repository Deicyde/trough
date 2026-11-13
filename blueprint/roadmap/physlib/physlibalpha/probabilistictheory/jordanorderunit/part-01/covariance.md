---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsJordanOrderUnit.variance_eq_covarianceForm_self, ProbabilisticTheory.IsJordanOrderUnit.moment_centered_mul, ProbabilisticTheory.IsJordanOrderUnit.covarianceForm_isPosSemidef, ProbabilisticTheory.IsJordanOrderUnit.covariance_cauchy_schwarz, ProbabilisticTheory.IsJordanOrderUnit.covMatrix_posSemidef
statement: formalized
proof: formalized
---

# Covariance

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Covariance`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Covariance.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Covariance.lean): 5 declarations, 5 with a docstring.

> Covariance of observables in a Jordan order-unit space, and positivity of covariance matrices.

## i. Overview

> The Jordan product gives second moments `ω(a ∘ b)` of a state, and so the covariance `Cov\_ω(a, b) =
> ω(a ∘ b) - ω(a) ω(b)`, with the variance on the diagonal. For a C⋆-algebra this is the symmetrized
> quantum covariance `½ ⟨A B + B A⟩ - ⟨A⟩ ⟨B⟩`. Since squares are nonnegative, every covariance matrix
> is positive semidefinite, which gives a Cauchy–Schwarz inequality for covariances.

## ii. Key results

> - `IsJordanOrderUnit.variance_eq_covarianceForm_self` : the variance is the covariance on the
>   diagonal.
> - `IsJordanOrderUnit.covarianceForm_isPosSemidef` : the covariance form is positive semidefinite.
> - `IsJordanOrderUnit.covariance_cauchy_schwarz` : `Cov(a, b)² ≤ Var(a) Var(b)`.
> - `IsJordanOrderUnit.covMatrix_posSemidef` : covariance matrices are positive semidefinite.

## iv. References

> * None.

## A. Covariance

**`ProbabilisticTheory.IsJordanOrderUnit.variance_eq_covarianceForm_self`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Covariance.lean#L53).

> The Jordan variance is the diagonal of the canonical generic covariance form.

```lean
lemma variance_eq_covarianceForm_self (ω : 𝓢[ℝ, E]) (a : E) :
    variance ω a = LinearMap.covarianceForm ω.toLinearMap a a
```

**`ProbabilisticTheory.IsJordanOrderUnit.moment_centered_mul`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Covariance.lean#L58).

> The state's value on the Jordan product of two centered observables is exactly their
> covariance: the algebraic identity underlying `covMatrix_posSemidef` below.

```lean
lemma moment_centered_mul (ω : 𝓢[ℝ, E]) (a b : E) :
    ω (LinearMap.centered ω.toLinearMap a * LinearMap.centered ω.toLinearMap b) =
      LinearMap.covarianceForm ω.toLinearMap a b
```

**`ProbabilisticTheory.IsJordanOrderUnit.covarianceForm_isPosSemidef`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Covariance.lean#L66).

> The covariance form of a state is positive semidefinite. This is the coordinate-free form of
> covariance-matrix positivity and uses only positivity of Jordan squares.

```lean
lemma covarianceForm_isPosSemidef (ω : 𝓢[ℝ, E]) :
    (LinearMap.covarianceForm ω.toLinearMap).IsPosSemidef
```

**`ProbabilisticTheory.IsJordanOrderUnit.covariance_cauchy_schwarz`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Covariance.lean#L74).

> **Cauchy–Schwarz for covariances**: `Cov(a, b)² ≤ Var(a) Var(b)`.

```lean
lemma covariance_cauchy_schwarz (ω : 𝓢[ℝ, E]) (a b : E) :
    (LinearMap.covarianceForm ω.toLinearMap a b) ^ 2 ≤ variance ω a * variance ω b
```

## B. Positivity of the covariance matrix

**`ProbabilisticTheory.IsJordanOrderUnit.covMatrix_posSemidef`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Covariance.lean#L86).

> **Uncertainty theory, the Jordan-algebraic core**: the covariance matrix of a finite family of
> observables is positive semidefinite. This is the coordinate form of
> `covarianceForm_isPosSemidef`, obtained by evaluating the form on `∑ i, c i • a i`.

```lean
lemma covMatrix_posSemidef {ι : Type*} [Fintype ι] (ω : 𝓢[ℝ, E]) (a : ι → E) (c : ι → ℝ) :
    0 ≤ ∑ i, ∑ j, c i * c j * LinearMap.covarianceForm ω.toLinearMap (a i) (a j)
```

## Depends on

- [Moments, variance and Jordan projections](observable.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Covariance.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Covariance.lean)

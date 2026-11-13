---
declaration: module
origin: cited
lean: LinearPMap.covariance, LinearPMap.covariance_eq_re_inner_centered, LinearPMap.covariance_comm, LinearPMap.covariance_eq_re_symm_centered, LinearPMap.covariance_self_eq_variance
statement: formalized
proof: formalized
---

# Covariance

The module `Physlib.QuantumMechanics.Operators.Covariance`, [Physlib/QuantumMechanics/Operators/Covariance.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Covariance.lean): 5 declarations, 4 with a docstring.

## i. Overview

> In this module we define the covariance of two partial linear maps `A` and `B` in a common state
> `ψ` as the real part of the inner product of their centered vectors.

## ii. Key results

> - `covariance` : the real part of the centered inner product.
> - `covariance_comm` : covariance is symmetric in the two observables.
> - `covariance_eq_re_symm_centered` : covariance as the real part of the symmetrized centered
>   inner product.
> - `covariance_self_eq_variance` : the covariance of an observable with itself is its variance.

## iv. References

> * B. C. Hall, Quantum Theory for Mathematicians, Chapter 12. [ref: hall2013quantum]

## A. Covariance

**`LinearPMap.covariance`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Covariance.lean#L58).

> Covariance, defined as the real part of the centered inner product.

```lean
def covariance : ℝ
```

**`LinearPMap.covariance_eq_re_inner_centered`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Covariance.lean#L62).

> Covariance, unfolded to the real part of the centered inner product.

```lean
lemma covariance_eq_re_inner_centered :
    covariance A B ψ hψB =
      (⟪centered A ψ, centered B ⟨ψ, hψB⟩⟫_ℂ).re
```

**`LinearPMap.covariance_comm`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Covariance.lean#L68).

> Swapping the two observables does not change the covariance.

```lean
lemma covariance_comm :
    covariance A B ψ hψB = covariance B A ⟨ψ, hψB⟩ ψ.2
```

**`LinearPMap.covariance_eq_re_symm_centered`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Covariance.lean#L81).

> Covariance as the real part of the symmetrized centered inner product.

```lean
lemma covariance_eq_re_symm_centered :
    covariance A B ψ hψB =
      ((⟪centered A ψ, centered B ⟨ψ, hψB⟩⟫_ℂ +
        ⟪centered B ⟨ψ, hψB⟩, centered A ψ⟫_ℂ).re) / 2
```

**`LinearPMap.covariance_self_eq_variance`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Covariance.lean#L93).

```lean
lemma covariance_self_eq_variance (A : H →ₗ.[ℂ] H) (ψ : A.domain) :
    covariance A A ψ (by exact ψ.2) = variance A ψ
```

## Depends on

- [Variance and standard deviation](stateobservables-variance.md)

## Sources

- [Physlib/QuantumMechanics/Operators/Covariance.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Covariance.lean)

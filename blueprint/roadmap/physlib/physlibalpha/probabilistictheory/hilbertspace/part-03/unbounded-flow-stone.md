---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_strong_slope_tendsto, ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_hasDerivAt_zero, ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_hasDerivAt, ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.mem_domain_iff_expUnitaryGroup_strong_slope, ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.mem_domain_iff_expUnitaryGroup_hasDerivAt_zero, ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_star
statement: formalized
proof: formalized
---

# The unitary group of a self-adjoint operator

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Flow.Stone`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/Stone.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/Stone.lean): 6 declarations, 3 with a docstring.

> The unitary group exp(i t T) of a self-adjoint operator and its differentiable orbits.

## i. Overview

> For a self-adjoint operator `T` with spectral measure `μ`, the unitary group `exp(i t T)` is the
> integral of `exp(i t λ)`. A vector `x` lies in the domain of `T` exactly when its orbit is
> differentiable at `0`, and then the derivative at time `t` is `i T exp(i t T) x`.

## ii. Key results

> - `expUnitaryGroup_strong_slope_tendsto` : the difference quotients of the orbit converge to `i T
>   x`.
> - `expUnitaryGroup_hasDerivAt` : orbits of domain vectors are differentiable at every time.
> - `mem_domain_iff_expUnitaryGroup_hasDerivAt_zero` : the domain is the set of vectors with
>   differentiable orbit.
> - `expUnitaryGroup_star` : `exp(i t T)⋆ = exp(-i t T)`.

## iv. References

> * None.

## A. Differentiability of orbits

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_strong_slope_tendsto`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/Stone.lean#L69).

> For `x` in the domain of `T`, the difference quotients `(exp(i t T) x - x) / t` converge to `i T
> x`.

```lean
lemma expUnitaryGroup_strong_slope_tendsto
    (D : DomainAwareSelfAdjointSpectralTheorem T μS) (x : T.domain) :
    Filter.Tendsto
      (fun t : ℝ => t⁻¹ • (D.expUnitaryGroup t x - x))
      (𝓝[≠] (0 : ℝ))
      (𝓝 (Complex.I • T x))
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_hasDerivAt_zero`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/Stone.lean#L102).

```lean
lemma expUnitaryGroup_hasDerivAt_zero
    (D : DomainAwareSelfAdjointSpectralTheorem T μS) (x : T.domain) :
    HasDerivAt (fun t : ℝ => D.expUnitaryGroup t (x : H))
      (Complex.I • T x) 0
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_hasDerivAt`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/Stone.lean#L112).

> For `x` in the domain of `T`, the orbit `t ↦ exp(i t T) x` is differentiable at every time.

```lean
lemma expUnitaryGroup_hasDerivAt
    (D : DomainAwareSelfAdjointSpectralTheorem T μS) (x : T.domain) (s : ℝ) :
    HasDerivAt (fun t : ℝ => D.expUnitaryGroup t (x : H))
      (D.expUnitaryGroup s (Complex.I • T x)) s
```

## B. The domain via differentiable orbits

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.mem_domain_iff_expUnitaryGroup_strong_slope`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/Stone.lean#L152).

```lean
lemma mem_domain_iff_expUnitaryGroup_strong_slope
    (D : DomainAwareSelfAdjointSpectralTheorem T μS) (x : H) :
    x ∈ T.domain ↔
      ∃ y : H, Filter.Tendsto
        (fun t : ℝ => t⁻¹ • (D.expUnitaryGroup t x - x))
        (𝓝[≠] (0 : ℝ)) (𝓝 y)
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.mem_domain_iff_expUnitaryGroup_hasDerivAt_zero`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/Stone.lean#L278).

```lean
lemma mem_domain_iff_expUnitaryGroup_hasDerivAt_zero
    (D : DomainAwareSelfAdjointSpectralTheorem T μS) (x : H) :
    x ∈ T.domain ↔
      ∃ y : H, HasDerivAt (fun t : ℝ => D.expUnitaryGroup t x) y 0
```

## C. The adjoint of the unitary group

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_star`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/Stone.lean#L301).

> `exp(i t T)⋆ = exp(-i t T)`.

```lean
lemma expUnitaryGroup_star (D : DomainAwareSelfAdjointSpectralTheorem T μS) (t : ℝ) :
    star (D.expUnitaryGroup t) = D.expUnitaryGroup (-t)
```

## Depends on

- [The spectral theorem, stated](../part-02/unbounded-selfadjointspectraltheorem.md)

## Proof depends on

- [The integral of the identity is self-adjoint](../part-04/unbounded-spectralintegral-spectheorem.md)
- [Differentiating the exponential multiplier](../part-02/unbounded-stone.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/Stone.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/Stone.lean)

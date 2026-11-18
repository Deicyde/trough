---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_hasDerivAt_zero_iff, ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.mem_domain_iff_expUnitaryGroup_hasDerivAt, ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_hasDerivAt_iff
statement: formalized
proof: formalized
---

# The generator of the unitary group

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Flow.StoneAPI`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/StoneAPI.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/StoneAPI.lean): 3 declarations, 3 with a docstring.

> The domain of T is the set of vectors with differentiable orbit under exp(i t T).

## i. Overview

> A vector is in the domain of a self-adjoint operator `T` exactly when its orbit under `exp(i t T)`
> is differentiable at `0`, and the derivative is then `i T x`.

## ii. Key results

> - `mem_domain_iff_expUnitaryGroup_hasDerivAt` : the domain in terms of differentiable orbits.
> - `expUnitaryGroup_hasDerivAt_iff` : the derivative of an orbit is `i T x`.

## iv. References

> * None.

## A. The derivative at zero

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_hasDerivAt_zero_iff`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/StoneAPI.lean#L65).

> If the orbit is differentiable at zero, its derivative is forced by the operator.

```lean
lemma expUnitaryGroup_hasDerivAt_zero_iff (x : H) (y : H) :
    HasDerivAt (fun t : ℝ => D.expUnitaryGroup t x) y 0 ↔
      ∃ hx : x ∈ T.domain, y = Complex.I • T ⟨x, hx⟩
```

## B. The derivative at an arbitrary time

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.mem_domain_iff_expUnitaryGroup_hasDerivAt`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/StoneAPI.lean#L93).

> The generator domain is independent of the time at which differentiability is tested.  This
> is the orbit-level form of Stone's theorem used by evolution arguments.

```lean
lemma mem_domain_iff_expUnitaryGroup_hasDerivAt (x : H) (s : ℝ) :
    x ∈ T.domain ↔
      ∃ y : H, HasDerivAt (fun t : ℝ => D.expUnitaryGroup t x) y s
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_hasDerivAt_iff`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/StoneAPI.lean#L132).

> The derivative at an arbitrary time is uniquely the evolved generator vector.

```lean
lemma expUnitaryGroup_hasDerivAt_iff (x : H) (y : H) (s : ℝ) :
    HasDerivAt (fun t : ℝ => D.expUnitaryGroup t x) y s ↔
      ∃ hx : x ∈ T.domain,
        y = D.expUnitaryGroup s (Complex.I • T ⟨x, hx⟩)
```

## Depends on

- [The spectral theorem, stated](../part-02/unbounded-selfadjointspectraltheorem.md)

## Proof depends on

- [The unitary group of a self-adjoint operator](unbounded-flow-stone.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/StoneAPI.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/StoneAPI.lean)

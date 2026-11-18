---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_translate_comm, ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_translate_mem, ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_translate
statement: formalized
proof: formalized
---

# The unitary group preserves the domain of its generator (StoneInvariance)

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Flow.StoneInvariance`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/StoneInvariance.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/StoneInvariance.lean): 3 declarations, 3 with a docstring.

> The unitary group exp(i t T) preserves the domain of T and commutes with T.

## i. Overview

> For a self-adjoint operator `T` with spectral measure `μ`, the unitary group `exp(i t T)` preserves
> the domain of `T` and commutes with `T` there.

## ii. Key results

> - `expUnitaryGroup_translate_mem` : `exp(i s T)` preserves the domain of `T`.
> - `expUnitaryGroup_translate` : `T` commutes with `exp(i s T)` on its domain.

## iv. References

> * None.

## A. Invariance of the domain

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_translate_comm`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/StoneInvariance.lean#L66).

> The group law: `D.expUnitaryGroup t (D.expUnitaryGroup s x) = D.expUnitaryGroup (t + s) x`,
> via `expUnitaryGroup_add` and the (definitional) fact that `WOT`-multiplication is composition.

```lean
lemma expUnitaryGroup_translate_comm (x : H) (s t : ℝ) :
    D.expUnitaryGroup t (D.expUnitaryGroup s x) = D.expUnitaryGroup (t + s) x
```

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_translate_mem`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/StoneInvariance.lean#L73).

> `exp(i s T)` preserves the domain of `T`: the orbit of `exp(i s T) x` is the orbit of `x`
> shifted by `s`, so it is differentiable at `0`.

```lean
lemma expUnitaryGroup_translate_mem (x : T.domain) (s : ℝ) :
    D.expUnitaryGroup s (x : H) ∈ T.domain
```

## B. Commutation with the generator

**`ProbabilisticTheory.QuantumMechanics.DomainAwareSelfAdjointSpectralTheorem.expUnitaryGroup_translate`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/StoneInvariance.lean#L98).

> `T` commutes with `D.expUnitaryGroup s` on `T.domain`: for `x ∈ T.domain`,
> `D.expUnitaryGroup s x ∈ T.domain` and `T (D.expUnitaryGroup s x) = D.expUnitaryGroup s (T x)`.

```lean
lemma expUnitaryGroup_translate (x : T.domain) (s : ℝ) :
    T ⟨D.expUnitaryGroup s (x : H), D.expUnitaryGroup_translate_mem x s⟩ =
      D.expUnitaryGroup s (T x)
```

## Depends on

- [The spectral theorem, stated](../part-02/unbounded-selfadjointspectraltheorem.md)

## Proof depends on

- [The unitary group of a self-adjoint operator](unbounded-flow-stone.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/StoneInvariance.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Flow/StoneInvariance.lean)

---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.ofDensity, ProbabilisticTheory.UnitalPositiveLinearMap.ofDensity_apply
statement: formalized
proof: formalized
---

# Density operators

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.State.Density`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Density.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Density.lean): 2 declarations, 1 with a docstring.

> A positive trace-one operator on a Hilbert space defines the state `x ↦ Tr (x ρ)`.

## i. Overview

> A positive operator `ρ` with trace `1` defines the state `x ↦ Tr (x ρ)`. The trace here is the
> linear-algebra trace, so this applies to finite-dimensional Hilbert spaces.

## ii. Key results

> - `UnitalPositiveLinearMap.ofDensity` : the state of a density operator.

## iv. References

> * None.

## A. The state of a density operator

**`ProbabilisticTheory.UnitalPositiveLinearMap.ofDensity`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Density.lean#L53).

> A trace-one positive continuous linear map defines a state.

```lean
noncomputable def ofDensity : 𝓢[ℂ, H →L[ℂ] H]
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.ofDensity_apply`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Density.lean#L57).

```lean
lemma ofDensity_apply {ρ : H →L[ℂ] H} (hpos : 0 ≤ ρ)
    (hnorm : (ρ : H →ₗ[ℂ] H).trace ℂ H = 1) (x : H →L[ℂ] H) :
    ofDensity hpos hnorm x = (↑x * ↑ρ : H →ₗ[ℂ] H).trace ℂ H
```

## Depends on

- [Channels](../../channel/basic.md)
- [The trace as a positive map](trace.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Density.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/State/Density.lean)

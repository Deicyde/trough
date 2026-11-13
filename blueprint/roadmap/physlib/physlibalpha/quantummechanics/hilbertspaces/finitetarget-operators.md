---
declaration: module
origin: cited
---

# Operators on the Hilbert space of a finite target system

The module `PhyslibAlpha.QuantumMechanics.HilbertSpaces.FiniteTarget.Operators`, [PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Operators.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Operators.lean): 3 declarations (3 instances with no name), 0 with a docstring.

> Real scalar tower and self-adjoint decomposition instances for operators on `𝓗[d]`.

## i. Overview

> The bounded operators `𝓗[d] →L[ℂ] 𝓗[d]` form a C⋆-algebra, ordered by the Loewner order.
> This file registers, directly on these operators, the real scalar action commuting with
> composition and the decomposition of a self-adjoint operator into positive and negative parts.
>
> These instances hold for the operators on any complex Hilbert space, but on `𝓗[d]` inferring
> them unifies the two real actions on operators through the transferred complex module,
> which runs out of budget. Stated here once, they let hermitian operators on `𝓗[d]` be used
> where `SelfAdjointDecompose` is required, for instance as observables.

## ii. Key results

> - `IsScalarTower ℝ`, `SMulCommClass ℝ` instances : the real scalar action on `𝓗[d] →L[ℂ] 𝓗[d]`
>   commutes with composition.
> - `SelfAdjointDecompose` instance : the decomposition of a self-adjoint operator into positive and
>   negative parts, from the continuous functional calculus.

## iv. References

> * None.

## A. The real scalar action

**An instance with no name**, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Operators.lean#L60).

```lean
instance : IsScalarTower ℝ (𝓗[d] →L[ℂ] 𝓗[d]) (𝓗[d] →L[ℂ] 𝓗[d])
```

**An instance with no name**, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Operators.lean#L63).

```lean
instance : SMulCommClass ℝ (𝓗[d] →L[ℂ] 𝓗[d]) (𝓗[d] →L[ℂ] 𝓗[d])
```

## B. Positive and negative parts

**An instance with no name**, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Operators.lean#L72).

```lean
instance : SelfAdjointDecompose (𝓗[d] →L[ℂ] 𝓗[d])
```

## Depends on

- [The Hilbert space of a finite target quantum mechanical system](../../../physlib/quantummechanics/hilbertspaces/finitetarget-basic.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Operators.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/HilbertSpaces/FiniteTarget/Operators.lean)

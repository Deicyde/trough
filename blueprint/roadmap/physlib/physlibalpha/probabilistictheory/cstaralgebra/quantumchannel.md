---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.QuantumChannel, PhyslibAlpha.ProbabilisticTheory.QuantumChannel.ext, PhyslibAlpha.ProbabilisticTheory.QuantumChannel.toChannel
statement: formalized
proof: formalized
---

# Quantum channels

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.QuantumChannel`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/QuantumChannel.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/QuantumChannel.lean): 7 declarations (4 instances with no name), 2 with a docstring.

> Quantum channels as unital completely positive maps, and the channels they induce on observables.

## i. Overview

> A quantum channel between C⋆-algebras is a unital completely positive map: it stays positive when
> applied to one half of any larger, possibly entangled, system. Complete positivity is Mathlib's
> `CompletelyPositiveMap`. On self-adjoint parts every quantum channel is a channel between the
> order-unit spaces of observables.

## ii. Key results

> - `QuantumChannel A₁ A₂` : unital completely positive maps from `A₁` to `A₂`.
> - `QuantumChannel.toChannel` : the channel it induces between the self-adjoint parts.

## iv. References

> * None.

## A. Quantum channels

**`PhyslibAlpha.ProbabilisticTheory.QuantumChannel`**, a structure, [line 54](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/QuantumChannel.lean#L54).

> A quantum channel: a unital completely positive map between C⋆-algebras.

```lean
structure QuantumChannel (A₁ A₂ : Type*) [NonUnitalCStarAlgebra A₁] [NonUnitalCStarAlgebra A₂]
    [PartialOrder A₁] [PartialOrder A₂] [StarOrderedRing A₁] [StarOrderedRing A₂]
    [One A₁] [One A₂] extends A₁ →CP A₂, OneHom A₁ A₂
```

**An instance with no name**, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/QuantumChannel.lean#L63).

```lean
instance : FunLike (QuantumChannel A₁ A₂) A₁ A₂
```

**An instance with no name**, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/QuantumChannel.lean#L72).

```lean
instance : LinearMapClass (QuantumChannel A₁ A₂) ℂ A₁ A₂
```

**An instance with no name**, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/QuantumChannel.lean#L76).

```lean
instance : CompletelyPositiveMapClass (QuantumChannel A₁ A₂) A₁ A₂
```

**An instance with no name**, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/QuantumChannel.lean#L79).

```lean
instance : OneHomClass (QuantumChannel A₁ A₂) A₁ A₂
```

**`PhyslibAlpha.ProbabilisticTheory.QuantumChannel.ext`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/QuantumChannel.lean#L83).

```lean
lemma ext {f g : QuantumChannel A₁ A₂} (h : ∀ x, f x = g x) : f = g
```

## B. The induced channel on observables

**`PhyslibAlpha.ProbabilisticTheory.QuantumChannel.toChannel`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/QuantumChannel.lean#L94).

> The channel a quantum channel induces between the self-adjoint parts.

```lean
noncomputable def toChannel (f : QuantumChannel A₁ A₂) :
    Channel (selfAdjoint A₁) (selfAdjoint A₂)
```

## Depends on

- [The observables of a C⋆-algebra (PhyslibAlpha)](orderunit.md)
- [Restricting positive maps](../staralgebra/restrict.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/QuantumChannel.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/QuantumChannel.lean)

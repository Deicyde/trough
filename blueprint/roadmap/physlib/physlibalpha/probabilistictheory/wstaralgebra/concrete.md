---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.TraceClass.tracePairing_surjective, PhyslibAlpha.ProbabilisticTheory.TraceClass.tracePairingEquiv, PhyslibAlpha.ProbabilisticTheory.TraceClass.tracePairingEquiv_apply, PhyslibAlpha.ProbabilisticTheory.instWStarAlgebraStructureContinuousLinearMap
statement: formalized
proof: formalized
---

# The bounded operators as a W⋆-algebra

The module `PhyslibAlpha.ProbabilisticTheory.WStarAlgebra.Concrete`, [PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Concrete.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Concrete.lean): 4 declarations, 3 with a docstring.

> The bounded operators on a Hilbert space form a W⋆-algebra with the trace class as predual.

## i. Overview

> The trace pairing `A ↦ (ρ ↦ Tr (A ρ))` is an isometric isomorphism from the bounded operators on a
> Hilbert space onto the dual of the trace-class operators. So the bounded operators form a W⋆-algebra
> with predual the trace-class operators.

## ii. Key results

> - `tracePairingEquiv` : the trace pairing as an isometric isomorphism onto the dual.
> - `instWStarAlgebraStructureContinuousLinearMap` : the bounded operators with the trace-class
>   operators as predual.

## iv. References

> * None.

**`PhyslibAlpha.ProbabilisticTheory.TraceClass.tracePairing_surjective`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Concrete.lean#L52).

> The concrete trace pairing is surjective onto the strong dual of the trace class.

```lean
lemma tracePairing_surjective :
    Function.Surjective (⇑(tracePairingLinearIsometry (H := H)))
```

**`PhyslibAlpha.ProbabilisticTheory.TraceClass.tracePairingEquiv`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Concrete.lean#L57).

> The isometric identification of `H →L[ℂ] H` with the strong dual of its trace class.

```lean
def tracePairingEquiv : (H →L[ℂ] H) ≃ₗᵢ[ℂ] StrongDual ℂ (TraceClass H)
```

**`PhyslibAlpha.ProbabilisticTheory.TraceClass.tracePairingEquiv_apply`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Concrete.lean#L60).

```lean
lemma tracePairingEquiv_apply (A : H →L[ℂ] H) :
    tracePairingEquiv A = tracePairing A
```

## A. The `WStarAlgebraStructure (H →L[ℂ] H)` instance

**`PhyslibAlpha.ProbabilisticTheory.instWStarAlgebraStructureContinuousLinearMap`**, an instance, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Concrete.lean#L71).

> **The bounded operators form a W⋆-algebra**, with predual the trace-class operators and the
> trace pairing `a ↦ (ρ ↦ Tr (a ρ))`.

```lean
noncomputable instance instWStarAlgebraStructureContinuousLinearMap :
    WStarAlgebraStructure (H →L[ℂ] H)
```

## Depends on

- [W⋆-algebras and normal states](basic.md)
- [The trace pairing is isometric](tracepairingnorm.md)

## Proof depends on

- [The trace pairing is surjective](tracepairingsurjectivity.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Concrete.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/WStarAlgebra/Concrete.lean)

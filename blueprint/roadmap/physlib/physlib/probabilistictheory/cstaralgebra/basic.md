---
declaration: module
origin: cited
lean: ProbabilisticTheory.instPosSMulMonoSelfAdjoint, ProbabilisticTheory.selfAdjoint_le_nsmul_one_ceil_norm, ProbabilisticTheory.selfAdjoint_le_zero_of_forall_pos_smul_one_le, ProbabilisticTheory.ofCStarAlgebra, ProbabilisticTheory.realEquivComplex
statement: formalized
proof: formalized
---

# The observables of a C⋆-algebra (Physlib)

The module `Physlib.ProbabilisticTheory.CStarAlgebra.Basic`, [Physlib/ProbabilisticTheory/CStarAlgebra/Basic.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Basic.lean): 5 declarations, 5 with a docstring.

> The self-adjoint part of a unital C⋆-algebra is an Archimedean order-unit space.

## i. Overview

> The observables of a quantum system are the self-adjoint elements of its C⋆-algebra. One
> observable lies below another if their difference has no negative measurement outcome. The
> identity is the certain outcome.
>
> Every observable lies below a multiple of the identity. So no outcome exceeds the norm.
>
> An observable that lies below every positive multiple of the identity has no positive outcome.
> This is the Archimedean property.

## ii. Key results

> - `ProbabilisticTheory.selfAdjoint_le_nsmul_one_ceil_norm` : bound observables by natural
>   multiples of the identity.
> - `ProbabilisticTheory.selfAdjoint_le_zero_of_forall_pos_smul_one_le` : an observable below
>   every positive multiple of the identity is nonpositive.
> - `ProbabilisticTheory.ofCStarAlgebra` : the self-adjoint observables of a quantum system.
> - `ProbabilisticTheory.realEquivComplex` : real outcomes are the self-adjoint complex scalars.

## iv. References

## A. The order-unit space of observables

**`ProbabilisticTheory.instPosSMulMonoSelfAdjoint`**, an instance, [line 62](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Basic.lean#L62).

> Nonnegative real scalars preserve the order on observables.

```lean
instance instPosSMulMonoSelfAdjoint : PosSMulMono ℝ (selfAdjoint 𝒜)
```

**`ProbabilisticTheory.selfAdjoint_le_nsmul_one_ceil_norm`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Basic.lean#L68).

> Every observable lies below a natural multiple of the identity.

```lean
lemma selfAdjoint_le_nsmul_one_ceil_norm (x : selfAdjoint 𝒜) :
    x ≤ ⌈‖(x : 𝒜)‖⌉₊ • (1 : selfAdjoint 𝒜)
```

## B. The Archimedean property

**`ProbabilisticTheory.selfAdjoint_le_zero_of_forall_pos_smul_one_le`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Basic.lean#L86).

> An observable below every positive multiple of the identity is below zero.

```lean
lemma selfAdjoint_le_zero_of_forall_pos_smul_one_le {x : selfAdjoint 𝒜}
    (h : ∀ ε : ℝ, 0 < ε → x ≤ ε • (1 : selfAdjoint 𝒜)) : x ≤ 0
```

## C. Quantum observables and scalar outcomes

**`ProbabilisticTheory.ofCStarAlgebra`**, an abbrev, [line 97](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Basic.lean#L97).

> The self-adjoint elements of a C⋆-algebra, with their Archimedean order and unit.

```lean
noncomputable abbrev ofCStarAlgebra (𝒜 : Type*) [CStarAlgebra 𝒜] [PartialOrder 𝒜]
    [StarOrderedRing 𝒜] : ProbabilisticTheory
```

**`ProbabilisticTheory.realEquivComplex`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Basic.lean#L105).

> The real numbers are the observables of the quantum system with algebra `ℂ`.

```lean
noncomputable def realEquivComplex : Reversible real (ofCStarAlgebra ℂ)
```

## Depends on

- [Reversible transformations of observables](../channel/reversible.md)

## Sources

- [Physlib/ProbabilisticTheory/CStarAlgebra/Basic.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/CStarAlgebra/Basic.lean)

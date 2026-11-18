---
declaration: module
origin: cited
lean: selfAdjoint.instPosSMulMono, selfAdjoint.le_nsmul_one_ceil_norm, selfAdjoint.instOrderUnitSpace, selfAdjoint.le_zero_of_forall_pos_smul_one_le, selfAdjoint.instArchimedeanOrderUnitSpace
statement: formalized
proof: formalized
---

# The observables of a C⋆-algebra

The module `Physlib.ProbabilisticTheory.CStarAlgebra.OrderUnit`, [Physlib/ProbabilisticTheory/CStarAlgebra/OrderUnit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/CStarAlgebra/OrderUnit.lean): 5 declarations, 5 with a docstring.

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

> - `selfAdjoint.le_nsmul_one_ceil_norm` : every observable lies below a natural multiple of the
>   identity.
> - `selfAdjoint.le_zero_of_forall_pos_smul_one_le` : an element below every positive multiple of
>   the identity is below zero.
> - `selfAdjoint.instOrderUnitSpace` : the observables form an order-unit space.
> - `selfAdjoint.instArchimedeanOrderUnitSpace` : it is Archimedean.

## iv. References

## A. The order-unit space of observables

**`selfAdjoint.instPosSMulMono`**, an instance, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/CStarAlgebra/OrderUnit.lean#L60).

> Nonnegative real scalars preserve the order on observables.

```lean
instance instPosSMulMono : PosSMulMono ℝ (selfAdjoint 𝒜)
```

**`selfAdjoint.le_nsmul_one_ceil_norm`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/CStarAlgebra/OrderUnit.lean#L66).

> Every observable lies below a natural multiple of the identity.

```lean
lemma le_nsmul_one_ceil_norm (x : selfAdjoint 𝒜) : x ≤ ⌈‖(x : 𝒜)‖⌉₊ • (1 : selfAdjoint 𝒜)
```

**`selfAdjoint.instOrderUnitSpace`**, an instance, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/CStarAlgebra/OrderUnit.lean#L77).

> The observables of a quantum system form an order-unit space with unit `1`.

```lean
noncomputable instance instOrderUnitSpace : OrderUnitSpace (selfAdjoint 𝒜)
```

## B. The Archimedean property

**`selfAdjoint.le_zero_of_forall_pos_smul_one_le`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/CStarAlgebra/OrderUnit.lean#L88).

> An observable below every positive multiple of the identity is below zero.

```lean
lemma le_zero_of_forall_pos_smul_one_le {x : selfAdjoint 𝒜}
    (h : ∀ ε : ℝ, 0 < ε → x ≤ ε • (1 : selfAdjoint 𝒜)) : x ≤ 0
```

**`selfAdjoint.instArchimedeanOrderUnitSpace`**, an instance, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/CStarAlgebra/OrderUnit.lean#L97).

> The order of observables is Archimedean.

```lean
noncomputable instance instArchimedeanOrderUnitSpace :
    ArchimedeanOrderUnitSpace (selfAdjoint 𝒜)
```

## Depends on

- [Archimedean order-unit spaces](../orderunit/archimedean.md)

## Sources

- [Physlib/ProbabilisticTheory/CStarAlgebra/OrderUnit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/CStarAlgebra/OrderUnit.lean)

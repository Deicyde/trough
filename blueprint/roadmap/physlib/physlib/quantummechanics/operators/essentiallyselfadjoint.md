---
declaration: module
origin: cited
lean: LinearPMap.IsEssentiallySelfAdjoint, LinearPMap.isEssentiallySelfAdjoint_def, LinearPMap.IsSymmetric.isEssentiallySelfAdjoint_iff, LinearPMap.IsSelfAdjoint.isEssentiallySelfAdjoint, LinearPMap.IsEssentiallySelfAdjoint.hasDenseDomain, LinearPMap.IsEssentiallySelfAdjoint.isSymmetric, LinearPMap.IsEssentiallySelfAdjoint.isClosable, LinearPMap.IsEssentiallySelfAdjoint.isUnbounded
statement: formalized
proof: formalized
---

# Essentially self-adjoint operators

The module `Physlib.QuantumMechanics.Operators.EssentiallySelfAdjoint`, [Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean): 12 declarations, 8 with a docstring.

## i. Overview

> An operator on a Hilbert space is said to be *essentially self-adjoint* (ESA) if its closure
> is self-adjoint. This module defines ESA operators and collects their basic properties.
>
> The spectral theory of ESA operators is very closely tied to that of self-adjoint operators,
> by virtue of their having a unique self-adjoint extension. As such, it is often more convenient
> to define and work with ESA operators on simpler domains rather than their closures directly.

## ii. Key results

> - `IsEssentiallySelfAdjoint` : The definition of an ESA operator as having a self-adjoint closure.
> - `unique_self_adjoint_extension` : The closure of an ESA operator is its *unique* self-adjoint
>   extension.

## iv. References

## A. Definition of ESA

**`LinearPMap.IsEssentiallySelfAdjoint`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean#L51).

> An operator is essentially self-adjoint if its closure is self-adjoint.

```lean
def IsEssentiallySelfAdjoint (T : H →ₗ.[ℂ] H) : Prop
```

**`LinearPMap.isEssentiallySelfAdjoint_def`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean#L55).

```lean
lemma isEssentiallySelfAdjoint_def :
    T.IsEssentiallySelfAdjoint ↔ IsSelfAdjoint T.closure
```

## B. ESA from symmetric or self-adjoint

**`LinearPMap.IsSymmetric.isEssentiallySelfAdjoint_iff`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean#L64).

> A densely-defined symmetric operator is essentially self-adjoint *if and only if*
> its adjoint and closure have the same domain.

```lean
lemma IsSymmetric.isEssentiallySelfAdjoint_iff (h : T.IsSymmetric) (h' : T.HasDenseDomain) :
    T.IsEssentiallySelfAdjoint ↔ T†.domain = T.closure.domain
```

**`LinearPMap.IsSelfAdjoint.isEssentiallySelfAdjoint`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean#L73).

> A self-adjoint operators is essentially self-adjoint.

```lean
lemma IsSelfAdjoint.isEssentiallySelfAdjoint (h : IsSelfAdjoint T) : T.IsEssentiallySelfAdjoint
```

## C. Properties

**`LinearPMap.IsEssentiallySelfAdjoint.hasDenseDomain`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean#L87).

> An essentially self-adjoint operator is densely defined.

```lean
lemma hasDenseDomain : T.HasDenseDomain
```

**`LinearPMap.IsEssentiallySelfAdjoint.isSymmetric`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean#L91).

> An essentially self-adjoint operator is symmetric.

```lean
lemma isSymmetric : T.IsSymmetric
```

**`LinearPMap.IsEssentiallySelfAdjoint.isClosable`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean#L94).

> An essentially self-adjoint operator is closable.

```lean
lemma isClosable : T.IsClosable
```

**`LinearPMap.IsEssentiallySelfAdjoint.isUnbounded`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean#L97).

> An essentially self-adjoint operator is unbounded (densely defined and closable).

```lean
lemma isUnbounded : T.IsUnbounded
```

### C.1. Algebraic

**`LinearPMap.IsEssentiallySelfAdjoint.smul`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean#L106).

```lean
protected lemma smul {c : ℂ} (hc : c ≠ 0) (hc' : conj c = c) :
    (c • T).IsEssentiallySelfAdjoint
```

**`LinearPMap.IsEssentiallySelfAdjoint.real_smul`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean#L111).

```lean
protected lemma real_smul {r : ℝ} (hr : r ≠ 0) : (r • T).IsEssentiallySelfAdjoint
```

**`LinearPMap.IsEssentiallySelfAdjoint.neg`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean#L115).

```lean
protected lemma neg : (-T).IsEssentiallySelfAdjoint
```

### C.2. Uniqueness of self-adjoint extension

**`LinearPMap.IsEssentiallySelfAdjoint.unique_self_adjoint_extension`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean#L123).

> The closure is the unique self-adjoint extension of an essentially self-adjoint operator.

```lean
lemma unique_self_adjoint_extension {T₂ : H →ₗ.[ℂ] H} (h_le : T ≤ T₂) (h₂ : IsSelfAdjoint T₂) :
    T₂ = T.closure
```

## Depends on

- [Unbounded operators (Basic)](basic.md)

## Sources

- [Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/EssentiallySelfAdjoint.lean)

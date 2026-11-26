---
declaration: module
origin: cited
lean: QuantumMechanics.QuantumSystem, QuantumMechanics.QuantumSystem.mkESA, QuantumMechanics.QuantumSystem.instZero, QuantumMechanics.QuantumSystem.UnitaryRelation, QuantumMechanics.QuantumSystem.unitaryRelation_refl, QuantumMechanics.QuantumSystem.unitaryRelation_symm, QuantumMechanics.QuantumSystem.unitaryRelation_trans, QuantumMechanics.QuantumSystem.unitaryRelation_equiv
statement: formalized
proof: formalized
---

# Quantum system

The module `Physlib.QuantumMechanics.QuantumSystem.Basic`, [Physlib/QuantumMechanics/QuantumSystem/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/QuantumSystem/Basic.lean): 9 declarations, 8 with a docstring.

## i. Overview

> In non-relativistic quantum mechanics a quantum system is characterized by a Hilbert space
> (complete inner product space) and self-adjoint Hamiltonian operator; these data are collected in
> the `QuantumSystem` structure.
>
> Two quantum systems are said to be "unitary equivalent" if there is a unitary bijection between
> their respective Hilbert spaces which sends one Hamiltonian to the other under conjugation.
> Unitary equivalent quantum systems are physically indestinguishable, as all operators, states,
> matrix elements, probabilities, eigenvalues, etc. are in 1-1 correspondence.

## ii. Key results

> Definitions
> - `QuantumSystem` : Structure bundling together a choice of Hilbert space
>     and self-adjoint Hamiltonian operator.
> - `UnitaryRelation` : The unitary equivalence relation.

## iv. References

> * None.

## A. Definition

**`QuantumMechanics.QuantumSystem`**, a structure, [line 56](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/QuantumSystem/Basic.lean#L56).

> A quantum system is identified by its Hilbert space and self-adjoint Hamiltonian operator.

```lean
structure QuantumSystem where
  /-- The complex Hilbert space. -/
  HS : Type*
  /-- The Hilbert space is a normed, commutative group. -/
  [instNormed : NormedAddCommGroup HS]
  /-- The Hilbert space is a complex inner product space. -/
  [instInner : InnerProductSpace ℂ HS]
  /-- The Hilbert space is complete. -/
  [instComplete : CompleteSpace HS]
  /-- The self-adjoint Hamiltonian operator. -/
  ℋ : HS →ₗ.[ℂ] HS
  ℋ_self_adjoint : IsSelfAdjoint ℋ
```

## B. Creation from an essentially self-adjoint operator

> An essentially self-adjoint operator has a unique self-adjoint extension
> (c.f. `IsEssentiallySelfAdjoint.unique_self_adjoint_extension`).
> For this reason, a quantum system can be uniquely associated to an e.s.a. Hamiltonian operator.

**`QuantumMechanics.QuantumSystem.mkESA`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/QuantumSystem/Basic.lean#L83).

> Create a quantum system from a Hamiltonian operator which is merely
> essentially self-adjoint by taking its closure.

```lean
def mkESA {HS : Type*} [NormedAddCommGroup HS] [InnerProductSpace ℂ HS] [CompleteSpace HS]
    {ℋ : HS →ₗ.[ℂ] HS} (hℋ : IsEssentiallySelfAdjoint ℋ) : QuantumSystem
```

## C. Zero

**`QuantumMechanics.QuantumSystem.instZero`**, an instance, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/QuantumSystem/Basic.lean#L90).

```lean
instance instZero : Zero QuantumSystem
```

## D. Unitary equivalence

**`QuantumMechanics.QuantumSystem.UnitaryRelation`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/QuantumSystem/Basic.lean#L99).

> The relation on quantum systems where `Q₁` is related to `Q₂` if there exists a linear isometry
> equivalence `e : Q₁.HS ≃ₗᵢ[ℂ] Q₂.HS` between the respective Hilbert spaces satisfying
> `e ∘ Q₁.ℋ ∘ e.symm = Q₂.ℋ`.

```lean
def UnitaryRelation (Q₁ Q₂ : QuantumSystem) : Prop
```

**`QuantumMechanics.QuantumSystem.unitaryRelation_refl`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/QuantumSystem/Basic.lean#L104).

> The relation `UnitaryRelation` is reflexive.

```lean
lemma unitaryRelation_refl (Q : QuantumSystem) : UnitaryRelation Q Q
```

**`QuantumMechanics.QuantumSystem.unitaryRelation_symm`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/QuantumSystem/Basic.lean#L108).

> The relation `UnitaryRelation` is symmetric.

```lean
lemma unitaryRelation_symm {Q₁ Q₂ : QuantumSystem} (h₁₂ : UnitaryRelation Q₁ Q₂) :
    UnitaryRelation Q₂ Q₁
```

**`QuantumMechanics.QuantumSystem.unitaryRelation_trans`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/QuantumSystem/Basic.lean#L116).

> The relation `UnitaryRelation` is transitive.

```lean
lemma unitaryRelation_trans {Q₁ Q₂ Q₃ : QuantumSystem} (h₁₂ : UnitaryRelation Q₁ Q₂)
    (h₂₃ : UnitaryRelation Q₂ Q₃) : UnitaryRelation Q₁ Q₃
```

**`QuantumMechanics.QuantumSystem.unitaryRelation_equiv`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/QuantumSystem/Basic.lean#L123).

> The relation `UnitaryRelation` is an equivalence relation.

```lean
lemma unitaryRelation_equiv : Equivalence UnitaryRelation
```

**`QuantumMechanics.QuantumSystem.QuantumSystemSetoid`**, an instance, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/QuantumSystem/Basic.lean#L129).

> The setoid of quantum systems with `UnitaryRelation` for equivalence relation.

```lean
instance QuantumSystemSetoid : Setoid QuantumSystem
```

## Depends on

- [Essentially self-adjoint operators](../operators/essentiallyselfadjoint.md)

## Sources

- [Physlib/QuantumMechanics/QuantumSystem/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/QuantumSystem/Basic.lean)

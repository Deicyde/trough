---
declaration: module
origin: cited
lean: Lorentz.ComplexVector.pauliVal, Lorentz.ComplexVector.pauliVal_expand_basis, Lorentz.ComplexVector.pauliVal_repr, Lorentz.ComplexVector.pauliVal_expand_tmul, Lorentz.ComplexVector.pauliVal_invariant, Lorentz.ComplexVector.pauli, Lorentz.ComplexVector.pauli_apply_one
statement: formalized
proof: formalized
---

# Physlib.Relativity.Bispinors.Pauli.Basic

The module `Physlib.Relativity.Bispinors.Pauli.Basic`, [Physlib/Relativity/Bispinors/Pauli/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Basic.lean): 7 declarations, 7 with a docstring.

## Pauli matrices as Lorentz tensors

> The results in this file are primarily used to show that
> the pauli matrices in invariant under the `SL(2,ℂ)` action.

**`Lorentz.ComplexVector.pauliVal`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Basic.lean#L37).

> The tensor `σ^μ^a^{dot a}` based on the Pauli-matrices as an element of
> `ComplexVector ⊗ LeftHandedWeyl ⊗ RightHandedWeyl`.

```lean
def pauliVal : ComplexVector ⊗[ℂ] (LeftHandedWeyl ⊗[ℂ] RightHandedWeyl)
```

**`Lorentz.ComplexVector.pauliVal_expand_basis`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Basic.lean#L41).

> The expansion of `ComplexVector.pauliVal` into `ComplexVector.basis` basis vectors.

```lean
lemma pauliVal_expand_basis : ComplexVector.pauliVal =
    ComplexVector.basis (Sum.inl 0) ⊗ₜ leftRightToMatrix.symm (pauliBasis (Sum.inl 0))
    + ComplexVector.basis (Sum.inr 0) ⊗ₜ leftRightToMatrix.symm (pauliBasis (Sum.inr 0))
    + ComplexVector.basis (Sum.inr 1) ⊗ₜ leftRightToMatrix.symm (pauliBasis (Sum.inr 1))
    + ComplexVector.basis (Sum.inr 2) ⊗ₜ leftRightToMatrix.symm (pauliBasis (Sum.inr 2))
```

**`Lorentz.ComplexVector.pauliVal_repr`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Basic.lean#L50).

> The components of `pauliVal` in the basis `e_μ ⊗ e_a ⊗ e_ḃ` are the entries of the
> Pauli matrices.

```lean
lemma pauliVal_repr (μ : Fin 1 ⊕ Fin 3) (a b : Fin 2) :
    (ComplexVector.basis.tensorProduct
      (LeftHandedWeyl.basis.tensorProduct RightHandedWeyl.basis)).repr pauliVal (μ, (a, b)) =
      pauliMatrix μ a b
```

**`Lorentz.ComplexVector.pauliVal_expand_tmul`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Basic.lean#L63).

> The expansion of `ComplexVector.pauliVal` into the basis of tensor product vectors.

```lean
lemma pauliVal_expand_tmul : ComplexVector.pauliVal =
    ComplexVector.basis (Sum.inl 0) ⊗ₜ (LeftHandedWeyl.basis 0 ⊗ₜ RightHandedWeyl.basis 0)
    + ComplexVector.basis (Sum.inl 0) ⊗ₜ (LeftHandedWeyl.basis 1 ⊗ₜ RightHandedWeyl.basis 1)
    + ComplexVector.basis (Sum.inr 0) ⊗ₜ (LeftHandedWeyl.basis 0 ⊗ₜ RightHandedWeyl.basis 1)
    + ComplexVector.basis (Sum.inr 0) ⊗ₜ (LeftHandedWeyl.basis 1 ⊗ₜ RightHandedWeyl.basis 0)
    - I • ComplexVector.basis (Sum.inr 1) ⊗ₜ (LeftHandedWeyl.basis 0 ⊗ₜ RightHandedWeyl.basis 1)
    + I • ComplexVector.basis (Sum.inr 1) ⊗ₜ (LeftHandedWeyl.basis 1 ⊗ₜ RightHandedWeyl.basis 0)
    + ComplexVector.basis (Sum.inr 2) ⊗ₜ (LeftHandedWeyl.basis 0 ⊗ₜ RightHandedWeyl.basis 0)
    - ComplexVector.basis (Sum.inr 2) ⊗ₜ (LeftHandedWeyl.basis 1 ⊗ₜ RightHandedWeyl.basis 1)
```

**`Lorentz.ComplexVector.pauliVal_invariant`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Basic.lean#L78).

> The Pauli tensor is invariant under the `SL(2, ℂ)` action.

```lean
lemma pauliVal_invariant (Λ : SL(2,ℂ)) :
    TensorProduct.map (SL2CRep Λ)
      (TensorProduct.map (LeftHandedWeyl.rep Λ) (RightHandedWeyl.rep Λ)) pauliVal = pauliVal
```

**`Lorentz.ComplexVector.pauli`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Basic.lean#L99).

> The tensor `σ^μ^a^{dot a}` based on the Pauli-matrices as a morphism,
> `𝟙_ (Rep ℂ SL(2,ℂ)) ⟶ ComplexVector ⊗ LeftHandedWeyl ⊗ RightHandedWeyl` manifesting
> the invariance under the `SL(2,ℂ)` action.

```lean
def pauli :(Representation.trivial ℂ SL(2,ℂ) ℂ).IntertwiningMap
    (ComplexVector.SL2CRep.tprod (LeftHandedWeyl.rep.tprod RightHandedWeyl.rep))
```

**`Lorentz.ComplexVector.pauli_apply_one`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Basic.lean#L117).

> The map `𝟙_ (Rep ℂ SL(2,ℂ)) ⟶ ComplexVector ⊗ LeftHandedWeyl ⊗ RightHandedWeyl`
> corresponding to Pauli matrices, when evaluated on `1` corresponds to the tensor
> `ComplexVector.pauliVal`.

```lean
lemma pauli_apply_one :
    ComplexVector.pauli (1 : ℂ) = ComplexVector.pauliVal
```

## Depends on

- [Tensor product of two Weyl fermion](../fermions/weyl/two.md)
- [Complex Lorentz vectors](../tensors/part-02/complextensor-vector-basic.md)

## Sources

- [Physlib/Relativity/Bispinors/Pauli/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Bispinors/Pauli/Basic.lean)

---
declaration: module
origin: cited
lean: Lorentz.ComplexVector.contrBi, Lorentz.ComplexCoVector.contrBi, Lorentz.ComplexVector.contr, Lorentz.ComplexVector.contr_tmul, Lorentz.ComplexVector.contr_basis, Lorentz.ComplexVector.contr_basis', Lorentz.ComplexCoVector.contr, Lorentz.ComplexCoVector.contr_tmul
statement: formalized
proof: formalized
---

# Contraction of Lorentz vectors

The module `Physlib.Relativity.Tensors.ComplexTensor.Vector.Contraction`, [Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean): 12 declarations, 4 with a docstring.

**`Lorentz.ComplexVector.contrBi`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean#L29).

> The bi-linear map corresponding to contraction of a contravariant Lorentz vector with a
> covariant Lorentz vector.

```lean
def ComplexVector.contrBi : ComplexVector →ₗ[ℂ] ComplexCoVector →ₗ[ℂ] ℂ
```

**`Lorentz.ComplexCoVector.contrBi`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean#L53).

> The bi-linear map corresponding to contraction of a covariant Lorentz vector with a
> contravariant Lorentz vector.

```lean
def ComplexCoVector.contrBi : ComplexCoVector →ₗ[ℂ] ComplexVector →ₗ[ℂ] ℂ
```

**`Lorentz.ComplexVector.contr`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean#L80).

> The linear map from complexContr ⊗ complexCo to ℂ given by
> summing over components of contravariant Lorentz vector and
> covariant Lorentz vector in the
> standard basis (i.e. the dot product).
> In terms of index notation this is the contraction is ψⁱ φᵢ.

```lean
def ComplexVector.contr : (ComplexVector.SL2CRep.tprod ComplexCoVector.SL2CRep).IntertwiningMap
    (Representation.trivial ℂ SL(2,ℂ) ℂ)
```

**`Lorentz.ComplexVector.contr_tmul`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean#L91).

```lean
lemma ComplexVector.contr_tmul (ψ : ComplexVector) (φ : ComplexCoVector) :
    ComplexVector.contr (ψ ⊗ₜ φ) = ψ.toFin13ℂ ⬝ᵥ φ.toFin13ℂ
```

**`Lorentz.ComplexVector.contr_basis`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean#L95).

```lean
lemma ComplexVector.contr_basis (i j : Fin 4) :
    ComplexVector.contr (ComplexVector.basisFin4 i ⊗ₜ ComplexCoVector.basisFin4 j) =
    if i.1 = j.1 then (1 : ℂ) else 0
```

**`Lorentz.ComplexVector.contr_basis'`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean#L106).

```lean
lemma ComplexVector.contr_basis' (i j : Fin 1 ⊕ Fin 3) :
    ComplexVector.contr (ComplexVector.basis i ⊗ₜ ComplexCoVector.basis j) =
    if i = j then (1 : ℂ) else 0
```

**`Lorentz.ComplexCoVector.contr`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean#L121).

> The linear map from complexCo ⊗ complexContr to ℂ given by
> summing over components of covariant Lorentz vector and
> contravariant Lorentz vector in the
> standard basis (i.e. the dot product).
> In terms of index notation this is the contraction is φᵢ ψⁱ.

```lean
def ComplexCoVector.contr : (ComplexCoVector.SL2CRep.tprod ComplexVector.SL2CRep).IntertwiningMap
    (Representation.trivial ℂ SL(2,ℂ) ℂ)
```

**`Lorentz.ComplexCoVector.contr_tmul`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean#L131).

```lean
lemma ComplexCoVector.contr_tmul (φ : ComplexCoVector) (ψ : ComplexVector) :
    ComplexCoVector.contr (φ ⊗ₜ ψ) = φ.toFin13ℂ ⬝ᵥ ψ.toFin13ℂ
```

**`Lorentz.ComplexCoVector.contr_basis`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean#L135).

```lean
lemma ComplexCoVector.contr_basis (i j : Fin 4) :
    ComplexCoVector.contr (ComplexCoVector.basisFin4 i ⊗ₜ ComplexVector.basisFin4 j) =
    if i.1 = j.1 then (1 : ℂ) else 0
```

**`Lorentz.ComplexCoVector.contr_basis'`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean#L146).

```lean
lemma ComplexCoVector.contr_basis' (i j : Fin 1 ⊕ Fin 3) :
    ComplexCoVector.contr (ComplexCoVector.basis i ⊗ₜ ComplexVector.basis j) =
    if i = j then (1 : ℂ) else 0
```

## Symmetry

**`Lorentz.ComplexVector.contr_tmul_symm`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean#L168).

```lean
lemma ComplexVector.contr_tmul_symm (φ : ComplexVector) (ψ : ComplexCoVector) :
    ComplexVector.contr (φ ⊗ₜ ψ) = ComplexCoVector.contr (ψ ⊗ₜ φ)
```

**`Lorentz.ComplexCoVector.contr_tmul_symm`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean#L172).

```lean
lemma ComplexCoVector.contr_tmul_symm (φ : ComplexCoVector) (ψ : ComplexVector) :
    ComplexCoVector.contr (φ ⊗ₜ ψ) = ComplexVector.contr (ψ ⊗ₜ φ)
```

## Depends on

- [Complex Lorentz vectors](complextensor-vector-basic.md)

## Sources

- [Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Contraction.lean)

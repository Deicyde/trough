---
declaration: module
origin: cited
lean: Lorentz.ComplexVector.basis, Lorentz.ComplexVector.basis_toFin13ℂ, Lorentz.ComplexVector.basis_ρ_apply, Lorentz.ComplexVector.basis_ρ_val, Lorentz.ComplexVector.basisFin4, Lorentz.ComplexVector.basisFin4_eq_reindex, Lorentz.ComplexVector.basis_reindex_apply_eq_fin4, Lorentz.ComplexVector.basisFin4_apply_zero
statement: formalized
proof: formalized
---

# Complex Lorentz vectors

The module `Physlib.Relativity.Tensors.ComplexTensor.Vector.Basic`, [Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean): 32 declarations, 6 with a docstring.

> We define complex Lorentz vectors in 4d space-time as representations of SL(2, C).

**`Lorentz.ComplexVector.basis`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L29).

> The standard basis of complex contravariant Lorentz vectors.

```lean
def ComplexVector.basis : Basis (Fin 1 ⊕ Fin 3) ℂ ComplexVector
```

**`Lorentz.ComplexVector.basis_toFin13ℂ`**, a lemma, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L33).

```lean
lemma ComplexVector.basis_toFin13ℂ (i :Fin 1 ⊕ Fin 3) :
    (ComplexVector.basis i).toFin13ℂ = Pi.single i 1
```

**`Lorentz.ComplexVector.basis_ρ_apply`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L39).

```lean
lemma ComplexVector.basis_ρ_apply (M : SL(2,ℂ)) (i j : Fin 1 ⊕ Fin 3) :
    (LinearMap.toMatrix ComplexVector.basis ComplexVector.basis) (ComplexVector.SL2CRep M) i j =
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M)) i j
```

**`Lorentz.ComplexVector.basis_ρ_val`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L47).

```lean
lemma ComplexVector.basis_ρ_val (M : SL(2,ℂ)) (v : ComplexVector) :
    ((ComplexVector.SL2CRep M) v).val =
    LorentzGroup.toComplex (SL2C.toLorentzGroup M) *ᵥ v.val
```

**`Lorentz.ComplexVector.basisFin4`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L53).

> The standard basis of complex contravariant Lorentz vectors indexed by `Fin 4`.

```lean
def ComplexVector.basisFin4 : Basis (Fin 4) ℂ ComplexVector
```

**`Lorentz.ComplexVector.basisFin4_eq_reindex`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L56).

```lean
lemma ComplexVector.basisFin4_eq_reindex :
    ComplexVector.basisFin4 = ComplexVector.basis.reindex finSumFinEquiv
```

**`Lorentz.ComplexVector.basis_reindex_apply_eq_fin4`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L60).

```lean
lemma ComplexVector.basis_reindex_apply_eq_fin4 (j : Fin 4) :
    (ComplexVector.basis.reindex finSumFinEquiv) j = ComplexVector.basisFin4 j
```

**`Lorentz.ComplexVector.basisFin4_apply_zero`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L65).

```lean
lemma ComplexVector.basisFin4_apply_zero :
    ComplexVector.basisFin4 0 = ComplexVector.basis (Sum.inl 0)
```

**`Lorentz.ComplexVector.basisFin4_apply_one`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L71).

```lean
lemma ComplexVector.basisFin4_apply_one :
    ComplexVector.basisFin4 1 = ComplexVector.basis (Sum.inr 0)
```

**`Lorentz.ComplexVector.basisFin4_apply_two`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L77).

```lean
lemma ComplexVector.basisFin4_apply_two :
    ComplexVector.basisFin4 2 = ComplexVector.basis (Sum.inr 1)
```

**`Lorentz.ComplexVector.basisFin4_apply_three`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L83).

```lean
lemma ComplexVector.basisFin4_apply_three :
    ComplexVector.basisFin4 3 = ComplexVector.basis (Sum.inr 2)
```

**`Lorentz.ComplexVector.basisFin4_apply_succ`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L89).

```lean
lemma ComplexVector.basisFin4_apply_succ (i : Fin 3) :
    ComplexVector.basisFin4 i.succ = ComplexVector.basis (Sum.inr i)
```

**`Lorentz.ComplexCoVector.basis`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L96).

> The standard basis of complex covariant Lorentz vectors.

```lean
def ComplexCoVector.basis : Basis (Fin 1 ⊕ Fin 3) ℂ ComplexCoVector
```

**`Lorentz.ComplexCoVector.basis_toFin13ℂ`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L100).

```lean
lemma ComplexCoVector.basis_toFin13ℂ (i :Fin 1 ⊕ Fin 3) :
    (ComplexCoVector.basis i).toFin13ℂ = Pi.single i 1
```

**`Lorentz.ComplexCoVector.basis_ρ_apply`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L106).

```lean
lemma ComplexCoVector.basis_ρ_apply (M : SL(2,ℂ)) (i j : Fin 1 ⊕ Fin 3) :
    (LinearMap.toMatrix ComplexCoVector.basis ComplexCoVector.basis)
      (ComplexCoVector.SL2CRep M) i j =
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M))⁻¹ᵀ i j
```

**`Lorentz.ComplexCoVector.SL2CRep_val`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L116).

```lean
lemma ComplexCoVector.SL2CRep_val (M : SL(2,ℂ)) (v : ComplexCoVector) :
    ((ComplexCoVector.SL2CRep M) v).val =
    (LorentzGroup.toComplex (SL2C.toLorentzGroup M))⁻¹ᵀ *ᵥ v.val
```

**`Lorentz.ComplexCoVector.basisFin4`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L122).

> The standard basis of complex covariant Lorentz vectors indexed by `Fin 4`.

```lean
def ComplexCoVector.basisFin4 : Basis (Fin 4) ℂ ComplexCoVector
```

**`Lorentz.ComplexCoVector.basisFin4_eq_reindex`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L125).

```lean
lemma ComplexCoVector.basisFin4_eq_reindex :
    ComplexCoVector.basisFin4 = ComplexCoVector.basis.reindex finSumFinEquiv
```

**`Lorentz.ComplexCoVector.basis_reindex_apply_eq_fin4`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L129).

```lean
lemma ComplexCoVector.basis_reindex_apply_eq_fin4 (j : Fin 4) :
    (ComplexCoVector.basis.reindex finSumFinEquiv) j = ComplexCoVector.basisFin4 j
```

**`Lorentz.ComplexCoVector.basisFin4_apply_zero`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L134).

```lean
lemma ComplexCoVector.basisFin4_apply_zero :
    ComplexCoVector.basisFin4 0 = ComplexCoVector.basis (Sum.inl 0)
```

**`Lorentz.ComplexCoVector.basisFin4_apply_one`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L140).

```lean
lemma ComplexCoVector.basisFin4_apply_one :
    ComplexCoVector.basisFin4 1 = ComplexCoVector.basis (Sum.inr 0)
```

**`Lorentz.ComplexCoVector.basisFin4_apply_two`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L146).

```lean
lemma ComplexCoVector.basisFin4_apply_two :
    ComplexCoVector.basisFin4 2 = ComplexCoVector.basis (Sum.inr 1)
```

**`Lorentz.ComplexCoVector.basisFin4_apply_three`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L152).

```lean
lemma ComplexCoVector.basisFin4_apply_three :
    ComplexCoVector.basisFin4 3 = ComplexCoVector.basis (Sum.inr 2)
```

## Relation to real

**`Lorentz.inclCongrRealLorentz`**, a def, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L165).

> The semilinear map including real Lorentz vectors into complex contravariant
> lorentz vectors.

```lean
def inclCongrRealLorentz : ContrMod 3 →ₛₗ[Complex.ofRealHom] ComplexVector
```

**`Lorentz.inclCongrRealLorentz_val`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L180).

```lean
lemma inclCongrRealLorentz_val (v : ContrMod 3) :
    (inclCongrRealLorentz v).val = ofRealHom ∘ v.toFin1dℝ
```

**`Lorentz.ComplexVector.basis_of_real`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L183).

```lean
lemma ComplexVector.basis_of_real (i : Fin 1 ⊕ Fin 3) :
    (ComplexVector.basis i) = inclCongrRealLorentz (ContrMod.stdBasis i)
```

**`Lorentz.inclCongrRealLorentz_ρ`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L198).

```lean
lemma inclCongrRealLorentz_ρ (M : SL(2, ℂ)) (v : ContrMod 3) :
    (ComplexVector.SL2CRep M) (inclCongrRealLorentz v) =
    inclCongrRealLorentz (ContrMod.rep (SL2C.toLorentzGroup M) v)
```

**`Lorentz.SL2CRep_ρ_basis`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L206).

```lean
lemma SL2CRep_ρ_basis (M : SL(2, ℂ)) (i : Fin 1 ⊕ Fin 3) :
    (ComplexVector.SL2CRep M) (ComplexVector.basis i) =
    ∑ j, (SL2C.toLorentzGroup M).1 j i •
    ComplexVector.basis j
```

**`Lorentz.inclCoRealLorentz`**, a def, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L219).

> The semilinear map including real Lorentz co-vectors into complex covariant
> Lorentz vectors.

```lean
def inclCoRealLorentz : CoMod 3 →ₛₗ[Complex.ofRealHom] ComplexCoVector
```

**`Lorentz.inclCoRealLorentz_val`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L232).

```lean
lemma inclCoRealLorentz_val (v : CoMod 3) :
    (inclCoRealLorentz v).val = ofRealHom ∘ v.toFin1dℝ
```

**`Lorentz.ComplexCoVector.basis_of_real`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L235).

```lean
lemma ComplexCoVector.basis_of_real (i : Fin 1 ⊕ Fin 3) :
    (ComplexCoVector.basis i) = inclCoRealLorentz (CoMod.stdBasis i)
```

**`Lorentz.inclCoRealLorentz_ρ`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean#L250).

```lean
lemma inclCoRealLorentz_ρ (M : SL(2, ℂ)) (v : CoMod 3) :
    (ComplexCoVector.SL2CRep M) (inclCoRealLorentz v) =
    inclCoRealLorentz (CoMod.rep (SL2C.toLorentzGroup M) v)
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Vector.Modules](complextensor-vector-modules.md)

## Sources

- [Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Basic.lean)

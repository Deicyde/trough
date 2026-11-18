---
declaration: module
origin: cited
lean: Lorentz.contrModCoModBi, Lorentz.coModContrModBi, Lorentz.ContrMod.contr, Lorentz.ContrMod.contr_tmul, Lorentz.CoMod.contr, Lorentz.CoMod.contr_tmul, Lorentz.ContrMod.contr_tmul_symm, Lorentz.CoMod.contr_tmul_symm
statement: formalized
proof: formalized
---

# Contraction of Real Lorentz vectors

The module `Physlib.Relativity.Tensors.RealTensor.Vector.Pre.Contraction`, [Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean): 40 declarations, 8 with a docstring.

**`Lorentz.contrModCoModBi`**, a def, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L33).

> The bi-linear map corresponding to contraction of a contravariant Lorentz vector with a
> covariant Lorentz vector.

```lean
def contrModCoModBi (d : ℕ) : ContrMod d →ₗ[ℝ] CoMod d →ₗ[ℝ] ℝ
```

**`Lorentz.coModContrModBi`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L57).

> The bi-linear map corresponding to contraction of a covariant Lorentz vector with a
> contravariant Lorentz vector.

```lean
def coModContrModBi (d : ℕ) : CoMod d →ₗ[ℝ] ContrMod d →ₗ[ℝ] ℝ
```

**`Lorentz.ContrMod.contr`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L84).

> The linear map from ContrMod d ⊗ CoMod d to ℝ given by
> summing over components of contravariant Lorentz vector and
> covariant Lorentz vector in the
> standard basis (i.e. the dot product).
> In terms of index notation this is the contraction is ψⁱ φᵢ.

```lean
def ContrMod.contr : ((ContrMod.rep).tprod (CoMod.rep)).IntertwiningMap
    (Representation.trivial ℝ (LorentzGroup d) ℝ)
```

**`Lorentz.ContrMod.contr_tmul`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L101).

```lean
lemma ContrMod.contr_tmul (ψ : ContrMod d) (φ : CoMod d) :
    ⟪ψ, φ⟫ₘ = ψ.toFin1dℝ ⬝ᵥ φ.toFin1dℝ
```

**`Lorentz.CoMod.contr`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L110).

> The linear map from CoMod d ⊗ ContrMod d to ℝ given by
> summing over components of contravariant Lorentz vector and
> covariant Lorentz vector in the
> standard basis (i.e. the dot product).
> In terms of index notation this is the contraction is ψⁱ φᵢ.

```lean
def CoMod.contr : ((CoMod.rep (d := d)).tprod (ContrMod.rep (d := d))).IntertwiningMap
    (Representation.trivial ℝ (LorentzGroup d) ℝ)
```

**`Lorentz.CoMod.contr_tmul`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L124).

```lean
lemma CoMod.contr_tmul (φ : CoMod d) (ψ : ContrMod d) :
    ⟪φ, ψ⟫ₘ = φ.toFin1dℝ ⬝ᵥ ψ.toFin1dℝ
```

## Symmetry relations

**`Lorentz.ContrMod.contr_tmul_symm`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L134).

```lean
lemma ContrMod.contr_tmul_symm (φ : ContrMod d) (ψ : CoMod d) : ⟪φ, ψ⟫ₘ = ⟪ψ, φ⟫ₘ
```

**`Lorentz.CoMod.contr_tmul_symm`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L137).

```lean
lemma CoMod.contr_tmul_symm (φ : CoMod d) (ψ : ContrMod d) : ⟪φ, ψ⟫ₘ = ⟪ψ, φ⟫ₘ
```

## Contracting contr vectors with contr vectors etc.

**`Lorentz.contrContrContract`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L150).

> The linear map from ContrMod d ⊗ ContrMod d to ℝ induced by the homomorphism
> `Contr.toCo` and the contraction `ContrMod.contr`.

```lean
def contrContrContract : ((ContrMod.rep (d := d)).tprod (ContrMod.rep (d := d))).IntertwiningMap
    (Representation.trivial ℝ (LorentzGroup d) ℝ)
```

**`Lorentz.contrContrContractField`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L156).

> The linear map from ContrMod d ⊗ ContrMod d to ℝ induced by the homomorphism
> `Contr.toCo` and the contraction `ContrMod.contr`.

```lean
def contrContrContractField : ContrMod d ⊗[ℝ] ContrMod d →ₗ[ℝ] ℝ
```

**`Lorentz.contrContrContract_hom_tmul`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L162).

```lean
lemma contrContrContract_hom_tmul (φ : ContrMod d) (ψ : ContrMod d) :
    ⟪φ, ψ⟫ₘ = φ.toFin1dℝ ⬝ᵥ η *ᵥ ψ.toFin1dℝ
```

**`Lorentz.coCoContract`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L168).

> The linear map from CoMod d ⊗ CoMod d to ℝ induced by the homomorphism
> `Co.toContr` and the contraction `CoMod.contr`.

```lean
def coCoContract : ((CoMod.rep (d := d)).tprod (CoMod.rep (d := d))).IntertwiningMap
    (Representation.trivial ℝ (LorentzGroup d) ℝ)
```

**`Lorentz.coCoContract_hom_tmul`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L175).

```lean
lemma coCoContract_hom_tmul (φ : CoMod d) (ψ : CoMod d) :
    ⟪φ, ψ⟫ₘ = φ.toFin1dℝ ⬝ᵥ η *ᵥ ψ.toFin1dℝ
```

## Lemmas related to contraction.

> We derive the lemmas in main for `contrContrContractField`.

**`Lorentz.contrContrContractField.action_tmul`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L190).

```lean
lemma action_tmul (g : LorentzGroup d) : ⟪ContrMod.rep g x, ContrMod.rep g y⟫ₘ = ⟪x, y⟫ₘ
```

**`Lorentz.contrContrContractField.as_sum`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L193).

```lean
lemma as_sum : ⟪x, y⟫ₘ = x.val (Sum.inl 0) * y.val (Sum.inl 0) -
    ∑ i, x.val (Sum.inr i) * y.val (Sum.inr i)
```

**`Lorentz.contrContrContractField.as_sum_toSpace`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L203).

```lean
lemma as_sum_toSpace : ⟪x, y⟫ₘ = x.val (Sum.inl 0) * y.val (Sum.inl 0) -
    ⟪x.toSpace, y.toSpace⟫_ℝ
```

**`Lorentz.contrContrContractField.stdBasis_inl`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L211).

```lean
lemma stdBasis_inl {d : ℕ} :
    ⟪@ContrMod.stdBasis d (Sum.inl 0), ContrMod.stdBasis (Sum.inl 0)⟫ₘ = (1 : ℝ)
```

**`Lorentz.contrContrContractField.symm`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L223).

```lean
lemma symm : ⟪x, y⟫ₘ = ⟪y, x⟫ₘ
```

**`Lorentz.contrContrContractField.dual_mulVec_right`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L231).

```lean
lemma dual_mulVec_right : ⟪x, dual Λ *ᵥ y⟫ₘ = ⟪Λ *ᵥ x, y⟫ₘ
```

**`Lorentz.contrContrContractField.dual_mulVec_left`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L237).

```lean
lemma dual_mulVec_left : ⟪dual Λ *ᵥ x, y⟫ₘ = ⟪x, Λ *ᵥ y⟫ₘ
```

**`Lorentz.contrContrContractField.right_parity`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L240).

```lean
lemma right_parity : ⟪x, ContrMod.rep LorentzGroup.parity y⟫ₘ = ∑ i, x.val i * y.val i
```

**`Lorentz.contrContrContractField.self_parity_eq_zero_iff`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L258).

```lean
lemma self_parity_eq_zero_iff : ⟪y, ContrMod.rep LorentzGroup.parity y⟫ₘ = 0 ↔ y = 0
```

**`Lorentz.contrContrContractField.nondegenerate`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L275).

> The metric tensor is non-degenerate.

```lean
lemma nondegenerate : (∀ (x : ContrMod d), ⟪x, y⟫ₘ = 0) ↔ y = 0
```

**`Lorentz.contrContrContractField.matrix_apply_eq_iff_sub`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L280).

```lean
lemma matrix_apply_eq_iff_sub : ⟪x, Λ *ᵥ y⟫ₘ = ⟪x, Λ' *ᵥ y⟫ₘ ↔ ⟪x, (Λ - Λ') *ᵥ y⟫ₘ = 0
```

**`Lorentz.contrContrContractField.matrix_eq_iff_eq_forall'`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L283).

```lean
lemma matrix_eq_iff_eq_forall' : (∀ (v : ContrMod d), (Λ *ᵥ v) = Λ' *ᵥ v) ↔
    ∀ (w v : ContrMod d), ⟪v, Λ *ᵥ w⟫ₘ = ⟪v, Λ' *ᵥ w⟫ₘ
```

**`Lorentz.contrContrContractField.matrix_eq_iff_eq_forall`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L294).

```lean
lemma matrix_eq_iff_eq_forall : Λ = Λ' ↔ ∀ (w v : ContrMod d), ⟪v, Λ *ᵥ w⟫ₘ = ⟪v, Λ' *ᵥ w⟫ₘ
```

**`Lorentz.contrContrContractField.matrix_eq_id_iff`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L303).

```lean
lemma matrix_eq_id_iff : Λ = 1 ↔ ∀ (w v : ContrMod d), ⟪v, Λ *ᵥ w⟫ₘ = ⟪v, w⟫ₘ
```

**`LorentzGroup.mem_iff_invariant`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L307).

```lean
lemma _root_.LorentzGroup.mem_iff_invariant : Λ ∈ LorentzGroup d ↔
    ∀ (w v : ContrMod d), ⟪Λ *ᵥ v, Λ *ᵥ w⟫ₘ = ⟪v, w⟫ₘ
```

**`LorentzGroup.mem_iff_norm`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L321).

```lean
lemma _root_.LorentzGroup.mem_iff_norm : Λ ∈ LorentzGroup d ↔
    ∀ (w : ContrMod d), ⟪Λ *ᵥ w, Λ *ᵥ w⟫ₘ = ⟪w, w⟫ₘ
```

## Some equalities and inequalities

**`Lorentz.contrContrContractField.inl_sq_eq`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L347).

```lean
lemma inl_sq_eq (v : ContrMod d) : v.val (Sum.inl 0) ^ 2 =
    (⟪v, v⟫ₘ) + ∑ i, v.val (Sum.inr i) ^ 2
```

**`Lorentz.contrContrContractField.le_inl_sq`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L356).

```lean
lemma le_inl_sq (v : ContrMod d) : ⟪v, v⟫ₘ ≤ v.val (Sum.inl 0) ^ 2
```

**`Lorentz.contrContrContractField.ge_abs_inner_product`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L362).

```lean
lemma ge_abs_inner_product (v w : ContrMod d) : v.val (Sum.inl 0) * w.val (Sum.inl 0) -
    ‖⟪v.toSpace, w.toSpace⟫_ℝ‖ ≤ ⟪v, w⟫ₘ
```

**`Lorentz.contrContrContractField.ge_sub_norm`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L367).

```lean
lemma ge_sub_norm (v w : ContrMod d) : v.val (Sum.inl 0) * w.val (Sum.inl 0) -
    ‖v.toSpace‖ * ‖w.toSpace‖ ≤ ⟪v, w⟫ₘ
```

## The Minkowski metric and the standard basis

**`Lorentz.contrContrContractField.basis_left`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L380).

```lean
lemma basis_left {v : ContrMod d} (μ : Fin 1 ⊕ Fin d) :
    ⟪ ContrMod.stdBasis μ, v⟫ₘ = η μ μ * v.toFin1dℝ μ
```

**`Lorentz.contrContrContractField.on_basis_mulVec`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L394).

```lean
lemma on_basis_mulVec (μ ν : Fin 1 ⊕ Fin d) :
    ⟪ContrMod.stdBasis μ, Λ *ᵥ ContrMod.stdBasis ν⟫ₘ = η μ μ * Λ μ ν
```

**`Lorentz.contrContrContractField.on_basis`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L399).

```lean
lemma on_basis (μ ν : Fin 1 ⊕ Fin d) : ⟪ContrMod.stdBasis μ, ContrMod.stdBasis ν⟫ₘ = η μ ν
```

**`Lorentz.contrContrContractField.matrix_apply_stdBasis`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L408).

```lean
lemma matrix_apply_stdBasis (ν μ : Fin 1 ⊕ Fin d) :
    Λ ν μ = η ν ν * ⟪ContrMod.stdBasis ν, Λ *ᵥ ContrMod.stdBasis μ⟫ₘ
```

## Self-adjoint

**`Lorentz.contrContrContractField.same_eq_det_toSelfAdjoint`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L419).

```lean
lemma same_eq_det_toSelfAdjoint (x : ContrMod 3) :
    ⟪x, x⟫ₘ = det (ContrMod.toSelfAdjoint x).1
```

## The contraction on the basis

**`Lorentz.ContrMod.contr_basis`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L443).

```lean
lemma ContrMod.contr_basis {d : ℕ} (i j : Fin 1 ⊕ Fin d) :
    ContrMod.contr (contrBasis d i ⊗ₜ coBasis d j) = if i = j then (1 : ℝ) else 0
```

**`Lorentz.CoMod.contr_basis`**, a lemma, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean#L451).

```lean
lemma CoMod.contr_basis {d : ℕ} (i j : Fin 1 ⊕ Fin d) :
    CoMod.contr (coBasis d i ⊗ₜ[ℝ] contrBasis d j) = if i = j then (1 : ℝ) else 0
```

## Depends on

- [Real Lorentz vectors](realtensor-vector-pre-basic.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Contraction.lean)

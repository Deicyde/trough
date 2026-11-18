---
declaration: module
origin: cited
lean: Fermion.DualLeftHandedWeyl.unitVal, Fermion.DualLeftHandedWeyl.unitVal_expand_tmul, Fermion.DualLeftHandedWeyl.unit, Fermion.DualLeftHandedWeyl.unit_apply_one, Fermion.LeftHandedWeyl.unitVal, Fermion.LeftHandedWeyl.unitVal_expand_tmul, Fermion.LeftHandedWeyl.unit, Fermion.LeftHandedWeyl.unit_apply_one
statement: formalized
proof: formalized
---

# Units of Weyl fermions

The module `Physlib.Relativity.Fermions.Weyl.Unit`, [Physlib/Relativity/Fermions/Weyl/Unit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean): 24 declarations, 17 with a docstring.

> We define the units for Weyl fermions, often denoted `δ` in the literature.

**`Fermion.DualLeftHandedWeyl.unitVal`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L30).

> The left-dual-left unit `δᵃₐ` as an element of `(leftHanded ⊗ dualLeftHanded).V`.

```lean
def DualLeftHandedWeyl.unitVal : (LeftHandedWeyl ⊗[ℂ] DualLeftHandedWeyl)
```

**`Fermion.DualLeftHandedWeyl.unitVal_expand_tmul`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L34).

> Expansion of `DualLeftHandedWeyl.unitVal` into the basis.

```lean
lemma DualLeftHandedWeyl.unitVal_expand_tmul : DualLeftHandedWeyl.unitVal =
    LeftHandedWeyl.basis 0 ⊗ₜ[ℂ] DualLeftHandedWeyl.basis 0 +
      LeftHandedWeyl.basis 1 ⊗ₜ[ℂ] DualLeftHandedWeyl.basis 1
```

**`Fermion.DualLeftHandedWeyl.unit`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L44).

> The left-dual-left unit `δᵃₐ` as a morphism `𝟙_ (Rep ℂ SL(2,ℂ)) ⟶ leftHanded ⊗ dualLeftHanded `,
> manifesting the invariance under the `SL(2,ℂ)` action.

```lean
def DualLeftHandedWeyl.unit : (Representation.trivial ℂ SL(2,ℂ) ℂ).IntertwiningMap
    (LeftHandedWeyl.rep.tprod DualLeftHandedWeyl.rep)
```

**`Fermion.DualLeftHandedWeyl.unit_apply_one`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L66).

```lean
lemma DualLeftHandedWeyl.unit_apply_one :
    DualLeftHandedWeyl.unit (1 : ℂ) = DualLeftHandedWeyl.unitVal
```

**`Fermion.LeftHandedWeyl.unitVal`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L72).

> The dual-left-left unit `δₐᵃ` as an element of `(dualLeftHanded ⊗ leftHanded).V`.

```lean
def LeftHandedWeyl.unitVal : (DualLeftHandedWeyl ⊗[ℂ] LeftHandedWeyl)
```

**`Fermion.LeftHandedWeyl.unitVal_expand_tmul`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L76).

> Expansion of `LeftHandedWeyl.unitVal` into the basis.

```lean
lemma LeftHandedWeyl.unitVal_expand_tmul : LeftHandedWeyl.unitVal =
    DualLeftHandedWeyl.basis 0 ⊗ₜ[ℂ] LeftHandedWeyl.basis 0 +
      DualLeftHandedWeyl.basis 1 ⊗ₜ[ℂ] LeftHandedWeyl.basis 1
```

**`Fermion.LeftHandedWeyl.unit`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L86).

> The dual-left-left unit `δₐᵃ` as a morphism `𝟙\_ (Rep ℂ SL(2,ℂ)) ⟶
> dualLeftHanded ⊗ leftHanded `, manifesting the invariance under the `SL(2,ℂ)` action.

```lean
def LeftHandedWeyl.unit :
    (Representation.trivial ℂ SL(2,ℂ) ℂ).IntertwiningMap
      (DualLeftHandedWeyl.rep.tprod LeftHandedWeyl.rep)
```

**`Fermion.LeftHandedWeyl.unit_apply_one`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L111).

> Applying the morphism `LeftHandedWeyl.unit` to `1` returns `LeftHandedWeyl.unitVal`.

```lean
lemma LeftHandedWeyl.unit_apply_one : LeftHandedWeyl.unit (1 : ℂ) = LeftHandedWeyl.unitVal
```

**`Fermion.DualRightHandedWeyl.unitVal`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L117).

> The right-dual-right unit `δ^{dot a}_{dot a}` as an element of
> `(rightHanded ⊗ dualRightHanded).V`.

```lean
def DualRightHandedWeyl.unitVal : RightHandedWeyl ⊗[ℂ] DualRightHandedWeyl
```

**`Fermion.DualRightHandedWeyl.unitVal_expand_tmul`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L121).

> Expansion of `DualRightHandedWeyl.unitVal` into the basis.

```lean
lemma DualRightHandedWeyl.unitVal_expand_tmul : DualRightHandedWeyl.unitVal =
    RightHandedWeyl.basis 0 ⊗ₜ[ℂ] DualRightHandedWeyl.basis 0 +
      RightHandedWeyl.basis 1 ⊗ₜ[ℂ] DualRightHandedWeyl.basis 1
```

**`Fermion.DualRightHandedWeyl.unit`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L132).

> The right-dual-right unit `δ^{dot a}_{dot a}` as a morphism
> `𝟙_ (Rep ℂ SL(2,ℂ)) ⟶ rightHanded ⊗ dualRightHanded`, manifesting
> the invariance under the `SL(2,ℂ)` action.

```lean
def DualRightHandedWeyl.unit : (Representation.trivial ℂ SL(2,ℂ) ℂ).IntertwiningMap
    (RightHandedWeyl.rep.tprod DualRightHandedWeyl.rep)
```

**`Fermion.DualRightHandedWeyl.unit_apply_one`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L160).

```lean
lemma DualRightHandedWeyl.unit_apply_one :
    DualRightHandedWeyl.unit (1 : ℂ) = DualRightHandedWeyl.unitVal
```

**`Fermion.RightHandedWeyl.unitVal`**, a def, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L167).

> The dual-right-right unit `δ_{dot a}^{dot a}` as an element of
> `(rightHanded ⊗ dualRightHanded).V`.

```lean
def RightHandedWeyl.unitVal : (DualRightHandedWeyl ⊗[ℂ] RightHandedWeyl)
```

**`Fermion.RightHandedWeyl.unitVal_expand_tmul`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L171).

> Expansion of `RightHandedWeyl.unitVal` into the basis.

```lean
lemma RightHandedWeyl.unitVal_expand_tmul : RightHandedWeyl.unitVal =
    DualRightHandedWeyl.basis 0 ⊗ₜ[ℂ] RightHandedWeyl.basis 0 +
      DualRightHandedWeyl.basis 1 ⊗ₜ[ℂ] RightHandedWeyl.basis 1
```

**`Fermion.RightHandedWeyl.unit`**, a def, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L182).

> The dual-right-right unit `δ_{dot a}^{dot a}` as a morphism
> `𝟙_ (Rep ℂ SL(2,ℂ)) ⟶ dualRightHanded ⊗ rightHanded`, manifesting
> the invariance under the `SL(2,ℂ)` action.

```lean
def RightHandedWeyl.unit : (Representation.trivial ℂ SL(2,ℂ) ℂ).IntertwiningMap
    (DualRightHandedWeyl.rep.tprod RightHandedWeyl.rep)
```

**`Fermion.RightHandedWeyl.unit_apply_one`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L208).

```lean
lemma RightHandedWeyl.unit_apply_one : RightHandedWeyl.unit (1 : ℂ) = RightHandedWeyl.unitVal
```

## Contraction of the units

**`Fermion.LeftHandedWeyl.contr_unit`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L219).

> Contraction on the right with `LeftHandedWeyl.unit` does nothing.

```lean
lemma LeftHandedWeyl.contr_unit (x : LeftHandedWeyl) :
    (TensorProduct.lid ℂ _ <|
    LeftHandedWeyl.contr.toLinearMap.rTensor _ <|
    (TensorProduct.assoc ℂ _ _ _).symm <|
    x ⊗ₜ[ℂ] (LeftHandedWeyl.unit (1 : ℂ))) = x
```

**`Fermion.DualLeftHandedWeyl.contr_unit`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L231).

> Contraction on the right with `DualLeftHandedWeyl.unit` does nothing.

```lean
lemma DualLeftHandedWeyl.contr_unit (x : DualLeftHandedWeyl) :
    (TensorProduct.lid ℂ _ <|
    DualLeftHandedWeyl.contr.toLinearMap.rTensor _ <|
    (TensorProduct.assoc ℂ _ _ _).symm <|
    x ⊗ₜ[ℂ] (DualLeftHandedWeyl.unit (1 : ℂ))) = x
```

**`Fermion.RightHandedWeyl.contr_unit`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L243).

> Contraction on the right with `RightHandedWeyl.unit` does nothing.

```lean
lemma RightHandedWeyl.contr_unit (x : RightHandedWeyl) :
    (TensorProduct.lid ℂ _ <|
    RightHandedWeyl.contr.toLinearMap.rTensor _ <|
    (TensorProduct.assoc ℂ _ _ _).symm <|
    x ⊗ₜ[ℂ] (RightHandedWeyl.unit (1 : ℂ))) = x
```

**`Fermion.DualRightHandedWeyl.contr_unit`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L255).

> Contraction on the right with `DualRightHandedWeyl.unit` does nothing.

```lean
lemma DualRightHandedWeyl.contr_unit (x : DualRightHandedWeyl) :
    (TensorProduct.lid ℂ _ <|
    DualRightHandedWeyl.contr.toLinearMap.rTensor _ <|
    (TensorProduct.assoc ℂ _ _ _).symm <|
    x ⊗ₜ[ℂ] (DualRightHandedWeyl.unit (1 : ℂ))) = x
```

## Symmetry properties of the units

**`Fermion.LeftHandedWeyl.unit_symm`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L273).

```lean
lemma LeftHandedWeyl.unit_symm :
    LeftHandedWeyl.unit (1 : ℂ) = LinearMap.lTensor _ (LinearEquiv.refl _ _).toLinearMap
    (TensorProduct.comm ℂ _ _ (DualLeftHandedWeyl.unit (1 : ℂ)))
```

**`Fermion.DualLeftHandedWeyl.unit_symm`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L280).

```lean
lemma DualLeftHandedWeyl.unit_symm :
    DualLeftHandedWeyl.unit (1 : ℂ) = LinearMap.lTensor _ (LinearEquiv.refl _ _).toLinearMap
      (TensorProduct.comm ℂ _ _ (LeftHandedWeyl.unit (1 : ℂ)))
```

**`Fermion.RightHandedWeyl.unit_symm`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L287).

```lean
lemma RightHandedWeyl.unit_symm :
    RightHandedWeyl.unit (1 : ℂ) = LinearMap.lTensor _ (LinearEquiv.refl _ _).toLinearMap
      (TensorProduct.comm ℂ _ _ (DualRightHandedWeyl.unit (1 : ℂ)))
```

**`Fermion.DualRightHandedWeyl.unit_symm`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean#L294).

```lean
lemma DualRightHandedWeyl.unit_symm :
    DualRightHandedWeyl.unit (1 : ℂ) = LinearMap.lTensor _ (LinearEquiv.refl _ _).toLinearMap
      (TensorProduct.comm ℂ _ _ (RightHandedWeyl.unit (1 : ℂ)))
```

## Depends on

- [Contraction of Weyl fermions](contraction.md)
- [Tensor product of two Weyl fermion](two.md)

## Sources

- [Physlib/Relativity/Fermions/Weyl/Unit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Unit.lean)

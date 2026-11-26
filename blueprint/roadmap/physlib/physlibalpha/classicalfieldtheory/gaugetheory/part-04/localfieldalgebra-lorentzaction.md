---
declaration: module
origin: cited
lean: GaugeFieldData.lorentzConnection, GaugeFieldData.lorentzAssignment, GaugeFieldData.repLorentzAlgHom, GaugeFieldData.repLorentzAlgHom_ιFermion, GaugeFieldData.repLorentzAlgHom_ιBoson, GaugeFieldData.repLorentzAlgHom_ιConnection, GaugeFieldData.repLorentzAlgHom_comp_includeConnection, GaugeFieldData.repLorentzAlgHom_includeConnection
statement: formalized
proof: formalized
---

# The Lorentz action on the local field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.LorentzAction`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean): 20 declarations, 11 with a docstring.

> The action of `SL(2,ℂ)` on the local field algebra by algebra endomorphisms.

## i. Overview

> The Lorentz group `SL(2,ℂ)` acts on the local field algebra `J(T)` of a field datum by
> algebra endomorphisms. It acts on the generators of a matter species by the action
> `FieldDerivSpace.repLorentzGroup` of that species, mixing the derivative label and the
> target index, and on the connection generators by the gauge-only action
> `LocalGaugeFieldAlgebra.repLorentzGroup`. The construction is that of the jet gauge action
> in `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.GaugeAction`, the lift of a
> compatible assignment, with the representation laws from uniqueness.

## ii. Key results

> - `GaugeFieldData.repLorentzAlgHom`, `GaugeFieldData.repLorentzGroup` : the action of a
>   Lorentz transformation, as an algebra endomorphism and as a representation, with
>   `repLorentzGroup_ιFermion`, `repLorentzGroup_ιBoson`, `repLorentzGroup_ιConnection` on the
>   generators.
> - `GaugeFieldData.repLorentzGroup_includeConnection` : on the connection factor the action
>   is the complexified gauge-only action.
> - `GaugeFieldData.repLorentzGroup_ιConnection_eq` : the law of the connection generators.

## iv. References

> * None.

## A. The Lorentz assignment of a transformation

**`GaugeFieldData.lorentzConnection`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L63).

> The connection generators after a Lorentz transformation, the gauge-only action on the
> degree-one element, included into the local field algebra.

```lean
noncomputable def lorentzConnection (Λ : SL(2,ℂ)) :
    GaugeBoson.FieldDerivSpace G →ₗ[ℝ] T.LocalFieldAlgebra
```

**`GaugeFieldData.lorentzAssignment`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L75).

> The assignment of the generators defining the action of a Lorentz transformation. Each
> matter species acts on its own component functions, the connection generators through
> the gauge-only action.

```lean
noncomputable def lorentzAssignment (Λ : SL(2,ℂ)) : T.Assignment T.LocalFieldAlgebra
```

## B. The action of a transformation

**`GaugeFieldData.repLorentzAlgHom`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L95).

> The action of a Lorentz transformation on the local field algebra, as an algebra
> endomorphism, the lift of its Lorentz assignment.

```lean
noncomputable def repLorentzAlgHom (Λ : SL(2,ℂ)) :
    T.LocalFieldAlgebra →ₐ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.repLorentzAlgHom_ιFermion`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L102).

```lean
lemma repLorentzAlgHom_ιFermion (Λ : SL(2,ℂ)) (i : T.FermionSpecies)
    (x : FieldDerivSpace (T.fermion i)) :
    T.repLorentzAlgHom Λ (T.ιFermion i x)
      = T.ιFermion i (FieldDerivSpace.repLorentzGroup (T.fermion i) Λ x)
```

**`GaugeFieldData.repLorentzAlgHom_ιBoson`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L109).

```lean
lemma repLorentzAlgHom_ιBoson (Λ : SL(2,ℂ)) (j : T.BosonSpecies)
    (y : FieldDerivSpace (T.boson j)) :
    T.repLorentzAlgHom Λ (T.ιBoson j y)
      = T.ιBoson j (FieldDerivSpace.repLorentzGroup (T.boson j) Λ y)
```

**`GaugeFieldData.repLorentzAlgHom_ιConnection`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L116).

```lean
lemma repLorentzAlgHom_ιConnection (Λ : SL(2,ℂ)) (v : GaugeBoson.FieldDerivSpace G) :
    T.repLorentzAlgHom Λ (T.ιConnection v)
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ]
          LocalGaugeFieldAlgebra.repLorentzGroup G Λ (SymmetricAlgebra.ι ℝ _ v))
```

## C. The action on the connection factor

**`GaugeFieldData.repLorentzAlgHom_comp_includeConnection`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L131).

> The action of a Lorentz transformation restricts to the complexified gauge-only action
> on the connection factor, as an equation of algebra maps out of the complexified
> gauge-only algebra, compared on the real generators.

```lean
lemma repLorentzAlgHom_comp_includeConnection (Λ : SL(2,ℂ)) :
    (T.repLorentzAlgHom Λ).comp T.includeConnection
      = T.includeConnection.comp (LocalGaugeFieldAlgebra.complexRepLorentzGroupAlgHom G Λ)
```

**`GaugeFieldData.repLorentzAlgHom_includeConnection`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L141).

> The action of a Lorentz transformation restricts to the complexified gauge-only action
> on the connection factor.

```lean
lemma repLorentzAlgHom_includeConnection (Λ : SL(2,ℂ)) (y : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G) :
    T.repLorentzAlgHom Λ (T.includeConnection y)
      = T.includeConnection (LocalGaugeFieldAlgebra.complexRepLorentzGroup G Λ y)
```

**`GaugeFieldData.repLorentzAlgHom_includeConnection_one_tmul`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L149).

> On the real gauge-only algebra, included, a Lorentz transformation acts through the
> gauge-only action.

```lean
lemma repLorentzAlgHom_includeConnection_one_tmul (Λ : SL(2,ℂ)) (x : LocalGaugeFieldAlgebra G) :
    T.repLorentzAlgHom Λ (T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ] x))
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ] LocalGaugeFieldAlgebra.repLorentzGroup G Λ
        x)
```

## D. The representation

**`GaugeFieldData.repLorentzAlgHom_one`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L162).

> The identity transformation acts as the identity.

```lean
lemma repLorentzAlgHom_one : T.repLorentzAlgHom 1 = AlgHom.id ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.repLorentzAlgHom_mul`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L170).

> The action of a product of transformations is the composite of the actions.

```lean
lemma repLorentzAlgHom_mul (Λ₁ Λ₂ : SL(2,ℂ)) :
    T.repLorentzAlgHom (Λ₁ * Λ₂) = (T.repLorentzAlgHom Λ₁).comp (T.repLorentzAlgHom Λ₂)
```

**`GaugeFieldData.repLorentzGroup`**, a def, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L187).

> The action of the Lorentz group on the local field algebra.

```lean
noncomputable def repLorentzGroup : Representation ℂ SL(2,ℂ) T.LocalFieldAlgebra
```

**`GaugeFieldData.repLorentzGroup_apply`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L194).

```lean
lemma repLorentzGroup_apply (Λ : SL(2,ℂ)) (x : T.LocalFieldAlgebra) :
    T.repLorentzGroup Λ x = T.repLorentzAlgHom Λ x
```

**`GaugeFieldData.repLorentzGroup_apply_mul`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L197).

```lean
lemma repLorentzGroup_apply_mul (Λ : SL(2,ℂ)) (x y : T.LocalFieldAlgebra) :
    T.repLorentzGroup Λ (x * y) = T.repLorentzGroup Λ x * T.repLorentzGroup Λ y
```

**`GaugeFieldData.repLorentzGroup_apply_one`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L201).

```lean
lemma repLorentzGroup_apply_one (Λ : SL(2,ℂ)) :
    T.repLorentzGroup Λ (1 : T.LocalFieldAlgebra) = 1
```

**`GaugeFieldData.repLorentzGroup_ιFermion`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L206).

```lean
lemma repLorentzGroup_ιFermion (Λ : SL(2,ℂ)) (i : T.FermionSpecies)
    (x : FieldDerivSpace (T.fermion i)) :
    T.repLorentzGroup Λ (T.ιFermion i x)
      = T.ιFermion i (FieldDerivSpace.repLorentzGroup (T.fermion i) Λ x)
```

**`GaugeFieldData.repLorentzGroup_ιBoson`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L213).

```lean
lemma repLorentzGroup_ιBoson (Λ : SL(2,ℂ)) (j : T.BosonSpecies)
    (y : FieldDerivSpace (T.boson j)) :
    T.repLorentzGroup Λ (T.ιBoson j y)
      = T.ιBoson j (FieldDerivSpace.repLorentzGroup (T.boson j) Λ y)
```

**`GaugeFieldData.repLorentzGroup_ιConnection`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L220).

```lean
lemma repLorentzGroup_ιConnection (Λ : SL(2,ℂ)) (v : GaugeBoson.FieldDerivSpace G) :
    T.repLorentzGroup Λ (T.ιConnection v)
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ]
          LocalGaugeFieldAlgebra.repLorentzGroup G Λ (SymmetricAlgebra.ι ℝ _ v))
```

**`GaugeFieldData.repLorentzGroup_includeConnection`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L228).

> The Lorentz action restricts to the complexified gauge-only action on the connection
> factor.

```lean
lemma repLorentzGroup_includeConnection (Λ : SL(2,ℂ)) (y : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G) :
    T.repLorentzGroup Λ (T.includeConnection y)
      = T.includeConnection (LocalGaugeFieldAlgebra.complexRepLorentzGroup G Λ y)
```

**`GaugeFieldData.repLorentzGroup_ιConnection_eq`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean#L237).

> The Lorentz law of the connection generators. A transformation carries a connection
> generator to the generator of the transformed component, with no shift. This is the
> generator-level form of `GaugeFieldData.repLorentzGroup_ιConnection`, with no reference
> to the connection factor.

```lean
lemma repLorentzGroup_ιConnection_eq (Λ : SL(2,ℂ)) (v : GaugeBoson.FieldDerivSpace G) :
    T.repLorentzGroup Λ (T.ιConnection v)
      = T.ιConnection (GaugeBoson.FieldDerivSpace.repLorentzGroup G Λ v)
```

## Depends on

- [The Lorentz action on the gauge-boson jet algebra](../part-01/gaugeboson-localgaugefieldalgebra-lorentzaction.md)
- [The local field algebra of a gauge theory and its universal property](localfieldalgebra-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/LorentzAction.lean)

---
declaration: module
origin: cited
lean: GaugeFieldData.lorentzConnection, GaugeFieldData.lorentzAssignment, GaugeFieldData.repLorentzAlgHom, GaugeFieldData.repLorentzAlgHom_ιFermion, GaugeFieldData.repLorentzAlgHom_ιBoson, GaugeFieldData.repLorentzAlgHom_ιConnection, GaugeFieldData.repLorentzAlgHom_comp_includeConnection, GaugeFieldData.repLorentzAlgHom_includeConnection
statement: formalized
proof: formalized
---

# The Lorentz action on the local field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalField.LorentzAction`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean): 20 declarations, 11 with a docstring.

## i. Overview

> The Lorentz group `SL(2,ℂ)` acts on the local field algebra `J(T)` of a field datum by
> algebra endomorphisms: on the generators of a matter species by the action
> `JetComponentSpace.repLorentzGroup` of that species, mixing the derivative label and the
> target index, and on the connection generators by the gauge-only action
> `LocalGaugeFieldAlgebra.repLorentzGroup`. The construction is that of the jet gauge action
> in `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalField.GaugeAction`: the lift of a
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

**`GaugeFieldData.lorentzConnection`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L63).

> The connection generators after a Lorentz transformation: the gauge-only action on the
> degree-one element, included into the local field algebra.

```lean
noncomputable def lorentzConnection (Λ : SL(2,ℂ)) :
    GaugeBoson.JetComponentSpace 𝔤 →ₗ[ℝ] T.LocalFieldAlgebra
```

**`GaugeFieldData.lorentzAssignment`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L74).

> The assignment of the generators defining the action of a Lorentz transformation: each
> matter species acts on its own component functions, the connection generators through
> the gauge-only action.

```lean
noncomputable def lorentzAssignment (Λ : SL(2,ℂ)) : T.Assignment T.LocalFieldAlgebra
```

## B. The action of a transformation

**`GaugeFieldData.repLorentzAlgHom`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L94).

> The action of a Lorentz transformation on the local field algebra, as an algebra
> endomorphism: the lift of its Lorentz assignment.

```lean
noncomputable def repLorentzAlgHom (Λ : SL(2,ℂ)) :
    T.LocalFieldAlgebra →ₐ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.repLorentzAlgHom_ιFermion`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L101).

```lean
lemma repLorentzAlgHom_ιFermion (Λ : SL(2,ℂ)) (i : T.FermionSpecies)
    (x : JetComponentSpace (T.fermion i)) :
    T.repLorentzAlgHom Λ (T.ιFermion i x)
      = T.ιFermion i (JetComponentSpace.repLorentzGroup (T.fermion i) Λ x)
```

**`GaugeFieldData.repLorentzAlgHom_ιBoson`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L108).

```lean
lemma repLorentzAlgHom_ιBoson (Λ : SL(2,ℂ)) (j : T.BosonSpecies)
    (y : JetComponentSpace (T.boson j)) :
    T.repLorentzAlgHom Λ (T.ιBoson j y)
      = T.ιBoson j (JetComponentSpace.repLorentzGroup (T.boson j) Λ y)
```

**`GaugeFieldData.repLorentzAlgHom_ιConnection`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L115).

```lean
lemma repLorentzAlgHom_ιConnection (Λ : SL(2,ℂ)) (v : GaugeBoson.JetComponentSpace 𝔤) :
    T.repLorentzAlgHom Λ (T.ιConnection v)
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ]
          LocalGaugeFieldAlgebra.repLorentzGroup 𝔤 Λ (SymmetricAlgebra.ι ℝ _ v))
```

## C. The action on the connection factor

**`GaugeFieldData.repLorentzAlgHom_comp_includeConnection`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L130).

> The action of a Lorentz transformation restricts to the complexified gauge-only action
> on the connection factor, as an equation of algebra maps out of the complexified
> gauge-only algebra, compared on the real generators.

```lean
lemma repLorentzAlgHom_comp_includeConnection (Λ : SL(2,ℂ)) :
    (T.repLorentzAlgHom Λ).comp T.includeConnection
      = T.includeConnection.comp (LocalGaugeFieldAlgebra.complexRepLorentzGroupAlgHom 𝔤 Λ)
```

**`GaugeFieldData.repLorentzAlgHom_includeConnection`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L140).

> The action of a Lorentz transformation restricts to the complexified gauge-only action
> on the connection factor.

```lean
lemma repLorentzAlgHom_includeConnection (Λ : SL(2,ℂ)) (y : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤) :
    T.repLorentzAlgHom Λ (T.includeConnection y)
      = T.includeConnection (LocalGaugeFieldAlgebra.complexRepLorentzGroup 𝔤 Λ y)
```

**`GaugeFieldData.repLorentzAlgHom_includeConnection_one_tmul`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L148).

> On the real gauge-only algebra, included, a Lorentz transformation acts through the
> gauge-only action.

```lean
lemma repLorentzAlgHom_includeConnection_one_tmul (Λ : SL(2,ℂ)) (x : LocalGaugeFieldAlgebra 𝔤) :
    T.repLorentzAlgHom Λ (T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ] x))
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ] LocalGaugeFieldAlgebra.repLorentzGroup 𝔤 Λ x)
```

## D. The representation

**`GaugeFieldData.repLorentzAlgHom_one`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L160).

> The identity transformation acts as the identity.

```lean
lemma repLorentzAlgHom_one : T.repLorentzAlgHom 1 = AlgHom.id ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.repLorentzAlgHom_mul`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L168).

> The action of a product of transformations is the composite of the actions.

```lean
lemma repLorentzAlgHom_mul (Λ₁ Λ₂ : SL(2,ℂ)) :
    T.repLorentzAlgHom (Λ₁ * Λ₂) = (T.repLorentzAlgHom Λ₁).comp (T.repLorentzAlgHom Λ₂)
```

**`GaugeFieldData.repLorentzGroup`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L185).

> The action of the Lorentz group on the local field algebra.

```lean
noncomputable def repLorentzGroup : Representation ℂ SL(2,ℂ) T.LocalFieldAlgebra
```

**`GaugeFieldData.repLorentzGroup_apply`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L192).

```lean
lemma repLorentzGroup_apply (Λ : SL(2,ℂ)) (x : T.LocalFieldAlgebra) :
    T.repLorentzGroup Λ x = T.repLorentzAlgHom Λ x
```

**`GaugeFieldData.repLorentzGroup_apply_mul`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L195).

```lean
lemma repLorentzGroup_apply_mul (Λ : SL(2,ℂ)) (x y : T.LocalFieldAlgebra) :
    T.repLorentzGroup Λ (x * y) = T.repLorentzGroup Λ x * T.repLorentzGroup Λ y
```

**`GaugeFieldData.repLorentzGroup_apply_one`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L199).

```lean
lemma repLorentzGroup_apply_one (Λ : SL(2,ℂ)) :
    T.repLorentzGroup Λ (1 : T.LocalFieldAlgebra) = 1
```

**`GaugeFieldData.repLorentzGroup_ιFermion`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L204).

```lean
lemma repLorentzGroup_ιFermion (Λ : SL(2,ℂ)) (i : T.FermionSpecies)
    (x : JetComponentSpace (T.fermion i)) :
    T.repLorentzGroup Λ (T.ιFermion i x)
      = T.ιFermion i (JetComponentSpace.repLorentzGroup (T.fermion i) Λ x)
```

**`GaugeFieldData.repLorentzGroup_ιBoson`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L211).

```lean
lemma repLorentzGroup_ιBoson (Λ : SL(2,ℂ)) (j : T.BosonSpecies)
    (y : JetComponentSpace (T.boson j)) :
    T.repLorentzGroup Λ (T.ιBoson j y)
      = T.ιBoson j (JetComponentSpace.repLorentzGroup (T.boson j) Λ y)
```

**`GaugeFieldData.repLorentzGroup_ιConnection`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L218).

```lean
lemma repLorentzGroup_ιConnection (Λ : SL(2,ℂ)) (v : GaugeBoson.JetComponentSpace 𝔤) :
    T.repLorentzGroup Λ (T.ιConnection v)
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ]
          LocalGaugeFieldAlgebra.repLorentzGroup 𝔤 Λ (SymmetricAlgebra.ι ℝ _ v))
```

**`GaugeFieldData.repLorentzGroup_includeConnection`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L226).

> The Lorentz action restricts to the complexified gauge-only action on the connection
> factor.

```lean
lemma repLorentzGroup_includeConnection (Λ : SL(2,ℂ)) (y : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤) :
    T.repLorentzGroup Λ (T.includeConnection y)
      = T.includeConnection (LocalGaugeFieldAlgebra.complexRepLorentzGroup 𝔤 Λ y)
```

**`GaugeFieldData.repLorentzGroup_ιConnection_eq`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean#L235).

> The Lorentz law of the connection generators: a transformation carries a connection
> generator to the generator of the transformed component, with no shift. This is the
> generator-level form of `GaugeFieldData.repLorentzGroup_ιConnection`, with no reference
> to the connection factor.

```lean
lemma repLorentzGroup_ιConnection_eq (Λ : SL(2,ℂ)) (v : GaugeBoson.JetComponentSpace 𝔤) :
    T.repLorentzGroup Λ (T.ιConnection v)
      = T.ιConnection (GaugeBoson.JetComponentSpace.repLorentzGroup 𝔤 Λ v)
```

## Depends on

- [The local field algebra of a gauge theory and its universal property](localfield-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/LorentzAction.lean)

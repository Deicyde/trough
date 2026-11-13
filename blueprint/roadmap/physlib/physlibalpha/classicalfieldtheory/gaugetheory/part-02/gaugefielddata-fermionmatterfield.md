---
declaration: module
origin: cited
lean: GaugeFieldData.fermionMatterField, GaugeFieldData.fermionMatterField_V, GaugeFieldData.fermionMatterField_massWeight, GaugeFieldData.fermionMatterField_statistic, GaugeFieldData.repLorentzFermionModule, GaugeFieldData.repLorentzFermionModule_apply, GaugeFieldData.repJetFermionModule, GaugeFieldData.repJetFermionModule_smul
statement: formalized
proof: formalized
---

# The fermionic matter field of a gauge theory

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeFieldData.FermionMatterField`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean): 19 declarations, 17 with a docstring.

## i. Overview

> `GaugeFieldData.FermionModule` is the value space of all the fermions of a theory at
> once. This file puts on it the structure of a single `MatterField`: the Lorentz
> representation, the action of the jets of gauge transformations, the infinitesimal action
> of the gauge algebra and the mass weight, all acting species by species. It is the direct
> sum `MatterField.pi` of the family `T.fermion`, and it is the object a physicist means by
> "the fermion field" of a theory, as against the fifteen separate multiplets the Standard
> Model is usually presented by.
>
> Beyond the datum, the assembly needs a shared mass weight. The construction packages the
> family into one `MatterField`, which has one weight, so the family must be degenerate in mass
> dimension, and the assembled field carries the common mass weight of its entries. That weight
> `w` is taken as an argument together with the proof that every species has it. For the
> Standard Model, and for any theory whose fermions are Weyl spinors, this is no restriction:
> every fermionic species has weight three. The common statistics comes from the datum itself,
> whose field `fermion_statistic` requires every fermionic species to be declared fermionic.
>
> Assembling the species loses nothing, and this is the content of the lemmas below: each
> species includes into the fermionic matter field as a subrepresentation, of the Lorentz
> group and of the gauge algebra alike, so the several multiplets can be read off the single
> field again. What it does lose is the ability to record *different* mass weights, which is
> exactly why `GaugeFieldData.FermionGenerators` is a direct sum of component spaces rather
> than the component space of this one field.

## ii. Key results

> - `GaugeFieldData.fermionMatterField` : the matter field of all the fermions of the
>   theory.
> - `GaugeFieldData.repJetFermionModule` : the action of the jets of gauge transformations
>   on the jets of the fermionic module, needing no common mass weight.
> - `GaugeFieldData.fermionMatterField_repLorentz_inclFermionValue`,
>   `GaugeFieldData.fermionMatterField_repAlgebra_inclFermionValue` : each species is a
>   subrepresentation of it.
> - `GaugeFieldData.finrank_fermionMatterField` : its dimension is the sum of the
>   dimensions of the species.

## iv. References

> * None.

## A. The fermionic matter field

**`GaugeFieldData.fermionMatterField`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L84).

> **The fermionic matter field of a gauge theory**: the direct sum of the fermionic
> species, valued in `T.FermionModule`, with the Lorentz group, the jets of gauge
> transformations and the gauge algebra all acting species by species. It exists only for
> a family degenerate in mass dimension: `w` is the common mass weight of the species and
> `h` the proof that they all have it, which for the Standard Model, and for any theory
> whose fermions are Weyl spinors, is weight three.

```lean
noncomputable def fermionMatterField (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w) :
    MatterField jets
```

**`GaugeFieldData.fermionMatterField_V`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L90).

```lean
lemma fermionMatterField_V (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w) :
    (T.fermionMatterField w h).V = T.FermionModule
```

**`GaugeFieldData.fermionMatterField_massWeight`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L95).

> The fermionic matter field carries the common mass weight of the species.

```lean
lemma fermionMatterField_massWeight (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w) :
    (T.fermionMatterField w h).massWeight = w
```

**`GaugeFieldData.fermionMatterField_statistic`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L100).

> The fermionic matter field is fermionic, as every fermionic species is declared to be.

```lean
lemma fermionMatterField_statistic (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w) :
    (T.fermionMatterField w h).statistic = .fermionic
```

### A.1. The transformation data species by species

**`GaugeFieldData.repLorentzFermionModule`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L114).

> **The Lorentz action on the fermionic module**, acting species by species. This is the
> Lorentz representation of the fermionic matter field, typed on `T.FermionModule` itself so
> that it can be spoken of without fixing a common mass weight.

```lean
noncomputable def repLorentzFermionModule : Representation ℂ SL(2,ℂ) T.FermionModule
```

**`GaugeFieldData.repLorentzFermionModule_apply`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L120).

```lean
lemma repLorentzFermionModule_apply (Λ : SL(2,ℂ)) (v : T.FermionModule) (i : T.FermionSpecies) :
    T.repLorentzFermionModule Λ v i = (T.fermion i).repLorentz Λ (v i)
```

**`GaugeFieldData.repJetFermionModule`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L130).

> The action of the jets of gauge transformations on the jets of the fermionic
> module, acting species by species. Like `repLorentzFermionModule` it is typed on
> `T.FermionModule` itself, so that it can be spoken of without fixing a common mass
> weight; the gauge action of a theory whose fermions carry different mass dimensions is
> perfectly well defined, only its packaging as one `MatterField` is not.

```lean
noncomputable def repJetFermionModule :
    Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] T.FermionModule)
```

**`GaugeFieldData.repJetFermionModule_smul`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L137).

> The jet gauge action on the fermionic module is fibrewise, as each species is.

```lean
lemma repJetFermionModule_smul (U : GJ) (χ : SpaceTimeAlgebra)
    (z : SpaceTimeAlgebra ⊗[ℂ] T.FermionModule) :
    T.repJetFermionModule U (χ • z) = χ • T.repJetFermionModule U z
```

**`GaugeFieldData.lTensor_projFermionValue_repJetFermionModule`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L144).

> A fermionic species is a subrepresentation of the jet gauge action on the fermionic
> module: the projection onto its value space intertwines the two actions on the jets.

```lean
lemma lTensor_projFermionValue_repJetFermionModule (i : T.FermionSpecies) (U : GJ) :
    (LinearMap.lTensor SpaceTimeAlgebra (T.projFermionValue i)).comp (T.repJetFermionModule U)
      = ((T.fermion i).repJet U).comp
        (LinearMap.lTensor SpaceTimeAlgebra (T.projFermionValue i))
```

**`GaugeFieldData.fermionMatterField_repJet`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L151).

> The jet gauge action of the fermionic matter field is that of the fermionic module.

```lean
lemma fermionMatterField_repJet (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w) :
    (T.fermionMatterField w h).repJet = T.repJetFermionModule
```

**`GaugeFieldData.fermionMatterField_repLorentz`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L155).

> The Lorentz action of the fermionic matter field is that of the fermionic module.

```lean
lemma fermionMatterField_repLorentz (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w) :
    (T.fermionMatterField w h).repLorentz = T.repLorentzFermionModule
```

**`GaugeFieldData.fermionMatterField_repLorentz_apply`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L160).

> The Lorentz group acts on a fermionic configuration species by species.

```lean
lemma fermionMatterField_repLorentz_apply (w : ℕ)
    (h : ∀ i, (T.fermion i).massWeight = w) (Λ : SL(2,ℂ)) (v : T.FermionModule)
    (i : T.FermionSpecies) :
    (T.fermionMatterField w h).repLorentz Λ v i = (T.fermion i).repLorentz Λ (v i)
```

**`GaugeFieldData.fermionMatterField_repAlgebra_apply`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L167).

> The gauge algebra acts on a fermionic configuration species by species.

```lean
lemma fermionMatterField_repAlgebra_apply (w : ℕ)
    (h : ∀ i, (T.fermion i).massWeight = w) (c : 𝔤) (v : T.FermionModule)
    (i : T.FermionSpecies) :
    (T.fermionMatterField w h).repAlgebra c v i = (T.fermion i).repAlgebra c (v i)
```

**`GaugeFieldData.fermionMatterField_repJet_apply`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L175).

> The jets of gauge transformations act on the jets of the fermionic field species by
> species, through the identification `jetPiEquiv` of the jets of the fermionic module
> with the family of the jets of the species.

```lean
lemma fermionMatterField_repJet_apply (w : ℕ)
    (h : ∀ i, (T.fermion i).massWeight = w) (U : GJ)
    (z : SpaceTimeAlgebra ⊗[ℂ] T.FermionModule) :
    (T.fermionMatterField w h).repJet U z =
      (jetPiEquiv T.FermionValue).symm
        (fun i => (T.fermion i).repJet U (jetPiEquiv T.FermionValue z i))
```

**`GaugeFieldData.repCoeff_fermionMatterField`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L184).

> The base-point Taylor coefficients of the fermionic jet action are those of the
> species, index by index.

```lean
lemma repCoeff_fermionMatterField (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w) (U : GJ)
    (x : Multiset (Fin 1 ⊕ Fin 3)) :
    GaugeAlgebraRealization.repCoeff (T.fermionMatterField w h).repJet U x =
      LinearMap.piMap fun i =>
        GaugeAlgebraRealization.repCoeff (T.fermion i).repJet U x
```

### A.2. The species as subrepresentations

**`GaugeFieldData.fermionMatterField_repLorentz_inclFermionValue`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L201).

> **A fermionic species is a Lorentz subrepresentation of the fermionic matter field**:
> including a value of one species and then transforming is transforming and then
> including. Assembling the species into one field therefore loses no Lorentz
> information.

```lean
lemma fermionMatterField_repLorentz_inclFermionValue (w : ℕ)
    (h : ∀ i, (T.fermion i).massWeight = w) (Λ : SL(2,ℂ)) (i : T.FermionSpecies)
    (x : T.FermionValue i) :
    (T.fermionMatterField w h).repLorentz Λ (T.inclFermionValue i x)
      = T.inclFermionValue i ((T.fermion i).repLorentz Λ x)
```

**`GaugeFieldData.fermionMatterField_repAlgebra_inclFermionValue`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L212).

> **A fermionic species is a subrepresentation of the gauge algebra action** on the
> fermionic matter field, for the same reason: the gauge algebra does not mix the
> species.

```lean
lemma fermionMatterField_repAlgebra_inclFermionValue (w : ℕ)
    (h : ∀ i, (T.fermion i).massWeight = w) (c : 𝔤) (i : T.FermionSpecies)
    (x : T.FermionValue i) :
    (T.fermionMatterField w h).repAlgebra c (T.inclFermionValue i x)
      = T.inclFermionValue i ((T.fermion i).repAlgebra c x)
```

**`GaugeFieldData.finrank_fermionMatterField`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L222).

> The dimension of the fermionic matter field is the sum of the dimensions of the
> species.

```lean
lemma finrank_fermionMatterField (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w) :
    Module.finrank ℂ (T.fermionMatterField w h).V
      = ∑ i, Module.finrank ℂ (T.FermionValue i)
```

**`GaugeFieldData.projFermionField`**, an abbrev, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean#L231).

> The projection of the fermionic matter field onto one species, typed as a map out of
> `(T.fermionMatterField w h).V` rather than out of `T.FermionModule`. The two are the same
> type by definition, but naming the first keeps unification from having to unfold the
> direct sum every time the projection meets the matter field.

```lean
noncomputable abbrev projFermionField (w : ℕ) (h : ∀ i, (T.fermion i).massWeight = w)
    (i : T.FermionSpecies) : (T.fermionMatterField w h).V →ₗ[ℂ] (T.fermion i).V
```

## Depends on

- [The fermionic module of a gauge theory](gaugefielddata-fermionmodule.md)
- [The direct sum of a finite family of matter fields](../part-05/matterfield-pi.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/FermionMatterField.lean)

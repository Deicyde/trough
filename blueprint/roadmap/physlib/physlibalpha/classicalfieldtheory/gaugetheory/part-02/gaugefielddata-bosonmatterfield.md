---
declaration: module
origin: cited
lean: GaugeFieldData.bosonMatterField, GaugeFieldData.bosonMatterField_V, GaugeFieldData.bosonMatterField_massWeight, GaugeFieldData.bosonMatterField_statistic, GaugeFieldData.repLorentzBosonModule, GaugeFieldData.repLorentzBosonModule_apply, GaugeFieldData.repJetBosonModule, GaugeFieldData.repJetBosonModule_smul
statement: formalized
proof: formalized
---

# The bosonic matter field of a gauge theory

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeFieldData.BosonMatterField`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean): 19 declarations, 17 with a docstring.

## i. Overview

> `GaugeFieldData.BosonModule` is the value space of all the bosons of a theory at
> once. This file puts on it the structure of a single `MatterField`: the Lorentz
> representation, the action of the jets of gauge transformations, the infinitesimal action
> of the gauge algebra and the mass weight, all acting species by species. It is the direct
> sum `MatterField.pi` of the family `T.boson`, and it is the object a physicist means by
> "the scalar field" of a theory: for the Standard Model the Higgs doublet, for a
> two-Higgs-doublet model the pair of doublets read as one field.
>
> The bosons here are the matter bosons — the scalars. The gauge bosons are not a species of
> `GaugeFieldData` at all, their generator space being fixed by the gauge algebra alone, so
> they are not part of this assembly.
>
> Beyond the datum, the assembly needs a shared mass weight. The construction packages the
> family into one `MatterField`, which has one weight, so the family must be degenerate in mass
> dimension, and the assembled field carries the common mass weight of its entries. That weight
> `w` is taken as an argument together with the proof that every species has it. For a theory
> whose scalars are all of the same mass dimension, the Standard Model included, this is no
> restriction: every bosonic species has weight two. The common statistics comes from the datum
> itself, whose field `boson_statistic` requires every bosonic species to be declared bosonic.
>
> Assembling the species loses nothing, and this is the content of the lemmas below: each
> species includes into the bosonic matter field as a subrepresentation, of the Lorentz
> group and of the gauge algebra alike, so the several multiplets can be read off the single
> field again. What it does lose is the ability to record *different* mass weights, which is
> exactly why `GaugeFieldData.BosonGenerators` is a direct sum of component spaces rather
> than the component space of this one field.

## ii. Key results

> - `GaugeFieldData.bosonMatterField` : the matter field of all the bosons of the
>   theory.
> - `GaugeFieldData.repJetBosonModule` : the action of the jets of gauge transformations on
>   the jets of the bosonic module, needing no common mass weight.
> - `GaugeFieldData.bosonMatterField_repLorentz_inclBosonValue`,
>   `GaugeFieldData.bosonMatterField_repAlgebra_inclBosonValue` : each species is a
>   subrepresentation of it.
> - `GaugeFieldData.finrank_bosonMatterField` : its dimension is the sum of the
>   dimensions of the species.

## iv. References

> * None.

## A. The bosonic matter field

**`GaugeFieldData.bosonMatterField`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L88).

> **The bosonic matter field of a gauge theory**: the direct sum of the bosonic
> species, valued in `T.BosonModule`, with the Lorentz group, the jets of gauge
> transformations and the gauge algebra all acting species by species. It exists only for
> a family degenerate in mass dimension: `w` is the common mass weight of the species and
> `h` the proof that they all have it, which for the Standard Model, whose only scalar is
> the Higgs doublet, is weight two.

```lean
noncomputable def bosonMatterField (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w) :
    MatterField jets
```

**`GaugeFieldData.bosonMatterField_V`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L94).

```lean
lemma bosonMatterField_V (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w) :
    (T.bosonMatterField w h).V = T.BosonModule
```

**`GaugeFieldData.bosonMatterField_massWeight`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L99).

> The bosonic matter field carries the common mass weight of the species.

```lean
lemma bosonMatterField_massWeight (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w) :
    (T.bosonMatterField w h).massWeight = w
```

**`GaugeFieldData.bosonMatterField_statistic`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L104).

> The bosonic matter field is bosonic, as every bosonic species is declared to be.

```lean
lemma bosonMatterField_statistic (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w) :
    (T.bosonMatterField w h).statistic = .bosonic
```

### A.1. The transformation data species by species

**`GaugeFieldData.repLorentzBosonModule`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L118).

> **The Lorentz action on the bosonic module**, acting species by species. This is the
> Lorentz representation of the bosonic matter field, typed on `T.BosonModule` itself so
> that it can be spoken of without fixing a common mass weight.

```lean
noncomputable def repLorentzBosonModule : Representation ℂ SL(2,ℂ) T.BosonModule
```

**`GaugeFieldData.repLorentzBosonModule_apply`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L124).

```lean
lemma repLorentzBosonModule_apply (Λ : SL(2,ℂ)) (v : T.BosonModule) (i : T.BosonSpecies) :
    T.repLorentzBosonModule Λ v i = (T.boson i).repLorentz Λ (v i)
```

**`GaugeFieldData.repJetBosonModule`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L132).

> The action of the jets of gauge transformations on the jets of the bosonic
> module, acting species by species, and typed on `T.BosonModule` itself so that it can
> be spoken of without fixing a common mass weight.

```lean
noncomputable def repJetBosonModule :
    Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] T.BosonModule)
```

**`GaugeFieldData.repJetBosonModule_smul`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L139).

> The jet gauge action on the bosonic module is fibrewise, as each species is.

```lean
lemma repJetBosonModule_smul (U : GJ) (χ : SpaceTimeAlgebra)
    (z : SpaceTimeAlgebra ⊗[ℂ] T.BosonModule) :
    T.repJetBosonModule U (χ • z) = χ • T.repJetBosonModule U z
```

**`GaugeFieldData.lTensor_projBosonValue_repJetBosonModule`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L146).

> A bosonic species is a subrepresentation of the jet gauge action on the bosonic
> module: the projection onto its value space intertwines the two actions on the jets.

```lean
lemma lTensor_projBosonValue_repJetBosonModule (j : T.BosonSpecies) (U : GJ) :
    (LinearMap.lTensor SpaceTimeAlgebra (T.projBosonValue j)).comp (T.repJetBosonModule U)
      = ((T.boson j).repJet U).comp
        (LinearMap.lTensor SpaceTimeAlgebra (T.projBosonValue j))
```

**`GaugeFieldData.bosonMatterField_repJet`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L153).

> The jet gauge action of the bosonic matter field is that of the bosonic module.

```lean
lemma bosonMatterField_repJet (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w) :
    (T.bosonMatterField w h).repJet = T.repJetBosonModule
```

**`GaugeFieldData.bosonMatterField_repLorentz`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L157).

> The Lorentz action of the bosonic matter field is that of the bosonic module.

```lean
lemma bosonMatterField_repLorentz (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w) :
    (T.bosonMatterField w h).repLorentz = T.repLorentzBosonModule
```

**`GaugeFieldData.bosonMatterField_repLorentz_apply`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L162).

> The Lorentz group acts on a bosonic configuration species by species.

```lean
lemma bosonMatterField_repLorentz_apply (w : ℕ)
    (h : ∀ i, (T.boson i).massWeight = w) (Λ : SL(2,ℂ)) (v : T.BosonModule)
    (i : T.BosonSpecies) :
    (T.bosonMatterField w h).repLorentz Λ v i = (T.boson i).repLorentz Λ (v i)
```

**`GaugeFieldData.bosonMatterField_repAlgebra_apply`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L169).

> The gauge algebra acts on a bosonic configuration species by species.

```lean
lemma bosonMatterField_repAlgebra_apply (w : ℕ)
    (h : ∀ i, (T.boson i).massWeight = w) (c : 𝔤) (v : T.BosonModule)
    (i : T.BosonSpecies) :
    (T.bosonMatterField w h).repAlgebra c v i = (T.boson i).repAlgebra c (v i)
```

**`GaugeFieldData.bosonMatterField_repJet_apply`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L177).

> The jets of gauge transformations act on the jets of the bosonic field species by
> species, through the identification `jetPiEquiv` of the jets of the bosonic module
> with the family of the jets of the species.

```lean
lemma bosonMatterField_repJet_apply (w : ℕ)
    (h : ∀ i, (T.boson i).massWeight = w) (U : GJ)
    (z : SpaceTimeAlgebra ⊗[ℂ] T.BosonModule) :
    (T.bosonMatterField w h).repJet U z =
      (jetPiEquiv T.BosonValue).symm
        (fun i => (T.boson i).repJet U (jetPiEquiv T.BosonValue z i))
```

**`GaugeFieldData.repCoeff_bosonMatterField`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L186).

> The base-point Taylor coefficients of the bosonic jet action are those of the
> species, index by index.

```lean
lemma repCoeff_bosonMatterField (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w) (U : GJ)
    (x : Multiset (Fin 1 ⊕ Fin 3)) :
    GaugeAlgebraRealization.repCoeff (T.bosonMatterField w h).repJet U x =
      LinearMap.piMap fun i =>
        GaugeAlgebraRealization.repCoeff (T.boson i).repJet U x
```

### A.2. The species as subrepresentations

**`GaugeFieldData.bosonMatterField_repLorentz_inclBosonValue`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L203).

> **A bosonic species is a Lorentz subrepresentation of the bosonic matter field**:
> including a value of one species and then transforming is transforming and then
> including. Assembling the species into one field therefore loses no Lorentz
> information.

```lean
lemma bosonMatterField_repLorentz_inclBosonValue (w : ℕ)
    (h : ∀ i, (T.boson i).massWeight = w) (Λ : SL(2,ℂ)) (i : T.BosonSpecies)
    (x : T.BosonValue i) :
    (T.bosonMatterField w h).repLorentz Λ (T.inclBosonValue i x)
      = T.inclBosonValue i ((T.boson i).repLorentz Λ x)
```

**`GaugeFieldData.bosonMatterField_repAlgebra_inclBosonValue`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L214).

> **A bosonic species is a subrepresentation of the gauge algebra action** on the
> bosonic matter field, for the same reason: the gauge algebra does not mix the
> species.

```lean
lemma bosonMatterField_repAlgebra_inclBosonValue (w : ℕ)
    (h : ∀ i, (T.boson i).massWeight = w) (c : 𝔤) (i : T.BosonSpecies)
    (x : T.BosonValue i) :
    (T.bosonMatterField w h).repAlgebra c (T.inclBosonValue i x)
      = T.inclBosonValue i ((T.boson i).repAlgebra c x)
```

**`GaugeFieldData.finrank_bosonMatterField`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L224).

> The dimension of the bosonic matter field is the sum of the dimensions of the
> species.

```lean
lemma finrank_bosonMatterField (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w) :
    Module.finrank ℂ (T.bosonMatterField w h).V
      = ∑ i, Module.finrank ℂ (T.BosonValue i)
```

**`GaugeFieldData.projBosonField`**, an abbrev, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean#L233).

> The projection of the bosonic matter field onto one species, typed as a map out of
> `(T.bosonMatterField w h).V` rather than out of `T.BosonModule`. The two are the same
> type by definition, but naming the first keeps unification from having to unfold the
> direct sum every time the projection meets the matter field.

```lean
noncomputable abbrev projBosonField (w : ℕ) (h : ∀ i, (T.boson i).massWeight = w)
    (i : T.BosonSpecies) : (T.bosonMatterField w h).V →ₗ[ℂ] (T.boson i).V
```

## Depends on

- [The bosonic module of a gauge theory](gaugefielddata-bosonmodule.md)
- [The direct sum of a finite family of matter fields](../part-05/matterfield-pi.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GaugeFieldData/BosonMatterField.lean)

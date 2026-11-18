---
declaration: module
origin: cited
lean: StandardModel.fermionProj_comp_repLorentzGroup, StandardModel.fermionSpaceEquiv_comp_repLorentzGroup, StandardModel.higgsModuleEquiv_comp_repLorentzGroup, StandardModel.lTensor_fermionProj_repJetGaugeGroupI, StandardModel.lTensor_fermionSpaceEquiv_repJetGaugeGroupI, StandardModel.lTensor_higgsModuleEquiv_repJetGaugeGroupI, StandardModel.fermionGeneratorsEquiv_repLorentzFermion, StandardModel.fermionGeneratorsEquiv_comp_repLorentzFermion
statement: formalized
proof: formalized
---

# The generator identifications respect the transformation data

The module `PhyslibAlpha.Particles.StandardModel.JetAlgebra.SectorEquiv.Structure`, [PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean): 24 declarations, 24 with a docstring.

## i. Overview

> `PhyslibAlpha.Particles.StandardModel.JetAlgebra.SectorEquiv.Basic` identifies the two matter
> generator spaces of `StandardModel.fieldData` with the two the Standard Model sector
> algebras are built on. This file proves that those identifications respect the
> transformation data: the Lorentz action, the jet gauge action and the mass weights.
>
> The generic half of each statement is already proved once and for all in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GaugeFieldData.FermionGenerators`:
> `GaugeFieldData.fermionGeneratorsEquiv` intertwines the species-diagonal Lorentz and jet
> gauge actions on the direct sum with the actions on the component functions of a single
> field valued in `T.FermionModule`, and likewise for the mass-weight scaling under a common
> weight. What is added here is the Standard Model half: the relabelling `fermionSpaceEquiv`
> of the target space is itself equivariant for both actions, which is the two families of
> five species lemmas of
> `PhyslibAlpha.Particles.StandardModel.Fermions.JetAlgebra.Species` read at the fifteen species
> of the datum. Naturality of `JetComponentSpace.comap` in the value space then carries the
> generic statements across the relabelling; for the mass-weight scaling no equivariance is
> needed at all, the scaling being blind to the value space.
>
> Gauge equivariance is the one statement of the three that is not formal. The gauge action
> on a component function is the all-orders Leibniz convolution of the Taylor coefficients of
> the gauge jet, so it sees the derivative label as well as the target index, and its
> conjugate half carries `star` of the gauge matrix rather than the matrix. Neither half
> follows from the other, and neither follows from linearity: both are proved, for every
> derivative label, from `JetComponentSpace.comap_comp_repJet`. No common mass weight enters
> any of it — the fifteen fermionic species do share weight three, but the gauge statement
> does not use that, and is stated over `GaugeFieldData.repJetFermionModule`, which is
> defined whatever the weights are.
>
> Section C lifts the four resulting generator statements to the sector algebras, which are
> the two matter factors of the carrier. The ordinary derivative is treated in section D of
> `PhyslibAlpha.Particles.StandardModel.JetAlgebra.SectorEquiv.Basic`. The connection sector needs
> no identification at all: the Standard Model gauge bosons are the generic ones at
> `GaugeAlgebra`.

## ii. Key results

> - `StandardModel.fermionSpaceEquiv_comp_repLorentzGroup`,
>   `StandardModel.lTensor_fermionSpaceEquiv_repJetGaugeGroupI` : the relabelling of the
>   fermionic target space is equivariant for the Lorentz and the jet gauge action.
> - `StandardModel.fermionGeneratorsEquiv_repLorentzFermion`,
>   `StandardModel.bosonGeneratorsEquiv_repLorentzBoson` : the generator identifications
>   intertwine the Lorentz actions.
> - `StandardModel.fermionGeneratorsEquiv_repJetFermion`,
>   `StandardModel.bosonGeneratorsEquiv_repJetBoson` : and the jet gauge actions.
> - `StandardModel.fermionGeneratorsEquiv_massWeightScaleFermion`,
>   `StandardModel.bosonGeneratorsEquiv_massWeightScaleBoson` : and the mass-weight
>   scalings.
> - `StandardModel.fermionAlgebraEquiv_repJetGaugeGroupI`,
>   `StandardModel.higgsAlgebraEquiv_repJetGaugeGroupI`,
>   `StandardModel.fermionAlgebraEquiv_repLorentzGroup`,
>   `StandardModel.higgsAlgebraEquiv_repLorentzGroup` : the sector algebra equivalences
>   intertwine both actions.

## iv. References

> * None.

## A. The relabellings intertwine the Standard Model structure

> Both actions on the total fermionic target space are species-diagonal, which is already
> recorded species by species in
> `PhyslibAlpha.Particles.StandardModel.Fermions.JetAlgebra.Species`. Reading those two families
> of five lemmas at the fifteen species of the datum is the only Standard Model input the
> comparison of the transformation data needs.

### A.1. The Lorentz action

**`StandardModel.fermionProj_comp_repLorentzGroup`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L112).

> The projection onto a species intertwines the total Lorentz action on the fermionic
> target space with that species' own.

```lean
lemma fermionProj_comp_repLorentzGroup (t : fieldData.FermionSpecies) (Λ : SL(2,ℂ)) :
    (fermionProj t).comp (FermionSpace.repLorentzGroup Λ)
      = ((fieldData.fermion t).repLorentz Λ).comp (fermionProj t)
```

**`StandardModel.fermionSpaceEquiv_comp_repLorentzGroup`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L124).

> The relabelling of the fermionic target space is Lorentz-equivariant. Both actions
> are species-diagonal, so this is the previous lemma read one species at a time.

```lean
lemma fermionSpaceEquiv_comp_repLorentzGroup (Λ : SL(2,ℂ)) :
    fermionSpaceEquiv.toLinearMap.comp (FermionSpace.repLorentzGroup Λ)
      = (fieldData.repLorentzFermionModule Λ).comp fermionSpaceEquiv.toLinearMap
```

**`StandardModel.higgsModuleEquiv_comp_repLorentzGroup`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L133).

> The relabelling of the Higgs is Lorentz-equivariant. The Higgs is a Lorentz scalar,
> so both sides are the identity; the content is that the one bosonic species of the datum
> carries exactly the trivial Higgs representation.

```lean
lemma higgsModuleEquiv_comp_repLorentzGroup (Λ : SL(2,ℂ)) :
    higgsModuleEquiv.toLinearMap.comp (Representation.trivial ℂ SL(2,ℂ) HiggsVec Λ)
      = (fieldData.repLorentzBosonModule Λ).comp higgsModuleEquiv.toLinearMap
```

### A.2. The jet gauge action

> The jet gauge action on the total fermionic target space is species-diagonal through
> `FermionSpace.jetActionMap`, so each projection intertwines it with that species' own.
> The relabelling is the assembly of the fifteen projections, and a jet of the fermionic
> module is determined by its species components, so the relabelling too is equivariant.

**`StandardModel.lTensor_fermionProj_repJetGaugeGroupI`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L151).

> The projection onto a species intertwines the total jet gauge action on the jets of
> the fermionic target space with that species' own.

```lean
lemma lTensor_fermionProj_repJetGaugeGroupI (t : fieldData.FermionSpecies)
    (U : JetGaugeGroupI) :
    (LinearMap.lTensor SpaceTimeAlgebra (fermionProj t)).comp (fermionMatterField.repJet U)
      = ((fieldData.fermion t).repJet U).comp
        (LinearMap.lTensor SpaceTimeAlgebra (fermionProj t))
```

**`StandardModel.lTensor_fermionSpaceEquiv_repJetGaugeGroupI`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L167).

> The relabelling of the fermionic target space is equivariant for the jet gauge
> action. Both actions are species-diagonal, so this is the previous lemma read one
> species at a time, the two being compared through the splitting of the jets of a
> product.

```lean
lemma lTensor_fermionSpaceEquiv_repJetGaugeGroupI (U : JetGaugeGroupI) :
    (LinearMap.lTensor SpaceTimeAlgebra fermionSpaceEquiv.toLinearMap).comp
        (fermionMatterField.repJet U)
      = ((fieldData.fermionMatterField 3 fieldData_fermion_massWeight).repJet U).comp
        (LinearMap.lTensor SpaceTimeAlgebra fermionSpaceEquiv.toLinearMap)
```

**`StandardModel.lTensor_higgsModuleEquiv_repJetGaugeGroupI`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L202).

> The relabelling of the Higgs is equivariant for the jet gauge action. There is one
> bosonic species, and reading it off undoes the relabelling, so both sides are the Higgs
> action itself; the content is that the single bosonic species of the datum carries
> exactly the Higgs representation.

```lean
lemma lTensor_higgsModuleEquiv_repJetGaugeGroupI (U : JetGaugeGroupI) :
    (LinearMap.lTensor SpaceTimeAlgebra higgsModuleEquiv.toLinearMap).comp
        (HiggsVec.matterField.repJet U)
      = ((fieldData.bosonMatterField 2 fieldData_boson_massWeight).repJet U).comp
        (LinearMap.lTensor SpaceTimeAlgebra higgsModuleEquiv.toLinearMap)
```

## B. The generator identifications intertwine the transformation data

> Nothing in this section is a consequence of transport: the two sides are the generic
> species-diagonal structure on the direct sum and the existing Standard Model structure on
> the component space of the total target space, and the comparison of the two is what has
> content.

### B.1. The Lorentz action

**`StandardModel.fermionGeneratorsEquiv_repLorentzFermion`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L250).

> The fermionic generator identification intertwines the Lorentz actions: the
> species-diagonal action of the datum with the Standard Model action on the component
> space of the total fermionic target space.

```lean
lemma fermionGeneratorsEquiv_repLorentzFermion (Λ : SL(2,ℂ))
    (v : fieldData.FermionGenerators) :
    fermionGeneratorsEquiv (fieldData.repLorentzFermion Λ v)
      = JetComponentSpace.repLorentzGroup fermionMatterField Λ
        (fermionGeneratorsEquiv v)
```

**`StandardModel.fermionGeneratorsEquiv_comp_repLorentzFermion`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L263).

> The composed form of `fermionGeneratorsEquiv_repLorentzFermion`.

```lean
lemma fermionGeneratorsEquiv_comp_repLorentzFermion (Λ : SL(2,ℂ)) :
    fermionGeneratorsEquiv.toLinearMap.comp (fieldData.repLorentzFermion Λ)
      = (JetComponentSpace.repLorentzGroup fermionMatterField Λ).comp
        fermionGeneratorsEquiv.toLinearMap
```

**`StandardModel.bosonGeneratorsEquiv_repLorentzBoson`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L273).

> The bosonic generator identification intertwines the Lorentz actions. The Higgs is
> a Lorentz scalar, so both sides act only on the derivative labels; the content is that
> the single bosonic species of the datum carries exactly the trivial Higgs representation
> of the Standard Model.

```lean
lemma bosonGeneratorsEquiv_repLorentzBoson (Λ : SL(2,ℂ))
    (w : fieldData.BosonGenerators) :
    bosonGeneratorsEquiv (fieldData.repLorentzBoson Λ w)
      = JetComponentSpace.repLorentzGroup HiggsVec.matterField Λ
        (bosonGeneratorsEquiv w)
```

**`StandardModel.bosonGeneratorsEquiv_comp_repLorentzBoson`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L286).

> The composed form of `bosonGeneratorsEquiv_repLorentzBoson`.

```lean
lemma bosonGeneratorsEquiv_comp_repLorentzBoson (Λ : SL(2,ℂ)) :
    bosonGeneratorsEquiv.toLinearMap.comp (fieldData.repLorentzBoson Λ)
      = (JetComponentSpace.repLorentzGroup HiggsVec.matterField
          Λ).comp bosonGeneratorsEquiv.toLinearMap
```

**`StandardModel.fermionGeneratorsEquiv_symm_repLorentzGroup`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L293).

> The inverse form of `fermionGeneratorsEquiv_repLorentzFermion`.

```lean
lemma fermionGeneratorsEquiv_symm_repLorentzGroup (Λ : SL(2,ℂ))
    (w : JetComponentSpace fermionMatterField) :
    fermionGeneratorsEquiv.symm
        (JetComponentSpace.repLorentzGroup fermionMatterField Λ w)
      = fieldData.repLorentzFermion Λ (fermionGeneratorsEquiv.symm w)
```

**`StandardModel.bosonGeneratorsEquiv_symm_repLorentzGroup`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L305).

> The inverse form of `bosonGeneratorsEquiv_repLorentzBoson`.

```lean
lemma bosonGeneratorsEquiv_symm_repLorentzGroup (Λ : SL(2,ℂ))
    (w : JetComponentSpace HiggsVec.matterField) :
    bosonGeneratorsEquiv.symm (JetComponentSpace.repLorentzGroup HiggsVec.matterField Λ w)
      = fieldData.repLorentzBoson Λ (bosonGeneratorsEquiv.symm w)
```

### B.2. The jet gauge action

> Neither half of this is formal. The gauge action mixes a component function with the lower
> ones through the Taylor coefficients of the gauge jet, so it sees the derivative label; and
> its conjugate half carries `star` of the gauge matrix. Both are covered, at every
> derivative label, by `JetComponentSpace.comap_comp_repJet`, whose two halves are proved
> separately. The inverse forms below are what the sector algebra equivalences of section C
> consume.

**`StandardModel.fermionGeneratorsEquiv_repJetFermion`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L331).

> The fermionic generator identification intertwines the jet gauge actions: the
> species-diagonal action of the datum with the Standard Model action on the component
> space of the total fermionic target space. No common mass weight is used.

```lean
lemma fermionGeneratorsEquiv_repJetFermion (U : JetGaugeGroupI)
    (v : fieldData.FermionGenerators) :
    fermionGeneratorsEquiv (fieldData.repJetFermion U v)
      = JetComponentSpace.repJet fermionMatterField U (fermionGeneratorsEquiv v)
```

**`StandardModel.fermionGeneratorsEquiv_symm_repJet`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L342).

> The inverse form of `fermionGeneratorsEquiv_repJetFermion`.

```lean
lemma fermionGeneratorsEquiv_symm_repJet (U : JetGaugeGroupI)
    (w : JetComponentSpace fermionMatterField) :
    fermionGeneratorsEquiv.symm (JetComponentSpace.repJet fermionMatterField U w)
      = fieldData.repJetFermion U (fermionGeneratorsEquiv.symm w)
```

**`StandardModel.bosonGeneratorsEquiv_repJetBoson`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L354).

> The bosonic generator identification intertwines the jet gauge actions, at the one
> Higgs species.

```lean
lemma bosonGeneratorsEquiv_repJetBoson (U : JetGaugeGroupI)
    (v : fieldData.BosonGenerators) :
    bosonGeneratorsEquiv (fieldData.repJetBoson U v)
      = JetComponentSpace.repJet HiggsVec.matterField U (bosonGeneratorsEquiv v)
```

**`StandardModel.bosonGeneratorsEquiv_symm_repJet`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L365).

> The inverse form of `bosonGeneratorsEquiv_repJetBoson`.

```lean
lemma bosonGeneratorsEquiv_symm_repJet (U : JetGaugeGroupI)
    (w : JetComponentSpace HiggsVec.matterField) :
    bosonGeneratorsEquiv.symm (JetComponentSpace.repJet HiggsVec.matterField U w)
      = fieldData.repJetBoson U (bosonGeneratorsEquiv.symm w)
```

### B.3. The mass weights

**`StandardModel.fermionGeneratorsEquiv_massWeightScaleFermion`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L387).

> The fermionic generator identification intertwines the mass-weight scalings: the
> per-species scaling of the datum, which carries the weight three of every Standard Model
> fermion, with the single weight-three scaling of the component space of the total target
> space. That the two agree is exactly the statement that all fifteen species have the same
> weight; the relabelling of the target space costs nothing, the scaling being natural in
> the value space.

```lean
lemma fermionGeneratorsEquiv_massWeightScaleFermion (c : ℂ)
    (v : fieldData.FermionGenerators) :
    fermionGeneratorsEquiv (fieldData.massWeightScaleFermion c v)
      = JetComponentSpace.massWeightScale 3 c (fermionGeneratorsEquiv v)
```

**`StandardModel.fermionGeneratorsEquiv_comp_massWeightScaleFermion`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L399).

> The composed form of `fermionGeneratorsEquiv_massWeightScaleFermion`.

```lean
lemma fermionGeneratorsEquiv_comp_massWeightScaleFermion (c : ℂ) :
    fermionGeneratorsEquiv.toLinearMap.comp (fieldData.massWeightScaleFermion c)
      = (JetComponentSpace.massWeightScale 3 c).comp
        fermionGeneratorsEquiv.toLinearMap
```

**`StandardModel.bosonGeneratorsEquiv_massWeightScaleBoson`**, a lemma, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L407).

> The bosonic generator identification intertwines the mass-weight scalings, at the
> Higgs weight two.

```lean
lemma bosonGeneratorsEquiv_massWeightScaleBoson (c : ℂ)
    (w : fieldData.BosonGenerators) :
    bosonGeneratorsEquiv (fieldData.massWeightScaleBoson c w)
      = JetComponentSpace.massWeightScale 2 c (bosonGeneratorsEquiv w)
```

**`StandardModel.bosonGeneratorsEquiv_comp_massWeightScaleBoson`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L419).

> The composed form of `bosonGeneratorsEquiv_massWeightScaleBoson`.

```lean
lemma bosonGeneratorsEquiv_comp_massWeightScaleBoson (c : ℂ) :
    bosonGeneratorsEquiv.toLinearMap.comp (fieldData.massWeightScaleBoson c)
      = (JetComponentSpace.massWeightScale 2 c).comp bosonGeneratorsEquiv.toLinearMap
```

## C. The sector algebra equivalences intertwine the two actions

> Each of the two sector algebra equivalences of
> `PhyslibAlpha.Particles.StandardModel.JetAlgebra.SectorEquiv.Basic` is the free-algebra functor
> applied to a generator identification, and each of the four actions is the free-algebra
> functor applied to an action on the generators. So each statement below is the
> corresponding generator statement pushed along an algebra map, by extensionality of algebra
> maps on the free algebra — not by induction, unlike the derivative, since a group element
> here acts by an algebra homomorphism.

**`StandardModel.fermionAlgebraEquiv_repJetGaugeGroupI`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L439).

> The fermionic sector equivalence intertwines the jet gauge actions.

```lean
lemma fermionAlgebraEquiv_repJetGaugeGroupI (U : JetGaugeGroupI) (f : FermionJetAlgebra) :
    fermionAlgebraEquiv (FermionJetAlgebra.repJetGaugeGroupI U f)
      = fieldData.repJetFermion.exteriorAlgebra U (fermionAlgebraEquiv f)
```

**`StandardModel.higgsAlgebraEquiv_repJetGaugeGroupI`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L447).

> The Higgs sector equivalence intertwines the jet gauge actions.

```lean
lemma higgsAlgebraEquiv_repJetGaugeGroupI (U : JetGaugeGroupI) (h : HiggsJetAlgebra) :
    higgsAlgebraEquiv (HiggsJetAlgebra.repJetGaugeGroupI U h)
      = fieldData.repJetBoson.symmetricAlgebra U (higgsAlgebraEquiv h)
```

**`StandardModel.fermionAlgebraEquiv_repLorentzGroup`**, a lemma, [line 455](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L455).

> The fermionic sector equivalence intertwines the Lorentz actions.

```lean
lemma fermionAlgebraEquiv_repLorentzGroup (Λ : SL(2,ℂ)) (f : FermionJetAlgebra) :
    fermionAlgebraEquiv (FermionJetAlgebra.repLorentzGroup Λ f)
      = fieldData.repLorentzFermion.exteriorAlgebra Λ (fermionAlgebraEquiv f)
```

**`StandardModel.higgsAlgebraEquiv_repLorentzGroup`**, a lemma, [line 463](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean#L463).

> The Higgs sector equivalence intertwines the Lorentz actions.

```lean
lemma higgsAlgebraEquiv_repLorentzGroup (Λ : SL(2,ℂ)) (h : HiggsJetAlgebra) :
    higgsAlgebraEquiv (HiggsJetAlgebra.repLorentzGroup Λ h)
      = fieldData.repLorentzBoson.symmetricAlgebra Λ (higgsAlgebraEquiv h)
```

## Depends on

- [The sector algebras of the Standard Model inside its local field algebra](jetalgebra-sectorequiv-basic.md)

## Proof depends on

- [Species compatibility inside the fermionic target space](../part-03/fermions-jetalgebra-species.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Structure.lean)

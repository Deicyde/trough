---
declaration: module
origin: cited
lean: StandardModel.fermionSpaceEquiv, StandardModel.fermionProj, StandardModel.fermionProj_eq, StandardModel.fermionProj_leptonDoublet, StandardModel.fermionProj_leptonSinglet, StandardModel.fermionProj_quarkDoublet, StandardModel.fermionProj_upSinglet, StandardModel.fermionProj_downSinglet
statement: formalized
proof: formalized
---

# The sector algebras of the Standard Model inside its local field algebra

The module `PhyslibAlpha.Particles.StandardModel.JetAlgebra.SectorEquiv.Basic`, [PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean): 36 declarations, 25 with a docstring; 1 private, not shown.

## i. Overview

> The Standard Model jet algebra is `fieldData.LocalFieldAlgebra`, the local field algebra
> the generic theory builds from the Standard Model field datum: one exterior algebra on the
> direct sum of the fifteen fermionic species component spaces, a symmetric algebra on the
> one bosonic species, and the complexified real symmetric algebra on the connection
> generators.
>
> Its two matter factors are not the sector algebras the Standard Model files are written
> with. `FermionJetAlgebra` is an exterior algebra on the component space of a fifteen-fold
> product of value spaces, and the fermionic factor of the carrier an exterior algebra on a
> fifteen-fold direct sum of component spaces; `HiggsJetAlgebra` is a symmetric algebra on
> the component space of `HiggsVec`, and the bosonic factor one on the generators of the
> one-species direct sum. This file identifies the two presentations and lifts the
> identification to the sector algebras, which is what the sector inclusions
> `JetAlgebra.includeFermion` and `JetAlgebra.includeHiggs` are built from. The connection
> factors need no comparison: the Standard Model gauge bosons are the generic
> `GaugeBoson GaugeAlgebra`.
>
> The identification of the generators is Joseph Tooby-Smith's generic
> `GaugeFieldData.fermionGeneratorsEquiv`, which presents the direct sum over the species as
> the component space of a single field valued in `fieldData.FermionModule`. What is left for
> the Standard Model is one relabelling: `FermionSpace` is a nested product of five
> three-generation blocks and `fieldData.FermionModule` is a dependent function on the fifteen
> constructors of `FermionType`. `StandardModel.fermionSpaceEquiv` is that relabelling, and
> `JetComponentSpace.comapEquiv` carries it to the component spaces — contravariantly, a
> component function being a covector on the target.

## ii. Key results

> - `StandardModel.fermionSpaceEquiv` : the total fermionic target space as the family of
>   species value spaces.
> - `StandardModel.fermionProj` : the projection onto a species, computing to the existing
>   Standard Model projections.
> - `StandardModel.higgsModuleEquiv` : the Higgs as the one-species bosonic module.
> - `StandardModel.fermionGeneratorsEquiv`, `StandardModel.bosonGeneratorsEquiv` : the two
>   matter generator identifications.
> - `StandardModel.fermionAlgebraEquiv`, `StandardModel.higgsAlgebraEquiv` : the two sector
>   algebra equivalences.
> - `StandardModel.fermionAlgebraEquiv_jetDeriv`,
>   `StandardModel.higgsAlgebraEquiv_jetDeriv` : the sector equivalences are maps of
>   differential algebras.

## iv. References

> * None.

## A. The two matter generator identifications

### A.1. The fermionic species as a family over the total target space

> The generic theory presents the fermionic generators as the component space of a field
> valued in `fieldData.FermionModule`, a dependent function on the fifteen species. The
> Standard Model writes the same target space as a nested product of five three-generation
> blocks. The only Standard Model input the comparison needs is the relabelling between the
> two.

**`StandardModel.fermionSpaceEquiv`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L102).

> The total fermionic target space is the fermionic module of the datum. The nested
> product of five three-generation blocks that `FermionSpace` is, rearranged into a
> dependent function on the fifteen species. It is a relabelling: every component of a
> value on one side is a component of the corresponding value on the other.

```lean
noncomputable def fermionSpaceEquiv :
    fermionMatterField.V ≃ₗ[ℂ] (fieldData.fermionMatterField 3 fieldData_fermion_massWeight).V
```

**`StandardModel.fermionProj`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L139).

> The projection of the total fermionic target space onto the value space of a species
> of the datum: the relabelling followed by the projection of the module.

```lean
noncomputable def fermionProj (t : fieldData.FermionSpecies) :
    fermionMatterField.V →ₗ[ℂ] (fieldData.fermion t).V
```

**`StandardModel.fermionProj_eq`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L144).

```lean
lemma fermionProj_eq (t : fieldData.FermionSpecies) :
    fermionProj t = (fieldData.projFermionField 3 fieldData_fermion_massWeight t).comp
      fermionSpaceEquiv.toLinearMap
```

**`StandardModel.fermionProj_leptonDoublet`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L149).

```lean
lemma fermionProj_leptonDoublet (i : Fin 3) :
    fermionProj (.leptonDoublet i) = FermionSpace.leptonDoubletProj i
```

**`StandardModel.fermionProj_leptonSinglet`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L153).

```lean
lemma fermionProj_leptonSinglet (i : Fin 3) :
    fermionProj (.leptonSinglet i) = FermionSpace.leptonSingletProj i
```

**`StandardModel.fermionProj_quarkDoublet`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L157).

```lean
lemma fermionProj_quarkDoublet (i : Fin 3) :
    fermionProj (.quarkDoublet i) = FermionSpace.quarkDoubletProj i
```

**`StandardModel.fermionProj_upSinglet`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L161).

```lean
lemma fermionProj_upSinglet (i : Fin 3) :
    fermionProj (.upSinglet i) = FermionSpace.upSingletProj i
```

**`StandardModel.fermionProj_downSinglet`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L165).

```lean
lemma fermionProj_downSinglet (i : Fin 3) :
    fermionProj (.downSinglet i) = FermionSpace.downSingletProj i
```

### A.2. The Higgs as the one bosonic species

**`StandardModel.higgsModuleEquiv`**, a def, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L176).

> The Higgs multiplet is the bosonic module of the datum. There is one bosonic
> species, so the module of bosonic values is the constant family on it.

```lean
noncomputable def higgsModuleEquiv :
    HiggsVec.matterField.V ≃ₗ[ℂ] (fieldData.bosonMatterField 2 fieldData_boson_massWeight).V
```

**`StandardModel.projBosonValue_comp_higgsModuleEquiv`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L186).

> Reading off the one species undoes the relabelling.

```lean
lemma projBosonValue_comp_higgsModuleEquiv (j : fieldData.BosonSpecies) :
    (fieldData.projBosonField 2 fieldData_boson_massWeight j).comp
        higgsModuleEquiv.toLinearMap = LinearMap.id
```

**`StandardModel.comap_projBosonValue_comp_comap_higgsModuleEquiv`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L192).

> The pullback along the relabelling undoes the pullback along the one projection.

```lean
lemma comap_projBosonValue_comp_comap_higgsModuleEquiv (j : fieldData.BosonSpecies) :
    (JetComponentSpace.comap higgsModuleEquiv.toLinearMap).comp
        (JetComponentSpace.comap (fieldData.projBosonField 2 fieldData_boson_massWeight j))
      = LinearMap.id
```

### A.3. The generator identifications

> The generic identification of a generator space with the component space of the whole
> matter field, composed with the relabelling of the target space. `JetComponentSpace.comap`
> is contravariant, so the relabelling `FermionSpace ≃ₗ fieldData.FermionModule` is carried
> by `comapEquiv` to a map *from* the component space of the module *to* that of
> `FermionSpace`, which is the direction the composite needs.

**`StandardModel.fermionGeneratorsEquiv`**, a def, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L217).

> The fermionic generator space of the datum is the component space of the total
> fermionic target space. The generic presentation of the direct sum as the component
> space of the fermionic module, followed by the relabelling of the target space.

```lean
noncomputable def fermionGeneratorsEquiv :
    fieldData.FermionGenerators ≃ₗ[ℂ] JetComponentSpace fermionMatterField
```

**`StandardModel.fermionGeneratorsEquiv_inclFermion`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L226).

> A species sits inside the fermionic generators as the pullback along the projection
> onto that species.

```lean
lemma fermionGeneratorsEquiv_inclFermion (t : fieldData.FermionSpecies)
    (x : JetComponentSpace (fieldData.fermion t)) :
    fermionGeneratorsEquiv (fieldData.inclFermion t x)
      = JetComponentSpace.comap (fermionProj t) x
```

**`StandardModel.fermionGeneratorsEquiv_symm_comap`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L238).

```lean
lemma fermionGeneratorsEquiv_symm_comap (t : fieldData.FermionSpecies)
    (x : JetComponentSpace (fieldData.fermion t)) :
    fermionGeneratorsEquiv.symm (JetComponentSpace.comap (fermionProj t) x)
      = fieldData.inclFermion t x
```

**`JetComponentSpace.comap_snd_of_zero`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L245).

> The second half of a pullback of an unconjugated symbol vanishes.

```lean
lemma _root_.JetComponentSpace.comap_snd_of_zero {G₀ : Type} [Group G₀] {𝔤 : Type} [LieRing 𝔤]
    [LieAlgebra ℝ 𝔤]
    {GJ : Type} [Group GJ] {𝔤J : Type} [LieRing 𝔤J] [LieAlgebra ℝ 𝔤J]
    {jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J} {M N : MatterField jets}
    (f : M.V →ₗ[ℂ] N.V) (x : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ N.V) :
    (JetComponentSpace.comap f ((x, 0) : JetComponentSpace N)).2 = 0
```

**`JetComponentSpace.comap_fst_of_zero`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L256).

> The first half of a pullback of a conjugate symbol vanishes.

```lean
lemma _root_.JetComponentSpace.comap_fst_of_zero {G₀ : Type} [Group G₀] {𝔤 : Type} [LieRing 𝔤]
    [LieAlgebra ℝ 𝔤]
    {GJ : Type} [Group GJ] {𝔤J : Type} [LieRing 𝔤J] [LieAlgebra ℝ 𝔤J]
    {jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J} {M N : MatterField jets}
    (f : M.V →ₗ[ℂ] N.V) (y : SpaceTimeDerivAlgebraℂ ⊗[ℂ] Module.Dual ℂ (ConjModule N.V)) :
    (JetComponentSpace.comap f ((0, y) : JetComponentSpace N)).1 = 0
```

**`StandardModel.fermionGeneratorsEquiv_symm_basis_tmul`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L267).

> The unconjugated symbol `∂_s ψ_φ` of a species, read on the total target space.

```lean
lemma fermionGeneratorsEquiv_symm_basis_tmul (t : fieldData.FermionSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3)) (φ : Module.Dual ℂ (fieldData.FermionValue t)) :
    fermionGeneratorsEquiv.symm ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ]
        Module.Dual.transpose (fermionProj t) φ, 0) : JetComponentSpace fermionMatterField)
      = fieldData.inclFermion t ((SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ, 0) :
          JetComponentSpace (fieldData.fermion t))
```

**`StandardModel.fermionGeneratorsEquiv_symm_basis_tmul_conj`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L283).

> The conjugate symbol `∂_s ψ̄_φ` of a species, read on the total target space.

```lean
lemma fermionGeneratorsEquiv_symm_basis_tmul_conj (t : fieldData.FermionSpecies)
    (s : Multiset (Fin 1 ⊕ Fin 3))
    (φ : Module.Dual ℂ (ConjModule (fieldData.FermionValue t))) :
    fermionGeneratorsEquiv.symm ((0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ]
        Module.Dual.transpose (ConjModule.map (fermionProj t)) φ) :
          JetComponentSpace fermionMatterField)
      = fieldData.inclFermion t ((0, SpaceTimeDerivAlgebraℂ.basis s ⊗ₜ[ℂ] φ) :
          JetComponentSpace (fieldData.fermion t))
```

**`StandardModel.bosonGeneratorsEquiv`**, a def, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L304).

> The bosonic generator space of the datum is the component space of the Higgs.
> There is one bosonic species, so the direct sum has one summand and the relabelling of
> the target space is the identification of a one-element function space with its
> value.

```lean
noncomputable def bosonGeneratorsEquiv :
    fieldData.BosonGenerators ≃ₗ[ℂ] JetComponentSpace HiggsVec.matterField
```

**`StandardModel.bosonGeneratorsEquiv_inclBoson`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L310).

```lean
lemma bosonGeneratorsEquiv_inclBoson (j : fieldData.BosonSpecies)
    (y : JetComponentSpace (fieldData.boson j)) :
    bosonGeneratorsEquiv (fieldData.inclBoson j y) = y
```

**`StandardModel.bosonGeneratorsEquiv_symm_apply`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L319).

```lean
lemma bosonGeneratorsEquiv_symm_apply (y : JetComponentSpace HiggsVec.matterField) :
    bosonGeneratorsEquiv.symm y = fieldData.inclBoson () y
```

## B. The sector algebra equivalences

> Each sector algebra is a free algebra over one presentation of its generator space and the
> corresponding factor of the carrier a free algebra over the other, so the generator
> identifications of section A lift to algebra equivalences by functoriality.

**`StandardModel.fermionAlgebraEquiv`**, a def, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L337).

> The fermionic factor: one exterior algebra, over the two presentations of the same
> generator space.

```lean
noncomputable def fermionAlgebraEquiv :
    FermionJetAlgebra ≃ₐ[ℂ] ExteriorAlgebra ℂ fieldData.FermionGenerators
```

**`StandardModel.higgsAlgebraEquiv`**, a def, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L343).

> The Higgs factor: one symmetric algebra, over the two presentations of the same
> generator space.

```lean
noncomputable def higgsAlgebraEquiv :
    HiggsJetAlgebra ≃ₐ[ℂ] SymmetricAlgebra ℂ fieldData.BosonGenerators
```

**`StandardModel.fermionAlgebraEquiv_ι`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L349).

```lean
lemma fermionAlgebraEquiv_ι (v : JetComponentSpace fermionMatterField) :
    fermionAlgebraEquiv (ExteriorAlgebra.ι ℂ v)
      = ExteriorAlgebra.ι ℂ (fermionGeneratorsEquiv.symm v)
```

**`StandardModel.higgsAlgebraEquiv_ι`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L355).

```lean
lemma higgsAlgebraEquiv_ι (v : JetComponentSpace HiggsVec.matterField) :
    higgsAlgebraEquiv (SymmetricAlgebra.ι ℂ (JetComponentSpace HiggsVec.matterField) v)
      = SymmetricAlgebra.ι ℂ fieldData.BosonGenerators (bosonGeneratorsEquiv.symm v)
```

## C. The generic generators of the field datum

> The degree-one elements of the three factors, included, are the generic generators
> `ιFermion`, `ιBoson` and `ιConnection` of the field datum. These are the reductions the
> named Standard Model field symbols are computed by.

**`StandardModel.includeFermion_ι`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L372).

> A degree-one element of the fermionic factor, included, is a total fermionic
> generator.

```lean
lemma includeFermion_ι (w : fieldData.FermionGenerators) :
    fieldData.includeFermion (ExteriorAlgebra.ι ℂ w) = fieldData.ιFermionTotal w
```

**`StandardModel.includeBoson_ι`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L376).

> A degree-one element of the bosonic factor, included, is a total bosonic generator.

```lean
lemma includeBoson_ι (w : fieldData.BosonGenerators) :
    fieldData.includeBoson (SymmetricAlgebra.ι ℂ fieldData.BosonGenerators w)
      = fieldData.ιBosonTotal w
```

**`StandardModel.includeConnection_one_tmul_ι`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L382).

> A real degree-one element of the connection factor, included, is a connection
> generator.

```lean
lemma includeConnection_one_tmul_ι (v : GaugeBoson.JetComponentSpace GaugeAlgebra) :
    fieldData.includeConnection ((1 : ℂ) ⊗ₜ[ℝ]
        SymmetricAlgebra.ι ℝ (GaugeBoson.JetComponentSpace GaugeAlgebra) v)
      = fieldData.ιConnection v
```

**`StandardModel.ιFermionTotal_inclFermion`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L388).

> The total fermionic generator of a species summand is that species' generator.

```lean
lemma ιFermionTotal_inclFermion (t : fieldData.FermionSpecies)
    (x : JetComponentSpace (fieldData.fermion t)) :
    fieldData.ιFermionTotal (fieldData.inclFermion t x) = fieldData.ιFermion t x
```

**`StandardModel.ιBosonTotal_inclBoson`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L393).

> The total bosonic generator of a species summand is that species' generator.

```lean
lemma ιBosonTotal_inclBoson (j : fieldData.BosonSpecies)
    (y : JetComponentSpace (fieldData.boson j)) :
    fieldData.ιBosonTotal (fieldData.inclBoson j y) = fieldData.ιBoson j y
```

## D. The sector equivalences and the ordinary derivative

> The derivative shift is blind to the value space, so it commutes with the pullback along
> any map of target spaces; the two generator identifications therefore carry the derivative
> shift of the datum to the derivative shift of the total component space, and the
> free-algebra derivations extending them agree.
>
> These are the bridges the migrated total derivative uses to restrict to the sector
> derivatives under their existing names. The species-diagonal half of each is Joseph
> Tooby-Smith's generic `GaugeFieldData.fermionGeneratorsEquiv_jetDerivFermion`; what is
> added here is the relabelling of the target space, which `JetComponentSpace.comap_jetDeriv`
> lets through.

**`StandardModel.fermionGeneratorsEquiv_jetDerivFermion`**, a lemma, [line 416](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L416).

> The fermionic generator identification intertwines the derivative shift of the datum
> with the derivative shift on the component space of the total target space.

```lean
lemma fermionGeneratorsEquiv_jetDerivFermion (μ : Fin 1 ⊕ Fin 3)
    (w : fieldData.FermionGenerators) :
    fermionGeneratorsEquiv (fieldData.jetDerivFermion μ w)
      = JetComponentSpace.jetDeriv μ (fermionGeneratorsEquiv w)
```

**`StandardModel.fermionGeneratorsEquiv_symm_jetDeriv`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L427).

> The inverse form of `fermionGeneratorsEquiv_jetDerivFermion`.

```lean
lemma fermionGeneratorsEquiv_symm_jetDeriv (μ : Fin 1 ⊕ Fin 3)
    (v : JetComponentSpace fermionMatterField) :
    fermionGeneratorsEquiv.symm (JetComponentSpace.jetDeriv μ v)
      = fieldData.jetDerivFermion μ (fermionGeneratorsEquiv.symm v)
```

**`StandardModel.bosonGeneratorsEquiv_jetDerivBoson`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L438).

> The bosonic generator identification intertwines the two derivative shifts.

```lean
lemma bosonGeneratorsEquiv_jetDerivBoson (μ : Fin 1 ⊕ Fin 3)
    (w : fieldData.BosonGenerators) :
    bosonGeneratorsEquiv (fieldData.jetDerivBoson μ w)
      = JetComponentSpace.jetDeriv μ (bosonGeneratorsEquiv w)
```

**`StandardModel.bosonGeneratorsEquiv_symm_jetDeriv`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L449).

> The inverse form of `bosonGeneratorsEquiv_jetDerivBoson`.

```lean
lemma bosonGeneratorsEquiv_symm_jetDeriv (μ : Fin 1 ⊕ Fin 3)
    (v : JetComponentSpace HiggsVec.matterField) :
    bosonGeneratorsEquiv.symm (JetComponentSpace.jetDeriv μ v)
      = fieldData.jetDerivBoson μ (bosonGeneratorsEquiv.symm v)
```

**`StandardModel.fermionAlgebraEquiv_jetDeriv`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L473).

> The fermionic sector equivalence is a map of differential algebras: the exterior
> derivation extending the derivative shift on the total target space goes to the exterior
> derivation extending the derivative shift of the datum.

```lean
lemma fermionAlgebraEquiv_jetDeriv (μ : Fin 1 ⊕ Fin 3) (f : FermionJetAlgebra) :
    fermionAlgebraEquiv (FermionicAlgebra.jetDeriv μ f)
      = ExteriorAlgebra.derivationOfLinear (fieldData.jetDerivFermion μ)
          (fermionAlgebraEquiv f)
```

**`StandardModel.higgsAlgebraEquiv_jetDeriv`**, a lemma, [line 482](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean#L482).

> The Higgs sector equivalence is a map of differential algebras.

```lean
lemma higgsAlgebraEquiv_jetDeriv (μ : Fin 1 ⊕ Fin 3) (h : HiggsJetAlgebra) :
    higgsAlgebraEquiv (BosonicAlgebra.jetDeriv μ h)
      = SymmetricAlgebra.derivationOfLinear (fieldData.jetDerivBoson μ)
          (higgsAlgebraEquiv h)
```

## Depends on

- [The local field algebra of a gauge theory and its universal property](../../../classicalfieldtheory/gaugetheory/part-03/localfield-basic.md)
- [The fermionic jet algebra of the Standard Model](../part-03/fermions-jetalgebra-basic.md)
- [The field data of the Standard Model](../part-01/fielddata.md)
- [The jet algebra of the Higgs field](../part-05/higgsboson-jetalgebra-algebra.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/SectorEquiv/Basic.lean)

---
declaration: module
origin: cited
lean: StandardModel.FermionSpace, StandardModel.generations, StandardModel.fermionMatterField, StandardModel.fermionMatterField_V, StandardModel.FermionSpace.leptonDoubletProj, StandardModel.FermionSpace.leptonSingletProj, StandardModel.FermionSpace.quarkDoubletProj, StandardModel.FermionSpace.upSingletProj
statement: formalized
proof: formalized
---

# The fermionic jet algebra of the Standard Model

The module `PhyslibAlpha.Particles.StandardModel.Fermions.JetAlgebra.Basic`, [PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean): 49 declarations, 43 with a docstring.

## i. Overview

> The jet algebra of the Standard Model is the algebra in which a Lagrangian lives: the free
> algebra on the component functions of every field and all their spacetime derivatives,
> subject only to the statistics of the fields.
>
> This file builds its fermionic factor, `FermionJetAlgebra`; the bosonic factors — the gauge
> fields and the Higgs — commute with everything and will enter as separate tensor factors.
>
> The Standard Model carries five fermion species — the lepton doublet, the charged-lepton
> singlet, the quark doublet, and the up- and down-type quark singlets — each in three
> generations, and the fermionic jet algebra is the *exterior product* of their individual
> fermionic algebras: generators anticommute, and they do so **across species and generations
> as well as within a species**, since all of them are fermionic.
>
> That exterior product is *realized* here as a single exterior algebra on the direct sum of
> the fifteen target spaces, and then *identified* with the graded tensor product of the
> species algebras by `FermionicAlgebra.prodEquiv`, applied once per species
> (`FermionJetAlgebra.exteriorProductLeptonDoublet` and its siblings below). The
> identification is genuine, not a convention: the exterior algebra of a direct sum is the
> graded (super) tensor product of the exterior algebras of the summands. An ordinary tensor
> product `⊗[ℂ]` would instead make generators of different species *commute*, which is wrong
> for fermions.
>
> The direct sum is taken as the definition rather than the graded tensor product because
> Mathlib's `GradedTensorProduct` carries no `GradedAlgebra` instance, so a graded tensor
> product of three or more factors cannot currently be written down as a type; the peeled
> form, one species at a time, is as far as the type-level statement goes. Working inside a
> single `ExteriorAlgebra` also keeps every algebraic class projecting from one root, and lets
> the whole `FermionicAlgebra` API — the Lorentz action, the jet gauge action, the total
> derivative and its iterates — apply to `FermionJetAlgebra` unchanged.

## ii. Key results

> - `FermionSpace` : the total target space of the Standard Model fermions.
> - `FermionSpace.leptonDoubletProj`, … : the projections onto a species and generation.
> - `FermionSpace.leptonDoubletIncl`, … : the inclusions of a species and generation.
> - `FermionJetAlgebra` : the jet algebra of the Standard Model fermions.
> - `FermionJetAlgebra.ofLeptonDoublet`, … : the component functions of each species and
>   generation.
> - `FermionJetAlgebra.exteriorProductLeptonDoublet`, … : the jet algebra as the exterior
>   product of the species algebras.

## iv. References

> * None.

## A. The target space of the Standard Model fermions

**`StandardModel.FermionSpace`**, an abbrev, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L96).

> The total target space of the Standard Model fermions: the direct sum of three
> generations each of the lepton doublet, the charged-lepton singlet, the quark doublet, and
> the up- and down-type quark singlets. The three generations of a species sit together, so
> that a species can be split off the jet algebra as a single exterior factor.

```lean
abbrev FermionSpace : Type
```

**`StandardModel.generations`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L102).

> The matter field of three generations of one fermion species: the direct sum of three
> copies of it, which all carry the same mass weight and the same declared statistic.

```lean
noncomputable def generations (M : MatterField localGaugeData) : MatterField localGaugeData
```

**`StandardModel.fermionMatterField`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L109).

> **The fermionic matter field of the Standard Model**: the direct sum of three
> generations of each of the five species, in the order in which `FermionSpace` lists them.
> Its value space is `FermionSpace` by definition, and every summand carries mass weight
> three and is declared fermionic, which is what lets the direct sums be formed.

```lean
noncomputable def fermionMatterField : MatterField localGaugeData
```

**`StandardModel.fermionMatterField_V`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L116).

```lean
lemma fermionMatterField_V : fermionMatterField.V = FermionSpace
```

### A.1. The projections onto the species

> The component functions of a field are *covectors* on its target space, so it is the
> projections — not the inclusions — that carry the individual species into the jet algebra.
> Each projection takes a generation index `i : Fin 3`.

**`StandardModel.FermionSpace.leptonDoubletProj`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L131).

> The projection onto the `i`-th generation of the lepton doublet.

```lean
noncomputable def leptonDoubletProj (i : Fin 3) : FermionSpace →ₗ[ℂ] LeptonDoubletV
```

**`StandardModel.FermionSpace.leptonSingletProj`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L135).

> The projection onto the `i`-th generation of the charged-lepton singlet.

```lean
noncomputable def leptonSingletProj (i : Fin 3) : FermionSpace →ₗ[ℂ] LeptonSinglet
```

**`StandardModel.FermionSpace.quarkDoubletProj`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L139).

> The projection onto the `i`-th generation of the quark doublet.

```lean
noncomputable def quarkDoubletProj (i : Fin 3) : FermionSpace →ₗ[ℂ] QuarkDoublet
```

**`StandardModel.FermionSpace.upSingletProj`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L144).

> The projection onto the `i`-th generation of the up-type quark singlet.

```lean
noncomputable def upSingletProj (i : Fin 3) : FermionSpace →ₗ[ℂ] UpSinglet
```

**`StandardModel.FermionSpace.downSingletProj`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L149).

> The projection onto the `i`-th generation of the down-type quark singlet.

```lean
noncomputable def downSingletProj (i : Fin 3) : FermionSpace →ₗ[ℂ] DownSinglet
```

### A.2. The inclusions onto the species

> The one-sided inverses of the projections: the inclusion of a single species and generation
> as a summand of the total target space, zero in every other slot. `…Proj i ∘ …Incl i` is the
> identity, and every other composite of a projection with an inclusion vanishes.

**`StandardModel.FermionSpace.leptonDoubletIncl`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L164).

> The inclusion of the `i`-th generation lepton doublet as a summand.

```lean
noncomputable def leptonDoubletIncl (i : Fin 3) : LeptonDoubletV →ₗ[ℂ] FermionSpace
```

**`StandardModel.FermionSpace.leptonSingletIncl`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L168).

> The inclusion of the `i`-th generation charged-lepton singlet as a summand.

```lean
noncomputable def leptonSingletIncl (i : Fin 3) : LeptonSinglet →ₗ[ℂ] FermionSpace
```

**`StandardModel.FermionSpace.quarkDoubletIncl`**, a def, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L173).

> The inclusion of the `i`-th generation quark doublet as a summand.

```lean
noncomputable def quarkDoubletIncl (i : Fin 3) : QuarkDoublet →ₗ[ℂ] FermionSpace
```

**`StandardModel.FermionSpace.upSingletIncl`**, a def, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L179).

> The inclusion of the `i`-th generation up-type quark singlet as a summand.

```lean
noncomputable def upSingletIncl (i : Fin 3) : UpSinglet →ₗ[ℂ] FermionSpace
```

**`StandardModel.FermionSpace.downSingletIncl`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L185).

> The inclusion of the `i`-th generation down-type quark singlet as a summand.

```lean
noncomputable def downSingletIncl (i : Fin 3) : DownSinglet →ₗ[ℂ] FermionSpace
```

**`StandardModel.FermionSpace.leptonDoubletProj_comp_leptonDoubletIncl`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L191).

```lean
lemma leptonDoubletProj_comp_leptonDoubletIncl (i : Fin 3) :
    (leptonDoubletProj i).comp (leptonDoubletIncl i) = LinearMap.id
```

**`StandardModel.FermionSpace.leptonSingletProj_comp_leptonSingletIncl`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L196).

```lean
lemma leptonSingletProj_comp_leptonSingletIncl (i : Fin 3) :
    (leptonSingletProj i).comp (leptonSingletIncl i) = LinearMap.id
```

**`StandardModel.FermionSpace.quarkDoubletProj_comp_quarkDoubletIncl`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L201).

```lean
lemma quarkDoubletProj_comp_quarkDoubletIncl (i : Fin 3) :
    (quarkDoubletProj i).comp (quarkDoubletIncl i) = LinearMap.id
```

**`StandardModel.FermionSpace.upSingletProj_comp_upSingletIncl`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L206).

```lean
lemma upSingletProj_comp_upSingletIncl (i : Fin 3) :
    (upSingletProj i).comp (upSingletIncl i) = LinearMap.id
```

**`StandardModel.FermionSpace.downSingletProj_comp_downSingletIncl`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L211).

```lean
lemma downSingletProj_comp_downSingletIncl (i : Fin 3) :
    (downSingletProj i).comp (downSingletIncl i) = LinearMap.id
```

### A.3. The action of the Lorentz group

**`Representation.pi`**, a def, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L222).

> The pointwise representation on a finite power of the representation space.

```lean
noncomputable def _root_.Representation.pi {k G V : Type*} (ι : Type*) [CommSemiring k]
    [Monoid G] [AddCommMonoid V] [Module k V] (ρ : Representation k G V) :
    Representation k G (ι → V)
```

**`StandardModel.FermionSpace.repLorentzGroup`**, a def, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L236).

> The Lorentz action on the total fermionic target space: each species and generation
> transforms in its own Lorentz representation.

```lean
noncomputable def repLorentzGroup : Representation ℂ SL(2,ℂ) FermionSpace
```

### A.4. The action of the global gauge group

**`StandardModel.FermionSpace.repGaugeGroupI`**, a def, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L251).

> The global gauge action on the total fermionic target space: each species and
> generation transforms in its own representation of the gauge group.

```lean
noncomputable def repGaugeGroupI : Representation ℂ GaugeGroupI FermionSpace
```

### A.5. The action of the jet gauge group

> The jets of the total fermionic field split as the product of the jets of the species,
> generation by generation; a jet of gauge transformations acts on each factor through the
> species' own jet action. The identification is `SpaceTimeAlgebra`-linear, so the fibrewise
> linearity of the species actions is inherited by the product.

**`StandardModel.FermionSpace.jetEquiv`**, a def, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L272).

> The jets of the total fermionic field as the product of the jets of the species and
> generations. The identification is `SpaceTimeAlgebra`-linear.

```lean
noncomputable def jetEquiv :
    SpaceTimeAlgebra ⊗[ℂ] FermionSpace ≃ₗ[SpaceTimeAlgebra]
      (Fin 3 → SpaceTimeAlgebra ⊗[ℂ] LeptonDoubletV) ×
        ((Fin 3 → SpaceTimeAlgebra ⊗[ℂ] LeptonSinglet) ×
          ((Fin 3 → SpaceTimeAlgebra ⊗[ℂ] QuarkDoublet) ×
            ((Fin 3 → SpaceTimeAlgebra ⊗[ℂ] UpSinglet) ×
              (Fin 3 → SpaceTimeAlgebra ⊗[ℂ] DownSinglet))))
```

**`StandardModel.FermionSpace.jetActionMap`**, a def, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L292).

> The map through which a jet of gauge transformations acts on the jets of the total
> fermionic field: the species actions, factor by factor.

```lean
noncomputable def jetActionMap (U : JetGaugeGroupI) :
    ((Fin 3 → SpaceTimeAlgebra ⊗[ℂ] LeptonDoubletV) ×
      ((Fin 3 → SpaceTimeAlgebra ⊗[ℂ] LeptonSinglet) ×
        ((Fin 3 → SpaceTimeAlgebra ⊗[ℂ] QuarkDoublet) ×
          ((Fin 3 → SpaceTimeAlgebra ⊗[ℂ] UpSinglet) ×
            (Fin 3 → SpaceTimeAlgebra ⊗[ℂ] DownSinglet))))) →ₗ[ℂ]
    ((Fin 3 → SpaceTimeAlgebra ⊗[ℂ] LeptonDoubletV) ×
      ((Fin 3 → SpaceTimeAlgebra ⊗[ℂ] LeptonSinglet) ×
        ((Fin 3 → SpaceTimeAlgebra ⊗[ℂ] QuarkDoublet) ×
          ((Fin 3 → SpaceTimeAlgebra ⊗[ℂ] UpSinglet) ×
            (Fin 3 → SpaceTimeAlgebra ⊗[ℂ] DownSinglet)))))
```

**`LinearMap.piMap_id`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L310).

> The pointwise lift of the identity maps is the identity.

```lean
lemma _root_.LinearMap.piMap_id {R ι : Type*} {φ : ι → Type*} [Semiring R]
    [∀ i, AddCommMonoid (φ i)] [∀ i, Module R (φ i)] :
    LinearMap.piMap (fun i => (LinearMap.id : φ i →ₗ[R] φ i)) = LinearMap.id
```

**`LinearMap.piMap_comp_piMap`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L316).

> The pointwise lift of compositions is the composition of the pointwise lifts.

```lean
lemma _root_.LinearMap.piMap_comp_piMap {R ι : Type*} {φ ψ ω : ι → Type*} [Semiring R]
    [∀ i, AddCommMonoid (φ i)] [∀ i, Module R (φ i)]
    [∀ i, AddCommMonoid (ψ i)] [∀ i, Module R (ψ i)]
    [∀ i, AddCommMonoid (ω i)] [∀ i, Module R (ω i)]
    (f : ∀ i, ψ i →ₗ[R] ω i) (g : ∀ i, φ i →ₗ[R] ψ i) :
    (LinearMap.piMap f).comp (LinearMap.piMap g)
      = LinearMap.piMap fun i => (f i).comp (g i)
```

**`StandardModel.FermionSpace.jetActionMap_one`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L327).

> The map of jets of the identity is the identity.

```lean
lemma jetActionMap_one : jetActionMap 1 = LinearMap.id
```

**`StandardModel.FermionSpace.jetActionMap_mul`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L333).

> The map of jets of a product is the composition of the maps of jets.

```lean
lemma jetActionMap_mul (U V : JetGaugeGroupI) :
    jetActionMap (U * V) = (jetActionMap U).comp (jetActionMap V)
```

**`StandardModel.FermionSpace.repJetGaugeGroupI`**, a def, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L345).

> **The jet gauge action on the jets of the total fermionic field**: the species
> actions, transported through the splitting of the jets.

```lean
noncomputable def repJetGaugeGroupI :
    Representation ℂ JetGaugeGroupI (SpaceTimeAlgebra ⊗[ℂ] FermionSpace)
```

**`StandardModel.FermionSpace.repJetGaugeGroupI_smul`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L370).

> **The jet gauge action on the jets of the total fermionic field is fibrewise**: it
> commutes with multiplication by scalar jets, because the splitting of the jets is
> `SpaceTimeAlgebra`-linear and each species action is fibrewise.

```lean
lemma repJetGaugeGroupI_smul (U : JetGaugeGroupI) (χ : SpaceTimeAlgebra)
    (z : SpaceTimeAlgebra ⊗[ℂ] FermionSpace) :
    repJetGaugeGroupI U (χ • z) = χ • repJetGaugeGroupI U z
```

## B. The fermionic jet algebra

**`StandardModel.FermionJetAlgebra`**, an abbrev, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L411).

> **The jet algebra of the Standard Model fermions**: the exterior product of the fermionic
> algebras of the five species, realized as the fermionic algebra of their direct sum. Its
> generators are the component functions `∂_s ψ_φ` and `∂_s ψ̄_φ` of every species and
> generation, and any two of them anticommute — within a species and across species alike.
>
> This is the fermionic factor of the full Standard Model jet algebra; the gauge and Higgs
> factors are bosonic and commute with it.

```lean
abbrev FermionJetAlgebra : Type
```

### B.1. The component functions of each species

> Each species and generation enters through its projection out of `FermionSpace`: a covector
> on the species pulls back to a covector on the total target space, and thence to a generator
> of the jet algebra. Their iterated derivatives `FermionicAlgebra.iteratedJetDeriv` are the
> higher generators.

**`StandardModel.FermionJetAlgebra.ofLeptonDoublet`**, a def, [line 428](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L428).

> The component functions of the `i`-th generation lepton doublet inside the Standard
> Model jet algebra.

```lean
noncomputable def ofLeptonDoublet (i : Fin 3) :
    Module.Dual ℂ LeptonDoubletV →ₗ[ℂ] FermionJetAlgebra
```

**`StandardModel.FermionJetAlgebra.ofLeptonSinglet`**, a def, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L433).

> The component functions of the `i`-th generation charged-lepton singlet.

```lean
noncomputable def ofLeptonSinglet (i : Fin 3) :
    Module.Dual ℂ LeptonSinglet →ₗ[ℂ] FermionJetAlgebra
```

**`StandardModel.FermionJetAlgebra.ofQuarkDoublet`**, a def, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L438).

> The component functions of the `i`-th generation quark doublet.

```lean
noncomputable def ofQuarkDoublet (i : Fin 3) :
    Module.Dual ℂ QuarkDoublet →ₗ[ℂ] FermionJetAlgebra
```

**`StandardModel.FermionJetAlgebra.ofUpSinglet`**, a def, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L443).

> The component functions of the `i`-th generation up-type quark singlet.

```lean
noncomputable def ofUpSinglet (i : Fin 3) :
    Module.Dual ℂ UpSinglet →ₗ[ℂ] FermionJetAlgebra
```

**`StandardModel.FermionJetAlgebra.ofDownSinglet`**, a def, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L448).

> The component functions of the `i`-th generation down-type quark singlet.

```lean
noncomputable def ofDownSinglet (i : Fin 3) :
    Module.Dual ℂ DownSinglet →ₗ[ℂ] FermionJetAlgebra
```

**`StandardModel.FermionJetAlgebra.ofConjLeptonDoublet`**, a def, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L453).

> The conjugate component functions of the `i`-th generation lepton doublet.

```lean
noncomputable def ofConjLeptonDoublet (i : Fin 3) :
    Module.Dual ℂ (ConjModule LeptonDoubletV) →ₗ[ℂ] FermionJetAlgebra
```

**`StandardModel.FermionJetAlgebra.ofConjLeptonSinglet`**, a def, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L459).

> The conjugate component functions of the `i`-th generation charged-lepton singlet.

```lean
noncomputable def ofConjLeptonSinglet (i : Fin 3) :
    Module.Dual ℂ (ConjModule LeptonSinglet) →ₗ[ℂ] FermionJetAlgebra
```

**`StandardModel.FermionJetAlgebra.ofConjQuarkDoublet`**, a def, [line 465](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L465).

> The conjugate component functions of the `i`-th generation quark doublet.

```lean
noncomputable def ofConjQuarkDoublet (i : Fin 3) :
    Module.Dual ℂ (ConjModule QuarkDoublet) →ₗ[ℂ] FermionJetAlgebra
```

**`StandardModel.FermionJetAlgebra.ofConjUpSinglet`**, a def, [line 471](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L471).

> The conjugate component functions of the `i`-th generation up-type quark singlet.

```lean
noncomputable def ofConjUpSinglet (i : Fin 3) :
    Module.Dual ℂ (ConjModule UpSinglet) →ₗ[ℂ] FermionJetAlgebra
```

**`StandardModel.FermionJetAlgebra.ofConjDownSinglet`**, a def, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L477).

> The conjugate component functions of the `i`-th generation down-type quark singlet.

```lean
noncomputable def ofConjDownSinglet (i : Fin 3) :
    Module.Dual ℂ (ConjModule DownSinglet) →ₗ[ℂ] FermionJetAlgebra
```

### B.2. The exterior product decomposition

> `FermionicAlgebra.prodEquiv` identifies the fermionic algebra of a direct sum with the
> graded tensor product of the two fermionic algebras. Applied repeatedly it exhibits the jet
> algebra as the exterior product of the five species algebras, peeling off one species — all
> three of its generations at once — at a time. It has to be stated one species at a time:
> `GradedTensorProduct` carries no `GradedAlgebra` instance in Mathlib, so the fully nested
> five-fold graded tensor product is not expressible as a type.

**`StandardModel.FermionJetAlgebra.exteriorProductLeptonDoublet`**, a def, [line 499](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L499).

> The fermionic jet algebra as the exterior product of the three-generation
> lepton-doublet algebra with the algebra of the remaining four species.

```lean
noncomputable def exteriorProductLeptonDoublet :
    FermionJetAlgebra ≃ₐ[ℂ] (FermionicAlgebra.evenOdd (generations LeptonDoubletV.matterField) ᵍ⊗[ℂ]
      FermionicAlgebra.evenOdd
          ((generations LeptonSinglet.matterField).prod
          ((generations QuarkDoublet.matterField).prod
          ((generations UpSinglet.matterField).prod
          (generations DownSinglet.matterField) rfl rfl) rfl rfl) rfl rfl))
```

**`StandardModel.FermionJetAlgebra.exteriorProductLeptonSinglet`**, a def, [line 513](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L513).

> The charged-lepton singlets split off the remaining three species.

```lean
noncomputable def exteriorProductLeptonSinglet :
    FermionicAlgebra
        ((generations LeptonSinglet.matterField).prod
        ((generations QuarkDoublet.matterField).prod
        ((generations UpSinglet.matterField).prod (generations DownSinglet.matterField) rfl rfl)
        rfl rfl) rfl rfl) ≃ₐ[ℂ]
      (FermionicAlgebra.evenOdd (generations LeptonSinglet.matterField) ᵍ⊗[ℂ]
        FermionicAlgebra.evenOdd
            ((generations QuarkDoublet.matterField).prod
            ((generations UpSinglet.matterField).prod
            (generations DownSinglet.matterField) rfl rfl) rfl rfl))
```

**`StandardModel.FermionJetAlgebra.exteriorProductQuarkDoublet`**, a def, [line 530](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L530).

> The quark doublets split off the two quark singlets.

```lean
noncomputable def exteriorProductQuarkDoublet :
    FermionicAlgebra
        ((generations QuarkDoublet.matterField).prod
        ((generations UpSinglet.matterField).prod
        (generations DownSinglet.matterField) rfl rfl) rfl rfl) ≃ₐ[ℂ]
      (FermionicAlgebra.evenOdd (generations QuarkDoublet.matterField) ᵍ⊗[ℂ]
        FermionicAlgebra.evenOdd
            ((generations UpSinglet.matterField).prod (generations DownSinglet.matterField)
              rfl rfl))
```

**`StandardModel.FermionJetAlgebra.exteriorProductUpSinglet`**, a def, [line 543](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L543).

> The two quark singlets as an exterior product.

```lean
noncomputable def exteriorProductUpSinglet :
    FermionicAlgebra
        ((generations UpSinglet.matterField).prod (generations DownSinglet.matterField)
          rfl rfl) ≃ₐ[ℂ]
      (FermionicAlgebra.evenOdd (generations UpSinglet.matterField) ᵍ⊗[ℂ]
        FermionicAlgebra.evenOdd (generations DownSinglet.matterField))
```

### B.3. The actions on the fermionic jet algebra

**`StandardModel.FermionJetAlgebra.repLorentzGroup`**, a def, [line 560](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L560).

> The Lorentz action on the fermionic jet algebra of the Standard Model.

```lean
noncomputable def repLorentzGroup : Representation ℂ SL(2,ℂ) FermionJetAlgebra
```

**`StandardModel.FermionJetAlgebra.repJetGaugeGroupI`**, a def, [line 564](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L564).

> The jet gauge action on the fermionic jet algebra of the Standard Model.

```lean
noncomputable def repJetGaugeGroupI : Representation ℂ JetGaugeGroupI FermionJetAlgebra
```

**`StandardModel.FermionJetAlgebra.repGaugeGroupI`**, a def, [line 568](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L568).

> The global gauge action on the fermionic jet algebra of the Standard Model.

```lean
noncomputable def repGaugeGroupI : Representation ℂ GaugeGroupI FermionJetAlgebra
```

### B.4. The mass-dimension scaling

**`StandardModel.FermionJetAlgebra.massWeightScale`**, a def, [line 580](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean#L580).

> The mass-dimension scaling on the fermionic jet algebra: every Standard Model fermion
> has mass dimension `3/2`, that is mass weight three, and each derivative adds mass
> weight two.

```lean
noncomputable def massWeightScale (c : ℂ) : FermionJetAlgebra →ₐ[ℂ] FermionJetAlgebra
```

## Depends on

- [The direct sum of a finite family of matter fields](../../../classicalfieldtheory/gaugetheory/part-05/matterfield-pi.md)
- [The Standard Model fermions as matter fields](fermions-matterfield.md)
- [The gauge action on the fermionic algebra](../part-09/matter-fermionic-gaugeaction.md)
- [The Lorentz action on the fermionic algebra](../part-09/matter-fermionic-lorentzaction.md)
- [Mass dimension on the fermionic algebra](../part-09/matter-fermionic-massdim.md)
- [The fermionic algebra of a direct sum](../part-09/matter-fermionic-prod.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/JetAlgebra/Basic.lean)

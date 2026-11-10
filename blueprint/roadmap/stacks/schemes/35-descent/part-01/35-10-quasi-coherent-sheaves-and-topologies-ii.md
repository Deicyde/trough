---
declaration: section
origin: cited
lean: AlgebraicGeometry.SmallEtale.isFlatMapULift_inverseImageStructureMap, AlgebraicGeometry.BigFppfOver.baseAssociatedModuleTensorIso, AlgebraicGeometry.BigFppfOver.essImage_X₂_of_shortExact_big, AlgebraicGeometry.BigFppfOver.exists_isoSections_X₂_of_shortExact_big, AlgebraicGeometry.BigFppfOver.fullyFaithfulBaseAssociatedModuleQcoh, AlgebraicGeometry.AssociatedModuleNotExact.not_mono_map_two_nsmul_qcoh, AlgebraicGeometry.AssociatedModuleNotExact.not_preservesMonomorphisms_baseAssociatedModuleQcoh, AlgebraicGeometry.AssociatedModuleNotExact.not_preservesFiniteLimits_baseAssociatedModuleQcoh
statement: formalized
proof: formalized
---

# 35.10 Quasi-coherent sheaves and topologies, II

Section 35.10 of the Stacks Project, [Tag 0GN9](https://stacks.math.columbia.edu/tag/0GN9). 5 tags here are carried by 72 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GNA, a lemma

[Tag 0GNA](https://stacks.math.columbia.edu/tag/0GNA) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.isFlatMapULift_inverseImageStructureMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFlatInverseImage.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleFlatInverseImage.lean#L354).

> **Stacks 0GNA.**  The morphism of ringed sites `ε = id_{small, étale, Zar} : S_étale → S_Zar`
> is flat: `𝒪_{S_étale}` is a flat module over `ε⁻¹𝒪_{S_Zar}`, the flatness being asserted for
> the structure map `AlgebraicGeometry.SmallEtale.inverseImageStructureMap` of `ε` in
> inverse-image form.
>
> This is also the first assertion of **Stacks 08H8**, which states exactly that the `ε` of
> Equation 75.4.0.1 — `AlgebraicGeometry.SmallEtale.toZariskiRingedToposHom`, carrying Stacks
> 08H7 — is a flat morphism of ringed sites, and cites Descent, Lemma 35.10.1, which is 0GNA,
> for it.  The second assertion of 08H8, exactness of `ε^*`, is carried by
> `AlgebraicGeometry.SmallEtale.exactFunctor_pullbackModules_toZariski`.  The third, the
> implication `ε^*𝓕 = 0 ⟹ 𝓕 = 0`, is *not* carried by this statement and is not available in
> the library; the attribute clause records that scope.

```lean
public theorem isFlatMapULift_inverseImageStructureMap :
    AlgebraicGeometry.SheafOfModules.IsFlatMapULift.{u, u + 1, u}
      (inverseImageStructureMap B S hS)
```

## Tag 06VE, a lemma

[Tag 06VE](https://stacks.math.columbia.edu/tag/06VE) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.baseAssociatedModuleTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseAssociatedModuleTensor.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseAssociatedModuleTensor.lean#L177). The attribute's comment: “part (7), big site (Sch/S)_τ at every τ, for arbitrary 𝒪_S-modules”.

> **Descent, Lemma 06VE (7) for the big `τ`-site, at every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.**  The comparison `𝓕 ↦ 𝓕^a` of Descent,
> Proposition 03DX carries a tensor product of `𝒪_S`-modules to the tensor product of their
> images: `(𝓗 ⊗_{𝒪_S} 𝓘)^a ≅ 𝓗^a ⊗_𝒪 𝓘^a` in `Mod((Sch/S)_τ, 𝒪)`.
>
> This is Stacks 03EL, `Stacks.SheafOfModules.pullbackTensorIso`, for the morphism of ringed
> topoi attached to the comparison of Stacks 070U, carried across
> `AlgebraicGeometry.BigFppfOver.pullbackModulesIsoBaseAssociatedModule`.
>
> No hypothesis is carried, and in particular quasi-coherence is not needed: the statement holds
> for arbitrary `𝒪_S`-modules.  06VE states it for `QCoh(𝒪_S)` only because that is the source
> category on which its functor is an equivalence, so this is the clause with its hypothesis
> dropped rather than added to.
>
> The tensor products are `(Stacks.SheafOfModules.Tensor.sheafTensor O).obj H`, the sheafification
> of the objectwise tensor product of the underlying presheaves of modules (Stacks 05NB); that
> functor's value agrees with the bifunctor of Tag 01CA by
> `AlgebraicGeometry.BigFppfOver.tensorSheafBifunctor_obj_eq`.

```lean
public def baseAssociatedModuleTensorIso (τ : SiteKind) (H I : S.Modules) :
    (baseAssociatedModule B S hS τ).obj
        (((Stacks.SheafOfModules.Tensor.sheafTensor S.sheaf).obj H).obj I) ≅
      ((Stacks.SheafOfModules.Tensor.sheafTensor
            (FibredSite.baseStructureSheaf B S hS τ)).obj
          ((baseAssociatedModule B S hS τ).obj H)).obj
        ((baseAssociatedModule B S hS τ).obj I)
```

**`AlgebraicGeometry.BigFppfOver.essImage_X₂_of_shortExact_big`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseExtensionEssImage.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseExtensionEssImage.lean#L118). The attribute's comment: “part (10), big site (Sch/S)_τ at every τ ∈ {Zariski, étale, smooth, syntomic, fppf}, for the PULLBACK-defined functor 𝓕 ↦ 𝓕ᵃ of Remark 03FH. The same clause for the sections-defined 𝓕ᵃ of Definition 03DU (3) is exists_isoSections_X₂_of_shortExact_big; the two sheaves are identified by baseAssociatedModuleIsoSections, Stacks 070S (1). The clause read as "the middle term is quasi-coherent", which names no functor, is clause (4) of Stacks 0GNC and sits on isQuasicoherentOnSite_shortExact_X₂_all”.

> **Stacks 06VE (10) on the big site `(Sch/S)_τ`, at every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}` and with no hypothesis.**  Given a short exact
> sequence `0 → 𝓕₁ᵃ → 𝓔 → 𝓕₂ᵃ → 0` of `𝒪`-modules on `(Sch/S)_τ` whose outer terms are
> quasi-coherent — which at every `τ` is the same as their being `𝓕ᵃ`'s, by Descent,
> Proposition 03DX (1) — the middle term `𝓔` is itself in the essential image of
> `𝓕 ↦ 𝓕ᵃ : QCoh(𝒪_S) ⥤ Mod((Sch/S)_τ, 𝒪)`, namely of `𝓔|_{S_Zar}`.
>
> The source's three steps are
> `StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseExtensionClosure.lean`; of the two
> hypotheses they carry, essential surjectivity is
> `AlgebraicGeometry.BigFppfOver.baseQuasicoherentIsEssImageAssociatedModule` and right
> exactness of restriction to `S_Zar` is
> `AlgebraicGeometry.BigFppfOver.epi_baseRestrictModule_map_all`.
>
> This is the clause for the *pullback*-defined `𝓕 ↦ 𝓕ᵃ` of Remark 03FH;
> `AlgebraicGeometry.BigFppfOver.exists_isoSections_X₂_of_shortExact_big` is it for the
> sections-defined `𝓕ᵃ` of Definition 03DU (3), which is the sheaf the source constructs.

```lean
public theorem essImage_X₂_of_shortExact_big (τ : SiteKind)
    {C : ShortComplex (SheafOfModules.{u} (FibredSite.baseRingStructureSheaf B S hS τ))}
    (hC : C.ShortExact) (h₁ : C.X₁.IsQuasicoherentOnSite) (h₃ : C.X₃.IsQuasicoherentOnSite) :
    (baseAssociatedModuleQcoh B S hS τ).essImage C.X₂
```

**`AlgebraicGeometry.BigFppfOver.exists_isoSections_X₂_of_shortExact_big`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseExtensionEssImage.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseExtensionEssImage.lean#L176). The attribute's comment: “part (10), big site (Sch/S)_τ at every τ ∈ {Zariski, étale, smooth, syntomic, fppf}, for the SECTIONS-defined 𝓕ᵃ of Definition 03DU (3) — the τ-sheafification of (f : T → S) ↦ Γ(T, f^*𝓕). The same clause for the pullback-defined functor of Remark 03FH is essImage_X₂_of_shortExact_big; the two sheaves are identified by baseAssociatedModuleIsoSections, Stacks 070S (1)”.

> **Stacks 06VE (10) on the big site `(Sch/S)_τ` at every `τ`, for the sheaf the source
> constructs.**  Given a short exact sequence `0 → 𝓕₁ᵃ → 𝓔 → 𝓕₂ᵃ → 0` of `𝒪`-modules on
> `(Sch/S)_τ` whose outer terms are quasi-coherent, there is a quasi-coherent `𝒪_S`-module `𝓕` with
> `𝓔 ≅ 𝓕ᵃ`, where `𝓕ᵃ` is the **sections**-defined associated module of Stacks Definition 03DU (3)
> — the `τ`-sheafification of `(f : T → S) ↦ Γ(T, f^*𝓕)`.
>
> `AlgebraicGeometry.BigFppfOver.essImage_X₂_of_shortExact_big` is the same clause for the
> pullback-defined `𝓕ᵃ` of Remark 03FH; this is it read through
> `AlgebraicGeometry.BigFppfOver.baseAssociatedModuleIsoSections`, Stacks 070S (1).  The witness is
> `𝓕 = 𝓔|_{S_Zar}`, quasi-coherent by
> `AlgebraicGeometry.BigFppfOver.isQuasicoherent_baseRestrictModule_X₂`, and the isomorphism is
> `AlgebraicGeometry.BigFppfOver.sectionsIso_X₂_of_shortExact_big`.

```lean
public theorem exists_isoSections_X₂_of_shortExact_big (τ : SiteKind)
    {C : ShortComplex (SheafOfModules.{u} (FibredSite.baseRingStructureSheaf B S hS τ))}
    (hC : C.ShortExact) (h₁ : C.X₁.IsQuasicoherentOnSite) (h₃ : C.X₃.IsQuasicoherentOnSite) :
    ∃ F : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory,
      Nonempty (C.X₂ ≅ (PresheafOfModules.sheafification.{u}
          (𝟙 (FibredSite.baseRingStructureSheaf B S hS τ).obj)).obj
        (sectionsPresheafOfModules B S hS F.obj))
```

**`AlgebraicGeometry.BigFppfOver.fullyFaithfulBaseAssociatedModuleQcoh`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseFullyFaithful.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseFullyFaithful.lean#L208). The attribute's comment: “part (1), big site, every τ”.

> **Stacks 0GN7 for the big site, and clause (1) of Stacks 06VE for it.**  For every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}` the functor `𝓕 ↦ 𝓕^a` of Definition 03DU, from
> the quasi-coherent `𝒪_S`-modules to the `𝒪`-modules on the big site `(Sch/S)_τ`, is fully
> faithful.
>
> The two tags assert one thing of one functor, and the clause strings record the scope this
> declaration proves — on **one source line**, because a tag registry that reads the attributes
> matches a second `stacks` clause only when it is on the same line as the first, and two clause
> strings plus the attribute syntax do not fit in a hundred characters unless both are short.  The
> 0GN7 string therefore no longer ends `; small site S_τ untreated`: that is information about
> *where else the tag is registered*, not about the scope proved, and
> `big site (Sch/S)_τ, every τ` already states the scope exactly.  The other registrations are
> named in the last paragraph below.
>
> 06VE's first functor is `QCoh(𝒪_S) → Mod((Sch/S)_τ, 𝒪)`, whose target is
> `Mod` — which is the target below on the nose, `SheafOfModules` over the structure sheaf of
> `(Sch/S)_τ` — so clause (1) of 06VE needs no reading through a subcategory.  0GN7 spells the
> same functor with target `QCoh((Sch/S)_τ, 𝒪)`, and that too is the same statement: full
> faithfulness of a functor into a category is full faithfulness into any full subcategory
> containing its image, and the image does land in `QCoh` by Stacks 03DV (1),
> `AlgebraicGeometry.BigFppfOver.isQuasicoherentOnSite_baseAssociatedModule_of_isQuasicoherent`.
>
> What is **not** claimed by either tag here is the source's second functor,
> `QCoh(𝒪_S) → Mod(S_τ, 𝒪)` into the *small* site of `S` for `τ ∈ {Zariski, étale}` — a different
> construction, Definition 03DU (4).  It is claimed elsewhere, and 0GN7 quantifies over nothing
> beyond these: Definition 03DU gives a small site only at `τ ∈ {Zariski, étale}`, so this
> declaration together with
> `AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedModuleQcoh`
> (`StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealFullyFaithful.lean`)
> and `AlgebraicGeometry.SmallEtale.fullyFaithfulAssociatedModuleQcoh'`
> (`StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleLocalBijectivity.lean`) is
> every functor the lemma speaks of.  At `τ = Zariski` the *sections*-defined form of the functor
> carries the tag too, as
> `AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedSheafFunctor`.
>
> (The small étale functor is `AlgebraicGeometry.SmallEtale.associatedModule`, in
> `StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRingedSite.lean`, and its full
> faithfulness rests on `AlgebraicGeometry.SmallEtale.unitIsoOnQuasicoherent` of
> `SmallEtaleLocalBijectivity.lean`, which proves
> `AlgebraicGeometry.SmallEtale.UnitIsoOnQuasicoherent` with no hypothesis.)

```lean
public noncomputable def fullyFaithfulBaseAssociatedModuleQcoh (τ : SiteKind) :
    (baseAssociatedModuleQcoh B S hS τ).FullyFaithful
```

**`AlgebraicGeometry.AssociatedModuleNotExact.not_mono_map_two_nsmul_qcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BigSiteNotExact.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BigSiteNotExact.lean#L322). The attribute's comment: “part (6), the witness: at S = Spec(ℤ), on every big site and at every τ, the monomorphism 2 : 𝒪_S → 𝒪_S of QCoh(𝒪_S) has non-monomorphic image”.

> **Stacks 06VE (6), the witness.**  For `S = Spec(ℤ)`, every big fppf site containing it and
> every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, the monomorphism `2 : 𝒪_S → 𝒪_S` of
> `QCoh(𝒪_S)` is carried by `𝓕 ↦ 𝓕^a` to a morphism of `Mod((Sch/S)_τ, 𝒪)` that is **not** a
> monomorphism.
>
> This is the example the source gives: `2 : 𝔽₂ → 𝔽₂` is not injective and `Spec(𝔽₂)` is an object
> of `(Sch/S)_τ`.  Paired with
> `AlgebraicGeometry.AssociatedModuleNotExact.mono_two_nsmul_unitQcoh`, which says the source
> morphism *is* a monomorphism, it is the whole of clause (6).

```lean
public theorem not_mono_map_two_nsmul_qcoh :
    ¬ Mono ((associatedModuleQcoh B τ).map (2 • 𝟙 unitQcoh.{u}))
```

**`AlgebraicGeometry.AssociatedModuleNotExact.not_preservesMonomorphisms_baseAssociatedModuleQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BigSiteNotExact.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BigSiteNotExact.lean#L333). The attribute's comment: “part (6), as the failure to preserve monomorphisms, at S = Spec(ℤ) on every big site and at every τ”.

> **Stacks 06VE (6), as the failure to preserve monomorphisms.**

```lean
public theorem not_preservesMonomorphisms_baseAssociatedModuleQcoh :
    ¬ (associatedModuleQcoh B τ).PreservesMonomorphisms
```

**`AlgebraicGeometry.AssociatedModuleNotExact.not_preservesFiniteLimits_baseAssociatedModuleQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BigSiteNotExact.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BigSiteNotExact.lean#L349). The attribute's comment: “part (6): the functor QCoh(𝒪_S) → Mod((Sch/S)_τ, 𝒪) is not left exact, at S = Spec(ℤ), on every big site and at every τ; with part (4) this is the failure of exactness”.

> **Stacks 06VE (6).**  The functor `QCoh(𝒪_S) → Mod((Sch/S)_τ, 𝒪)`, `𝓕 ↦ 𝓕^a`, is **not**
> exact in general: at `S = Spec(ℤ)` it does not preserve finite limits, on every big fppf site
> and at every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.
>
> By clause (4) the functor is always right exact, so this is exactly the failure of exactness the
> source asserts.  A functor preserving finite limits preserves pullbacks, hence monomorphisms,
> which `not_preservesMonomorphisms_baseAssociatedModuleQcoh` of this namespace rules out.

```lean
public theorem not_preservesFiniteLimits_baseAssociatedModuleQcoh :
    ¬ Limits.PreservesFiniteLimits (associatedModuleQcoh B τ)
```

**`AlgebraicGeometry.AssociatedModuleSheafHomNotCommute.exists_isQuasicoherent_not_iso_sheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BigSiteSheafHomNotCommute.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BigSiteSheafHomNotCommute.lean#L395). The attribute's comment: “part (9): the sheaf Hom does NOT commute with 𝓕 ↦ 𝓕ᵃ on the big site, at S = Spec ℤ, and not even when 𝓕 is of finite presentation”.

> **Stacks 06VE (9).**  Given two quasi-coherent `𝒪_S`-modules `𝓕`, `𝓖` one does **not** have
> `(SheafHom_{𝒪_S}(𝓕, 𝓖))^a = SheafHom_𝒪(𝓕^a, 𝓖^a)` in `Mod((Sch/S)_τ, 𝒪)` in general: at
> `S = Spec(ℤ)`, on every big fppf site containing it and at every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, the two are not isomorphic, for
> `𝓕 = Coker(2 : 𝒪_S → 𝒪_S)` and `𝓖 = 𝒪_S`.
>
> This is the example the source gives, and the two halves are the two named statements of this
> file: the left-hand side is a zero object
> (`AlgebraicGeometry.AssociatedModuleSheafHomNotCommute.isZero_associatedModule_sheafHomModules`)
> and the right-hand side is not
> (`…not_isZero_internalHomSheaf`), the latter for the very reason clause (6) fails —
> `Spec(𝔽₂)` is an object of `(Sch/S)_τ`.
>
> `𝓕` is asserted to be **of finite presentation**, which is the source's "even if `𝓕` is of
> finite presentation": the failure is not repaired by the hypothesis under which clause (8) holds
> on the small sites.  It holds by construction, `𝓕` being the cokernel of a map
> `𝒪_S → 𝒪_S` (Stacks 0H96, `Stacks.SheafOfModules.isFinitePresentation_cokernel`).  See the
> implementation notes for why the conjunct is needed and not merely true.
>
> All three modules in play — `𝓕`, `𝓖` and `SheafHom_{𝒪_S}(𝓕, 𝓖)` — are asserted to be
> quasi-coherent, so both sides of the clause are values of the functor
> `QCoh(𝒪_S) → Mod((Sch/S)_τ, 𝒪)` the clause is about and not of some extension of it to all
> `𝒪_S`-modules; that functor is
> `AlgebraicGeometry.AssociatedModuleNotExact.associatedModuleQcoh`, and
> `AlgebraicGeometry.AssociatedModuleSheafHomNotCommute.associatedModuleQcoh_obj` says it agrees
> with the `associatedModule` written here on every quasi-coherent module, on the nose.
>
> The universe lift is the canonical fully faithful `Stacks.SheafOfModules.moduleULift`: the
> internal Hom of Stacks 03EM on the big site raises the module universe by construction, so the
> two sides of the clause are objects of two different categories.  See the implementation notes
> of this file; the zero/nonzero dichotomy above is universe-free and is the real content.

```lean
public theorem exists_isQuasicoherent_not_iso_sheafHom :
    ∃ F G : specInt.{u}.Modules, F.IsQuasicoherent ∧ G.IsQuasicoherent ∧
      F.IsFinitePresentation ∧ (sheafHomModules F G).IsQuasicoherent ∧
      ¬ Nonempty ((Stacks.SheafOfModules.moduleULift.{u + 1, u}
            (bigStructureSheaf B τ)).obj
            ((associatedModule B τ).obj (sheafHomModules F G)) ≅
          RingedSite.internalHomSheaf
            (BigFppfOver.baseRingedSite B specInt.{u} (contains_specInt B) τ)
            ((associatedModule B τ).obj F) ((associatedModule B τ).obj G))
```

**`AlgebraicGeometry.SmallEtale.associatedModuleTensorBifunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleAssociatedModuleTensorBifunctor.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleAssociatedModuleTensorBifunctor.lean#L99). The attribute's comment: “part (7), small site at τ = étale, for all 𝒪_S-modules; bifunctor form, whose components are the objectwise form in which the source states the clause”.

> **Stacks 06VE (7) at `τ = étale`.**  The functor `𝓕 ↦ 𝓕^a` into the `𝒪`-modules of the small
> étale site of `S` carries the tensor product of two `𝒪_S`-modules to the tensor product of their
> images:
>
> `(𝓕 ⊗_{𝒪_S} 𝓖)^a ≅ 𝓕^a ⊗_𝒪 𝓖^a`,
>
> naturally in the pair `(𝓕, 𝓖)`, with no hypothesis on `𝓕` or `𝓖`.
>
> This is Modules on Sites, Lemma 03EL — `Stacks.SheafOfModules.pullbackTensorIso` — for the
> morphism of ringed topoi underlying `ε : (S_étale, 𝒪) ⟶ (S_Zar, 𝒪_S)` of Stacks 070R and 08H7,
> conjugated on both sides by `AlgebraicGeometry.SmallEtale.pullbackModulesToZariskiIso`.  Its
> component at a pair is the objectwise form in which the source states the clause,
> `AlgebraicGeometry.SmallEtale.associatedModuleTensorIso`, by
> `AlgebraicGeometry.SmallEtale.associatedModuleTensorBifunctorIso_app`.
>
> With `AlgebraicGeometry.SmallZariski.associatedModuleTensorIsoOfComparison` at `τ = Zariski` and
> `AlgebraicGeometry.BigFppfOver.baseAssociatedModuleTensorIso` on the big sites, clause (7) is
> covered at every functor the lemma quantifies over.

```lean
def associatedModuleTensorBifunctorIso :
    Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
          S.zariskiRingedSite.toRingedTopos.O) ⋙ associatedModule B S hS ≅
      Functor.prod (associatedModule B S hS) (associatedModule B S hS) ⋙
        Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u}
          (smallEtaleRingedSite B S hS).toRingedTopos.O)
```

**`AlgebraicGeometry.SmallEtale.fullyFaithfulAssociatedModuleQcoh'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleLocalBijectivity.lean, line 660](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleLocalBijectivity.lean#L660). The attribute's comment: “part (1), small site at τ = étale”.

> **The small étale half of Stacks 0GN7 and of Stacks 06VE (1), with no hypothesis at all**:
> the functor `𝓕 ↦ 𝓕^a` of Definition 03DU (4) at `τ = étale`, from the quasi-coherent
> `𝒪_S`-modules to the `𝒪`-modules on `S_étale`, is fully faithful.

```lean
public noncomputable def fullyFaithfulAssociatedModuleQcoh' :
    (associatedModuleQcoh B S hS).FullyFaithful
```

**`AlgebraicGeometry.SmallEtale.essImage_X₂_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRestrictionRightExact.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRestrictionRightExact.lean#L279). The attribute's comment: “part (10), small site at τ = étale”.

> **Stacks 06VE (10) at `τ = étale`.**  Given a short exact sequence
> `0 → 𝓕₁^a → 𝓔 → 𝓕₂^a → 0` of `𝒪`-modules on the small étale site of `S` — the outer terms being
> given as quasi-coherent, which at `τ = étale` is the same as being in the essential image, by
> Stacks 03DX (2) — the middle term `𝓔` is in the essential image of
> `QCoh(𝒪_S) ⥤ Mod(S_étale, 𝒪)`, `𝓕 ↦ 𝓕^a`, namely of `𝓔|_{S_Zar}`.
>
> The source's three steps are
> `StacksFrontier.AlgebraicGeometry.Descent.AssociatedModule.SmallEtaleExtensionReduction`; the one
> they carried, right exactness of `ε_*`, is `epi_restrictModule_map` above.

```lean
public theorem essImage_X₂_of_shortExact (hC : C.ShortExact)
    (h₁ : C.X₁.IsQuasicoherentOnSite) (h₃ : C.X₃.IsQuasicoherentOnSite) :
    (associatedModuleQcoh B S hS).essImage C.X₂
```

**`AlgebraicGeometry.SmallEtale.associatedModuleInternalHomSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteSheafHomComparison.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteSheafHomComparison.lean#L182). The attribute's comment: “part (8), small site at τ = étale, for the pullback-defined functor 𝓕 ↦ 𝓕ᵃ of Remark 03FH and Tag 03EM's internal Hom on S_étale”.

> **Stacks 06VE (8) at `τ = étale`.**  For `𝒪_S`-modules `𝓕`, `𝓖` on a scheme `S` with `𝓖`
> quasi-coherent and `𝓕` of finite presentation — Stacks 03DL (7) on the site of opens of `S` —
>
> `(SheafHom_{𝒪_S}(𝓕, 𝓖))^a ≅ SheafHom_𝒪(𝓕^a, 𝓖^a)` in `Mod(S_étale, 𝒪)`,
>
> where `𝓕 ↦ 𝓕^a` is the functor of Definition 03DU (4) at `τ = étale` in its pullback description
> of Remark 03FH, `AlgebraicGeometry.SmallEtale.associatedModule`, and the internal Hom on the
> right is Tag 03EM's on the small étale site.
>
> The proof is the one the module docstring describes: the mate of clause (7),
> `AlgebraicGeometry.SmallEtale.restrictModuleInternalHomIso`, computes the Zariski restriction of
> the right-hand side as `SheafHom_{𝒪_S}(𝓕, ε_* 𝓖^a)`; the unit of the associated-module
> adjunction is an isomorphism at the quasi-coherent `𝓖`, Stacks 0GN7, so that restriction is
> `SheafHom_{𝒪_S}(𝓕, 𝓖)`; and the counit is an isomorphism at the right-hand side because that
> internal Hom is quasi-coherent, which is clause (6) of Stacks 0GNB and is where the finite
> presentation of `𝓕` is spent, through Stacks 03DO for the clause 03DL (7),
> `AlgebraicGeometry.SmallEtale.isFinitePresentationOnSite_associatedModule`.
>
> Quasi-coherence of `𝓕` is not needed.

```lean
def associatedModuleInternalHomSheafIso (𝓕 𝓖 : S.Modules)
    (h𝓖 : SheafOfModules.IsQuasicoherent 𝓖)
    (h𝓕 : SheafOfModules.IsFinitePresentationOnSite 𝓕) :
    (associatedModule B S hS).obj
        (Stacks.AlgebraicGeometry.InternalHomModules.sheafHomModules 𝓕 𝓖) ≅
      internalHomSheaf B S hS ((associatedModule B S hS).obj 𝓕)
        ((associatedModule B S hS).obj 𝓖)
```

**`AlgebraicGeometry.SmallZariski.associatedModuleInternalHomSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteSheafHomComparisonZariski.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallSiteSheafHomComparisonZariski.lean#L155). The attribute's comment: “part (8), small site at τ = Zariski, for the pullback-defined functor 𝓕 ↦ 𝓕ᵃ of Remark 03FH and Tag 03EM's internal Hom on S_Zar, for all 𝒪_S-modules”.

> **Stacks 06VE (8) at `τ = Zariski`.**  For `𝒪_S`-modules `𝓕` and `𝓖` on a scheme `S`,
>
> `(SheafHom_{𝒪_S}(𝓕, 𝓖))^a ≅ SheafHom_𝒪(𝓕^a, 𝓖^a)` in `Mod(S_Zar, 𝒪)`,
>
> where `𝓕 ↦ 𝓕^a` is the functor of Definition 03DU (4) at `τ = Zariski` in its pullback
> description of Remark 03FH, `AlgebraicGeometry.SmallZariski.associatedModule`, and the internal
> Hom on the right is Tag 03EM's on the small Zariski site of schemes over `S`.
>
> The proof is the source's: the mate of clause (7),
> `AlgebraicGeometry.SmallZariski.restrictModuleInternalHomIso`, computes the restriction of the
> right-hand side as `SheafHom_{𝒪_S}(𝓕, ε_* 𝓖^a)`; the unit of the associated-module adjunction
> identifies `ε_* 𝓖^a` with `𝓖`, so that restriction is the left-hand side's source; and the
> counit identifies the right-hand side with the associated module of its own restriction.  Both
> unit and counit are isomorphisms because `𝓕 ↦ 𝓕^a` is an equivalence at `τ = Zariski`,
> Stacks 03FG — which is the content of the source's one-sentence argument, and the only thing
> clause (8) needs at this topology.
>
> Neither quasi-coherence nor finite presentation of `𝓕` is assumed: they are what the clause
> needs at `τ = étale`, where they buy the two isomorphisms that come for free here.

```lean
def associatedModuleInternalHomSheafIso (𝓕 𝓖 : S.Modules) :
    (associatedModule B S hS).obj
        (Stacks.AlgebraicGeometry.InternalHomModules.sheafHomModules 𝓕 𝓖) ≅
      RingedSite.internalHomSheafSmall.{u} (smallZariskiRingedSite B S hS)
        ((associatedModule B S hS).obj 𝓕) ((associatedModule B S hS).obj 𝓖)
```

**`AlgebraicGeometry.SmallZariski.preservesColimitsOfShape_discrete_associatedModuleQcohOfComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealClosureProperties.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealClosureProperties.lean#L188). The attribute's comment: “part (2), small site at τ = Zariski”.

> **Stacks 06VE (2) for the small site at `τ = Zariski`.**  The functor
> `QCoh(𝒪_S) ⥤ Mod(S_Zar, 𝒪)`, `𝓕 ↦ 𝓕^a` of Definition 03DU (4), commutes with direct sums: a
> direct sum is a colimit over a discrete index category, so this is the discrete case of
> clause (3).
>
> Definition 03DU gives a small site only for `τ ∈ {Zariski, étale}`, so with
> `AlgebraicGeometry.SmallEtale.preservesColimitsOfShape_discrete_associatedModuleQcoh` (the small
> site at `τ = étale`) and
> `AlgebraicGeometry.BigFppfOver.preservesColimitsOfShape_discrete_baseAssociatedModuleQcoh` (the
> big site, every `τ`) this completes the covering set of the clause.

```lean
public theorem preservesColimitsOfShape_discrete_associatedModuleQcohOfComparison (I : Type u) :
    PreservesColimitsOfShape (Discrete I)
      (AlgebraicGeometry.SmallZariski.associatedModuleQcoh B S hS)
```

**`AlgebraicGeometry.SmallZariski.preservesColimitsOfSize_associatedModuleQcohOfComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealClosureProperties.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealClosureProperties.lean#L199). The attribute's comment: “part (3), small site at τ = Zariski”.

> **Stacks 06VE (3) for the small site at `τ = Zariski`.**  The functor
> `QCoh(𝒪_S) ⥤ Mod(S_Zar, 𝒪)`, `𝓕 ↦ 𝓕^a` of Definition 03DU (4), commutes with all colimits
> indexed at the size of the scheme.
>
> Scope as on `preservesColimitsOfShape_discrete_associatedModuleQcohOfComparison`.

```lean
public theorem preservesColimitsOfSize_associatedModuleQcohOfComparison :
    PreservesColimitsOfSize.{u, u}
      (AlgebraicGeometry.SmallZariski.associatedModuleQcoh B S hS)
```

**`AlgebraicGeometry.SmallZariski.preservesFiniteColimits_associatedModuleQcohOfComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealClosureProperties.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealClosureProperties.lean#L212). The attribute's comment: “part (4), small site at τ = Zariski”.

> **Stacks 06VE (4) for the small site at `τ = Zariski`.**  The functor
> `QCoh(𝒪_S) ⥤ Mod(S_Zar, 𝒪)`, `𝓕 ↦ 𝓕^a` of Definition 03DU (4), is right exact, i.e. commutes
> with finite colimits.
>
> As on the big site this is not read off clause (3) but assembled from the two factors, the
> inclusion of the quasi-coherent modules being right exact because they are a weak Serre
> subcategory.

```lean
public theorem preservesFiniteColimits_associatedModuleQcohOfComparison :
    PreservesFiniteColimits
      (AlgebraicGeometry.SmallZariski.associatedModuleQcoh B S hS)
```

**`AlgebraicGeometry.SmallZariski.essImage_X₂_of_shortExactOfComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealClosureProperties.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealClosureProperties.lean#L290). The attribute's comment: “part (10), small site at τ = Zariski”.

> **Stacks 06VE (10) for the small site at `τ = Zariski`.**  Given a short exact sequence
> `0 → 𝓕₁^a → 𝓔 → 𝓕₂^a → 0` of `𝒪`-modules on the small Zariski site of `S`, with `𝓕₁` and `𝓕₂`
> quasi-coherent on `S`, the module `𝓔` is itself in the essential image of `𝓕 ↦ 𝓕^a`.
>
> Restriction along the morphism of ringed sites of Remark 03FH is an equivalence at `τ = Zariski`
> (Stacks 03FG), hence exact, so it carries the sequence to a short exact sequence of
> `𝒪_S`-modules; by `AlgebraicGeometry.SmallZariski.essImage_associatedModuleQcohOfComparison_iff`
> its outer terms are quasi-coherent, so its middle term is too, quasi-coherent modules on a scheme
> being closed under extensions (Schemes, Section 01LA).  The same lemma turns that back into
> membership of the essential image.
>
> The clause at `τ = étale` and on the big sites is a different statement and is not implied by
> this one; see the implementation notes of this module.

```lean
public theorem essImage_X₂_of_shortExactOfComparison
    {C : ShortComplex (SheafOfModules.{u} (structureSheaf B S hS))} (hC : C.ShortExact)
    (h₁ : (associatedModuleQcoh B S hS).essImage C.X₁)
    (h₃ : (associatedModuleQcoh B S hS).essImage C.X₃) :
    (associatedModuleQcoh B S hS).essImage C.X₂
```

**`AlgebraicGeometry.SmallZariski.isQuasicoherentOnSite_X₂_of_shortExactOfComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealClosureProperties.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealClosureProperties.lean#L331). The attribute's comment: “part (10), small site at τ = Zariski, as quasi-coherence on the site”.

> **Stacks 06VE (10) for the small site at `τ = Zariski`, in the form the source states it**:
> given a short exact sequence `0 → 𝓕₁ → 𝓕₂ → 𝓕₃ → 0` of `𝒪`-modules on the small Zariski site of
> `S` whose outer terms are quasi-coherent, the middle term is quasi-coherent.
>
> The source states clause (10) as "`𝓔` is quasi-coherent, i.e. `𝓔` is in the essential image of
> the functor"; this is the first reading and
> `AlgebraicGeometry.SmallZariski.essImage_X₂_of_shortExactOfComparison` is the second.  The two
> agree by Stacks 03DX (2) at `τ = Zariski`,
> `essImage_associatedModuleQcohOfComparison_iff_isQuasicoherentOnSite`. It is also the third case
> of Stacks 0GNB (4) and 0GNC (4) at this site.

```lean
public theorem isQuasicoherentOnSite_X₂_of_shortExactOfComparison
    {C : ShortComplex (SheafOfModules.{u} (structureSheaf B S hS))} (hC : C.ShortExact)
    (h₁ : C.X₁.IsQuasicoherentOnSite) (h₃ : C.X₃.IsQuasicoherentOnSite) :
    C.X₂.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedModuleQcoh`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealFullyFaithful.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiRealFullyFaithful.lean#L275). The attribute's comment: “part (1), small site at τ = Zariski”.

> **Stacks 0GN7 for the small site at `τ = Zariski`, and clause (1) of Stacks 06VE for it.**
> The functor `𝓕 ↦ 𝓕^a` of Definition 03DU (4) at `τ = Zariski` — the pullback of sheaves of
> modules along the morphism of ringed sites `(S_Zar, 𝒪) → (S_Zar, 𝒪_S)` of Remark 03FH, with the
> coefficient sheaf `T/S ↦ Γ(T, 𝒪_T)` of Definition 03DU (2) — from the quasi-coherent
> `𝒪_S`-modules to the `𝒪`-modules on the small Zariski site, is fully faithful.
>
> Together with `AlgebraicGeometry.BigFppfOver.fullyFaithfulBaseAssociatedModuleQcoh` (the big
> site, every `τ`) and `AlgebraicGeometry.SmallEtale.fullyFaithfulAssociatedModuleQcoh'` (the
> small site at `τ = étale`) this completes the covering set of 0GN7: Definition 03DU gives a small
> site only for `τ ∈ {Zariski, étale}`, so those three statements are every functor the lemma
> quantifies over.
>
> 0GN7 spells the target `QCoh(S_Zar, 𝒪)` where this is `Mod(S_Zar, 𝒪)`, and that is the same
> statement for the same reason as at `τ = étale` and on the big site: full faithfulness of a
> functor into a category is full faithfulness into any full subcategory containing its image, and
> the image lands in `QCoh(S_Zar, 𝒪)` by Stacks 03DV (2),
> `AlgebraicGeometry.SmallZariski.isQuasicoherentOnSite_associatedModule_of_isQuasicoherent`;
> the corestriction itself is
> `AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedModuleQcohOnSite` below.  06VE's second
> functor has target `Mod(S_τ, 𝒪)`, which is the target here with nothing to read through.

```lean
public noncomputable def fullyFaithfulAssociatedModuleQcoh :
    (associatedModuleQcoh B S hS).FullyFaithful
```

**`AlgebraicGeometry.SmallZariski.preservesColimitsOfShape_discrete_associatedSheafFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsClosure.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsClosure.lean#L236). The attribute's comment: “part (2), small site at τ = Zariski, for the SECTIONS-defined functor 𝓕 ↦ 𝓕ᵃ of Definition 03DU (4) — SmallZariski.associatedSheafFunctor. The same clause for the pullback-defined functor of Remark 03FH is preservesColimitsOfShape_discrete_associatedModuleQcohOfComparison; the two functors are identified by associatedModuleQcohIsoAssociatedSheafFunctor”.

> **[Stacks, Tag 06VE] (2) for the small site at `τ = Zariski`, for the functor the source
> defines.**  The sections-defined `𝓕 ↦ 𝓕ᵃ` of [Stacks, Tag 03DU] (4), as a functor
> `QCoh(𝒪_S) ⥤ Mod(S_Zar, 𝒪)`, commutes with direct sums.
>
> `AlgebraicGeometry.SmallZariski.preservesColimitsOfShape_discrete_associatedModuleQcohOfComparison`
> is the same clause for the pullback-defined functor of [Stacks, Remark 03FH]; this is it read
> through `AlgebraicGeometry.SmallZariski.associatedModuleQcohIsoAssociatedSheafFunctor`.  06VE's
> second functor has target `Mod(S_τ, 𝒪)`, which is the target here on the nose.

```lean
public theorem preservesColimitsOfShape_discrete_associatedSheafFunctor (I : Type u) :
    PreservesColimitsOfShape (Discrete I) (associatedSheafFunctor B S hS)
```

**`AlgebraicGeometry.SmallZariski.preservesColimitsOfSize_associatedSheafFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsClosure.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsClosure.lean#L251). The attribute's comment: “part (3), small site at τ = Zariski, for the SECTIONS-defined functor 𝓕 ↦ 𝓕ᵃ of Definition 03DU (4) — SmallZariski.associatedSheafFunctor. The same clause for the pullback-defined functor of Remark 03FH is preservesColimitsOfSize_associatedModuleQcohOfComparison; the two functors are identified by associatedModuleQcohIsoAssociatedSheafFunctor”.

> **[Stacks, Tag 06VE] (3) for the small site at `τ = Zariski`, for the functor the source
> defines.**  The sections-defined `𝓕 ↦ 𝓕ᵃ` commutes with all colimits indexed at the size of the
> scheme.
>
> Scope and route as on
> `AlgebraicGeometry.SmallZariski.preservesColimitsOfShape_discrete_associatedSheafFunctor`.

```lean
public theorem preservesColimitsOfSize_associatedSheafFunctor :
    PreservesColimitsOfSize.{u, u} (associatedSheafFunctor B S hS)
```

**`AlgebraicGeometry.SmallZariski.preservesFiniteColimits_associatedSheafFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsClosure.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsClosure.lean#L270). The attribute's comment: “part (4), small site at τ = Zariski, for the SECTIONS-defined functor 𝓕 ↦ 𝓕ᵃ of Definition 03DU (4) — SmallZariski.associatedSheafFunctor. The same clause for the pullback-defined functor of Remark 03FH is preservesFiniteColimits_associatedModuleQcohOfComparison; the two functors are identified by associatedModuleQcohIsoAssociatedSheafFunctor”.

> **[Stacks, Tag 06VE] (4) for the small site at `τ = Zariski`, for the functor the source
> defines.**  The sections-defined `𝓕 ↦ 𝓕ᵃ` is right exact, i.e. commutes with finite colimits.
>
> Scope and route as on
> `AlgebraicGeometry.SmallZariski.preservesColimitsOfShape_discrete_associatedSheafFunctor`; see the
> implementation notes of this module for why this is not read off clause (3).

```lean
public theorem preservesFiniteColimits_associatedSheafFunctor :
    PreservesFiniteColimits (associatedSheafFunctor B S hS)
```

**`AlgebraicGeometry.SmallZariski.essImage_X₂_of_shortExact_associatedSheafFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsClosure.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsClosure.lean#L310). The attribute's comment: “part (10), small site at τ = Zariski, for the SECTIONS-defined functor 𝓕 ↦ 𝓕ᵃ of Definition 03DU (4) — SmallZariski.associatedSheafFunctor. The same clause for the pullback-defined functor of Remark 03FH is essImage_X₂_of_shortExactOfComparison; the two functors have the same essential image by essImage_associatedSheafFunctor_iff”.

> **[Stacks, Tag 06VE] (10) for the small site at `τ = Zariski`, for the functor the source
> defines.**  Given a short exact sequence `0 → 𝓕₁ᵃ → 𝓔 → 𝓕₂ᵃ → 0` of `𝒪`-modules on the small
> Zariski site of `S`, with `𝓕₁` and `𝓕₂` quasi-coherent on `S` and `𝓕 ↦ 𝓕ᵃ` the sections-defined
> functor of [Stacks, Tag 03DU] (4), the module `𝓔` is itself in the essential image of that
> functor.
>
> `AlgebraicGeometry.SmallZariski.essImage_X₂_of_shortExactOfComparison` is the same clause for the
> pullback-defined functor of [Stacks, Remark 03FH]; the two functors have the same essential image
> by `AlgebraicGeometry.SmallZariski.essImage_associatedSheafFunctor_iff`, and all three hypotheses
> and the conclusion read across it.
>
> The clause in the form the source states it — "`𝓔` is quasi-coherent" — is
> `AlgebraicGeometry.SmallZariski.isQuasicoherentOnSite_X₂_of_shortExactOfComparison`, whose
> statement names no functor and so needs no sections-defined counterpart.

```lean
public theorem essImage_X₂_of_shortExact_associatedSheafFunctor
    {C : ShortComplex (SheafOfModules.{u} (structureSheaf B S hS))} (hC : C.ShortExact)
    (h₁ : (associatedSheafFunctor B S hS).essImage C.X₁)
    (h₃ : (associatedSheafFunctor B S hS).essImage C.X₃) :
    (associatedSheafFunctor B S hS).essImage C.X₂
```

**`AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedSheafFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsIso.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallZariskiSectionsIso.lean#L572). The attribute's comment: “part (1), small site at τ = Zariski, for the SECTIONS-defined functor 𝓕 ↦ 𝓕ᵃ of Definition 03DU (4) — SmallZariski.associatedSheafFunctor, whose target Mod(S_Zar, 𝒪) is the target 06VE spells for its second functor. The same clause for the pullback-defined functor of Remark 03FH is fullyFaithfulAssociatedModuleQcoh”.

> **[Stacks, Tag 0GN7] for the small site at `τ = Zariski`, for the functor the source
> defines**: the assignment `𝓕 ↦ 𝓕ᵃ` of [Stacks, Tag 03DU] (4) — the sheaf of `𝒪`-modules on
> `S_Zar` whose sections over `f : T → S` are `Γ(T, f^*𝓕)`,
> `AlgebraicGeometry.SmallZariski.associatedSheafFunctor` — is fully faithful on the quasi-coherent
> `𝒪_S`-modules.
>
> `AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedModuleQcoh` is the same statement for the
> *pullback*-defined functor of [Stacks, Remark 03FH]; this is it read through
> `AlgebraicGeometry.SmallZariski.associatedModuleQcohIsoAssociatedSheafFunctor`, which identifies
> the two.  Both are 0GN7 at `τ = Zariski`, and the source's own statement is about the sections
> description, so the clause is only about the object the source names once this form exists.
>
> 0GN7 spells the target `QCoh(S_Zar, 𝒪)` where this is `Mod(S_Zar, 𝒪)`; that is the same
> statement for the reason recorded on
> `AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedModuleQcoh`, full faithfulness into a
> category being full faithfulness into any full subcategory containing the image, and the image
> landing in `QCoh(S_Zar, 𝒪)` by [Stacks, Tag 03DV] (2).
>
> **This is also clause (1) of [Stacks, Tag 06VE] at `τ = Zariski` for the sections-defined
> functor**, that clause being the same assertion of full faithfulness; its second functor has
> target `Mod(S_τ, 𝒪)`, which is the target here with nothing to read through.  The two attributes
> sit together for the same reason they do on
> `AlgebraicGeometry.SmallZariski.fullyFaithfulAssociatedModuleQcoh` for the pullback-defined
> functor.

```lean
public noncomputable def fullyFaithfulAssociatedSheafFunctor :
    (associatedSheafFunctor B S hS).FullyFaithful
```

**`AlgebraicGeometry.BigFppfOver.preservesColimitsOfShape_discrete_associatedModuleQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/AssociatedModuleColimits.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/AssociatedModuleColimits.lean#L252). The attribute's comment: “direct_sums, big site at τ = fppf only”.

> **Stacks 06VE (2).**  The functor `𝓕 ↦ 𝓕^a` commutes with direct sums: a direct sum is a
> colimit over a discrete index category, so this is the discrete case of clause (3).
>
> Stated for the **big fppf** site, which is what this declaration's functor is.  The base's
> clause string "fppf only" is kept byte-identical (a base registration line is never rewritten);
> read it as the scope of *this* declaration, not of the library, since the reason the previous
> version gave for the restriction — that the clause's inputs were proved at fppf only — was
> false: `AlgebraicGeometry.BigFppfOver.preservesColimitsOfSize_baseAssociatedModule`
> (`StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseRingedSite.lean:317`) is an
> instance at every `τ : SiteKind`.  **The clause at every `τ` is
> `AlgebraicGeometry.BigFppfOver.preservesColimitsOfShape_discrete_baseAssociatedModuleQcoh`**, in
> `StacksFrontier.AlgebraicGeometry.Stacks.Quasicoherent.Descent.BaseAssociatedModuleColimits`, of
> which this is the `τ = .fppf` case.
>
> The source's second functor, `QCoh(𝒪_S) ⥤ Mod(S_τ, 𝒪)` into a **small** site of `S`, is a
> different construction, and **this clause holds for it too**, at `τ = étale`:
> `AlgebraicGeometry.SmallEtale.preservesColimitsOfShape_discrete_associatedModuleQcoh`, over
> `AlgebraicGeometry.SmallEtale.associatedModule`
> (`StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRingedSite.lean:417`).  An
> earlier note here said "small site untreated"; that was true when written and is now false.

```lean
public theorem preservesColimitsOfShape_discrete_associatedModuleQcoh (I : Type u) :
    PreservesColimitsOfShape (Discrete I) (associatedModuleQcoh B S hS)
```

**`AlgebraicGeometry.BigFppfOver.preservesColimitsOfSize_associatedModuleQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/AssociatedModuleColimits.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/AssociatedModuleColimits.lean#L269). The attribute's comment: “colimits, big site at τ = fppf only”.

> **Stacks 06VE (3).**  The functor `𝓕 ↦ 𝓕^a` commutes with all colimits indexed at the size
> of the site.
>
> Stated for the big fppf site, as on
> `AlgebraicGeometry.BigFppfOver.preservesColimitsOfShape_discrete_associatedModuleQcoh`, and for
> the same reason: that is this declaration's functor.  The clause at every `τ` is
> `AlgebraicGeometry.BigFppfOver.preservesColimitsOfSize_baseAssociatedModuleQcoh`, of which this
> is the `τ = .fppf` case; the clause's inputs are not specific to fppf.
>
> The small-site functor of the source statement is treated at `τ = étale`, where this clause is
> `AlgebraicGeometry.SmallEtale.preservesColimitsOfSize_associatedModuleQcoh`.  The clause string
> "fppf only" is kept byte-identical and reads as the scope of this declaration.

```lean
public theorem preservesColimitsOfSize_associatedModuleQcoh :
    PreservesColimitsOfSize.{u, u} (associatedModuleQcoh B S hS)
```

**`AlgebraicGeometry.BigFppfOver.preservesColimitsOfShape_discrete_baseAssociatedModuleQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/BaseAssociatedModuleColimits.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/BaseAssociatedModuleColimits.lean#L125). The attribute's comment: “part (2), big site (Sch/S)_τ, every τ”.

> **Stacks 06VE (2), for every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.**  The functor
> `QCoh(𝒪_S) ⥤ Mod((Sch/S)_τ, 𝒪)`, `𝓕 ↦ 𝓕^a`, commutes with direct sums: a direct sum is a
> colimit over a discrete index category, so this is the discrete case of clause (3).
>
> The earlier `AlgebraicGeometry.BigFppfOver.preservesColimitsOfShape_discrete_associatedModuleQcoh`
> carries the clause string "big site at τ = fppf only", on the ground that the clause's inputs
> were proved at fppf only.  They are not: the adjunction, and with it cocontinuity of
> `𝓕 ↦ 𝓕^a`, exists at every `τ` as
> `AlgebraicGeometry.BigFppfOver.preservesColimitsOfSize_baseAssociatedModule`, and the other
> input is about `QCoh(𝒪_S)` alone.  Hence this statement, which drops the restriction.

```lean
public theorem preservesColimitsOfShape_discrete_baseAssociatedModuleQcoh (I : Type u) :
    PreservesColimitsOfShape (Discrete I) (baseAssociatedModuleQcoh B S hS τ)
```

**`AlgebraicGeometry.BigFppfOver.preservesColimitsOfSize_baseAssociatedModuleQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/BaseAssociatedModuleColimits.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/BaseAssociatedModuleColimits.lean#L136). The attribute's comment: “part (3), big site (Sch/S)_τ, every τ”.

> **Stacks 06VE (3), for every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.**  The functor
> `QCoh(𝒪_S) ⥤ Mod((Sch/S)_τ, 𝒪)`, `𝓕 ↦ 𝓕^a`, commutes with all colimits indexed at the size of
> the site.
>
> Scope as on
> `AlgebraicGeometry.BigFppfOver.preservesColimitsOfShape_discrete_baseAssociatedModuleQcoh`.

```lean
public theorem preservesColimitsOfSize_baseAssociatedModuleQcoh :
    PreservesColimitsOfSize.{u, u} (baseAssociatedModuleQcoh B S hS τ)
```

**`AlgebraicGeometry.BigFppfOver.preservesFiniteColimits_baseAssociatedModuleQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/BaseAssociatedModuleColimits.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/BaseAssociatedModuleColimits.lean#L150). The attribute's comment: “part (4), big site (Sch/S)_τ, every τ”.

> **Stacks 06VE (4), for every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.**  The functor
> `QCoh(𝒪_S) ⥤ Mod((Sch/S)_τ, 𝒪)`, `𝓕 ↦ 𝓕^a`, is right exact, i.e. commutes with finite colimits.
>
> The source deduces this from clause (3); here it is the composite of the two factors' finite
> colimit preservation, because `CategoryTheory.Limits.PreservesFiniteColimits` quantifies over
> finite categories in `Type 0` while clause (3) above is stated at the universe of the site, and
> neither statement contains the other.

```lean
public theorem preservesFiniteColimits_baseAssociatedModuleQcoh :
    PreservesFiniteColimits (baseAssociatedModuleQcoh B S hS τ)
```

**`AlgebraicGeometry.SmallEtale.preservesColimitsOfShape_discrete_associatedModuleQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallEtaleAssociatedModuleColimits.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallEtaleAssociatedModuleColimits.lean#L186). The attribute's comment: “direct_sums, small site at τ = étale”.

> **Stacks 06VE (2) for the small site at `τ = étale`.**  The functor
> `QCoh(𝒪_S) ⥤ Mod(S_étale, 𝒪)`, `𝓕 ↦ 𝓕^a`, commutes with direct sums: a direct sum is a colimit
> over a discrete index category, so this is the discrete case of clause (3).
>
> The clause string records exactly the scope proved: the second functor of 06VE,
> on the small site, at `τ = étale`.  The functor is the one of Definition 03DU (4), which is
> defined for `τ ∈ {Zariski, étale}`; the Zariski half of this clause is a separate statement about
> `AlgebraicGeometry.SmallZariski.associatedModule`, which exists — see the implementation notes
> above.  The big-site half of the same clause is
> `AlgebraicGeometry.BigFppfOver.preservesColimitsOfShape_discrete_associatedModuleQcoh`.

```lean
public theorem preservesColimitsOfShape_discrete_associatedModuleQcoh (I : Type u) :
    PreservesColimitsOfShape (Discrete I) (associatedModuleQcoh B S hS)
```

**`AlgebraicGeometry.SmallEtale.preservesColimitsOfSize_associatedModuleQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallEtaleAssociatedModuleColimits.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallEtaleAssociatedModuleColimits.lean#L199). The attribute's comment: “colimits, small site at τ = étale”.

> **Stacks 06VE (3) for the small site at `τ = étale`.**  The functor
> `QCoh(𝒪_S) ⥤ Mod(S_étale, 𝒪)`, `𝓕 ↦ 𝓕^a`, commutes with all colimits indexed at the size of the
> scheme.
>
> Scope as on
> `AlgebraicGeometry.SmallEtale.preservesColimitsOfShape_discrete_associatedModuleQcoh`; the
> big-site half is
> `AlgebraicGeometry.BigFppfOver.preservesColimitsOfSize_associatedModuleQcoh`.

```lean
public theorem preservesColimitsOfSize_associatedModuleQcoh :
    PreservesColimitsOfSize.{u, u} (associatedModuleQcoh B S hS)
```

**`AlgebraicGeometry.SmallEtale.preservesFiniteColimits_associatedModuleQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallEtaleAssociatedModuleExact.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallEtaleAssociatedModuleExact.lean#L78). The attribute's comment: “part (4), small site at τ = étale”.

> **Stacks 06VE (4) for the second functor of the lemma.**  The functor
> `QCoh(𝒪_S) ⥤ Mod(S_étale, 𝒪)`, `𝓕 ↦ 𝓕^a`, is right exact: the inclusion of the quasi-coherent
> modules is right exact, quasi-coherence on a scheme being a weak Serre class, and `𝓕 ↦ 𝓕^a` is
> right exact because it is a left adjoint.

```lean
public theorem preservesFiniteColimits_associatedModuleQcoh :
    PreservesFiniteColimits (AlgebraicGeometry.SmallEtale.associatedModuleQcoh B S hS)
```

**`AlgebraicGeometry.SmallEtale.preservesFiniteLimits_associatedModuleQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallEtaleAssociatedModuleExact.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallEtaleAssociatedModuleExact.lean#L95). The attribute's comment: “part (5), left exactness half”.

> **The half of Stacks 06VE (5) that is special to the small étale site.**  The functor
> `QCoh(𝒪_S) ⥤ Mod(S_étale, 𝒪)`, `𝓕 ↦ 𝓕^a`, is left exact.
>
> The inclusion of the quasi-coherent modules is left exact because quasi-coherence on a scheme is
> a weak Serre class, and `𝓕 ↦ 𝓕^a` is left exact because `ε : (S_étale, 𝒪) ⟶ (S_Zar, 𝒪_S)` is
> flat — an étale morphism is flat, Morphisms, Lemma 02GS, which is Stacks 0GNA for `ε` and gives
> the exactness assertion of Stacks 08H8.

```lean
public theorem preservesFiniteLimits_associatedModuleQcoh :
    PreservesFiniteLimits (associatedModuleQcoh B S hS)
```

**`AlgebraicGeometry.SmallEtale.shortExact_map_associatedModuleQcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallEtaleAssociatedModuleExact.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallEtaleAssociatedModuleExact.lean#L106). The attribute's comment: “part (5), as preservation of short exact sequences”.

> **Stacks 06VE (5).**  The functor `QCoh(𝒪_S) ⥤ Mod(S_étale, 𝒪)`, `𝓕 ↦ 𝓕^a`, is exact: it
> carries a short exact sequence of quasi-coherent `𝒪_S`-modules to a short exact sequence of
> `𝒪`-modules on the small étale site.

```lean
public theorem shortExact_map_associatedModuleQcoh
    {T : ShortComplex (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory}
    (hT : T.ShortExact) : (T.map (associatedModuleQcoh B S hS)).ShortExact
```

**`AlgebraicGeometry.SmallZariski.associatedModuleTensorIsoOfComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallZariskiAssociatedModuleTensor.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallZariskiAssociatedModuleTensor.lean#L148). The attribute's comment: “part (7), small site at τ = Zariski, for the PULLBACK-defined functor 𝓕 ↦ 𝓕ᵃ of Remark 03FH, for all 𝒪_S-modules; bifunctor form”.

> **Stacks 06VE (7) at `τ = Zariski`.**  The functor `𝓕 ↦ 𝓕^a` into the `𝒪`-modules of the
> small Zariski site of `S` carries the tensor product of two `𝒪_S`-modules to the tensor product
> of their images:
>
> `(𝓕 ⊗_{𝒪_S} 𝓖)^a ≅ 𝓕^a ⊗_𝒪 𝓖^a`,
>
> naturally in the pair `(𝓕, 𝓖)`.
>
> This is Modules on Sites, Lemma 03EL — `Stacks.SheafOfModules.pullbackTensorIso` — for the
> morphism of ringed topoi underlying `id_{small, Zar, Zar}` of Remark 03FH, conjugated on both
> sides by `AlgebraicGeometry.SmallZariski.pullbackModulesIsoAssociatedModule`.
>
> The functor is the pullback description of Stacks 03DU (4); the clause for the sections
> description, which is the one 03DU (4) gives, is
> `AlgebraicGeometry.SmallZariski.associatedModuleOfSectionsTensorObjIso`.  With
> `AlgebraicGeometry.SmallEtale.associatedModuleTensorBifunctorIso` (small site at `τ = étale`) and
> `AlgebraicGeometry.BigFppfOver.baseAssociatedModuleTensorIso` (big site, every `τ`) this
> completes clause (7) at every functor the lemma quantifies over.

```lean
public def associatedModuleTensorIsoOfComparison :
    Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} S.sheaf) ⋙
        associatedModule B S hS ≅
      Functor.prod (associatedModule B S hS) (associatedModule B S hS) ⋙
        Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u}
          (smallZariskiRingedSite B S hS).O)
```

**`AlgebraicGeometry.SmallZariski.associatedModuleTensorObjIsoOfComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallZariskiAssociatedModuleTensor.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallZariskiAssociatedModuleTensor.lean#L164). The attribute's comment: “part (7), small site at τ = Zariski, for the PULLBACK-defined functor 𝓕 ↦ 𝓕ᵃ of Remark 03FH, for all 𝒪_S-modules; objectwise form”.

> **Stacks 06VE (7) at `τ = Zariski`, objectwise** — the form in which the source states it:
> `(𝓕 ⊗_{𝒪_S} 𝓖)^a = 𝓕^a ⊗_𝒪 𝓖^a`, for the pullback description of `𝓕 ↦ 𝓕^a`.

```lean
public def associatedModuleTensorObjIsoOfComparison (F G : S.Modules) :
    (associatedModule B S hS).obj
        ((Functor.uncurry.obj
            (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} S.sheaf)).obj (F, G)) ≅
      (Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u}
          (smallZariskiRingedSite B S hS).O)).obj
        ((associatedModule B S hS).obj F, (associatedModule B S hS).obj G)
```

**`AlgebraicGeometry.SmallZariski.associatedModuleOfSectionsTensorObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallZariskiAssociatedModuleTensor.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/SmallZariskiAssociatedModuleTensor.lean#L186). The attribute's comment: “part (7), small site at τ = Zariski, for the SECTIONS-defined functor 𝓕 ↦ 𝓕ᵃ of Definition 03DU (4), for quasi-coherent 𝒪_S-modules”.

> **Stacks 06VE (7) at `τ = Zariski`, for the sections-defined `𝓕^a` of Stacks 03DU (4).**
> For quasi-coherent `𝒪_S`-modules `𝓕`, `𝓖`,
>
> `(𝓕 ⊗_{𝒪_S} 𝓖)^a ≅ 𝓕^a ⊗_𝒪 𝓖^a`,
>
> where `𝓕^a` is the sheaf on `S_Zar` whose sections over `f : T → S` are `Γ(T, f^*𝓕)`.
>
> This is `AlgebraicGeometry.SmallZariski.associatedModuleTensorObjIsoOfComparison` read through
> Remark 03FH (1), `AlgebraicGeometry.SmallZariski.associatedModuleIsoOfSections`, at the three
> modules involved.  It is the description Stacks 03DU (4) gives, and so the description every
> statement of this tag is about.

```lean
public def associatedModuleOfSectionsTensorObjIso (F G : S.Modules)
    [F.IsQuasicoherent] [G.IsQuasicoherent] :
    associatedModuleOfSections B S hS
        ((Functor.uncurry.obj
            (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} S.sheaf)).obj (F, G)) ≅
      (Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u}
          (smallZariskiRingedSite B S hS).O)).obj
        (associatedModuleOfSections B S hS F, associatedModuleOfSections B S hS G)
```

## Tag 0GNB, a lemma

[Tag 0GNB](https://stacks.math.columbia.edu/tag/0GNB) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.isQuasicoherentOnSite_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleQuasicoherentTransfer.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleQuasicoherentTransfer.lean#L178). The attribute's comment: “part (2): colimits”.

> **Stacks 0GNB (2).**  A colimit of quasi-coherent `𝒪`-modules on the small étale site of a
> scheme is quasi-coherent; the shape is indexed at the size of the scheme, as in Stacks 06VE (3)
> on the same site.

```lean
public theorem isQuasicoherentOnSite_of_isColimit {K : Type u} [SmallCategory K]
    {D : K ⥤ SheafOfModules.{u} (structureSheaf B S hS)}
    (hD : ∀ k, (D.obj k).IsQuasicoherentOnSite) {c : Cocone D} (hc : IsColimit c) :
    c.pt.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.SmallEtale.isQuasicoherentOnSite_of_isColimit_cofan`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleQuasicoherentTransfer.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleQuasicoherentTransfer.lean#L187). The attribute's comment: “part (1): direct sums”.

> **Stacks 0GNB (1).**  A direct sum of quasi-coherent `𝒪`-modules on the small étale site of
> a scheme is quasi-coherent.

```lean
public theorem isQuasicoherentOnSite_of_isColimit_cofan {I : Type u}
    {F : I → SheafOfModules.{u} (structureSheaf B S hS)}
    (hF : ∀ i, (F i).IsQuasicoherentOnSite)
    {c : Cocone (Discrete.functor F)} (hc : IsColimit c) :
    c.pt.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.SmallEtale.isQuasicoherentOnSite_of_isColimit_cokernelCofork`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleQuasicoherentTransfer.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleQuasicoherentTransfer.lean#L199). The attribute's comment: “part (3): cokernels”.

> **Stacks 0GNB (3), the cokernel half.**  A cokernel of a morphism of quasi-coherent
> `𝒪`-modules on the small étale site of a scheme is quasi-coherent.

```lean
public theorem isQuasicoherentOnSite_of_isColimit_cokernelCofork
    {M N : SheafOfModules.{u} (structureSheaf B S hS)} (f : M ⟶ N)
    (hM : M.IsQuasicoherentOnSite) (hN : N.IsQuasicoherentOnSite)
    {c : CokernelCofork f} (hc : IsColimit c) : c.pt.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.SmallEtale.isQuasicoherentOnSite_of_isLimit_kernelFork`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleQuasicoherentTransfer.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleQuasicoherentTransfer.lean#L209). The attribute's comment: “part (3): kernels”.

> **Stacks 0GNB (3), the kernel half.**  A kernel of a morphism of quasi-coherent
> `𝒪`-modules on the small étale site of a scheme is quasi-coherent.

```lean
public theorem isQuasicoherentOnSite_of_isLimit_kernelFork
    {M N : SheafOfModules.{u} (structureSheaf B S hS)} (f : M ⟶ N)
    (hM : M.IsQuasicoherentOnSite) (hN : N.IsQuasicoherentOnSite)
    {c : KernelFork f} (hc : IsLimit c) : c.pt.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.SmallEtale.isQuasicoherentOnSite_shortExact_X₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleQuasicoherentTransfer.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleQuasicoherentTransfer.lean#L231). The attribute's comment: “part (4): the case of the sub, from the kernel clause”.

> **Stacks 0GNB (4), the case in which the quotient and the middle term are quasi-coherent.**
> The kernel term of a short exact sequence of `𝒪`-modules on the small étale site of a scheme is
> quasi-coherent when the other two are.

```lean
public theorem isQuasicoherentOnSite_shortExact_X₁
    {T : ShortComplex (SheafOfModules.{u} (structureSheaf B S hS))} (hT : T.ShortExact)
    (h₂ : T.X₂.IsQuasicoherentOnSite) (h₃ : T.X₃.IsQuasicoherentOnSite) :
    T.X₁.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.SmallEtale.isQuasicoherentOnSite_shortExact_X₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleQuasicoherentTransfer.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleQuasicoherentTransfer.lean#L241). The attribute's comment: “part (4): the case of the quotient, from the cokernel clause”.

> **Stacks 0GNB (4), the case in which the sub and the middle term are quasi-coherent.**
> The quotient term of a short exact sequence of `𝒪`-modules on the small étale site of a scheme
> is quasi-coherent when the other two are.

```lean
public theorem isQuasicoherentOnSite_shortExact_X₃
    {T : ShortComplex (SheafOfModules.{u} (structureSheaf B S hS))} (hT : T.ShortExact)
    (h₁ : T.X₁.IsQuasicoherentOnSite) (h₂ : T.X₂.IsQuasicoherentOnSite) :
    T.X₃.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.SmallEtale.isQuasicoherentOnSite_shortExact_X₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRestrictionRightExact.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleRestrictionRightExact.lean#L291). The attribute's comment: “clause (4), third case: the middle term of a short exact sequence”.

> **The third case of Stacks 0GNB (4): the middle term of a short exact sequence of
> `𝒪`-modules on the small étale site of a scheme is quasi-coherent when the outer two are.**
>
> The source derives this case not from clause (3) but from Stacks 06VE (10), and on this site the
> two are the same statement, by
> `AlgebraicGeometry.SmallEtale.isQuasicoherentOnSite_iff_essImage_associatedModuleQcoh`.

```lean
public theorem isQuasicoherentOnSite_shortExact_X₂ (hC : C.ShortExact)
    (h₁ : C.X₁.IsQuasicoherentOnSite) (h₃ : C.X₃.IsQuasicoherentOnSite) :
    SheafOfModules.IsQuasicoherentOnSite
      (R := AlgebraicGeometry.SmallEtale.structureSheaf B S hS) C.X₂
```

**`AlgebraicGeometry.SmallEtale.isQuasicoherentOnSite_internalHomSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInternalHomFinitePresentation.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmallEtaleInternalHomFinitePresentation.lean#L321). The attribute's comment: “clause (6): the internal Hom out of a module of finite presentation is quasi-coherent, small site at τ = étale”.

> **Clause (6) of Stacks 0GNB.**  The internal Hom `𝓗om_𝒪(𝓕, 𝓖)` of two `𝒪`-modules on the
> small étale site of a scheme `S` is quasi-coherent when `𝓕` is of finite presentation — Stacks
> 03DL (7) — and `𝓖` is quasi-coherent.
>
> Quasi-coherence is local on the site (Stacks 03DN), so it is enough to produce a covering family
> of the final object on whose members the restriction of the internal Hom is quasi-coherent, and
> the objects carrying a finite global presentation of `𝓕` form one, by the finite-presentation
> hypothesis itself.  On such an object the conclusion is
> `isQuasicoherentOnSite_internalHomSheaf_of_hasFiniteGlobalPresentation` of this namespace.

```lean
theorem isQuasicoherentOnSite_internalHomSheaf (hF : F.IsFinitePresentationOnSite)
    (hG : G.IsQuasicoherentOnSite) :
    (internalHomSheaf B S hS F G).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.SmallEtale.tensorSheaf_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/SmallEtaleQuasicoherentTensor.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/SmallEtaleQuasicoherentTensor.lean#L72). The attribute's comment: “tensor_products”.

> **The tensor product clause of Stacks 0GNB.**  The tensor product of two quasi-coherent
> `𝒪`-modules on the small étale site of a scheme is quasi-coherent.

```lean
public theorem tensorSheaf_isQuasicoherentOnSite
    (F G : SheafOfModules.{u} (structureSheaf B S hS))
    [F.IsQuasicoherentOnSite] [G.IsQuasicoherentOnSite] :
    SheafOfModules.IsQuasicoherentOnSite
      ((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u}
        (commRingStructureSheaf B S hS))).obj (F, G))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.tensorSheaf_isQuasicoherent`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorProduct/Basic.lean#L604), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/Parasitic/SmallEtaleTensorProduct.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Parasitic/SmallEtaleTensorProduct.lean#L66) (StacksFrontier): “tensor_products”.

## Tag 0GNC, a lemma

[Tag 0GNC](https://stacks.math.columbia.edu/tag/0GNC) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.isQuasicoherentOnSite_shortExact_X₂_all`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseRestrictionRightExactAll.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseRestrictionRightExactAll.lean#L355). The attribute's comment: “part (4), big site at every τ ∈ {Zariski, étale, smooth, syntomic, fppf}, unconditionally”.

> **Clause (4) of Stacks 0GNC on the big `τ`-site of a scheme, at every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`.**  Given a short exact sequence
> `0 → 𝓕₁ → 𝓕₂ → 𝓕₃ → 0` of `𝒪`-modules on `(Sch/S)_τ` with `𝓕₁` and `𝓕₃` quasi-coherent, the
> middle term `𝓕₂` is quasi-coherent.
>
> The source's three steps are
> `StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseExtensionClosure.lean`.  Of the two
> hypotheses they carried, essential surjectivity of `𝓕 ↦ 𝓕^a` is Descent, Proposition 03DX (1) and
> is `AlgebraicGeometry.BigFppfOver.baseQuasicoherentIsEssImageAssociatedModule`, and right
> exactness of restriction to `S_Zar` is
> `AlgebraicGeometry.BigFppfOver.epi_baseRestrictModule_map_all` above.

```lean
public theorem isQuasicoherentOnSite_shortExact_X₂_all (hC : C.ShortExact)
    (h₁ : C.X₁.IsQuasicoherentOnSite) (h₃ : C.X₃.IsQuasicoherentOnSite) :
    SheafOfModules.IsQuasicoherentOnSite
      (R := AlgebraicGeometry.FibredSite.baseRingStructureSheaf B S hS τ) C.X₂
```

**`AlgebraicGeometry.BigFppfOver.isClosedUnderExtensions_baseIsQuasicoherentOnSite_all`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseRestrictionRightExactAll.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/BaseRestrictionRightExactAll.lean#L370). The attribute's comment: “part (4), big site at every τ, as a closure-under-extensions instance”.

> Quasi-coherence of `𝒪`-modules on the big `τ`-site of a scheme is closed under extensions, at
> every `τ`.  This is clause (4) of Stacks 0GNC in the shape
> `CategoryTheory.ObjectProperty.IsClosedUnderExtensions` records; it has no hypothesis, so it is
> safe as an instance.

```lean
public instance isClosedUnderExtensions_baseIsQuasicoherentOnSite_all (τ : SiteKind) :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      (FibredSite.baseRingStructureSheaf B S hS τ)).IsClosedUnderExtensions
```

**`AlgebraicGeometry.BigFppfOver.isQuasicoherentOnSite_tensorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteProperties.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteProperties.lean#L133). The attribute's comment: “part (5)”.

> **Stacks 0GNC, part (5).**  The tensor product of two quasi-coherent `𝒪`-modules on the big
> `τ`-site of a scheme `S` is quasi-coherent, for each of the five topologies.
>
> The tensor product is the one of Stacks 0GMW, the sheafification of the objectwise tensor
> product of the underlying presheaves of modules.  The statement is the quasi-coherent clause of
> Stacks 03L6 on a ringed site,
> `Stacks.SheafOfModules.TensorLocalProperties.tensorSheaf_isQuasicoherentOnSite`, read at this
> site: the two factors are globally presented on the members of two covering families, the
> objects admitting an arrow into a member of each again cover, and over such an object the
> tensor product of two globally presented modules is globally presented.

```lean
theorem isQuasicoherentOnSite_tensorSheaf (τ : SiteKind)
    (F G : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (baseRingedSite B S hS τ).O))
    [SheafOfModules.IsQuasicoherentOnSite F] [SheafOfModules.IsQuasicoherentOnSite G] :
    SheafOfModules.IsQuasicoherentOnSite
      ((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u}
        (FibredSite.baseStructureSheaf B S hS τ))).obj (F, G))
```

**`AlgebraicGeometry.BigFppfOver.isQuasicoherentOnSite_internalHomSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteProperties.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteProperties.lean#L156). The attribute's comment: “part (6)”.

> **Stacks 0GNC, part (6).**  The internal hom `𝓗om_𝒪(𝓕, 𝓖)` of Stacks 03EM is quasi-coherent
> on the big `τ`-site of a scheme `S`, for each of the five topologies, when `𝓕` and `𝓖` are
> quasi-coherent and `𝓕` is finite locally free.
>
> This is `AlgebraicGeometry.RingedSite.internalHomSheaf_isQuasicoherent`, the statement for an
> arbitrary ringed site, with its two sheafification hypotheses on the slice sites discharged:
> every slice of the big category of schemes over `S` is essentially small, so abelian presheaves
> on it have a sheafification whose weak equivalences are the locally bijective maps.

```lean
theorem isQuasicoherentOnSite_internalHomSheaf (τ : SiteKind)
    (F G : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (baseRingedSite B S hS τ).O))
    [SheafOfModules.IsQuasicoherentOnSite F] [SheafOfModules.IsQuasicoherentOnSite G]
    [SheafOfModules.IsFiniteLocallyFree.{u, u, u + 1} F] :
    (RingedSite.internalHomSheaf (baseRingedSite B S hS τ) F G).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.RingedSite.internalHomSheaf_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/InternalHom.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/InternalHom.lean#L432). The attribute's comment: “internal_hom”.

> Internal Hom from a finite locally free quasi-coherent sheaf is quasi-coherent.

```lean
theorem internalHomSheaf_isQuasicoherent
    (X : RingedSite.{u, v, w})
    (F G : _root_.SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    [∀ U : X.C, HasWeakSheafify (X.J.over U) AddCommGrpCat.{w}]
    [∀ U : X.C, (X.J.over U).WEqualsLocallyBijective AddCommGrpCat.{w}]
    [F.IsQuasicoherentOnSite] [G.IsQuasicoherentOnSite]
    [SheafOfModules.IsFiniteLocallyFree.{w, v, u} F] :
    (internalHomSheaf X F G).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.BigFppfOver.isClosedUnderColimitsOfShape_baseIsQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentColimitsBigSites.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentColimitsBigSites.lean#L121). The attribute's comment: “part (2), big site at every τ ∈ {Zariski, étale, smooth, syntomic, fppf}, unconditionally, for an index category K at an arbitrary universe”.

> **Stacks 0GNC (2) on the big `τ`-site of `S`, at every `τ` and with no hypothesis**:
> quasi-coherence of `𝒪`-modules on `(Sch/S)_τ` is closed under colimits of shape `K`, for `K` at
> an arbitrary universe.
>
> This is the transfer the source performs with Lemma 06VE, carried out at every `τ`: the
> quasi-coherent modules of `(Sch/S)_τ` are the essential image of `𝓕 ↦ 𝓕^a`, which is fully
> faithful (Stacks 0GN7) and preserves colimits (Stacks 06VE (3)) out of `QCoh(𝒪_S)`, where the
> colimits exist and are quasi-coherent; so they are closed under those colimits.  That the
> essential image is *all* the quasi-coherent modules is the essential-surjectivity half of
> Descent, Proposition 03DX (1) at `(Sch/S)_τ`, and is
> `AlgebraicGeometry.BigFppfOver.baseQuasicoherentIsEssImageAssociatedModule`.

```lean
public theorem isClosedUnderColimitsOfShape_baseIsQuasicoherentOnSite (τ : SiteKind)
    (K : Type uK) [Category.{uK} K]
    [∀ R : CommRingCat.{u}, HasColimitsOfShape K (ModuleCat.{u} R)]
    [HasColimitsOfShape K (SheafOfModules.{u} S.ringCatSheaf)] :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      (FibredSite.baseRingStructureSheaf B S hS τ)).IsClosedUnderColimitsOfShape K
```

**`AlgebraicGeometry.BigFppfOver.isClosedUnderColimitsOfShape_discrete_baseIsQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentColimitsBigSites.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentColimitsBigSites.lean#L142). The attribute's comment: “part (1), big site at every τ ∈ {Zariski, étale, smooth, syntomic, fppf}, unconditionally”.

> **Stacks 0GNC (1) on the big `τ`-site of `S`, at every `τ` and with no hypothesis**: a
> direct sum of quasi-coherent `𝒪`-modules on `(Sch/S)_τ` is quasi-coherent.  A direct sum is a
> colimit over a discrete index category, which is how the source argues it.

```lean
public theorem isClosedUnderColimitsOfShape_discrete_baseIsQuasicoherentOnSite (τ : SiteKind)
    (I : Type u) :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      (FibredSite.baseRingStructureSheaf B S hS τ)).IsClosedUnderColimitsOfShape
      (Discrete I)
```

**`AlgebraicGeometry.BigFppfOver.isClosedUnderColimitsOfShape_walkingParallelPair_baseIsQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentColimitsBigSites.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentColimitsBigSites.lean#L155). The attribute's comment: “part (3), big site at every τ ∈ {Zariski, étale, smooth, syntomic, fppf}, unconditionally”.

> **Stacks 0GNC (3) on the big `τ`-site of `S`, at every `τ` and with no hypothesis**: the
> cokernel of a morphism of quasi-coherent `𝒪`-modules on `(Sch/S)_τ` is quasi-coherent.  A
> cokernel is a colimit over `CategoryTheory.Limits.WalkingParallelPair`, and the source obtains
> clause (3) from clause (2) in exactly this way.

```lean
public theorem isClosedUnderColimitsOfShape_walkingParallelPair_baseIsQuasicoherentOnSite
    (τ : SiteKind) :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      (FibredSite.baseRingStructureSheaf B S hS τ)).IsClosedUnderColimitsOfShape
      WalkingParallelPair
```

**`AlgebraicGeometry.BigFppfOver.isClosedUnderColimitsOfShape_isQuasicoherentOnSite_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentColimitsFppfSite.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentColimitsFppfSite.lean#L87). The attribute's comment: “part (2), big site at τ = fppf”.

> **Stacks 0GNC (2)** for `τ = fppf`: a colimit of quasi-coherent `𝒪`-modules on the big fppf
> site of a scheme `S` is quasi-coherent.
>
> `AlgebraicGeometry.BigFppfOver.isClosedUnderColimitsOfShape_baseIsQuasicoherentOnSite`, the
> `τ`-indexed form of the clause, at `τ = .fppf`; the statement here is the one about the fppf
> structure sheaf itself, and the two agree because
> `FibredSite.baseRingStructureSheaf B S hS .fppf = structureSheaf B S hS` holds by `rfl`.
> This is the transfer the source performs with Lemma 06VE: the colimit is formed in `QCoh(𝒪_S)`,
> where it exists and is quasi-coherent, and carried up by `𝓕 ↦ 𝓕^a`, which preserves colimits
> and whose essential image is exactly the quasi-coherent modules of the site.

```lean
public theorem isClosedUnderColimitsOfShape_isQuasicoherentOnSite_unconditional
    (K : Type u) [Category.{u} K] :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      (structureSheaf B S hS)).IsClosedUnderColimitsOfShape K
```

**`AlgebraicGeometry.BigFppfOver.isClosedUnderColimitsOfShape_discrete_isQuasicoherentOnSite_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentColimitsFppfSite.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentColimitsFppfSite.lean#L97). The attribute's comment: “part (1), big site at τ = fppf”.

> **Stacks 0GNC (1)** for `τ = fppf`: a direct sum of quasi-coherent `𝒪`-modules on the big
> fppf site of a scheme `S` is quasi-coherent.  A direct sum is a colimit over a discrete index
> category, which is how the source argues it.

```lean
public theorem isClosedUnderColimitsOfShape_discrete_isQuasicoherentOnSite_unconditional
    (I : Type u) :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      (structureSheaf B S hS)).IsClosedUnderColimitsOfShape (Discrete I)
```

**`AlgebraicGeometry.BigFppfOver.isClosedUnderColimitsOfShape_walkingParallelPair_isQuasicoherentOnSite_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentColimitsFppfSite.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Descent/QuasicoherentColimitsFppfSite.lean#L108). The attribute's comment: “part (3), big site at τ = fppf”.

> **Stacks 0GNC (3)** for `τ = fppf`: the cokernel of a morphism of quasi-coherent
> `𝒪`-modules on the big fppf site of a scheme `S` is quasi-coherent.  A cokernel is a colimit
> over `CategoryTheory.Limits.WalkingParallelPair`, and the source obtains clause (3) from
> clause (2) in exactly this way.

```lean
public theorem
    isClosedUnderColimitsOfShape_walkingParallelPair_isQuasicoherentOnSite_unconditional :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      (structureSheaf B S hS)).IsClosedUnderColimitsOfShape WalkingParallelPair
```

**`AlgebraicGeometry.RingedSite.internalHomSheaf_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/QuasicoherentInternalHom.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/QuasicoherentInternalHom.lean#L321). The attribute's comment: “internal_hom”. References: EGA I (9.1.1), “special case”; SGA 3 III (0.6), “special case”.

> On a ringed site whose slices admit sheafification of abelian sheaves, the internal Hom of
> Stacks 03EM from a finite locally free quasi-coherent module to a quasi-coherent module is
> quasi-coherent.

```lean
public theorem internalHomSheaf_isQuasicoherent
    [∀ U : X.C, HasWeakSheafify (X.J.over U) AddCommGrpCat.{w}]
    [∀ U : X.C, (X.J.over U).WEqualsLocallyBijective AddCommGrpCat.{w}]
    [F.IsQuasicoherentOnSite] [G.IsQuasicoherentOnSite]
    [SheafOfModules.IsFiniteLocallyFree.{w, v, u} F] :
    (X.internalHomSheaf F G).IsQuasicoherentOnSite
```

## Tag 0GNE, a lemma

[Tag 0GNE](https://stacks.math.columbia.edu/tag/0GNE) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.hasColimitsOfSize_quasicoherentOnSite_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteColimitAgreement.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteColimitAgreement.lean#L125). The attribute's comment: “part (1), existence: QCoh((Sch/S)_fppf, O) has colimits indexed at the size of the site”.

> **Stacks 0GNE (1), the existence half**, with no hypothesis: the category of quasi-coherent
> `𝒪`-modules on the big fppf site of `S` has all colimits indexed at the size of the site.
>
> `AlgebraicGeometry.BigFppfOver.hasColimitsOfSize_quasicoherentOnSite'` with its
> essential-surjectivity hypothesis discharged by
> `AlgebraicGeometry.BigFppfOver.quasicoherentIsEssImageAssociatedModule'`.

```lean
public theorem hasColimitsOfSize_quasicoherentOnSite_fppf :
    HasColimitsOfSize.{u, u}
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (structureSheaf B S hS)).FullSubcategory
```

**`AlgebraicGeometry.BigFppfOver.preservesColimitsOfSize_quasicoherentOnSite_ι_fppf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteColimitAgreement.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteColimitAgreement.lean#L140). The attribute's comment: “part (1), agreement: the colimits of QCoh((Sch/S)_fppf, O) are the colimits taken in Mod((Sch/S)_fppf, O)”.

> **Stacks 0GNE (1), the agreement with `Mod((Sch/S)_fppf, 𝒪)`**, with no hypothesis: a colimit
> of quasi-coherent `𝒪`-modules on `(Sch/S)_fppf` is the colimit of the same diagram taken in all
> `𝒪`-modules on `(Sch/S)_fppf`.
>
> `AlgebraicGeometry.BigFppfOver.preservesColimitsOfSize_quasicoherentOnSite_ι'` with its
> essential-surjectivity hypothesis discharged.

```lean
public theorem preservesColimitsOfSize_quasicoherentOnSite_ι_fppf :
    PreservesColimitsOfSize.{u, u}
      (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (structureSheaf B S hS)).ι
```

**`AlgebraicGeometry.BigFppfOver.preservesColimitsOfSize_quasicoherentOnSite_ι_comp_restrictTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteColimitAgreement.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteColimitAgreement.lean#L194). The attribute's comment: “part (1), agreement: the colimits of QCoh((Sch/S)_fppf, O) are the colimits taken in Mod((Sch/S)_tau, O), for every one of the five topologies and for an arbitrary diagram”.

> **Stacks 0GNE (1), the agreement with `Mod((Sch/S)_τ, 𝒪)`**, over every shape indexed at the
> size of the site: the colimits of `QCoh((Sch/S)_fppf, 𝒪)` are the colimits taken in
> `Mod((Sch/S)_τ, 𝒪)`, at every one of the five topologies and for an arbitrary diagram.
>
> Together with `AlgebraicGeometry.BigFppfOver.hasColimitsOfSize_quasicoherentOnSite_fppf` and
> `…preservesColimitsOfSize_quasicoherentOnSite_ι_fppf` this is the source's clause (1): the
> colimits exist and agree with those computed in `Mod((Sch/S)_Zar, 𝒪)`,
> `Mod((Sch/S)_étale, 𝒪)` and `Mod((Sch/S)_fppf, 𝒪)`.

```lean
public theorem preservesColimitsOfSize_quasicoherentOnSite_ι_comp_restrictTopology :
    PreservesColimitsOfSize.{u, u}
      ((SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u} (structureSheaf B S hS)).ι ⋙
        restrictTopology B S hS τ)
```

**`AlgebraicGeometry.BigFppfOver.isFiniteLocallyFreeOnSite_restrictTopology_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteFiniteLocallyFreeAgreement.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteFiniteLocallyFreeAgreement.lean#L414). The attribute's comment: “part (3), the parenthetical: finite local freeness agrees at τ = fppf, étale and Zariski”.

> **Descent, Lemma 0GNE (3), the parenthetical.**  A quasi-coherent `𝒪`-module `𝓕` on the big
> fppf site of `S` is finite locally free there if and only if its reading as an `𝒪`-module on
> `(Sch/S)_τ` is finite locally free, for every one of the five topologies — in particular for the
> étale and the Zariski topology, which are the two the source names alongside fppf.
>
> The source's proof is run unchanged: `𝓕 = 𝓗ᵃ` by the essential surjectivity half of Descent,
> Proposition 03DX (1) at `τ = fppf`
> (`AlgebraicGeometry.BigFppfOver.essImage_associatedModuleQcoh_of_isQuasicoherentOnSite`), and
> both sides are then compared with "`𝓗` is finite locally free on `S`" by
> `AlgebraicGeometry.BigFppfOver.isFiniteLocallyFreeOnSite_baseAssociatedModule_iff`, the reading
> on `(Sch/S)_τ` of `𝓗ᵃ` being `𝓗ᵃ` computed on `(Sch/S)_τ` by
> `AlgebraicGeometry.BigFppfOver.restrictTopologyAssociatedModuleIso`.
>
> The `if` half needs no quasi-coherence and no reduction at all: it is
> `Stacks.SheafOfModules.isFiniteLocallyFreeOnSite_of_comparisonPushforward`, valid for an
> arbitrary module and an arbitrary pair of topologies.  Quasi-coherence is used only for the
> `only if` half, and it is the hypothesis the source's clause carries.

```lean
public theorem isFiniteLocallyFreeOnSite_restrictTopology_iff (τ : SiteKind)
    (𝓕 : SheafOfModules.{u} (structureSheaf B S hS))
    (h𝓕 : SheafOfModules.IsQuasicoherentOnSite.{u + 1, u, u, u} 𝓕) :
    SheafOfModules.IsFiniteLocallyFreeOnSite 𝓕 ↔
      SheafOfModules.IsFiniteLocallyFreeOnSite ((restrictTopology B S hS τ).obj 𝓕)
```

**`AlgebraicGeometry.BigFppfOver.restrictTopology_internalHomSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteInternalHomQuasicoherence.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteInternalHomQuasicoherence.lean#L94). The attribute's comment: “part (3), the internal homs computed on (Sch/S)_fppf and on (Sch/S)_tau agree, for arbitrary O-modules, at every one of the five topologies”.

> **Stacks 0GNE (3), the agreement, at the big sites of a scheme.**  For arbitrary `𝒪`-modules
> `𝓕`, `𝓖` on `(Sch/S)_fppf`, the internal hom `𝓗om_𝒪(𝓕, 𝓖)` computed in `Mod((Sch/S)_fppf, 𝒪)`
> and read for the coarser topology *is* the internal hom of the readings computed in
> `Mod((Sch/S)_τ, 𝒪)`, at every one of the five topologies — so in particular the Zariski, étale
> and fppf values of the source's statement agree.
>
> This is `AlgebraicGeometry.RingedSite.coarsenModules_internalHomSheaf`, the statement for an
> arbitrary ringed site read with a coarser topology, at `(Sch/S)_fppf` and
> `AlgebraicGeometry.BigFppfOver.baseOverTopology_le_fppf`: the ringed site `(Sch/S)_fppf` read
> with the `τ`-topology is `(Sch/S)_τ`, the structure sheaves having the same underlying presheaf
> and a sheaf condition that is a proposition.
>
> An *equality* of sheaves of modules, not an isomorphism: the internal hom of Stacks 03EM is a
> construction on presheaves of modules and the topology enters only in the proof that the result
> is a sheaf, so there is nothing to compare.  No quasi-coherence and no finite local freeness are
> needed for the agreement; they are the hypotheses of the quasi-coherence clause below.

```lean
public theorem restrictTopology_internalHomSheaf (τ : SiteKind)
    (F G : SheafOfModules.{u} (structureSheaf B S hS)) :
    (restrictTopology B S hS τ).obj
        (RingedSite.internalHomSheaf (baseRingedSite B S hS .fppf) F G) =
      RingedSite.internalHomSheaf (baseRingedSite B S hS τ)
        ((restrictTopology B S hS τ).obj F) ((restrictTopology B S hS τ).obj G)
```

**`AlgebraicGeometry.BigFppfOver.isQuasicoherentOnSite_internalHomSheaf_of_isFiniteLocallyFreeOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteInternalHomQuasicoherence.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteInternalHomQuasicoherence.lean#L121). The attribute's comment: “part (3), quasi-coherence of the common value, on the big tau-site for every one of the five topologies, with finite local freeness in the sense of Modules on Sites 03DL (2)”.

> **Stacks 0GNE (3), the quasi-coherence of the common value**, on the big `τ`-site of `S` for
> every `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`, with finite local freeness in the sense of
> Modules on Sites, Definition 03DL (2) — the sense in which the source's part (3) states it.
>
> At `τ = fppf` this is the source's "the common value is an object of `QCoh((Sch/S)_fppf, 𝒪)`";
> the agreement of the values computed at the five topologies, which is what makes "the common
> value" a legitimate phrase, is
> `AlgebraicGeometry.BigFppfOver.restrictTopology_internalHomSheaf` above, an equality of sheaves
> of modules and not merely an isomorphism.
>
> This is `AlgebraicGeometry.BigFppfOver.isQuasicoherentOnSite_internalHomSheaf` — Stacks 0GNC on
> the big `τ`-site — with its finite-local-freeness hypothesis supplied from the 03DL (2) form by
> `AlgebraicGeometry.SheafOfModules.isFiniteLocallyFree_of_isFiniteLocallyFreeOnSite`, whose two
> sheafification hypotheses on the slices of the big site are the instances
> `AlgebraicGeometry.BigFppfOver.hasSheafify_baseOver` and
> `…wEqualsLocallyBijective_baseOver`.

```lean
public theorem isQuasicoherentOnSite_internalHomSheaf_of_isFiniteLocallyFreeOnSite
    (τ : SiteKind)
      (F G : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
        (baseRingedSite B S hS τ).O))
    [SheafOfModules.IsQuasicoherentOnSite F] [SheafOfModules.IsQuasicoherentOnSite G]
    (hF : SheafOfModules.IsFiniteLocallyFreeOnSite F) :
    (RingedSite.internalHomSheaf (baseRingedSite B S hS τ) F G).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.BigFppfOver.tensorAgreementQuasicoherentOnSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteTensorAgreement.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteTensorAgreement.lean#L288). The attribute's comment: “part (2), the tensor products computed on (Sch/S)_fppf and on (Sch/S)_tau agree, for an arbitrary pair of quasi-coherent O-modules on (Sch/S)_fppf, at every one of the five topologies”.

> **Stacks 0GNE (2), the agreement, at the source's own scope.**  For an **arbitrary** pair
> `𝓕`, `𝓖` of quasi-coherent `𝒪`-modules on `(Sch/S)_fppf`, the tensor product `𝓕 ⊗_𝒪 𝓖` computed
> in `Mod((Sch/S)_fppf, 𝒪)`, read for the coarser topology, *is* the tensor product computed in
> `Mod((Sch/S)_τ, 𝒪)` — at every one of the five topologies, so in particular the Zariski, étale
> and fppf values of the source's statement agree.
>
> `AlgebraicGeometry.BigFppfOver.tensorAgreementAssociatedModule` is this for `𝓕 = 𝓗^a` and
> `𝓖 = 𝓘^a`; the reduction of an arbitrary pair to that case is Stacks 03DX (1) at `τ = fppf`
> together with the functoriality of the tensor product in both arguments — see the implementation
> notes.  The comparison itself is the same one, the inverse of the unit of "sheafify for fppf" ⊣
> "read an fppf sheaf for `τ`", so this is not a transported isomorphism but the canonical one
> with its invertibility now known at every quasi-coherent pair.

```lean
def tensorAgreementQuasicoherentOnSite
    (hF : F.IsQuasicoherentOnSite) (hG : G.IsQuasicoherentOnSite) :
    (restrictTopology B S hS τ).obj
        ((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor
            (FibredSite.baseStructureSheaf B S hS .fppf))).obj (F, G)) ≅
      (Functor.uncurry.obj
          (Stacks.SheafOfModules.Tensor.sheafTensor (FibredSite.baseStructureSheaf B S hS τ))).obj
        ((restrictTopology B S hS τ).obj F, (restrictTopology B S hS τ).obj G)
```

**`AlgebraicGeometry.BigFppfOver.isQuasicoherentOnSite_tensorRestrictTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteTensorAgreement.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteTensorAgreement.lean#L311). The attribute's comment: “part (2), quasi-coherence of the common value, for an arbitrary pair of quasi-coherent O-modules on (Sch/S)_fppf, at every one of the five topologies”.

> **Stacks 0GNE (2), the quasi-coherence of the common value, at the source's own scope.**  For
> an arbitrary pair of quasi-coherent `𝒪`-modules on `(Sch/S)_fppf`, the common value of the
> tensor products — the right-hand side of
> `AlgebraicGeometry.BigFppfOver.tensorAgreementQuasicoherentOnSite` — is quasi-coherent on
> `(Sch/S)_τ`, at every one of the five topologies; at `τ = fppf` this is the source's "the common
> value is an object of `QCoh((Sch/S)_fppf, 𝒪)`".
>
> By the reduction it is the reading of `(𝓗 ⊗_{𝒪_S} 𝓘)^a`, which is quasi-coherent by Stacks
> 01CE (3) and Stacks 03DV at every `τ`.

```lean
theorem isQuasicoherentOnSite_tensorRestrictTopology
    (hF : F.IsQuasicoherentOnSite) (hG : G.IsQuasicoherentOnSite) :
    ((Functor.uncurry.obj
        (Stacks.SheafOfModules.Tensor.sheafTensor (FibredSite.baseStructureSheaf B S hS τ))).obj
      ((restrictTopology B S hS τ).obj F,
        (restrictTopology B S hS τ).obj G)).IsQuasicoherentOnSite
```

**`Stacks.SheafOfModules.tensorLeftFactorization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean#L424). The attribute's comment: “part (2), the tensor product for the finer topology is the sheafification of the one for the coarser topology, for an arbitrary pair of topologies on one category”.

> **Stacks 0GNE (2), the comparison.**  The tensor product of two sheaves of modules for the
> finer topology is the sheafification, for the finer topology, of their tensor product taken for
> the coarser one.  Both are sheafifications of the objectwise tensor product of the two
> underlying presheaves of modules, which does not mention a topology, so this is one component
> of `Stacks.SheafOfModules.sheafificationFactorization`.

```lean
noncomputable def tensorLeftFactorization :
    ((Stacks.SheafOfModules.Tensor.sheafTensor (J := J) (R)).obj F).obj G ≅
      (comparisonPullback.{u, v, w, m} h ((Stacks.SheafOfModules.Tensor.ringSheaf (J := J)) R)).obj
        (((Stacks.SheafOfModules.Tensor.sheafTensor (J := K) ((commRingOfLe h R))).obj
            ((comparisonPushforward.{u, v, w, m} h ((Stacks.SheafOfModules.Tensor.ringSheaf (J := J)) R)).obj F)).obj
          ((comparisonPushforward.{u, v, w, m} h ((Stacks.SheafOfModules.Tensor.ringSheaf (J := J)) R)).obj G))
```

**`Stacks.SheafOfModules.tensorLeftAgreement`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean#L450). The attribute's comment: “part (2), the two tensor products agree once the coarser one is a sheaf for the finer topology”.

> **Towards Stacks 0GNE (2), the agreement.**  The tensor product computed for the finer
> topology, read for the coarser one, is the tensor product computed for the coarser topology, as
> soon as the latter is already a sheaf for the finer topology — which is what invertibility of
> the unit at it says.
>
> `hunit` is a hypothesis the source does not have, and the clause string of the `stacks`
> attribute below says so: what is proved here is the implication.  It is discharged at the big
> sites of a scheme, by Stacks 06VE (7), in
> `AlgebraicGeometry.BigFppfOver.isIso_comparisonUnit_tensorRestrictTopology`
> (`StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteTensorAgreement.lean`),
> and the 0GNE (2) attribute for the clause without that hypothesis sits there, on
> `…tensorAgreementQuasicoherentOnSite`, which is this declaration with `hunit` supplied for an
> arbitrary pair of quasi-coherent modules on `(Sch/S)_fppf` — note that the arbitrary pair is
> reached by widening `hunit`, so the isomorphism it returns is still this canonical one.  The
> half of part (2) that needs no hypothesis at all is
> `Stacks.SheafOfModules.tensorLeftFactorization`, which carries the tag here.

```lean
noncomputable def tensorLeftAgreement
    (hunit : IsIso ((comparisonAdjunction.{u, v, w, m} h
        ((Stacks.SheafOfModules.Tensor.ringSheaf (J := J)) R)).unit.app
      (((Stacks.SheafOfModules.Tensor.sheafTensor (J := K) ((commRingOfLe h R))).obj
          ((comparisonPushforward.{u, v, w, m} h ((Stacks.SheafOfModules.Tensor.ringSheaf (J := J)) R)).obj F)).obj
        ((comparisonPushforward.{u, v, w, m} h ((Stacks.SheafOfModules.Tensor.ringSheaf (J := J)) R)).obj G)))) :
    (comparisonPushforward.{u, v, w, m} h ((Stacks.SheafOfModules.Tensor.ringSheaf (J := J)) R)).obj
        (((Stacks.SheafOfModules.Tensor.sheafTensor (J := J) (R)).obj F).obj G) ≅
      ((Stacks.SheafOfModules.Tensor.sheafTensor (J := K) ((commRingOfLe h R))).obj
          ((comparisonPushforward.{u, v, w, m} h ((Stacks.SheafOfModules.Tensor.ringSheaf (J := J)) R)).obj F)).obj
        ((comparisonPushforward.{u, v, w, m} h ((Stacks.SheafOfModules.Tensor.ringSheaf (J := J)) R)).obj G)
```

**`AlgebraicGeometry.RingedSite.coarsenModules_internalHomSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean#L498). The attribute's comment: “part (3), the internal homs computed for two topologies agree, for arbitrary sheaves of modules on a ringed site”.

> **Stacks 0GNE (3), the agreement clause.**  The internal hom of two sheaves of modules
> computed on a ringed site, read for a coarser topology, *is* the internal hom of their readings
> computed for the coarser topology.
>
> This is the source's own argument for part (3): the internal hom of Stacks 03EM is a
> construction on presheaves of modules, and the topology enters only in the proof that the
> result is a sheaf, which needs the sheaf condition on the target alone.  So no comparison map
> is involved — the two sheaves of modules have the same underlying presheaf of modules, and
> their sheaf conditions are propositions.

```lean
theorem coarsenModules_internalHomSheaf (X : RingedSite.{u, v, w})
    {J' : GrothendieckTopology X.C} (h : J' ≤ X.J)
    (A B : SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    (coarsenModules X h).obj (internalHomSheaf X A B) =
      internalHomSheaf (X.ofLE h) ((coarsenModules X h).obj A)
        ((coarsenModules X h).obj B)
```

**`AlgebraicGeometry.BigFppfOver.restrictTopologyAssociatedModuleIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean, line 602](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean#L602). The attribute's comment: “the key to the proof: the associated-module functor is given by one formula for all five topologies, so its values for the five topologies agree”.

> **The key to Stacks 0GNE.**  The functor `𝓕 ↦ 𝓕^a` is given by the same formula for every
> `τ ∈ {Zariski, étale, smooth, syntomic, fppf}`: the associated module of a quasi-coherent
> `𝒪_S`-module on `(Sch/S)_τ` is the associated module on `(Sch/S)_fppf`, read for the coarser
> topology.
>
> Every clause of the source's lemma is deduced from this, which is why it carries the tag: the
> source's proof of all three parts is "the equivalence of Proposition 03DX is given by the same
> formula independent of the choice of the topology", applied to a colimit, to a tensor product
> and to an internal hom.

```lean
noncomputable def restrictTopologyAssociatedModuleIso (τ : SiteKind) (F : S.Modules)
    [F.IsQuasicoherent] :
    (restrictTopology B S hS τ).obj ((associatedModule B S hS).obj F) ≅
      (baseAssociatedModule B S hS τ).obj F
```

**`AlgebraicGeometry.BigFppfOver.isColimitMapCoconeBaseAssociatedModuleQcoh`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean, line 762](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean#L762). The attribute's comment: “part (1), the colimit of a diagram of associated modules computed in Mod((Sch/S)_τ, O), for every one of the five topologies”.

> **Stacks 0GNE (1), the comparison with the modules of `(Sch/S)_τ`, every `τ`.**  A colimit
> of a diagram of quasi-coherent modules on `S` is carried by `𝓕 ↦ 𝓕^a` to a colimit in
> `Mod((Sch/S)_τ, 𝒪)`.  Together with
> `AlgebraicGeometry.BigFppfOver.restrictTopologyAssociatedModuleIso`, which identifies the
> vertex at `τ` with the vertex at fppf read for the coarser topology, this says that the
> colimits computed in the five module categories agree.
>
> The source states the clause for a diagram in `QCoh((Sch/S)_fppf, 𝒪)`, and reduces it to a
> diagram in `QCoh(𝒪_S)` by the essential surjectivity of `𝓕 ↦ 𝓕^a`; the diagram here is the
> reduced one.  That reduction is now available, and the clause for an arbitrary diagram is
> `AlgebraicGeometry.BigFppfOver.preservesColimitsOfSize_quasicoherentOnSite_ι_comp_restrictTopology`
> (`StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/BigSiteColimitAgreement.lean`).

```lean
noncomputable def isColimitMapCoconeBaseAssociatedModuleQcoh
    {D : K ⥤ (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory}
    {c : Cocone D} (hc : IsColimit c) :
    IsColimit ((baseAssociatedModuleQcoh B S hS τ).mapCocone c)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.RingedSite.internalHomSheaf_isQuasicoherent`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/InternalHom.lean#L432), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean, line 811](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherentTopologiesTwo/TopologyIndependence.lean#L811) (StacksFrontier): “part (3), quasi-coherence of the common value”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.10, Tag 0GN9](https://stacks.math.columbia.edu/tag/0GN9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

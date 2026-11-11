---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.acyclicPushforwardOfInjective_of_isAffineSpace, Stacks.Cohomology.isTotallyAcyclic_pushforwardModules_of_injective_largeSource, Stacks.Cohomology.isTotallyAcyclic_pushforwardModules_of_injective, AlgebraicGeometry.Space.preservesInjectiveObjects_modulePushforward_of_isFlat, AlgebraicGeometry.RingedToposHom.pushforwardModules_injective, Stacks.Cohomology.rightAcyclic_pushforwardModules_of_isTotallyAcyclic, Stacks.Cohomology.isTotallyAcyclic_rightAcyclic_globalSections, Stacks.Cohomology.GlobalSectionsLargeSite.isZero_rightDerived_globalSectionsFunctor_of_isTotallyAcyclic
statement: formalized
proof: formalized
---

# 21.14 The Leray spectral sequence

Section 21.14 of the Stacks Project, [Tag 072X](https://stacks.math.columbia.edu/tag/072X). 7 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 072Z, a lemma

[Tag 072Z](https://stacks.math.columbia.edu/tag/072Z) in the Stacks Project.

**`AlgebraicGeometry.Space.acyclicPushforwardOfInjective_of_isAffineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineBasePushforwardInjectiveAcyclic.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineBasePushforwardInjectiveAcyclic.lean#L120). The attribute's comment: “at the small étale seating of algebraic spaces, in the shape 0731(3) puts it in: acyclicity of the direct image of an injective for global sections over an affine base”.

> If `Y` is an affine algebraic space, the direct image along `f : X ⟶ Y` of an injective
> `𝒪_X`-module is acyclic for global sections of `𝒪_Y`-modules, that is,
> `AlgebraicGeometry.Space.AcyclicPushforwardOfInjective` holds for `f`.

```lean
theorem acyclicPushforwardOfInjective_of_isAffineSpace (f : X ⟶ Y)
    (hY : IsAffineSpace B S hS Y.1) : AcyclicPushforwardOfInjective B S hS f
```

**`Stacks.Cohomology.isTotallyAcyclic_pushforwardModules_of_injective_largeSource`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/PushforwardLargeSource.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/PushforwardLargeSource.lean#L273). The attribute's comment: “the source ringed topos's object, morphism and section universes unrelated”.

> **Stacks 072Z with the source ringed topos's universes unconstrained.**  The sheaf of
> abelian groups underlying the direct image of an injective sheaf of modules along a morphism of
> ringed topoi is totally acyclic: its cohomology over every sheaf of sets on the target vanishes
> in positive degrees.
>
> `Stacks.Cohomology.isTotallyAcyclic_pushforwardModules_of_injective` is this statement for a
> source whose three universes are equal.  Here the source site's objects, morphisms and sections
> lie at three unrelated universes, which is the seating of the small étale site of an algebraic
> space.

```lean
theorem isTotallyAcyclic_pushforwardModules_of_injective_largeSource :
    Stacks.Cohomology.IsTotallyAcyclic Y.J
      ((SheafOfModules.toSheaf (ringSheaf Y.O)).obj
        ((pushforwardModules f).obj I))
```

**`Stacks.Cohomology.isTotallyAcyclic_pushforwardModules_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/PushforwardOfAnInjective.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/PushforwardOfAnInjective.lean#L268).

> **Stacks 072Z.** The sheaf of abelian groups underlying the direct image of an injective
> sheaf of modules along a morphism of ringed topoi is totally acyclic: its cohomology over every
> sheaf of sets on the target vanishes in positive degrees.

```lean
theorem isTotallyAcyclic_pushforwardModules_of_injective :
    IsTotallyAcyclic Y.J ((SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)).obj
      ((pushforwardModules f).obj I))
```

## Tag 0730, a lemma

[Tag 0730](https://stacks.math.columbia.edu/tag/0730) in the Stacks Project.

**`AlgebraicGeometry.Space.preservesInjectiveObjects_modulePushforward_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatAffineCohomologyCollapse.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatAffineCohomologyCollapse.lean#L53). The attribute's comment: “for a flat morphism of algebraic spaces, on the small étale ringed topoi”. References: SGA 4 V (4.9), “clause 3”.

> The direct image along a flat morphism `f : X ⟶ Y` of algebraic spaces carries injective
> `𝒪_X`-modules to injective `𝒪_Y`-modules.

```lean
theorem preservesInjectiveObjects_modulePushforward_of_isFlat (f : X ⟶ Y)
    (hf : IsFlat B S hS f.hom) :
    (modulePushforward B S hS f).PreservesInjectiveObjects
```

**`AlgebraicGeometry.RingedToposHom.pushforwardModules_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FlatMorphisms/PushforwardInjective.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FlatMorphisms/PushforwardInjective.lean#L72). References: SGA 4 V (4.9), “clause 3”.

> **Stacks 0730.** The direct image of a sheaf of modules along a *flat* morphism of ringed
> topoi is injective whenever the sheaf is.

```lean
theorem pushforwardModules_injective {X : RingedTopos.{v, u, w}} {Y : RingedTopos.{v', u', w}}
    [X.J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{w}]
    [HasWeakSheafify X.J AddCommGrpCat.{w}]
    (f : RingedToposHom X Y) (hf : f.IsFlat)
    (I : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) [Injective I] :
    Injective (f.pushforwardModules.obj I)
```

## Tag 0731, a lemma

[Tag 0731](https://stacks.math.columbia.edu/tag/0731) in the Stacks Project.

**`Stacks.Cohomology.rightAcyclic_pushforwardModules_of_isTotallyAcyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/TotallyAcyclicDirectImage.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/TotallyAcyclicDirectImage.lean#L259). The attribute's comment: “part (4): direct images”. References: SGA 4 V (5.2), “totally acyclic modules”.

> **Stacks 0731, part (4).** A sheaf of modules whose underlying abelian sheaf is totally
> acyclic is right acyclic for the direct image along a morphism of ringed topoi.

```lean
theorem rightAcyclic_pushforwardModules_of_isTotallyAcyclic
    [HasDerivedCategory.{u} (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    [HasDerivedCategory.{u} (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))]
    (N : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hN : IsTotallyAcyclic X.J
      ((SheafOfModules.toSheaf (Stacks.SheafOfModules.Tensor.ringSheaf X.O)).obj N)) :
    (pushforwardModules f).rightAcyclic N
```

**`Stacks.Cohomology.isTotallyAcyclic_rightAcyclic_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/TotallyAcyclicGlobalSections.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/TotallyAcyclicGlobalSections.lean#L340). The attribute's comment: “part (3): the functor of global sections”. References: SGA 4 V (4.6), “flasque ⇒ Γ-acyclic”.

> **Stacks 0731, part (3).** A sheaf of modules whose underlying abelian sheaf is totally
> acyclic is right acyclic for the functor of global sections.

```lean
theorem isTotallyAcyclic_rightAcyclic_globalSections
    (hM : IsTotallyAcyclic J ((SheafOfModules.toSheaf R).obj M))
    [HasDerivedCategory.{u} (SheafOfModules.{u} R)]
    [HasDerivedCategory.{u} (ModuleCat.{u} (RingCat.sectionsSubring R.obj))] :
    (SiteModules.globalSectionsFunctor R).rightAcyclic M
```

**`Stacks.Cohomology.GlobalSectionsLargeSite.isZero_rightDerived_globalSectionsFunctor_of_isTotallyAcyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/TotallyAcyclicGlobalSectionsLargeSite.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/TotallyAcyclicGlobalSectionsLargeSite.lean#L181). The attribute's comment: “part (3): the functor of global sections, on a site whose objects need not be small”.

> **Stacks 0731, part (3), on a site whose objects need not be small.** A sheaf of modules
> whose underlying abelian sheaf is totally acyclic has vanishing higher right derived global
> sections.
>
> Global sections, forgotten to abelian groups, are `Hom(ℤ_e, -)` of the underlying abelian sheaf
> (`globalSectionsCorepresentation`); the forgetful functor is exact and carries injective modules
> to `Hom(ℤ_e, -)`-acyclic sheaves, so the derived functors of the composite are those of
> `Hom(ℤ_e, -)`, that is `Ext(ℤ_e, -)`, at the underlying abelian sheaf; and total acyclicity at
> the terminal sheaf `e` is the vanishing of exactly those.

```lean
theorem isZero_rightDerived_globalSectionsFunctor_of_isTotallyAcyclic
    (M : SheafOfModules.{u} R)
    (hM : IsTotallyAcyclic J ((SheafOfModules.toSheaf R).obj M)) (n : ℕ)
    (hn : 0 < n) :
    IsZero (((globalSectionsFunctor.{u', u, u, u} R).rightDerived n).obj M)
```

**`Stacks.Cohomology.rightAcyclic_evaluation_of_isTotallyAcyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/TotallyAcyclicSections.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/TotallyAcyclicSections.lean#L242). The attribute's comment: “part (1): the functor H^0(U, -) of sections over an object of the site”.

> **Stacks 0731, part (1).** A sheaf of modules whose underlying abelian sheaf is totally
> acyclic is right acyclic for the functor `H^0(U, -)` of sections over an object of the site.

```lean
theorem rightAcyclic_evaluation_of_isTotallyAcyclic (X : Cᵒᵖ)
    [HasDerivedCategory.{u} (ModuleCat.{u} (R.obj.obj X))]
    (N : SheafOfModules.{u} R)
    (hN : IsTotallyAcyclic J ((SheafOfModules.toSheaf R).obj N)) :
    (SheafOfModules.evaluation R X).rightAcyclic N
```

**`Stacks.Cohomology.rightAcyclic_sectionsOverPresheaf_of_isTotallyAcyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/TotallyAcyclicSections.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/TotallyAcyclicSections.lean#L277). The attribute's comment: “part (2): the functor F ↦ F(K) of sections against a presheaf of sets”.

> **Stacks 0731, part (2).** A sheaf of modules whose underlying abelian sheaf is totally
> acyclic is right acyclic for the functor `F ↦ F(K)` of sections against a presheaf of sets.

```lean
theorem rightAcyclic_sectionsOverPresheaf_of_isTotallyAcyclic (K : Cᵒᵖ ⥤ Type u)
    [HasDerivedCategory.{u} AddCommGrpCat.{u}]
    (N : SheafOfModules.{u} R)
    (hN : IsTotallyAcyclic J ((SheafOfModules.toSheaf R).obj N)) :
    (sectionsOverPresheaf J R K).rightAcyclic N
```

**`Stacks.Cohomology.rightAcyclic_pushforwardModules_of_isTotallyAcyclic_largeSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RelativeLeraySpectralSequenceLargeSite.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RelativeLeraySpectralSequenceLargeSite.lean#L292). The attribute's comment: “part (4): direct images, with the two ringed topoi's object, morphism and section universes unrelated”.

> **Stacks 0731, part (4), with both ringed topoi's universes unconstrained.**  A sheaf of
> modules whose underlying abelian sheaf is totally acyclic is right acyclic for the direct image
> along a morphism of ringed topoi.
>
> `Stacks.Cohomology.rightAcyclic_pushforwardModules_of_isTotallyAcyclic` is this statement for
> two ringed topoi whose three universes are equal.  Here each site's objects, morphisms and
> sections lie at three unrelated universes, which is the seating of the small étale site of an
> algebraic space.  The proof is the original one: the totally acyclic modules form a class
> adapted to `f_*` in the sense of Stacks 05T8, and Stacks 05T8 says that every object of an
> adapted class is acyclic.

```lean
theorem rightAcyclic_pushforwardModules_of_isTotallyAcyclic_largeSite
    (N : SheafOfModules.{w} (ringSheaf X.O))
    (hN : IsTotallyAcyclic.{x} X.J
      ((SheafOfModules.toSheaf (ringSheaf X.O)).obj N)) :
    (pushforwardModules f).rightAcyclic N
```

**`Stacks.Cohomology.isZero_rightDerivedΓ_of_isTotallyAcyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InverseSystem/GlobalSectionsAcyclicityOfColimitOfFiniteSites.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InverseSystem/GlobalSectionsAcyclicityOfColimitOfFiniteSites.lean#L166). The attribute's comment: “part (3) for an abelian sheaf, in the derived-functor spelling: a totally acyclic abelian sheaf has vanishing (Sheaf.Gamma J Ab).rightDerived p for p > 0. The tag's part (3) for a sheaf of MODULES, stated as right acyclicity of SiteModules.globalSectionsFunctor, is isTotallyAcyclic\_rightAcyclic\_globalSections; this is not that statement specialised, the abelian sheaf not being a module over the constant sheaf of rings. Parts (1), (2) and (4) are not here.”.

> **Part (3) of [Stacks, Tag 0731] for an abelian sheaf.** A totally acyclic abelian sheaf on a
> small site — one whose cohomology over every sheaf of sets vanishes in positive degrees,
> [Stacks, Tag 072Y] — has vanishing right derived global sections in every positive degree.
>
> No induction and no Čech argument is involved: total acyclicity is vanishing of
> `Ext^p(**Z**_K^♯, -)` for *every* sheaf of sets `K`, so it suffices to take `K` to be the terminal
> sheaf. The free abelian sheaf on the terminal sheaf is the constant sheaf on `ℤ`
> (`ColimitsOfCohomology.freeAbelianSheafTerminalIsoConstantSheaf`), `Ext` out of that is
> `CategoryTheory.Sheaf.functorH`, and that is the right derived functor of global sections
> (`ColimitsOfCohomology.globalSectionsRightDerivedIsoFunctorH`).
>
> The library's `isTotallyAcyclic_rightAcyclic_globalSections` is the same part of the same tag for a
> sheaf of *modules*, stated as right acyclicity of `SiteModules.globalSectionsFunctor`; it does not
> specialise to an abelian sheaf, an injective object of `Sheaf J Ab` not being an injective module
> over the constant sheaf of rings `ℤ`.

```lean
theorem isZero_rightDerivedΓ_of_isTotallyAcyclic {C : Type u} [SmallCategory C]
    (J : GrothendieckTopology C) (F : Sheaf J Ab.{u}) (hF : IsTotallyAcyclic.{u} J F)
    (p : ℕ) (hp : 0 < p) :
    IsZero (((Sheaf.Γ J Ab.{u}).rightDerived p).obj F)
```

## Tag 08J6, a remark

[Tag 08J6](https://stacks.math.columbia.edu/tag/08J6) in the Stacks Project.

**`Stacks.Cohomology.Leray.derivedGlobalSectionsPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/LeraySpectralSequence.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/LeraySpectralSequence.lean#L242). The attribute's comment: “the identification RΓ(D, Rf\_*F) = RΓ(C, F), read in abelian groups”.

> **Stacks 08J6**, read in abelian groups: `RΓ(C, F) = RΓ(D, Rf_*F)`.
>
> The source's remark observes that [Stacks, Tag 015M] applies to the composition
> `Γ(C, -) = Γ(D, -) ∘ f_*`, because the direct image of an injective module is totally acyclic
> (Stacks 072Z) and a totally acyclic module is acyclic for global sections (Stacks 0731). This
> is that application: the canonical map `R(Γ(D, -) ∘ f_*) ⟶ RΓ(D, -) ∘ Rf_*` is invertible, and
> `Γ(C, -) ≅ Γ(D, -) ∘ f_*` carries the left hand side to `RΓ(C, -)`. The statement is an
> isomorphism of functors on `D⁺(Mod(O_C))`, so it holds in particular at a single module placed
> in degree zero, which is the form the remark displays.

```lean
def derivedGlobalSectionsPushforwardIso :
    (globalSectionsAb X).rightDerivedFunctorPlus ≅
      (pushforwardModules f).rightDerivedFunctorPlus ⋙
        (globalSectionsAb Y).rightDerivedFunctorPlus
```

## Tag 0732, a lemma

[Tag 0732](https://stacks.math.columbia.edu/tag/0732) in the Stacks Project.

**`Stacks.Cohomology.Leray.exists_leraySpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/LeraySpectralSequence.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/LeraySpectralSequence.lean#L273). The attribute's comment: “read in abelian groups”. References: EGA 0 (12.2.4), “special case”; SGA 4 V (5.3), “more general”; SGA 4 VII (1.5), “more general”; SGA 4½ Arcata (2.3.3), “more general”.

> **Stacks 0732, the Leray spectral sequence**, read in abelian groups. Let
> `f : (Sh(C), O_C) → (Sh(D), O_D)` be a morphism of ringed topoi and `F^•` a bounded below
> complex of `O_C`-modules, i.e. an object of `D⁺(Mod(O_C))`. There is a spectral sequence with
>
> `E_2^{p,q} = H^p(D, R^q f_*(F^•))`
>
> converging to `H^{p+q}(C, F^•)`.
>
> This is the Grothendieck spectral sequence
> `CategoryTheory.Functor.exists_spectralSequence_rightDerivedFunctorPlus_comp`
> ([Stacks, Tag 015N]) of the composition `Γ(C, -) = Γ(D, -) ∘ f_*`, whose hypothesis is
> `Stacks.Cohomology.Leray.rightAcyclic_globalSectionsAb_pushforward_of_injective`; its abutment
> `H^n(R(Γ(D, -) ∘ f_*)(F^•))` is identified with `H^n(C, F^•)` by
> `Stacks.Cohomology.Leray.derivedGlobalSectionsPushforwardIso`, and convergence is read off the
> degreewise finiteness of the filtration of the total complex by
> `CochainComplex.Filtered.abutsTo_of_isDegreewiseFinite`.

```lean
theorem exists_leraySpectralSequence
    (K : DerivedCategory.Plus (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) :
    ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{u} 0,
      (∀ p q : ℤ, Nonempty ((E.page 2 zero_le_two).X (p, q) ≅
        ((globalSectionsAb Y).rightDerivedPlus p).obj
          ((DerivedCategory.Plus.homologyFunctor
            (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) q).obj
              ((pushforwardModules f).rightDerivedFunctorPlus.obj K)))) ∧
      SpectralSequence.AbutsTo E (fun n =>
        (DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{u} n).obj
          ((globalSectionsAb X).rightDerivedFunctorPlus.obj K))
```

## Tag 0733, a lemma

[Tag 0733](https://stacks.math.columbia.edu/tag/0733) in the Stacks Project.

**`AlgebraicGeometry.Space.cohomologyPushforwardIsoOfIsFlatOfIsAffineHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatAffineCohomologyPullback.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatAffineCohomologyPullback.lean#L121). The attribute's comment: “part (1), for a flat affine morphism of algebraic spaces on the small étale ringed sites, as a chosen isomorphism and with nothing carried”.

> For a flat affine `f : X ⟶ Y` and a quasi-coherent `𝒪_X`-module `𝓕`, `H^i(X, 𝓕) ≅ H^i(Y, f_*𝓕)`
> in every degree, as `Γ(Y, 𝒪_Y)`-modules, the scalars of the left-hand side being restricted along
> the ring map `Γ(Y, 𝒪_Y) ⟶ Γ(X, 𝒪_X)`.

```lean
def cohomologyPushforwardIsoOfIsFlatOfIsAffineHom (f : X ⟶ Y) (haff : IsAffineHom B S hS f.hom)
    (hflat : IsFlat B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) (i : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    have := enoughInjectives_modules B S hS Y.1 Y.2
    ((globalSectionsRestrictScalars B S hS f).obj
        (((globalSectionsFunctor.{u + 1, u, u, u}
          (ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O)).rightDerived i).obj F) ≅
      ((globalSectionsFunctor.{u + 1, u, u, u}
          (ringSheaf (smallEtaleRingedSite B S hS Y.1 Y.2).O)).rightDerived i).obj
        ((modulePushforward B S hS f).obj F))
```

**`Stacks.Cohomology.Leray.nonempty_cohomologyIso_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/LerayCollapse.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/LerayCollapse.lean#L249). The attribute's comment: “part (1)”. References: SGA 4½ Arcata (2.3.5), “H^p(X,F)=H^p(Y,f\_*F)”.

> **Stacks 0733, part (1).** Let `f : (Sh(C), O_C) → (Sh(D), O_D)` be a morphism of ringed
> topoi and `F` an `O_C`-module. If `R^q f_* F = 0` for `q > 0`, then
> `H^p(C, F) = H^p(D, f_* F)` for all `p`, as modules over `Γ(D, O_D)` once the scalars of the left
> hand side are restricted along the comparison `Γ(D, O_D) ⟶ Γ(C, O_C)` of global section rings.

```lean
theorem nonempty_cohomologyIso_pushforward
    (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hF : ∀ q, 0 < q → IsZero (((pushforwardModules f).rightDerived q).obj F))
    (p : ℕ) :
    Nonempty ((ModuleCat.restrictScalars (globalSectionsRingHom f)).obj
        ((globalModuleCohomology.{u, u, u, u}
          (Stacks.SheafOfModules.Tensor.ringSheaf X.O) p).obj F) ≅
      (globalModuleCohomology.{u, u, u, u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) p).obj
        ((pushforwardModules f).obj F))
```

**`Stacks.Cohomology.Leray.nonempty_cohomologyIso_globalSections_higherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/LerayCollapse.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/LerayCollapse.lean#L273). The attribute's comment: “part (2)”.

> **Stacks 0733, part (2).** Let `f : (Sh(C), O_C) → (Sh(D), O_D)` be a morphism of ringed
> topoi and `F` an `O_C`-module. If `H^p(D, R^q f_* F) = 0` for all `q` and all `p > 0`, then
> `H^q(C, F) = H^0(D, R^q f_* F)` for all `q`, again after restricting the scalars of the left hand
> side along the comparison of global section rings. Degree-zero cohomology on the target is the
> module of global sections, by
> `Stacks.Cohomology.SiteModules.globalModuleCohomologyZeroIso`.

```lean
theorem nonempty_cohomologyIso_globalSections_higherDirectImage
    (F : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hcoh : ∀ q p, 0 < p →
      IsZero ((globalModuleCohomology.{u, u, u, u}
          (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) p).obj
        (((pushforwardModules f).rightDerived q).obj F)))
    (n : ℕ) :
    Nonempty ((ModuleCat.restrictScalars (globalSectionsRingHom f)).obj
        ((globalModuleCohomology.{u, u, u, u}
          (Stacks.SheafOfModules.Tensor.ringSheaf X.O) n).obj F) ≅
      (globalSectionsFunctor.{u, u, u, u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)).obj
        (((pushforwardModules f).rightDerived n).obj F))
```

## Tag 0734, a lemma

[Tag 0734](https://stacks.math.columbia.edu/tag/0734) in the Stacks Project.

**`Stacks.Cohomology.Leray.relativeLeraySpectralSequenceComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RelativeLeraySpectralSequenceFunctorial.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RelativeLeraySpectralSequenceFunctorial.lean#L313). The attribute's comment: “the spectral sequence for a module, functorial in the module, with its second page R^p g\_*(R^q f\_* F) and its functorial filtered abutment on R^\{p+q}(g ∘ f)\_* F”. References: SGA 4 V (5.3), “more general”; SGA 4½ Arcata (2.3.3), “more general”; SGA 4½ Th finitude (1.3), “more general”.

> **[Stacks, Tag 0734] for a module.** Let `f : (Sh(C), O_C) ⟶ (Sh(D), O_D)` and
> `g : (Sh(D), O_D) ⟶ (Sh(E), O_E)` be morphisms of ringed topoi and let `F` be an
> `O_C`-module. There is a spectral sequence with
>
> `E_2^{p,q} = R^p g_*(R^q f_* F)`
>
> converging to `R^{p+q}(g ∘ f)_* F`, **functorial in `F`**: the spectral sequence is a functor
> of `F`, its second-page identification is an isomorphism of functors, and the finite filtration
> of the abutment together with the identification of its graded pieces with the terms of the
> infinity page is natural in `F`.
>
> This is `relativeLeraySpectralSequence` for the canonical composite of `f` and `g`
> (part (3) of [Stacks, Tag 01D3]), for which the comparison of direct images is the identity.

```lean
def relativeLeraySpectralSequenceComp :
    RelativeLeraySpectralSequenceData f.toRingedToposModulesHom g.toRingedToposModulesHom
      (g.comp f).toRingedToposModulesHom
```

**`Stacks.Cohomology.Leray.relativeLeraySpectralSequencePlusComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RelativeLeraySpectralSequenceFunctorial.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RelativeLeraySpectralSequenceFunctorial.lean#L331). The attribute's comment: “the version for bounded below complexes of modules, functorial in the complex, with its second page R^p g\_*(H^q(Rf\_* K)) and its functorial filtered abutment on H^\{p+q}(R(g ∘ f)\_* K)”. References: EGA 0 (12.2.4); SGA 4 V (5.4).

> **[Stacks, Tag 0734] for a bounded below complex**, the "version for bounded below
> complexes of `O_C`-modules" the source asserts alongside the module case. For `f` and `g` as
> above and `K` an object of `D⁺(Mod(O_C))` there is a spectral sequence with
>
> `E_2^{p,q} = R^p g_*(H^q(Rf_* K))`
>
> converging to `H^{p+q}(R(g ∘ f)_* K)`, **functorial in `K`** in the same three senses.
>
> This is `relativeLeraySpectralSequencePlus` for the canonical composite of `f` and `g`.

```lean
def relativeLeraySpectralSequencePlusComp :
    RelativeLeraySpectralSequencePlusData f.toRingedToposModulesHom
      g.toRingedToposModulesHom (g.comp f).toRingedToposModulesHom
```

**`Stacks.Cohomology.Leray.exists_relativeLeraySpectralSequence_largeSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RelativeLeraySpectralSequenceLargeSite.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Modules/RelativeLeraySpectralSequenceLargeSite.lean#L424). The attribute's comment: “the spectral sequence, its second page and its convergence, for a bounded below complex, with the three ringed topoi's object, morphism and section universes unrelated; the functoriality in F is not covered”. References: EGA 0 (12.2.4); SGA 4 V (5.4); SGA 4 V (5.3), “more general”; SGA 4½ Arcata (2.3.4), “more general”.

> **Stacks 0734, the relative Leray spectral sequence, with the three ringed topoi's object,
> morphism and section universes unrelated.**  Let `f : (Sh(C), O_C) ⟶ (Sh(D), O_D)` and
> `g : (Sh(D), O_D) ⟶ (Sh(E), O_E)` be morphisms of ringed topoi, let `g ∘ f` be presented as
> their composite by a comparison `τ` of the geometric direct images, and let `F^•` be an object
> of `D⁺(Mod(O_C))`.  There is a spectral sequence with
>
> `E_2^{p,q} = R^p g_*(R^q f_*(F^•))`
>
> converging to `R^{p+q}(g ∘ f)_*(F^•)`.
>
> `Stacks.Cohomology.Leray.exists_relativeLeraySpectralSequence` is this statement for three
> ringed topoi whose three universes are equal.  Here each site's objects may lie above its
> morphisms and its sheaves, as they do on the small étale site of an algebraic space.  The
> acyclicity input is
> `Stacks.Cohomology.Leray.rightAcyclic_pushforwardModules_pushforward_of_injective_largeSite`,
> i.e. Stacks 072Z followed by part (4) of Stacks 0731; the statement is for a bounded below
> complex, which is the "version for bounded below complexes" the source also asserts, the
> single-module case being the image of a module placed in degree zero.
>
> The tag carries a qualifier because the source additionally asserts that the spectral sequence
> is **functorial in `F`**, and that clause is outside this statement: it produces a spectral
> sequence for one object of `D⁺(Mod(O_C))` at a time.  See the section "Functoriality in `F` is
> not covered" in the module documentation for what the obstruction is and for
> `Stacks.Cohomology.Leray.derivedPushforwardCompIso_largeSite`, the natural identification of the
> abutment, which is the part of the clause that is available.

```lean
theorem exists_relativeLeraySpectralSequence_largeSite
    (K : DerivedCategory.Plus (SheafOfModules.{w} (ringSheaf X.O))) :
    ∃ E : CohomologicalSpectralSequence (SheafOfModules.{w''} (ringSheaf Z.O)) 0,
      (∀ p q : ℤ, Nonempty ((E.page 2 zero_le_two).X (p, q) ≅
        ((pushforwardModules g).rightDerivedPlus p).obj
          ((DerivedCategory.Plus.homologyFunctor
            (SheafOfModules.{w'} (ringSheaf Y.O)) q).obj
              ((pushforwardModules f).rightDerivedFunctorPlus.obj K)))) ∧
      SpectralSequence.AbutsTo E (fun n =>
        (DerivedCategory.Plus.homologyFunctor
          (SheafOfModules.{w''} (ringSheaf Z.O)) n).obj
            ((pushforwardModules gf).rightDerivedFunctorPlus.obj K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.14, Tag 072X](https://stacks.math.columbia.edu/tag/072X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

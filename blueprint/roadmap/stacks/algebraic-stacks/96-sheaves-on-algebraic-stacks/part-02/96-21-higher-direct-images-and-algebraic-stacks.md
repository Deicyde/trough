---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.exists_etaleDirectImageSpectralSequence, AlgebraicGeometry.Stack.AlgebraicStacks.exists_etaleModuleDirectImageSpectralSequence, AlgebraicGeometry.Stack.AlgebraicStacks.exists_fppfDirectImageSpectralSequence, AlgebraicGeometry.Stack.AlgebraicStacks.exists_fppfModuleDirectImageSpectralSequence, AlgebraicGeometry.Stack.AlgebraicStacks.exists_etaleDirectImageSpectralSequenceData, AlgebraicGeometry.Stack.AlgebraicStacks.exists_fppfDirectImageSpectralSequenceData, AlgebraicGeometry.Stack.derivedDirectImageIsoSheafifyDerivedPresheafDirectImage, AlgebraicGeometry.Stack.higherDirectImageIsoSheafifyFibreCohomology
statement: formalized
proof: formalized
---

# 96.21 Higher direct images and algebraic stacks

Section 96.21 of the Stacks Project, [Tag 072F](https://stacks.math.columbia.edu/tag/072F). 3 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 072G, a proposition

[Tag 072G](https://stacks.math.columbia.edu/tag/072G) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_etaleDirectImageSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/PresentationDirectImageSpectralSequence.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/PresentationDirectImageSpectralSequence.lean#L123). The attribute's comment: “part (1)(a): spectral sequence in Ab(𝒴\_étale) along a smooth surjective presentation”.

> Let `f : 𝒰 ⟶ 𝒳` and `g : 𝒳 ⟶ 𝒴` be composable `1`-morphisms of algebraic stacks and assume `f`
> is representable by algebraic spaces, surjective and smooth. For an abelian sheaf `𝓕` on the étale
> site of `𝒳` there is a first-quadrant spectral sequence of abelian sheaves on the étale site of `𝒴`
> `E₁^{p,q} = R^q (g ∘ fₚ)_* fₚ⁻¹𝓕 ⇒ R^{p+q} g_* 𝓕`,
> all higher direct images computed in the étale topology, where `𝒰ₚ` is the degree `p` term of the
> relative Čech nerve of `f`, that is the `(p+1)`-fold fibre product of `𝒰` over `𝒳`, and `fₚ` its
> projection to `𝒳`. The first page, the first-quadrant vanishing and the abutment are the fields of
> `Stacks.RelativeCech.PushforwardSpectralSequenceData`.

```lean
theorem exists_etaleDirectImageSpectralSequence
    (hrep : Stack.IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (hsurj : Stack.IsSurjective B S hS f) (hsmooth : IsSmooth B S hS f)
    (𝓕 : Sheaf (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p SiteKind.etale)
      AddCommGrpCat.{max (u + 1) a}) :
    Nonempty (Stacks.RelativeCech.PushforwardSpectralSequenceData B S hS 𝒳.val.val.p
      𝒴.val.val.p (CatFiberedInGroupoids.homFunctor f.hom)
      (CatFiberedInGroupoids.homFunctor g.hom) SiteKind.etale 𝓕)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_etaleModuleDirectImageSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/PresentationDirectImageSpectralSequence.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/PresentationDirectImageSpectralSequence.lean#L144). The attribute's comment: “part (1)(b): spectral sequence in Mod(𝒴\_étale, 𝒪\_𝒴) along a smooth surjective presentation”.

> Let `f : 𝒰 ⟶ 𝒳` and `g : 𝒳 ⟶ 𝒴` be composable `1`-morphisms of algebraic stacks and assume `f`
> is representable by algebraic spaces, surjective and smooth. For a sheaf of `𝒪_𝒳`-modules `𝓕` on
> the étale site of `𝒳` there is a first-quadrant spectral sequence of sheaves of `𝒪_𝒴`-modules on
> the étale site of `𝒴`
> `E₁^{p,q} = R^q (g ∘ fₚ)_* fₚ⁻¹𝓕 ⇒ R^{p+q} g_* 𝓕`,
> all higher direct images computed in sheaves of modules for the étale topology, where `𝒰ₚ` is the
> degree `p` term of the relative Čech nerve of `f` and `fₚ` its projection to `𝒳`. The first page,
> the first-quadrant vanishing and the abutment are the fields of
> `Stacks.RelativeCech.ModulePushforwardSpectralSequenceData`.

```lean
theorem exists_etaleModuleDirectImageSpectralSequence
    (hrep : Stack.IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (hsurj : Stack.IsSurjective B S hS f) (hsmooth : IsSmooth B S hS f)
    (𝓕 : SheafOfModules.{max (u + 1) a} (Stacks.RelativeCech.moduleRingSheaf B S hS
      𝒳.val.val.p 𝒳.val.isFiberedInGroupoids SiteKind.etale)) :
    Nonempty (Stacks.RelativeCech.ModulePushforwardSpectralSequenceData.{u, u + 1, u + 1, u + 1,
      u, u, u, a} B S hS 𝒰.val.val.p 𝒳.val.val.p 𝒴.val.val.p
      (CatFiberedInGroupoids.homFunctor f.hom) (CatFiberedInGroupoids.homFunctor g.hom)
      SiteKind.etale 𝒰.val.isFiberedInGroupoids 𝒳.val.isFiberedInGroupoids
      𝒴.val.isFiberedInGroupoids
      (Functor.isFibredOneMorphism_of_isFiberedInGroupoids 𝒳.val.isFiberedInGroupoids
        f.hom.hom.w)
      (Functor.isFibredOneMorphism_of_isFiberedInGroupoids 𝒴.val.isFiberedInGroupoids
        g.hom.hom.w) 𝓕)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_fppfDirectImageSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/PresentationDirectImageSpectralSequence.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/PresentationDirectImageSpectralSequence.lean#L178). The attribute's comment: “part (2)(a): spectral sequence in Ab(𝒴) along a flat, locally finitely presented, surjective presentation”.

> Let `f : 𝒰 ⟶ 𝒳` and `g : 𝒳 ⟶ 𝒴` be composable `1`-morphisms of algebraic stacks and assume `f`
> is representable by algebraic spaces, surjective, flat and locally of finite presentation. For an
> abelian sheaf `𝓕` on the fppf site of `𝒳` there is a first-quadrant spectral sequence of abelian
> sheaves on the fppf site of `𝒴`
> `E₁^{p,q} = R^q (g ∘ fₚ)_* fₚ⁻¹𝓕 ⇒ R^{p+q} g_* 𝓕`,
> all higher direct images computed in the fppf topology, where `𝒰ₚ` is the degree `p` term of the
> relative Čech nerve of `f` and `fₚ` its projection to `𝒳`. The first page, the first-quadrant
> vanishing and the abutment are the fields of
> `Stacks.RelativeCech.PushforwardSpectralSequenceData`.

```lean
theorem exists_fppfDirectImageSpectralSequence
    (hrep : Stack.IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (hsurj : Stack.IsSurjective B S hS f) (hflat : IsFlat B S hS f)
    (hlfp : IsLocallyOfFinitePresentation B S hS f)
    (𝓕 : Sheaf (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p SiteKind.fppf)
      AddCommGrpCat.{max (u + 1) a}) :
    Nonempty (Stacks.RelativeCech.PushforwardSpectralSequenceData B S hS 𝒳.val.val.p
      𝒴.val.val.p (CatFiberedInGroupoids.homFunctor f.hom)
      (CatFiberedInGroupoids.homFunctor g.hom) SiteKind.fppf 𝓕)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_fppfModuleDirectImageSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/PresentationDirectImageSpectralSequence.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/PresentationDirectImageSpectralSequence.lean#L200). The attribute's comment: “part (2)(b): spectral sequence in Mod(𝒪\_𝒴) along a flat, locally finitely presented, surjective presentation”.

> Let `f : 𝒰 ⟶ 𝒳` and `g : 𝒳 ⟶ 𝒴` be composable `1`-morphisms of algebraic stacks and assume `f`
> is representable by algebraic spaces, surjective, flat and locally of finite presentation. For a
> sheaf of `𝒪_𝒳`-modules `𝓕` on the fppf site of `𝒳` there is a first-quadrant spectral sequence of
> sheaves of `𝒪_𝒴`-modules on the fppf site of `𝒴`
> `E₁^{p,q} = R^q (g ∘ fₚ)_* fₚ⁻¹𝓕 ⇒ R^{p+q} g_* 𝓕`,
> all higher direct images computed in sheaves of modules for the fppf topology, where `𝒰ₚ` is the
> degree `p` term of the relative Čech nerve of `f` and `fₚ` its projection to `𝒳`. The first page,
> the first-quadrant vanishing and the abutment are the fields of
> `Stacks.RelativeCech.ModulePushforwardSpectralSequenceData`.

```lean
theorem exists_fppfModuleDirectImageSpectralSequence
    (hrep : Stack.IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (hsurj : Stack.IsSurjective B S hS f) (hflat : IsFlat B S hS f)
    (hlfp : IsLocallyOfFinitePresentation B S hS f)
    (𝓕 : SheafOfModules.{max (u + 1) a} (Stacks.RelativeCech.moduleRingSheaf B S hS
      𝒳.val.val.p 𝒳.val.isFiberedInGroupoids SiteKind.fppf)) :
    Nonempty (Stacks.RelativeCech.ModulePushforwardSpectralSequenceData.{u, u + 1, u + 1, u + 1,
      u, u, u, a} B S hS 𝒰.val.val.p 𝒳.val.val.p 𝒴.val.val.p
      (CatFiberedInGroupoids.homFunctor f.hom) (CatFiberedInGroupoids.homFunctor g.hom)
      SiteKind.fppf 𝒰.val.isFiberedInGroupoids 𝒳.val.isFiberedInGroupoids
      𝒴.val.isFiberedInGroupoids
      (Functor.isFibredOneMorphism_of_isFiberedInGroupoids 𝒳.val.isFiberedInGroupoids
        f.hom.hom.w)
      (Functor.isFibredOneMorphism_of_isFiberedInGroupoids 𝒴.val.isFiberedInGroupoids
        g.hom.hom.w) 𝓕)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_etaleDirectImageSpectralSequenceData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/SmoothCoveringSpectralSequence.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/SmoothCoveringSpectralSequence.lean#L379). The attribute's comment: “part (1)(a): the étale spectral sequence for higher direct images along a smooth surjective presentation”.

> **Stacks 072G, part (1)(a).** Let `f : 𝒰 ⟶ 𝒳` and `g : 𝒳 ⟶ 𝒴` be composable `1`-morphisms of
> algebraic stacks and assume `f` is representable by algebraic spaces, surjective and smooth. For
> an abelian sheaf `𝓕` on the étale site of `𝒳` there is a first-quadrant spectral sequence of
> abelian sheaves on the étale site of `𝒴`
> `E₁^{p,q} = R^q (g ∘ fₚ)_* fₚ⁻¹𝓕 ⇒ R^{p+q} g_* 𝓕`,
> all higher direct images computed in the étale topology, where `𝒰ₚ` is the degree `p` term of the
> relative Čech nerve of `f`, that is the `(p+1)`-fold fibre product of `𝒰` over `𝒳`, and `fₚ` its
> projection to `𝒳`.

```lean
theorem exists_etaleDirectImageSpectralSequenceData
    (𝓕 : Sheaf (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p SiteKind.etale)
      AddCommGrpCat.{max (u + 1) a}) :
    Nonempty (Stacks.RelativeCech.PushforwardSpectralSequenceData B S hS 𝒳.val.val.p
      𝒴.val.val.p (CatFiberedInGroupoids.homFunctor f.hom)
      (CatFiberedInGroupoids.homFunctor g.hom) SiteKind.etale 𝓕)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_fppfDirectImageSpectralSequenceData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/SmoothCoveringSpectralSequence.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Cech/SmoothCoveringSpectralSequence.lean#L423). The attribute's comment: “part (2)(a): the fppf spectral sequence for higher direct images along a flat surjective presentation”.

> **Stacks 072G, part (2)(a).** Let `f : 𝒰 ⟶ 𝒳` and `g : 𝒳 ⟶ 𝒴` be composable `1`-morphisms of
> algebraic stacks and assume `f` is representable by algebraic spaces, surjective, flat and
> locally of finite presentation. For an abelian sheaf `𝓕` on the fppf site of `𝒳` there is a
> first-quadrant spectral sequence of abelian sheaves on the fppf site of `𝒴`
> `E₁^{p,q} = R^q (g ∘ fₚ)_* fₚ⁻¹𝓕 ⇒ R^{p+q} g_* 𝓕`,
> all higher direct images computed in the fppf topology, where `𝒰ₚ` is the degree `p` term of the
> relative Čech nerve of `f`, that is the `(p+1)`-fold fibre product of `𝒰` over `𝒳`, and `fₚ` its
> projection to `𝒳`.

```lean
theorem exists_fppfDirectImageSpectralSequenceData
    (𝓕 : Sheaf (BigFppfOver.associatedTopology B S hS 𝒳.val.val.p SiteKind.fppf)
      AddCommGrpCat.{max (u + 1) a}) :
    Nonempty (Stacks.RelativeCech.PushforwardSpectralSequenceData B S hS 𝒳.val.val.p
      𝒴.val.val.p (CatFiberedInGroupoids.homFunctor f.hom)
      (CatFiberedInGroupoids.homFunctor g.hom) SiteKind.fppf 𝓕)
```

## Tag 075G, a lemma

[Tag 075G](https://stacks.math.columbia.edu/tag/075G) in the Stacks Project.

**`AlgebraicGeometry.Stack.derivedDirectImageIsoSheafifyDerivedPresheafDirectImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImage.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImage.lean#L104). The attribute's comment: “abelian sheafification formula”.

> **Stacks 075G.** Higher direct image of abelian sheaves is the sheafification of the
> derived presheaf direct image.

```lean
noncomputable def derivedDirectImageIsoSheafifyDerivedPresheafDirectImage
    [p.IsFibered] [q.IsFibered] (hF : p.IsFibredOneMorphism q F) (n : ℕ)
    [∀ G : 𝒳ᵒᵖ ⥤ AddCommGrpCat.{a}, F.op.HasPointwiseRightKanExtension G]
    [HasSheafify (associatedTopology B S hS p τ) AddCommGrpCat.{a}]
    [HasSheafify (associatedTopology B S hS q τ) AddCommGrpCat.{a}]
    [HasInjectiveResolutions (Sheaf (associatedTopology B S hS p τ) AddCommGrpCat.{a})] :
    letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology (τ.over (B.obj hS))).2
    letI := additive_sheafPushforwardCocontinuous B S hS p q F τ hF
    (F.sheafPushforwardCocontinuous AddCommGrpCat.{a}
        (associatedTopology B S hS p τ) (associatedTopology B S hS q τ)).rightDerived n ≅
      derivedPresheafDirectImage B S hS p F τ n ⋙
        presheafToSheaf (associatedTopology B S hS q τ) AddCommGrpCat.{a}
```

**`AlgebraicGeometry.Stack.higherDirectImageIsoSheafifyFibreCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageFibreCohomology.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageFibreCohomology.lean#L348). The attribute's comment: “abelian sheaves: R^n f\_* F is the sheafification of y ↦ H^n((Sch/V) ×\_\{y,Y} X, pr^\{-1} F)”. References: SGA 4 V (5.1), “clause 1”.

> **Stacks 075G, abelian sheaves.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over
> `S` and `τ` one of the Zariski, étale, smooth, syntomic and fppf topologies. For an abelian sheaf
> `ℱ` on `𝒳_τ`, the higher direct image `Rⁿf_*ℱ` is the sheaf associated to the presheaf
> `y ↦ H^n_τ((Sch/V)_{fppf} ×_{y, 𝒴} 𝒳, pr⁻¹ℱ)`, `y` an object of `𝒴` lying over the scheme `V`.
>
> The direct image is right Kan extension followed by sheafification, and sheafification is exact
> (`abelianHigherDirectImage_iso_sheafify_fibreCohomology`); the derived presheaf direct image is
> computed objectwise (`CategoryTheory.Functor.rightDerivedFlipObjIso`), and its value at `y` is the
> cohomology of the 2-fibre product by Stacks 06W6 and Stacks 06X1
> (`derivedPresheafDirectImageEvaluationIso`).

```lean
def higherDirectImageIsoSheafifyFibreCohomology (n : ℕ)
    (F : Sheaf JX AddCommGrpCat.{max (u + 1) a}) :
    (((g).sheafPushforwardCocontinuous AddCommGrpCat.{max (u + 1) a} JX JY).rightDerived n).obj F ≅
      (presheafToSheaf JY AddCommGrpCat.{max (u + 1) a}).obj
        (objectFibreCohomologyPresheaf.{u, w, a} B S hS f c τ n F)
```

**`AlgebraicGeometry.Stack.moduleHigherDirectImageIsoSheafifyFibreModuleCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageFibreCohomologyScalars.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageFibreCohomologyScalars.lean#L350). The attribute's comment: “sheaves of modules: R^n f\_* F is, as an O\_Y-module, the sheafification of the presheaf of O\_Y-modules y ↦ H^n((Sch/V) ×\_\{y,Y} X, pr^\{-1} F)”.

> **Stacks 075G, sheaves of modules.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks
> over `S` and `τ` one of the Zariski, étale, smooth, syntomic and fppf topologies. For a sheaf `ℱ`
> of `𝒪_𝒳`-modules on `𝒳_τ`, the higher direct image `Rⁿf_*ℱ` is, as a sheaf of `𝒪_𝒴`-modules, the
> sheaf associated to the presheaf of `𝒪_𝒴`-modules `y ↦ H^n_τ((Sch/V)_{fppf} ×_{y, 𝒴} 𝒳, pr⁻¹ℱ)`,
> `y` an object of `𝒴` lying over the scheme `V`, the cohomology of the sheaf of modules `pr⁻¹ℱ`
> being an `𝒪_𝒴(y)`-module through the pullback of functions `𝒪_𝒴(y) ⟶ Γ(…, 𝒪)`.
>
> The direct image is the presheaf direct image followed by sheafification, which is exact
> (`moduleHigherDirectImageIsoSheafify`); evaluation at `y` is exact, and the sections over `y` of
> the presheaf direct image are the global sections over the 2-fibre product as `𝒪_𝒴(y)`-modules
> (`modulePresheafDirectImageEvaluationLinearIso`, Stacks 06W6), whose derived functors are the
> cohomology of the 2-fibre product because `pr⁻¹` preserves injectives (Stacks 06X2).

```lean
def moduleHigherDirectImageIsoSheafifyFibreModuleCohomology (n : ℕ)
    (F : SheafOfModules.{max (u + 1) a} OX) :
    ((moduleSheafPushforward.{u, u + 1, u, a, u + 1, u} B S hS 𝒳.val.val.p 𝒴.val.val.p
        𝒳.val.isFiberedInGroupoids 𝒴.val.isFiberedInGroupoids g
        (CatFiberedInGroupoids.homFunctor_comp_p f.hom) (B.baseTopology τ)
        (B.baseTopology_le_topology τ)).rightDerived n).obj F ≅
      (PresheafOfModules.sheafification.{max (u + 1) a} (𝟙 (OY).obj)).obj
        (objectFibreModuleCohomologyPresheafOfModules.{u, w, a} B S hS f c τ n F)
```

## Tag 075H, a lemma

[Tag 075H](https://stacks.math.columbia.edu/tag/075H) in the Stacks Project.

**`AlgebraicGeometry.Stack.abelianDirectImageBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChange.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChange.lean#L358). The attribute's comment: “degree zero, abelian sheaves: g⁻¹f\_*ℱ ≅ f'\_*(g')⁻¹ℱ”.

> **Stacks 075H in degree zero.** For the canonical 2-cartesian square of categories fibred in
> groupoids over the big fppf category of `S` and any topology `τ` on `B.Schemes`, the
> base-change map `g⁻¹f_*ℱ ⟶ f'_*(g')⁻¹ℱ` of abelian sheaves on the associated sites is an
> isomorphism, naturally in `ℱ`.
>
> This is the identification the source quotes from Stacks 075B at the start of the proof of
> Stacks 075H. Both composites become, on underlying presheaves, the two ways round the square of
> a right Kan extension and a restriction (Stacks 06NW), where they are identified by
> `AlgebraicGeometry.Stack.abelianPresheafBaseChangeIso`; the descent to sheaves is full
> faithfulness of `sheafToPresheaf`.

```lean
noncomputable def abelianDirectImageBaseChangeIso
    [p𝒳.IsFibered] [p𝒴'.IsFibered] [p𝒴.IsFibered]
    (h𝒳 : p𝒳.IsFiberedInGroupoids) (h𝒴' : p𝒴'.IsFiberedInGroupoids)
    (h𝒴 : p𝒴.IsFiberedInGroupoids) (hfc : f ⋙ p𝒴 = p𝒳) (hgc : g ⋙ p𝒴 = p𝒴')
    [∀ G : 𝒳ᵒᵖ ⥤ AddCommGrpCat.{a}, f.op.HasPointwiseRightKanExtension G]
    [∀ G : (TwoFibreProductOver p𝒳 p𝒴' p𝒴 f g)ᵒᵖ ⥤ AddCommGrpCat.{a},
      (TwoFibreProductOver.snd p𝒳 p𝒴' p𝒴 f g).op.HasPointwiseRightKanExtension G] :
    letI : (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g).IsFibered :=
      isFibered_twoFibreProductStructureFunctor p𝒳 p𝒴' p𝒴 f g h𝒳 h𝒴' h𝒴 hfc hgc
    letI := isCocontinuous_of_isFiberedInGroupoids B S hS p𝒳 p𝒴 f τ h𝒴 hfc
    letI := isContinuous_of_isFiberedInGroupoids B S hS p𝒴' p𝒴 g τ h𝒴 hgc
    letI := isContinuous_of_isFiberedInGroupoids B S hS
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) p𝒳
      (TwoFibreProductOver.fst p𝒳 p𝒴' p𝒴 f g) τ h𝒳 TwoFibreProductOver.fst_comp_eq
    letI := isCocontinuous_of_isFiberedInGroupoids B S hS
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) p𝒴'
      (TwoFibreProductOver.snd p𝒳 p𝒴' p𝒴 f g) τ h𝒴' TwoFibreProductOver.snd_comp_eq
    f.sheafPushforwardCocontinuous AddCommGrpCat.{a}
          (associatedTopology B S hS p𝒳 τ) (associatedTopology B S hS p𝒴 τ) ⋙
        g.sheafPushforwardContinuous AddCommGrpCat.{a}
          (associatedTopology B S hS p𝒴' τ) (associatedTopology B S hS p𝒴 τ) ≅
      (TwoFibreProductOver.fst p𝒳 p𝒴' p𝒴 f g).sheafPushforwardContinuous AddCommGrpCat.{a}
          (associatedTopology B S hS
            (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) τ)
          (associatedTopology B S hS p𝒳 τ) ⋙
        (TwoFibreProductOver.snd p𝒳 p𝒴' p𝒴 f g).sheafPushforwardCocontinuous
          AddCommGrpCat.{a}
          (associatedTopology B S hS
            (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) τ)
          (associatedTopology B S hS p𝒴' τ)
```

**`AlgebraicGeometry.Stack.abelianHigherDirectImageBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChange.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChange.lean#L438). The attribute's comment: “all degrees, abelian sheaves; Rⁱf'\_*(g')⁻¹ as the right derived functor of the composite f'\_* ∘ (g')⁻¹”.

> **Stacks 075H in every degree.** For the canonical 2-cartesian square of categories fibred
> in groupoids over the big fppf category of `S` and any topology `τ` on `B.Schemes`, the
> base-change map is an isomorphism
> `g⁻¹Rⁱf_*ℱ ≅ Rⁱ(f'_*(g')⁻¹)ℱ`
> of abelian sheaves on the associated site of `𝒴'`, naturally in `ℱ`.
>
> The right-hand side is the `i`-th right derived functor of the composite `f'_* ∘ (g')⁻¹`. The
> source writes instead `Rⁱf'_*((g')⁻¹ℱ)`, the `i`-th right derived functor of `f'_*` evaluated
> at `(g')⁻¹ℱ`; the two differ by whether `(g')⁻¹` sends injective abelian sheaves to
> `f'_*`-acyclic ones, which is not available here. See the implementation notes of this file.
>
> The proof uses nothing beyond the degree-zero isomorphism
> `AlgebraicGeometry.Stack.abelianDirectImageBaseChangeIso` and exactness of `g⁻¹` (Stacks 06NW):
> an exact functor may be pulled out of a right derived functor, so
> `(f_* ⋙ g⁻¹).rightDerived i ≅ (f_*).rightDerived i ⋙ g⁻¹`, and the degree-zero isomorphism
> rewrites the left-hand side.

```lean
noncomputable def abelianHigherDirectImageBaseChangeIso
    [p𝒳.IsFibered] [p𝒴'.IsFibered] [p𝒴.IsFibered]
    (h𝒳 : p𝒳.IsFiberedInGroupoids) (h𝒴' : p𝒴'.IsFiberedInGroupoids)
    (h𝒴 : p𝒴.IsFiberedInGroupoids) (hfc : f ⋙ p𝒴 = p𝒳) (hgc : g ⋙ p𝒴 = p𝒴') (n : ℕ)
    [∀ G : 𝒳ᵒᵖ ⥤ AddCommGrpCat.{a}, f.op.HasPointwiseRightKanExtension G]
    [∀ G : 𝒴'ᵒᵖ ⥤ AddCommGrpCat.{a}, g.op.HasPointwiseRightKanExtension G]
    [∀ G : (TwoFibreProductOver p𝒳 p𝒴' p𝒴 f g)ᵒᵖ ⥤ AddCommGrpCat.{a},
      (TwoFibreProductOver.snd p𝒳 p𝒴' p𝒴 f g).op.HasPointwiseRightKanExtension G]
    [HasSheafify (associatedTopology B S hS p𝒳 τ) AddCommGrpCat.{a}]
    [HasSheafify (associatedTopology B S hS p𝒴' τ) AddCommGrpCat.{a}]
    [HasSheafify (associatedTopology B S hS p𝒴 τ) AddCommGrpCat.{a}]
    [HasSheafify (associatedTopology B S hS
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) τ) AddCommGrpCat.{a}]
    [HasInjectiveResolutions
      (Sheaf (associatedTopology B S hS p𝒳 τ) AddCommGrpCat.{a})] :
    letI : (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g).IsFibered :=
      isFibered_twoFibreProductStructureFunctor p𝒳 p𝒴' p𝒴 f g h𝒳 h𝒴' h𝒴 hfc hgc
    letI := isCocontinuous_of_isFiberedInGroupoids B S hS p𝒳 p𝒴 f τ h𝒴 hfc
    letI := isContinuous_of_isFiberedInGroupoids B S hS p𝒴' p𝒴 g τ h𝒴 hgc
    letI := isContinuous_of_isFiberedInGroupoids B S hS
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) p𝒳
      (TwoFibreProductOver.fst p𝒳 p𝒴' p𝒴 f g) τ h𝒳 TwoFibreProductOver.fst_comp_eq
    letI := isCocontinuous_of_isFiberedInGroupoids B S hS
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) p𝒴'
      (TwoFibreProductOver.snd p𝒳 p𝒴' p𝒴 f g) τ h𝒴' TwoFibreProductOver.snd_comp_eq
    letI : (f.sheafPushforwardCocontinuous AddCommGrpCat.{a}
        (associatedTopology B S hS p𝒳 τ) (associatedTopology B S hS p𝒴 τ)).Additive :=
      additive_sheafPushforwardCocontinuous B S hS p𝒳 p𝒴 f τ (h𝒴.isFibredOneMorphism hfc)
    letI : ((TwoFibreProductOver.fst p𝒳 p𝒴' p𝒴 f g).sheafPushforwardContinuous
        AddCommGrpCat.{a}
        (associatedTopology B S hS
          (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) τ)
        (associatedTopology B S hS p𝒳 τ)).Additive :=
      additive_sheafPushforwardContinuous B S hS
        (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) p𝒳
        (TwoFibreProductOver.fst p𝒳 p𝒴' p𝒴 f g) τ
        (h𝒳.isFibredOneMorphism TwoFibreProductOver.fst_comp_eq)
    letI : ((TwoFibreProductOver.snd p𝒳 p𝒴' p𝒴 f g).sheafPushforwardCocontinuous
        AddCommGrpCat.{a}
        (associatedTopology B S hS
          (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) τ)
        (associatedTopology B S hS p𝒴' τ)).Additive :=
      additive_sheafPushforwardCocontinuous B S hS
        (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) p𝒴'
        (TwoFibreProductOver.snd p𝒳 p𝒴' p𝒴 f g) τ
        (h𝒴'.isFibredOneMorphism TwoFibreProductOver.snd_comp_eq)
    (f.sheafPushforwardCocontinuous AddCommGrpCat.{a}
            (associatedTopology B S hS p𝒳 τ)
            (associatedTopology B S hS p𝒴 τ)).rightDerived n ⋙
        g.sheafPushforwardContinuous AddCommGrpCat.{a}
          (associatedTopology B S hS p𝒴' τ) (associatedTopology B S hS p𝒴 τ) ≅
      ((TwoFibreProductOver.fst p𝒳 p𝒴' p𝒴 f g).sheafPushforwardContinuous AddCommGrpCat.{a}
            (associatedTopology B S hS
              (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) τ)
            (associatedTopology B S hS p𝒳 τ) ⋙
          (TwoFibreProductOver.snd p𝒳 p𝒴' p𝒴 f g).sheafPushforwardCocontinuous
            AddCommGrpCat.{a}
            (associatedTopology B S hS
              (TwoFibreProductOver.structureFunctor p𝒳 p𝒴' p𝒴 f g) τ)
            (associatedTopology B S hS p𝒴' τ)).rightDerived n
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.abelianHigherDirectImageBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChangeAlgebraicStacks.lean, line 938](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChangeAlgebraicStacks.lean#L938). The attribute's comment: “abelian sheaves: g⁻¹Rⁱf\_*F ≅ Rⁱf'\_*((g')⁻¹F) for every i, naturally in F”.

> **Stacks 075H for abelian sheaves.** Let `f : 𝒳 ⟶ 𝒴` and `g : 𝒴' ⟶ 𝒴` be 1-morphisms of
> algebraic stacks over `S`, with 2-cartesian square
> ```
> 𝒴' ×_𝒴 𝒳 --- g' ---> 𝒳
>    |                 |
>    f'                f
>    v                 v
>   𝒴' ------ g -----> 𝒴
> ```
> For every topology `τ` on the schemes of the big fppf site, the base change map is an
> isomorphism `g⁻¹Rⁱf_*ℱ ≅ Rⁱf'_*((g')⁻¹ℱ)` of abelian sheaves on `𝒴'_τ`, functorially in the
> abelian sheaf `ℱ` on `𝒳_τ`, for every `i`.

```lean
noncomputable def abelianHigherDirectImageBaseChangeIso {𝒳 𝒴 𝒴' : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴) (τ : GrothendieckTopology B.Schemes) (n : ℕ) :
    letI : (TwoFibreProductOver.structureFunctor 𝒳.val.val.p 𝒴'.val.val.p 𝒴.val.val.p
        (CatFiberedInGroupoids.homFunctor f.hom)
        (CatFiberedInGroupoids.homFunctor g.hom)).IsFibered :=
      isFibered_twoFibreProductStructureFunctor _ _ _ _ _ 𝒳.val.property 𝒴'.val.property
        𝒴.val.property (CatFiberedInGroupoids.homFunctor_comp_p f.hom)
        (CatFiberedInGroupoids.homFunctor_comp_p g.hom)
    letI : 𝒳.val.val.p.IsFibered := 𝒳.val.property.isFibered
    letI : 𝒴'.val.val.p.IsFibered := 𝒴'.val.property.isFibered
    letI : 𝒴.val.val.p.IsFibered := 𝒴.val.property.isFibered
    letI := isCocontinuous_of_isFiberedInGroupoids B S hS _ _
      (CatFiberedInGroupoids.homFunctor f.hom) τ 𝒴.val.property
      (CatFiberedInGroupoids.homFunctor_comp_p f.hom)
    letI := isContinuous_of_isFiberedInGroupoids B S hS _ _
      (CatFiberedInGroupoids.homFunctor g.hom) τ 𝒴.val.property
      (CatFiberedInGroupoids.homFunctor_comp_p g.hom)
    letI := isContinuous_of_isFiberedInGroupoids B S hS _ _
      (TwoFibreProductOver.fst 𝒳.val.val.p 𝒴'.val.val.p 𝒴.val.val.p
        (CatFiberedInGroupoids.homFunctor f.hom) (CatFiberedInGroupoids.homFunctor g.hom))
      τ 𝒳.val.property TwoFibreProductOver.fst_comp_eq
    letI := isCocontinuous_of_isFiberedInGroupoids B S hS _ _
      (TwoFibreProductOver.snd 𝒳.val.val.p 𝒴'.val.val.p 𝒴.val.val.p
        (CatFiberedInGroupoids.homFunctor f.hom) (CatFiberedInGroupoids.homFunctor g.hom))
      τ 𝒴'.val.property TwoFibreProductOver.snd_comp_eq
    letI : ((CatFiberedInGroupoids.homFunctor f.hom).sheafPushforwardCocontinuous
        AddCommGrpCat.{max (u + 1) a}
        (associatedTopology B S hS 𝒳.val.val.p τ)
        (associatedTopology B S hS 𝒴.val.val.p τ)).Additive :=
      additive_sheafPushforwardCocontinuous B S hS _ _ _ τ
        (𝒴.val.property.isFibredOneMorphism (CatFiberedInGroupoids.homFunctor_comp_p f.hom))
    letI : ((TwoFibreProductOver.snd 𝒳.val.val.p 𝒴'.val.val.p 𝒴.val.val.p
        (CatFiberedInGroupoids.homFunctor f.hom)
        (CatFiberedInGroupoids.homFunctor g.hom)).sheafPushforwardCocontinuous
        AddCommGrpCat.{max (u + 1) a}
        (associatedTopology B S hS (TwoFibreProductOver.structureFunctor 𝒳.val.val.p
          𝒴'.val.val.p 𝒴.val.val.p (CatFiberedInGroupoids.homFunctor f.hom)
          (CatFiberedInGroupoids.homFunctor g.hom)) τ)
        (associatedTopology B S hS 𝒴'.val.val.p τ)).Additive :=
      additive_sheafPushforwardCocontinuous B S hS _ _ _ τ
        (𝒴'.val.property.isFibredOneMorphism TwoFibreProductOver.snd_comp_eq)
    ((CatFiberedInGroupoids.homFunctor f.hom).sheafPushforwardCocontinuous
          AddCommGrpCat.{max (u + 1) a}
          (associatedTopology B S hS 𝒳.val.val.p τ)
          (associatedTopology B S hS 𝒴.val.val.p τ)).rightDerived n ⋙
        (CatFiberedInGroupoids.homFunctor g.hom).sheafPushforwardContinuous
          AddCommGrpCat.{max (u + 1) a}
          (associatedTopology B S hS 𝒴'.val.val.p τ)
          (associatedTopology B S hS 𝒴.val.val.p τ) ≅
      (TwoFibreProductOver.fst 𝒳.val.val.p 𝒴'.val.val.p 𝒴.val.val.p
          (CatFiberedInGroupoids.homFunctor f.hom)
          (CatFiberedInGroupoids.homFunctor g.hom)).sheafPushforwardContinuous
          AddCommGrpCat.{max (u + 1) a}
          (associatedTopology B S hS (TwoFibreProductOver.structureFunctor 𝒳.val.val.p
            𝒴'.val.val.p 𝒴.val.val.p (CatFiberedInGroupoids.homFunctor f.hom)
            (CatFiberedInGroupoids.homFunctor g.hom)) τ)
          (associatedTopology B S hS 𝒳.val.val.p τ) ⋙
        ((TwoFibreProductOver.snd 𝒳.val.val.p 𝒴'.val.val.p 𝒴.val.val.p
            (CatFiberedInGroupoids.homFunctor f.hom)
            (CatFiberedInGroupoids.homFunctor g.hom)).sheafPushforwardCocontinuous
            AddCommGrpCat.{max (u + 1) a}
            (associatedTopology B S hS (TwoFibreProductOver.structureFunctor 𝒳.val.val.p
              𝒴'.val.val.p 𝒴.val.val.p (CatFiberedInGroupoids.homFunctor f.hom)
              (CatFiberedInGroupoids.homFunctor g.hom)) τ)
            (associatedTopology B S hS 𝒴'.val.val.p τ)).rightDerived n
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.moduleHigherDirectImageBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChangeAlgebraicStacks.lean, line 1018](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChangeAlgebraicStacks.lean#L1018). The attribute's comment: “sheaves of modules: g⁻¹Rⁱf\_*F ≅ Rⁱf'\_*((g')⁻¹F) in Mod(O) for every i, naturally in F”.

> **Stacks 075H for sheaves of modules.** For 1-morphisms `f : 𝒳 ⟶ 𝒴` and `g : 𝒴' ⟶ 𝒴` of
> algebraic stacks over `S` with 2-cartesian square `𝒴' ×_𝒴 𝒳` as in
> `AlgebraicStacks.abelianHigherDirectImageBaseChangeIso`, and every topology `τ` coarser than the
> fppf topology, the base change map is an isomorphism `g^*Rⁱf_*ℱ ≅ Rⁱf'_*((g')^*ℱ)` of sheaves of
> `𝒪_{𝒴'}`-modules, functorially in the sheaf of `𝒪_𝒳`-modules `ℱ`, for every `i`; the higher
> direct images are the right derived functors on sheaves of modules.

```lean
noncomputable def moduleHigherDirectImageBaseChangeIso {𝒳 𝒴 𝒴' : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴) (τ : GrothendieckTopology B.Schemes) (hτ : τ ≤ B.topology)
    (n : ℕ) :
    (moduleSheafPushforward.{u, u + 1, u, max (u + 1) a} B S hS 𝒳.val.val.p 𝒴.val.val.p
          𝒳.val.property 𝒴.val.property (CatFiberedInGroupoids.homFunctor f.hom)
          (CatFiberedInGroupoids.homFunctor_comp_p f.hom) τ hτ).rightDerived n ⋙
        modulePullback B S hS 𝒴'.val.val.p 𝒴.val.val.p 𝒴'.val.property 𝒴.val.property
          (CatFiberedInGroupoids.homFunctor g.hom)
          (CatFiberedInGroupoids.homFunctor_comp_p g.hom) τ hτ ≅
      modulePullback B S hS (TwoFibreProductOver.structureFunctor 𝒳.val.val.p 𝒴'.val.val.p
          𝒴.val.val.p (CatFiberedInGroupoids.homFunctor f.hom)
          (CatFiberedInGroupoids.homFunctor g.hom)) 𝒳.val.val.p
          (TwoFibreProductOver.isFiberedInGroupoids _ _ _ _ _ 𝒳.val.property 𝒴'.val.property
            𝒴.val.property (CatFiberedInGroupoids.homFunctor_comp_p f.hom)
            (CatFiberedInGroupoids.homFunctor_comp_p g.hom)) 𝒳.val.property
          (TwoFibreProductOver.fst 𝒳.val.val.p 𝒴'.val.val.p 𝒴.val.val.p
            (CatFiberedInGroupoids.homFunctor f.hom) (CatFiberedInGroupoids.homFunctor g.hom))
          TwoFibreProductOver.fst_comp_eq τ hτ ⋙
        (moduleSheafPushforward.{u, u + 1, u, max (u + 1) a} B S hS
          (TwoFibreProductOver.structureFunctor 𝒳.val.val.p 𝒴'.val.val.p 𝒴.val.val.p
            (CatFiberedInGroupoids.homFunctor f.hom) (CatFiberedInGroupoids.homFunctor g.hom))
          𝒴'.val.val.p
          (TwoFibreProductOver.isFiberedInGroupoids _ _ _ _ _ 𝒳.val.property 𝒴'.val.property
            𝒴.val.property (CatFiberedInGroupoids.homFunctor_comp_p f.hom)
            (CatFiberedInGroupoids.homFunctor_comp_p g.hom)) 𝒴'.val.property
          (TwoFibreProductOver.snd 𝒳.val.val.p 𝒴'.val.val.p 𝒴.val.val.p
            (CatFiberedInGroupoids.homFunctor f.hom) (CatFiberedInGroupoids.homFunctor g.hom))
          TwoFibreProductOver.snd_comp_eq τ hτ).rightDerived n
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isIso_abelianDerivedDirectImageBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChangeMap.lean, line 640](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChangeMap.lean#L640). The attribute's comment: “abelian sheaves: the base change map g⁻¹Rf\_*F ⟶ Rf'\_*(g')⁻¹F is an isomorphism, functorially in F in D⁺(Ab(𝒳\_τ))”.

> **Stacks 075H for abelian sheaves.** Let `f : 𝒳 ⟶ 𝒴` and `g : 𝒴' ⟶ 𝒴` be 1-morphisms of
> algebraic stacks over `S`, with 2-cartesian square
> ```
> 𝒴' ×_𝒴 𝒳 --- g' ---> 𝒳
>    |                 |
>    f'                f
>    v                 v
>   𝒴' ------ g -----> 𝒴
> ```
> For every topology `τ` on the schemes of the big fppf site, the base change map
> `g⁻¹Rf_*ℱ ⟶ Rf'_*(g')⁻¹ℱ` (`AlgebraicGeometry.Stack.abelianDerivedDirectImageBaseChange`, the
> map of Stacks 0736 built from the adjunctions `f⁻¹ ⊣ f_*`, `f'⁻¹ ⊣ f'_*` and the 2-commutativity
> of the square) is an isomorphism, functorially in `ℱ` in the bounded below derived category of
> abelian sheaves on `𝒳_τ`; in particular for `ℱ` an abelian sheaf, placed in degree zero.

```lean
theorem isIso_abelianDerivedDirectImageBaseChange {𝒳 𝒴 𝒴' : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴) (τ : GrothendieckTopology B.Schemes) :
    IsIso (abelianDerivedDirectImageBaseChange.{u, a} B S hS _ _ _
      (CatFiberedInGroupoids.homFunctor f.hom) (CatFiberedInGroupoids.homFunctor g.hom) τ
      𝒳.val.property 𝒴'.val.property 𝒴.val.property
      (CatFiberedInGroupoids.homFunctor_comp_p f.hom)
      (CatFiberedInGroupoids.homFunctor_comp_p g.hom))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isIso_moduleDerivedDirectImageBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChangeMap.lean, line 663](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/HigherDirectImageBaseChangeMap.lean#L663). The attribute's comment: “sheaves of modules: the base change map g⁻¹Rf\_*F ⟶ Rf'\_*(g')⁻¹F is an isomorphism, functorially in F in D⁺(Mod(𝒳\_τ, O\_𝒳))”.

> **Stacks 075H for sheaves of modules.** For 1-morphisms `f : 𝒳 ⟶ 𝒴` and `g : 𝒴' ⟶ 𝒴` of
> algebraic stacks over `S` with 2-cartesian square `𝒴' ×_𝒴 𝒳` as in
> `AlgebraicGeometry.Stack.AlgebraicStacks.isIso_abelianDerivedDirectImageBaseChange`, and every
> topology `τ` coarser than the fppf topology, the base change map `g^*Rf_*ℱ ⟶ Rf'_*(g')^*ℱ`
> (`AlgebraicGeometry.Stack.moduleDerivedDirectImageBaseChange`) is an isomorphism, functorially in
> `ℱ` in the bounded below derived category of sheaves of `𝒪_𝒳`-modules on `𝒳_τ`; in particular for
> `ℱ` a sheaf of `𝒪_𝒳`-modules, placed in degree zero.

```lean
theorem isIso_moduleDerivedDirectImageBaseChange {𝒳 𝒴 𝒴' : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴' ⟶ 𝒴) (τ : GrothendieckTopology B.Schemes) (hτ : τ ≤ B.topology) :
    IsIso (moduleDerivedDirectImageBaseChange.{u, a} B S hS _ _ _
      (CatFiberedInGroupoids.homFunctor f.hom) (CatFiberedInGroupoids.homFunctor g.hom) τ hτ
      𝒳.val.property 𝒴'.val.property 𝒴.val.property
      (CatFiberedInGroupoids.homFunctor_comp_p f.hom)
      (CatFiberedInGroupoids.homFunctor_comp_p g.hom))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.21, Tag 072F](https://stacks.math.columbia.edu/tag/072F)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

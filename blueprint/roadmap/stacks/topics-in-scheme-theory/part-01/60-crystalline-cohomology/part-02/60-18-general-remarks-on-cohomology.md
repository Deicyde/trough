---
declaration: section
origin: cited
lean: Crystalline.GlobalCrystallineSituation.SmallSite.vanishing07JJ_abelianSheaf, Crystalline.GlobalCrystallineSituation.SmallSite.isZero_overCohomology_abelianSheaf_of_isAffine, Crystalline.GlobalCrystallineSituation.SmallSite.chaoticCohomologyComparisonIso, Crystalline.completedCrystallineToposMorphism, Crystalline.abelianSheafPushforwardIsoDirectImage, Crystalline.abelianSheafPushforwardForgetIsoPushforward, Crystalline.abelianDirectImageObjObjIsoLimitFiniteLevelSections, Crystalline.abelianSheafPushforwardObjObjIsoLimitFiniteLevelSections
statement: formalized
proof: formalized
---

# 60.18 General remarks on cohomology

Section 60.18 of the Stacks Project, [Tag 07JI](https://stacks.math.columbia.edu/tag/07JI). 4 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07JJ, a lemma

[Tag 07JJ](https://stacks.math.columbia.edu/tag/07JJ) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.vanishing07JJ_abelianSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/StandardCoverAcyclicity.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/StandardCoverAcyclicity.lean#L302). The attribute's comment: “the case of the objects (U, T, δ) whose ambient divided power scheme T is affine, in the packaged form SmallSite.Vanishing07JJ that the consumers of the tag in this library use, and for the abelian sheaf SmallSite.abelianSheaf F of the coefficient universe u + 1 attached to a locally quasi-coherent module F. The source's remaining case of U affine is reduced to this one in isZero\_overCohomology\_abelianSheaf\_of\_isAffine, which states both”.

> Let `F` be a locally quasi-coherent sheaf of `𝒪_{X/S}`-modules on the small crystalline site
> `Cris(X/S)` of a global crystalline situation. Then for every object `(U, T, δ)` of `Cris(X/S)`
> whose ambient divided power scheme `T` is affine, and every `p > 0`, the cohomology of the
> localized site vanishes:
>
> `H^p(Cris(X/S)/(U, T, δ), F) = 0`.
>
> The statement is about the abelian sheaf `SmallSite.abelianSheaf F` of the coefficient universe
> `u + 1`, which is the universe in which the cohomology of `Cris(X/S)` and of its localizations
> exists; the modules of `F` itself live in `Type u`.

```lean
theorem vanishing07JJ_abelianSheaf (F : SheafOfModules.{u} (structureSheaf S))
    (hF : IsLocallyQuasiCoherent F) : Vanishing07JJ S (abelianSheaf F)
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.isZero_overCohomology_abelianSheaf_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/StandardCoverAcyclicity.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/StandardCoverAcyclicity.lean#L323). The attribute's comment: “both cases of the hypothesis: the objects (U, T, δ) with T or U affine, for the abelian sheaf SmallSite.abelianSheaf F of the coefficient universe u + 1 attached to a locally quasi-coherent module F”.

> Let `F` be a locally quasi-coherent sheaf of `𝒪_{X/S}`-modules on the small crystalline site
> `Cris(X/S)` of a global crystalline situation. Then for every object `(U, T, δ)` of `Cris(X/S)`
> with `T` **or** `U` affine, and every `p > 0`, the cohomology of the localized site vanishes:
>
> `H^p(Cris(X/S)/(U, T, δ), F) = 0`.

```lean
theorem isZero_overCohomology_abelianSheaf_of_isAffine
    (F : SheafOfModules.{u} (structureSheaf S)) (hF : IsLocallyQuasiCoherent F)
    (A : CrystallineThickening S)
    (hA : IsAffine A.obj.thickening.target.scheme ∨ IsAffine A.obj.thickening.source)
    (p : ℕ) (hp : 0 < p) :
    IsZero ((overCohomologyFunctor S A p).obj ((restrictToOver S A).obj (abelianSheaf F)))
```

## Tag 07JK, a lemma

[Tag 07JK](https://stacks.math.columbia.edu/tag/07JK) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.chaoticCohomologyComparisonIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/ChaoticComparison.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/ChaoticComparison.lean#L113). The attribute's comment: “for the abelian sheaf SmallSite.abelianSheaf F of the coefficient universe u + 1 attached to a locally quasi-coherent sheaf F of 𝒪\_\{X/S}-modules, which is the generality in which the input [Stacks, Tag 07JJ] holds”.

> In Situation [Stacks, Tag 07MF] with `X` and `S` affine, let
> `𝒞 ⊆ Cris(X/S)` be the full subcategory of divided power thickenings `(X, T, δ)` of the whole of
> `X` with the chaotic topology of [Stacks, Tag 07GE].  Then for every locally quasi-coherent sheaf
> `F` of `𝒪_{X/S}`-modules on `Cris(X/S)` and every degree `j`,
>
> `H^j(𝒞, F|_𝒞) ≅ H^j(Cris(X/S), F)`.
>
> Both sides are read on the abelian sheaf `SmallSite.abelianSheaf F` of the coefficient universe
> `u + 1`.

```lean
def chaoticCohomologyComparisonIso (F : SheafOfModules.{u} (structureSheaf S))
    (hF : IsLocallyQuasiCoherent F) (j : ℕ) :
    (chaoticCohomologyFunctor S j).obj ((restrictToWhole S).obj (abelianSheaf F)) ≅
      (cohomologyFunctor S j).obj (abelianSheaf F)
```

## Tag 07JL, a lemma

[Tag 07JL](https://stacks.math.columbia.edu/tag/07JL) in the Stacks Project.

**`Crystalline.completedCrystallineToposMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineCrystallineSite/CompletedToposMorphism.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/AffineCrystallineSite/CompletedToposMorphism.lean#L170). The attribute's comment: “the morphism of topoi”.

> The morphism of topoi induced by the canonical functor from crystalline
> thickenings to completed crystalline thickenings.

```lean
public def completedCrystallineToposMorphism
    (S : AffineCrystallineSituation.{u, v}) :
    MorphismOfTopoi
      (Sheaf (⊥ : GrothendieckTopology (CrystallineThickening.{u, v, w} S)ᵒᵖ)
        (Type (max u v (w + 1))))
      (Sheaf (⊥ : GrothendieckTopology (CompletedCrystallineThickening.{u, v, w} S)ᵒᵖ)
        (Type (max u v (w + 1))))
```

**`Crystalline.abelianSheafPushforwardIsoDirectImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineCrystallineSite/CompletedToposMorphism.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/AffineCrystallineSite/CompletedToposMorphism.lean#L209). The attribute's comment: “identification of the abelian direct image”.

> The natural isomorphism identifying the abelian-sheaf pushforward induced by the
> crystalline site functor with the right Kan extension used to compute its derived
> functors. It comes from the uniqueness of right adjoints, and is an isomorphism of
> functors, not merely an objectwise comparison.

```lean
public noncomputable def abelianSheafPushforwardIsoDirectImage
    (S : AffineCrystallineSituation.{u, v}) :
    abelianSheafPushforward S ⋙
        (completedAbelianSheafEquivalence.{u, v, w} S).functor ≅
      (abelianSheafEquivalence.{u, v, w} S).functor ⋙ abelianDirectImage S
```

**`Crystalline.abelianSheafPushforwardForgetIsoPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineCrystallineSite/CompletedToposMorphism.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/AffineCrystallineSite/CompletedToposMorphism.lean#L244). The attribute's comment: “compatibility with the geometric morphism”.

> The natural isomorphism exhibiting the abelian-sheaf direct image, on underlying
> sets, as the direct image of the same morphism of topoi. It comes from the uniqueness
> of right adjoints, and is natural in the sheaf.

```lean
public noncomputable def abelianSheafPushforwardForgetIsoPushforward
    (S : AffineCrystallineSituation.{u, v}) :
    abelianSheafPushforward S ⋙
        sheafForget
          (⊥ : GrothendieckTopology (CompletedCrystallineThickening.{u, v, w} S)ᵒᵖ) ≅
      sheafForget
          (⊥ : GrothendieckTopology (CrystallineThickening.{u, v, w} S)ᵒᵖ) ⋙
        (completedCrystallineToposMorphism S).pushforward
```

**`Crystalline.abelianDirectImageObjObjIsoLimitFiniteLevelSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineCrystallineSite/CompletedToposMorphism.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/AffineCrystallineSite/CompletedToposMorphism.lean#L320). The attribute's comment: “the direct image computed as the limit over the finite levels”.

> **The direct image of [Stacks, Tag 07JL], computed.** For an abelian presheaf `F` on the
> ordinary affine crystalline category and a finite-level system `T` for a completed thickening
> `X`, the value at `X` of the direct image of `F` is the inverse limit of the sections of `F` on
> the finite-level quotients of `X`:
> `g_*(F)(X) ≅ lim_e F(X/(p)^(N + e))`.
>
> The direct image is the right Kan extension along `crystallineToCompleted`, whose value at `X`
> is the limit over the structured-arrow category, and the finite-level diagram is initial there
> by `Crystalline.finiteLevel_initial`.

```lean
public noncomputable def abelianDirectImageObjObjIsoLimitFiniteLevelSections
    {S : AffineCrystallineSituation.{u, v}}
    (F : CrystallineThickening.{u, v, w} S ⥤ Ab.{max u v (w + 1)})
    {X : CompletedCrystallineThickening.{u, v, w} S} (T : FiniteLevelSystem X) :
    ((abelianDirectImage S).obj F).obj X ≅ limit (finiteLevelSections T F)
```

**`Crystalline.abelianSheafPushforwardObjObjIsoLimitFiniteLevelSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineCrystallineSite/CompletedToposMorphism.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/AffineCrystallineSite/CompletedToposMorphism.lean#L340). The attribute's comment: “the sections of the direct image as the limit over the finite levels”.

> **The sections of the direct image of [Stacks, Tag 07JL].** The value at a completed
> thickening `X` of the direct image of an abelian sheaf `F` on the ordinary affine crystalline
> site is the inverse limit of the sections of `F` on the finite-level quotients of `X`.
>
> This is `Crystalline.abelianDirectImageObjObjIsoLimitFiniteLevelSections` transported along
> `Crystalline.abelianSheafPushforwardIsoDirectImage`, so that it speaks about the
> site-theoretic pushforward rather than the right Kan extension.

```lean
public noncomputable def abelianSheafPushforwardObjObjIsoLimitFiniteLevelSections
    (S : AffineCrystallineSituation.{u, v})
    (F : Sheaf (⊥ : GrothendieckTopology (CrystallineThickening.{u, v, w} S)ᵒᵖ)
      Ab.{max u v (w + 1)})
    {X : CompletedCrystallineThickening.{u, v, w} S} (T : FiniteLevelSystem X) :
    ((completedAbelianSheafEquivalence.{u, v, w} S).functor.obj
        ((abelianSheafPushforward S).obj F)).obj X ≅
      limit (finiteLevelSections T
        ((abelianSheafEquivalence.{u, v, w} S).functor.obj F))
```

**`Crystalline.rightDerivedPushforwardSectionsIsoRightDerivedLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CompletedHigherDirectImages.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CompletedHigherDirectImages.lean#L53). The attribute's comment: “the higher direct images as the derived limits over the finite levels”.

> For an abelian sheaf `𝓖` on `𝒞 = (Cris(C/A))ᵒᵖ`, a completed thickening `B` and every degree
> `p`, the sections over `B` of the `p`-th higher direct image of `𝓖` along the morphism of topoi
> `g : Sh(𝒞) ⟶ Sh(𝒞^∧)` are the `p`-th derived inverse limit of the sections of `𝓖` on the finite
> levels of `B`:
>
> `R ᵖ g_* 𝓖 (B) ≅ R ᵖ lim_e 𝓖(B/(p)^{N + e})`.

```lean
def rightDerivedPushforwardSectionsIsoRightDerivedLimit
    (𝓖 : Sheaf (littleChaoticTopology.{u, v, w} s) Ab.{max u v (w + 1)})
    (B : CompletedCrystallineThickening.{u, v, w} s) (p : ℕ) :
    ((completedAbelianSheafEquivalence.{u, v, w} s).functor.obj
        (((abelianSheafPushforward.{u, v, w} s).rightDerived p).obj 𝓖)).obj B ≅
      ((lim : Rlim.InvSystemAb.{max u v (w + 1)} ⥤ Ab.{max u v (w + 1)}).rightDerived p).obj
        (finiteLevelSections (uniformLevelSystem B)
          ((abelianSheafEquivalence.{u, v, w} s).functor.obj 𝓖))
```

**`Crystalline.rightDerivedOnePushforwardSectionsIsoRightDerivedOneLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CompletedHigherDirectImages.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CompletedHigherDirectImages.lean#L71). The attribute's comment: “the first higher direct image as the first derived limit over the finite levels”.

> `R ¹ g_* 𝓖 (B) ≅ R ¹ lim_e 𝓖(B_e)`: for an abelian sheaf `𝓖` on `𝒞 = (Cris(C/A))ᵒᵖ` and a
> completed thickening `B`, the sections over `B` of the first higher direct image of `𝓖` along the
> morphism of topoi `g : Sh(𝒞) ⟶ Sh(𝒞^∧)` are the first derived inverse limit of the inverse system
> `e ↦ 𝓖(B/(p)^{N + e})` of sections on the finite levels of `B`.

```lean
def rightDerivedOnePushforwardSectionsIsoRightDerivedOneLimit
    (𝓖 : Sheaf (littleChaoticTopology.{u, v, w} s) Ab.{max u v (w + 1)})
    (B : CompletedCrystallineThickening.{u, v, w} s) :
    ((completedAbelianSheafEquivalence.{u, v, w} s).functor.obj
        (((abelianSheafPushforward.{u, v, w} s).rightDerived 1).obj 𝓖)).obj B ≅
      ((lim : Rlim.InvSystemAb.{max u v (w + 1)} ⥤ Ab.{max u v (w + 1)}).rightDerived 1).obj
        (finiteLevelSections (uniformLevelSystem B)
          ((abelianSheafEquivalence.{u, v, w} s).functor.obj 𝓖))
```

**`Crystalline.isZero_rightDerived_abelianSheafPushforward_of_two_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CompletedHigherDirectImages.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CompletedHigherDirectImages.lean#L85). The attribute's comment: “the vanishing of the higher direct images in degrees at least two”.

> `R ᵖ g_* 𝓖 = 0` for every `p ≥ 2` and every abelian sheaf `𝓖` on `𝒞 = (Cris(C/A))ᵒᵖ`, where
> `g_*` is the direct image `Crystalline.abelianSheafPushforward` of the morphism of topoi
> `g : Sh(𝒞) ⟶ Sh(𝒞^∧)`.

```lean
theorem isZero_rightDerived_abelianSheafPushforward_of_two_le
    (𝓖 : Sheaf (littleChaoticTopology.{u, v, w} s) Ab.{max u v (w + 1)})
    (p : ℕ) (hp : 2 ≤ p) :
    IsZero (((abelianSheafPushforward.{u, v, w} s).rightDerived p).obj 𝓖)
```

## Tag 07JM, a lemma

[Tag 07JM](https://stacks.math.columbia.edu/tag/07JM) in the Stacks Project.

**`Stacks.Cohomology.derivedGlobalSectionsIsoPowerCechComplexExtend`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/ChaoticSiteCoveringObject.lean, line 584](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/ChaoticSiteCoveringObject.lean#L584).

> **Stacks Project, Tag 07JM.** Let `𝒞` carry the chaotic topology, let `X` be an object of
> `𝒞` to which every object of `𝒞` admits a morphism, and let `𝒞` have products of pairs. For every
> abelian sheaf `𝓕` on `𝒞` the total cohomology `RΓ(𝒞, 𝓕)` is represented by the complex
> `𝓕(X) → 𝓕(X × X) → 𝓕(X × X × X) → ⋯` associated to the cosimplicial abelian group
> `[n] ↦ 𝓕(X^{n + 1})`.
>
> This is the comparison itself, an isomorphism of complexes of abelian groups between
> `RΓ(𝒞, 𝓕)` and that complex placed in the nonnegative degrees. An isomorphism of complexes is
> sent to an isomorphism of `D(Ab)` by the localisation functor, which is
> `Stacks.Cohomology.derivedGlobalSectionsQIsoPowerCechComplexExtend`, and to the isomorphism of
> cohomology groups in each degree, which is
> `Stacks.Cohomology.sheafHAddEquivPowerCechComplexHomology`.

```lean
def derivedGlobalSectionsIsoPowerCechComplexExtend :
    chaoticDerivedGlobalSections X hX F ≅
      (powerCechComplex F.obj X).extend ComplexShape.embeddingUpNat
```

**`Stacks.Cohomology.derivedGlobalSectionsQIsoPowerCechComplexExtend`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/ChaoticSiteCoveringObject.lean, line 600](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/ChaoticSiteCoveringObject.lean#L600).

> **Stacks Project, Tag 07JM**, in the derived category of abelian groups: on the chaotic site
> with a covering object `X` and products of pairs, `RΓ(𝒞, 𝓕)` and the complex
> `𝓕(X) → 𝓕(X × X) → 𝓕(X × X × X) → ⋯` become isomorphic in `D(Ab)`.
>
> This is `Stacks.Cohomology.derivedGlobalSectionsIsoPowerCechComplexExtend` read through the
> localisation functor `CategoryTheory.DerivedCategory.Q`. The instance
> `HasDerivedCategory.{w} AddCommGrpCat.{u}` only chooses a model of `D(Ab)` with morphisms in a
> given universe; one always exists, by `CategoryTheory.HasDerivedCategory.standard`.

```lean
def derivedGlobalSectionsQIsoPowerCechComplexExtend
    [HasDerivedCategory.{w} AddCommGrpCat.{u}] :
    DerivedCategory.Q.obj (chaoticDerivedGlobalSections X hX F) ≅
      DerivedCategory.Q.obj ((powerCechComplex F.obj X).extend ComplexShape.embeddingUpNat)
```

**`Stacks.Cohomology.sheafHAddEquivPowerCechComplexHomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/ChaoticSiteCoveringObject.lean, line 614](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/ChaoticSiteCoveringObject.lean#L614).

> **Stacks Project, Tag 07JM** in degree `n`: the cohomology `H^n(𝒞, 𝓕)` of the chaotic site
> is the degree-`n` cohomology of the complex `𝓕(X) → 𝓕(X × X) → 𝓕(X × X × X) → ⋯`.
>
> This is `H^n` of `Stacks.Cohomology.derivedGlobalSectionsIsoPowerCechComplexExtend`, the
> cohomology of `RΓ(𝒞, 𝓕)` being `CategoryTheory.Sheaf.H` by
> `CategoryTheory.ProjectiveResolution.extAddEquivCohomologyClass`. It is the map whose existence
> `Stacks.Cohomology.nonempty_addEquiv_sheafH_homology_powerCechComplex` asserts.

```lean
def sheafHAddEquivPowerCechComplexHomology
    [HasExt.{u} (Sheaf (⊥ : GrothendieckTopology C) AddCommGrpCat.{u})] (n : ℕ) :
    Sheaf.H F n ≃+ (powerCechComplex F.obj X).homology n
```

**`Stacks.Cohomology.functorHObjIsoPowerCechComplexHomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/ChaoticSiteCoveringObject.lean, line 634](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/ChaoticSiteCoveringObject.lean#L634).

> **Stacks Project, Tag 07JM** in degree `n`, as an isomorphism of objects of
> `AddCommGrpCat`: the value at `𝓕` of Mathlib's cohomology functor `CategoryTheory.Sheaf.functorH`
> of the chaotic site is the degree-`n` cohomology of the complex
> `𝓕(X) → 𝓕(X × X) → 𝓕(X × X × X) → ⋯`.
>
> This is `Stacks.Cohomology.sheafHAddEquivPowerCechComplexHomology` read as a morphism of the
> category `AddCommGrpCat`, which is the form in which an isomorphism of cohomology groups is
> stated elsewhere in the library.

```lean
def functorHObjIsoPowerCechComplexHomology
    [HasExt.{u} (Sheaf (⊥ : GrothendieckTopology C) AddCommGrpCat.{u})] (n : ℕ) :
    (Sheaf.functorH (⊥ : GrothendieckTopology C) n).obj F ≅
      (powerCechComplex F.obj X).homology n
```

**`Stacks.Cohomology.nonempty_addEquiv_sheafH_homology_powerCechComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/ChaoticSiteCoveringObject.lean, line 682](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Acyclicity/ChaoticSiteCoveringObject.lean#L682).

> **Stacks Project, Tag 07JM.** Let `𝒞` carry the chaotic topology, let `X` be an object of
> `𝒞` to which every object of `𝒞` admits a morphism, and let the nonempty finite powers
> `X^{n + 1}` of `X` exist in `𝒞`. For every abelian sheaf `𝓕` on `𝒞` the total cohomology
> `RΓ(𝒞, 𝓕)` is represented by the complex `𝓕(X) → 𝓕(X × X) → 𝓕(X × X × X) → ⋯` associated to the
> cosimplicial abelian group `[n] ↦ 𝓕(X^{n + 1})`: in every degree the cohomology of the site
> agrees with the cohomology of that complex.
>
> The source asks `𝒞` to have products of pairs; the hypothesis here is the weaker one that the
> proof uses, and the source's implies it by `Stacks.Cohomology.hasProduct_fin_succ`.
>
> The comparison itself is `Stacks.Cohomology.addEquivSheafHHomologyPowerCechComplex`; this is
> that `def` read as an existence statement.

```lean
theorem nonempty_addEquiv_sheafH_homology_powerCechComplex
    [HasExt.{u} (Sheaf (⊥ : GrothendieckTopology C) AddCommGrpCat.{u})] (n : ℕ) :
    Nonempty (Sheaf.H F n ≃+ (powerCechComplex F.obj X).homology n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.18, Tag 07JI](https://stacks.math.columbia.edu/tag/07JI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

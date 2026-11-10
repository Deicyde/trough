---
declaration: section
origin: cited
lean: CategoryTheory.SemiRepresentable.LocalizationSites.localizationFunctor_isContinuous, CategoryTheory.SemiRepresentable.LocalizationSites.localizationFunctor_isCocontinuous, CategoryTheory.SemiRepresentable.LocalizationSites.localizationFunctor_hasCoverPullbacks, CategoryTheory.SemiRepresentable.LocalizationSites.relocalizationFunctor_isContinuous, CategoryTheory.SemiRepresentable.LocalizationSites.relocalizationFunctor_isCocontinuous, CategoryTheory.SemiRepresentable.LocalizationSites.relocalizationFunctor_hasCoverPullbacks, CategoryTheory.SemiRepresentable.abelianLocalizationPushforwardPullbackNatIsoSheafHomPrime, CategoryTheory.SemiRepresentable.localizationPushforwardPullbackNatIsoSheafHom
statement: formalized
proof: formalized
---

# 85.15 The site associated to a semi-representable object

Section 85.15 of the Stacks Project, [Tag 09WK](https://stacks.math.columbia.edu/tag/09WK). 7 tags here are carried by 54 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D85, a lemma

[Tag 0D85](https://stacks.math.columbia.edu/tag/0D85) in the Stacks Project.

**`CategoryTheory.SemiRepresentable.LocalizationSites.localizationFunctor_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Continuity.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Continuity.lean#L258). The attribute's comment: “semi\_representable\_localization\_has\_p”.

> **Stacks 0D85.** The componentwise localization functor `C / K ⥤ C` is continuous.

```lean
instance localizationFunctor_isContinuous (S : LocalizationSites.{w} C J) :
    S.localizationFunctor.IsContinuous S.sourceTopology J
```

**`CategoryTheory.SemiRepresentable.LocalizationSites.localizationFunctor_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Continuity.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Continuity.lean#L301). The attribute's comment: “semi\_representable\_localization\_has\_p”.

> **Stacks 0D85.** The componentwise localization functor `C / K ⥤ C` is cocontinuous.

```lean
instance localizationFunctor_isCocontinuous (S : LocalizationSites.{w} C J) :
    S.localizationFunctor.IsCocontinuous S.sourceTopology J
```

**`CategoryTheory.SemiRepresentable.LocalizationSites.localizationFunctor_hasCoverPullbacks`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Continuity.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Continuity.lean#L318). The attribute's comment: “semi\_representable\_localization\_has\_p”.

> **Stacks 0D85.** The componentwise localization functor has property P under the site's
> covering-pullback axiom: relative pullbacks of covering families exist and their projections
> cover.

```lean
lemma localizationFunctor_hasCoverPullbacks (S : LocalizationSites.{w} C J)
    [J.toCoverage.HasPullbacks] :
    ∀ (𝒱 : Covering.{u, v, w'} C), 𝒱.2.presieve₀ ∈ J.toCoverage 𝒱.1 →
      ∀ (U : S.source) (g : S.localizationFunctor.obj U ⟶ 𝒱.1),
        ∃ (P : 𝒱.2.I₀ → S.source) (p₁ : ∀ i, P i ⟶ U)
          (p₂ : ∀ i, S.localizationFunctor.obj (P i) ⟶ 𝒱.2.X i),
          (∀ i,
            S.localizationFunctor.map (p₁ i) ≫ g = p₂ i ≫ 𝒱.2.f i ∧
              ∀ (T : S.source) (a : T ⟶ U)
                (b : S.localizationFunctor.obj T ⟶ 𝒱.2.X i),
                S.localizationFunctor.map a ≫ g = b ≫ 𝒱.2.f i →
                  ∃! l : T ⟶ P i,
                    (l ≫ p₁ i = a ∧ S.localizationFunctor.map l ≫ p₂ i = b)) ∧
            (PreZeroHypercover.mk 𝒱.2.I₀ P p₁).presieve₀ ∈
              S.sourceTopology.toCoverage U
```

**`CategoryTheory.SemiRepresentable.LocalizationSites.relocalizationFunctor_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Continuity.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Continuity.lean#L430). The attribute's comment: “semi\_representable\_relocalization\_has\_p”.

> **Stacks 0D85.** The componentwise relocalization functor `C / K ⥤ C / L` is continuous.

```lean
instance relocalizationFunctor_isContinuous (S : LocalizationSites.{w} C J) :
    S.relocalizationFunctor.IsContinuous S.sourceTopology S.targetTopology
```

**`CategoryTheory.SemiRepresentable.LocalizationSites.relocalizationFunctor_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Continuity.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Continuity.lean#L454). The attribute's comment: “semi\_representable\_relocalization\_has\_p”.

> **Stacks 0D85.** The componentwise relocalization functor `C / K ⥤ C / L` is
> cocontinuous.

```lean
instance relocalizationFunctor_isCocontinuous (S : LocalizationSites.{w} C J) :
    S.relocalizationFunctor.IsCocontinuous S.sourceTopology S.targetTopology
```

**`CategoryTheory.SemiRepresentable.LocalizationSites.relocalizationFunctor_hasCoverPullbacks`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Continuity.lean, line 469](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Continuity.lean#L469). The attribute's comment: “semi\_representable\_relocalization\_has\_p”.

> **Stacks 0D85.** The componentwise relocalization functor has property P: covering families
> admit representable pullbacks, and those pullbacks cover.

```lean
lemma relocalizationFunctor_hasCoverPullbacks (S : LocalizationSites.{w} C J)
    [J.toCoverage.HasPullbacks] :
    S.relocalizationFunctor.HasCoverPullbacks
      (fun 𝒰 ↦ 𝒰.2.presieve₀ ∈ S.sourceTopology.toCoverage 𝒰.1)
      (fun 𝒱 ↦ 𝒱.2.presieve₀ ∈ S.targetTopology.toCoverage 𝒱.1)
```

## Tag 0D86, a lemma

[Tag 0D86](https://stacks.math.columbia.edu/tag/0D86) in the Stacks Project.

**`CategoryTheory.SemiRepresentable.abelianLocalizationPushforwardPullbackNatIsoSheafHomPrime`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/AbelianPushPull.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/AbelianPushPull.lean#L273). The attribute's comment: “the abelian form: abelian-sheaf coefficients, primed internal hom”.

> **Stacks 0D86 for abelian coefficients.** For a semi-representable object `K = {U i}` of a
> small site `(C, J)`, the product of the localization push-pull functors `j_{i,*} j_i^{-1}` on
> abelian sheaves is naturally isomorphic to `ℋom'(F(K)^#, -)`.
>
> This is the source's `j_* j^{-1} F = ℋom'(F(K)^#, F)` under the product description of sheaves on
> `C / K`, for `F` an abelian sheaf and naturally in `F`, which is the form in which Stacks 0D8F
> uses Stacks 0D86. Both sides are the abelian readings of Stacks 04DB of the corresponding
> functors of sheaves of sets — the same reading by which the terms `a_{n,*}a_n^{-1}F` of the Čech
> complex of Stacks 0D79 are built — and the isomorphism is the one of Stacks 0D86 carried through
> that reading, which is possible because both functors preserve finite products and the reading is
> functorial in the finite-product-preserving functor.

```lean
def abelianLocalizationPushforwardPullbackNatIsoSheafHomPrime
    (J : GrothendieckTopology C) (K : FormalCoproduct.{u} C) :
    abelianLocalizationPushPull J K ≅ abelianSheafHomPrime J K
```

**`CategoryTheory.SemiRepresentable.localizationPushforwardPullbackNatIsoSheafHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/PushPull.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/PushPull.lean#L263).

> **Stacks 0D86.** For a semi-representable object `K = {U i}`, the product of the
> localization push-pull functors `j_{i,*} j_i^{-1}` is naturally isomorphic to
> `SheafHom(F(K)^#, -)`. This is the source's `j_* j^{-1} F = SheafHom(F(K)^#, F)` under the
> product description of sheaves on `C / K`, naturally in `F`.

```lean
noncomputable def localizationPushforwardPullbackNatIsoSheafHom
    (J : GrothendieckTopology C) (K : FormalCoproduct.{u} C) :
    (Functor.pi' (fun i : K.I =>
        localizationPullback (K.obj i) J ⋙ localizationPushforward (K.obj i) J) ⋙
        Pi.functor K.I) ≅
      CategoryTheory.SheafHomAdj.sheafHomFunctor
        ((presheafToSheaf J (Type u)).obj ((FormalCoproduct.yoneda (C := C)).obj K))
```

## Tag 0D87, a lemma

[Tag 0D87](https://stacks.math.columbia.edu/tag/0D87) in the Stacks Project.

**`CategoryTheory.SemiRepresentable.componentwiseRelocalization_comp_sheafEquivalence_iso_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Relocalization.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Relocalization.lean#L405). The attribute's comment: “(3): f^\{-1} corresponds to base change along F(K)^sharp to F(L)^sharp”.

> **Stacks 0D87 part (3).** Under the identifications of part (1), the relocalization inverse
> image `f^{-1} : Sh(C / L) ⥤ Sh(C / K)` along a morphism `f : K ⟶ L` of semi-representable objects
> is base change along `F(K)^♯ ⟶ F(L)^♯`: an object `G ⟶ F(L)^♯` is sent to
> `G ×_{F(L)^♯} F(K)^♯ ⟶ F(K)^♯`.
>
> Following the source, this is Stacks 04IL applied to each re-localization morphism
> `C / K.obj i ⟶ C / L.obj (f.f i)` — that is `hComponent` — and then assembled over the index set
> by `assembleOverPullbackIso`, which is where the van Kampen property of the coproduct
> `F(K)^♯ = ∐ i, h_{K.obj i}^♯` is used.

```lean
theorem componentwiseRelocalization_comp_sheafEquivalence_iso_pullback
    {K L : FormalCoproduct.{v} C} (f : K ⟶ L) :
    Nonempty
      (componentwiseRelocalization J f ⋙ (sheafEquivalence J K).functor ≅
        (sheafEquivalence J L).functor ⋙
          Over.pullback (formalCoproductSheafificationMap J f))
```

**`CategoryTheory.SemiRepresentable.isEquivalence_sheafFunctorToOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/SheavesOverSheafification.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/SheavesOverSheafification.lean#L200). The attribute's comment: “(1): the functor j\_! is an equivalence Sh(C/K) to Sh(C)/F(K)^sharp”. References: SGA 4 III (5.4), “special case”.

> **Stacks 0D87 part (1).** The lower shriek functor `j_!` identifies sheaves on the
> localization of `C` at a semi-representable object `K` with sheaves over the associated sheaf
> `F(K)^♯`.
>
> Following the source: `Sh(C / K)` is the product of the `Sh(C / K.obj i)` — which is how
> `SheafOverFormalCoproduct` presents it — and `Sh(C)/F(K)^♯` is the product of the
> `Sh(C)/h_{K.obj i}^♯` by `isEquivalence_sheafCoproductToOver`, so the statement follows from
> Stacks 00Y1 for each component.

```lean
theorem isEquivalence_sheafFunctorToOver : (sheafFunctorToOver J K).IsEquivalence
```

**`CategoryTheory.SemiRepresentable.sheafEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/SheavesOverSheafification.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/SheavesOverSheafification.lean#L208). The attribute's comment: “(1): the resulting equivalence of categories Sh(C/K) to Sh(C)/F(K)^sharp”.

> **Stacks 0D87 part (1)**, as an equivalence of categories
> `Sh(C / K) ≌ Sh(C) / F(K)^♯`. Its functor is `sheafFunctorToOver`, the sheaf level `j_!` viewed
> as a functor into the slice (`sheafEquivalence_functor`).

```lean
noncomputable def sheafEquivalence :
    SheafOverFormalCoproduct J K ≌ Over (formalCoproductSheafification J K)
```

**`CategoryTheory.SemiRepresentable.componentwiseRestrictionCompSheafFunctorToOverIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/SheavesOverSheafification.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/SheavesOverSheafification.lean#L373). The attribute's comment: “(2): j^\{-1} corresponds to F maps to (F times F(K)^sharp over F(K)^sharp)”.

> **Stacks 0D87 part (2).** Under the identification of part (1), restriction
> `j^{-1} : Sh(C) ⥤ Sh(C / K)` is `F ↦ (F × F(K)^♯ ⟶ F(K)^♯)`, i.e. Mathlib's
> `CategoryTheory.toOver (F(K)^♯)`.
>
> Following the source: `toOver A` is right adjoint to `Over.forget A`, and so is
> `j^{-1} ⋙ j_!` read in the slice, because `j_! ⋙ Over.forget A ⊣ j^{-1}`
> (`sheafFunctorToOverForgetAdjunction`) and `j_!` is an equivalence by part (1). Uniqueness of
> right adjoints identifies them.

```lean
noncomputable def componentwiseRestrictionCompSheafFunctorToOverIso :
    componentwiseRestriction J K ⋙ sheafFunctorToOver J K ≅
      toOver (formalCoproductSheafification J K)
```

**`CategoryTheory.SemiRepresentable.componentwiseRestriction_comp_sheafEquivalence_iso_toOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/SheavesOverSheafification.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/SheavesOverSheafification.lean#L387). The attribute's comment: “(2): under the equivalence of (1), j^\{-1} is toOver of F(K)^sharp”.

> **Stacks 0D87 part (2)**, stated through the equivalence of categories of part (1): under
> `sheafEquivalence`, componentwise restriction corresponds to `toOver (F(K)^♯)`.

```lean
theorem componentwiseRestriction_comp_sheafEquivalence_iso_toOver :
    Nonempty (componentwiseRestriction J K ⋙ (sheafEquivalence J K).functor ≅
      toOver (formalCoproductSheafification J K))
```

## Tag 0D88, a lemma

[Tag 0D88](https://stacks.math.columbia.edu/tag/0D88) in the Stacks Project.

**`CategoryTheory.SemiRepresentable.injective_localizationInverseImage_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Injective.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Injective.lean#L88). The attribute's comment: “injectives are preserved”.

> **Stacks 0D88.** The inverse image along the localization at a semi-representable object
> sends injective abelian sheaves to injective abelian sheaves.

```lean
theorem injective_localizationInverseImage_obj
    (I : Sheaf J AddCommGrpCat.{max u v t}) [Injective I] :
    Injective ((localizationInverseImage J K AddCommGrpCat.{max u v t}).obj I)
```

**`CategoryTheory.SemiRepresentable.isKInjective_localizationInverseImage_mapHomologicalComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/KInjective.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/KInjective.lean#L176). The attribute's comment: “K-injective complexes are preserved”.

> **Stacks 0D88.** Inverse image along the localization at a semi-representable object sends a
> K-injective complex of abelian sheaves to a K-injective complex.

```lean
theorem isKInjective_localizationInverseImage_mapHomologicalComplex
    (I : CochainComplex (Sheaf J AddCommGrpCat.{max u v w}) ℤ) [I.IsKInjective] :
    ((localizationInverseImageMapHomologicalComplex J K).obj I).IsKInjective
```

## Tag 0D89, a remark

[Tag 0D89](https://stacks.math.columbia.edu/tag/0D89) in the Stacks Project.

**`CategoryTheory.SemiRepresentable.componentwiseLocalizationFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean#L87). The attribute's comment: “localization”.

> The localization functor from the componentwise site `C / K` of a semi-representable object
> `K` over `X` to `C / X`. On the component indexed by `i` it is relocalization along
> `K.obj i : U i ⟶ X`.

```lean
def componentwiseLocalizationFunctor {X : C} (K : FormalCoproduct.{w} (Over X)) :
    ComponentOver (⟨K.I, fun i => (K.obj i).left⟩ : FormalCoproduct.{w} C) ⥤ Over X
```

**`CategoryTheory.SemiRepresentable.componentwiseLocalizationFunctorCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean#L94). The attribute's comment: “localization”.

> On each component, the functor `C / K ⥤ C / X` is canonically the relocalization functor
> associated to the structural map `U i ⟶ X`.

```lean
def componentwiseLocalizationFunctorCompIso {X : C} (K : FormalCoproduct.{w} (Over X))
    (i : K.I) :
    CategoryTheory.Sigma.incl (C := fun i : K.I => Over (K.obj i).left) i ⋙
      componentwiseLocalizationFunctor K ≅ Over.map (K.obj i).hom
```

**`CategoryTheory.SemiRepresentable.componentwiseLocalization_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean#L195). The attribute's comment: “localization\_property”.

> **Stacks 0D89.** The componentwise localization functor to `C / X` is continuous.

```lean
instance componentwiseLocalization_isContinuous :
    (componentwiseLocalizationFunctor K).IsContinuous
      (componentwiseTopology J
        (⟨K.I, fun i => (K.obj i).left⟩ : FormalCoproduct.{w} C))
  (J.over X)
```

**`CategoryTheory.SemiRepresentable.componentwiseLocalization_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean#L211). The attribute's comment: “localization\_property”.

> **Stacks 0D89.** The componentwise localization functor to `C / X` is cocontinuous.

```lean
instance componentwiseLocalization_isCocontinuous :
    (componentwiseLocalizationFunctor K).IsCocontinuous
      (componentwiseTopology J
        (⟨K.I, fun i => (K.obj i).left⟩ : FormalCoproduct.{w} C))
  (J.over X)
```

**`CategoryTheory.SemiRepresentable.componentwiseLocalization_hasCoverPullbacks`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean#L228). The attribute's comment: “localization\_property”.

> **Stacks 0D89.** The componentwise localization functor to `C / X` has property P:
> pullbacks of covering families along maps out of its image are representable and cover.

```lean
lemma componentwiseLocalization_hasCoverPullbacks
    [(J.over X).toCoverage.HasPullbacks] :
    ∀ (𝒱 : Covering.{max u v, v, w'} (Over X)),
      𝒱.2.presieve₀ ∈ (J.over X).toCoverage 𝒱.1 →
      ∀ (U : ComponentOver
        (⟨K.I, fun i => (K.obj i).left⟩ : FormalCoproduct.{w} C))
        (g : (componentwiseLocalizationFunctor K).obj U ⟶ 𝒱.1),
        ∃ (P : 𝒱.2.I₀ → ComponentOver
            (⟨K.I, fun i => (K.obj i).left⟩ : FormalCoproduct.{w} C))
          (p₁ : ∀ i, P i ⟶ U)
          (p₂ : ∀ i, (componentwiseLocalizationFunctor K).obj (P i) ⟶ 𝒱.2.X i),
          (∀ i,
            (componentwiseLocalizationFunctor K).map (p₁ i) ≫ g =
              p₂ i ≫ 𝒱.2.f i ∧
              ∀ (T : ComponentOver
                  (⟨K.I, fun i => (K.obj i).left⟩ : FormalCoproduct.{w} C))
                (a : T ⟶ U)
                (b : (componentwiseLocalizationFunctor K).obj T ⟶ 𝒱.2.X i),
                (componentwiseLocalizationFunctor K).map a ≫ g = b ≫ 𝒱.2.f i →
                  ∃! l : T ⟶ P i,
                    (l ≫ p₁ i = a ∧
                      (componentwiseLocalizationFunctor K).map l ≫ p₂ i = b)) ∧
            (PreZeroHypercover.mk 𝒱.2.I₀ P p₁).presieve₀ ∈
              (componentwiseTopology J
                (⟨K.I, fun i => (K.obj i).left⟩ : FormalCoproduct.{w} C)).toCoverage U
```

**`CategoryTheory.SemiRepresentable.componentwiseRelocalizationMorphismOfTopoi`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean#L358). The attribute's comment: “relocalization”.

> **Stacks 0D89.** The morphism of topoi from `Sh(C / K)` to `Sh(C / L)` induced by
> componentwise relocalization along a morphism `K ⟶ L` of `SR(C, X)`, together with the
> identification of its inverse image with restriction along the componentwise functor.

```lean
noncomputable def componentwiseRelocalizationMorphismOfTopoi
    {K L : FormalCoproduct.{w} (Over X)} (f : K ⟶ L) :
    let S := componentwiseLocalizationSitesOver J X f
    { g : MorphismOfTopoi
        (Sheaf S.sourceTopology (Type (max w v u)))
        (Sheaf S.targetTopology (Type (max w v u))) //
      g.inverseImage ⋙ sheafToPresheaf S.sourceTopology (Type (max w v u)) =
        sheafToPresheaf S.targetTopology (Type (max w v u)) ⋙
          (CategoryTheory.Functor.whiskeringLeft _ _ _).obj S.relocalizationFunctor.op }
```

**`CategoryTheory.SemiRepresentable.componentwiseRelocalization_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean#L379). The attribute's comment: “relocalization\_property”.

> **Stacks 0D89.** The componentwise relocalization functor is continuous.

```lean
instance componentwiseRelocalization_isContinuous
    {K L : FormalCoproduct.{w} (Over X)} (f : K ⟶ L) :
    let S := componentwiseLocalizationSitesOver J X f
    S.relocalizationFunctor.IsContinuous S.sourceTopology S.targetTopology
```

**`CategoryTheory.SemiRepresentable.componentwiseRelocalization_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean#L387). The attribute's comment: “relocalization\_property”.

> **Stacks 0D89.** The componentwise relocalization functor is cocontinuous.

```lean
instance componentwiseRelocalization_isCocontinuous
    {K L : FormalCoproduct.{w} (Over X)} (f : K ⟶ L) :
    let S := componentwiseLocalizationSitesOver J X f
    S.relocalizationFunctor.IsCocontinuous S.sourceTopology S.targetTopology
```

**`CategoryTheory.SemiRepresentable.componentwiseRelocalization_hasCoverPullbacks`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean#L396). The attribute's comment: “relocalization\_property”.

> **Stacks 0D89.** The componentwise relocalization functor has property P: pullbacks of
> covering families along maps out of its image are representable and covering.

```lean
lemma componentwiseRelocalization_hasCoverPullbacks
    {K L : FormalCoproduct.{w} (Over X)} (f : K ⟶ L)
    [J.toCoverage.HasPullbacks] :
    let S := componentwiseLocalizationSitesOver J X f
    S.relocalizationFunctor.HasCoverPullbacks
      (fun 𝒰 ↦ 𝒰.2.presieve₀ ∈ S.sourceTopology.toCoverage 𝒰.1)
      (fun 𝒱 ↦ 𝒱.2.presieve₀ ∈ S.targetTopology.toCoverage 𝒱.1)
```

**`CategoryTheory.SemiRepresentable.componentwiseLocalizationPushforwardPullbackNatIsoSheafHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/OverPushPull.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/OverPushPull.lean#L260). The attribute's comment: “push\_pull”.

> **Stacks 0D89.** The localization push-pull on `C / X` at a semi-representable object `K`
> over `X` is naturally the sheaf internal hom out of the sheafification of the semi-representable
> presheaf associated to `K`.

```lean
noncomputable def componentwiseLocalizationPushforwardPullbackNatIsoSheafHom
    {C : Type u} [SmallCategory C] (J : GrothendieckTopology C) (X : C)
    (K : FormalCoproduct.{u} (Over X)) :
    ((componentwiseLocalizationFunctor K).sheafPushforwardContinuous
      (Type u)
      (componentwiseTopology J
        (⟨K.I, fun i => (K.obj i).left⟩ : FormalCoproduct.{u} C))
      (J.over X)) ⋙
      ((componentwiseLocalizationFunctor K).sheafPushforwardCocontinuous
        (Type u)
        (componentwiseTopology J
          (⟨K.I, fun i => (K.obj i).left⟩ : FormalCoproduct.{u} C))
        (J.over X)) ≅
      CategoryTheory.SheafHomAdj.sheafHomFunctor
        ((presheafToSheaf (J.over X) (Type u)).obj
        ((FormalCoproduct.yoneda (C := Over X)).obj K))
```

Declarations registered for the tag:

- [`CategoryTheory.SemiRepresentable.ComponentOver`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Site.lean#L61), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean#L409) (StacksFrontier): “site”.
- [`CategoryTheory.SemiRepresentable.componentwiseTopology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Site.lean#L67), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean#L410) (StacksFrontier): “site”.
- [`CategoryTheory.SemiRepresentable.formalCoproductSliceSheavesEquivalence`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Sheaves.lean#L492), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Over.lean#L411) (StacksFrontier): “product”.

## Tag 0D9U, a remark

[Tag 0D9U](https://stacks.math.columbia.edu/tag/0D9U) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.familyLowerShriek_iso_directSum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/DirectSum.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/DirectSum.lean#L215). The attribute's comment: “part (3): j\_! is the direct sum of the j\_\{i,!}”.

> **Stacks 0D9U, part (3): the direct-sum formula.** In terms of the product decomposition of
> part (2), `j_!` sends a family `(F i)` to `⨁ i, j_{i,!} F i`: both are left adjoint to `j^*`.

```lean
noncomputable def familyLowerShriek_iso_directSum :
    familyLowerShriek X K ≅ familyDirectSumLowerShriek X K
```

**`AlgebraicGeometry.RingedSite.familyLowerShriek_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/DirectSum.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/DirectSum.lean#L241). The attribute's comment: “part (3): j\_! is exact”.

> **Stacks 0D9U, part (3).** The lower shriek `j_!` is exact: it preserves finite colimits
> because it is a left adjoint, and finite limits because it is the direct sum of the exact
> functors `j_{i,!}`.

```lean
theorem familyLowerShriek_exact : exactFunctor _ _ (familyLowerShriek X K)
```

**`AlgebraicGeometry.RingedSite.lowerShriekModules_iso_familyLowerShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/DirectSum.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/DirectSum.lean#L357). The attribute's comment: “part (3): j\_! is the left adjoint of the pullback of modules along j”.

> **Stacks 0D9U, part (3).** The lower shriek of the morphism of ringed topoi `j` — the left
> adjoint of the pullback `j^*` of sheaves of modules, which is what the source means by `j_!` —
> is `familyLowerShriek` up to the equivalence by which `j^*` differs from restriction.

```lean
noncomputable def lowerShriekModules_iso_familyLowerShriek :
    (familyLocalizationMorphism X K).lowerShriekModules ≅
      (familyPullbackScalarsEquivalence X K).inverse ⋙ familyLowerShriek X K
```

**`AlgebraicGeometry.RingedSite.lowerShriekModules_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/DirectSum.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/DirectSum.lean#L383). The attribute's comment: “part (3): the left adjoint of j^* is exact”.

> **Stacks 0D9U, part (3).** The lower shriek of the morphism of ringed topoi `j`, the left
> adjoint of `j^*`, is exact: it is `familyLowerShriek`, which is exact, composed with an
> equivalence.

```lean
theorem lowerShriekModules_exact (X : RingedSite.{u, u, u}) (K : FormalCoproduct.{u} X.C) :
    exactFunctor _ _ ((familyLocalizationMorphism X K).lowerShriekModules)
```

**`AlgebraicGeometry.RingedSite.morphismRestr_isRightAdjoint`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/DirectSum.lean, line 729](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/DirectSum.lean#L729). The attribute's comment: “f^* has a left adjoint f\_!”.

> **Stacks 0D9U.** `f^*` has a left adjoint `f_!`.

```lean
instance morphismRestr_isRightAdjoint : (morphismRestr X f).IsRightAdjoint
```

**`AlgebraicGeometry.RingedSite.morphismLowerShriek_iso_directSum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/DirectSum.lean, line 735](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/DirectSum.lean#L735). The attribute's comment: “f\_! is the direct sum of the componentwise lower shrieks”.

> **Stacks 0D9U.** In terms of the product decomposition of part (2), `f_!` sends a family
> `(F i)` to `⨁ i, f_{i,!} F i`: both are left adjoint to `f^*`.

```lean
noncomputable def morphismLowerShriek_iso_directSum :
    (morphismRestr X f).leftAdjoint ≅
      (componentwiseModuleRestrictionEquivalence X K).functor ⋙
        piCoproduct (morphismComponentLowerShriek X f)
```

**`AlgebraicGeometry.RingedSite.morphismLowerShriek_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/DirectSum.lean, line 746](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/DirectSum.lean#L746). The attribute's comment: “f\_! is exact”.

> **Stacks 0D9U.** The lower shriek `f_!` is exact: it preserves finite colimits because it
> is a left adjoint, and finite limits because it is the direct sum of the exact functors
> `f_{i,!}`, coproducts of sheaves of modules being exact.

```lean
theorem morphismLowerShriek_exact : exactFunctor _ _ (morphismRestr X f).leftAdjoint
```

**`AlgebraicGeometry.RingedSite.familyMorphism_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Flat.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Flat.lean#L248). The attribute's comment: “f\_flat”.

> **Stacks 0D9U.** The morphism of ringed topoi induced by a morphism of semi-representable
> objects is flat.

```lean
theorem familyMorphism_isFlat (X : RingedSite.{u, v, max u v w r})
    {K L : FormalCoproduct.{w} X.C} (f : K ⟶ L) :
    Stacks.Sheaf.RingedToposFlat.RingedToposHom.IsFlat.{max u v w, max u v w,
        max u v w r, max u v w, max u v w, max u v w r}
      (familyMorphism.{w, v, u, r} X f).val
```

**`AlgebraicGeometry.RingedSite.familyLocalizationMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Localization.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Localization.lean#L191). The attribute's comment: “part (3): the localization morphism j of ringed topoi”.

> **Stacks 0D9U, part (3).** The localization morphism
> `j : (Sh(C / K), O_K) ⟶ (Sh(C), O_X)` of ringed topoi attached to a semi-representable object
> `K`: its geometric morphism is restriction along the componentwise localization functor and its
> structure map is the canonical identity comparison of structure sheaves.

```lean
noncomputable def familyLocalizationMorphism (X : RingedSite.{u, v, max u v w})
    (K : FormalCoproduct.{w} X.C) :
    RingedToposHom (localizationRingedTopos X K) (ringedTopos.{u, v, w} X)
```

**`AlgebraicGeometry.RingedSite.familyLocalizationMorphism_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Localization.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Localization.lean#L234). The attribute's comment: “part (3): j is flat”.

> **Stacks 0D9U.** The localization morphism `j` is flat: its inverse-image structure map is
> an isomorphism, and an isomorphism of sheaves of commutative rings is flat.

```lean
theorem familyLocalizationMorphism_isFlat (X : RingedSite.{u, v, max u v w})
    (K : FormalCoproduct.{w} X.C) :
    AlgebraicGeometry.SheafOfModules.IsFlatMapULift
      (familyLocalizationMorphism X K).fSharpInverseImage
```

**`AlgebraicGeometry.RingedSite.familyLocalizationMorphism_pullback_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Localization.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Localization.lean#L246). The attribute's comment: “part (3): j^* is exact”.

> **Stacks 0D9U.** Pullback of sheaves of modules along the localization morphism is exact,
> the morphism being flat.

```lean
theorem familyLocalizationMorphism_pullback_exact (X : RingedSite.{u, v, max u v w})
    (K : FormalCoproduct.{w} X.C) :
    exactFunctor _ _ (Stacks.Sheaves.RingedToposModules.RingedToposHom.pullbackModules
      (X := localizationRingedTopos X K) (Y := ringedTopos.{u, v, w} X)
      (familyLocalizationMorphism X K).toRingedToposModulesHom)
```

**`AlgebraicGeometry.RingedSite.familyLocalizationMorphism_pullback_isRightAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Localization.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Localization.lean#L260). The attribute's comment: “part (3): j^* has a left adjoint j\_!”.

> **Stacks 0D9U.** Pullback of sheaves of modules along the localization morphism has a left
> adjoint `j_!`, namely `AlgebraicGeometry.RingedToposHom.lowerShriekModules` of that morphism:
> the structure map is an isomorphism, and the inverse image of sheaves of modules is restriction
> along the componentwise localization functor, which has a left adjoint because `C / K` is
> essentially small.

```lean
theorem familyLocalizationMorphism_pullback_isRightAdjoint (X : RingedSite.{u, v, max u v w})
    (K : FormalCoproduct.{w} X.C) :
    (familyLocalizationMorphism X K).toModulesHom.pullbackModules.IsRightAdjoint
```

**`AlgebraicGeometry.RingedSite.familyMorphism_pullback_isRightAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Localization.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Localization.lean#L275). The attribute's comment: “part (3): f^* has a left adjoint f\_!”.

> **Stacks 0D9U.** Pullback of sheaves of modules along the morphism of ringed topoi attached
> to a morphism `f : K ⟶ L` of semi-representable objects has a left adjoint `f_!`, namely
> `AlgebraicGeometry.RingedToposHom.lowerShriekModules` of that morphism: the structure map is an
> isomorphism and the inverse image of sheaves of modules is restriction along the componentwise
> relocalization functor, which has a left adjoint because `C / K` is essentially small.

```lean
theorem familyMorphism_pullback_isRightAdjoint (X : RingedSite.{u, v, max u v w})
    {K L : FormalCoproduct.{w} X.C} (f : K ⟶ L) :
    (familyMorphism.{w, v, u, u} X f).val.toModulesHom.pullbackModules.IsRightAdjoint
```

**`AlgebraicGeometry.RingedSite.familyComponentInclLowerShriek_comp_familyLowerShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Localization.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Localization.lean#L395). The attribute's comment: “part (3): j\_! is j\_\{i,!} on the i-th summand”.

> **Stacks 0D9U, part (3).** On the `i`-th summand of the decomposition
> `Mod(O_K) = ∏ Mod(O_{U i})` the lower shriek `j_!` is the extension by zero `j_{i,!}` of that
> component: the inclusion of the `i`-th component followed by the componentwise localization
> functor is the localization functor of `U i`, so the two left adjoints agree. This is the
> sentence of the source that `j_!` sends `(F i)` to `⨁ j_{i,!} F i`, read one summand at a
> time.

```lean
noncomputable def familyComponentInclLowerShriek_comp_familyLowerShriek
    (X : RingedSite.{u, v, max u v w}) (K : FormalCoproduct.{w} X.C) (i : K.I) :
    familyComponentInclLowerShriek X K i ⋙ familyLowerShriek X K ≅
      familyComponentLowerShriek X K i
```

**`AlgebraicGeometry.RingedSite.moduleSheavesProductEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/ModuleProduct.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/ModuleProduct.lean#L411). The attribute's comment: “module\_product”.

> Modules on the disjoint union of localized ringed sites are componentwise modules, via the
> canonical componentwise restriction functor.

```lean
noncomputable def moduleSheavesProductEquivalence
    (X : RingedSite.{u, u, u}) (K : FormalCoproduct.{w} X.C) :
    { e : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (X.localization K).O) ≌
      ((i : K.I) → SheafOfModules.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf (X.over (K.obj i)).O)) //
      e.functor = componentwiseModuleRestriction X K }
```

**`AlgebraicGeometry.RingedSite.moduleSheavesProductEquivalence'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/ModuleProduct.lean, line 467](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/ModuleProduct.lean#L467). The attribute's comment: “module\_product”.

> Modules on the disjoint union of localized ringed sites are componentwise modules, via the
> canonical componentwise restriction functor.

```lean
noncomputable def moduleSheavesProductEquivalence'
    (X : RingedSite.{u, v, r}) (K : FormalCoproduct.{w} X.C) :
    { e : SheafOfModules.{t} (Stacks.SheafOfModules.Tensor.ringSheaf (X.localization' K).O) ≌
      ((i : K.I) → SheafOfModules.{t}
          (Stacks.SheafOfModules.Tensor.ringSheaf (X.over (K.obj i)).O)) //
      e.functor = componentwiseModuleRestriction' X K }
```

**`AlgebraicGeometry.RingedSite.familyMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Morphism.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/Morphism.lean#L104). The attribute's comment: “family\_morphism”.

> **Stacks 0D9U.** A morphism of semi-representable objects induces a morphism of the ringed
> topoi of their componentwise localizations: its inverse image on sheaves of sets is restriction
> along the componentwise relocalization functor, and its structure map is the canonical identity
> comparison, which is an isomorphism.

```lean
noncomputable def familyMorphism (X : RingedSite.{u, v, max u v w r})
    {K L : FormalCoproduct.{w} X.C} (f : K ⟶ L) :
    let S : LocalizationSites.{w} X.C X.J := ⟨K, L, f⟩
    { g : RingedToposHom (localizationRingedTopos X K) (localizationRingedTopos X L) //
      (g.toToposHom.inverseImage ⋙
          sheafToPresheaf S.sourceTopology (Type (max u v w r)) =
        sheafToPresheaf S.targetTopology (Type (max u v w r)) ⋙
          (CategoryTheory.Functor.whiskeringLeft _ _ _).obj S.relocalizationFunctor.op) ∧
      (∃ h : (localizationRingedTopos X K).forgetRing.obj
          ((inverseImageCommRingFunctor g.toToposHom).obj
            (localizationRingedTopos X L).O) =
          (localizationRingedTopos X K).forgetRing.obj (localizationRingedTopos X K).O,
        (localizationRingedTopos X K).forgetRing.map g.fSharpInverseImage =
          eqToHom h) ∧
      IsIso g.fSharpInverseImage }
```

**`AlgebraicGeometry.RingedSite.familyMorphism_pullback_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/PullbackExact.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/PullbackExact.lean#L54). The attribute's comment: “f\_flat”.

> **Stacks 0D9U.** Pullback of sheaves of modules along the morphism of ringed topoi induced
> by a morphism of semi-representable objects is exact.

```lean
theorem familyMorphism_pullback_exact (X : RingedSite.{u, v, max u v w r})
    {K L : FormalCoproduct.{w} X.C} (f : K ⟶ L)
    [(componentwiseTopology X.J K).HasSheafCompose
      (forget₂ CommRingCat.{max u v w r} RingCat.{max u v w r})]
    [(componentwiseTopology X.J L).HasSheafCompose
      (forget₂ CommRingCat.{max u v w r} RingCat.{max u v w r})]
    [(componentwiseTopology X.J K).HasSheafCompose (forget RingCat.{max u v w r})]
    [(componentwiseTopology X.J L).HasSheafCompose (forget RingCat.{max u v w r})]
    [(componentwiseTopology X.J K).HasSheafCompose (forget AddCommGrpCat.{max u v w r})]
    [(componentwiseTopology X.J L).HasSheafCompose (forget AddCommGrpCat.{max u v w r})]
    [HasWeakSheafify (componentwiseTopology X.J K) AddCommGrpCat.{max u v w r}]
    [(componentwiseTopology X.J K).WEqualsLocallyBijective
      AddCommGrpCat.{max u v w r}] :
    exactFunctor _ _
      ((familyMorphism.{w, v, u, r} X f).val.toRingedToposModulesHom.pullbackModules)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.RingedSite.localizationStructureSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Ringed.lean#L51), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/PullbackExact.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/PullbackExact.lean#L80) (StacksFrontier): “structure\_sheaf\_o\_k”.
- [`AlgebraicGeometry.RingedSite.localization`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Ringed.lean#L63), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/PullbackExact.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/PullbackExact.lean#L83) (StacksFrontier): “ringed\_site”.

## Tag 0D9V, a remark

[Tag 0D9V](https://stacks.math.columbia.edu/tag/0D9V) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.localizationToposMorphismOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean#L185). The attribute's comment: “part (3): the geometric morphism underlying the localization over Y”.

> **Stacks 0D9V, part (3).** The geometric morphism `Sh(C / K) ⟶ Sh(C / Y)` underlying the
> localization morphism of a semi-representable object `K` over `Y`: its inverse image is
> restriction along the componentwise localization functor `C / K ⥤ C / Y` and its direct image is
> the right adjoint of that restriction.

```lean
noncomputable def localizationToposMorphismOver (X : RingedSite.{u, v, max u v w}) {Y : X.C}
    (K : FormalCoproduct.{w} (Over Y)) :
    MorphismOfTopoi
      (Sheaf (componentwiseTopology X.J (underlyingFormalCoproduct X K)) (Type (max u v w)))
      (Sheaf (X.J.over Y) (Type (max u v w)))
```

**`AlgebraicGeometry.RingedSite.localizationStructureIsoOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean#L213). The attribute's comment: “part (3): the structure map of the localization over Y”.

> **Stacks 0D9V, part (3).** The structure map of the localization morphism over `Y`, in
> inverse-image form: the inverse image of `O_Y` along restriction is the restriction of `O_Y`,
> and that restriction is `O_K` because the composite of the componentwise localization functor
> with the slice projection is the componentwise localization functor to `C`.

```lean
noncomputable def localizationStructureIsoOver (X : RingedSite.{u, v, max u v w}) {Y : X.C}
    (K : FormalCoproduct.{w} (Over Y)) :
    (inverseImageCommRingFunctor (localizationToposMorphismOver X K)).obj
        (ringedTopos.{max u v, v, w} (X.over Y)).O ≅
      (localizationRingedTopos X (underlyingFormalCoproduct X K)).O
```

**`AlgebraicGeometry.RingedSite.localizationMorphismOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean#L236). The attribute's comment: “part (3): the localization morphism of ringed topoi over Y”.

> **Stacks 0D9V, part (3).** The localization morphism
> `j : (Sh(C / K), O_K) ⟶ (Sh(C / Y), O_Y)` of ringed topoi attached to a semi-representable
> object `K` over `Y`: its geometric morphism is restriction along the componentwise localization
> functor and its structure map is the canonical identity comparison of structure sheaves.

```lean
noncomputable def localizationMorphismOver (X : RingedSite.{u, v, max u v w}) {Y : X.C}
    (K : FormalCoproduct.{w} (Over Y)) :
    RingedToposHom (localizationRingedTopos X (underlyingFormalCoproduct X K))
      (ringedTopos.{max u v, v, w} (X.over Y))
```

**`AlgebraicGeometry.RingedSite.forgetRing_localizationMorphismOver_fSharpInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean#L308). The attribute's comment: “part (3): the structure map of the localization over Y is the identity”.

> **Stacks 0D9V, part (3).** The structure map of the localization morphism over `Y` is the
> canonical identity comparison: on underlying sheaves of sets it is the identification
> `forgetRing_inverseImage_structureSheaf_over` and nothing more.

```lean
theorem forgetRing_localizationMorphismOver_fSharpInverseImage
    (X : RingedSite.{u, v, max u v w}) {Y : X.C} (K : FormalCoproduct.{w} (Over Y)) :
    (localizationRingedTopos X (underlyingFormalCoproduct X K)).forgetRing.map
        (localizationMorphismOver X K).fSharpInverseImage =
      eqToHom (forgetRing_inverseImage_structureSheaf_over X K)
```

**`AlgebraicGeometry.RingedSite.localizationMorphismOver_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean, line 335](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean#L335). The attribute's comment: “flatness of the localization morphism over Y”.

> **Stacks 0D9V.** The localization morphism over `Y` is flat: its inverse-image structure map
> is an isomorphism, and an isomorphism of sheaves of commutative rings is flat.

```lean
theorem localizationMorphismOver_isFlat (X : RingedSite.{u, v, max u v w}) {Y : X.C}
    (K : FormalCoproduct.{w} (Over Y)) :
    AlgebraicGeometry.SheafOfModules.IsFlatMapULift
      (localizationMorphismOver X K).fSharpInverseImage
```

**`AlgebraicGeometry.RingedSite.localizationMorphismOver_pullback_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean#L348). The attribute's comment: “exactness of the pullback of modules along the localization over Y”.

> **Stacks 0D9V.** Pullback of sheaves of modules along the localization morphism over `Y` is
> exact, the morphism being flat.

```lean
theorem localizationMorphismOver_pullback_exact (X : RingedSite.{u, v, max u v w}) {Y : X.C}
    (K : FormalCoproduct.{w} (Over Y)) :
    exactFunctor _ _ ((localizationMorphismOver X K).toRingedToposModulesHom.pullbackModules)
```

**`AlgebraicGeometry.RingedSite.localizationMorphismOver_pullback_isRightAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean#L360). The attribute's comment: “the left adjoint of the pullback of modules along the localization over Y”.

> **Stacks 0D9V.** Pullback of sheaves of modules along the localization morphism over `Y`
> has a left adjoint `j_!`, namely `AlgebraicGeometry.RingedToposHom.lowerShriekModules` of that
> morphism: the structure map is an isomorphism, and the inverse image of sheaves of modules is
> restriction along the componentwise localization functor, which has a left adjoint because
> `C / K` is essentially small.

```lean
theorem localizationMorphismOver_pullback_isRightAdjoint (X : RingedSite.{u, v, max u v w})
    {Y : X.C} (K : FormalCoproduct.{w} (Over Y)) :
    (localizationMorphismOver X K).toModulesHom.pullbackModules.IsRightAdjoint
```

**`AlgebraicGeometry.RingedSite.familyMorphismOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean#L376). The attribute's comment: “part (4): the morphism of ringed topoi attached to a morphism of SR(C, Y)”.

> **Stacks 0D9V, part (4).** The morphism of ringed topoi
> `(Sh(C / K), O_K) ⟶ (Sh(C / L), O_L)` attached to a morphism `K ⟶ L` of semi-representable
> objects over `Y`: it is the morphism of Stacks 0D9U attached to the induced morphism of the
> underlying semi-representable objects of `C`, since neither the two localization sites nor their
> structure sheaves see the structural maps to `Y`. Its inverse image and its structure map are
> specified by `AlgebraicGeometry.RingedSite.familyMorphism`.

```lean
noncomputable def familyMorphismOver (X : RingedSite.{u, v, max u v w}) {Y : X.C}
    {K L : FormalCoproduct.{w} (Over Y)} (f : K ⟶ L) :
    RingedToposHom (localizationRingedTopos X (underlyingFormalCoproduct X K))
      (localizationRingedTopos X (underlyingFormalCoproduct X L))
```

**`AlgebraicGeometry.RingedSite.familyMorphismOver_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean#L407). The attribute's comment: “flatness of the morphism attached to a morphism of SR(C, Y)”.

> **Stacks 0D9V.** The morphism attached to a morphism of `SR(C, Y)` is flat. This is the
> corresponding clause of Stacks 0D9U for the induced morphism of underlying semi-representable
> objects of `C`.

```lean
theorem familyMorphismOver_isFlat (X : RingedSite.{u, v, max u v w}) {Y : X.C}
    {K L : FormalCoproduct.{w} (Over Y)} (f : K ⟶ L) :
    AlgebraicGeometry.SheafOfModules.IsFlatMapULift
      (familyMorphismOver X f).fSharpInverseImage
```

**`AlgebraicGeometry.RingedSite.familyMorphismOver_pullback_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean, line 418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean#L418). The attribute's comment: “exactness of the pullback of modules along a morphism of SR(C, Y)”.

> **Stacks 0D9V.** Pullback of sheaves of modules along the morphism attached to a morphism of
> `SR(C, Y)` is exact, that morphism being flat.

```lean
theorem familyMorphismOver_pullback_exact (X : RingedSite.{u, v, max u v w}) {Y : X.C}
    {K L : FormalCoproduct.{w} (Over Y)} (f : K ⟶ L) :
    exactFunctor _ _ ((familyMorphismOver X f).toRingedToposModulesHom.pullbackModules)
```

**`AlgebraicGeometry.RingedSite.familyMorphismOver_pullback_isRightAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean#L430). The attribute's comment: “the left adjoint of the pullback of modules along a morphism of SR(C, Y)”.

> **Stacks 0D9V.** Pullback of sheaves of modules along the morphism attached to a morphism of
> `SR(C, Y)` has a left adjoint `f_!`, namely
> `AlgebraicGeometry.RingedToposHom.lowerShriekModules` of that morphism: the structure map is an
> isomorphism and the inverse image of sheaves of modules is restriction along the componentwise
> relocalization functor, which has a left adjoint because `C / K` is essentially small.

```lean
theorem familyMorphismOver_pullback_isRightAdjoint (X : RingedSite.{u, v, max u v w}) {Y : X.C}
    {K L : FormalCoproduct.{w} (Over Y)} (f : K ⟶ L) :
    (familyMorphismOver X f).toModulesHom.pullbackModules.IsRightAdjoint
```

Declarations registered for the tag:

- [`AlgebraicGeometry.RingedSite.localizationStructureSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Ringed.lean#L51), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean#L461) (StacksFrontier): “part (1): the structure sheaf O\_K”.
- [`AlgebraicGeometry.RingedSite.localization`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Ringed.lean#L63), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean#L464) (StacksFrontier): “part (1): the ringed site (C / K, O\_K)”.
- [`AlgebraicGeometry.RingedSite.moduleSheavesProductEquivalence`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/Family/ModuleProduct.lean#L411), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean, line 467](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/SemiRepresentable/RingedOver.lean#L467) (StacksFrontier): “part (2): the decomposition of Mod(O\_K) into componentwise modules”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.15, Tag 09WK](https://stacks.math.columbia.edu/tag/09WK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

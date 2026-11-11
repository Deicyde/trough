---
declaration: section
origin: cited
lean: Stacks.ComparingTopologies.comparisonPullbackOverMapPullbackIso, Stacks.ComparingTopologies.overMapPullback_comp_comparisonPushforward, Stacks.ComparingTopologies.CohomologyComparison, Stacks.ComparingTopologies.CohomologyComparison.fineWeakSerre, Stacks.ComparingTopologies.CohomologyComparison.fineWeakSerre_iff_weakSerre_pushforward, Stacks.ComparingTopologies.CohomologyComparison.fineWeakSerre_overMapPullback, Stacks.ComparingTopologies.higherDirectImageComparison, Stacks.ComparingTopologies.isIso_higherDirectImageComparison_app
statement: formalized
proof: formalized
---

# 21.30 Comparing cohomology

Section 21.30 of the Stacks Project, [Tag 0EZ1](https://stacks.math.columbia.edu/tag/0EZ1). 11 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EZ2, an equation

[Tag 0EZ2](https://stacks.math.columbia.edu/tag/0EZ2) in the Stacks Project.

**`Stacks.ComparingTopologies.comparisonPullbackOverMapPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/ComparisonSituation.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/ComparisonSituation.lean#L318). The attribute's comment: “commutativity of the square of topoi”.

> **Stacks 0EZ2.** For two comparable topologies, change of topology commutes with
> restriction along a morphism, up to the canonical natural isomorphism of inverse-image
> functors.

```lean
noncomputable def comparisonPullbackOverMapPullbackIso
    {J K : GrothendieckTopology C} (h : K ≤ J) {X Y : C} (f : X ⟶ Y) :
    comparisonPullback (over_le_over h Y) ⋙ J.overMapPullback (Type (max u v)) f ≅
      K.overMapPullback (Type (max u v)) f ⋙ comparisonPullback (over_le_over h X)
```

**`Stacks.ComparingTopologies.overMapPullback_comp_comparisonPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/ComparisonSituation.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/ComparisonSituation.lean#L349). The attribute's comment: “the identity `ε_{X,*} f_J^{-1} = f_K^{-1} ε_{Y,*}`”.

> **Stacks 0EZ2.** On direct images for the comparison morphisms and inverse images for
> restriction, the square commutes strictly:
> `ε_{X,*} ∘ f_J^{-1} = f_K^{-1} ∘ ε_{Y,*}`.

```lean
theorem overMapPullback_comp_comparisonPushforward
    {J K : GrothendieckTopology C} (h : K ≤ J) {X Y : C} (f : X ⟶ Y) :
    J.overMapPullback (Type (max u v)) f ⋙ comparisonPushforward (over_le_over h X) =
      comparisonPushforward (over_le_over h Y) ⋙ K.overMapPullback (Type (max u v)) f
```

## Tag 0EZ3, a situation

[Tag 0EZ3](https://stacks.math.columbia.edu/tag/0EZ3) in the Stacks Project.

**`Stacks.ComparingTopologies.CohomologyComparison`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/ComparisonSituation.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/ComparisonSituation.lean#L116).

> **Stacks 0EZ3.** The standing situation for comparing cohomology computed in a finer
> coverage with cohomology computed in a coarser one.

```lean
structure CohomologyComparison (C : Type u) [Category.{v} C]
```

## Tag 0EZ9, a lemma

[Tag 0EZ9](https://stacks.math.columbia.edu/tag/0EZ9) in the Stacks Project.

**`Stacks.ComparingTopologies.CohomologyComparison.fineWeakSerre`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/ComparisonClass.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/ComparisonClass.lean#L71). The attribute's comment: “the category `𝒜_X`”.

> **Stacks 0EZ9.** The class `𝒜_X` of abelian sheaves on the finer localized site: those of
> the form `ε⁻¹ F` for `F` in the given weak Serre class `𝒜'_X` on the coarser localized site,
> with `ε` the change-of-topology morphism.

```lean
noncomputable abbrev fineWeakSerre (S : CohomologyComparison C) (X : C) :
    ObjectProperty (Sheaf (S.fineCoverage.toGrothendieck.over X) Ab.{max u v})
```

**`Stacks.ComparingTopologies.CohomologyComparison.fineWeakSerre_iff_weakSerre_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/ComparisonClass.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/ComparisonClass.lean#L78). The attribute's comment: “the membership criterion for `𝒜_X`”.

> **Stacks 0EZ9.** A sheaf on the finer localized site belongs to `𝒜_X` if and only if its
> change-of-topology direct image belongs to `𝒜'_X`.

```lean
theorem fineWeakSerre_iff_weakSerre_pushforward
    (S : CohomologyComparison C) (X : C)
    (F : Sheaf (S.fineCoverage.toGrothendieck.over X) Ab.{max u v}) :
    S.fineWeakSerre X F ↔
      S.weakSerre X
        ((abelianComparisonPushforward S.fineCoverage S.coarseCoverage
          S.coarse_le_fine X).obj F)
```

**`Stacks.ComparingTopologies.CohomologyComparison.fineWeakSerre_overMapPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/ComparisonClass.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/ComparisonClass.lean#L154). The attribute's comment: “stability of `𝒜_X` under restriction”.

> **Stacks 0EZ9.** Restriction along a morphism of the site preserves the class `𝒜` of
> abelian sheaves on the finer localized sites.

```lean
theorem fineWeakSerre_overMapPullback (S : CohomologyComparison C)
    {X Y : C} (f : X ⟶ Y)
    (F : Sheaf (S.fineCoverage.toGrothendieck.over Y) Ab.{max u v})
    (hF : S.fineWeakSerre Y F) :
    S.fineWeakSerre X
      ((S.fineCoverage.toGrothendieck.overMapPullback Ab.{max u v} f).obj F)
```

## Tag 0EZA, a lemma

[Tag 0EZA](https://stacks.math.columbia.edu/tag/0EZA) in the Stacks Project.

**`Stacks.ComparingTopologies.higherDirectImageComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/HigherDirectImages.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/HigherDirectImages.lean#L210). The attribute's comment: “canonical comparison transformation”.

> **The comparison transformation.** The canonical degree-`i` map from the coarse
> higher direct image of the change-of-topology direct image to the change-of-topology direct
> image of the fine higher direct image,
>
> `R^i f_{τ',*} ε_{X,*} ℱ ⟶ ε_{Y,*} R^i f_{τ,*} ℱ`,
>
> natural in the abelian sheaf `ℱ` on the finer localized site over `X`.
>
> It is the composite of the two edge morphisms of the Grothendieck spectral sequence of the
> square of topoi `abelianComparisonPushforward_square`: the edge `E₂^{i,0} ⟶ H^i` for the pair
> `(ε_{X,*}, f_{τ',*})`, followed by the edge `H^i ⟶ E₂^{0,i}` for the pair `(f_{τ,*}, ε_{Y,*})`.

```lean
def higherDirectImageComparison (S : CohomologyComparison C) {X Y : C} (f : X ⟶ Y) (i : ℕ) :
    abelianComparisonPushforward S.fineCoverage S.coarseCoverage S.coarse_le_fine X ⋙
        (overPushforward S.coarseCoverage.toGrothendieck f).rightDerived i ⟶
      (overPushforward S.fineCoverage.toGrothendieck f).rightDerived i ⋙
        abelianComparisonPushforward S.fineCoverage S.coarseCoverage S.coarse_le_fine Y
```

**`Stacks.ComparingTopologies.isIso_higherDirectImageComparison_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/VanishingConditionInduction.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/VanishingConditionInduction.lean#L250). The attribute's comment: “the comparison is an isomorphism through degree `n`”.

> **Stacks 0EZA.** Assume the vanishing condition `(V_n)`. For a morphism `f : X ⟶ Y` of the
> distinguished class, an abelian sheaf `ℱ` of `𝒜_X` on the finer localized site over `X`, and a
> degree `i ≤ n`, the comparison
>
> `R^i f_{τ',*} ε_{X,*} ℱ ⟶ ε_{Y,*} R^i f_{τ,*} ℱ`
>
> is an isomorphism.
>
> Both factors of the comparison are invertible, for different reasons. The first edge morphism is
> invertible in degree `i` as soon as `R^q ε_{X,*} ℱ` vanishes for `1 ≤ q ≤ i`, which is `(V_n)`;
> this is `Stacks.Cohomology.RightDerivedEdgeIso.isIso_edge_app`, and no spectral sequence is
> needed for it. The second edge morphism is invertible as soon as the object it starts from lies
> in the essential image of the change-of-topology direct image, by
> `Stacks.Cohomology.RightDerivedCoEdge.isIso_secondEdge_app_of_isIso_unit`; and that object is
> `R^i f_{τ',*} ε_{X,*} ℱ` — by the first edge morphism, which has just been seen to be
> invertible — which lies in the weak Serre class `𝒜'_Y` because `ε_{X,*} ℱ` lies in `𝒜'_X` and the
> distinguished class is stable under higher direct images.

```lean
theorem isIso_higherDirectImageComparison_app (S : CohomologyComparison C) (n : ℕ)
    (hV : S.vanishingCondition n) {X Y : C} (f : X ⟶ Y) (hf : S.morphismProperty f)
    (i : ℕ) (hi : i ≤ n) (F : Sheaf (S.fineCoverage.toGrothendieck.over X) Ab.{max u v})
    (hF : S.fineWeakSerre X F) :
    IsIso ((higherDirectImageComparison S f i).app F)
```

## Tag 0EZB, a lemma

[Tag 0EZB](https://stacks.math.columbia.edu/tag/0EZB) in the Stacks Project.

**`Stacks.ComparingTopologies.isIso_homology_derivedCohomologyComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/ComparingCohomology.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/ComparingCohomology.lean#L396).

> **Stacks 0EZB.** In the comparison situation of Stacks 0EZ3, assume the vanishing condition
> `(V_n)`. Let `X` be an object of `C` and let `L` be an object of `D(C_{τ'}/X)` whose cohomology
> sheaves vanish in negative degrees and lie in the weak Serre class `𝒜'_X` in the degrees
> `0 ≤ i ≤ n`. Then the canonical map
>
> `H^n_{τ'}(X, L) ⟶ H^n_τ(X, ε_X^{-1}L)`
>
> of `Stacks.ComparingTopologies.derivedCohomologyComparison` is an isomorphism.
>
> The truncation `τ_{≤n}L` has all of its cohomology in `𝒜'_X` and none outside the degrees
> `0, …, n`, so the comparison is invertible in degree `n` there; and the truncation morphism
> `τ_{≤n}L ⟶ L` becomes invertible on `H^n` after applying either `RΓ_{τ'}(X, -)` or `ε_X^{-1}`
> followed by `RΓ_τ(X, -)`. The naturality square of the comparison then carries the conclusion
> from `τ_{≤n}L` to `L`.

```lean
theorem isIso_homology_derivedCohomologyComparison (S : CohomologyComparison C) (n : ℕ)
    (hV : S.vanishingCondition n) (X : C)
    (L : DerivedCategory (AbelianSheaves S.coarseCoverage.toGrothendieck X))
    (hneg : ∀ i : ℤ, i < 0 → IsZero ((DerivedCategory.homologyFunctor
      (AbelianSheaves S.coarseCoverage.toGrothendieck X) i).obj L))
    (hmem : ∀ i : ℕ, i ≤ n → S.weakSerre X ((DerivedCategory.homologyFunctor
      (AbelianSheaves S.coarseCoverage.toGrothendieck X) (i : ℤ)).obj L)) :
    IsIso ((DerivedCategory.Plus.homologyFunctor Ab.{max u v} (n : ℤ)).map
      ((derivedCohomologyComparison S X).app
        (DerivedCategory.Plus.ofNonnegative L hneg)))
```

## Tag 0EZC, a lemma

[Tag 0EZC](https://stacks.math.columbia.edu/tag/0EZC) in the Stacks Project.

**`Stacks.ComparingTopologies.cohomologyComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/Cohomology.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/Cohomology.lean#L313). The attribute's comment: “canonical cohomology map”.

> The natural change-of-topology map `H^i_{τ'}(X, ε_{X,*} F) ⟶ H^i_τ(X, F)`, given by
> pulling back cohomology classes along `ε_X`.

```lean
def cohomologyComparison (S : CohomologyComparison C) (X : C) (i : ℕ) :
    abelianComparisonPushforward S.fineCoverage S.coarseCoverage S.coarse_le_fine X ⋙
        (globalSectionsOver S.coarseCoverage.toGrothendieck X).rightDerived i ⟶
      (globalSectionsOver S.fineCoverage.toGrothendieck X).rightDerived i
```

**`Stacks.ComparingTopologies.cohomologyComparison_eq_injectiveResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/Cohomology.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/Cohomology.lean#L347). The attribute's comment: “canonical map via injective resolutions”.

> An augmentation-preserving comparison from an injective resolution of the coarse direct
> image to the direct image of an injective resolution computes the canonical cohomology map.
> This characterizes its components in every degree.

```lean
theorem cohomologyComparison_eq_injectiveResolution (S : CohomologyComparison C) (X : C) (i : ℕ)
    (F : Sheaf (S.fineCoverage.toGrothendieck.over X) Ab.{max u v})
    (I : InjectiveResolution F)
    (J : InjectiveResolution ((abelianComparisonPushforward S.fineCoverage
      S.coarseCoverage S.coarse_le_fine X).obj F))
    (φ : J.cocomplex ⟶
      ((abelianComparisonPushforward S.fineCoverage S.coarseCoverage
        S.coarse_le_fine X).mapHomologicalComplex (.up ℕ)).obj I.cocomplex)
    (hφ : J.ι.f 0 ≫ φ.f 0 =
      (abelianComparisonPushforward S.fineCoverage S.coarseCoverage
        S.coarse_le_fine X).map (I.ι.f 0)) :
    (cohomologyComparison S X i).app F =
      (J.isoRightDerivedObj (globalSectionsOver S.coarseCoverage.toGrothendieck X) i).hom ≫
        HomologicalComplex.homologyMap
          (((globalSectionsOver S.coarseCoverage.toGrothendieck X).mapHomologicalComplex
            (.up ℕ)).map φ) i ≫
          (I.isoRightDerivedObj (globalSectionsOver S.fineCoverage.toGrothendieck X) i).inv
```

**`Stacks.ComparingTopologies.mono_cohomologyComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/Cohomology.lean, line 922](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/Cohomology.lean#L922). The attribute's comment: “injectivity”.

> **Stacks 0EZC.** Under `(Vₙ)`, the change-of-topology map on cohomology in degree `n + 1`
> is injective.

```lean
theorem mono_cohomologyComparison (S : CohomologyComparison C) (n : ℕ)
    (hV : S.vanishingCondition n) (X : C)
    (F : Sheaf (S.fineCoverage.toGrothendieck.over X) Ab.{max u v})
    (hF : S.fineWeakSerre X F) :
    Mono ((cohomologyComparison S X (n + 1)).app F)
```

**`Stacks.ComparingTopologies.mem_range_cohomologyComparison_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/Cohomology.lean, line 933](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/Cohomology.lean#L933). The attribute's comment: “image of the map”.

> **Stacks 0EZC.** Under `(Vₙ)`, a class in degree `n + 1` is in the image of the
> change-of-topology map on cohomology precisely when it becomes zero on the members of a
> covering for the coarser topology.

```lean
theorem mem_range_cohomologyComparison_iff (S : CohomologyComparison C) (n : ℕ)
    (hV : S.vanishingCondition n) (X : C)
    (F : Sheaf (S.fineCoverage.toGrothendieck.over X) Ab.{max u v})
    (hF : S.fineWeakSerre X F)
    (ξ : sheafCohomology (S.fineCoverage.toGrothendieck.over X) F (Over.mk (𝟙 X)) (n + 1)) :
    (∃ η : sheafCohomology (S.coarseCoverage.toGrothendieck.over X)
        ((abelianComparisonPushforward S.fineCoverage S.coarseCoverage
          S.coarse_le_fine X).obj F) (Over.mk (𝟙 X)) (n + 1),
        (cohomologyComparison S X (n + 1)).app F η = ξ) ↔
      (∃ R : Presieve X, R ∈ S.coarseCoverage X ∧
        ∀ ⦃V : C⦄ (f : V ⟶ X), R f →
          sheafCohomologyRestriction (S.fineCoverage.toGrothendieck.over X)
            (Over.homMk (U := Over.mk f) (V := Over.mk (𝟙 X)) f (by simp))
            (n + 1) F ξ = 0)
```

## Tag 0EZD, a lemma

[Tag 0EZD](https://stacks.math.columbia.edu/tag/0EZD) in the Stacks Project.

**`Stacks.ComparingTopologies.exists_coarseCovering_restrict_eq_zero_of_equalizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/DescentOfCohomologyClasses.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/DescentOfCohomologyClasses.lean#L175).

> **Stacks 0EZD.** Let `f : X ⟶ Y` be a morphism of the distinguished class which by itself
> is a covering for the finer topology, and let `F` be a sheaf of the weak Serre class `𝒜'_Y` on
> the coarser site localized at `Y`. If a cohomology class of degree `n + 1` over `X` has equal
> restrictions along the two projections from `X ×_Y X`, then there is a covering of `Y` for the
> coarser topology such that the class restricts to zero over every base change `Yᵢ ×_Y X`.

```lean
theorem exists_coarseCovering_restrict_eq_zero_of_equalizer (S : CohomologyComparison C)
    {X Y : C} (f : X ⟶ Y) (hf : S.morphismProperty f)
    (hcover : Presieve.singleton f ∈ S.fineCoverage Y)
    (F : Sheaf (S.coarseCoverage.toGrothendieck.over Y) Ab.{max u v}) (hF : S.weakSerre Y F) (n : ℕ)
    (P : Over Y) (p₁ p₂ : P ⟶ Over.mk f) (hP : IsPullback p₁.left p₂.left f f)
    (θ : Stacks.sheafCohomology (S.coarseCoverage.toGrothendieck.over Y) F (Over.mk f) (n + 1))
    (hθ : Stacks.sheafCohomologyRestriction (S.coarseCoverage.toGrothendieck.over Y) p₁
        (n + 1) F θ =
      Stacks.sheafCohomologyRestriction (S.coarseCoverage.toGrothendieck.over Y) p₂
        (n + 1) F θ) :
    ∃ R : Presieve Y, R ∈ S.coarseCoverage Y ∧
      ∀ ⦃Z : C⦄ (g : Z ⟶ Y), R g →
        ∃ (Q : Over Y) (a : Q ⟶ Over.mk f) (b : Q ⟶ Over.mk g),
          IsPullback a.left b.left f g ∧
            Stacks.sheafCohomologyRestriction (S.coarseCoverage.toGrothendieck.over Y) a
              (n + 1) F θ = 0
```

## Tag 0EZE, a lemma

[Tag 0EZE](https://stacks.math.columbia.edu/tag/0EZE) in the Stacks Project.

**`Stacks.ComparingTopologies.CohomologyComparison.vanishingCondition_succ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/HigherDirectImageVanishing.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/HigherDirectImageVanishing.lean#L62).

> **Stacks 0EZE.** In the comparison situation of Stacks 0EZ3 the vanishing condition `(V_n)`
> implies `(V_{n+1})`.

```lean
theorem CohomologyComparison.vanishingCondition_succ (S : CohomologyComparison C) (n : ℕ)
    (hV : S.vanishingCondition n) : S.vanishingCondition (n + 1)
```

## Tag 0EZF, a lemma

[Tag 0EZF](https://stacks.math.columbia.edu/tag/0EZF) in the Stacks Project.

**`Stacks.ComparingTopologies.rightDerivedPushforward_mem_derivedCategoryBPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/DerivedPushforwardPreservesComparison.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/DerivedPushforwardPreservesComparison.lean#L116). The attribute's comment: “part (2), membership: `R f_{τ',*}` carries `D⁺_{𝒜'_X}` into `D⁺_{𝒜'_Y}`”.

> **Stacks 0EZF**, the first assertion of part (2). In a cohomology comparison situation,
> total right derived direct image along a morphism of the distinguished class `P` carries
> `D⁺_{𝒜'_X}` into `D⁺_{𝒜'_Y}`.
>
> No hypothesis beyond those of the tag is used: in particular the vanishing conditions `(V_n)`,
> which the tag asserts first, are not needed for this half. See the implementation notes for the
> other clauses of the tag and where they live.

```lean
theorem rightDerivedPushforward_mem_derivedCategoryBPlus
    (S : CohomologyComparison C) {X Y : C} (f : X ⟶ Y)
    (hf : S.morphismProperty f)
    (K : DerivedCategory.Plus
      (Sheaf (S.coarseCoverage.toGrothendieck.over X) Ab.{max u v}))
    (hK : DerivedCategoryB.derivedCategoryBPlus (S.weakSerre X) K.obj) :
    DerivedCategoryB.derivedCategoryBPlus (S.weakSerre Y)
      ((((Over.map f).sheafPushforwardCocontinuous Ab.{max u v}
          (S.coarseCoverage.toGrothendieck.over X)
          (S.coarseCoverage.toGrothendieck.over Y)).rightDerivedFunctorPlus.obj K).obj)
```

**`Stacks.ComparingTopologies.CohomologyComparison.vanishingCondition_all`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/HigherDirectImageVanishing.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/HigherDirectImageVanishing.lean#L70). The attribute's comment: “(V\_n) holds for all n”.

> **Stacks 0EZF, the leading assertion.** In the comparison situation of Stacks 0EZ3 the
> vanishing condition `(V_n)` holds for every `n`: `(V_0)` is empty and Stacks 0EZE is the
> induction step.

```lean
theorem CohomologyComparison.vanishingCondition_all (S : CohomologyComparison C) (n : ℕ) :
    S.vanishingCondition n
```

**`Stacks.ComparingTopologies.isIso_derivedComparisonUnit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/HigherDirectImageVanishing.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/HigherDirectImageVanishing.lean#L79). The attribute's comment: “(1)”.

> **Stacks 0EZF (1).** For `X` in `C` and `K'` in `D⁺_{𝒜'_X}(C_{τ'}/X)` the canonical map
> `K' ⟶ Rε_{X,*}(ε_X^{-1}K')` is an isomorphism.

```lean
theorem isIso_derivedComparisonUnit_app (S : CohomologyComparison C) (X : C)
    (K : DerivedCategory.Plus (AbelianSheaves S.coarseCoverage.toGrothendieck X))
    (hK : ∀ i : ℤ, S.weakSerre X ((DerivedCategory.Plus.homologyFunctor _ i).obj K)) :
    IsIso ((derivedComparisonUnit S X).app K)
```

**`Stacks.ComparingTopologies.isIso_derivedComparisonBaseChange_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/HigherDirectImageVanishing.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/HigherDirectImageVanishing.lean#L89). The attribute's comment: “(2), base change”.

> **Stacks 0EZF (2), the base change.** For a morphism `f : X ⟶ Y` of `C` and `K'` in
> `D⁺_{𝒜'_X}(C_{τ'}/X)` the base change map `ε_Y^{-1}(Rf_{τ',*}K') ⟶ Rf_{τ,*}(ε_X^{-1}K')` is an
> isomorphism. The source states this for `f` in the distinguished class; it holds for every `f`.

```lean
theorem isIso_derivedComparisonBaseChange_app (S : CohomologyComparison C) {X Y : C} (f : X ⟶ Y)
    (K : DerivedCategory.Plus (AbelianSheaves S.coarseCoverage.toGrothendieck X))
    (hK : ∀ n : ℤ, S.weakSerre X
      ((DerivedCategory.Plus.homologyFunctor
        (AbelianSheaves S.coarseCoverage.toGrothendieck X) n).obj K)) :
    IsIso ((derivedComparisonBaseChange S f).app K)
```

## Tag 0EZG, a lemma

[Tag 0EZG](https://stacks.math.columbia.edu/tag/0EZG) in the Stacks Project.

**`Stacks.ComparingTopologies.CohomologyComparison.fineWeakSerre_isWeakSerreClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/DerivedComparisonEquivalence.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/DerivedComparisonEquivalence.lean#L61). The attribute's comment: “first assertion: `𝒜_X` is a weak Serre subcategory of `Ab(C_τ/X)`”.

> **First assertion of Stacks 0EZG.** In the comparison situation of Stacks 0EZ3, for any
> object `X` of `C` the class `𝒜_X ⊂ Ab(C_τ/X)` of Stacks 0EZ9 is a weak Serre subcategory.

```lean
theorem fineWeakSerre_isWeakSerreClass (S : CohomologyComparison C) (X : C) :
    (S.fineWeakSerre X).IsWeakSerreClass
```

**`Stacks.ComparingTopologies.boundedBelowComparisonEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/DerivedComparisonEquivalence.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/DerivedComparisonEquivalence.lean#L137). The attribute's comment: “second assertion: `Rε_{X,*} : D⁺_{𝒜_X}(C_τ/X) ⟶ D⁺_{𝒜'_X}(C_{τ'}/X)` is an equivalence”.

> **Second assertion of Stacks 0EZG.** In the comparison situation of Stacks 0EZ3, for any
> object `X` of `C` the derived change-of-topology direct image
>
> `Rε_{X,*} : D⁺_{𝒜_X}(C_τ/X) ⟶ D⁺_{𝒜'_X}(C_{τ'}/X)`
>
> is an equivalence of categories, with quasi-inverse `ε_X^{-1}`.

```lean
def boundedBelowComparisonEquivalence (S : CohomologyComparison C) (X : C) :
    (derivedFineWeakSerre S X).FullSubcategory ≌
      (derivedWeakSerre S X).FullSubcategory
```

**`Stacks.ComparingTopologies.boundedBelowComparisonEquivalence_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/DerivedComparisonEquivalence.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/DerivedComparisonEquivalence.lean#L162). The attribute's comment: “the second assertion: the functor of the equivalence is `Rε_{X,*}`”.

> **Stacks 0EZG**, the identification of the functor of the equivalence with the restriction
> of the derived change-of-topology direct image `Rε_{X,*}`.

```lean
theorem boundedBelowComparisonEquivalence_functor (S : CohomologyComparison C) (X : C) :
    (boundedBelowComparisonEquivalence S X).functor =
      derivedComparisonPushforwardLift S X
```

**`Stacks.ComparingTopologies.boundedBelowComparisonEquivalence_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/DerivedComparisonEquivalence.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/DerivedComparisonEquivalence.lean#L170). The attribute's comment: “the second assertion: the quasi-inverse of the equivalence is `ε_X^{-1}`”.

> **Stacks 0EZG**, the identification of the quasi-inverse of the equivalence with the
> restriction of the change-of-topology inverse image `ε_X^{-1}`.

```lean
theorem boundedBelowComparisonEquivalence_inverse (S : CohomologyComparison C) (X : C) :
    (boundedBelowComparisonEquivalence S X).inverse =
      derivedComparisonPullbackLift S X
```

## Tag 0EZH, a lemma

[Tag 0EZH](https://stacks.math.columbia.edu/tag/0EZH) in the Stacks Project.

**`Stacks.ComparingTopologies.isIso_cohomologyChangeOfTopology_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/CohomologyComparisonIsomorphism.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/CohomologyComparisonIsomorphism.lean#L91). The attribute's comment: “(1)”.

> **Clause (1) of Stacks 0EZH.** In the comparison situation of Stacks 0EZ3, let `X` be an
> object of `C` and let `ℱ'` be a sheaf of the weak Serre class `𝒜'_X` on the coarser localized
> site. Then for every `n` the canonical map
>
> `H^n_{τ'}(X, ℱ') ⟶ H^n_τ(X, ε_X^{-1}ℱ')`
>
> is an isomorphism.

```lean
theorem isIso_cohomologyChangeOfTopology_app (S : CohomologyComparison C) (X : C)
    (F : Sheaf (S.coarseCoverage.toGrothendieck.over X) Ab.{max u v})
    (hF : S.weakSerre X F) (n : ℕ) :
    IsIso ((cohomologyChangeOfTopology S X n).app F)
```

**`Stacks.ComparingTopologies.isIso_derivedCohomologyComparison_app_of_weakSerre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/CohomologyComparisonIsomorphism.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/CohomologyComparisonIsomorphism.lean#L118). The attribute's comment: “(2), as an isomorphism of derived global sections”.

> **Clause (2) of Stacks 0EZH, as an isomorphism in `D⁺(Ab)`.** In the comparison situation of
> Stacks 0EZ3, let `X` be an object of `C` and let `K'` be a bounded below object of the derived
> category of abelian sheaves on `C_{τ'}/X` all of whose cohomology sheaves lie in `𝒜'_X`, that
> is, an object of `D⁺_{𝒜'_X}(C_{τ'}/X)`. Then the canonical map
>
> `RΓ_{τ'}(X, K') ⟶ RΓ_τ(X, ε_X^{-1}K')`
>
> is an isomorphism.

```lean
theorem isIso_derivedCohomologyComparison_app_of_weakSerre (S : CohomologyComparison C) (X : C)
    (K : DerivedCategory.Plus (AbelianSheaves S.coarseCoverage.toGrothendieck X))
    (hK : ∀ i : ℤ, S.weakSerre X ((DerivedCategory.Plus.homologyFunctor _ i).obj K)) :
    IsIso ((derivedCohomologyComparison S X).app K)
```

**`Stacks.ComparingTopologies.isIso_homology_derivedCohomologyComparison_app_of_weakSerre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/CohomologyComparisonIsomorphism.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChangeOfTopology/CohomologyComparisonIsomorphism.lean#L131). The attribute's comment: “(2)”.

> **Clause (2) of Stacks 0EZH.** With `X` and `K'` as above, the canonical map
>
> `H^n_{τ'}(X, K') ⟶ H^n_τ(X, ε_X^{-1}K')`
>
> is an isomorphism for every `n`.

```lean
theorem isIso_homology_derivedCohomologyComparison_app_of_weakSerre
    (S : CohomologyComparison C) (X : C)
    (K : DerivedCategory.Plus (AbelianSheaves S.coarseCoverage.toGrothendieck X))
    (hK : ∀ i : ℤ, S.weakSerre X ((DerivedCategory.Plus.homologyFunctor _ i).obj K))
    (n : ℤ) :
    IsIso ((DerivedCategory.Plus.homologyFunctor Ab.{max u v} n).map
      ((derivedCohomologyComparison S X).app K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.30, Tag 0EZ1](https://stacks.math.columbia.edu/tag/0EZ1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

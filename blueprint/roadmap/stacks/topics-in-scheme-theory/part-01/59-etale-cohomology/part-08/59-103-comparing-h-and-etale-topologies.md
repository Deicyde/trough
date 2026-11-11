---
declaration: section
origin: cited
lean: AlgebraicGeometry.smallEtaleInverseImage_isZariskiSheaf_h, AlgebraicGeometry.smallEtaleInverseImage_isSheaf_h_and_isIso_unit, AlgebraicGeometry.hToBigEtaleMorphism, AlgebraicGeometry.hToSmallEtaleMorphism, AlgebraicGeometry.bigHBigEtale_pushforwardCommIso, AlgebraicGeometry.bigHSmallEtale_pushforwardCommIso, AlgebraicGeometry.isIso_bigHSmallEtaleBaseChange, AlgebraicGeometry.BigHSite.exists_hEtaleCohomologyComparison
statement: formalized
proof: formalized
---

# 59.103 Comparing h and étale topologies

Section 59.103 of the Stacks Project, [Tag 0EW7](https://stacks.math.columbia.edu/tag/0EW7). 7 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EW8, a lemma

[Tag 0EW8](https://stacks.math.columbia.edu/tag/0EW8) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleInverseImage_isZariskiSheaf_h`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopologyEtaleComparison.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopologyEtaleComparison.lean#L107). The attribute's comment: “the Zariski half of the h sheaf condition, condition (1) of Stacks 0EU5; descent along a proper surjective morphism of finite presentation is not proved”.

> **Stacks 0EW8, the Zariski half of the h sheaf condition.** For a sheaf of sets `F` on the
> small étale site of `S`, the presheaf underlying `π_S⁻¹F` — by the sections formula the rule
> `X ↦ Γ(X_ét, f_X⁻¹F)` of the source — satisfies descent for every family of the big h category
> over `S` whose underlying family of schemes is a Zariski covering.
>
> A Zariski covering family is an fpqc covering family, and `π_S⁻¹F` is a sheaf for the fpqc
> topology of the slice by Stacks 09XN,
> `AlgebraicGeometry.bigEtaleToSmallEtale_inverseImage_isSheaf_fpqc`.

```lean
public theorem smallEtaleInverseImage_isZariskiSheaf_h :
    BigHOver.IsZariskiSheaf B S hS
      ((bigEtaleToSmallEtaleMorphism (hAssociatedBigEtaleSite B) S hS).inverseImage.obj
        F).obj
```

**`AlgebraicGeometry.smallEtaleInverseImage_isSheaf_h_and_isIso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopologyEtaleComparisonProperBaseChange.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/HTopologyEtaleComparisonProperBaseChange.lean#L86).

> **Stacks 0EW8.** For a sheaf of sets `F` on the small étale site of `S`, the rule
> `(f : X ⟶ S) ↦ Γ(X_ét, f⁻¹F)` — the presheaf underlying `π_S⁻¹F` on the big étale category over
> `S`, by the sections formula `AlgebraicGeometry.etaleInverseImageSectionsIso` and Stacks 09XN —
> is a sheaf for the h topology of the big h category over `S`, and the unit of `ε_S⁻¹ ⊣ ε_{S,*}`
> at `π_S⁻¹F` is an isomorphism, so that this h sheaf is `ε_S⁻¹π_S⁻¹F`.
>
> The h sheaf condition is Stacks 0EU5: the Zariski half is
> `AlgebraicGeometry.smallEtaleInverseImage_isZariskiSheaf_h` and the proper half is
> `AlgebraicGeometry.smallEtaleInverseImage_isProperFinitePresentationSheaf`.

```lean
public theorem smallEtaleInverseImage_isSheaf_h_and_isIso_unit :
    Presieve.IsSheaf (BigHOver.topology B S hS)
        ((bigEtaleToSmallEtaleMorphism (hAssociatedBigEtaleSite B) S hS).inverseImage.obj
          F).obj ∧
      IsIso ((hToBigEtaleMorphism B (B.obj S hS)).adj.unit.app
        ((bigEtaleToSmallEtaleMorphism (hAssociatedBigEtaleSite B) S hS).inverseImage.obj F))
```

## Tag 0EW9, a lemma

[Tag 0EW9](https://stacks.math.columbia.edu/tag/0EW9) in the Stacks Project.

**`AlgebraicGeometry.hToBigEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/HToEtaleSquares.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/HToEtaleSquares.lean#L192). The attribute's comment: “change-of-topology morphism”.

> The comparison `ε_X` from the big h topos to the big étale topos, induced by the identity
> functor on the common slice category.

```lean
public def hToBigEtaleMorphism (B : BigHSite.{u}) (X : B.Schemes) :
    MorphismOfTopoi
      (Sheaf (B.topology.over X) (Type (u + 1)))
      (Sheaf (BigEtaleOver.topology (hAssociatedBigEtaleSite B) X.1 X.2) (Type (u + 1)))
```

**`AlgebraicGeometry.hToSmallEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/HToEtaleSquares.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/HToEtaleSquares.lean#L227). The attribute's comment: “factorization through the big étale topos”.

> The comparison `a_X = π_X ∘ ε_X` from the big h topos to the small étale topos.

```lean
public def hToSmallEtaleMorphism (B : BigHSite.{u}) (X : B.Schemes) :
    MorphismOfTopoi
      (Sheaf (B.topology.over X) (Type (u + 1)))
      (Sheaf (SmallEtale.topology (hAssociatedBigEtaleSite B) X.1 X.2) (Type (u + 1)))
```

**`AlgebraicGeometry.bigHBigEtale_pushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/HToEtaleSquares.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/HToEtaleSquares.lean#L256). The attribute's comment: “the big h–big étale square”.

> **Stacks 0EW9, first diagram.** The square formed by the big h and big étale base-change
> morphisms over the change-of-topology comparisons `ε_X` and `ε_Y` commutes on direct
> images.

```lean
public def bigHBigEtale_pushforwardCommIso (B : BigHSite.{u}) {X Y : B.Schemes} (f : X ⟶ Y) :
    ((bigEtaleMorphism (hAssociatedBigEtaleSite B) X Y f).comp
      (hToBigEtaleMorphism B X)).pushforward ≅
      ((hToBigEtaleMorphism B Y).comp (bigHMorphismOfTopoi B f)).pushforward
```

**`AlgebraicGeometry.bigHSmallEtale_pushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/HToEtaleSquares.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/HToEtaleSquares.lean#L294). The attribute's comment: “the big h–small étale square”.

> **Stacks 0EW9, second diagram.** The square formed by the big h and small étale
> base-change morphisms over the comparisons `a_X = π_X ∘ ε_X` and `a_Y = π_Y ∘ ε_Y` commutes on
> direct images.

```lean
public def bigHSmallEtale_pushforwardCommIso (B : BigHSite.{u}) {X Y : B.Schemes} (f : X ⟶ Y) :
    ((hSmallEtaleMorphism B f).comp (hToSmallEtaleMorphism B X)).pushforward ≅
      ((hToSmallEtaleMorphism B Y).comp (bigHMorphismOfTopoi B f)).pushforward
```

## Tag 0EWA, a lemma

[Tag 0EWA](https://stacks.math.columbia.edu/tag/0EWA) in the Stacks Project.

**`AlgebraicGeometry.isIso_bigHSmallEtaleBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProperHDirectImage.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/ProperHDirectImage.lean#L68).

> **Stacks 0EWA.** Let `f : X ⟶ Y` be a proper morphism of the big h site. Then the base change
> map `a_Y⁻¹ ∘ f_{small,*} ⟶ f_{big,h,*} ∘ a_X⁻¹` of the square of topoi of Stacks 0EW9 is an
> isomorphism.

```lean
public theorem isIso_bigHSmallEtaleBaseChange [IsProper (B.inclusion.map f)] :
    IsIso (bigHSmallEtaleBaseChange B f)
```

## Tag 0F0J, a lemma

[Tag 0F0J](https://stacks.math.columbia.edu/tag/0F0J) in the Stacks Project.

**`AlgebraicGeometry.BigHSite.exists_hEtaleCohomologyComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HComparisonSituationProperties.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HComparisonSituationProperties.lean#L70).

> **Stacks 0F0J.** Consider the comparison of the h topology of a big h site `B` with the étale
> topology on the same category of schemes. Let `𝒫` be the class of proper morphisms, and for `X`
> in the site let `𝒜'_X ⊂ Ab((Sch/X)_étale)` be the full subcategory of sheaves of the form
> `π_X⁻¹F` with `F` a torsion abelian sheaf on `X_étale`. Then `𝒜'_X` is a weak Serre subcategory
> and properties (0EZ4)–(0EZ8) of the comparison situation of Stacks 0EZ3 hold: there is a
> comparison situation with the h topology as finer topology, the étale topology as coarser
> topology, `𝒫` as distinguished class and the `𝒜'_X` as weak Serre classes.

```lean
public theorem exists_hEtaleCohomologyComparison (B : BigHSite.{u}) :
    ∃ S : Stacks.ComparingTopologies.CohomologyComparison (hAssociatedBigEtaleSite B).Scheme,
      S.fineCoverage = B.precoverage ∧
      S.coarseCoverage = (hAssociatedBigEtaleSite B).precoverage ∧
      S.morphismProperty = (fun _ _ f => IsProper ((hAssociatedBigEtaleSite B).inclusion.map f)) ∧
      ∀ X : (hAssociatedBigEtaleSite B).Scheme,
        HEq (S.weakSerre X)
          (smallEtaleTorsionPullbackClass (hAssociatedBigEtaleSite B) X
            ((hAssociatedBigEtaleSite B).topology.over X))
```

## Tag 0EWF, a lemma

[Tag 0EWF](https://stacks.math.columbia.edu/tag/0EWF) in the Stacks Project.

**`AlgebraicGeometry.hTorsionComparison_smallEtaleInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HTorsionInverseImageComparison.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HTorsionInverseImageComparison.lean#L87). The attribute's comment: “(1)”.

> For an object `X` of the big h site and an abelian torsion sheaf `F` on `X_étale`,
> `ε_{X,*}a_X⁻¹F = π_X⁻¹F` — the unit `π_X⁻¹F ⟶ ε_{X,*}ε_X⁻¹π_X⁻¹F` of the change of topology is an
> isomorphism — and `R^i ε_{X,*}(a_X⁻¹F) = 0` for `i > 0`.

```lean
public theorem hTorsionComparison_smallEtaleInclusion (X : (hAssociatedBigEtaleSite B).Scheme)
    (F : Sheaf (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property) Ab.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property) F) :
    IsIso ((abelianComparisonAdjunction B.precoverage
        (hAssociatedBigEtaleSite B).precoverage
        (BigHSite.etalePrecoverage_le_precoverage B) X).unit.app
        (((SmallEtale.inclusion (hAssociatedBigEtaleSite B) X.obj X.property).sheafPullback
          Ab.{u + 1} (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property)
          ((hAssociatedBigEtaleSite B).topology.over X)).obj F)) ∧
      ∀ i : ℕ, 0 < i → IsZero (((abelianComparisonPushforward B.precoverage
          (hAssociatedBigEtaleSite B).precoverage
          (BigHSite.etalePrecoverage_le_precoverage B) X).rightDerived i).obj
        ((abelianComparisonPullback B.precoverage
          (hAssociatedBigEtaleSite B).precoverage X).obj
          (((SmallEtale.inclusion (hAssociatedBigEtaleSite B) X.obj X.property).sheafPullback
            Ab.{u + 1} (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property)
            ((hAssociatedBigEtaleSite B).topology.over X)).obj F)))
```

**`AlgebraicGeometry.isIso_hTorsionHigherSmallEtaleBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HTorsionInverseImageComparison.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HTorsionInverseImageComparison.lean#L124). The attribute's comment: “(2)”.

> For a proper morphism `f : X ⟶ Y` of the big h site and an abelian torsion sheaf `F` on
> `X_étale`, the base change map `a_Y⁻¹(R^i f_{small,*}F) ⟶ R^i f_{big,h,*}(a_X⁻¹F)` is an
> isomorphism for every `i`. The map is `AlgebraicGeometry.higherSmallEtaleFineBaseChange`, the
> degree `i` cohomology of the derived base change map
> `AlgebraicGeometry.derivedSmallEtaleFineBaseChange` at `F` placed in degree zero.

```lean
public theorem isIso_hTorsionHigherSmallEtaleBaseChange
    {X Y : (hAssociatedBigEtaleSite B).Scheme} (f : X ⟶ Y)
    (hf : IsProper ((hAssociatedBigEtaleSite B).inclusion.map f))
    (F : Sheaf (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property) Ab.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property) F)
    (i : ℕ) :
    IsIso (higherSmallEtaleFineBaseChange (hAssociatedBigEtaleSite B) B.precoverage
      (BigHSite.etalePrecoverage_le_precoverage B)
      (fun X F => (smallEtaleInverseImage_isSheaf_h_and_isIso_unit B X.1 X.2 F).1)
      (BigHSite.properDirectImageComparison B)
      (BigHSite.exists_properRefinement B) f F i)
```

**`AlgebraicGeometry.isIso_hTorsionDerivedComparisonUnit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HTorsionInverseImageComparison.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HTorsionInverseImageComparison.lean#L143). The attribute's comment: “(3)”.

> For an object `X` of the big h site and `K` in `D⁺(X_étale)` with torsion cohomology sheaves,
> the map `π_X⁻¹K ⟶ Rε_{X,*}(a_X⁻¹K)`, the derived unit of the change of topology at `π_X⁻¹K`, is an
> isomorphism.

```lean
public theorem isIso_hTorsionDerivedComparisonUnit_app (X : (hAssociatedBigEtaleSite B).Scheme)
    (K : DerivedCategory.Plus
      (Sheaf (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property) Ab.{u + 1}))
    (hK : ∀ i : ℤ, Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property)
      ((DerivedCategory.Plus.homologyFunctor _ i).obj K)) :
    IsIso ((derivedComparisonUnit (hEtaleCohomologyComparison B) X).app
      (((SmallEtale.inclusion (hAssociatedBigEtaleSite B) X.obj X.property).sheafPullback
        Ab.{u + 1} (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property)
        ((hAssociatedBigEtaleSite B).topology.over X)).mapDerivedCategoryPlus.obj K))
```

**`AlgebraicGeometry.isIso_hTorsionDerivedSmallEtaleBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HTorsionInverseImageComparison.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HTorsionInverseImageComparison.lean#L165). The attribute's comment: “(4)”.

> For a proper morphism `f : X ⟶ Y` of the big h site and `K` in `D⁺(X_étale)` with torsion
> cohomology sheaves, the base change map `a_Y⁻¹(Rf_{small,*}K) ⟶ Rf_{big,h,*}(a_X⁻¹K)` of the
> square of topoi `a_Y ∘ f_h = f_small ∘ a_X`, `AlgebraicGeometry.derivedSmallEtaleFineBaseChange`,
> is an isomorphism.

```lean
public theorem isIso_hTorsionDerivedSmallEtaleBaseChange
    {X Y : (hAssociatedBigEtaleSite B).Scheme} (f : X ⟶ Y)
    (hf : IsProper ((hAssociatedBigEtaleSite B).inclusion.map f))
    (K : DerivedCategory.Plus
      (Sheaf (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property) Ab.{u + 1}))
    (hK : ∀ i : ℤ, Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property)
      ((DerivedCategory.Plus.homologyFunctor _ i).obj K)) :
    IsIso (derivedSmallEtaleFineBaseChange (hAssociatedBigEtaleSite B) B.precoverage
      (BigHSite.etalePrecoverage_le_precoverage B)
      (fun X F => (smallEtaleInverseImage_isSheaf_h_and_isIso_unit B X.1 X.2 F).1)
      (BigHSite.properDirectImageComparison B)
      (BigHSite.exists_properRefinement B) f K)
```

## Tag 0EWG, a lemma

[Tag 0EWG](https://stacks.math.columbia.edu/tag/0EWG) in the Stacks Project.

**`AlgebraicGeometry.isIso_hDerivedSmallEtaleUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HCohomologyComparison.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HCohomologyComparison.lean#L84).

> Let `X` be a scheme, an object of a big h site `B`. For `K` in `D⁺(X_étale)` with torsion
> cohomology sheaves, the map `K ⟶ Ra_{X,*}a_X⁻¹K` is an isomorphism, with
> `a_X : Sh((Sch/X)_h) ⟶ Sh(X_étale)` the composite of the change of topology
> `ε_X : Sh((Sch/X)_h) ⟶ Sh((Sch/X)_étale)` and the projection
> `π_X : Sh((Sch/X)_étale) ⟶ Sh(X_étale)`.

```lean
public theorem isIso_hDerivedSmallEtaleUnit (X : (hAssociatedBigEtaleSite B).Scheme)
    (K : DerivedCategory.Plus
      (Sheaf (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property) Ab.{u + 1}))
    (hK : ∀ i : ℤ, Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property)
      ((DerivedCategory.Plus.homologyFunctor _ i).obj K)) :
    IsIso (hDerivedSmallEtaleUnit B X K)
```

## Tag 0EWH, a lemma

[Tag 0EWH](https://stacks.math.columbia.edu/tag/0EWH) in the Stacks Project.

**`AlgebraicGeometry.hCohomologyComparisonIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HTorsionCohomologyComparison.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HTorsionCohomologyComparison.lean#L85). The attribute's comment: “(1)”.

> **Stacks 0EWH (1).** Let `X` be a scheme, an object of a big h site `B`, and let `F` be a
> torsion abelian sheaf on `X_étale`. For every `q`,
>
> `H^q(X_étale, F) = H^q_h(X, a_X⁻¹F)`,
>
> where `a_X⁻¹F = ε_X⁻¹π_X⁻¹F` is the h sheafification of the pullback of `F` to the big étale site
> over `X`. The isomorphism is the canonical one: the degree `q` cohomology, at `F` placed in degree
> zero, of `AlgebraicGeometry.derivedGlobalSectionsFineComparisonIso`, the pullback along `a_X` on
> derived global sections.

```lean
public def hCohomologyComparisonIso
    (F : Sheaf (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property)
      AddCommGrpCat.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property) F)
    (q : ℕ) :
    (((sheafSections (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property)
        AddCommGrpCat.{u + 1}).obj
        (op (SmallEtale.final (hAssociatedBigEtaleSite B) X.obj X.property))).rightDerived q).obj
        F ≅
      ((Stacks.globalSectionsOver B.precoverage.toGrothendieck X).rightDerived q).obj
        ((abelianComparisonPullback B.precoverage (hAssociatedBigEtaleSite B).precoverage X).obj
          (((SmallEtale.inclusion (hAssociatedBigEtaleSite B) X.obj X.property).sheafPullback
            AddCommGrpCat.{u + 1} (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property)
            ((hAssociatedBigEtaleSite B).topology.over X)).obj F))
```

**`AlgebraicGeometry.hCohomologyComparisonPlusIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HTorsionCohomologyComparison.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HTorsionCohomologyComparison.lean#L115). The attribute's comment: “(2)”.

> **Stacks 0EWH (2).** Let `X` be a scheme, an object of a big h site `B`, and let `K` be an
> object of `D⁺(X_étale)` whose cohomology sheaves are torsion. For every `q`,
>
> `H^q(X_étale, K) = H^q_h(X, a_X⁻¹K)`,
>
> the cohomology of the derived global sections `RΓ(X_étale, K)` and `RΓ_h(X, a_X⁻¹K)`, where
> `a_X⁻¹ = ε_X⁻¹ ∘ π_X⁻¹` on `D⁺`. The isomorphism is the canonical one: the degree `q` cohomology of
> `AlgebraicGeometry.derivedGlobalSectionsFineComparisonIso`, the pullback along `a_X` on derived
> global sections.

```lean
public def hCohomologyComparisonPlusIso
    (K : DerivedCategory.Plus (Sheaf (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj
      X.property) AddCommGrpCat.{u + 1}))
    (hK : ∀ i : ℤ, Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property)
      ((DerivedCategory.Plus.homologyFunctor _ i).obj K))
    (q : ℤ) :
    (DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{u + 1} q).obj
        (((sheafSections (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property)
          AddCommGrpCat.{u + 1}).obj
          (op (SmallEtale.final (hAssociatedBigEtaleSite B) X.obj
            X.property))).rightDerivedFunctorPlus.obj K) ≅
      (DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{u + 1} q).obj
        ((Stacks.globalSectionsOver B.precoverage.toGrothendieck X).rightDerivedFunctorPlus.obj
          ((abelianComparisonPullback B.precoverage (hAssociatedBigEtaleSite B).precoverage
              X).mapDerivedCategoryPlus.obj
            (((SmallEtale.inclusion (hAssociatedBigEtaleSite B) X.obj X.property).sheafPullback
              AddCommGrpCat.{u + 1}
              (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property)
              ((hAssociatedBigEtaleSite B).topology.over X)).mapDerivedCategoryPlus.obj K)))
```

**`AlgebraicGeometry.hCohomologyConstantComparisonIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HTorsionCohomologyComparison.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/HTorsionCohomologyComparison.lean#L150). The attribute's comment: “example”.

> **Stacks 0EWH, the example.** Let `X` be a scheme, an object of a big h site `B`, and let `A`
> be a torsion abelian group. For every `q`,
>
> `H^q_étale(X, A) = H^q_h(X, A)`,
>
> the cohomology of the constant sheaves with value `A` on the small étale site of `X` and on the
> h site over `X`. The isomorphism is the canonical one: part (1) at the constant sheaf, followed by
> the identification `a_X⁻¹A = A` of constant sheaves (both are left adjoint to global sections).

```lean
public def hCohomologyConstantComparisonIso (A : AddCommGrpCat.{u + 1}) (hA : IsAddTorsion A)
    (q : ℕ) :
    (((sheafSections (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property)
        AddCommGrpCat.{u + 1}).obj
        (op (SmallEtale.final (hAssociatedBigEtaleSite B) X.obj X.property))).rightDerived q).obj
        ((constantSheaf (SmallEtale.topology (hAssociatedBigEtaleSite B) X.obj X.property)
          AddCommGrpCat.{u + 1}).obj A) ≅
      ((Stacks.globalSectionsOver B.precoverage.toGrothendieck X).rightDerived q).obj
        ((constantSheaf (B.precoverage.toGrothendieck.over X) AddCommGrpCat.{u + 1}).obj A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.103, Tag 0EW7](https://stacks.math.columbia.edu/tag/0EW7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

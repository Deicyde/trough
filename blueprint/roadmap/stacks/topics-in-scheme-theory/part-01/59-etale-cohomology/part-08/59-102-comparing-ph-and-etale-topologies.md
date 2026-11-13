---
declaration: section
origin: cited
lean: AlgebraicGeometry.smallEtaleInverseImage_isZariskiSheaf_ph, AlgebraicGeometry.smallEtaleInverseImage_isSheaf_ph_and_isIso_unit, AlgebraicGeometry.etaleInverseImageSectionsIso, AlgebraicGeometry.phToBigEtaleMorphism, AlgebraicGeometry.phToSmallEtaleMorphism, AlgebraicGeometry.bigPHBigEtale_pushforwardCommIso, AlgebraicGeometry.bigPHSmallEtale_pushforwardCommIso, AlgebraicGeometry.isIso_bigPHSmallEtaleDirectImageBaseChange
statement: formalized
proof: formalized
---

# 59.102 Comparing ph and étale topologies

Section 59.102 of the Stacks Project, [Tag 0DDV](https://stacks.math.columbia.edu/tag/0DDV). 7 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DDW, a lemma

[Tag 0DDW](https://stacks.math.columbia.edu/tag/0DDW) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleInverseImage_isZariskiSheaf_ph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/SmallEtalePullbackSheaf.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Ph/SmallEtalePullbackSheaf.lean#L103). The attribute's comment: “the Zariski half of the ph sheaf condition, Stacks 0DBQ; descent along a proper surjective morphism is not proved”.

> **Stacks 0DDW, the Zariski half of the ph sheaf condition.** For a sheaf of sets `F` on the
> small étale site of `S`, the presheaf underlying `π_S⁻¹F` — by the sections formula the rule
> `X ↦ Γ(X_ét, f_X⁻¹F)` of the source — satisfies descent for every family of the big ph category
> over `S` whose underlying family of schemes is a Zariski covering.
>
> A Zariski covering family is an fpqc covering family, and `π_S⁻¹F` is a sheaf for the fpqc
> topology of the slice by Stacks 09XN,
> `AlgebraicGeometry.bigEtaleToSmallEtale_inverseImage_isSheaf_fpqc`.

```lean
public theorem smallEtaleInverseImage_isZariskiSheaf_ph :
    IsZariskiSheaf B S hS
      ((bigEtaleToSmallEtaleMorphism (phAssociatedBigEtaleSite B) S hS).inverseImage.obj
        F).obj
```

**`AlgebraicGeometry.smallEtaleInverseImage_isSheaf_ph_and_isIso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/SmallEtalePullbackSheafUnconditional.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Ph/SmallEtalePullbackSheafUnconditional.lean#L60).

> **Stacks 0DDW.** For a sheaf of sets `F` on the small étale site of `S`, the rule
> `(f : X ⟶ S) ↦ Γ(X_ét, f⁻¹F)` — the presheaf underlying `π_S⁻¹F` on the big étale category over
> `S`, by the sections formula `AlgebraicGeometry.etaleInverseImageSectionsIso` and Stacks 09XN —
> is a sheaf for the ph topology of the big ph category over `S`, and the unit of
> `ε_S⁻¹ ⊣ ε_{S,*}` at `π_S⁻¹F` is an isomorphism, so that this ph sheaf is `ε_S⁻¹π_S⁻¹F`.
>
> By Stacks 0DBQ the ph sheaf condition splits into its Zariski half and descent along proper
> surjections; the latter follows from the proper base change theorem in degree zero, Stacks 0A3U,
> `Stacks.EtaleCohomology.isIso_smallEtaleSetBaseChange_of_isProper`.

```lean
public theorem smallEtaleInverseImage_isSheaf_ph_and_isIso_unit :
    Presieve.IsSheaf (BigPHOver.topology B S hS)
        ((bigEtaleToSmallEtaleMorphism (phAssociatedBigEtaleSite B) S hS).inverseImage.obj
          F).obj ∧
      IsIso ((phToBigEtaleMorphism B (B.obj S hS)).adj.unit.app
        ((bigEtaleToSmallEtaleMorphism (phAssociatedBigEtaleSite B) S hS).inverseImage.obj F))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.etaleInverseImageSectionsIso`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmallEtalePullbackSections.lean#L327), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/SmallEtalePullbackSheaf.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Ph/SmallEtalePullbackSheaf.lean#L75) (StacksFrontier): “the rule is the inverse image π\_S⁻¹F on the big étale site”.

## Tag 0DDX, a lemma

[Tag 0DDX](https://stacks.math.columbia.edu/tag/0DDX) in the Stacks Project.

**`AlgebraicGeometry.phToBigEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToEtaleSquares.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToEtaleSquares.lean#L208). The attribute's comment: “change-of-topology morphism”.

> The comparison `ε_X` from the big ph topos to the big étale topos, induced by the identity
> functor on the common slice category.

```lean
public def phToBigEtaleMorphism (B : BigPHSite.{u}) (X : B.Schemes) :
    MorphismOfTopoi
      (Sheaf (B.topology.over X) (Type (u + 1)))
      (Sheaf (BigEtaleOver.topology (phAssociatedBigEtaleSite B) X.1 X.2)
        (Type (u + 1)))
```

**`AlgebraicGeometry.phToSmallEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToEtaleSquares.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToEtaleSquares.lean#L244). The attribute's comment: “factorization through the big étale topos”.

> The comparison `a_X = π_X ∘ ε_X` from the big ph topos to the small étale topos.

```lean
public def phToSmallEtaleMorphism (B : BigPHSite.{u}) (X : B.Schemes) :
    MorphismOfTopoi
      (Sheaf (B.topology.over X) (Type (u + 1)))
      (Sheaf (SmallEtale.topology (phAssociatedBigEtaleSite B) X.1 X.2) (Type (u + 1)))
```

**`AlgebraicGeometry.bigPHBigEtale_pushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToEtaleSquares.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToEtaleSquares.lean#L273). The attribute's comment: “the big ph–big étale square”.

> **Stacks 0DDX, first diagram.** The square formed by the big ph and big étale base-change
> morphisms over the change-of-topology comparisons `ε_X` and `ε_Y` commutes on direct
> images.

```lean
public def bigPHBigEtale_pushforwardCommIso (B : BigPHSite.{u}) {X Y : B.Schemes} (f : X ⟶ Y) :
    ((bigEtaleMorphism (phAssociatedBigEtaleSite B) X Y f).comp
      (phToBigEtaleMorphism B X)).pushforward ≅
      ((phToBigEtaleMorphism B Y).comp (bigPHMorphism B X Y f)).pushforward
```

**`AlgebraicGeometry.bigPHSmallEtale_pushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToEtaleSquares.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChangeOfSites/PhToEtaleSquares.lean#L320). The attribute's comment: “the big ph–small étale square”.

> **Stacks 0DDX, second diagram.** The square formed by the big ph and small étale
> base-change morphisms over the comparisons `a_X = π_X ∘ ε_X` and `a_Y = π_Y ∘ ε_Y` commutes on
> direct images.

```lean
public def bigPHSmallEtale_pushforwardCommIso
    (B : BigPHSite.{u}) {X Y : B.Schemes} (f : X ⟶ Y) :
    ((phSmallEtaleMorphism B f).comp (phToSmallEtaleMorphism B X)).pushforward ≅
      ((phToSmallEtaleMorphism B Y).comp (bigPHMorphism B X Y f)).pushforward
```

## Tag 0DDY, a lemma

[Tag 0DDY](https://stacks.math.columbia.edu/tag/0DDY) in the Stacks Project.

**`AlgebraicGeometry.isIso_bigPHSmallEtaleDirectImageBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhProperDirectImage.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhProperDirectImage.lean#L93).

> **Stacks 0DDY.** Let `B` be a big ph site and `f : X ⟶ Y` a proper morphism of it. Then
> `a_Y⁻¹ ∘ f_{small,*} = f_{big,ph,*} ∘ a_X⁻¹` as functors from sheaves of sets on `X_étale` to
> sheaves of sets on `(Sch/Y)_ph`: the base change map
> `AlgebraicGeometry.bigPHSmallEtaleDirectImageBaseChange` of the square of topoi of Stacks 0DDX
> is an isomorphism.

```lean
public theorem isIso_bigPHSmallEtaleDirectImageBaseChange [IsProper (B.inclusion.map f)] :
    IsIso (bigPHSmallEtaleDirectImageBaseChange B f)
```

## Tag 0F0I, a lemma

[Tag 0F0I](https://stacks.math.columbia.edu/tag/0F0I) in the Stacks Project.

**`AlgebraicGeometry.BigPHSite.exists_phEtaleCohomologyComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhComparisonSituationProperties.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhComparisonSituationProperties.lean#L74).

> Consider the comparison of the ph topology of a big ph site `B` with the étale topology on
> the same category of schemes. Let `𝒫` be the class of proper morphisms, and for `X` in the site
> let `𝒜'_X ⊂ Ab((Sch/X)_étale)` be the full subcategory of sheaves of the form `π_X⁻¹F` with `F` a
> torsion abelian sheaf on `X_étale`. Then `𝒜'_X` is a weak Serre subcategory and properties
> (0EZ4)–(0EZ8) of the comparison situation of Stacks 0EZ3 hold: there is a comparison situation
> with the ph topology as finer topology, the étale topology as coarser topology, `𝒫` as
> distinguished class and the `𝒜'_X` as weak Serre classes.

```lean
public theorem exists_phEtaleCohomologyComparison (B : BigPHSite.{u}) :
    ∃ S : Stacks.ComparingTopologies.CohomologyComparison (phAssociatedBigEtaleSite B).Scheme,
      S.fineCoverage = B.precoverage ∧
      S.coarseCoverage = (phAssociatedBigEtaleSite B).precoverage ∧
      S.morphismProperty = (fun _ _ f => IsProper ((phAssociatedBigEtaleSite B).inclusion.map f)) ∧
      ∀ X : (phAssociatedBigEtaleSite B).Scheme,
        HEq (S.weakSerre X)
          (smallEtaleTorsionPullbackClass (phAssociatedBigEtaleSite B) X
            ((phAssociatedBigEtaleSite B).topology.over X))
```

## Tag 0DE4, a lemma

[Tag 0DE4](https://stacks.math.columbia.edu/tag/0DE4) in the Stacks Project.

**`AlgebraicGeometry.phEtaleTorsionComparison_smallEtaleInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionComparison.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionComparison.lean#L123). The attribute's comment: “(1)”.

> **Stacks 0DE4 (1).** For an object `X` of the big ph site and an abelian torsion sheaf `F` on
> `X_étale`, `ε_{X,*}a_X⁻¹F = π_X⁻¹F` — the unit `π_X⁻¹F ⟶ ε_{X,*}ε_X⁻¹π_X⁻¹F` of
> `ε_X⁻¹ ⊣ ε_{X,*}` is an isomorphism, `a_X⁻¹ = ε_X⁻¹ ∘ π_X⁻¹` — and
> `R^i ε_{X,*}(a_X⁻¹F) = 0` for `i > 0`.

```lean
public theorem phEtaleTorsionComparison_smallEtaleInclusion
    (X : (phAssociatedBigEtaleSite B).Scheme)
    (F : Sheaf (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property) Ab.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property) F) :
    IsIso ((abelianComparisonAdjunction B.precoverage
        (phAssociatedBigEtaleSite B).precoverage
        (BigPHSite.etalePrecoverage_le_precoverage B) X).unit.app
        (((SmallEtale.inclusion (phAssociatedBigEtaleSite B) X.obj X.property).sheafPullback
          Ab.{u + 1} (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property)
          ((phAssociatedBigEtaleSite B).topology.over X)).obj F)) ∧
      ∀ i : ℕ, 0 < i → IsZero (((abelianComparisonPushforward B.precoverage
          (phAssociatedBigEtaleSite B).precoverage
          (BigPHSite.etalePrecoverage_le_precoverage B) X).rightDerived i).obj
        ((abelianComparisonPullback B.precoverage
          (phAssociatedBigEtaleSite B).precoverage X).obj
          (((SmallEtale.inclusion (phAssociatedBigEtaleSite B) X.obj X.property).sheafPullback
            Ab.{u + 1} (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property)
            ((phAssociatedBigEtaleSite B).topology.over X)).obj F)))
```

**`AlgebraicGeometry.isIso_phEtaleTorsionHigherBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionComparison.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionComparison.lean#L154). The attribute's comment: “(2)”.

> **Stacks 0DE4 (2).** For a proper morphism `f : X ⟶ Y` of the big ph site and an abelian
> torsion sheaf `F` on `X_étale`, the base change map
> `a_Y⁻¹(R^i f_{small,*}F) ⟶ R^i f_{big,ph,*}(a_X⁻¹F)` is an isomorphism for every `i`. The map is
> `AlgebraicGeometry.higherSmallEtaleFineBaseChange`, the degree `i` cohomology of the derived base
> change map of part (4) at `F` placed in degree zero; `f_{big,ph,*}` is the direct image
> `overPushforward` of the ph topology along `f`.

```lean
public theorem isIso_phEtaleTorsionHigherBaseChange
    {X Y : (phAssociatedBigEtaleSite B).Scheme} (f : X ⟶ Y)
    (hf : IsProper ((phAssociatedBigEtaleSite B).inclusion.map f))
    (F : Sheaf (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property) Ab.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property) F)
    (i : ℕ) :
    IsIso (higherSmallEtaleFineBaseChange (phAssociatedBigEtaleSite B) B.precoverage
      (BigPHSite.etalePrecoverage_le_precoverage B)
      (fun X F => (smallEtaleInverseImage_isSheaf_ph B X.1 X.2 F).1)
      (properDirectImageComparison _) (BigPHSite.exists_properRefinement B) f F i)
```

**`AlgebraicGeometry.isIso_phEtaleTorsionDerivedComparisonUnit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionComparison.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionComparison.lean#L173). The attribute's comment: “(3)”.

> **Stacks 0DE4 (3).** For an object `X` of the big ph site and `K` in `D⁺(X_étale)` with torsion
> cohomology sheaves, the map `π_X⁻¹K ⟶ Rε_{X,*}(a_X⁻¹K)` is an isomorphism: it is the derived unit
> of `ε_X⁻¹ ⊣ ε_{X,*}` at `π_X⁻¹K`, and `a_X⁻¹K = ε_X⁻¹π_X⁻¹K`.

```lean
public theorem isIso_phEtaleTorsionDerivedComparisonUnit_app
    (X : (phAssociatedBigEtaleSite B).Scheme)
    (K : DerivedCategory.Plus
      (Sheaf (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property) Ab.{u + 1}))
    (hK : ∀ i : ℤ, Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property)
      ((DerivedCategory.Plus.homologyFunctor _ i).obj K)) :
    IsIso ((derivedComparisonUnit (phEtaleTorsionComparison B) X).app
      (((SmallEtale.inclusion (phAssociatedBigEtaleSite B) X.obj X.property).sheafPullback
        Ab.{u + 1} (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property)
        ((phAssociatedBigEtaleSite B).topology.over X)).mapDerivedCategoryPlus.obj K))
```

**`AlgebraicGeometry.isIso_phEtaleTorsionDerivedBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionComparison.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionComparison.lean#L194). The attribute's comment: “(4)”.

> **Stacks 0DE4 (4).** For a proper morphism `f : X ⟶ Y` of the big ph site and `K` in
> `D⁺(X_étale)` with torsion cohomology sheaves, the base change map
> `a_Y⁻¹(Rf_{small,*}K) ⟶ Rf_{big,ph,*}(a_X⁻¹K)` is an isomorphism. The map is
> `AlgebraicGeometry.derivedSmallEtaleFineBaseChange`, the base change map of the square of topoi
> `a_Y ∘ f_{big,ph} = f_{small} ∘ a_X`.

```lean
public theorem isIso_phEtaleTorsionDerivedBaseChange
    {X Y : (phAssociatedBigEtaleSite B).Scheme} (f : X ⟶ Y)
    (hf : IsProper ((phAssociatedBigEtaleSite B).inclusion.map f))
    (K : DerivedCategory.Plus
      (Sheaf (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property) Ab.{u + 1}))
    (hK : ∀ i : ℤ, Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property)
      ((DerivedCategory.Plus.homologyFunctor _ i).obj K)) :
    IsIso (derivedSmallEtaleFineBaseChange (phAssociatedBigEtaleSite B) B.precoverage
      (BigPHSite.etalePrecoverage_le_precoverage B)
      (fun X F => (smallEtaleInverseImage_isSheaf_ph B X.1 X.2 F).1)
      (properDirectImageComparison _) (BigPHSite.exists_properRefinement B) f K)
```

## Tag 0DE5, a lemma

[Tag 0DE5](https://stacks.math.columbia.edu/tag/0DE5) in the Stacks Project.

**`AlgebraicGeometry.isIso_phEtaleTorsionDerivedSmallEtaleUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionDerivedUnit.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionDerivedUnit.lean#L62).

> For an object `X` of the big ph site and `K` in `D⁺(X_étale)` with torsion cohomology
> sheaves, the map `K ⟶ Ra_{X,*}a_X⁻¹K` is an isomorphism, where
> `a_X = π_X ∘ ε_X : Sh((Sch/X)_ph) ⟶ Sh(X_étale)`; the map is
> `AlgebraicGeometry.derivedSmallEtaleFineUnit`, the unit of `a_X⁻¹ ⊣ a_{X,*}` on `D⁺`.

```lean
public theorem isIso_phEtaleTorsionDerivedSmallEtaleUnit (X : (phAssociatedBigEtaleSite B).Scheme)
    (K : DerivedCategory.Plus
      (Sheaf (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property) Ab.{u + 1}))
    (hK : ∀ i : ℤ, Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property)
      ((DerivedCategory.Plus.homologyFunctor _ i).obj K)) :
    IsIso (derivedSmallEtaleFineUnit (phAssociatedBigEtaleSite B) B.precoverage
      (BigPHSite.etalePrecoverage_le_precoverage B)
      (fun X F => (smallEtaleInverseImage_isSheaf_ph B X.1 X.2 F).1)
      (properDirectImageComparison _) (BigPHSite.exists_properRefinement B) X K)
```

## Tag 0DE6, a lemma

[Tag 0DE6](https://stacks.math.columbia.edu/tag/0DE6) in the Stacks Project.

**`AlgebraicGeometry.phEtaleTorsionCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionCohomology.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionCohomology.lean#L78). The attribute's comment: “(1)”.

> **Stacks 0DE6 (1).** For an object `X` of the big ph site, a torsion abelian sheaf `F` on
> `X_étale` and every `q`, `H^q(X_étale, F) = H^q_ph(X, a_X⁻¹F)`, where
> `a_X⁻¹F = ε_X⁻¹π_X⁻¹F` is the pullback to the ph site over `X`. The isomorphism is the canonical
> one, the pullback along `a_X` on cohomology (`AlgebraicGeometry.cohomologyFineComparisonIso`).

```lean
public def phEtaleTorsionCohomologyIso
    (F : Sheaf (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property)
      AddCommGrpCat.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property) F)
    (q : ℕ) :
    (((sheafSections (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property)
        AddCommGrpCat.{u + 1}).obj
        (op (SmallEtale.final (phAssociatedBigEtaleSite B) X.obj X.property))).rightDerived q).obj
        F ≅
      ((Stacks.globalSectionsOver (phEtaleTorsionComparison B).fineCoverage.toGrothendieck
          X).rightDerived q).obj
        ((abelianComparisonPullback (phEtaleTorsionComparison B).fineCoverage
            (phEtaleTorsionComparison B).coarseCoverage X).obj
          (((SmallEtale.inclusion (phAssociatedBigEtaleSite B) X.obj X.property).sheafPullback
            AddCommGrpCat.{u + 1}
            (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property)
            ((phAssociatedBigEtaleSite B).topology.over X)).obj F))
```

**`AlgebraicGeometry.phEtaleTorsionDerivedCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionCohomology.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionCohomology.lean#L107). The attribute's comment: “(2)”.

> **Stacks 0DE6 (2).** For an object `X` of the big ph site, `K` in `D⁺(X_étale)` with torsion
> cohomology sheaves and every `q`, `H^q(X_étale, K) = H^q_ph(X, a_X⁻¹K)`: the degree `q`
> cohomology of the derived global sections `RΓ(X_étale, K)` and `RΓ_ph(X, a_X⁻¹K)`, with
> `a_X⁻¹ = ε_X⁻¹ ∘ π_X⁻¹` on `D⁺`. The isomorphism is the canonical one, the degree `q` cohomology of
> the pullback along `a_X`, `AlgebraicGeometry.derivedGlobalSectionsFineComparisonIso`.

```lean
public def phEtaleTorsionDerivedCohomologyIso
    (K : DerivedCategory.Plus (Sheaf (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj
      X.property) AddCommGrpCat.{u + 1}))
    (hK : ∀ i : ℤ, Stacks.Torsion.torsionSheafProperty.{u + 1}
      (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property)
      ((DerivedCategory.Plus.homologyFunctor _ i).obj K))
    (q : ℤ) :
    (DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{u + 1} q).obj
        (((sheafSections (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property)
          AddCommGrpCat.{u + 1}).obj
          (op (SmallEtale.final (phAssociatedBigEtaleSite B) X.obj
            X.property))).rightDerivedFunctorPlus.obj K) ≅
      (DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{u + 1} q).obj
        ((Stacks.globalSectionsOver (phEtaleTorsionComparison B).fineCoverage.toGrothendieck
            X).rightDerivedFunctorPlus.obj
          ((abelianComparisonPullback (phEtaleTorsionComparison B).fineCoverage
              (phEtaleTorsionComparison B).coarseCoverage X).mapDerivedCategoryPlus.obj
            (((SmallEtale.inclusion (phAssociatedBigEtaleSite B) X.obj X.property).sheafPullback
              AddCommGrpCat.{u + 1}
              (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property)
              ((phAssociatedBigEtaleSite B).topology.over X)).mapDerivedCategoryPlus.obj K)))
```

**`AlgebraicGeometry.phEtaleTorsionConstantCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionCohomology.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ComparingBigSmall/PhTorsionCohomology.lean#L139). The attribute's comment: “the example: H^q\_et(X, A) = H^q\_ph(X, A) for a torsion abelian group A”.

> **Stacks 0DE6, the example.** For an object `X` of the big ph site, a torsion abelian group `A`
> and every `q`, `H^q_étale(X, A) = H^q_ph(X, A)`, the cohomology of the constant sheaves with value
> `A` on `X_étale` and on the ph site over `X`. The isomorphism is part (1) at the constant sheaf,
> which is torsion, followed by the identification `a_X⁻¹A = A` of constant sheaves (both are left
> adjoint to global sections); see `AlgebraicGeometry.cohomologyConstantFineComparisonIso`.

```lean
public def phEtaleTorsionConstantCohomologyIso (A : AddCommGrpCat.{u + 1}) (hA : IsAddTorsion A)
    (q : ℕ) :
    (((sheafSections (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property)
        AddCommGrpCat.{u + 1}).obj
        (op (SmallEtale.final (phAssociatedBigEtaleSite B) X.obj X.property))).rightDerived q).obj
        ((constantSheaf (SmallEtale.topology (phAssociatedBigEtaleSite B) X.obj X.property)
          AddCommGrpCat.{u + 1}).obj A) ≅
      ((Stacks.globalSectionsOver (phEtaleTorsionComparison B).fineCoverage.toGrothendieck
          X).rightDerived q).obj
        ((constantSheaf ((phEtaleTorsionComparison B).fineCoverage.toGrothendieck.over X)
          AddCommGrpCat.{u + 1}).obj A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.102, Tag 0DDV](https://stacks.math.columbia.edu/tag/0DDV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

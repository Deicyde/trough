---
declaration: section
origin: cited
lean: AlgebraicGeometry.BigPHSpaceSite.isIso_phToBigEtale_unit_app_inverseImage, AlgebraicGeometry.BigPHSpaceSite.isIso_phToSmallEtale_unit_app, AlgebraicGeometry.BigPHSpaceSite.isZero_rightDerived_phToBigEtale_abelianInverseImage, AlgebraicGeometry.BigPHSpaceSite.isIso_phToSmallEtale_derivedUnits, AlgebraicGeometry.BigPHSpaceSite.etaleCohomologyDerivedIsoOfTorsion, AlgebraicGeometry.BigPHSpaceSite.etaleCohomologyIsoOfTorsion, AlgebraicGeometry.BigPHSpaceSite.etaleCohomologyConstantIsoOfTorsion, AlgebraicGeometry.BigPHSpaceSite.phToBigEtaleMorphism
statement: formalized
proof: formalized
---

# 84.8 Comparing ph and étale topologies

Section 84.8 of the Stacks Project, [Tag 0DGS](https://stacks.math.columbia.edu/tag/0DGS). 5 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DGT, a lemma

[Tag 0DGT](https://stacks.math.columbia.edu/tag/0DGT) in the Stacks Project.

**`AlgebraicGeometry.BigPHSpaceSite.isIso_phToBigEtale_unit_app_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSmallEtalePullbackSheaf.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSmallEtalePullbackSheaf.lean#L134). The attribute's comment: “part (1), the equality ε\_\{X,*}a\_X⁻¹ℱ = π\_X⁻¹ℱ”.

> **Stacks 0DGT, part (1), `ε_{X,*}a_X⁻¹ℱ = π_X⁻¹ℱ`.** For a sheaf of sets `ℱ` on `X_étale` the
> unit `π_X⁻¹ℱ ⟶ ε_{X,*}ε_X⁻¹π_X⁻¹ℱ = ε_{X,*}a_X⁻¹ℱ` is an isomorphism.

```lean
theorem isIso_phToBigEtale_unit_app_inverseImage
    (X : P.Spaces)
    (ℱ : Sheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem (etaleSpace P E h X))
      (Type (u + 1))) :
    IsIso ((phToBigEtaleMorphism P E h X).adj.unit.app
      ((E.bigToSmallEtaleMorphism (etaleSpace P E h X)).inverseImage.obj ℱ))
```

**`AlgebraicGeometry.BigPHSpaceSite.isIso_phToSmallEtale_unit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSmallEtalePullbackSheaf.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSmallEtalePullbackSheaf.lean#L147). The attribute's comment: “part (1), the equality a\_\{X,*}a\_X⁻¹ℱ = ℱ”.

> **Stacks 0DGT, part (1), `a_{X,*}a_X⁻¹ℱ = ℱ`.** For a sheaf of sets `ℱ` on `X_étale` the unit
> `ℱ ⟶ a_{X,*}a_X⁻¹ℱ` is an isomorphism. It is the unit of `π_X⁻¹ ⊣ π_{X,*}`, an isomorphism by
> Stacks 0DF3, followed by `π_{X,*}` of the unit of `ε_X⁻¹ ⊣ ε_{X,*}` at `π_X⁻¹ℱ`.

```lean
theorem isIso_phToSmallEtale_unit_app
    (X : P.Spaces)
    (ℱ : Sheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem (etaleSpace P E h X))
      (Type (u + 1))) :
    IsIso ((phToSmallEtaleMorphism P E h X).adj.unit.app ℱ)
```

**`AlgebraicGeometry.BigPHSpaceSite.isZero_rightDerived_phToBigEtale_abelianInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSmallEtaleTorsionVanishing.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSmallEtaleTorsionVanishing.lean#L75). The attribute's comment: “part (2)”.

> **Stacks 0DGT, part (2).** Let `X` be an algebraic space and `ℱ` a torsion abelian sheaf on
> `X_étale`. Then `R^i ε_{X,*}(a_X⁻¹ℱ) = 0` for `i > 0`. Here
> `ε_X : (Spaces/X)_ph ⟶ (Spaces/X)_étale` is the comparison of Stacks 0DGW, `ε_{X,*}` is
> restriction of abelian sheaves along the identity-on-spaces functor of slices, `a_X⁻¹` is the
> abelian inverse image (Stacks 04JC) of `a_X = π_X ∘ ε_X`, and `R^i` is the right derived
> functor.

```lean
public theorem isZero_rightDerived_phToBigEtale_abelianInverseImage (X : P.Spaces)
    (ℱ : Sheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem (etaleSpace P E h X))
      AddCommGrpCat.{u + 1})
    (hℱ : Stacks.Torsion.torsionSheafProperty
      (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem (etaleSpace P E h X)) ℱ)
    (i : ℕ) (hi : 0 < i) :
    IsZero (((phToBigEtaleAbelianPushforward P E h X).rightDerived i).obj
      ((phToSmallEtaleAbelianInverseImage P E h X).obj ℱ))
```

## Tag 0DGU, a lemma

[Tag 0DGU](https://stacks.math.columbia.edu/tag/0DGU) in the Stacks Project.

**`AlgebraicGeometry.BigPHSpaceSite.isIso_phToSmallEtale_derivedUnits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtaleDerivedTorsion.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtaleDerivedTorsion.lean#L147).

> Let `X` be an algebraic space over `S` and `K` an object of `D⁺(X_étale)` whose cohomology
> sheaves are torsion. Then the maps `π_X⁻¹K ⟶ Rε_{X,*}a_X⁻¹K` and `K ⟶ Ra_{X,*}a_X⁻¹K` are
> isomorphisms, for the comparison morphisms `ε_X` and `a_X = π_X ∘ ε_X` from the big ph topos of `X`
> (Stacks 0DGW). The two maps are the units of the derived adjunctions `ε_X⁻¹ ⊣ Rε_{X,*}` at `π_X⁻¹K`
> and `a_X⁻¹ ⊣ Ra_{X,*}` at `K` on bounded below derived categories.

```lean
theorem isIso_phToSmallEtale_derivedUnits
    (K : DerivedCategory.Plus (Sheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem
      (etaleSpace P E h X)) AddCommGrpCat.{u + 1}))
    (hK : ∀ i : ℤ, Stacks.Torsion.torsionSheafProperty _
      ((DerivedCategory.homologyFunctor _ i).obj (DerivedCategory.Plus.ι.obj K))) :
    IsIso ((Stacks.ComparingTopologies.derivedPlusAdjunction
        (phToBigEtaleAbelianAdjunction P E h X)).unit.app
          ((CategoryTheory.Sites.abelianInverseImage
            (E.bigToSmallEtaleMorphism (etaleSpace P E h X))).mapDerivedCategoryPlus.obj K)) ∧
      IsIso ((Stacks.ComparingTopologies.derivedPlusAdjunction
        (phToSmallEtaleAbelianAdjunction P E h X)).unit.app K)
```

## Tag 0DGV, a lemma

[Tag 0DGV](https://stacks.math.columbia.edu/tag/0DGV) in the Stacks Project.

**`AlgebraicGeometry.BigPHSpaceSite.etaleCohomologyDerivedIsoOfTorsion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtaleCohomology.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtaleCohomology.lean#L146). The attribute's comment: “(2)”.

> **Stacks 0DGV, part (2).** For `K` in `D⁺(X_étale)` whose cohomology sheaves are torsion,
> `H^q(X_étale, K) = H^q_ph(X, a_X⁻¹K)` for every `q`, by the canonical map
> `AlgebraicGeometry.BigPHSpaceSite.etaleToPhDerivedGlobalSections`.

```lean
def etaleCohomologyDerivedIsoOfTorsion
    (K : DerivedCategory.Plus (Sheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem
      (etaleSpace P E h X)) AddCommGrpCat.{u + 1}))
    (hK : ∀ i : ℤ, Stacks.Torsion.torsionSheafProperty _
      ((DerivedCategory.homologyFunctor _ i).obj (DerivedCategory.Plus.ι.obj K))) (q : ℤ) :
    (DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{u + 1} q).obj
        ((etaleGlobalSections P E h X).rightDerivedFunctorPlus.obj K) ≅
      (DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{u + 1} q).obj
        ((phGlobalSections P X).rightDerivedFunctorPlus.obj
          ((CategoryTheory.Sites.abelianInverseImage
            (phToSmallEtaleMorphism P E h X)).mapDerivedCategoryPlus.obj K))
```

**`AlgebraicGeometry.BigPHSpaceSite.etaleCohomologyIsoOfTorsion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtaleCohomology.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtaleCohomology.lean#L164). The attribute's comment: “(1)”.

> **Stacks 0DGV, part (1).** For a torsion abelian sheaf `F` on `X_étale`,
> `H^q(X_étale, F) = H^q_ph(X, a_X⁻¹F)` for every `q`.

```lean
def etaleCohomologyIsoOfTorsion
    (F : Sheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem (etaleSpace P E h X))
      AddCommGrpCat.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty _ F) (q : ℕ) :
    ((etaleGlobalSections P E h X).rightDerived q).obj F ≅
      ((phGlobalSections P X).rightDerived q).obj
        ((CategoryTheory.Sites.abelianInverseImage (phToSmallEtaleMorphism P E h X)).obj F)
```

**`AlgebraicGeometry.BigPHSpaceSite.etaleCohomologyConstantIsoOfTorsion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtaleCohomology.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtaleCohomology.lean#L182). The attribute's comment: “the example of a torsion abelian group”.

> **The example of Stacks 0DGV.** For a torsion abelian group `A`,
> `H^q_étale(X, A) = H^q_ph(X, A)` for the constant sheaves.

```lean
def etaleCohomologyConstantIsoOfTorsion (A : AddCommGrpCat.{u + 1}) (hA : IsAddTorsion A)
    (q : ℕ) :
    ((etaleGlobalSections P E h X).rightDerived q).obj
        ((constantSheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem (etaleSpace P E h X))
          AddCommGrpCat.{u + 1}).obj A) ≅
      ((phGlobalSections P X).rightDerived q).obj
        ((constantSheaf (BigPHSpaceOver.topology P X) AddCommGrpCat.{u + 1}).obj A)
```

## Tag 0DGW, a lemma

[Tag 0DGW](https://stacks.math.columbia.edu/tag/0DGW) in the Stacks Project.

**`AlgebraicGeometry.BigPHSpaceSite.phToBigEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtale.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtale.lean#L192). The attribute's comment: “the comparison morphism ε from the big ph to the big étale topos”.

> **Stacks 0DGW.** The change-of-topology morphism `ε_X` from the big ph topos of `X` to its
> big étale topos: the identity-on-spaces functor of slice categories is a morphism of sites,
> because it is continuous and representably flat.

```lean
def phToBigEtaleMorphism (X : P.Spaces) :
    MorphismOfTopoi (Sheaf (BigPHSpaceOver.topology P X) (Type (u + 1)))
      (Sheaf (E.bigEtaleTopology (etaleSpace P E h X)) (Type (u + 1)))
```

**`AlgebraicGeometry.BigPHSpaceSite.phToSmallEtaleMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtale.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtale.lean#L230). The attribute's comment: “the comparison morphism a to the small étale topos, as the composite π ∘ ε”.

> **Stacks 0DGW.** The morphism `a_X` from the big ph topos of `X` to its small étale topos,
> defined as the composite of `ε_X` with the big-to-small étale morphism `π_X` of **Stacks 0DF3**.
> The factorization `a_X = π_X ∘ ε_X` asserted by Stacks 0DGW is therefore definitional.

```lean
def phToSmallEtaleMorphism (X : P.Spaces) :
    MorphismOfTopoi (Sheaf (BigPHSpaceOver.topology P X) (Type (u + 1)))
      (Sheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem (etaleSpace P E h X))
        (Type (u + 1)))
```

**`AlgebraicGeometry.BigPHSpaceSite.bigPHBigEtale_pushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtale.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtale.lean#L239). The attribute's comment: “the big ph–big étale square”.

> **Stacks 0DGW**, the first diagram. For a morphism `f : Y ⟶ X` of algebraic spaces the direct
> images of `ε_X ∘ f_{big, ph}` and of `f_{big, étale} ∘ ε_Y` are canonically isomorphic.

```lean
def bigPHBigEtale_pushforwardCommIso {X Y : P.Spaces} (f : Y ⟶ X) :
    ((E.bigEtaleMorphism (etaleMap P E h f)).comp (phToBigEtaleMorphism P E h Y)).pushforward ≅
      ((phToBigEtaleMorphism P E h X).comp (bigPHMorphism P f)).pushforward
```

**`AlgebraicGeometry.BigPHSpaceSite.bigPHSmallEtale_pushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtale.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtale.lean#L298). The attribute's comment: “the big ph–small étale square”.

> **Stacks 0DGW**, the second diagram. For a morphism `f : Y ⟶ X` of algebraic spaces the
> direct images of `a_X ∘ f_{big, ph}` and of `f_{small} ∘ a_Y` are canonically isomorphic.
>
> Since `a` is the composite of `ε` with `π`, this is the big square above pasted with the
> big–small étale square of **Stacks 0DF6**.

```lean
def bigPHSmallEtale_pushforwardCommIso {X Y : P.Spaces} (f : Y ⟶ X) :
    ((E.smallEtaleMorphism (etaleMap P E h f)).comp
        (phToSmallEtaleMorphism P E h Y)).pushforward ≅
      ((phToSmallEtaleMorphism P E h X).comp (bigPHMorphism P f)).pushforward
```

**`AlgebraicGeometry.BigPHSpaceSite.bigPHSmallEtaleCharts_pushforwardCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtale.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtale.lean#L435). The attribute's comment: “the big ph–small étale square, for the small étale site of scheme charts”.

> **Stacks 0DGW**, the second diagram, for the presentation of the small étale topos by the
> site of scheme charts. For a morphism `f : X ⟶ Y` of algebraic spaces of the ph site the direct
> images of `f_{small} ∘ a_X` and of `a_Y ∘ f_{big, ph}` are canonically isomorphic, where `a` is
> restriction along the chart functor `smallEtaleToPH`. No big étale site intervenes.

```lean
def bigPHSmallEtaleCharts_pushforwardCommIso {X Y : P.Spaces} (f : X ⟶ Y) :
    ((smallEtaleToPH P X).sheafPushforwardContinuous (Type (u + 1))
        (Space.SmallEtale.topology P.fppfSite S P.fppf_mem X.1)
        (BigPHSpaceOver.topology P X)) ⋙
      (Space.smallToposMorphism P.fppfSite S P.fppf_mem f).pushforward ≅
    (bigPHMorphism P f).pushforward ⋙
      (smallEtaleToPH P Y).sheafPushforwardContinuous (Type (u + 1))
        (Space.SmallEtale.topology P.fppfSite S P.fppf_mem Y.1)
        (BigPHSpaceOver.topology P Y)
```

**`AlgebraicGeometry.BigPHSpaceSite.bigPHBigEtale_inverseImageCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtaleInverseImage.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtaleInverseImage.lean#L69). The attribute's comment: “the big ph–big étale square, on inverse images”.

> The first diagram, on inverse images. For a morphism `f : Y ⟶ X` of algebraic spaces the
> inverse images of `ε_X ∘ f_{big, ph}` and of `f_{big, étale} ∘ ε_Y` are canonically isomorphic:
> `f_{big, ph}⁻¹ ∘ ε_X⁻¹ ≅ ε_Y⁻¹ ∘ f_{big, étale}⁻¹`. It is the conjugate of the direct-image
> isomorphism `bigPHBigEtale_pushforwardCommIso`.

```lean
def bigPHBigEtale_inverseImageCommIso {X Y : P.Spaces} (f : Y ⟶ X) :
    ((phToBigEtaleMorphism P E h X).comp (bigPHMorphism P f)).inverseImage ≅
      ((E.bigEtaleMorphism (etaleMap P E h f)).comp (phToBigEtaleMorphism P E h Y)).inverseImage
```

**`AlgebraicGeometry.BigPHSpaceSite.bigPHSmallEtale_inverseImageCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtaleInverseImage.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtaleInverseImage.lean#L92). The attribute's comment: “the big ph–small étale square, on inverse images”.

> The second diagram, on inverse images. For a morphism `f : Y ⟶ X` of algebraic spaces the
> inverse images of `a_X ∘ f_{big, ph}` and of `f_{small} ∘ a_Y` are canonically isomorphic:
> `f_{big, ph}⁻¹ ∘ a_X⁻¹ ≅ a_Y⁻¹ ∘ f_{small}⁻¹`, where `a = π ∘ ε`. It is the conjugate of the
> direct-image isomorphism `bigPHSmallEtale_pushforwardCommIso`.

```lean
def bigPHSmallEtale_inverseImageCommIso {X Y : P.Spaces} (f : Y ⟶ X) :
    ((phToSmallEtaleMorphism P E h X).comp (bigPHMorphism P f)).inverseImage ≅
      ((E.smallEtaleMorphism (etaleMap P E h f)).comp
        (phToSmallEtaleMorphism P E h Y)).inverseImage
```

**`AlgebraicGeometry.BigPHSpaceSite.bigPHSmallEtaleCharts_inverseImageCommIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtaleInverseImage.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhToSmallEtaleInverseImage.lean#L134). The attribute's comment: “the big ph–small étale square, for the small étale site of scheme charts, on inverse images”.

> The second diagram on inverse images, for the presentation of the small étale topos by the
> site of scheme charts. For a morphism `f : X ⟶ Y` of algebraic spaces of the ph site, with `a` the
> restriction along the chart functor `smallEtaleToPH` and `a⁻¹` its left adjoint,
> `f_{big, ph}⁻¹ ∘ a_Y⁻¹ ≅ a_X⁻¹ ∘ f_{small}⁻¹`. It is the conjugate of the direct-image isomorphism
> `bigPHSmallEtaleCharts_pushforwardCommIso`.

```lean
def bigPHSmallEtaleCharts_inverseImageCommIso {X Y : P.Spaces} (f : X ⟶ Y) :
    (smallEtaleToPH P Y).sheafPullback (Type (u + 1))
        (Space.SmallEtale.topology P.fppfSite S P.fppf_mem Y.1)
        (BigPHSpaceOver.topology P Y) ⋙ (bigPHMorphism P f).inverseImage ≅
      (Space.smallToposMorphism P.fppfSite S P.fppf_mem f).inverseImage ⋙
        (smallEtaleToPH P X).sheafPullback (Type (u + 1))
          (Space.SmallEtale.topology P.fppfSite S P.fppf_mem X.1)
          (BigPHSpaceOver.topology P X)
```

## Tag 0DGX, a lemma

[Tag 0DGX](https://stacks.math.columbia.edu/tag/0DGX) in the Stacks Project.

**`AlgebraicGeometry.BigPHSpaceSite.phToSmallEtaleDerivedPushforwardIsoOfIsProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSmallEtaleProperDerivedPushforward.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSmallEtaleProperDerivedPushforward.lean#L249). The attribute's comment: “(2)”.

> **Stacks 0DGX, part (2).** Let `f : Y ⟶ X` be a proper morphism of algebraic spaces over `S`
> and `K` an object of `D⁺(Y_étale)` whose cohomology sheaves are torsion. Then
> `a_X⁻¹(Rf_{small,*}K) = Rf_{big,ph,*}(a_Y⁻¹K)`, by the canonical comparison
> `AlgebraicGeometry.BigPHSpaceSite.phToSmallEtaleDerivedBaseChange`.

```lean
def phToSmallEtaleDerivedPushforwardIsoOfIsProper
    (hf : Space.IsProper P.fppfSite S P.fppf_mem f.hom)
    (K : DerivedCategory.Plus (Sheaf (Space.SpacesEtale.topology E.fppfSite S E.fppf_mem
      (etaleSpace P E h Y)) AddCommGrpCat.{u + 1}))
    (hK : ∀ i : ℤ, Stacks.Torsion.torsionSheafProperty _
      ((DerivedCategory.homologyFunctor _ i).obj (DerivedCategory.Plus.ι.obj K))) :
    (CategoryTheory.Sites.abelianInverseImage
        (phToSmallEtaleMorphism P E h X)).mapDerivedCategoryPlus.obj
        ((E.smallEtalePushforward (etaleMap P E h f)).rightDerivedFunctorPlus.obj K) ≅
      (phAbelianPushforward P f).rightDerivedFunctorPlus.obj
        ((CategoryTheory.Sites.abelianInverseImage
          (phToSmallEtaleMorphism P E h Y)).mapDerivedCategoryPlus.obj K)
```

**`AlgebraicGeometry.BigPHSpaceSite.phToSmallEtalePushforwardIsoOfIsProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSmallEtaleProperPushforward.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Topologies/BigPhSmallEtaleProperPushforward.lean#L224). The attribute's comment: “(1)”.

> **Stacks 0DGX, part (1).** Let `f : Y ⟶ X` be a proper morphism of algebraic spaces over `S`,
> and let `a = π ∘ ε` be the comparison morphisms from the big ph topoi to the small étale topoi of
> Stacks 0DGW. Then `a_X⁻¹ ∘ f_{small,*} = f_{big,ph,*} ∘ a_Y⁻¹` as functors from sheaves on the
> small étale site of `Y` to sheaves on the big ph site of `X`: the canonical base change map
> `AlgebraicGeometry.BigPHSpaceSite.phToSmallEtaleBaseChange`, the mate of the commutative square of
> Stacks 0DGW, is an isomorphism.

```lean
def phToSmallEtalePushforwardIsoOfIsProper
    (hf : Space.IsProper P.fppfSite S P.fppf_mem f.hom) :
    (E.smallEtaleMorphism (etaleMap P E h f)).pushforward ⋙
        (phToSmallEtaleMorphism P E h X).inverseImage ≅
      (phToSmallEtaleMorphism P E h Y).inverseImage ⋙ (bigPHMorphism P f).pushforward
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 84.8, Tag 0DGS](https://stacks.math.columbia.edu/tag/0DGS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

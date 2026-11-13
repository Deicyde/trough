---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.phComparisonMorphism, AlgebraicGeometry.Space.spacesEtaleComparisonMorphism, AlgebraicGeometry.BigPHSpaceSite.phEtaleComparisonSquarePushforwardIso, AlgebraicGeometry.BigPHSpaceSite.phEtaleComparisonSquareInverseImageIso, AlgebraicGeometry.BigPHSpaceSite.etaleAugmentation_inverseImage_fullyFaithful_of_isProperHypercovering, AlgebraicGeometry.BigPHSpaceSite.etaleAugmentation_abelianInverseImage_fullyFaithful_of_isProperHypercovering, AlgebraicGeometry.Space.isIso_etaleAugmentation_derivedPlusUnit_of_isProperHypercovering, AlgebraicGeometry.Space.derivedGlobalSectionsIsoOfIsProperHypercovering
statement: formalized
proof: formalized
---

# 85.36 Proper hypercoverings of algebraic spaces

Section 85.36 of the Stacks Project, [Tag 0DHI](https://stacks.math.columbia.edu/tag/0DHI). 6 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DHJ, a lemma

[Tag 0DHJ](https://stacks.math.columbia.edu/tag/0DHJ) in the Stacks Project.

**`AlgebraicGeometry.Space.phComparisonMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/PhComparisonFunctor.lean, line 604](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/PhComparisonFunctor.lean#L604). The attribute's comment: “the upper horizontal arrow h : Sh((Spaces/U)\_\{ph, total}) → Sh(U\_étale)”.

> **The upper horizontal arrow of Tag 0DHJ**, `h : Sh((Spaces/U)_total) → Sh(U_étale)`, the
> morphism of topoi of the morphism of sites given by `V/U_n ↦ V/U_n`.

```lean
def phComparisonMorphism :
    MorphismOfTopoi (Sheaf (SimplicialOver.totalTopology J A.left) (Type (u + 1)))
      (Sheaf (etaleSimplicialSite A).totalTopology (Type (u + 1)))
```

**`AlgebraicGeometry.Space.spacesEtaleComparisonMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/PhComparisonFunctor.lean, line 627](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/PhComparisonFunctor.lean#L627). The attribute's comment: “the lower horizontal arrow h\_\{-1} : Sh((Spaces/X)\_ph) → Sh(X\_étale)”.

> **The lower horizontal arrow of Tag 0DHJ**, `h_{-1} : Sh(Spaces/X) → Sh(X_étale)`, the
> morphism of topoi of the inclusion `X_{spaces, étale} → Spaces/X`, `W ↦ W/X`.

```lean
def spacesEtaleComparisonMorphism (X : AlgebraicSpaces B S hS) :
    MorphismOfTopoi (Sheaf (J.over X) (Type (u + 1)))
      (Sheaf (SpacesEtale.topology B S hS X) (Type (u + 1)))
```

**`AlgebraicGeometry.BigPHSpaceSite.phEtaleComparisonSquarePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/PhComparisonSquare.lean, line 623](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/PhComparisonSquare.lean#L623). The attribute's comment: “the commutative diagram of topoi, on direct images”.

> **Tag 0DHJ, on direct images.** Let `a : U → X` be an augmented simplicial algebraic space
> over `S`. The diagram of topoi
> ```
> Sh((Spaces/U)_{ph, total}) --h--> Sh(U_étale)
>         | a_ph                       | a
> Sh((Spaces/X)_ph)        --h₋₁--> Sh(X_étale)
> ```
> commutes: the direct image of `h₋₁ ∘ a_ph` is that of `a ∘ h`.

```lean
def phEtaleComparisonSquarePushforwardIso :
    (SimplicialOver.augmentationMorphismOfTopoi P.topology A.left A.hom).pushforward ⋙
        (spacesEtaleComparisonMorphism P.topology A.right).pushforward ≅
      (phComparisonMorphism A P.topology).pushforward ⋙ (etaleAugmentationMorphism A).pushforward
```

**`AlgebraicGeometry.BigPHSpaceSite.phEtaleComparisonSquareInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/PhComparisonSquare.lean, line 631](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/PhComparisonSquare.lean#L631). The attribute's comment: “the commutative diagram of topoi, on inverse images”.

> **Tag 0DHJ, on inverse images**: `h⁻¹ ∘ a⁻¹ ≅ a_ph⁻¹ ∘ h₋₁⁻¹`.

```lean
def phEtaleComparisonSquareInverseImageIso :
    (etaleAugmentationMorphism A).inverseImage ⋙ (phComparisonMorphism A P.topology).inverseImage ≅
      (spacesEtaleComparisonMorphism P.topology A.right).inverseImage ⋙
        (SimplicialOver.augmentationMorphismOfTopoi P.topology A.left A.hom).inverseImage
```

## Tag 0DHK, a lemma

[Tag 0DHK](https://stacks.math.columbia.edu/tag/0DHK) in the Stacks Project.

**`AlgebraicGeometry.BigPHSpaceSite.etaleAugmentation_inverseImage_fullyFaithful_of_isProperHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/ProperHypercoveringFullyFaithful.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/ProperHypercoveringFullyFaithful.lean#L235). The attribute's comment: “sheaves of sets”.

> **Stacks 0DHK, sheaves of sets.** Let `S` be a scheme, `X` an algebraic space over `S`, `U` a
> simplicial algebraic space over `S` and `a : U → X` an augmentation which is a proper hypercovering
> of `X`. Then `a⁻¹ : Sh(X_étale) ⥤ Sh(U_étale)` is fully faithful, its essential image consists
> exactly of the cartesian sheaves, and `a_*` is a quasi-inverse: the unit of `a⁻¹ ⊣ a_*` is
> invertible, and so is its counit at every cartesian sheaf. Here `a : Sh(U_étale) → Sh(X_étale)` is
> the morphism of topoi of Section 0DE7, and the category of algebraic spaces over `S` is the one of
> a big ph site `P`.

```lean
theorem etaleAugmentation_inverseImage_fullyFaithful_of_isProperHypercovering
    (hA : IsProperHypercovering P.fppfSite S P.fppf_mem A) :
    (etaleAugmentationMorphism A).inverseImage.Full ∧
      (etaleAugmentationMorphism A).inverseImage.Faithful ∧
      (∀ G, (etaleAugmentationMorphism A).inverseImage.essImage G ↔
        (etaleSituation A).IsCartesianSheaf G) ∧
      (∀ F, IsIso ((etaleAugmentationMorphism A).adj.unit.app F)) ∧
      (∀ G, (etaleSituation A).IsCartesianSheaf G →
        IsIso ((etaleAugmentationMorphism A).adj.counit.app G))
```

**`AlgebraicGeometry.BigPHSpaceSite.etaleAugmentation_abelianInverseImage_fullyFaithful_of_isProperHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/ProperHypercoveringFullyFaithful.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/ProperHypercoveringFullyFaithful.lean#L271). The attribute's comment: “sheaves of abelian groups”.

> **Stacks 0DHK, sheaves of abelian groups.** Let `a : U → X` be an augmented simplicial
> algebraic space which is a proper hypercovering of `X`. Then the inverse image
> `a⁻¹ : Ab(X_étale) ⥤ Ab(U_étale)` on abelian sheaves is fully faithful, its essential image
> consists exactly of the cartesian abelian sheaves, and the abelian direct image `a_*` is a
> quasi-inverse: the unit of `a⁻¹ ⊣ a_*` is invertible, and so is its counit at every cartesian
> abelian sheaf.

```lean
theorem etaleAugmentation_abelianInverseImage_fullyFaithful_of_isProperHypercovering
    (hA : IsProperHypercovering P.fppfSite S P.fppf_mem A) :
    (Sites.abelianInverseImage (etaleAugmentationMorphism A)).Full ∧
      (Sites.abelianInverseImage (etaleAugmentationMorphism A)).Faithful ∧
      (∀ G, (Sites.abelianInverseImage (etaleAugmentationMorphism A)).essImage G ↔
        (etaleSituation A).IsCartesianAbSheaf G) ∧
      (∀ F, IsIso ((Stacks.Topos.AbelianPushforward.abelianInverseImageAdjPushforward
        (etaleSimplicialSite A).totalTopology (etaleAugmentationMorphism A)).unit.app F)) ∧
      (∀ G, (etaleSituation A).IsCartesianAbSheaf G →
        IsIso ((Stacks.Topos.AbelianPushforward.abelianInverseImageAdjPushforward
          (etaleSimplicialSite A).totalTopology (etaleAugmentationMorphism A)).counit.app G))
```

## Tag 0DHL, a lemma

[Tag 0DHL](https://stacks.math.columbia.edu/tag/0DHL) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_etaleAugmentation_derivedPlusUnit_of_isProperHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/ProperHypercoveringDerivedDescent.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/ProperHypercoveringDerivedDescent.lean#L336). The attribute's comment: “for `K` with torsion cohomology sheaves; the torsion hypothesis is required: for `K = ℚ` the statement is false”.

> **Stacks Project, Tag 0DHL**, corrected statement. Let `S` be a scheme, `X` an algebraic
> space over `S`, `U` a simplicial algebraic space over `S` and `a : U → X` an augmentation. If
> `a : U → X` is a proper hypercovering of `X`, then for `K ∈ D⁺(X_étale)` with torsion cohomology
> sheaves the canonical map
>
> `K → Ra_*(a⁻¹K)`
>
> is an isomorphism, where `a : Sh(U_étale) → Sh(X_étale)` is the morphism of topoi of
> Section 0DE7.
>
> Here `X = A.right`, `U = A.left` and `a = A.hom`; `X_étale` is the spaces-étale site of `X`, the
> proper hypercovering condition is Section 0DHI (`AlgebraicGeometry.Space.IsProperHypercovering`),
> and `D⁺` is the bounded below derived category of abelian sheaves. The map is the unit at `K` of
> the adjunction `a⁻¹ ⊣ Ra_*` on `D⁺`, `a⁻¹` being exact and applied degreewise.
>
> The source states this for every `K ∈ D⁺(X_étale)`, and as printed it fails for `K = ℚ`; its proof
> cites Stacks 0DGU, a statement about complexes with torsion cohomology sheaves. Counterexample: let
> `k` be an algebraically closed field of characteristic `≠ 2`, let `f = y²z - x³ - x²z + z⁴`, and let
> `X` be the spectrum of the strict henselization of `k[x, y, z]/(f)` at the origin. The tangent cone
> of `X` is the nodal cubic `N = V(y²z - x³ - x²z) ⊂ ℙ²`, and the blow-up `π : Y → X` of the closed
> point is regular, with exceptional curve `E ≅ N` (in the chart `z = 1` its equation is
> `y² - x³ - x² + z = 0`). Let `U` be the Čech nerve of the proper surjective morphism `π`, a proper
> hypercovering of `X`. Since `Y ×_X ⋯ ×_X Y = Δ(Y) ∪ E × ⋯ × E`, closed Mayer-Vietoris gives
> `RΓ(U_étale, ℚ) = fib(RΓ(Y, ℚ) ⊕ ℚ → RΓ(E, ℚ))`. As `Y` is normal and connected, `H¹(Y, ℚ) = 0`,
> while `H¹(E, ℚ) = ℚ`; hence `H²(U_étale, ℚ) = ℚ`. But `X` is strictly henselian local, so
> `H²(X_étale, ℚ) = 0`, and `ℚ → Ra_*a⁻¹ℚ` is not an isomorphism. The torsion hypothesis on `K` is
> the correction.
>
> The proof is that of the source: a big ph site `(Spaces/S)_ph` on the algebraic spaces over `S`
> exists (`AlgebraicGeometry.BigFppfSite.bigPHSpaceSite`), and in it the square of Tag 0DHJ, the
> comparison of ph and étale cohomology of torsion sheaves (Stacks 0DGT, Stacks 0DGU), and descent
> along the ph hypercovering `U` of `X` (Stacks 0DA8, Stacks 0D8N) give
> `Ra_*a⁻¹K = Rh₋₁,* Ra_{ph,*} a_ph⁻¹ h₋₁⁻¹ K = K`; see
> `AlgebraicGeometry.BigPHSpaceSite.isIso_etaleAugmentation_derivedPlusUnit_of_torsion`.

```lean
theorem isIso_etaleAugmentation_derivedPlusUnit_of_isProperHypercovering
    (hA : IsProperHypercovering B S hS A)
    (K : DerivedCategory.Plus (Sheaf (SpacesEtale.topology B S hS A.right) AddCommGrpCat.{u + 1}))
    (hK : ∀ i : ℤ, Stacks.Torsion.torsionSheafProperty _
      ((DerivedCategory.homologyFunctor _ i).obj (DerivedCategory.Plus.ι.obj K))) :
    IsIso ((Stacks.ComparingTopologies.derivedPlusAdjunction
      (abelianInverseImageAdjPushforward (etaleSimplicialSite A).totalTopology
        (etaleAugmentationMorphism A))).unit.app K)
```

## Tag 0DHM, a lemma

[Tag 0DHM](https://stacks.math.columbia.edu/tag/0DHM) in the Stacks Project.

**`AlgebraicGeometry.Space.derivedGlobalSectionsIsoOfIsProperHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/ProperHypercoveringDerivedDescent.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/ProperHypercoveringDerivedDescent.lean#L367).

> **Stacks Project, Tag 0DHM**, corrected statement. Let `S` be a scheme, `X` an algebraic
> space over `S`, `U` a simplicial algebraic space over `S` and `a : U → X` an augmentation. If
> `a : U → X` is a proper hypercovering of `X`, then
>
> `RΓ(X_étale, K) = RΓ(U_étale, a⁻¹K)`
>
> for `K ∈ D⁺(X_étale)` with torsion cohomology sheaves, where `a : Sh(U_étale) → Sh(X_étale)` is the
> morphism of topoi of Section 0DE7.
>
> The isomorphism is the canonical one: `RΓ(X_étale, -)` of the unit `K → Ra_*a⁻¹K` followed by the
> factorisation `RΓ(U_étale, -) = RΓ(X_étale, -) ∘ Ra_*` of Cohomology on Sites, Remark 08J6
> (`Stacks.LerayPullbackComparison.lerayPullback`), invertible by
> `isIso_etaleAugmentation_derivedPlusUnit_of_isProperHypercovering` (Stacks 0DHL).
>
> As for Stacks 0DHL, the source states this for every `K ∈ D⁺(X_étale)`, and as printed it fails
> for `K = ℚ`: for the Čech nerve `U` of the blow-up `Y → X` of the strictly henselian surface
> singularity described at `isIso_etaleAugmentation_derivedPlusUnit_of_isProperHypercovering`,
> `H²(U_étale, ℚ) = ℚ` while `H²(X_étale, ℚ) = 0`. The torsion hypothesis on `K` is the
> correction.

```lean
def derivedGlobalSectionsIsoOfIsProperHypercovering (hA : IsProperHypercovering B S hS A)
    (K : DerivedCategory.Plus (Sheaf (SpacesEtale.topology B S hS A.right) AddCommGrpCat.{u + 1}))
    (hK : ∀ i : ℤ, Stacks.Torsion.torsionSheafProperty _
      ((DerivedCategory.homologyFunctor _ i).obj (DerivedCategory.Plus.ι.obj K))) :
    (Sheaf.Γ (SpacesEtale.topology B S hS A.right)
        AddCommGrpCat.{u + 1}).rightDerivedFunctorPlus.obj
        K ≅
      (Sheaf.Γ (etaleSimplicialSite A).totalTopology
        AddCommGrpCat.{u + 1}).rightDerivedFunctorPlus.obj
        ((CategoryTheory.Sites.abelianInverseImage
          (etaleAugmentationMorphism A)).mapDerivedCategoryPlus.obj
          K)
```

## Tag 0DHN, a lemma

[Tag 0DHN](https://stacks.math.columbia.edu/tag/0DHN) in the Stacks Project.

**`AlgebraicGeometry.Space.derivedPlusTorsionEquivalenceOfIsProperHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/ProperHypercoveringTorsionDerivedEquivalence.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/ProperHypercoveringTorsionDerivedEquivalence.lean#L164). The attribute's comment: “corrected form (errata.md, 2026-11-06): `a⁻¹ : D⁺_tors(X_étale) ≌ D⁺_{𝒜, tors}(U_étale)` with quasi-inverse `Ra_*`; as printed, for all of `D⁺(X_étale)`, the statement is false”.

> **Stacks Project, Tag 0DHN**, for torsion coefficients. Let `S` be a scheme, `X` an algebraic
> space over `S`, `U` a simplicial algebraic space over `S` and `a : U → X` an augmentation, and let
> `𝒜 ⊂ Ab(U_étale)` be the weak Serre subcategory of cartesian abelian sheaves. If `U` is a proper
> hypercovering of `X`, then `a⁻¹` defines an equivalence
>
> `D⁺_tors(X_étale) ⟶ D⁺_{𝒜, tors}(U_étale)`
>
> with quasi-inverse `Ra_*`, where `a : Sh(U_étale) → Sh(X_étale)` is the morphism of topoi of
> Section 0DE7, `D⁺_tors(X_étale)` consists of the bounded below complexes with torsion cohomology
> sheaves and `D⁺_{𝒜, tors}(U_étale)` of those whose cohomology sheaves are cartesian and torsion.
> The functors are identified by
> `AlgebraicGeometry.Space.derivedPlusTorsionEquivalenceOfIsProperHypercovering_functor` and
> `AlgebraicGeometry.Space.derivedPlusTorsionEquivalenceOfIsProperHypercovering_inverse`.
>
> The source states this for `D⁺(X_étale) ⟶ D⁺_𝒜(U_étale)`, and as written it is false: its proof
> uses Stacks 0DHL, whose proof cites Stacks 0DGU, which holds only for complexes with torsion
> cohomology sheaves. For a counterexample with rational coefficients let `X` be a normal surface
> over an algebraically closed field with a cusp singularity `x`, let `π : X̃ → X` be a resolution
> whose exceptional curve `E` over `x` is a cycle of rational curves, and let `U` be the Čech nerve
> of the proper surjective morphism `X̃ ⊔ {x} → X`, a proper hypercovering. If `a⁻¹` were fully
> faithful on `D⁺(X_étale)` with quasi-inverse `Ra_*`, then `ℚ = Ra_*a⁻¹ℚ`, and the spectral sequence
> of the hypercovering would give `H²(X_étale, ℚ) ≠ 0`, coming from `H¹(E, ℚ) = ℚ`; but
> `Hⁱ(X_étale, ℚ) = 0` for `i > 0` because `X` is normal. The torsion hypothesis is therefore part of
> the statement, and this is the corrected form. The erratum, with the counterexample checked in
> full, is recorded in `errata.md` (batch of 2026-11-06).
>
> The proof is the source's: Stacks 0DHK (`a⁻¹` on abelian sheaves is fully faithful with essential
> image the cartesian sheaves) and Stacks 0DHL (`K ≅ Ra_*a⁻¹K` on `D⁺_tors(X_étale)`) are the inputs
> of the formal equivalence of Stacks 0D7U,
> `CategoryTheory.SimplicialSiteSituation.Augmentation.derivedPlusTorsionEquivalence`.

```lean
def derivedPlusTorsionEquivalenceOfIsProperHypercovering (hA : IsProperHypercovering B S hS A) :
    ((DerivedCategoryB.derivedCategoryB
      (Stacks.Torsion.torsionSheafProperty.{u + 1, u + 1, u + 1}
        (SpacesEtale.topology B S hS A.right))).inverseImage
          DerivedCategory.Plus.ι).FullSubcategory ≌
      ((DerivedCategoryB.derivedCategoryB
        (cartesianTorsionAbSheaf (etaleSituation A))).inverseImage
          DerivedCategory.Plus.ι).FullSubcategory
```

**`AlgebraicGeometry.Space.derivedPlusTorsionEquivalenceOfIsProperHypercovering_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/ProperHypercoveringTorsionDerivedEquivalence.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/ProperHypercoveringTorsionDerivedEquivalence.lean#L181). The attribute's comment: “the equivalence is `a⁻¹`”.

> **The equivalence of Tag 0DHN is `a⁻¹`**: its forward functor, followed by the inclusion into
> `D⁺(U_étale)`, is the inclusion of `D⁺_tors(X_étale)` followed by
> `a⁻¹ : D⁺(X_étale) ⥤ D⁺(U_étale)`, the right derived functor of the exact functor `a⁻¹`.

```lean
theorem derivedPlusTorsionEquivalenceOfIsProperHypercovering_functor
    (hA : IsProperHypercovering B S hS A) :
    (derivedPlusTorsionEquivalenceOfIsProperHypercovering hA).functor ⋙
        ((DerivedCategoryB.derivedCategoryB
          (cartesianTorsionAbSheaf (etaleSituation A))).inverseImage DerivedCategory.Plus.ι).ι =
      ((DerivedCategoryB.derivedCategoryB
        (Stacks.Torsion.torsionSheafProperty.{u + 1, u + 1, u + 1}
          (SpacesEtale.topology B S hS A.right))).inverseImage DerivedCategory.Plus.ι).ι ⋙
        (totalInverseImageAb (etaleSituation A) _ _
          (etaleAugmentation A)).rightDerivedFunctorPlus
```

**`AlgebraicGeometry.Space.derivedPlusTorsionEquivalenceOfIsProperHypercovering_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/ProperHypercoveringTorsionDerivedEquivalence.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/ProperHypercoveringTorsionDerivedEquivalence.lean#L197). The attribute's comment: “the quasi-inverse is `Ra_*`”.

> **The quasi-inverse of the equivalence of Tag 0DHN is `Ra_*`**: its inverse functor, followed
> by the inclusion into `D⁺(X_étale)`, is the inclusion of `D⁺_{𝒜, tors}(U_étale)` followed by
> `Ra_* : D⁺(U_étale) ⥤ D⁺(X_étale)`.

```lean
theorem derivedPlusTorsionEquivalenceOfIsProperHypercovering_inverse
    (hA : IsProperHypercovering B S hS A) :
    (derivedPlusTorsionEquivalenceOfIsProperHypercovering hA).inverse ⋙
        ((DerivedCategoryB.derivedCategoryB
          (Stacks.Torsion.torsionSheafProperty.{u + 1, u + 1, u + 1}
            (SpacesEtale.topology B S hS A.right))).inverseImage DerivedCategory.Plus.ι).ι =
      ((DerivedCategoryB.derivedCategoryB
        (cartesianTorsionAbSheaf (etaleSituation A))).inverseImage DerivedCategory.Plus.ι).ι ⋙
        (abelianTotalPushforward (etaleSituation A) _ _
          (etaleAugmentation A)).rightDerivedFunctorPlus
```

## Tag 0DHP, a lemma

[Tag 0DHP](https://stacks.math.columbia.edu/tag/0DHP) in the Stacks Project.

**`AlgebraicGeometry.BigPHSpaceSite.phHypercoveringEtaleSpectralSequenceOfTorsion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/PhHypercoveringEtaleSpectralSequence.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/PhHypercoveringEtaleSpectralSequence.lean#L298).

> Let `S` be a scheme, `X` an algebraic space over `S`, `U` a simplicial algebraic space over
> `S` and `a : U → X` an augmentation. Let `𝓕` be a torsion abelian sheaf on `X_étale` and let
> `𝓕_p` be its pullback to `U_{p, étale}`. If `U` is a ph hypercovering of `X`, there is a
> canonical spectral sequence
>
> `E₁^{p,q} = H^q_étale(U_p, 𝓕_p)`
>
> converging to `H^{p+q}_étale(X, 𝓕)`.
>
> The spectral sequence is `phHypercoveringEtaleSpectralSequence`, the ph cohomology spectral
> sequence of the hypercovering (Stacks 09WJ on the total ph site, with ph descent along the
> hypercovering) at the pullback of `𝓕` to the big ph site of `X`; its first page and abutment are
> identified with étale cohomology by Stacks 0DGV and Stacks 0DGW.
>
> The source states the lemma for an arbitrary abelian sheaf `𝓕` and deduces it from Stacks 0DHM,
> whose proof only covers torsion coefficients (it rests on Stacks 0DGU). As written, for all
> abelian sheaves, the statement is false, and this is the corrected form, for torsion sheaves,
> which is the form the proof gives. A counterexample with `𝓕 = ℚ`: let `X` be a normal surface
> over an algebraically closed field with a cusp singularity `x`, let `X̃ → X` be its resolution,
> with exceptional curve `E` a cycle of rational curves, so that `H¹_étale(E, ℚ) = ℚ`, and let `U`
> be the Čech nerve of the proper surjective morphism `X̃ ⊔ {x} → X`, a proper and hence ph
> hypercovering. Convergence of the canonical spectral sequence to `H^{p+q}_étale(X, ℚ)` is
> cohomological descent for `ℚ` along `U`, which yields the Mayer–Vietoris sequence
> `H¹(X̃, ℚ) ⊕ H¹(x, ℚ) → H¹(E, ℚ) → H²(X, ℚ)` of the abstract blow-up square; as `X̃` is normal,
> `H¹(X̃, ℚ) = 0`, so `H²_étale(X, ℚ) ≠ 0`. But `H^i_étale(X, ℚ) = 0` for `i > 0` on the normal
> scheme `X`.

```lean
def phHypercoveringEtaleSpectralSequenceOfTorsion
    (hA : MorphismProperty.IsHypercovering P.IsPHCoveringMorphism A)
    (F : Sheaf (etaleTopology P E h A.right) AddCommGrpCat.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty _ F) :
    PhHypercoveringEtaleSpectralSequence P E h A F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.36, Tag 0DHI](https://stacks.math.columbia.edu/tag/0DHI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

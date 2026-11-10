---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.bigFppfAugmentationSquareIso, AlgebraicGeometry.Space.EtaleComponent.smallEtale_inverseImage_fullyFaithful, AlgebraicGeometry.Space.EtaleComponent.smallEtale_abelianInverseImage_fullyFaithful, AlgebraicGeometry.Space.IsFppfHypercovering.isIso_smallEtaleDerivedUnit, AlgebraicGeometry.Space.IsFppfHypercovering.smallEtaleDerivedGlobalSectionsIso, AlgebraicGeometry.Space.derivedPlusEquivalenceOfIsFppfHypercovering, AlgebraicGeometry.Space.derivedPlusEquivalenceOfIsFppfHypercovering_functor, AlgebraicGeometry.Space.derivedPlusEquivalenceOfIsFppfHypercovering_inverse
statement: formalized
proof: formalized
---

# 85.33 Fppf hypercoverings of algebraic spaces

Section 85.33 of the Stacks Project, [Tag 0DH4](https://stacks.math.columbia.edu/tag/0DH4). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DH5, a lemma

[Tag 0DH5](https://stacks.math.columbia.edu/tag/0DH5) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.SimplicialSpacesEtaleSite.bigFppfAugmentationSquareIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSmallEtaleBigFppfSquare.lean#L289), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDescentTags.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialQuasicoherentDescentTags.lean#L42) (StacksFrontier).

## Tag 0DH6, a lemma

[Tag 0DH6](https://stacks.math.columbia.edu/tag/0DH6) in the Stacks Project.

**`AlgebraicGeometry.Space.EtaleComponent.smallEtale_inverseImage_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringInverseImage.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringInverseImage.lean#L420). The attribute's comment: “sheaves of sets”.

> **Stacks 0DH6, sheaves of sets.** Let `S` be a scheme, `X` an algebraic space over `S`, and
> `a : U → X` an augmentation of a simplicial algebraic space over `S` which is an fppf
> hypercovering of `X`. Let `a : Sh(U_étale) → Sh(X_étale)` be the morphism of topoi of
> Section 0DE7, where `X_étale` is the small étale site of `X` (Stacks 03ED), its topos identified
> with that of `X_spaces,étale` by restriction along `AlgebraicGeometry.Space.comparisonFunctor`
> (Stacks 03G1, `AlgebraicGeometry.Space.comparisonFunctor_sheafEquivalence`).
> Then `a⁻¹ : Sh(X_étale) ⥤ Sh(U_étale)` is fully faithful, its essential image consists exactly of
> the cartesian sheaves, and `a_*` is a quasi-inverse: the unit of `a⁻¹ ⊣ a_*` is invertible, and
> so is its counit at every cartesian sheaf.

```lean
theorem smallEtale_inverseImage_fullyFaithful (hyp : IsFppfHypercovering A) :
    ((((comparisonFunctor B S hS A.right).sheafPushforwardContinuous
          (Type (u + 1))
          (SmallEtale.topology B S hS A.right.1)
          (SpacesEtale.topology B S hS A.right)).asEquivalence).inverse ⋙
        (etaleAugmentationMorphism A).inverseImage).Full ∧
      ((((comparisonFunctor B S hS A.right).sheafPushforwardContinuous
          (Type (u + 1))
          (SmallEtale.topology B S hS A.right.1)
          (SpacesEtale.topology B S hS A.right)).asEquivalence).inverse ⋙
        (etaleAugmentationMorphism A).inverseImage).Faithful ∧
      (∀ G, ((((comparisonFunctor B S hS A.right).sheafPushforwardContinuous
          (Type (u + 1))
          (SmallEtale.topology B S hS A.right.1)
          (SpacesEtale.topology B S hS A.right)).asEquivalence).inverse ⋙
          (etaleAugmentationMorphism A).inverseImage).essImage G ↔
        SimplicialSiteSituation.IsCartesianSheaf (etaleSimplicialSite A).situation G) ∧
      (∀ F, IsIso (((((comparisonFunctor B S hS A.right).sheafPushforwardContinuous
          (Type (u + 1))
          (SmallEtale.topology B S hS A.right.1)
          (SpacesEtale.topology B S hS A.right)).asEquivalence).symm.toAdjunction.comp
        (etaleAugmentationMorphism A).adj).unit.app F)) ∧
      (∀ G, SimplicialSiteSituation.IsCartesianSheaf (etaleSimplicialSite A).situation G →
        IsIso (((((comparisonFunctor B S hS A.right).sheafPushforwardContinuous
          (Type (u + 1))
          (SmallEtale.topology B S hS A.right.1)
          (SpacesEtale.topology B S hS A.right)).asEquivalence).symm.toAdjunction.comp
          (etaleAugmentationMorphism A).adj).counit.app G))
```

**`AlgebraicGeometry.Space.EtaleComponent.smallEtale_abelianInverseImage_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringInverseImage.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringInverseImage.lean#L461). The attribute's comment: “sheaves of abelian groups”.

> **Stacks 0DH6, sheaves of abelian groups.** Let `S` be a scheme, `X` an algebraic space over
> `S`, and `a : U → X` an augmentation of a simplicial algebraic space over `S` which is an fppf
> hypercovering of `X`. Let `a : Sh(U_étale) → Sh(X_étale)` be the morphism of topoi of
> Section 0DE7, where `X_étale` is the small étale site of `X` (Stacks 03ED), its category of
> abelian sheaves identified with that of `X_spaces,étale` by restriction along
> `AlgebraicGeometry.Space.comparisonFunctor` (Stacks 03G1,
> `AlgebraicGeometry.Space.comparisonFunctor_sheafEquivalence`). Then
> `a⁻¹ : Ab(X_étale) ⥤ Ab(U_étale)` is fully faithful, its essential image consists exactly of the
> cartesian abelian sheaves, and `a_*` is a quasi-inverse: the unit of `a⁻¹ ⊣ a_*` is invertible,
> and so is its counit at every cartesian abelian sheaf.

```lean
theorem smallEtale_abelianInverseImage_fullyFaithful (hyp : IsFppfHypercovering A) :
    ((((comparisonFunctor B S hS A.right).sheafPushforwardContinuous
          AddCommGrpCat.{u + 1}
          (SmallEtale.topology B S hS A.right.1)
          (SpacesEtale.topology B S hS A.right)).asEquivalence).inverse ⋙
        Sites.abelianInverseImage (etaleAugmentationMorphism A)).Full ∧
      ((((comparisonFunctor B S hS A.right).sheafPushforwardContinuous
          AddCommGrpCat.{u + 1}
          (SmallEtale.topology B S hS A.right.1)
          (SpacesEtale.topology B S hS A.right)).asEquivalence).inverse ⋙
        Sites.abelianInverseImage (etaleAugmentationMorphism A)).Faithful ∧
      (∀ G, ((((comparisonFunctor B S hS A.right).sheafPushforwardContinuous
          AddCommGrpCat.{u + 1}
          (SmallEtale.topology B S hS A.right.1)
          (SpacesEtale.topology B S hS A.right)).asEquivalence).inverse ⋙
          Sites.abelianInverseImage (etaleAugmentationMorphism A)).essImage G ↔
        SimplicialSiteSituation.IsCartesianAbSheaf (etaleSimplicialSite A).situation G) ∧
      (∀ F, IsIso (((((comparisonFunctor B S hS A.right).sheafPushforwardContinuous
          AddCommGrpCat.{u + 1}
          (SmallEtale.topology B S hS A.right.1)
          (SpacesEtale.topology B S hS A.right)).asEquivalence).symm.toAdjunction.comp
        (Stacks.Topos.AbelianPushforward.abelianInverseImageAdjPushforward
          (etaleSimplicialSite A).totalTopology (etaleAugmentationMorphism A))).unit.app F)) ∧
      (∀ G, SimplicialSiteSituation.IsCartesianAbSheaf (etaleSimplicialSite A).situation G →
        IsIso (((((comparisonFunctor B S hS A.right).sheafPushforwardContinuous
          AddCommGrpCat.{u + 1}
          (SmallEtale.topology B S hS A.right.1)
          (SpacesEtale.topology B S hS A.right)).asEquivalence).symm.toAdjunction.comp
          (Stacks.Topos.AbelianPushforward.abelianInverseImageAdjPushforward
            (etaleSimplicialSite A).totalTopology (etaleAugmentationMorphism A))).counit.app G))
```

## Tag 0DH7, a lemma

[Tag 0DH7](https://stacks.math.columbia.edu/tag/0DH7) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFppfHypercovering.isIso_smallEtaleDerivedUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringSmallEtaleDerived.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringSmallEtaleDerived.lean#L124).

> **Stacks 0DH7.** Let `S` be a scheme, `X` an algebraic space over `S`, `U` a simplicial
> algebraic space over `S` and `a : U → X` an augmentation which is an fppf hypercovering of `X`.
> Then for every `K ∈ D⁺(X_étale)` the map `K ⟶ Ra_*(a⁻¹K)` is an isomorphism. Here
> `a : Sh(U_étale) → Sh(X_étale)` is the morphism of topoi of Section 0DE7, with `X_étale` the small
> étale site of `X` (Stacks 03ED) and its abelian sheaves identified with those of `X_spaces,étale`
> by the equivalence of Stacks 03G1, so that `a⁻¹ ⊣ a_*` is the composite of that equivalence with
> the adjunction of Section 0DE7; the map is the unit of the derived adjunction `a⁻¹ ⊣ Ra_*` on
> bounded below derived categories.

```lean
theorem IsFppfHypercovering.isIso_smallEtaleDerivedUnit (hA : IsFppfHypercovering A)
    (K : DerivedCategory.Plus
      (Sheaf (SmallEtale.topology B S hS A.right.1) AddCommGrpCat.{u + 1})) :
    IsIso ((Stacks.ComparingTopologies.derivedPlusAdjunction
      (((comparisonFunctor B S hS A.right).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
        (SmallEtale.topology B S hS A.right.1)
        (SpacesEtale.topology B S hS A.right)).asEquivalence.symm.toAdjunction.comp
          (etaleAugmentationAbelianAdjunction A))).unit.app K)
```

## Tag 0DH8, a lemma

[Tag 0DH8](https://stacks.math.columbia.edu/tag/0DH8) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFppfHypercovering.smallEtaleDerivedGlobalSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringSmallEtaleDerived.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringSmallEtaleDerived.lean#L193).

> **Stacks 0DH8.** Let `S` be a scheme, `X` an algebraic space over `S`, `U` a simplicial
> algebraic space over `S` and `a : U → X` an augmentation which is an fppf hypercovering of `X`.
> Then `RΓ(X_étale, K) = RΓ(U_étale, a⁻¹K)` for `K ∈ D⁺(X_étale)`, naturally in `K`. Here
> `a : Sh(U_étale) → Sh(X_étale)` is the morphism of topoi of Section 0DE7, with `X_étale` the small
> étale site of `X` (Stacks 03ED) and `a⁻¹` as in `IsFppfHypercovering.isIso_smallEtaleDerivedUnit`.
> The isomorphism is the pullback on derived global sections: `RΓ(X_étale, -)` of the map
> `K ⟶ Ra_*(a⁻¹K)` of Stacks 0DH7 followed by the factorization
> `RΓ(U_étale, -) = RΓ(X_étale, -) ∘ Ra_*` of Stacks 08J6.

```lean
def IsFppfHypercovering.smallEtaleDerivedGlobalSectionsIso (hA : IsFppfHypercovering A) :
    (Sheaf.Γ (SmallEtale.topology B S hS A.right.1) AddCommGrpCat.{u + 1}).rightDerivedFunctorPlus ≅
      (((comparisonFunctor B S hS A.right).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
        (SmallEtale.topology B S hS A.right.1)
        (SpacesEtale.topology B S hS A.right)).asEquivalence.symm.functor ⋙
          etaleAugmentationAbelianInverseImage A).mapDerivedCategoryPlus ⋙
        (Sheaf.Γ (etaleSimplicialSite A).totalTopology
          AddCommGrpCat.{u + 1}).rightDerivedFunctorPlus
```

## Tag 0DH9, a lemma

[Tag 0DH9](https://stacks.math.columbia.edu/tag/0DH9) in the Stacks Project.

**`AlgebraicGeometry.Space.derivedPlusEquivalenceOfIsFppfHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringDerivedEquivalence.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringDerivedEquivalence.lean#L93).

> **Stacks Project, Tag 0DH9.** Let `S` be a scheme, `X` an algebraic space over `S`, `U` a
> simplicial algebraic space over `S` and `a : U → X` an augmentation, and let
> `𝒜 ⊂ Ab(U_étale)` be the weak Serre subcategory of cartesian abelian sheaves. If `U` is an fppf
> hypercovering of `X`, then `a⁻¹` defines an equivalence
>
> `D⁺(X_étale) ⟶ D⁺_𝒜(U_étale)`
>
> with quasi-inverse `Ra_*`, where `a : Sh(U_étale) → Sh(X_étale)` is the morphism of topoi of
> Section 0DE7 and `D⁺_𝒜(U_étale)` consists of the bounded below complexes whose cohomology sheaves
> are cartesian. The functors are identified by
> `AlgebraicGeometry.Space.derivedPlusEquivalenceOfIsFppfHypercovering_functor` and
> `AlgebraicGeometry.Space.derivedPlusEquivalenceOfIsFppfHypercovering_inverse`.
>
> The proof is the source's: the content of Stacks 0DH6 (every cartesian abelian sheaf on
> `U_étale` is `a⁻¹` of an abelian sheaf on `X_étale`) and of Stacks 0DH7 (`K ≅ Ra_*a⁻¹K` on
> `D⁺(X_étale)`) are the inputs of the formal equivalence of Stacks 0D7U,
> `CategoryTheory.SimplicialSiteSituation.Augmentation.derivedPlusInverseImageEquivalence`.

```lean
def derivedPlusEquivalenceOfIsFppfHypercovering (hA : IsFppfHypercovering A) :
    DerivedCategory.Plus (Sheaf (SpacesEtale.topology B S hS A.right) AddCommGrpCat.{u + 1}) ≌
      (cartesianDerivedPlus (etaleSituation A)).FullSubcategory
```

**`AlgebraicGeometry.Space.derivedPlusEquivalenceOfIsFppfHypercovering_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringDerivedEquivalence.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringDerivedEquivalence.lean#L104). The attribute's comment: “the equivalence is `a⁻¹`”.

> **The equivalence of Tag 0DH9 is `a⁻¹`**: its forward functor, followed by the inclusion of
> `D⁺_𝒜(U_étale)` into `D⁺(U_étale)`, is `a⁻¹ : D⁺(X_étale) ⥤ D⁺(U_étale)`, the right derived
> functor of the exact functor `a⁻¹`.

```lean
theorem derivedPlusEquivalenceOfIsFppfHypercovering_functor (hA : IsFppfHypercovering A) :
    (derivedPlusEquivalenceOfIsFppfHypercovering hA).functor ⋙
        (cartesianDerivedPlus (etaleSituation A)).ι =
      (totalInverseImageAb (etaleSituation A) _ _ (etaleAugmentation A)).rightDerivedFunctorPlus
```

**`AlgebraicGeometry.Space.derivedPlusEquivalenceOfIsFppfHypercovering_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringDerivedEquivalence.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringDerivedEquivalence.lean#L113). The attribute's comment: “the quasi-inverse is `Ra_*`”.

> **The quasi-inverse of the equivalence of Tag 0DH9 is `Ra_*`**: its inverse functor is the
> inclusion of `D⁺_𝒜(U_étale)` into `D⁺(U_étale)` followed by `Ra_* : D⁺(U_étale) ⥤ D⁺(X_étale)`.

```lean
theorem derivedPlusEquivalenceOfIsFppfHypercovering_inverse (hA : IsFppfHypercovering A) :
    (derivedPlusEquivalenceOfIsFppfHypercovering hA).inverse =
      (cartesianDerivedPlus (etaleSituation A)).ι ⋙
        (abelianTotalPushforward (etaleSituation A) _ _
          (etaleAugmentation A)).rightDerivedFunctorPlus
```

## Tag 0DHA, a lemma

[Tag 0DHA](https://stacks.math.columbia.edu/tag/0DHA) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFppfHypercovering.etaleSpectralSequence_pageOne_abutsTo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringEtaleSpectralSequence.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SimplicialSpaces/FppfHypercoveringEtaleSpectralSequence.lean#L123).

> **Stacks Project, Tag 0DHA.** Let `S` be a scheme, `X` an algebraic space over `S`, `U` a
> simplicial algebraic space over `S` and `a : U → X` an augmentation. Let `𝓕` be an abelian sheaf
> on `X_étale` and `𝓕_p` its pullback to `U_{p, étale}`. If `U` is an fppf hypercovering of `X`,
> then the canonical spectral sequence `etaleSpectralSequence A` at `𝓕` has
>
> `E_1^{p,q} = H^q_ét(U_p, 𝓕_p)`
>
> (vanishing outside the first quadrant) and converges to `H^{p+q}_ét(X, 𝓕)`.
>
> Here `X = A.right`, `U = A.left` and `a = A.hom`, the étale sites are the spaces-étale sites of
> Section 0DE7, `𝓕_p` is the abelian inverse image along the morphism of topoi of Stacks 03G2 induced
> by `a_p : U_p → X`, and `H^n_ét` is `CategoryTheory.Sheaf.functorH`; the first page is identified
> naturally in `𝓕` by `AlgebraicGeometry.Space.etaleSpectralSequence_pageOneIso`, and the abutment is
> zero in negative degrees.

```lean
theorem IsFppfHypercovering.etaleSpectralSequence_pageOne_abutsTo (hA : IsFppfHypercovering A)
    (F : Sheaf (SpacesEtale.topology B S hS A.right) AddCommGrpCat.{u + 1}) :
    (∀ p q : ℕ, Nonempty ((((etaleSpectralSequence A).obj F).page 1 le_rfl).X ((p : ℤ), (q : ℤ)) ≅
      (Sheaf.functorH.{u + 1, u + 1} (SpacesEtale.topology B S hS (A.left.obj (op ⦋p⦌))) q).obj
        ((Sites.abelianInverseImage (EtaleComponent.baseChangeMorphism (A := A) ⦋p⦌)).obj F))) ∧
    (∀ p q : ℤ, p < 0 ∨ q < 0 → IsZero ((((etaleSpectralSequence A).obj F).page 1 le_rfl).X
      (p, q))) ∧
    SpectralSequence.AbutsTo ((etaleSpectralSequence A).obj F)
      (fun n => if 0 ≤ n then Sheaf.functorH.{u + 1, u + 1}
          (SpacesEtale.topology B S hS A.right) n.toNat |>.obj F
        else AddCommGrpCat.of PUnit)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.33, Tag 0DH4](https://stacks.math.columbia.edu/tag/0DH4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

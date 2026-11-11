---
declaration: section
origin: cited
lean: Stacks.Topology.LocallyQuasiCompactZariskiSituation.comparisonSquarePushforwardIso, Stacks.Topology.Simplicial.qcSmallBottomMorphism, Stacks.Topology.Simplicial.qcComparisonSquarePushforwardIso, Stacks.Topology.Simplicial.qcComparisonSquareInverseImageIso, Stacks.Topology.Simplicial.exists_qcComparisonSquare, Stacks.Topology.Simplicial.qcSmallComparisonMorphism, Stacks.Topology.Simplicial.ProperHypercovering.inverseImage_fullyFaithful_of_isHypercovering, Stacks.Topology.Simplicial.ProperHypercovering.abelianInverseImage_fullyFaithful_of_isHypercovering
statement: formalized
proof: formalized
---

# 85.25 Proper hypercoverings in topology

Section 85.25 of the Stacks Project, [Tag 09XA](https://stacks.math.columbia.edu/tag/09XA). 6 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DAF, a lemma

[Tag 0DAF](https://stacks.math.columbia.edu/tag/0DAF) in the Stacks Project.

**`Stacks.Topology.LocallyQuasiCompactZariskiSituation.comparisonSquarePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ProperHypercovering/ComparisonSquare.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Simplicial/ProperHypercovering/ComparisonSquare.lean#L277).

> **Stacks Tag 0DAF.** Let `U` be a simplicial object of `LC` and let `a : U → X` be an
> augmentation. There is a commutative diagram of topoi
>
> ```
> Sh((LC_qc/U)_total) --h--> Sh(U_Zar)
>         | a_qc                 | a
> Sh(LC_qc/X)       --h₋₁--> Sh(X)
> ```
>
> where the left vertical arrow is the augmentation `qcAugmentation` of Stacks Section 09X8, the
> right vertical arrow is the augmentation `augmentationMorphism` of Tag 09W4, the top arrow
> `totalComparisonMorphism` is the morphism of topoi of the continuous functor
> `U_Zar → (LC_qc/U)_total`, `V ↦ V/U_n`, and the bottom arrow `qcTopologicalMorphism` is the
> comparison morphism of the continuous functor `X_Zar → LC_qc/X`, `V ↦ V/X`. Commutativity is
> the natural isomorphism `a_* ∘ h_* ≅ h₋₁,* ∘ a_qc,*` of direct images.

```lean
def comparisonSquarePushforwardIso :
    (totalComparisonMorphism.{x} S U a).pushforward ⋙
        (augmentationMorphism (simplicialSpace S U) ((toTop S).obj X)
          (spaceAugmentation S U a)).pushforward ≅
      (qcAugmentation.{x} S U a).pushforward ⋙ (qcTopologicalMorphism.{u, w, 0} S X).pushforward
```

**`Stacks.Topology.Simplicial.qcSmallBottomMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/QcComparisonSquare.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Simplicial/QcComparisonSquare.lean#L203). The attribute's comment: “the lower horizontal arrow h\_\{-1} : Sh(LC\_qc/X) → Sh(X) of the diagram”.

> **The bottom horizontal arrow of the diagram of Tag 0DAF**, the comparison morphism of topoi
> `h₋₁ = a_X : Sh(LC_qc/X) → Sh(X)` of Section 09WY, with `Sh(LC_qc/X)` read as the sheaves on the
> localization of the small model.

```lean
def qcSmallBottomMorphism :
    MorphismOfTopoi (Sheaf (S.qcSite.smallOverTopology X) (Type u))
      (Sheaf (Opens.grothendieckTopology X.obj.obj) (Type u))
```

**`Stacks.Topology.Simplicial.qcComparisonSquarePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/QcComparisonSquare.lean, line 711](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Simplicial/QcComparisonSquare.lean#L711). The attribute's comment: “the commutative diagram of topoi, on direct images”.

> **Tag 0DAF.** The diagram of topoi
> ```
> Sh((LC_qc/U)_total) --h--> Sh(U_Zar)
>         | a_qc                 | a
> Sh(LC_qc/X)       --h₋₁--> Sh(X)
> ```
> commutes: the direct image of `h₋₁ ∘ a_qc` is that of `a ∘ h`.

```lean
def qcComparisonSquarePushforwardIso :
    (qcAugmentationMorphism S X U a).pushforward ⋙ (qcSmallBottomMorphism S X).pushforward ≅
      (qcSmallComparisonMorphism S X U a).pushforward ⋙
        (qcZariskiAugmentation S X U a).pushforward
```

**`Stacks.Topology.Simplicial.qcComparisonSquareInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/QcComparisonSquare.lean, line 722](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Simplicial/QcComparisonSquare.lean#L722). The attribute's comment: “the commutative diagram of topoi, on inverse images”.

> **Tag 0DAF**, on inverse images: `a_qc⁻¹ ∘ h₋₁⁻¹ ≅ h⁻¹ ∘ a⁻¹`. The inverse images are left
> adjoint to the direct images, so this is the conjugate of
> `qcComparisonSquarePushforwardIso`.

```lean
def qcComparisonSquareInverseImageIso :
    (qcZariskiAugmentation S X U a).inverseImage ⋙
        (qcSmallComparisonMorphism S X U a).inverseImage ≅
      qcSmallTopologicalInverseImage S X ⋙ (qcAugmentationMorphism S X U a).inverseImage
```

**`Stacks.Topology.Simplicial.exists_qcComparisonSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/QcComparisonSquare.lean, line 763](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Simplicial/QcComparisonSquare.lean#L763). The attribute's comment: “for an arbitrary simplicial object U of LC and augmentation a : U → X: a site LC\_qc containing X and the U\_n exists, and for it the diagram of topoi commutes”.

> **Tag 0DAF for an arbitrary simplicial object of `LC`.** Let `U` be a simplicial object of
> `LC` and let `a : U → X` be an augmentation. Then a site `LC_qc` of Tag 09X2 can be chosen
> containing `X` and every `U_n`, and for it the square of topoi
> `h₋₁ ∘ a_qc = a ∘ h` commutes, both on direct images and on inverse images. The right-hand
> column is the augmentation of `U_Zar` towards `X` of Tag 09W4 for the underlying simplicial
> space of `U` itself: the simplicial space of the lift is `U` followed by the inclusion of `LC`
> into topological spaces, on the nose.

```lean
theorem exists_qcComparisonSquare (Y : SimplicialObject LocallyQuasiCompactHausdorff.{u})
    (T : LocallyQuasiCompactHausdorff.{u}) (b : Y ⟶ (SimplicialObject.const _).obj T) :
    ∃ (S : LocallyQuasiCompactZariskiSituation.{u, u + 1} (Set.range Y.obj ∪ {T})
        Cardinal.stacksBound) (hY : ∀ n, S.qcSite.Contains (Y.obj n))
      (hT : S.qcSite.Contains T),
      qcSimplicialSpace S (qcLift S Y hY) = Y ⋙ locallyQuasiCompactHausdorffToTop ∧
      Nonempty ((qcAugmentationMorphism S ⟨T, hT⟩ (qcLift S Y hY)
          (qcLiftAugmentation S b hY hT)).pushforward ⋙
            (qcSmallBottomMorphism S ⟨T, hT⟩).pushforward ≅
        (qcSmallComparisonMorphism S ⟨T, hT⟩ (qcLift S Y hY)
          (qcLiftAugmentation S b hY hT)).pushforward ⋙
            (qcZariskiAugmentation S ⟨T, hT⟩ (qcLift S Y hY)
              (qcLiftAugmentation S b hY hT)).pushforward) ∧
      Nonempty ((qcZariskiAugmentation S ⟨T, hT⟩ (qcLift S Y hY)
          (qcLiftAugmentation S b hY hT)).inverseImage ⋙
            (qcSmallComparisonMorphism S ⟨T, hT⟩ (qcLift S Y hY)
              (qcLiftAugmentation S b hY hT)).inverseImage ≅
        qcSmallTopologicalInverseImage S ⟨T, hT⟩ ⋙
          (qcAugmentationMorphism S ⟨T, hT⟩ (qcLift S Y hY)
            (qcLiftAugmentation S b hY hT)).inverseImage)
```

**`Stacks.Topology.Simplicial.qcSmallComparisonMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/QcSmallTotalSiteComparison.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Simplicial/QcSmallTotalSiteComparison.lean#L477). The attribute's comment: “the upper horizontal arrow h : Sh((LC\_qc/U)\_total) → Sh(U\_Zar) of the diagram”.

> **The upper horizontal arrow of the diagram of Tag 0DAF**, the morphism of topoi
> `h : Sh((LC_qc/U)_total) ⟶ Sh(U_Zar)` of the comparison functor, with `(LC_qc/U)_total` formed
> in the small model as in Section 09X8. Its direct image is restriction along the comparison
> functor.

```lean
def qcSmallComparisonMorphism :
    MorphismOfTopoi (Sheaf (qcSmallTotalTopology S X U a) (Type u))
      (Sheaf (SimplicialOpen.grothendieckTopology (qcSimplicialSpace S U)) (Type u))
```

## Tag 0DAG, a lemma

[Tag 0DAG](https://stacks.math.columbia.edu/tag/0DAG) in the Stacks Project.

**`Stacks.Topology.Simplicial.ProperHypercovering.inverseImage_fullyFaithful_of_isHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ProperHypercoveringFullyFaithful.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Simplicial/ProperHypercoveringFullyFaithful.lean#L221). The attribute's comment: “sheaves of sets”.

> **Stacks 0DAG, sheaves of sets.** Let `U` be a simplicial object of `LC` and `a : U ⟶ X` an
> augmentation which is a proper hypercovering of `X`. Then `a^{-1} : Sh(X) ⥤ Sh(U_Zar)` is fully
> faithful, its essential image consists exactly of the cartesian sheaves, and `a_*` is a
> quasi-inverse: the unit of `a^{-1} ⊣ a_*` is invertible, and so is its counit at every
> cartesian sheaf. Here `a : Sh(U_Zar) ⟶ Sh(X)` is the morphism of topoi of Tag 09W4.

```lean
theorem inverseImage_fullyFaithful_of_isHypercovering
    (hyp : MorphismProperty.IsHypercovering properSurjective ⟨Y, X, a⟩) :
    (inverseImage Y X a).Full ∧ (inverseImage Y X a).Faithful ∧
      (∀ G, (inverseImage Y X a).essImage G ↔ IsCartesian (U Y) G) ∧
      (∀ F, IsIso ((augmentationTopoi Y X a).adj.unit.app F)) ∧
      (∀ G, IsCartesian (U Y) G → IsIso ((augmentationTopoi Y X a).adj.counit.app G))
```

**`Stacks.Topology.Simplicial.ProperHypercovering.abelianInverseImage_fullyFaithful_of_isHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ProperHypercoveringFullyFaithful.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Simplicial/ProperHypercoveringFullyFaithful.lean#L238). The attribute's comment: “sheaves of abelian groups”.

> **Stacks 0DAG, sheaves of abelian groups.** Let `U` be a simplicial object of `LC` and
> `a : U ⟶ X` an augmentation which is a proper hypercovering of `X`. Then
> `a^{-1} : Ab(X) ⥤ Ab(U_Zar)` is fully faithful, its essential image consists exactly of the
> cartesian abelian sheaves, and `a_*` is a quasi-inverse: the unit of `a^{-1} ⊣ a_*` is
> invertible, and so is its counit at every cartesian abelian sheaf.

```lean
theorem abelianInverseImage_fullyFaithful_of_isHypercovering
    (hyp : MorphismProperty.IsHypercovering properSurjective ⟨Y, X, a⟩) :
    (abelianInverseImage Y X a).Full ∧ (abelianInverseImage Y X a).Faithful ∧
      (∀ G, (abelianInverseImage Y X a).essImage G ↔ IsCartesianAb (U Y) G) ∧
      (∀ F, IsIso ((abelianAdjunction Y X a).unit.app F)) ∧
      (∀ G, IsCartesianAb (U Y) G → IsIso ((abelianAdjunction Y X a).counit.app G))
```

## Tag 09XS, a lemma

[Tag 09XS](https://stacks.math.columbia.edu/tag/09XS) in the Stacks Project.

**`Stacks.Topology.Simplicial.ProperHypercovering.isIso_derivedAdjunction_unit_app_of_isHypercovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ProperHypercovering/DerivedUnit.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Simplicial/ProperHypercovering/DerivedUnit.lean#L556).

> Let `U` be a simplicial object of the category `LC` of Hausdorff, locally quasi-compact spaces
> and let `a : U → X` be an augmentation. If `a : U → X` gives a proper hypercovering of `X`, then
> for `K` in `D⁺(X)` the canonical map
>
> `K ⟶ Ra_*(a^{-1}K)`
>
> is an isomorphism, where `a : Sh(U_Zar) → Sh(X)` is the morphism of topoi of Stacks 09W4.
>
> Here `U = Y`; the proper hypercovering condition of Stacks Section 09XA is
> `MorphismProperty.IsHypercovering properSurjective`; `D⁺(X)` is the bounded below derived category
> of abelian sheaves on `X`, for any model of the derived categories involved; `a^{-1}` is the exact
> inverse image of abelian sheaves of the morphism of topoi of Stacks 09W4 applied degreewise, and
> `Ra_*` is the right derived functor on bounded below derived categories of its direct image. The
> canonical map is the unit at `K` of the adjunction `a^{-1} ⊣ Ra_*` (`derivedAdjunction`).
>
> By Leray's acyclicity lemma (Stacks 015E) the statement reduces to the underived unit
> `F ⟶ a_* a^{-1} F` being an isomorphism, which is Stacks 0DAG, and to `R^q a_*(a^{-1}F) = 0` for
> `q > 0`, `isZero_rightDerived_abelianDirectImage_of_isHypercovering`, which is the computation of
> the source through the diagram of Stacks 0DAF; see the module documentation.

```lean
theorem isIso_derivedAdjunction_unit_app_of_isHypercovering
    (hyp : MorphismProperty.IsHypercovering properSurjective ⟨Y, X, a⟩)
    (K : DerivedCategory.Plus (Sheaf (Opens.grothendieckTopology
      (locallyQuasiCompactHausdorffToTop.obj X)) AddCommGrpCat.{u})) :
    IsIso ((derivedAdjunction Y X a).unit.app K)
```

## Tag 09XC, a lemma

[Tag 09XC](https://stacks.math.columbia.edu/tag/09XC) in the Stacks Project.

**`Stacks.Topology.Simplicial.ProperHypercovering.derivedGlobalSectionsIsoOfIsHypercovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ProperHypercovering/DerivedDescent.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Simplicial/ProperHypercovering/DerivedDescent.lean#L134).

> **Stacks Project, Tag 09XC.** Let `U` be a simplicial object of `LC` and let `a : U → X` be an
> augmentation. If `U` is a proper hypercovering of `X`, then
>
> `RΓ(X, K) = RΓ(U_Zar, a^{-1}K)`
>
> for `K ∈ D⁺(X)`, where `a : Sh(U_Zar) → Sh(X)` is the morphism of topoi of Lemma 09W4.
>
> Here `U = Y`, `X = T` and `a = b`; the proper hypercovering condition of Stacks Section 09XA is
> `MorphismProperty.IsHypercovering properSurjective`, `a^{-1}` is the inverse image of abelian
> sheaves along the morphism of topoi of Stacks 09W4, extended to `D⁺` degreewise because it is
> exact, and `RΓ(X, -)`, `RΓ(U_Zar, -)` are the right derived functors on `D⁺` of the global
> sections functors of the space `X` and of the site `U_Zar`. The derived categories are arbitrary
> models. The isomorphism is the canonical one: its forward map is the pullback on derived
> sections, `RΓ(X, -)` of the unit `K → Ra_*a^{-1}K` followed by the factorization
> `RΓ(U_Zar, -) = RΓ(X, -) ∘ Ra_*` of Stacks 08J6 (`derivedGlobalSectionsIsoOfIsHypercovering_hom`).
> It is invertible because the unit is, by `isIso_derivedAdjunction_unit_app_of_isHypercovering`
> (Stacks 09XS).

```lean
def derivedGlobalSectionsIsoOfIsHypercovering
    (hyp : MorphismProperty.IsHypercovering properSurjective ⟨Y, T, b⟩) :
    (Sheaf.Γ (Opens.grothendieckTopology (locallyQuasiCompactHausdorffToTop.obj T))
        AddCommGrpCat.{u}).rightDerivedFunctorPlus ≅
      (abelianInverseImage Y T b).mapDerivedCategoryPlus ⋙
        (Sheaf.Γ (SimplicialOpen.grothendieckTopology (U Y))
          AddCommGrpCat.{u}).rightDerivedFunctorPlus
```

## Tag 0DAH, a lemma

[Tag 0DAH](https://stacks.math.columbia.edu/tag/0DAH) in the Stacks Project.

**`Stacks.Topology.Simplicial.ProperHypercovering.derivedInverseImage_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ProperHypercovering/DerivedEquivalence.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Simplicial/ProperHypercovering/DerivedEquivalence.lean#L85).

> **Stacks Project, Tag 0DAH.** Let `U` be a simplicial object of the category `LC` of Hausdorff,
> locally quasi-compact spaces and let `a : U → X` be an augmentation. Let `𝒜 ⊂ Ab(U_Zar)` denote
> the weak Serre subcategory of cartesian abelian sheaves. If `U` is a proper hypercovering of `X`,
> then the functor `a⁻¹` defines an equivalence
>
> `D⁺(X) ⟶ D⁺_𝒜(U_Zar)`
>
> with quasi-inverse `R a_*`, where `a : Sh(U_Zar) → Sh(X)` is the morphism of topoi of Stacks 09W4.
>
> Here `U = Y`; the proper hypercovering condition of Stacks Section 09XA is
> `MorphismProperty.IsHypercovering properSurjective`; `𝒜` is `IsCartesianAb (U Y)`, which is a
> weak Serre subcategory (the first conjunct); `D⁺_𝒜(U_Zar)` is `cartesianPlus Y`, the objects of
> `D⁺(U_Zar)` all of whose cohomology sheaves are cartesian; `a⁻¹` is the exact functor
> `(abelianInverseImage Y X a).mapDerivedCategoryPlus` and `R a_*` the total right derived functor
> of `a_*`. The derived categories are arbitrary models.

```lean
theorem derivedInverseImage_equivalence
    (hyp : MorphismProperty.IsHypercovering properSurjective ⟨Y, X, a⟩) :
    ObjectProperty.IsWeakSerreClass (IsCartesianAb (U Y)) ∧
      ∃ e : DerivedCategory.Plus (Sheaf (Opens.grothendieckTopology
          (locallyQuasiCompactHausdorffToTop.obj X)) AddCommGrpCat.{u}) ≌
            (cartesianPlus Y).FullSubcategory,
        e.functor = (cartesianPlus Y).lift (abelianInverseImage Y X a).mapDerivedCategoryPlus
          (cartesianPlus_mapDerivedCategoryPlus_obj Y X a) ∧
        e.inverse = (cartesianPlus Y).ι ⋙ (abelianDirectImage Y X a).rightDerivedFunctorPlus
```

## Tag 09XB, a lemma

[Tag 09XB](https://stacks.math.columbia.edu/tag/09XB) in the Stacks Project.

**`Stacks.Topology.Simplicial.properHypercoveringSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Simplicial/ProperHypercovering/SpectralSequence.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Simplicial/ProperHypercovering/SpectralSequence.lean#L340).

> Let `U` be a simplicial object of the category `LC` of Hausdorff, locally quasi-compact spaces
> and let `a : U → X` be an augmentation. Let `F` be an abelian sheaf on `X` and let `F_n` be its
> pullback to `U_n`. If `U` is a proper hypercovering of `X`, there is a canonical spectral sequence
>
> `E_1^{p,q} = H^q(U_p, F_p)`
>
> converging to `H^{p+q}(X, F)`.
>
> Here `U = Y`, `X = T` and `a = b`; the proper hypercovering condition of Stacks Section 09XA is
> `MorphismProperty.IsHypercovering properSurjective`. The spectral sequence is a functor of `F`,
> its first page is identified with `H^q(U_p, F_p)` naturally in `F`, and it abuts to `H^n(X, F)`
> (`SpectralSequence.AbutsTo`, the convergence of Stacks 01F2).

```lean
def properHypercoveringSpectralSequence
    (hyp : MorphismProperty.IsHypercovering ProperHypercovering.properSurjective ⟨Y, T, b⟩) :
    ProperHypercoveringSpectralSequence Y T b
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.25, Tag 09XA](https://stacks.math.columbia.edu/tag/09XA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

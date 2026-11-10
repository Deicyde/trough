---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.isDerivedLimit_tensorDerivedDual_of_isHomotopyColimit_of_isPerfect, Stacks.SheafOfModules.derivedDualPairingSquare_cup, Stacks.Cohomology.DerivedInternalHomPullback.isIso_derivedPullbackSheafHomMap_of_hasFiniteTorDimensionOverInverseImage, Stacks.Cohomology.DerivedInternalHomPullback.isIso_derivedPullbackSheafHomMap_of_isPerfect, Stacks.Cohomology.DerivedInternalHomPullback.isIso_derivedPullbackSheafHomMap_of_isPseudoCoherent, Stacks.Cohomology.DerivedInternalHomStalk.isIso_stalkSheafHomMap_of_isPerfect, Stacks.Cohomology.DerivedInternalHomStalk.isIso_stalkSheafHomMap_of_isPseudoCoherent
statement: formalized
proof: formalized
---

# 20.51 Miscellany

Section 20.51 of the Stacks Project, [Tag 0GM6](https://stacks.math.columbia.edu/tag/0GM6). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DJI, a lemma

[Tag 0DJI](https://stacks.math.columbia.edu/tag/0DJI) in the Stacks Project.

**`Stacks.SheafOfModules.isDerivedLimit_tensorDerivedDual_of_isHomotopyColimit_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedHomOfAHomotopyColimit.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedHomOfAHomotopyColimit.lean#L257). The attribute's comment: “the whole tag: for a system of perfect objects `Kₙ` of `D(O_X)` with `K = hocolim Kₙ` and every `E` in `D(O_X)`, the identity `RSheafHom(K, E) = R lim (E ⊗^L_{O_X} Kₙ^∨)`”.

> **Stacks 0DJI.** Let `(X, O_X)` be a ringed space, let `(Kₙ)` be a system of **perfect**
> objects of `D(O_X)` and let `K = hocolim Kₙ`. Then for every object `E` of `D(O_X)`
>
> `RSheafHom(K, E) = R lim (E ⊗^L_{O_X} Kₙ^∨)`.
>
> The source uses the perfectness of the `Kₙ` to invoke the third assertion of Stacks 08DQ, which
> is `isIso_derivedTensorDualToSheafHom_of_isPerfect`.

```lean
theorem isDerivedLimit_tensorDerivedDual_of_isHomotopyColimit_of_isPerfect
    (F : ℕ ⥤ DerivedCategory (StructureSheafModules Rc))
    (E : DerivedCategory (StructureSheafModules Rc))
    (hperf : ∀ n : ℕ, (ringedSite Rc).IsPerfect (F.obj n))
    {K : DerivedCategory (StructureSheafModules Rc)} (hK : IsHomotopyColimit F K) :
    IsDerivedLimit (tensorDerivedDualSystem Rc F E)
      (((derivedSheafHom Rc).flip.obj E).obj (op K))
```

## Tag 0FVB, a lemma

[Tag 0FVB](https://stacks.math.columbia.edu/tag/0FVB) in the Stacks Project.

**`Stacks.SheafOfModules.derivedDualPairingSquare_cup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DualityPairingCupProduct.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DualityPairingCupProduct.lean#L510).

> **Stacks 0FVB.** Let `(X, O_X)` be a ringed space
> and let `K` and `E` be objects of `D(O_X)` with `E` perfect (Tag 08CM). The diagram
>
> `H⁰(X, K ⊗^L E^∨) × H⁰(X, E) ⟶ H⁰(X, (K ⊗^L E^∨) ⊗^L E)`
> `        ↓                               ↓`
> `Hom_X(E, K) × H⁰(X, E)        ⟶       H⁰(X, K)`
>
> commutes: the cup product `ξ ∪ η` (Section 0FKU, the relative cup product of Stacks 0B68 for
> `(X, O_X) ⟶ (pt, Γ(X, O_X))`, `Stacks.SheafOfModules.globalCupProductZero`) followed by the map
> induced on `H⁰` by `1_K ⊗ ε` and the unit constraint (`ε : E^∨ ⊗^L E ⟶ O_X` of Example 0FPC)
> is the morphism `E ⟶ K` attached to `ξ` by the identification
> `H⁰(X, K ⊗^L E^∨) = Hom_{D(O_X)}(E, K)` of Lemma 08DQ
> (`Stacks.SheafOfModules.derivedTensorDualGlobalSectionsMap`), evaluated on `η`.

```lean
theorem derivedDualPairingSquare_cup (K E : DerivedCategory (StructureSheafModules X.sheaf))
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X) E)
    (ξ : ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
      ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj
        (((derivedTensor X.sheaf).obj K).obj (derivedDual X.sheaf E))) : Type u))
    (η : ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
      ((derivedModuleGlobalSections (ringedSite X.sheaf)).obj E) : Type u)) :
    (DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).map
        ((derivedModuleGlobalSections (ringedSite X.sheaf)).map
          (derivedDualContraction X.sheaf K E))
        (globalCupProductZero X (((derivedTensor X.sheaf).obj K).obj (derivedDual X.sheaf E)) E
          ξ η) =
      (DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).map
        ((derivedModuleGlobalSections (ringedSite X.sheaf)).map
          (derivedTensorDualGlobalSectionsMap X.sheaf E K ξ)) η
```

## Tag 0GM7, a lemma

[Tag 0GM7](https://stacks.math.columbia.edu/tag/0GM7) in the Stacks Project.

**`Stacks.Cohomology.DerivedInternalHomPullback.isIso_derivedPullbackSheafHomMap_of_hasFiniteTorDimensionOverInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomPullbackFiniteTorDimension.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomPullbackFiniteTorDimension.lean#L220). The attribute's comment: “clause (3)”.

> **Pullback of a derived internal hom along a morphism of finite tor dimension.** Let
> `h : X ⟶ Y` be a morphism of ringed spaces such that `𝒪_X` has finite tor dimension over
> `h⁻¹𝒪_Y`. For a pseudo-coherent `K ∈ D(𝒪_Y)` and a locally bounded below `M ∈ D(𝒪_Y)`, the
> canonical map `Lh^*R𝓗om(K, M) ⟶ R𝓗om(Lh^*K, Lh^*M)` of Tag 08I3 is an isomorphism.

```lean
theorem isIso_derivedPullbackSheafHomMap_of_hasFiniteTorDimensionOverInverseImage
    (hh : HasFiniteTorDimensionOverInverseImage h)
    (K : DerivedCategory (AlgebraicGeometry.RingedSpace.KFlatDerivedPullback.Modules Y))
    (hK : AlgebraicGeometry.RingedSpace.PseudoCoherence.IsPseudoCoherent (X := Y) K)
    (M : DerivedCategory (AlgebraicGeometry.RingedSpace.KFlatDerivedPullback.Modules Y))
    (hM : AlgebraicGeometry.RingedSpace.IsLocallyBoundedBelow Y M) :
    IsIso (derivedPullbackSheafHomMap h K M)
```

**`Stacks.Cohomology.DerivedInternalHomPullback.isIso_derivedPullbackSheafHomMap_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomPullbackPerfectAndPseudoCoherent.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomPullbackPerfectAndPseudoCoherent.lean#L59). The attribute's comment: “clause (1)”.

> **Pullback of a derived internal hom out of a perfect object.**  For a morphism of ringed
> spaces `h : X ⟶ Y`, a perfect `K ∈ D(𝒪_Y)` and an arbitrary `M ∈ D(𝒪_Y)`, the canonical map
> `Lh^*R𝓗om(K, M) ⟶ R𝓗om(Lh^*K, Lh^*M)` is an isomorphism.

```lean
theorem isIso_derivedPullbackSheafHomMap_of_isPerfect
    (K : DerivedCategory (AlgebraicGeometry.RingedSpace.KFlatDerivedPullback.Modules Y))
    (hK : AlgebraicGeometry.RingedSpace.IsPerfect (X := Y) K)
    (M : DerivedCategory (AlgebraicGeometry.RingedSpace.KFlatDerivedPullback.Modules Y)) :
    IsIso (derivedPullbackSheafHomMap h K M)
```

**`Stacks.Cohomology.DerivedInternalHomPullback.isIso_derivedPullbackSheafHomMap_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomPullbackPerfectAndPseudoCoherent.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomPullbackPerfectAndPseudoCoherent.lean#L71). The attribute's comment: “clause (2)”.

> **Flat pullback of a derived internal hom out of a pseudo-coherent object.**  For a flat
> morphism of ringed spaces `h : X ⟶ Y`, a pseudo-coherent `K ∈ D(𝒪_Y)` and a locally bounded below
> `M ∈ D(𝒪_Y)`, the canonical map `Lh^*R𝓗om(K, M) ⟶ R𝓗om(Lh^*K, Lh^*M)` is an isomorphism.

```lean
theorem isIso_derivedPullbackSheafHomMap_of_isPseudoCoherent (hh : AlgebraicGeometry.IsFlat h)
    (K : DerivedCategory (AlgebraicGeometry.RingedSpace.KFlatDerivedPullback.Modules Y))
    (hK : AlgebraicGeometry.RingedSpace.PseudoCoherence.IsPseudoCoherent (X := Y) K)
    (M : DerivedCategory (AlgebraicGeometry.RingedSpace.KFlatDerivedPullback.Modules Y))
    (hM : AlgebraicGeometry.RingedSpace.IsLocallyBoundedBelow Y M) :
    IsIso (derivedPullbackSheafHomMap h K M)
```

## Tag 0GM8, a lemma

[Tag 0GM8](https://stacks.math.columbia.edu/tag/0GM8) in the Stacks Project.

**`Stacks.Cohomology.DerivedInternalHomStalk.isIso_stalkSheafHomMap_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomStalkInvertibility.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomStalkInvertibility.lean#L66). The attribute's comment: “case (1): K perfect, M arbitrary”.

> **Tag 0GM8, case (1).**  For a ringed space `X`, a point `x ∈ X`, a perfect `K ∈ D(𝒪_X)` and
> an arbitrary `M ∈ D(𝒪_X)`, the canonical map
>
> `R𝓗om_{𝒪_X}(K, M)_x ⟶ RHom_{𝒪_{X,x}}(K_x, M_x)`
>
> is an isomorphism.  Here `Y = {x}` is the one-point ringed space with structure sheaf `𝒪_{X,x}`,
> and the map is the canonical map of Tag 08I3 along the flat inclusion `Y ⟶ X`, read through the
> identification `D(𝒪_Y) ≌ D(𝒪_{X,x})` given by the stalk.

```lean
theorem isIso_stalkSheafHomMap_of_isPerfect
    (hK : AlgebraicGeometry.RingedSpace.IsPerfect (X := X) K) :
    IsIso (stalkSheafHomMap X x (pointStalkPresentation X x) K M)
```

**`Stacks.Cohomology.DerivedInternalHomStalk.isIso_stalkSheafHomMap_of_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomStalkInvertibility.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/InternalHomStalkInvertibility.lean#L79). The attribute's comment: “case (2): K pseudo-coherent, M locally bounded below”.

> **Tag 0GM8, case (2).**  For a ringed space `X`, a point `x ∈ X`, a pseudo-coherent
> `K ∈ D(𝒪_X)` and a locally bounded below `M ∈ D(𝒪_X)`, the canonical map
>
> `R𝓗om_{𝒪_X}(K, M)_x ⟶ RHom_{𝒪_{X,x}}(K_x, M_x)`
>
> is an isomorphism, the map being that of `isIso_stalkSheafHomMap_of_isPerfect`.

```lean
theorem isIso_stalkSheafHomMap_of_isPseudoCoherent
    (hK : AlgebraicGeometry.RingedSpace.PseudoCoherence.IsPseudoCoherent (X := X) K)
    (hM : AlgebraicGeometry.RingedSpace.IsLocallyBoundedBelow X M) :
    IsIso (stalkSheafHomMap X x (pointStalkPresentation X x) K M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.51, Tag 0GM6](https://stacks.math.columbia.edu/tag/0GM6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

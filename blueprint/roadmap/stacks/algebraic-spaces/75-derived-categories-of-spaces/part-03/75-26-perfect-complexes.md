---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isEtaleLocallyConstructible_setOf_eq, AlgebraicGeometry.Space.upperSemicontinuous_of_isEtaleLocallyDerivedFibreBetti, AlgebraicGeometry.Space.upperSemicontinuous_geometricFibreBettiFunction, AlgebraicGeometry.Space.isEtaleLocallyConstructible_setOf_geometricFibreBettiFunction_eq, AlgebraicGeometry.Space.geometricFibreBettiFunction_derivedPullback, AlgebraicGeometry.Space.fibreBetti_baseChange, AlgebraicGeometry.Space.upperSemicontinuous_fibreBetti, AlgebraicGeometry.Space.isLocallyConstructible_fibreBetti_preimage
statement: formalized
proof: formalized
---

# 75.26 Perfect complexes

Section 75.26 of the Stacks Project, [Tag 0D1X](https://stacks.math.columbia.edu/tag/0D1X). 8 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D1Y, a lemma

[Tag 0D1Y](https://stacks.math.columbia.edu/tag/0D1Y) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtaleLocallyConstructible_setOf_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BettiNumbersOnPoints.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BettiNumbersOnPoints.lean#L120). The attribute's comment: “constructible levels, for a Betti-number function given as data”.

> **Stacks 0D1Y, the level sets of a Betti-number function are étale locally
> constructible.** The Betti-number function is data, characterised by `hβ`: the function of
> Stacks 0D1Y is built, but nothing identifies it with a derived-fibre Betti function on a
> scheme chart. `constructibleLevels` is part (3) of Stacks 0BDI, the same statement for a
> scheme, which holds for every scheme and is supplied in
> `StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BettiNumbersOnPointsUnconditional.lean`.

```lean
theorem isEtaleLocallyConstructible_setOf_eq
    (hβ : IsEtaleLocallyDerivedFibreBetti B S hS X β i)
    (constructibleLevels : ∀ (Z : Scheme.{u}) (F : DerivedCategory Z.Modules)
      (hF : RingedSpace.IsPseudoCoherent (X := Z.toRingedSpace) F) (m : ℕ),
      IsLocallyConstructible {z : Z | DerivedFibreBetti.derivedFiberBetti Z F hF i z = m})
    (n : ℕ) :
    IsEtaleLocallyConstructible B S hS X {x | β x = n}
```

**`AlgebraicGeometry.Space.upperSemicontinuous_of_isEtaleLocallyDerivedFibreBetti`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BettiNumbersOnPoints.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BettiNumbersOnPoints.lean#L148). The attribute's comment: “upper semicontinuity, for a Betti-number function given as data”.

> **Stacks 0D1Y, upper semicontinuity of a Betti-number function.** The Betti-number
> function is data, characterised by `hβ`: the function of Stacks 0D1Y is built, but nothing
> identifies it with a derived-fibre Betti function on a scheme chart.
> `upperSemicontinuousBetti` is part (2) of Stacks 0BDI, the same statement for a scheme, which
> holds for every scheme and is supplied in
> `StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BettiNumbersOnPointsUnconditional.lean`.

```lean
theorem upperSemicontinuous_of_isEtaleLocallyDerivedFibreBetti
    (hX : IsAlgebraicSpace B S hS X)
    (hβ : IsEtaleLocallyDerivedFibreBetti B S hS X β i)
    (upperSemicontinuousBetti : ∀ (Z : Scheme.{u}) (F : DerivedCategory Z.Modules)
      (hF : RingedSpace.IsPseudoCoherent (X := Z.toRingedSpace) F),
      UpperSemicontinuous (DerivedFibreBetti.derivedFiberBetti Z F hF i)) :
    UpperSemicontinuous β
```

**`AlgebraicGeometry.Space.upperSemicontinuous_geometricFibreBettiFunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BettiNumbersOnPointsPseudoCoherent.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BettiNumbersOnPointsPseudoCoherent.lean#L215). The attribute's comment: “clause (2)”.

> **Stacks 0D1Y, clause (2): the functions `β_i` are upper semi-continuous.**  For a
> pseudo-coherent object `E` of `D(𝒪_X)` on an algebraic space `X` over `S`, the `i`-th
> Betti-number function `β_i : |X| → ℕ` of `E` is upper semicontinuous.
>
> Nothing is assumed beyond pseudo-coherence of `E`.  The scheme-level input is part (2) of
> [Stacks, Tag 0BDI].

```lean
theorem upperSemicontinuous_geometricFibreBettiFunction
    (E : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hE : (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent E) (i : ℤ) :
    UpperSemicontinuous (geometricFibreBettiFunction B S hS E i)
```

**`AlgebraicGeometry.Space.isEtaleLocallyConstructible_setOf_geometricFibreBettiFunction_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BettiNumbersOnPointsPseudoCoherent.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BettiNumbersOnPointsPseudoCoherent.lean#L231). The attribute's comment: “clause (3)”.

> **Stacks 0D1Y, clause (3): the level sets of `β_i` are étale locally constructible.**  For a
> pseudo-coherent object `E` of `D(𝒪_X)` on an algebraic space `X` over `S` and a natural number
> `n`, the level set `{x ∈ |X| : β_i(x) = n}` is étale locally constructible in the sense of
> [Stacks, Tag 0ECU].
>
> Nothing is assumed beyond pseudo-coherence of `E`.  The scheme-level input is part (3) of
> [Stacks, Tag 0BDI].

```lean
theorem isEtaleLocallyConstructible_setOf_geometricFibreBettiFunction_eq
    (E : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)))
    (hE : (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent E) (i : ℤ) (n : ℕ) :
    IsEtaleLocallyConstructible B S hS X.1 {x | geometricFibreBettiFunction B S hS E i x = n}
```

**`AlgebraicGeometry.Space.geometricFibreBettiFunction_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedFibreBettiFunction.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedFibreBettiFunction.lean#L179). The attribute's comment: “clause (1)”.

> **Stacks 0D1Y, clause (1): formation of `β_i` commutes with arbitrary base change.** For a
> morphism `g : Y ⟶ X` of algebraic spaces the Betti-number function of `Lg^*E` is the Betti-number
> function of `E` composed with the map `|Y| → |X|`.

```lean
theorem geometricFibreBettiFunction_derivedPullback {Y : AlgebraicSpaces B S hS} (g : Y ⟶ X)
    (E : @DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS X)) _ _
      (HasDerivedCategory.standard _))
    (_hE : @AlgebraicGeometry.RingedSite.IsPseudoCoherent
      (smallEtaleRingedSite B S hS X.1 X.2) _ _ _ _ _ _ (HasDerivedCategory.standard _) E)
    (i : ℤ) :
    geometricFibreBettiFunction B S hS ((smallEtaleDerivedModulePullback B S hS g).obj E) i =
      geometricFibreBettiFunction B S hS E i ∘ pointsMap B S hS Y.1 g.hom
```

## Tag 0E0R, a lemma

[Tag 0E0R](https://stacks.math.columbia.edu/tag/0E0R) in the Stacks Project.

**`AlgebraicGeometry.Space.fibreBetti_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/FibreBettiNumbers.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/FibreBettiNumbers.lean#L115). The attribute's comment: “(1)”.

> **Stacks 0E0R, part (1): the formation of `β_i` commutes with arbitrary base change.** For
> `f : X ⟶ Y` proper and of finite presentation, `𝓕` of finite presentation and flat over `Y`,
> and any morphism `g : Y' ⟶ Y` of schemes of the site, the `i`-th Betti-number function of the
> base change `(X ×_Y Y' ⟶ Y', 𝓕_{Y'})` is `β_i ∘ g`.

```lean
theorem fibreBetti_baseChange (hf : IsProper B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hFfp : F.IsFinitePresentation) (hF : IsFlatOver B S hS X.2 f.hom F)
    {U' : BigFppfOver B S hS} (g : U' ⟶ U) (i : ℤ) :
    fibreBetti (pullback.snd f (representedSpaceMap B S hS g))
        ((modulePullback B S hS (pullback.fst f (representedSpaceMap B S hS g))).obj F) i =
      fibreBetti f F i ∘ ((BigFppfOver.toScheme B S hS).map g).base
```

**`AlgebraicGeometry.Space.upperSemicontinuous_fibreBetti`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/FibreBettiNumbers.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/FibreBettiNumbers.lean#L268). The attribute's comment: “(2)”.

> **Stacks 0E0R, part (2): the Betti numbers of the fibres are upper semicontinuous.** For
> `f : X ⟶ Y` proper and of finite presentation and `𝓕` of finite presentation and flat over `Y`,
> the function `y ↦ dim_{κ(y)} Hⁱ(X_y, 𝓕_y)` is upper semicontinuous on `Y`.

```lean
theorem upperSemicontinuous_fibreBetti (hf : IsProper B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hFfp : F.IsFinitePresentation) (hF : IsFlatOver B S hS X.2 f.hom F) (i : ℤ) :
    UpperSemicontinuous (fibreBetti f F i)
```

**`AlgebraicGeometry.Space.isLocallyConstructible_fibreBetti_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/FibreBettiNumbers.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/FibreBettiNumbers.lean#L286). The attribute's comment: “(3)”.

> **Stacks 0E0R, part (3): the level sets of the Betti numbers of the fibres are locally
> constructible.** For `f : X ⟶ Y` proper and of finite presentation and `𝓕` of finite
> presentation and flat over `Y`, each set `{y | dim_{κ(y)} Hⁱ(X_y, 𝓕_y) = n}` is locally
> constructible in `Y`.

```lean
theorem isLocallyConstructible_fibreBetti_preimage (hf : IsProper B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hFfp : F.IsFinitePresentation) (hF : IsFlatOver B S hS X.2 f.hom F) (i : ℤ) (n : ℕ) :
    Topology.IsLocallyConstructible (fibreBetti f F i ⁻¹' {n})
```

**`AlgebraicGeometry.Space.ProperFlatStein.isLocallyConstructible_fibreBetti_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperFlatStein/FibreBettiLevelSets.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperFlatStein/FibreBettiLevelSets.lean#L46). The attribute's comment: “(3)”.

> **Stacks 0E0R, part (3): the level sets of the Betti numbers of the fibres are locally
> constructible.** For `f : X ⟶ Y` proper and of finite presentation and `𝓕` of finite
> presentation and flat over `Y`, each set `{y | dim_{κ(y)} Hⁱ(X_y, 𝓕_y) = n}` is locally
> constructible in `Y`.

```lean
theorem isLocallyConstructible_fibreBetti_preimage (hf : IsProper B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hFfp : F.IsFinitePresentation) (hF : IsFlatOver B S hS X.2 f.hom F) (i : ℤ) (n : ℕ) :
    Topology.IsLocallyConstructible (fibreBettiFunction f F i ⁻¹' {n})
```

**`AlgebraicGeometry.Space.ProperFlatStein.fibreBetti_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperFlatStein/FibreBettiNumbers.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperFlatStein/FibreBettiNumbers.lean#L243). The attribute's comment: “(1)”.

> **Stacks 0E0R, part (1): the formation of `β_i` commutes with arbitrary base change.** For
> `f : X ⟶ Y` proper and of finite presentation, `𝓕` of finite presentation and flat over `Y`,
> and any morphism `g : Y' ⟶ Y` of schemes of the site, the `i`-th Betti-number function of the
> base change `(X ×_Y Y' ⟶ Y', 𝓕_{Y'})` is `β_i ∘ g`.

```lean
theorem fibreBetti_baseChange (hf : IsProper B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hFfp : F.IsFinitePresentation) (hF : IsFlatOver B S hS X.2 f.hom F)
    {U' : BigFppfOver B S hS} (g : U' ⟶ U) (i : ℤ) :
    fibreBettiFunction (pullback.snd f (representedSpaceMap B S hS g))
        ((modulePullback B S hS (pullback.fst f (representedSpaceMap B S hS g))).obj F) i =
      fibreBettiFunction f F i ∘ ((BigFppfOver.toScheme B S hS).map g).base
```

**`AlgebraicGeometry.Space.ProperFlatStein.upperSemicontinuous_fibreBetti`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperFlatStein/FibreBettiNumbers.lean, line 469](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperFlatStein/FibreBettiNumbers.lean#L469). The attribute's comment: “(2)”.

> **Stacks 0E0R, part (2): the Betti numbers of the fibres are upper semicontinuous.** For
> `f : X ⟶ Y` proper and of finite presentation and `𝓕` of finite presentation and flat over `Y`,
> the function `y ↦ dim_{κ(y)} Hⁱ(X_y, 𝓕_y)` is upper semicontinuous on `Y`.

```lean
theorem upperSemicontinuous_fibreBetti (hf : IsProper B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom) (F : Modules.{u, u} B S hS X.1 X.2)
    (hFfp : F.IsFinitePresentation) (hF : IsFlatOver B S hS X.2 f.hom F) (i : ℤ) :
    UpperSemicontinuous (fibreBettiFunction f F i)
```

## Tag 0D1Z, a lemma

[Tag 0D1Z](https://stacks.math.columbia.edu/tag/0D1Z) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyConstant_derivedFibreEuler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedFibreEulerLocallyConstant.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedFibreEulerLocallyConstant.lean#L294). References: SGA 6 III (5.5), “(i), special case”.

> **Stacks 0D1Z.**  Let `Y` be an algebraic space and `K` a perfect object of `D(𝒪_Y)`.  The
> derived-fibre Euler characteristic `y ↦ ∑ (-1)^n dim_k H^n(K ⊗^𝐋 k)` is locally constant on
> `|Y|`.
>
> The function is `AlgebraicGeometry.Space.derivedFibreEuler`, the alternating sum of the
> dimensions of the cohomology of `Lp^*K` for a field-valued point `p` representing the point; by
> `AlgebraicGeometry.Space.derivedFibreEuler_class` it may be computed at any representative.

```lean
theorem isLocallyConstant_derivedFibreEuler (Y : AlgebraicSpaces B S hS)
    (K : DerivedCategory (SheafOfModules.{u} (ringedToposStructureRingSheaf B S hS Y)))
    (hK : (smallEtaleRingedSite B S hS Y.1 Y.2).IsPerfect K) :
    IsLocallyConstant (derivedFibreEuler Y K)
```

**`AlgebraicGeometry.Space.isLocallyConstant_of_isEtaleLocallyDerivedFibreChi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/EulerCharacteristicOnPoints.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/EulerCharacteristicOnPoints.lean#L93). The attribute's comment: “for a derived-fibre Euler characteristic given as data”.

> **Stacks 0D1Z.**  The derived-fibre Euler characteristic of a perfect object of `D(𝒪_X)`
> on an algebraic space `X` is locally constant on `|X|`.
>
> The function is data, characterised by `hχ` (see the implementation notes); the proof
> reduces to the case of schemes, Stacks 0BDJ, by étale localization.

```lean
theorem isLocallyConstant_of_isEtaleLocallyDerivedFibreChi
    (hX : IsAlgebraicSpace B S hS X)
    (hχ : IsEtaleLocallyDerivedFibreChi B S hS X χ) :
    IsLocallyConstant χ
```

## Tag 0D20, a lemma

[Tag 0D20](https://stacks.math.columbia.edu/tag/0D20) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteLocallyFreeOfIntRankInDegree_of_isSingleDegreeRankLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SingleDegreeRankOpenSubspace.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SingleDegreeRankOpenSubspace.lean#L209). The attribute's comment: “clause (1), for an open subspace with the characterising universal property of clause (2); existence of such an open subspace is not proved”.

> **Clause (1) of Stacks 0D20.**  On an open subspace with the universal property of clause
> (2), the object `E` is a finite locally free module of rank `r` placed in degree `i`: the
> inclusion of the open subspace factors through it by way of the identity, so the universal
> property applies to it.

```lean
theorem isFiniteLocallyFreeOfIntRankInDegree_of_isSingleDegreeRankLocus
    (U : OpenSubspaces B S hS X.1)
    [(smallEtaleModulePullbackOnHomotopy B S hS
        (openSubspaceImmersion B S hS U)).HasLeftDerivedFunctor
      (smallEtaleModuleQuasiIso B S hS X)]
    (hU : IsSingleDegreeRankLocus B S hS X E i r U) :
    IsFiniteLocallyFreeOfIntRankInDegree B S hS (openSubspaceAsSpace B S hS U)
      ((smallEtaleDerivedModulePullback B S hS (openSubspaceImmersion B S hS U)).obj E) i r
```

**`AlgebraicGeometry.Space.eq_of_isSingleDegreeRankLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SingleDegreeRankOpenSubspace.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SingleDegreeRankOpenSubspace.lean#L241). The attribute's comment: “uniqueness of an open subspace with the characterising universal property of clause (2); existence of such an open subspace is not proved”.

> **The uniqueness half of "there exists an open subspace characterised by" in Stacks
> 0D20.**  At most one open subspace of `X` has the universal property of clause (2).
>
> Each of the two inclusions factors through the other open subspace, because by clause (1) the
> restriction of `E` along it has the required shape and the other open subspace's universal
> property turns that into a factorization; and a subfunctor through which another's inclusion
> factors contains it.

```lean
theorem eq_of_isSingleDegreeRankLocus (U U' : OpenSubspaces B S hS X.1)
    [(smallEtaleModulePullbackOnHomotopy B S hS
        (openSubspaceImmersion B S hS U)).HasLeftDerivedFunctor
      (smallEtaleModuleQuasiIso B S hS X)]
    [(smallEtaleModulePullbackOnHomotopy B S hS
        (openSubspaceImmersion B S hS U')).HasLeftDerivedFunctor
      (smallEtaleModuleQuasiIso B S hS X)]
    (hU : IsSingleDegreeRankLocus B S hS X E i r U)
    (hU' : IsSingleDegreeRankLocus B S hS X E i r U') :
    U = U'
```

**`AlgebraicGeometry.Space.exists_isSingleDegreeRankLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SingleDegreeRankOpenSubspaceExistence.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/SingleDegreeRankOpenSubspaceExistence.lean#L103).

> **Stacks 0D20.** Let `X` be an algebraic space over `S`, let `E` be a perfect object of
> `D(𝒪_X)` and let `i, r ∈ ℤ`. There is an open subspace `U ⊆ X`, and only one, characterised by:
> (1) `E|_U ≅ M[-i]` for a finite locally free `𝒪_U`-module `M` of rank `r` (so `M = H^i(E|_U)`);
> (2) a morphism `f : Y → X` factors through `U` if and only if `Lf^*E` is a finite locally free
> module of rank `r` placed in degree `i`.

```lean
theorem exists_isSingleDegreeRankLocus
    (hE : RingedSite.IsPerfect (smallEtaleRingedSite B S hS X.1 X.2) E) :
    ∃ U : OpenSubspaces B S hS X.1,
      IsFiniteLocallyFreeOfIntRankInDegree B S hS (openSubspaceAsSpace B S hS U)
        ((smallEtaleDerivedModulePullback B S hS (openSubspaceImmersion B S hS U)).obj E) i r ∧
      IsSingleDegreeRankLocus B S hS X E i r U ∧
      ∀ U' : OpenSubspaces B S hS X.1, IsSingleDegreeRankLocus B S hS X E i r U' → U' = U
```

## Tag 0E6A, a lemma

[Tag 0E6A](https://stacks.math.columbia.edu/tag/0E6A) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.exists_openSubspace_iff_isFiniteLocallyFreeOfIntRankInDegree_of_isProper`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeProper.lean#L132), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeProperTags.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CohomologyBaseChangeProperTags.lean#L34) (StacksFrontier).

## Tag 0D21, a lemma

[Tag 0D21](https://stacks.math.columbia.edu/tag/0D21) in the Stacks Project.

**`AlgebraicGeometry.Space.BottomRankLocus.exists_isBottomRankStratum_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BottomRankStratumExistence.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/BottomRankStratumExistence.lean#L582).

> **Stacks 0D21.** Let `E` be a perfect object of `D(𝒪_X)` of Tor amplitude in `[a, b]` and
> `r ≥ 0`. There is an immersion `j : Z ⟶ X` of algebraic spaces, of finite presentation, such that
> (1) `H^a(Lj^*E)` is finite locally free of rank `r`, (2) a morphism `f : Y ⟶ X` factors through
> `j` exactly when `H^a(L(f ∘ g)^*E)` is finite locally free of rank `r` for every `g : Y' ⟶ Y`,
> (3) for `f = j ∘ g` we have `H^a(Lf^*E) ≅ g^*H^a(Lj^*E)`, and (4) if `β_a(p) ≤ r` at every
> geometric point `p` of `X` (`bettiAt`, the dimension of `H^a(E ⊗^L k(p))`), then `j` is a closed
> immersion, `f` factors through `j` exactly when `H^a(Lf^*E)` is finite locally free of rank `r`,
> and, for `r = 1`, exactly when `𝒪_Y → ℋom(H^a(Lf^*E), H^a(Lf^*E))` is injective.
>
> The source writes `H^0` in (4)(b) and (4)(c); for `a ≠ 0` that reading is false: for
> `E = 𝒪_X[-a]` and `r = 1` the stratum is all of `X`, so every `f : Y ⟶ X` factors through it, while
> `H^0(Lf^*E) = 0` is not locally free of rank `1` when `Y` is nonempty. The statement here uses
> `H^a`, as in the corrected scheme version [stacks 0BDL].

```lean
theorem exists_isBottomRankStratum_isFinitePresentation
    (T : DerivedTensorProduct (smallEtaleRingedSite B S hS X.1 X.2))
    (hE : RingedSite.IsPerfect (smallEtaleRingedSite B S hS X.1 X.2) E) (b : ℤ)
    (hT : DerivedTensorProduct.HasTorAmplitude T E a b) (r : ℕ) :
    ∃ (Z : AlgebraicSpaces B S hS) (j : Z ⟶ X),
      IsBottomRankStratum E a r j ∧ IsFinitePresentation B S hS j.hom ∧
        (∀ (Y : AlgebraicSpaces B S hS) (g : Y ⟶ Z),
          Nonempty (pullbackHomology E a (g ≫ j) ≅ (pb g).obj (pullbackHomology E a j))) ∧
        ((∀ p : GeometricPoint B S hS X.1, bettiAt E a p.val.siteObject p.val.value ≤ r) →
          IsClosedImmersion B S hS j.hom ∧ (∀ (Y : AlgebraicSpaces B S hS) (f : Y ⟶ X),
            ((∃ g : Y ⟶ Z, g ≫ j = f) ↔
              SheafOfModules.IsFiniteLocallyFreeOfIntRank (pullbackHomology E a f) (r : ℤ))) ∧
          (r = 1 → ∀ (Y : AlgebraicSpaces B S hS) (f : Y ⟶ X),
            ((∃ g : Y ⟶ Z, g ≫ j = f) ↔
              AlgebraicGeometry.SheafOfModules.IsScalarFaithful (pullbackHomology E a f))))
```

## Tag 0E6B, a lemma

[Tag 0E6B](https://stacks.math.columbia.edu/tag/0E6B) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_presieve_isPerfect_hasTorAmplitudeGE_iso_etaleRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperFlatDerivedPushforwardFibreSurjective.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperFlatDerivedPushforwardFibreSurjective.lean#L457). The attribute's comment: “(b)”.

> **Stacks 0E6B, part (b).** Let `f : X ⟶ Y` be proper, flat and of finite presentation, such
> that `k = H⁰(X_k, 𝒪_{X_k})` for every morphism `Spec k ⟶ Y` from the spectrum of a field. Then
> étale locally on `Y` we have `Rf_*𝒪_X ≅ 𝒪_Y ⊕ P` in `D(𝒪_Y)` with `P` perfect of Tor amplitude in
> `[1, ∞)`: every étale chart `U` of `Y` has a covering family of charts `V` over which the
> restrictions satisfy `(Rf_*𝒪_X)|_V ≅ 𝒪_Y|_V ⊕ P`.

```lean
theorem exists_presieve_isPerfect_hasTorAmplitudeGE_iso_etaleRestrict (f : X ⟶ Y)
    (hf : IsProper B S hS f.hom) (hfl : IsFlat B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom)
    (h : ∀ p : FieldValuedPoint B S hS Y.1, Function.Bijective (algebraMap p.carrier
      (globalFunctions B (Spec (.of p.carrier)) p.contained
        (fibreOverFieldValuedPoint B S hS f.hom p))))
    (U : SmallEtale B S hS Y.1) :
    ∃ R : Presieve U, Sieve.generate R ∈ SmallEtale.topology B S hS Y.1 U ∧
      ∀ ⦃V : SmallEtale B S hS Y.1⦄ (g : V ⟶ U), R g →
        ∃ P : DerivedCategory (Modules.{u, u} B S hS (chartSpace B S hS Y V).1
            (chartSpace B S hS Y V).2),
          (smallEtaleRingedSite B S hS (chartSpace B S hS Y V).1
            (chartSpace B S hS Y V).2).IsPerfect P ∧
          Stacks.SheafOfModules.DerivedTensorProduct.HasTorAmplitudeGE
            (smallEtaleDerivedTensorProduct B S hS (chartSpace B S hS Y V)) P 1 ∧
          Nonempty ((etaleModulePullback.{u, u} B S hS (chartToSpace B S hS Y V)
              (isEtale_chartToSpace B S hS Y V)).mapDerivedCategory.obj
              ((derivedModulePushforward B S hS f).obj
                ((DerivedCategory.singleFunctor _ 0).obj (structureModule X))) ≅
            (etaleModulePullback.{u, u} B S hS (chartToSpace B S hS Y V)
              (isEtale_chartToSpace B S hS Y V)).mapDerivedCategory.obj
              ((DerivedCategory.singleFunctor _ 0).obj (structureModule Y)) ⊞ P)
```

**`AlgebraicGeometry.Space.isIso_structureSharp_and_baseChange_of_bijective_algebraMap_fibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperFlatStructureSheafPushforward.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperFlatStructureSheafPushforward.lean#L73). The attribute's comment: “(a)”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces which is proper, flat and of finite
> presentation, such that `k = H⁰(X_k, 𝒪_{X_k})` for every morphism `Spec k ⟶ Y` with `k` a field.
> Then `f_*𝒪_X = 𝒪_Y` — the structure map `𝒪_Y ⟶ f_*𝒪_X` is an isomorphism — and this holds after
> any base change `Y' ⟶ Y`.

```lean
theorem isIso_structureSharp_and_baseChange_of_bijective_algebraMap_fibre (f : X ⟶ Y)
    (hf : IsProper B S hS f.hom) (hfl : IsFlat B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom)
    (h : ∀ p : FieldValuedPoint B S hS Y.1, Function.Bijective (algebraMap p.carrier
      (globalFunctions B (Spec (.of p.carrier)) p.contained
        (fibreOverFieldValuedPoint B S hS f.hom p)))) :
    IsIso (structureSharp B S hS f) ∧
      ∀ (Y' : AlgebraicSpaces B S hS) (g : Y' ⟶ Y),
        IsIso (structureSharp B S hS (pullback.snd f g))
```

## Tag 0E0S, a lemma

[Tag 0E0S](https://stacks.math.columbia.edu/tag/0E0S) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_structureSharp_and_baseChange_of_geometricFibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperFlatStructureSheafPushforward.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperFlatStructureSheafPushforward.lean#L103).

> Let `f : X ⟶ Y` be a morphism of algebraic spaces which is proper, flat and of finite
> presentation, and whose geometric fibres are reduced and connected. Then `f_*𝒪_X = 𝒪_Y` — the
> structure map `𝒪_Y ⟶ f_*𝒪_X` is an isomorphism — and this holds after any base change
> `Y' ⟶ Y`.

```lean
theorem isIso_structureSharp_and_baseChange_of_geometricFibres (f : X ⟶ Y)
    (hf : IsProper B S hS f.hom) (hfl : IsFlat B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom)
    (hred : ∀ y : GeometricPoint B S hS Y.1,
      HasEtaleLocalProperty B (Spec (.of y.1.carrier)) y.1.contained
        (fibreOverFieldValuedPoint B S hS f.hom y.1)
        (fun T : Scheme.{u} => _root_.AlgebraicGeometry.IsReduced T))
    (hconn : ∀ y : GeometricPoint B S hS Y.1,
      ConnectedPoints B (Spec (.of y.1.carrier)) y.1.contained
        (fibreOverFieldValuedPoint B S hS f.hom y.1)) :
    IsIso (structureSharp B S hS f) ∧
      ∀ (Y' : AlgebraicSpaces B S hS) (g : Y' ⟶ Y),
        IsIso (structureSharp B S hS (pullback.snd f g))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.26, Tag 0D1X](https://stacks.math.columbia.edu/tag/0D1X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: section
origin: cited
lean: Stacks.Duality.preservesColimitsOfShape_rightAdjoint_quasiCoherentDerivedPushforward, Stacks.Duality.preservesColimitsOfShape_twistedInverseImage, Stacks.Duality.preservesCoproducts_twistedInverseImage_of_perfect_proper, Stacks.Duality.isIso_twistedInverseImageRestrictionMap_app_of_perfect, Stacks.Duality.isIso_qcqsTwistedInverseImageRestrictionMap_app_of_perfect, Stacks.Duality.isZero_derivedRestrict_twistedInverseImage_of_perfect, Stacks.Duality.isIso_twistedInverseImageCompareWithPullback_of_perfect_of_isProper, Stacks.Duality.isIso_compareWithPullback_twistedInverseImage
statement: formalized
proof: formalized
---

# 48.13 Right adjoint of pushforward for perfect proper morphisms

Section 48.13 of the Stacks Project, [Tag 0AA9](https://stacks.math.columbia.edu/tag/0AA9). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A9R, a lemma

[Tag 0A9R](https://stacks.math.columbia.edu/tag/0A9R) in the Stacks Project.

**`Stacks.Duality.preservesColimitsOfShape_rightAdjoint_quasiCoherentDerivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSumsPerfectProper.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSumsPerfectProper.lean#L111).

> Let `f : X ⟶ Y` be a perfect proper morphism of Noetherian schemes and let `a` be a right
> adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`. Then `a` commutes with direct sums.

```lean
theorem preservesColimitsOfShape_rightAdjoint_quasiCoherentDerivedPushforward [IsNoetherian X]
    [IsNoetherian Y] [Perfect f] [IsProper f]
    {a : quasiCoherentDerivedCategory Y ⥤ quasiCoherentDerivedCategory X}
    (adj : quasiCoherentDerivedPushforward f
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f) ⊣ a) (J : Type u) :
    PreservesColimitsOfShape (Discrete J) a
```

**`Stacks.Duality.preservesColimitsOfShape_twistedInverseImage`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSumsPerfectProper.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSumsPerfectProper.lean#L123).

> For a perfect proper morphism of Noetherian schemes `f : X ⟶ Y`, the twisted inverse image
> `f^× : D_QCoh(𝒪_Y) ⥤ D_QCoh(𝒪_X)`, the right adjoint `twistedInverseImage f` of `Rf_*`, commutes
> with direct sums.

```lean
instance preservesColimitsOfShape_twistedInverseImage [IsNoetherian X] [IsNoetherian Y]
    [Perfect f] [IsProper f] (J : Type u) :
    PreservesColimitsOfShape (Discrete J)
      (twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f))
```

**`Stacks.Duality.preservesCoproducts_twistedInverseImage_of_perfect_proper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSumsUnconditional.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSumsUnconditional.lean#L73). The attribute's comment: “a = f^× commutes with direct sums indexed by every type J in the universe of X and Y, the universe of the hom-sets of D\_QCoh”.

> **[Stacks, Tag 0A9R].** Let `f : X ⟶ Y` be a perfect proper morphism of Noetherian schemes.
> The twisted inverse image `a = f^×`, the right adjoint of
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` ([Stacks, Tag 0A9E]), commutes with direct sums: it
> preserves coproducts indexed by every `J : Type u`, the universe of the schemes, which is the
> universe of the hom-sets of `D_QCoh` and the one at which it has all direct sums.

```lean
theorem preservesCoproducts_twistedInverseImage_of_perfect_proper (J : Type u) :
    PreservesColimitsOfShape (Discrete J)
      (twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f))
```

## Tag 0AAA, a lemma

[Tag 0AAA](https://stacks.math.columbia.edu/tag/0AAA) in the Stacks Project.

**`Stacks.Duality.isIso_twistedInverseImageRestrictionMap_app_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperPerfectSupport.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperPerfectSupport.lean#L69). The attribute's comment: “(2) variant: for a supplied cartesian square with open immersion `j`; the tag is `isIso_qcqsTwistedInverseImageRestrictionMap_app_of_perfect`”.

> **[Stacks, Tag 0AAA] (2), for a supplied cartesian square.** Let `f : X ⟶ Y` be a perfect
> proper morphism of Noetherian schemes and `j : V ⟶ Y` an open immersion, with base change
> `j' : U ⟶ X` and `f' : U ⟶ V`. The map `(j')^* ∘ a ⟶ a' ∘ j^*` of [Stacks, Tag 0A9L] is an
> isomorphism at every `K ∈ D_QCoh(𝒪_Y)`. The invertibility of `ξ : Rj'_* ∘ a' ⟶ a ∘ Rj_*` that
> the map contains is the open-immersion case of [Stacks, Tag 0A9K],
> `Stacks.Duality.isIso_twistedInverseImagePushforwardBaseChange_of_isOpenImmersion`. The tag, for
> every open `V ⊆ Y`, is `Stacks.Duality.isIso_qcqsTwistedInverseImageRestrictionMap_app_of_perfect`.

```lean
theorem isIso_twistedInverseImageRestrictionMap_app_of_perfect (sq : IsPullback j' f' f j)
    (K : quasiCoherentDerivedCategory Y) :
    haveI : IsOpenImmersion j' := MorphismProperty.of_isPullback sq.flip inferInstance
    haveI : IsProper f' := MorphismProperty.of_isPullback sq inferInstance
    haveI := isNoetherian_of_isOpenImmersion j
    haveI := isNoetherian_of_isProper f'
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_isOpenImmersion j' f' f j
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j) sq
    IsIso ((twistedInverseImageRestrictionMap j' f' f j
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j)
      (isQuasicoherent_homology_derivedRestrict j) (isQuasicoherent_homology_derivedRestrict j')
      sq).app K)
```

**`Stacks.Duality.isIso_qcqsTwistedInverseImageRestrictionMap_app_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperPerfectSupport.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperPerfectSupport.lean#L101). The attribute's comment: “(2)”.

> **[Stacks, Tag 0AAA] (2).** Let `f : X ⟶ Y` be a perfect proper morphism of Noetherian
> schemes and `V ⊆ Y` an open, with `U = f⁻¹(V)`. The map `(j')^* ∘ a ⟶ a' ∘ j^*` of
> [Stacks, Tag 0A9L], `Stacks.Duality.OpenImmersion.qcqsTwistedInverseImageRestrictionMap`, is an
> isomorphism at every `K ∈ D_QCoh(𝒪_Y)`. The schemes `X`, `Y` are quasi-compact and
> quasi-separated and `V` is quasi-compact because they are Noetherian.

```lean
theorem isIso_qcqsTwistedInverseImageRestrictionMap_app_of_perfect (V : Y.Opens)
    (K : quasiCoherentDerivedCategory Y) :
    haveI := isNoetherian_of_isOpenImmersion V.ι
    IsIso ((qcqsTwistedInverseImageRestrictionMap f V).app K)
```

**`Stacks.Duality.isZero_derivedRestrict_twistedInverseImage_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperPerfectSupport.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperPerfectSupport.lean#L149). The attribute's comment: “(1)”.

> **[Stacks, Tag 0AAA] (1).** Let `f : X ⟶ Y` be a perfect proper morphism of Noetherian
> schemes, with `a` the right adjoint of `Rf_*` on `D_QCoh`. For every closed `T ⊆ Y`, if
> `Q ∈ D_QCoh(𝒪_Y)` is supported on `T` then `a(Q)` is supported on `f⁻¹(T)`. Here `T` is the
> complement of the open `W`, and "supported on `T`" is "restricts to zero on `W`". The functor `a`
> exists by [Stacks, Tag 0A9E],
> `Stacks.Duality.DerivedPushforward.isLeftAdjoint_quasiCoherentDerivedPushforward_of_qcqs`.

```lean
theorem isZero_derivedRestrict_twistedInverseImage_of_perfect (W : Y.Opens)
    (Q : quasiCoherentDerivedCategory Y) (hQ : IsZero ((derivedRestrict W.ι).obj Q.obj)) :
    haveI := DerivedPushforward.isLeftAdjoint_quasiCoherentDerivedPushforward_of_qcqs f
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
    IsZero ((derivedRestrict (f ⁻¹ᵁ W).ι).obj
      ((twistedInverseImage f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj Q).obj)
```

## Tag 0A9U, a lemma

[Tag 0A9U](https://stacks.math.columbia.edu/tag/0A9U) in the Stacks Project.

**`Stacks.Duality.isIso_twistedInverseImageCompareWithPullback_of_perfect_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonPerfectProper.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonPerfectProper.lean#L62).

> **Stacks Project, Tag 0A9U (Lemma 48.13.3).** Let `f : X ⟶ Y` be a perfect proper morphism of
> Noetherian schemes. The map `Lf^*K ⊗ᴸ_{𝒪_X} a(𝒪_Y) ⟶ a(K)` of [Stacks, Tag 0A9S] is an
> isomorphism for every object `K` of `D_QCoh(𝒪_Y)`.

```lean
theorem isIso_twistedInverseImageCompareWithPullback_of_perfect_of_isProper
    (K : quasiCoherentDerivedCategory Y) :
    IsIso (twistedInverseImageCompareWithPullback f
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (quasiCoherentDerivedPullbackTensorIso f).hom
      (quasiCoherentDerivedTensorRightUnitor Y) K)
```

**`Stacks.Duality.isIso_compareWithPullback_twistedInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonUnconditional.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonUnconditional.lean#L204). The attribute's comment: “complete: X, Y Noetherian, f perfect and proper, every K in D\_QCoh(𝒪\_Y)”.

> Let `f : X ⟶ Y` be a perfect proper morphism of Noetherian schemes and
> let `a = f^×` be the right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` ([Stacks, Tag 0A9E]).
> The map `Lf^*K ⊗ᴸ_{𝒪_X} a(𝒪_Y) ⟶ a(K)` of Equation 48.8.0.1 ([Stacks, Tag 0A9S]) is an
> isomorphism for every object `K` of `D_QCoh(𝒪_Y)`.
>
> The same holds at any right adjoint of `Rf_*`, by
> `Stacks.Duality.isIso_compareWithPullback_of_perfect_of_isProper`.

```lean
theorem isIso_compareWithPullback_twistedInverseImage [IsNoetherian X] [IsNoetherian Y]
    [IsProper f] [AlgebraicGeometry.Perfect f] (K : quasiCoherentDerivedCategory Y) :
    IsIso (compareWithPullback f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (pullbackCotensorator f)
      (twistedInverseImageAdjunction f (isQuasicoherent_homology_derivedPushforward_of_qcqs f))
      quasiCoherentRightUnitor K)
```

## Tag 0BZG, a lemma

[Tag 0BZG](https://stacks.math.columbia.edu/tag/0BZG) in the Stacks Project.

**`Stacks.Duality.isIso_torIndependentTwistedInverseImageBaseChange_app_of_perfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/PerfectBaseChange.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/PerfectBaseChange.lean#L157).

> **[Stacks, Tag 0BZG].** Let `f : X ⟶ Y` be a perfect proper morphism of Noetherian schemes and
> `g : Y' ⟶ Y` a morphism with `Y'` Noetherian, and let `X' = X ×_Y Y'`, with projections
> `g' : X' ⟶ X` and `f' : X' ⟶ Y'`. If `X` and `Y'` are Tor independent over `Y`, then the base
> change map `L(g')^* a(K) ⟶ a'(Lg^*K)` of [Stacks, Tag 0AA6] is an isomorphism for every
> `K ∈ D_QCoh(𝒪_Y)`, where `a` and `a'` are the right adjoints of `Rf_*` and `Rf'_*` on `D_QCoh`
> ([Stacks, Tag 0A9E]).

```lean
theorem isIso_torIndependentTwistedInverseImageBaseChange_app_of_perfect {X' X Y' Y : Scheme.{u}}
    [IsNoetherian X] [IsNoetherian Y] [IsNoetherian Y'] {g' : X' ⟶ X} {f' : X' ⟶ Y'}
    {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g) [IsProper f]
    [AlgebraicGeometry.Perfect f] (hTor : TorIndependent f g)
    (K : quasiCoherentDerivedCategory Y) :
    haveI : QuasiCompact f' := MorphismProperty.of_isPullback sq inferInstance
    haveI : QuasiSeparated f' := MorphismProperty.of_isPullback sq inferInstance
    haveI : CompactSpace X' := QuasiCompact.compactSpace_of_compactSpace f'
    haveI : QuasiSeparatedSpace X' := quasiSeparatedSpace_of_quasiSeparated f'
    IsIso ((torIndependentTwistedInverseImageBaseChange sq hTor).app K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.13, Tag 0AA9](https://stacks.math.columbia.edu/tag/0AA9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

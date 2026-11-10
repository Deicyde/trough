---
declaration: section
origin: cited
lean: Stacks.Duality.preservesColimitsOfShape_rightAdjoint_quasiCoherentDerivedPushforward_of_flat, Stacks.Duality.isIso_twistedInverseImageRestrictionMap_app_of_flat_of_unbounded, Stacks.Duality.isZero_derivedRestrict_twistedInverseImage_of_flat, Stacks.Duality.isIso_twistedInverseImageCompareWithPullback_of_flat, Stacks.Duality.isIso_twistedInverseImageBaseChangeMap_app_of_isProper_of_flat, Stacks.Duality.relativeDualizingComplexStructureSheaf, Stacks.Duality.relativeDualizingTraceStructureSheaf, Stacks.Duality.relativeDualizingTensorIso
statement: formalized
proof: formalized
---

# 48.12 Right adjoint of pushforward for proper flat morphisms

Section 48.12 of the Stacks Project, [Tag 0E4H](https://stacks.math.columbia.edu/tag/0E4H). 11 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0E4I, a lemma

[Tag 0E4I](https://stacks.math.columbia.edu/tag/0E4I) in the Stacks Project.

**`Stacks.Duality.preservesColimitsOfShape_rightAdjoint_quasiCoherentDerivedPushforward_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSumsFlat.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/RightAdjointDirectSumsFlat.lean#L52).

> Let `Y` be a quasi-compact and quasi-separated scheme, let `f : X ⟶ Y` be proper, flat and of
> finite presentation, and let `a` be a right adjoint of `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`. Then
> `a` commutes with direct sums.

```lean
theorem preservesColimitsOfShape_rightAdjoint_quasiCoherentDerivedPushforward_of_flat
    {a : quasiCoherentDerivedCategory Y ⥤ quasiCoherentDerivedCategory X}
    (adj : quasiCoherentDerivedPushforward f
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f) ⊣ a) (J : Type u) :
    PreservesColimitsOfShape (Discrete J) a
```

## Tag 0E4J, a lemma

[Tag 0E4J](https://stacks.math.columbia.edu/tag/0E4J) in the Stacks Project.

**`Stacks.Duality.isIso_twistedInverseImageRestrictionMap_app_of_flat_of_unbounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperFlatSupport.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperFlatSupport.lean#L44). The attribute's comment: “(2)”.

> Let `Y` be a quasi-compact and quasi-separated scheme, `f : X ⟶ Y` proper, flat and of finite
> presentation, and `j : V ⟶ Y` the inclusion of a quasi-compact open, with base change
> `j' : U ⟶ X`. The map `(j')^* ∘ a ⟶ a' ∘ j^*` of [Stacks, Tag 0A9L] is an isomorphism at every
> `K ∈ D_QCoh(𝒪_Y)`.

```lean
theorem isIso_twistedInverseImageRestrictionMap_app_of_flat_of_unbounded
    (sq : IsPullback j' f' f j) (K : quasiCoherentDerivedCategory Y) :
    haveI : IsOpenImmersion j' := MorphismProperty.of_isPullback sq.flip inferInstance
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : CompactSpace V := QuasiCompact.compactSpace_of_compactSpace j
    haveI : CompactSpace U := compactSpace_of_isPullback sq
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    haveI : QuasiSeparatedSpace V := j.isOpenEmbedding.quasiSeparatedSpace
    haveI : QuasiSeparatedSpace U := j'.isOpenEmbedding.quasiSeparatedSpace
    IsIso ((twistedInverseImageRestrictionMap j' f' f j
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs j)
      (isQuasicoherent_homology_derivedRestrict j) (isQuasicoherent_homology_derivedRestrict j')
      sq).app K)
```

**`Stacks.Duality.isZero_derivedRestrict_twistedInverseImage_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperFlatSupport.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/ProperFlatSupport.lean#L128). The attribute's comment: “(1)”.

> Let `Y` be a quasi-compact and quasi-separated scheme and `f : X ⟶ Y` proper, flat and of
> finite presentation, with `a` the right adjoint of `Rf_*` on `D_QCoh`. For every closed `T ⊆ Y`,
> if `Q ∈ D_QCoh(𝒪_Y)` is supported on `T` then `a(Q)` is supported on `f⁻¹(T)`. Here `T` is the
> complement of the open `W`, and "supported on `T`" is "restricts to zero on `W`".

```lean
theorem isZero_derivedRestrict_twistedInverseImage_of_flat (W : Y.Opens)
    (Q : quasiCoherentDerivedCategory Y) (hQ : IsZero ((derivedRestrict W.ι).obj Q.obj)) :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    IsZero ((derivedRestrict (f ⁻¹ᵁ W).ι).obj
      ((twistedInverseImage f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj Q).obj)
```

## Tag 0E4K, a lemma

[Tag 0E4K](https://stacks.math.columbia.edu/tag/0E4K) in the Stacks Project.

**`Stacks.Duality.isIso_twistedInverseImageCompareWithPullback_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonFlat.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonFlat.lean#L164).

> **[Stacks, Tag 0E4K].** Let `Y` be a quasi-compact and quasi-separated scheme and
> `f : X ⟶ Y` proper, flat and of finite presentation. The map `Lf^*K ⊗ᴸ a(𝒪_Y) ⟶ a(K)` of
> Equation 48.8.0.1 is an isomorphism for every `K ∈ D_QCoh(𝒪_Y)`.

```lean
theorem isIso_twistedInverseImageCompareWithPullback_of_flat (K : quasiCoherentDerivedCategory Y) :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    IsIso (twistedInverseImageCompareWithPullback f
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (quasiCoherentDerivedPullbackTensorIso f).hom
      (quasiCoherentDerivedTensorRightUnitor Y) K)
```

## Tag 0AAB, a lemma

[Tag 0AAB](https://stacks.math.columbia.edu/tag/0AAB) in the Stacks Project.

**`Stacks.Duality.isIso_twistedInverseImageBaseChangeMap_app_of_isProper_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/AffineBaseChangeLocal.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/AffineBaseChangeLocal.lean#L426).

> **[Stacks, Tag 0AAB].** Let `g : Y' ⟶ Y` be a morphism of quasi-compact and quasi-separated
> schemes and `f : X ⟶ Y` proper, flat and of finite presentation, with base change
> `f' : X' ⟶ Y'`. Then the base change map `L(g')^* a(K) ⟶ a'(Lg^*K)` of [Stacks, Tag 0AA6] is an
> isomorphism for every `K ∈ D_QCoh(𝒪_Y)`.

```lean
theorem isIso_twistedInverseImageBaseChangeMap_app_of_isProper_of_flat {X' X Y' Y : Scheme.{u}}
    [CompactSpace Y'] [QuasiSeparatedSpace Y'] [CompactSpace Y] [QuasiSeparatedSpace Y]
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback g' f' f g)
    [IsProper f] [Flat f] [LocallyOfFinitePresentation f] (K : quasiCoherentDerivedCategory Y) :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    haveI : QuasiCompact f' := MorphismProperty.of_isPullback sq inferInstance
    haveI : QuasiSeparated f' := MorphismProperty.of_isPullback sq inferInstance
    haveI : CompactSpace X' := QuasiCompact.compactSpace_of_compactSpace f'
    haveI : QuasiSeparatedSpace X' := quasiSeparatedSpace_of_quasiSeparated f'
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_torIndependent sq
      (torIndependent_of_flat_left f g)
    IsIso ((twistedInverseImageBaseChangeMap g' f' f g
      (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
      (isQuasicoherent_homology_derivedPushforward_of_qcqs g)
      sq).app K)
```

## Tag 0B6S, a remark

[Tag 0B6S](https://stacks.math.columbia.edu/tag/0B6S) in the Stacks Project.

**`Stacks.Duality.relativeDualizingComplexStructureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/RelativeDualizingComplexStructureSheaf.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/RelativeDualizingComplexStructureSheaf.lean#L104). The attribute's comment: “the relative dualizing complex omega^bullet_{X/Y} = a(O_Y) that the Remark names, the right adjoint of Tag 0A9E applied to the structure sheaf; defined for every quasi-compact quasi-separated morphism to a quasi-compact scheme, so in particular under the Remark's hypotheses”.

> **The relative dualizing complex `ω_{X/Y}^• = a(𝒪_Y)`** of [Stacks, Tag 0B6S], for `a = f^×`
> the right adjoint of [Stacks, Tag 0A9E]: the twisted inverse image of the structure sheaf of the
> base, placed in degree zero.
>
> Over `Y = Spec k` for a field `k` this is `Stacks.Duality.dualizingComplexOverField`, the
> dualizing complex of [Stacks, Tag 0BS2].

```lean
def relativeDualizingComplexStructureSheaf : quasiCoherentDerivedCategory X
```

**`Stacks.Duality.relativeDualizingTraceStructureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/RelativeDualizingComplexStructureSheaf.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedPushforward/RelativeDualizingComplexStructureSheaf.lean#L116). The attribute's comment: “the trace map Tr_{f,O_Y} : Rf_* omega^bullet_{X/Y} to O_Y that the Remark displays, the counit of the adjunction of Tag 0A9E at the structure sheaf of the base”.

> **The trace map `Tr_{f, 𝒪_Y} : Rf_* ω_{X/Y}^• ⟶ 𝒪_Y`** of [Stacks, Tag 0AWG], displayed in
> [Stacks, Tag 0B6S]: the counit of `Rf_* ⊣ f^×` at the structure sheaf of the base.
>
> That it induces the trace map `Tr_{f, K}` for every `K` in `D_QCoh(𝒪_Y)` — the commuting square
> of the Remark — is `Stacks.Duality.map_relativeDualizingTensorIso_hom_app_comp_trace`.

```lean
def relativeDualizingTraceStructureSheaf :
    (quasiCoherentDerivedPushforward f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
      (relativeDualizingComplexStructureSheaf f) ⟶
    Stacks.Duality.DerivedPushforward.derivedStructureSheaf Y
```

**`Stacks.Duality.relativeDualizingTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexTensorDescription.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexTensorDescription.lean#L142). The attribute's comment: “the functorial isomorphism a(K) = Lf^*K ⊗^L omega^bullet_{X/Y} for K in D_QCoh(O_Y), omega^bullet_{X/Y} = a(O_Y), for Y quasi-compact quasi-separated and f proper flat of finite presentation: an isomorphism of functors whose components are the map of Equation 48.8.0.1, invertible by Tag 0E4K”.

> **The functorial isomorphism `a(K) = Lf^*K ⊗ᴸ ω^•_{X/Y}` of [Stacks, Tag 0B6S]**, for
> `Y` quasi-compact and quasi-separated and `f : X ⟶ Y` proper, flat and of finite presentation:
> an isomorphism of functors `D_QCoh(𝒪_Y) ⥤ D_QCoh(𝒪_X)` from `K ↦ Lf^*K ⊗ᴸ_{𝒪_X} ω^•_{X/Y}`, where
> `ω^•_{X/Y} = a(𝒪_Y)` is the relative dualizing complex, to the right adjoint `a` of
> [Stacks, Tag 0A9E]. Its components are the map of Equation 48.8.0.1 ([Stacks, Tag 0A9S]), which
> is invertible by [Stacks, Tag 0E4K].

```lean
def relativeDualizingTensorIso :
    quasiCoherentDerivedPullback' f ⋙ (quasiCoherentDerivedTensor X).flip.obj
        ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
          (derivedStructureSheaf Y)) ≅
      twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
```

**`Stacks.Duality.map_relativeDualizingTensorIso_hom_app_comp_trace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexTensorDescription.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexTensorDescription.lean#L175). The attribute's comment: “the trace compatibility: Tr_{f,K} composed with Rf_* of the isomorphism a(K) = Lf^*K ⊗^L omega^bullet_{X/Y} is the projection formula of Tag 08EU followed by id_K ⊗ Tr_{f,O_Y} and K ⊗^L O_Y = K, the Remark's commuting square, for Y quasi-compact quasi-separated and f proper flat of finite presentation”.

> **The trace map `Tr_{f, 𝒪_Y}` induces the trace map `Tr_{f, K}` for every `K`**, the
> commuting square of [Stacks, Tag 0B6S]: `Rf_*` of the isomorphism
> `Lf^*K ⊗ᴸ ω^•_{X/Y} ≅ a(K)` followed by the trace `Tr_{f, K} : Rf_* a(K) ⟶ K` of
> [Stacks, Tag 0AWG] is the projection formula `Rf_*(Lf^*K ⊗ᴸ ω^•_{X/Y}) ≅ K ⊗ᴸ Rf_* ω^•_{X/Y}` of
> [Stacks, Tag 08EU], followed by `id_K ⊗ Tr_{f, 𝒪_Y} : K ⊗ᴸ Rf_* ω^•_{X/Y} ⟶ K ⊗ᴸ 𝒪_Y` and the
> identification `K ⊗ᴸ 𝒪_Y = K`.

```lean
theorem map_relativeDualizingTensorIso_hom_app_comp_trace (K : quasiCoherentDerivedCategory Y) :
    (quasiCoherentDerivedPushforward f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).map
        ((relativeDualizingTensorIso f).hom.app K) ≫
      (twistedInverseImageAdjunction f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).counit.app K =
    (relativeDualizingProjectionFormulaIso f K).inv ≫
      ((quasiCoherentDerivedTensor Y).obj K).map (relativeDualizingTraceStructureSheaf f) ≫
      quasiCoherentRightUnitor.hom.app K
```

**`Stacks.Duality.relativeDualizingBaseChangeIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexTensorDescription.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexTensorDescription.lean#L257). The attribute's comment: “the base change of the relative dualizing complex in the Remark's last sentence: for g : Y' to Y a morphism of quasi-compact quasi-separated schemes and X' = Y' x_Y X, the base change map L(g')^* a(O_Y) to a'(Lg^* O_Y) of Tag 0AA6 is an isomorphism (Tag 0AAB), so omega^bullet_{X'/Y'} = L(g')^* omega^bullet_{X/Y} through it and a'(Lg^* O_Y = O_{Y'})”.

> **`ω^•_{X'/Y'} = L(g')^* ω^•_{X/Y}`**, the first assertion of the last sentence of
> [Stacks, Tag 0B6S]: the base change map of [Stacks, Tag 0AA6] at `𝒪_Y` is an isomorphism
> ([Stacks, Tag 0AAB]), and composed with `a'(Lg^*𝒪_Y ≅ 𝒪_{Y'})` it is the isomorphism
> `relativeDualizingBaseChangeIso`.

```lean
theorem relativeDualizingBaseChangeIso_hom :
    haveI := quasiCompact_of_isPullback_relativeDualizing f sq
    haveI := quasiSeparated_of_isPullback_relativeDualizing f sq
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    haveI : CompactSpace X' := QuasiCompact.compactSpace_of_compactSpace f'
    haveI : QuasiSeparatedSpace X' := quasiSeparatedSpace_of_quasiSeparated f'
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_torIndependent sq
      (torIndependent_of_flat_left f g)
    IsIso ((twistedInverseImageBaseChangeMap g' f' f g
        (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
        (isQuasicoherent_homology_derivedPushforward_of_qcqs g) sq).app
          (derivedStructureSheaf Y)) ∧
      (relativeDualizingBaseChangeIso f sq).hom =
        (twistedInverseImageBaseChangeMap g' f' f g
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g) sq).app
            (derivedStructureSheaf Y) ≫
          (twistedInverseImage f' (isQuasicoherent_homology_derivedPushforward_of_qcqs f')).map
            (quasiCoherentDerivedPullbackDerivedStructureSheafIsoOfIsQuasicoherent g
        (isQuasicoherent_homology_derivedPullback' g)).hom
```

**`Stacks.Duality.map_trace_comp_eq_baseChange_comp_trace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexTensorDescription.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexTensorDescription.lean#L294). The attribute's comment: “the base change of the trace in the Remark's last sentence: Tr_{f',O_{Y'}} is the base change of Tr_{f,O_Y} via the base change isomorphism, i.e. Lg^* Tr_{f,O_Y} followed by Lg^* O_Y = O_{Y'} equals the base change map of Rf_* at omega^bullet_{X/Y} followed by Rf'_* of L(g')^* omega^bullet_{X/Y} = omega^bullet_{X'/Y'} and Tr_{f',O_{Y'}} (Tag 0B6J)”.

> **The trace map of `f'` is the base change of the trace map of `f`**, the second assertion of
> the last sentence of [Stacks, Tag 0B6S], by [Stacks, Tag 0B6J]: `Lg^*` of
> `Tr_{f, 𝒪_Y} : Rf_* ω^•_{X/Y} ⟶ 𝒪_Y`, followed by `Lg^*𝒪_Y ≅ 𝒪_{Y'}`, is the base change map
> `β : Lg^* Rf_* ⟶ Rf'_* L(g')^*` at `ω^•_{X/Y}` (invertible, [Stacks, Tag 08IB]), followed by
> `Rf'_*` of the base change isomorphism `L(g')^* ω^•_{X/Y} ≅ ω^•_{X'/Y'}` and
> `Tr_{f', 𝒪_{Y'}} : Rf'_* ω^•_{X'/Y'} ⟶ 𝒪_{Y'}`.

```lean
theorem map_trace_comp_eq_baseChange_comp_trace :
    haveI := quasiCompact_of_isPullback_relativeDualizing f sq
    haveI := quasiSeparated_of_isPullback_relativeDualizing f sq
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    haveI : CompactSpace X' := QuasiCompact.compactSpace_of_compactSpace f'
    haveI : QuasiSeparatedSpace X' := quasiSeparatedSpace_of_quasiSeparated f'
    IsIso (quasiCoherentDerivedBaseChange g' f' f g
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g)
          (isQuasicoherent_homology_derivedPullback' g)
          (isQuasicoherent_homology_derivedPullback' g') sq.w).natTrans ∧
    (quasiCoherentDerivedPullback' g).map
        ((twistedInverseImageAdjunction f
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).counit.app
          (derivedStructureSheaf Y)) ≫
      (quasiCoherentDerivedPullbackDerivedStructureSheafIsoOfIsQuasicoherent g
        (isQuasicoherent_homology_derivedPullback' g)).hom =
    (quasiCoherentDerivedBaseChange g' f' f g
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g)
          (isQuasicoherent_homology_derivedPullback' g)
          (isQuasicoherent_homology_derivedPullback' g') sq.w).natTrans.app
        ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
          (derivedStructureSheaf Y)) ≫
      (quasiCoherentDerivedPushforward f'
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f')).map
        (relativeDualizingBaseChangeIso f sq).hom ≫
      (twistedInverseImageAdjunction f'
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f')).counit.app
        (derivedStructureSheaf Y')
```

## Tag 0G81, a remark

[Tag 0G81](https://stacks.math.columbia.edu/tag/0G81) in the Stacks Project.

**`Stacks.Duality.isIso_homEquiv_symm_relativeCupProduct_comp_trace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingCupProduct.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingCupProduct.lean#L206).

> **Stacks Project, Tag 0G81.** Let `Y` be a quasi-compact quasi-separated scheme and
> `f : X ⟶ Y` a proper, flat morphism of finite presentation; let `a` be the right adjoint of
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` of [Stacks, Tag 0A9E], `ω^•_{X/Y} = a(𝒪_Y)` the relative
> dualizing complex and `Tr_{f, 𝒪_Y} : Rf_*ω^•_{X/Y} ⟶ 𝒪_Y` the trace of [Stacks, Tag 0B6S]. Let
> `K ∈ D(𝒪_X)` and `M ∈ D_QCoh(𝒪_X)` with `M` pseudo-coherent, and let
> `φ : K ⊗^L_{𝒪_X} M ⟶ ω^•_{X/Y}` be a map whose transpose `K ⟶ R𝓗om_{𝒪_X}(M, ω^•_{X/Y})` under
> the tensor–internal-Hom bijection of [Stacks, Tag 08DI] is an isomorphism. Then the map
> `Rf_*K ⟶ R𝓗om_{𝒪_Y}(Rf_*M, 𝒪_Y)` corresponding under that bijection on `Y` to
>
> `Rf_*K ⊗^L_{𝒪_Y} Rf_*M ⟶ Rf_*(K ⊗^L_{𝒪_X} M) ⟶ Rf_*ω^•_{X/Y} ⟶ 𝒪_Y`
>
> (the relative cup product of [Stacks, Tag 0B68], `Rf_*φ` and `Tr_{f, 𝒪_Y}`) is an isomorphism.
>
> The source asks `K` to lie in `D_QCoh(𝒪_X)`; that is not used. The instance arguments
> `CompactSpace X` and `QuasiSeparatedSpace X` restrict nothing: they hold for every proper `f` over
> a quasi-compact quasi-separated `Y` (`AlgebraicGeometry.QuasiCompact.compactSpace_of_compactSpace`
> and `AlgebraicGeometry.quasiSeparatedSpace_of_quasiSeparated`), and are arguments only because
> the right adjoint `a` of [Stacks, Tag 0A9E] at this model is found by instance search from them.

```lean
theorem isIso_homEquiv_symm_relativeCupProduct_comp_trace (K : DerivedCategory X.Modules)
    (M : quasiCoherentDerivedCategory X)
    (hM : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) M.obj)
    (φ : ((derivedTensorProductFunctor X.sheaf).obj K).obj M.obj ⟶
      (relativeDualizingComplex f (StandardModel.isQuasicoherent_homology_derivedPushforward f)
        (derivedStructureSheafInDegree Y 0)).obj)
    (hφ : IsIso (((derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite X.sheaf)).homEquiv
      K M.obj (relativeDualizingComplex f
        (StandardModel.isQuasicoherent_homology_derivedPushforward f)
        (derivedStructureSheafInDegree Y 0)).obj).symm φ)) :
    IsIso (((derivedTensorHomAdjunction (Stacks.SheafOfModules.ringedSite Y.sheaf)).homEquiv
      ((derivedPushforward f).obj K) ((derivedPushforward f).obj M.obj)
      (derivedStructureSheafInDegree Y 0).obj).symm
        (relativeCupProduct f.toLRSHom.toShHom K M.obj ≫ (derivedPushforward f).map φ ≫
          (ι _).map (relativeDualizingComplexTrace f
            (StandardModel.isQuasicoherent_homology_derivedPushforward f)
            (derivedStructureSheafInDegree Y 0))))
```

## Tag 0E4L, a lemma

[Tag 0E4L](https://stacks.math.columbia.edu/tag/0E4L) in the Stacks Project.

**`Stacks.Duality.StandardModel.isIso_derivedSheafHomothety_relativeDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperFlatDualizing/Endomorphisms.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ProperFlatDualizing/Endomorphisms.lean#L213). The attribute's comment: “(3)”.

> Let `Y` be a quasi-compact and quasi-separated scheme and `f : X ⟶ Y` a proper, flat
> morphism of finite presentation, with relative dualizing complex `ω_{X/Y} = a(𝒪_Y)`
> ([Stacks, Remark 0B6S]). Then the homothety `𝒪_X ⟶ R𝓗om_{𝒪_X}(ω_{X/Y}, ω_{X/Y})` is an
> isomorphism.

```lean
theorem isIso_derivedSheafHomothety_relativeDualizingComplex :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    IsIso (Stacks.SheafOfModules.derivedSheafHomothety X.sheaf
      (relativeDualizingComplex f).obj)
```

**`Stacks.Duality.StandardModel.isZero_homology_derivedPushforward_relativeDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperFlatDualizing/PushforwardVanishing.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ProperFlatDualizing/PushforwardVanishing.lean#L58). The attribute's comment: “(2)”.

> **[Stacks, Tag 0E4L] (2).** Let `Y` be a quasi-compact and quasi-separated scheme and
> `f : X ⟶ Y` a proper, flat morphism of finite presentation, with relative dualizing complex
> `ω_{X/Y} = a(𝒪_Y)` ([Stacks, Remark 0B6S]). Then `Rf_*ω_{X/Y}` has vanishing cohomology sheaves
> in positive degrees.

```lean
theorem isZero_homology_derivedPushforward_relativeDualizingComplex (i : ℤ) (hi : 0 < i) :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    IsZero ((DerivedCategory.homologyFunctor Y.Modules i).obj
      ((derivedPushforward f).obj (relativeDualizingComplex f).obj))
```

**`Stacks.Duality.StandardModel.isRelativelyPerfect_relativeDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperFlatDualizing/RelativelyPerfect.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ProperFlatDualizing/RelativelyPerfect.lean#L119). The attribute's comment: “(1)”. References: SGA 6 III (4.9.1), “Case S = Y and F = O_Y”; SGA 6 IV (3.3.2), “3.3.2.4”.

> **[Stacks, Tag 0E4L] (1).** Let `Y` be a quasi-compact and quasi-separated scheme and
> `f : X ⟶ Y` a proper, flat morphism of finite presentation, with relative dualizing complex
> `ω_{X/Y} = a(𝒪_Y)` ([Stacks, Remark 0B6S]). Then `ω_{X/Y}` is a `Y`-perfect object of `D(𝒪_X)`.
>
> Over an affine open `V ⊆ Y`, with `Spec Γ(V) ⟶ Y` the inclusion, the base change of `ω_{X/Y}` to
> `f⁻¹V ⟶ Spec Γ(V)` is the relative dualizing complex of the base change
> (`Stacks.Duality.StandardModel.pullbackRelativeDualizingComplexIso`), which is
> `Spec Γ(V)`-perfect (`isRelativelyPerfect_relativeDualizingComplex_of_spec`); relative
> perfectness is local on the source and on the base.

```lean
theorem isRelativelyPerfect_relativeDualizingComplex {X Y : Scheme.{u}} (f : X ⟶ Y)
    [CompactSpace Y] [QuasiSeparatedSpace Y] [IsProper f] [Flat f]
    [LocallyOfFinitePresentation f] :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    f.IsRelativelyPerfect (relativeDualizingComplex f).obj
```

## Tag 0E2P, a lemma

[Tag 0E2P](https://stacks.math.columbia.edu/tag/0E2P) in the Stacks Project.

**`Stacks.Duality.relativeDualizingComplexRigidity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/Rigidity.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/Rigidity.lean#L135).

> **Rigidity, [Stacks, Tag 0E2P].** Let `Y` be a quasi-compact and quasi-separated scheme and
> `f : X ⟶ Y` proper, flat and of finite presentation, with relative dualizing complex
> `ω = a(𝒪_Y)` ([Stacks, Tag 0B6S]), and let `c` be the right adjoint of `RΔ_*` on `D_QCoh` for the
> diagonal `Δ : X ⟶ X ×_Y X` ([Stacks, Tag 0A9E]). There are canonical isomorphisms
> `𝒪_X ≅ c(Lpr₁^*ω)`, `𝒪_X ≅ c(Lpr₂^*ω)` (Equation 0E2Q) and `ω ≅ c(Lpr₁^*ω ⊗ᴸ Lpr₂^*ω)`
> (Equation 0E2R).

```lean
def relativeDualizingComplexRigidity {X Y : Scheme.{u}} [CompactSpace Y] [QuasiSeparatedSpace Y]
    (f : X ⟶ Y) [IsProper f] [Flat f] [LocallyOfFinitePresentation f] :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    haveI : CompactSpace (pullback f f : Scheme.{u}) :=
      QuasiCompact.compactSpace_of_compactSpace (pullback.snd f f)
    haveI : QuasiSeparatedSpace (pullback f f : Scheme.{u}) :=
      quasiSeparatedSpace_of_quasiSeparated (pullback.snd f f)
    ((DerivedPushforward.derivedStructureSheaf X ≅
        (twistedInverseImage (pullback.diagonal f)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs (pullback.diagonal f))).obj
          ((quasiCoherentDerivedPullback' (pullback.fst f f)).obj
            ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
            (DerivedPushforward.derivedStructureSheaf Y)))) ×
      (DerivedPushforward.derivedStructureSheaf X ≅
        (twistedInverseImage (pullback.diagonal f)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs (pullback.diagonal f))).obj
          ((quasiCoherentDerivedPullback' (pullback.snd f f)).obj
            ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
            (DerivedPushforward.derivedStructureSheaf Y))))) ×
      (((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
          (DerivedPushforward.derivedStructureSheaf Y)) ≅
        (twistedInverseImage (pullback.diagonal f)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs (pullback.diagonal f))).obj
          (((quasiCoherentDerivedTensor (pullback f f)).obj
            ((quasiCoherentDerivedPullback' (pullback.fst f f)).obj
              ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
              (DerivedPushforward.derivedStructureSheaf Y)))).obj
            ((quasiCoherentDerivedPullback' (pullback.snd f f)).obj
              ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
              (DerivedPushforward.derivedStructureSheaf Y)))))
```

## Tag 0E2Q, an equation

[Tag 0E2Q](https://stacks.math.columbia.edu/tag/0E2Q) in the Stacks Project.

**`Stacks.Duality.structureSheafIsoDiagonalTwistedInverseImagePullbackFst`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexRigidity.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexRigidity.lean#L200). The attribute's comment: “first projection: 𝒪_X ≅ c(L pr₁^* ω_{X/Y}^•)”.

> **[Stacks, Tag 0E2Q], first projection**: `𝒪_X ≅ c(L pr₁^* ω_{X/Y}^•)`; this is the first
> isomorphism of [Stacks, Tag 0E2P], where
> `ω_{X/Y}^• = a(𝒪_Y)` is the relative dualizing complex and `c` the twisted inverse image of the
> diagonal `Δ : X ⟶ X ×_Y X`. With `b'` the twisted inverse image of `pr₂`, `𝒪_X = c(b'(𝒪_X))` as
> `pr₂ ∘ Δ = id`, and `b'(𝒪_X) = L pr₁^* a(𝒪_Y)` by flat base change.

```lean
def structureSheafIsoDiagonalTwistedInverseImagePullbackFst :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    haveI : CompactSpace (pullback f f : Scheme.{u}) :=
      QuasiCompact.compactSpace_of_compactSpace (pullback.fst f f)
    haveI : QuasiSeparatedSpace (pullback f f : Scheme.{u}) := quasiSeparatedSpace_of_quasiSeparated
      (pullback.fst f f)
    derivedStructureSheaf X ≅
      (twistedInverseImage (pullback.diagonal f)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs (pullback.diagonal f))).obj
        ((quasiCoherentDerivedPullback' (pullback.fst f f)).obj
          ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
            (derivedStructureSheaf Y)))
```

**`Stacks.Duality.structureSheafIsoDiagonalTwistedInverseImagePullbackSnd`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexRigidity.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexRigidity.lean#L229). The attribute's comment: “second projection: 𝒪_X ≅ c(L pr₂^* ω_{X/Y}^•)”.

> **[Stacks, Tag 0E2Q], second projection**: `𝒪_X ≅ c(L pr₂^* ω_{X/Y}^•)`; this is the second
> isomorphism of [Stacks, Tag 0E2P]. With `b` the twisted
> inverse image of `pr₁`, `𝒪_X = c(b(𝒪_X))` as `pr₁ ∘ Δ = id`, and `b(𝒪_X) = L pr₂^* a(𝒪_Y)` by
> flat base change.

```lean
def structureSheafIsoDiagonalTwistedInverseImagePullbackSnd :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    haveI : CompactSpace (pullback f f : Scheme.{u}) :=
      QuasiCompact.compactSpace_of_compactSpace (pullback.fst f f)
    haveI : QuasiSeparatedSpace (pullback f f : Scheme.{u}) := quasiSeparatedSpace_of_quasiSeparated
      (pullback.fst f f)
    derivedStructureSheaf X ≅
      (twistedInverseImage (pullback.diagonal f)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs (pullback.diagonal f))).obj
        ((quasiCoherentDerivedPullback' (pullback.snd f f)).obj
          ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
            (derivedStructureSheaf Y)))
```

**`Stacks.Duality.nonempty_twistedInverseImage_diagonal_pullback_relativeDualizingComplex_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DiagonalRigidity.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DiagonalRigidity.lean#L146).

> **Equation (0E2Q) of [Stacks, Tag 0E2P].** Let `Y` be quasi-compact and quasi-separated and
> `f : X ⟶ Y` proper, flat and of finite presentation, with relative dualizing complex
> `ω_{X/Y}^• = a(𝒪_Y)` ([Stacks, Remark 0B6S]). Then, `c` being the right adjoint of `RΔ_*` for the
> diagonal `Δ : X ⟶ X ×_Y X` ([Stacks, Tag 0A9E]),
>
> `𝒪_X ≅ c(L pr₁^* ω_{X/Y}^•)` and `𝒪_X ≅ c(L pr₂^* ω_{X/Y}^•)`.

```lean
theorem nonempty_twistedInverseImage_diagonal_pullback_relativeDualizingComplex_iso :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    haveI := QuasiCompact.compactSpace_of_compactSpace (pullback.snd f f)
    haveI := quasiSeparatedSpace_of_quasiSeparated (pullback.snd f f)
    Nonempty (DerivedPushforward.derivedStructureSheaf X ≅
      (twistedInverseImage (pullback.diagonal f)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs (pullback.diagonal f))).obj
        ((quasiCoherentDerivedPullback' (pullback.fst f f)).obj
          (relativeDualizingComplex f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
            (DerivedPushforward.derivedStructureSheaf Y)))) ∧
    Nonempty (DerivedPushforward.derivedStructureSheaf X ≅
      (twistedInverseImage (pullback.diagonal f)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs (pullback.diagonal f))).obj
        ((quasiCoherentDerivedPullback' (pullback.snd f f)).obj
          (relativeDualizingComplex f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
            (DerivedPushforward.derivedStructureSheaf Y))))
```

## Tag 0E2R, an equation

[Tag 0E2R](https://stacks.math.columbia.edu/tag/0E2R) in the Stacks Project.

**`Stacks.Duality.relativeDualizingComplexRigidityIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexRigidity.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexRigidity.lean#L261).

> **[Stacks, Tag 0E2R], the rigidity isomorphism**; this is the isomorphism of
> [Stacks, Tag 0E2P] in Equation 0E2R:
> `ω_{X/Y}^• ≅ c(L pr₁^* ω_{X/Y}^• ⊗ᴸ_{𝒪_{X ×_Y X}} L pr₂^* ω_{X/Y}^•)`, where
> `ω_{X/Y}^• = a(𝒪_Y)` is the relative dualizing complex of [Stacks, Tag 0B6S] and `c` the twisted
> inverse image of the diagonal `Δ : X ⟶ X ×_Y X`. With `b` the twisted inverse image of `pr₁`:
> `ω = c(b(ω))` as `pr₁ ∘ Δ = id`, `b(ω) = L pr₁^*ω ⊗ᴸ b(𝒪_X)` by [Stacks, Tag 0E4K], and
> `b(𝒪_X) = L pr₂^* a(𝒪_Y)` by [Stacks, Tag 0AAB].

```lean
def relativeDualizingComplexRigidityIso :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    haveI : CompactSpace (pullback f f : Scheme.{u}) :=
      QuasiCompact.compactSpace_of_compactSpace (pullback.fst f f)
    haveI : QuasiSeparatedSpace (pullback f f : Scheme.{u}) := quasiSeparatedSpace_of_quasiSeparated
      (pullback.fst f f)
    (twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
        (derivedStructureSheaf Y) ≅
      (twistedInverseImage (pullback.diagonal f)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs (pullback.diagonal f))).obj
        (((quasiCoherentDerivedTensor (pullback f f : Scheme.{u})).obj
          ((quasiCoherentDerivedPullback' (pullback.fst f f)).obj
            ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
              (derivedStructureSheaf Y)))).obj
          ((quasiCoherentDerivedPullback' (pullback.snd f f)).obj
            ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
              (derivedStructureSheaf Y))))
```

## Tag 0BRU, a remark

[Tag 0BRU](https://stacks.math.columbia.edu/tag/0BRU) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.Duality.relativeDualizingComplexRigidityIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexRigidity.lean#L261), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexRigidity.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RelativeDualizingComplexRigidity.lean#L313) (StacksFrontier): “the rigidity isomorphism ω_{X/Y}^• ≅ c(L pr₁^* ω_{X/Y}^• ⊗ᴸ L pr₂^* ω_{X/Y}^•) of Equation 0E2R”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.12, Tag 0E4H](https://stacks.math.columbia.edu/tag/0E4H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

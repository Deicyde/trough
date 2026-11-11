---
declaration: section
origin: cited
lean: Stacks.Duality.compareWithPullbackTensor, Stacks.Duality.homEquiv_symm_compareWithPullbackTensor, Stacks.Duality.projectionFormulaMap_comp_map_compareWithPullbackTensor_comp_counit, Stacks.Duality.compareWithPullbackTensor_naturality, Stacks.Duality.twistedInverseImageCompareWithPullbackTensor, Stacks.Duality.qcqsCompareWithPullbackTensor, Stacks.Duality.homEquiv_symm_qcqsCompareWithPullbackTensor, Stacks.Duality.qcqsCompareWithPullback
statement: formalized
proof: formalized
---

# 48.8 Right adjoint of pushforward and pullback

Section 48.8 of the Stacks Project, [Tag 0B6N](https://stacks.math.columbia.edu/tag/0B6N). 5 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A9S, an equation

[Tag 0A9S](https://stacks.math.columbia.edu/tag/0A9S) in the Stacks Project.

**`Stacks.Duality.compareWithPullbackTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparison.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparison.lean#L237). The attribute's comment: “variant: the two-variable map for an arbitrary cotensorator α and right adjoint a; the tag is Stacks.Duality.qcqsCompareWithPullback”.

> **The two-variable comparison map of Equation 48.8.0.1 of [Stacks, Tag 0A9S]**:
> `Lf^*K ⊗ᴸ_{𝒪_X} a(L) ⟶ a(K ⊗ᴸ_{𝒪_Y} L)`, for a right adjoint `a` of
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`. It is the map adjoint to the inverse of the projection
> formula `Rf_*(Lf^*K ⊗ᴸ_{𝒪_X} a(L)) ≅ K ⊗ᴸ_{𝒪_Y} Rf_*(a(L))` followed by the identity of `K`
> tensored with the trace map `adj.counit.app L : Rf_*(a(L)) ⟶ L`.

```lean
def compareWithPullbackTensor (K L : quasiCoherentDerivedCategory Y) :
    ((quasiCoherentDerivedTensor X).obj
        ((quasiCoherentDerivedPullback' f).obj K)).obj (a.obj L) ⟶
      a.obj (((quasiCoherentDerivedTensor Y).obj K).obj L)
```

**`Stacks.Duality.homEquiv_symm_compareWithPullbackTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparison.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparison.lean#L249). The attribute's comment: “variant: the adjunction characterization of the two-variable map for an arbitrary α and a; the tag is Stacks.Duality.qcqsCompareWithPullback”.

> **The adjunction characterization of the comparison map.** Its adjoint transpose is the
> inverse projection formula followed by the identity of `K` tensored with the trace map; this
> determines the comparison map uniquely.

```lean
theorem homEquiv_symm_compareWithPullbackTensor (K L : quasiCoherentDerivedCategory Y) :
    (adj.homEquiv _ _).symm (compareWithPullbackTensor f hpush α adj K L) =
      inv (projectionFormulaMap f hpush α (a.obj L) K) ≫
        ((quasiCoherentDerivedTensor Y).obj K).map (adj.counit.app L)
```

**`Stacks.Duality.projectionFormulaMap_comp_map_compareWithPullbackTensor_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparison.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparison.lean#L271). The attribute's comment: “variant: the characterization without the inverse for an arbitrary α and a; the tag is Stacks.Duality.qcqsCompareWithPullback”.

> **Equation 48.8.0.1 as the source states it**: the projection formula, followed by `Rf_*` of
> the comparison map and the trace map, is the identity of `K` tensored with the trace map. This is
> the characterization with no inverse in it.

```lean
theorem projectionFormulaMap_comp_map_compareWithPullbackTensor_comp_counit
    (K L : quasiCoherentDerivedCategory Y) :
    projectionFormulaMap f hpush α (a.obj L) K ≫
        (quasiCoherentDerivedPushforward f hpush).map
            (compareWithPullbackTensor f hpush α adj K L) ≫
          adj.counit.app (((quasiCoherentDerivedTensor Y).obj K).obj L) =
      ((quasiCoherentDerivedTensor Y).obj K).map (adj.counit.app L)
```

**`Stacks.Duality.compareWithPullbackTensor_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparison.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparison.lean#L337). The attribute's comment: “variant: naturality of the two-variable map for an arbitrary α and a; the tag is Stacks.Duality.qcqsCompareWithPullback”.

> The comparison map is natural in `K` and `L` jointly.

```lean
theorem compareWithPullbackTensor_naturality {K K' L L' : quasiCoherentDerivedCategory Y}
    (h : K ⟶ K') (g : L ⟶ L') :
    ((quasiCoherentDerivedTensor X).map
          ((quasiCoherentDerivedPullback' f).map h)).app (a.obj L) ≫
        ((quasiCoherentDerivedTensor X).obj
            ((quasiCoherentDerivedPullback' f).obj K')).map (a.map g) ≫
          compareWithPullbackTensor f hpush α adj K' L' =
      compareWithPullbackTensor f hpush α adj K L ≫
        a.map (((quasiCoherentDerivedTensor Y).map h).app L ≫
          ((quasiCoherentDerivedTensor Y).obj K').map g)
```

**`Stacks.Duality.twistedInverseImageCompareWithPullbackTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparison.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparison.lean#L366). The attribute's comment: “variant: the two-variable map at a = f^× for an arbitrary α; the tag is Stacks.Duality.qcqsCompareWithPullback”.

> **Equation 48.8.0.1 for the twisted inverse image `f^×`** of
> `Stacks.Duality.twistedInverseImage`: the comparison map
> `Lf^*K ⊗ᴸ_{𝒪_X} f^×L ⟶ f^×(K ⊗ᴸ_{𝒪_Y} L)`, obtained from `compareWithPullbackTensor` at the
> adjunction `Rf_* ⊣ f^×`.

```lean
def twistedInverseImageCompareWithPullbackTensor (K L : quasiCoherentDerivedCategory Y) :
    ((quasiCoherentDerivedTensor X).obj
        ((quasiCoherentDerivedPullback' f).obj K)).obj
        ((twistedInverseImage f hpush).obj L) ⟶
      (twistedInverseImage f hpush).obj (((quasiCoherentDerivedTensor Y).obj K).obj L)
```

**`Stacks.Duality.qcqsCompareWithPullbackTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonQcqs.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonQcqs.lean#L89). The attribute's comment: “the two-variable map Lf^*K ⊗ a(L) ⟶ a(K ⊗ L) from which the source obtains the equation, for a morphism of quasi-compact quasi-separated schemes and a = f^× of Tag 0A9E”.

> **The two-variable map of [Stacks, Tag 0A9S]** for a morphism `f : X ⟶ Y` of quasi-compact
> quasi-separated schemes: `Lf^*K ⊗ᴸ_{𝒪_X} a(L) ⟶ a(K ⊗ᴸ_{𝒪_Y} L)`, where `a = f^×` is the right
> adjoint of `Rf_*` of [Stacks, Tag 0A9E]. It is adjoint to the inverse of the projection formula
> `Rf_*(Lf^*K ⊗ᴸ a(L)) ≅ K ⊗ᴸ Rf_*(a(L))` of [Stacks, Tag 08EU] followed by the identity of `K`
> tensored with the trace map `Rf_*a(L) ⟶ L`.

```lean
def qcqsCompareWithPullbackTensor (K L : quasiCoherentDerivedCategory Y) :
    ((quasiCoherentDerivedTensor X).obj ((quasiCoherentDerivedPullback' f).obj K)).obj
        ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj L) ⟶
      (twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
        (((quasiCoherentDerivedTensor Y).obj K).obj L)
```

**`Stacks.Duality.homEquiv_symm_qcqsCompareWithPullbackTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonQcqs.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonQcqs.lean#L103). The attribute's comment: “defining property of the two-variable map: its adjoint is the inverse projection formula of Tag 08EU followed by K tensored with the trace map”.

> **The defining property of the two-variable map**: its adjoint transpose for `Rf_* ⊣ a` is
> the inverse of the projection-formula isomorphism followed by the identity of `K` tensored with
> the trace map `Rf_*a(L) ⟶ L`. This determines the map uniquely.

```lean
theorem homEquiv_symm_qcqsCompareWithPullbackTensor (K L : quasiCoherentDerivedCategory Y) :
    ((twistedInverseImageAdjunction f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).homEquiv _ _).symm
        (qcqsCompareWithPullbackTensor f K L) =
      inv (projectionFormulaMap f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          (pullbackCotensorator f)
          ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj L)
          K) ≫
        ((quasiCoherentDerivedTensor Y).obj K).map
          ((twistedInverseImageAdjunction f
            (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).counit.app L)
```

**`Stacks.Duality.qcqsCompareWithPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonQcqs.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonQcqs.lean#L162).

> **Equation 48.8.0.1 of [Stacks, Tag 0A9S].** Let `f : X ⟶ Y` be a morphism of quasi-compact
> and quasi-separated schemes and let `a = f^×` be the right adjoint of
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` of [Stacks, Tag 0A9E]. The canonical map
>
>   `Lf^*K ⊗ᴸ_{𝒪_X} a(𝒪_Y) ⟶ a(K)`,
>
> functorial in `K ∈ D_QCoh(𝒪_Y)`: the two-variable map `qcqsCompareWithPullbackTensor` at
> `L = 𝒪_Y`, followed by `a` of the right unitor `K ⊗ᴸ_{𝒪_Y} 𝒪_Y ≅ K`.

```lean
def qcqsCompareWithPullback :
    quasiCoherentDerivedPullback' f ⋙
        (quasiCoherentDerivedTensor X).flip.obj
          ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
            (derivedStructureSheaf Y)) ⟶
      twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
```

**`Stacks.Duality.homEquiv_symm_qcqsCompareWithPullback_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonQcqs.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonQcqs.lean#L189). The attribute's comment: “defining property of the map: its adjoint is the inverse projection formula of Tag 08EU, then K tensored with the trace map, then the unitor”.

> **The defining property of Equation 48.8.0.1**: the adjoint transpose of
> `Lf^*K ⊗ᴸ a(𝒪_Y) ⟶ a(K)` for `Rf_* ⊣ a` is the inverse of the projection formula
> `Rf_*(Lf^*K ⊗ᴸ a(𝒪_Y)) ≅ K ⊗ᴸ Rf_*a(𝒪_Y)`, followed by the identity of `K` tensored with the
> trace map `Rf_*a(𝒪_Y) ⟶ 𝒪_Y` and the right unitor `K ⊗ᴸ 𝒪_Y ≅ K`.

```lean
theorem homEquiv_symm_qcqsCompareWithPullback_app (K : quasiCoherentDerivedCategory Y) :
    ((twistedInverseImageAdjunction f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).homEquiv _ _).symm
        ((qcqsCompareWithPullback f).app K) =
      inv (projectionFormulaMap f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          (pullbackCotensorator f)
          ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
            (derivedStructureSheaf Y)) K) ≫
        ((quasiCoherentDerivedTensor Y).obj K).map
          ((twistedInverseImageAdjunction f
            (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).counit.app
            (derivedStructureSheaf Y)) ≫
          quasiCoherentRightUnitor.hom.app K
```

**`Stacks.Duality.commShift_qcqsCompareWithPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonQcqsCommShift.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonQcqsCommShift.lean#L132). The attribute's comment: “compatible with distinguished triangles: the map of 48.8.0.1 commutes with the shift, between exact functors”.

> **[Stacks, Tag 0A9S]: Equation 48.8.0.1 is compatible with distinguished triangles.** For a
> morphism `f : X ⟶ Y` of quasi-compact quasi-separated schemes, the map
> `Lf^*K ⊗ᴸ_{𝒪_X} a(𝒪_Y) ⟶ a(K)` commutes with the shift, `Lf^*` carrying its commutation with
> the shift as the left adjoint of `Rf_*` and `a` its commutation as the right adjoint of `Rf_*`.
> Its source and target are exact functors (`isTriangulated_qcqsCompareWithPullback_source`,
> `isTriangulated_qcqsTwistedInverseImage`), so it is a morphism of exact functors.

```lean
theorem commShift_qcqsCompareWithPullback :
    letI := commShift_quasiCoherentDerivedPullback f (isQuasicoherent_homology_derivedPullback' f)
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
    letI := (twistedInverseImageAdjunction f
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).rightAdjointCommShift ℤ
    NatTrans.CommShift (qcqsCompareWithPullback f) ℤ
```

**`Stacks.Duality.compareWithPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonStructureSheaf.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonStructureSheaf.lean#L92). The attribute's comment: “variant: the map for an arbitrary cotensorator α, right adjoint a and unitor ρ; the tag is Stacks.Duality.qcqsCompareWithPullback”.

> **Equation 48.8.0.1 of [Stacks, Tag 0A9S]**: the comparison map
> `Lf^*K ⊗ᴸ_{𝒪_X} a(𝒪_Y) ⟶ a(K)`, the two-variable comparison map at `L = 𝒪_Y` followed by `a`
> applied to the right unitor `K ⊗ᴸ_{𝒪_Y} 𝒪_Y ≅ K`.

```lean
def compareWithPullback (K : quasiCoherentDerivedCategory Y) :
    ((quasiCoherentDerivedTensor X).obj
        ((quasiCoherentDerivedPullback' f).obj K)).obj
        (a.obj (derivedStructureSheaf Y)) ⟶
      a.obj K
```

**`Stacks.Duality.compareWithPullback_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonStructureSheaf.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonStructureSheaf.lean#L103). The attribute's comment: “variant: functoriality in K for an arbitrary α, a and ρ; the tag is Stacks.Duality.qcqsCompareWithPullback”.

> Equation 48.8.0.1 is functorial in `K`.

```lean
theorem compareWithPullback_naturality {K K' : quasiCoherentDerivedCategory Y} (h : K ⟶ K') :
    ((quasiCoherentDerivedTensor X).map
          ((quasiCoherentDerivedPullback' f).map h)).app
          (a.obj (derivedStructureSheaf Y)) ≫
        compareWithPullback f hpush α adj ρ K' =
      compareWithPullback f hpush α adj ρ K ≫ a.map h
```

**`Stacks.Duality.twistedInverseImageCompareWithPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonStructureSheaf.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonStructureSheaf.lean#L169). The attribute's comment: “variant: the map at a = f^× for an arbitrary α and ρ; the tag is Stacks.Duality.qcqsCompareWithPullback”.

> **Equation 48.8.0.1 for the twisted inverse image `f^×`** of
> `Stacks.Duality.twistedInverseImage`: the comparison map `Lf^*K ⊗ᴸ_{𝒪_X} f^×𝒪_Y ⟶ f^×K` of
> [Stacks, Tag 0A9S].

```lean
def twistedInverseImageCompareWithPullback
    (ρ : (quasiCoherentDerivedTensor Y).flip.obj (derivedStructureSheaf Y) ≅ 𝟭 _)
    (K : quasiCoherentDerivedCategory Y) :
    ((quasiCoherentDerivedTensor X).obj
        ((quasiCoherentDerivedPullback' f).obj K)).obj
        ((twistedInverseImage f hpush).obj (derivedStructureSheaf Y)) ⟶
      (twistedInverseImage f hpush).obj K
```

## Tag 0A9T, a lemma

[Tag 0A9T](https://stacks.math.columbia.edu/tag/0A9T) in the Stacks Project.

**`Stacks.Duality.isIso_compareWithPullbackTensor_and_compareWithPullback_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonPerfectDual.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/RightAdjointPushforward/PullbackComparisonPerfectDual.lean#L67).

> **[Stacks, Tag 0A9T] (Lemma 48.8.1).** Let `f : X ⟶ Y` be a quasi-compact and
> quasi-separated morphism of schemes with `Y` quasi-compact (for instance a morphism of
> quasi-compact and quasi-separated schemes), and let `a` be a right adjoint of
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`. If `K ∈ D_QCoh(𝒪_Y)` is perfect, then
>
> * the map `Lf^*K ⊗ᴸ_{𝒪_X} a(L) ⟶ a(K ⊗ᴸ_{𝒪_Y} L)` of [Stacks, Tag 0A9S] is an isomorphism for
>   every `L ∈ D_QCoh(𝒪_Y)`, and
> * in particular Equation 48.8.0.1, `Lf^*K ⊗ᴸ_{𝒪_X} a(𝒪_Y) ⟶ a(K)`, is an isomorphism, for any
>   identification `ρ` of `- ⊗ᴸ 𝒪_Y` with the identity (such as the right unitor).

```lean
theorem isIso_compareWithPullbackTensor_and_compareWithPullback_of_isPerfect
    {K : quasiCoherentDerivedCategory Y}
    (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := Y.toRingedSpace) K.obj) :
    (∀ L : quasiCoherentDerivedCategory Y,
      IsIso (compareWithPullbackTensor f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (quasiCoherentDerivedPullbackTensorIso f).hom adj K L)) ∧
    ∀ ρ : (quasiCoherentDerivedTensor Y).flip.obj (DerivedPushforward.derivedStructureSheaf Y) ≅
        𝟭 _,
      IsIso (compareWithPullback f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (quasiCoherentDerivedPullbackTensorIso f).hom adj ρ K)
```

## Tag 0B6P, a lemma

[Tag 0B6P](https://stacks.math.columbia.edu/tag/0B6P) in the Stacks Project.

**`Stacks.Duality.map_twistedInverseImageCompareWithPullback_comp_baseChange_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChangeTrace.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/BaseChangeTrace.lean#L206).

> **[Stacks, Tag 0B6P] (Lemma 48.8.2).** For a cartesian square of quasi-compact and
> quasi-separated schemes with `f` and `g` Tor independent and `K ∈ D_QCoh(𝒪_Y)`, the square
>
> ```
> L(g')^*(Lf^*K ⊗ᴸ a(𝒪_Y)) ──────────────→ L(g')^*a(K)
>           │                                    │ α_K
>           ↓                                    ↓
> L(f')^*Lg^*K ⊗ᴸ a'(𝒪_{Y'}) ─────────────→ a'(Lg^*K)
> ```
>
> commutes, where the horizontal arrows are the maps of Equation 48.8.0.1 for `K` and `Lg^*K`, `α`
> is the base change map of Equation 48.5.0.1, and the left vertical arrow is the tensor comparison
> of `L(g')^*`, the identification `L(g')^*Lf^* ≅ L(f')^*Lg^*` of the composites around the
> square, and `α` at `𝒪_Y` followed by `a'` of `Lg^*𝒪_Y ≅ 𝒪_{Y'}`.

```lean
theorem map_twistedInverseImageCompareWithPullback_comp_baseChange_of_torIndependent
    (sq : IsPullback g' f' f g) (hTor : TorIndependent f g) (K : quasiCoherentDerivedCategory Y) :
    haveI := isIso_twistedInverseImagePushforwardBaseChange_of_torIndependent sq hTor
    (quasiCoherentDerivedPullback' g').map
        (twistedInverseImageCompareWithPullback f
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          (quasiCoherentDerivedPullbackTensorIso f).hom (quasiCoherentDerivedTensorRightUnitor Y)
          K) ≫
      (twistedInverseImageBaseChangeMap g' f' f g
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g) sq).app K =
      (quasiCoherentDerivedPullbackTensorIso g').hom.app
          ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
            (DerivedPushforward.derivedStructureSheaf Y), (quasiCoherentDerivedPullback' f).obj K) ≫
        ((quasiCoherentDerivedTensor X').map
          (((quasiCoherentDerivedPullbackCompIso g' f ≪≫ quasiCoherentDerivedPullbackCongr sq.w) ≪≫
            (quasiCoherentDerivedPullbackCompIso f' g).symm).hom.app K)).app
          ((quasiCoherentDerivedPullback' g').obj
            ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
              (DerivedPushforward.derivedStructureSheaf Y))) ≫
        ((quasiCoherentDerivedTensor X').obj
            ((quasiCoherentDerivedPullback' f').obj ((quasiCoherentDerivedPullback' g).obj K))).map
          ((twistedInverseImageBaseChangeMap g' f' f g
              (isQuasicoherent_homology_derivedPushforward_of_qcqs g')
              (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
              (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
              (isQuasicoherent_homology_derivedPushforward_of_qcqs g) sq).app
              (DerivedPushforward.derivedStructureSheaf Y) ≫
            (twistedInverseImage f' (isQuasicoherent_homology_derivedPushforward_of_qcqs f')).map
              ((quasiCoherentDerivedPullback' g).map
                  (eqToHom (tensorUnit_quasiCoherentDerivedCategory Y).symm) ≫
                Functor.OplaxMonoidal.η (quasiCoherentDerivedPullback' g) ≫
                eqToHom (tensorUnit_quasiCoherentDerivedCategory Y'))) ≫
        twistedInverseImageCompareWithPullback f'
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
          (quasiCoherentDerivedPullbackTensorIso f').hom (quasiCoherentDerivedTensorRightUnitor Y')
          ((quasiCoherentDerivedPullback' g).obj K)
```

## Tag 0B6Q, a lemma

[Tag 0B6Q](https://stacks.math.columbia.edu/tag/0B6Q) in the Stacks Project.

**`Stacks.Duality.isIso_map_twistedInverseImageCompareWithPullback_of_isIso_morphismRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekComparisonCharts.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekComparisonCharts.lean#L128).

> **Stacks Project, Tag 0B6Q (Lemma 48.8.3).** Let `f : X ⟶ Y` be a proper morphism of
> Noetherian schemes and let `V ⊆ Y` be an open such that `f⁻¹(V) ⟶ V` is an isomorphism. Then for
> `K ∈ D⁺_QCoh(𝒪_Y)` the map `Lf^*K ⊗ᴸ a(𝒪_Y) ⟶ a(K)` of Equation 48.8.0.1 restricts to an
> isomorphism over `f⁻¹(V)`.

```lean
theorem isIso_map_twistedInverseImageCompareWithPullback_of_isIso_morphismRestrict
    (V : Y.Opens) [IsIso (f ∣_ V)] (K : quasiCoherentDerivedCategory Y)
    (hK : DerivedCategoryB.IsBoundedBelow K.obj) :
    IsIso ((quasiCoherentDerivedPullback' (f ⁻¹ᵁ V).ι).map
      (twistedInverseImageCompareWithPullback f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (quasiCoherentDerivedPullbackTensorIso f).hom
        (quasiCoherentDerivedTensorRightUnitor Y) K))
```

## Tag 0B6R, a lemma

[Tag 0B6R](https://stacks.math.columbia.edu/tag/0B6R) in the Stacks Project.

**`Stacks.Duality.twistedInverseImageCompareWithPullback_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/CompositionComparison.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/CompositionComparison.lean#L158).

> Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of quasi-compact and quasi-separated schemes,
> `h = f ≫ g`, and `a`, `b`, `c` the right adjoints of `Rf_*`, `Rg_*`, `Rh_*` on `D_QCoh`. For
> `K ∈ D_QCoh(𝒪_Z)` the diagram
>
> ```
> Lf^*(Lg^*K ⊗ᴸ b(𝒪_Z)) ⊗ᴸ a(𝒪_Y) ──→ a(Lg^*K ⊗ᴸ b(𝒪_Z)) ──→ a(b(K))
>             ‖                                                  ‖
> Lh^*K ⊗ᴸ (Lf^*b(𝒪_Z) ⊗ᴸ a(𝒪_Y)) ──→ Lh^*K ⊗ᴸ c(𝒪_Z) ──────→ c(K)
> ```
>
> commutes, where the arrows are Equation 48.8.0.1 (for `f` at `Lg^*K ⊗ᴸ b(𝒪_Z)`, `a` of that for
> `g` at `K`; `Lh^*K` tensored with that for `f` at `b(𝒪_Z)`, then that for `h` at `K`), the left
> identification is the tensor comparison of `Lf^*`, the associator and `Lf^* ∘ Lg^* = Lh^*`, and
> `c = a ∘ b` is `Stacks.Duality.twistedInverseImageCompIso`.

```lean
theorem twistedInverseImageCompareWithPullback_comp (K : quasiCoherentDerivedCategory Z) :
    twistedInverseImageCompareWithPullback f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (quasiCoherentDerivedPullbackTensorIso f).hom (quasiCoherentDerivedTensorRightUnitor Y)
        (((quasiCoherentDerivedTensor Y).obj ((quasiCoherentDerivedPullback' g).obj K)).obj
          ((twistedInverseImage g (isQuasicoherent_homology_derivedPushforward_of_qcqs g)).obj
            (DerivedPushforward.derivedStructureSheaf Z))) ≫
      (twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).map
        (twistedInverseImageCompareWithPullback g
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g)
          (quasiCoherentDerivedPullbackTensorIso g).hom (quasiCoherentDerivedTensorRightUnitor Z)
          K) ≫
      (twistedInverseImageCompIso f g (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs g)
          (isQuasicoherent_homology_derivedPushforward_of_qcqs (f ≫ g))).inv.app K =
    (((quasiCoherentDerivedTensor X).map ((quasiCoherentDerivedPullbackTensorIso f).hom.app
          ((twistedInverseImage g (isQuasicoherent_homology_derivedPushforward_of_qcqs g)).obj
            (DerivedPushforward.derivedStructureSheaf Z),
          (quasiCoherentDerivedPullback' g).obj K))).app
          ((twistedInverseImage f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)).obj
            (DerivedPushforward.derivedStructureSheaf Y)) ≫
      ((quasiCoherentDerivedTensorIsoCurriedTensor X).hom.app _).app _ ≫
      ((quasiCoherentDerivedTensorIsoCurriedTensor X).hom.app
          ((quasiCoherentDerivedPullback' f).obj ((quasiCoherentDerivedPullback' g).obj K))).app
          ((quasiCoherentDerivedPullback' f).obj
            ((twistedInverseImage g (isQuasicoherent_homology_derivedPushforward_of_qcqs g)).obj
              (DerivedPushforward.derivedStructureSheaf Z))) ▷ _ ≫
      (α_ _ _ _).hom ≫
      _ ◁ ((quasiCoherentDerivedTensorIsoCurriedTensor X).inv.app _).app _ ≫
      ((quasiCoherentDerivedTensorIsoCurriedTensor X).inv.app _).app _ ≫
      ((quasiCoherentDerivedTensor X).map
          ((quasiCoherentDerivedPullbackCompIso f g).hom.app K)).app _) ≫
      ((quasiCoherentDerivedTensor X).obj ((quasiCoherentDerivedPullback' (f ≫ g)).obj K)).map
        (twistedInverseImageCompareWithPullback f
          (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
          (quasiCoherentDerivedPullbackTensorIso f).hom (quasiCoherentDerivedTensorRightUnitor Y)
          ((twistedInverseImage g (isQuasicoherent_homology_derivedPushforward_of_qcqs g)).obj
            (DerivedPushforward.derivedStructureSheaf Z)) ≫
          (twistedInverseImageCompIso f g (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
            (isQuasicoherent_homology_derivedPushforward_of_qcqs g)
            (isQuasicoherent_homology_derivedPushforward_of_qcqs (f ≫ g))).inv.app
            (DerivedPushforward.derivedStructureSheaf Z)) ≫
      twistedInverseImageCompareWithPullback (f ≫ g)
        (isQuasicoherent_homology_derivedPushforward_of_qcqs (f ≫ g))
        (quasiCoherentDerivedPullbackTensorIso (f ≫ g)).hom
        (quasiCoherentDerivedTensorRightUnitor Z) K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.8, Tag 0B6N](https://stacks.math.columbia.edu/tag/0B6N)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

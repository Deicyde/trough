---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IntegralClosedSubspace.closure_image_subspacePointSet_preimageComponent_of_isFlat, AlgebraicGeometry.Space.IntegralClosedSubspace.deltaDimension_preimageComponent_of_isFlat, AlgebraicGeometry.Space.deltaDimensionClosed_preimage_eq_iSup_add, AlgebraicGeometry.Space.isClosed_preimage_pointsMap, AlgebraicGeometry.Space.locallyFinite_preimage_pointsMap
statement: formalized
proof: formalized
---

# 82.9 Preparation for flat pullback

Section 82.9 of the Stacks Project, [Tag 0EP4](https://stacks.math.columbia.edu/tag/0EP4). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EP5, a lemma

[Tag 0EP5](https://stacks.math.columbia.edu/tag/0EP5) in the Stacks Project.

**`AlgebraicGeometry.Space.IntegralClosedSubspace.closure_image_subspacePointSet_preimageComponent_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatInverseImageDeltaDimension.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatInverseImageDeltaDimension.lean#L281). The attribute's comment: “a component of the inverse image of an integral closed subspace dominates it”.

> Let `f : X ⟶ Y` be a flat morphism of good algebraic spaces over the base and let `Z ⊆ Y` be
> an integral closed subspace. An irreducible component `Z'` of `f^{-1}(Z)` dominates `Z`: the
> closure of the image of `|Z'|` is `|Z|`.

```lean
theorem IntegralClosedSubspace.closure_image_subspacePointSet_preimageComponent_of_isFlat
    (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space) (hY : D.IsGood sY) {f : X ⟶ Y}
    (hflat : IsFlat D.site D.base D.base_mem f)
    (Z : IntegralClosedSubspace D.site D.base D.base_mem Y)
    (C : irreducibleComponents (Z.preimagePointSet D.site D.base D.base_mem f)) :
    closure (pointsMap D.site D.base D.base_mem X f ''
        subspacePointSet D.site D.base D.base_mem X
          (Z.preimageComponent D.site D.base D.base_mem f hX.1
            (D.isDecentSpace_of_isGood sX hX) hY.1 C).subspace) =
      subspacePointSet D.site D.base D.base_mem Y Z.subspace
```

**`AlgebraicGeometry.Space.IntegralClosedSubspace.deltaDimension_preimageComponent_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatInverseImageDeltaDimension.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatInverseImageDeltaDimension.lean#L385). The attribute's comment: “the δ-dimension of a component of the inverse image of an integral closed subspace”.

> Let `f : X ⟶ Y` be a morphism of good algebraic spaces over the base which is flat of
> relative dimension `r`, and let `Z ⊆ Y` be an integral closed subspace. An irreducible component
> `Z'` of `f^{-1}(Z)` satisfies `dim_δ(Z') = dim_δ(Z) + r`.

```lean
theorem IntegralClosedSubspace.deltaDimension_preimageComponent_of_isFlat
    (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space) (hY : D.IsGood sY) {f : X ⟶ Y}
    (hbase : f ≫ sY = sX) (r : ℕ) (hflat : IsFlat D.site D.base D.base_mem f)
    (hr : HasRelativeDimension r D.site D.base D.base_mem f)
    (Z : IntegralClosedSubspace D.site D.base D.base_mem Y)
    (C : irreducibleComponents (Z.preimagePointSet D.site D.base D.base_mem f)) :
    deltaDimension D sX (Z.preimageComponent D.site D.base D.base_mem f hX.1
        (D.isDecentSpace_of_isGood sX hX) hY.1 C) = deltaDimension D sY Z + r
```

**`AlgebraicGeometry.Space.deltaDimensionClosed_preimage_eq_iSup_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatInverseImageDeltaDimension.lean, line 526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatInverseImageDeltaDimension.lean#L526). The attribute's comment: “the δ-dimension of the inverse image of a closed set of points”.

> Let `f : X ⟶ Y` be a morphism of good algebraic spaces over the base which is flat of
> relative dimension `r`, and let `T ⊆ |Y|` be a closed set of points whose inverse image is
> nonempty. Then `dim_δ(f^{-1}(T))` is `r` more than the supremum of the δ-dimensions of the
> irreducible components of `T` which `f` meets.
>
> When `f` meets every component of `T`, in particular when `f` is surjective, the supremum is
> `dim_δ(T)` and the formula reads `dim_δ(f^{-1}(T)) = dim_δ(T) + r`.

```lean
theorem deltaDimensionClosed_preimage_eq_iSup_add (sX : X ⟶ D.space) (hX : D.IsGood sX)
    (sY : Y ⟶ D.space) (hY : D.IsGood sY) {f : X ⟶ Y} (hbase : f ≫ sY = sX) (r : ℕ)
    (hflat : IsFlat D.site D.base D.base_mem f)
    (hr : HasRelativeDimension r D.site D.base D.base_mem f)
    (T : Set (points D.site D.base D.base_mem Y)) (hT : IsClosed T)
    (_hne : (pointsMap D.site D.base D.base_mem X f ⁻¹' T).Nonempty) :
    deltaDimensionClosed D sX hX (pointsMap D.site D.base D.base_mem X f ⁻¹' T)
        (isClosed_preimage_pointsMap D.site D.base D.base_mem hX.1 hY.1 f hT) =
      (⨆ C : irreducibleComponents T,
        ⨆ _ : (pointsMap D.site D.base D.base_mem X f ⁻¹'
            (Subtype.val '' (C : Set T))).Nonempty,
          deltaDimensionClosed D sY hY (closure (Subtype.val '' (C : Set T)))
            isClosed_closure) + ((r : ℤ) : EInt)
```

## Tag 0EP6, a lemma

[Tag 0EP6](https://stacks.math.columbia.edu/tag/0EP6) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosed_preimage_pointsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullback.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullback.lean#L55). The attribute's comment: “closedness”.

> **Stacks 0EP6, closedness.** The inverse image of a closed subset of the points of `Y`
> under a morphism `f : X ⟶ Y` of algebraic spaces over `S` is closed in the points of `X`.

```lean
theorem isClosed_preimage_pointsMap
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (_hX : IsAlgebraicSpace B S hS X)
    (_hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    letI : TopologicalSpace (points B S hS X) := pointTopology B S hS X
    letI : TopologicalSpace (points B S hS Y) := pointTopology B S hS Y
    ∀ {T : Set (points B S hS Y)}, IsClosed T →
      IsClosed ((pointsMap B S hS X f) ⁻¹' T)
```

**`AlgebraicGeometry.Space.locallyFinite_preimage_pointsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullback.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullback.lean#L72). The attribute's comment: “local finiteness”.

> **Stacks 0EP6, local finiteness.** The inverse images of a locally finite collection of
> subsets of the points of `Y` under a morphism `f : X ⟶ Y` of algebraic spaces over `S` form a
> locally finite collection of subsets of the points of `X`.

```lean
theorem locallyFinite_preimage_pointsMap
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (_hX : IsAlgebraicSpace B S hS X)
    (_hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    {I : Type v} (T : I → Set (points B S hS Y)) :
    letI : TopologicalSpace (points B S hS X) := pointTopology B S hS X
    letI : TopologicalSpace (points B S hS Y) := pointTopology B S hS Y
    LocallyFinite T →
      LocallyFinite (fun i ↦ (pointsMap B S hS X f) ⁻¹' T i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.9, Tag 0EP4](https://stacks.math.columbia.edu/tag/0EP4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_isAffineOpen_separableDegreeWeightedFiberSum_eq_max, AlgebraicGeometry.affineStratificationNumber_le_ncard_separableDegreeWeightedFiberSum
statement: formalized
proof: formalized
---

# 37.77 Weightings and affine stratification numbers

Section 37.77 of the Stacks Project, [Tag 0F3Q](https://stacks.math.columbia.edu/tag/0F3Q). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F3R, a lemma

[Tag 0F3R](https://stacks.math.columbia.edu/tag/0F3R) in the Stacks Project.

**`AlgebraicGeometry.exists_isAffineOpen_separableDegreeWeightedFiberSum_eq_max`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/AffineMaxLocus.lean, line 1130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/AffineMaxLocus.lean#L1130).

> **Stacks Project, Tag 0F3R.** Let `f : X ⟶ Y` be a quasi-finite morphism of finite
> presentation between affine schemes and let `w` be an everywhere positive weighting of `f`.
> If the weighted fibre sum of `w` attains a greatest value `d`, then the locus in `Y` where
> that value is attained is an affine open subscheme of `Y`.
>
> Quasi-finiteness is expressed, as in Tag 01TD, by `AlgebraicGeometry.LocallyOfFiniteType`
> together with `AlgebraicGeometry.LocallyQuasiFinite`; the maximum value exists by Tag 0F3K, and
> the locus is produced together with its openness rather than assumed open.

```lean
theorem exists_isAffineOpen_separableDegreeWeightedFiberSum_eq_max
    {X Y : Scheme.{u}} [IsAffine X] [IsAffine Y] (f : X ⟶ Y)
    [LocallyOfFiniteType f] [LocallyQuasiFinite f] (hfp : FinitePresentation f)
    (w : X → ℤ) (hw : IsWeighting f w) (hpositive : ∀ x, 0 < w x) (d : ℤ)
    (hd : IsGreatest (Set.range (separableDegreeWeightedFiberSum f w)) d) :
    ∃ U : Y.Opens,
      (U : Set Y) = {y | separableDegreeWeightedFiberSum f w y = d} ∧ IsAffineOpen U
```

## Tag 0F3S, a proposition

[Tag 0F3S](https://stacks.math.columbia.edu/tag/0F3S) in the Stacks Project.

**`AlgebraicGeometry.affineStratificationNumber_le_ncard_separableDegreeWeightedFiberSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/WeightingBound.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/WeightingBound.lean#L208).

> Let `f : X ⟶ Y` be a surjective quasi-finite morphism of
> schemes and let `w : X → ℤ_{>0}` be a positive weighting of `f`. If `X` is affine and `Y` is
> separated, then the affine stratification number of `Y` is at most the number of distinct values
> of the weighted fibre integral `∫_f w`.

```lean
theorem affineStratificationNumber_le_ncard_separableDegreeWeightedFiberSum
    {X Y : Scheme.{u}} [IsAffine X] [Y.IsSeparated] (f : X ⟶ Y)
    [Surjective f] [LocallyOfFiniteType f] [LocallyQuasiFinite f]
    (w : X → ℤ) (hw : IsWeighting f w) (hpositive : ∀ x, 0 < w x) :
    affineStratificationNumber Y ≤
      (Set.range (separableDegreeWeightedFiberSum f w)).ncard
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.77, Tag 0F3Q](https://stacks.math.columbia.edu/tag/0F3Q)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

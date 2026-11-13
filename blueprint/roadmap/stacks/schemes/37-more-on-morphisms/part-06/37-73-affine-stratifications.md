---
declaration: section
origin: cited
lean: AlgebraicGeometry.AffineStratification, AlgebraicGeometry.exists_affineStratification_fin, AlgebraicGeometry.hasFiniteAffineStratification_iff, AlgebraicGeometry.affineStratificationNumber, AlgebraicGeometry.affineStratificationNumber_le_of_isOpenCover, AlgebraicGeometry.affineStratificationNumber_le_of_topologicalKrullDim, AlgebraicGeometry.nonempty_affineStratification_of_topologicalKrullDim_le, AlgebraicGeometry.isZero_cohomology_of_affineStratificationNumber
statement: formalized
proof: formalized
---

# 37.73 Affine stratifications

Section 37.73 of the Stacks Project, [Tag 0F2R](https://stacks.math.columbia.edu/tag/0F2R). 8 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F2S, a definition

[Tag 0F2S](https://stacks.math.columbia.edu/tag/0F2S) in the Stacks Project.

**`AlgebraicGeometry.AffineStratification`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/Defs.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/Defs.lean#L52).

> A locally finite stratification of `X` with affine reduced induced strata
> and affine inclusions into `X`.

```lean
structure AffineStratification (X : Scheme.{u}) (I : Type v) [PartialOrder I]
```

## Tag 0F2T, a lemma

[Tag 0F2T](https://stacks.math.columbia.edu/tag/0F2T) in the Stacks Project.

**`AlgebraicGeometry.exists_affineStratification_fin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/Reindex.lean, line 457](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/Reindex.lean#L457).

> A finite affine stratification can be reindexed by the interval from zero
> to the length of its indexing poset.

```lean
theorem exists_affineStratification_fin {X : Scheme.{u}}
    {I : Type v} [PartialOrder I] [Finite I]
    (s : AffineStratification X I) (n : ℕ)
    (hn : (Order.krullDim I = n) ∨ (IsEmpty I ∧ n = 0)) :
    Nonempty (AffineStratification X (Fin (n + 1)))
```

## Tag 0F2U, a lemma

[Tag 0F2U](https://stacks.math.columbia.edu/tag/0F2U) in the Stacks Project.

**`AlgebraicGeometry.hasFiniteAffineStratification_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/FiniteExistence.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/FiniteExistence.lean#L92).

> A scheme has an affine stratification indexed by a finite poset if and only if it is
> quasi-compact and quasi-separated.

```lean
theorem hasFiniteAffineStratification_iff (X : Scheme.{u}) :
    HasFiniteAffineStratification.{u, v} X ↔ (CompactSpace X ∧ QuasiSeparatedSpace X)
```

## Tag 0F2V, a definition

[Tag 0F2V](https://stacks.math.columbia.edu/tag/0F2V) in the Stacks Project.

**`AlgebraicGeometry.affineStratificationNumber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/Defs.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/Defs.lean#L69).

> The least `n` admitting an affine stratification of `X` with strata
> indexed by `0, …, n`.

```lean
noncomputable def affineStratificationNumber (X : Scheme.{u}) : ℕ
```

## Tag 0F2W, a lemma

[Tag 0F2W](https://stacks.math.columbia.edu/tag/0F2W) in the Stacks Project.

**`AlgebraicGeometry.affineStratificationNumber_le_of_isOpenCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/CoverBound.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/CoverBound.lean#L148).

> **[Stacks, Tag 0F2W].** A separated scheme with an open covering by `n + 1` affine opens
> has affine stratification number at most `n`.

```lean
theorem affineStratificationNumber_le_of_isOpenCover (X : Scheme.{u}) [X.IsSeparated] {n : ℕ}
    (U : Fin (n + 1) → X.Opens) (hU : IsOpenCover U) (hUaff : ∀ i, IsAffineOpen (U i)) :
    affineStratificationNumber X ≤ n
```

## Tag 0F2X, a lemma

[Tag 0F2X](https://stacks.math.columbia.edu/tag/0F2X) in the Stacks Project.

**`AlgebraicGeometry.affineStratificationNumber_le_of_topologicalKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/DimensionBound.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/DimensionBound.lean#L298).

> **[Stacks, Tag 0F2X].** A Noetherian scheme of finite dimension `d` has affine
> stratification number at most `d`.

```lean
theorem affineStratificationNumber_le_of_topologicalKrullDim (X : Scheme.{u}) [IsNoetherian X]
    (d : ℕ) (hdim : topologicalKrullDim X ≤ (d : WithBot ℕ∞)) :
    affineStratificationNumber X ≤ d
```

**`AlgebraicGeometry.nonempty_affineStratification_of_topologicalKrullDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/DimensionStratification.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/DimensionStratification.lean#L44). The attribute's comment: “an affine stratification indexed by 0, …, d exists”.

> A Noetherian scheme of dimension at most `d` has an affine stratification indexed by
> `0, …, d`; that is, its affine stratification number is at most `d` in the sense of
> [Stacks, Tag 0F2V].

```lean
theorem nonempty_affineStratification_of_topologicalKrullDim_le (X : Scheme.{u})
    [IsNoetherian X] (d : ℕ) (hdim : topologicalKrullDim X ≤ (d : WithBot ℕ∞)) :
    Nonempty (AffineStratification X (Fin (d + 1)))
```

## Tag 0F2Y, a proposition

[Tag 0F2Y](https://stacks.math.columbia.edu/tag/0F2Y) in the Stacks Project.

**`AlgebraicGeometry.isZero_cohomology_of_affineStratificationNumber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/CohomologyVanishingProof.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/CohomologyVanishingProof.lean#L253).

> **[Stacks, Tag 0F2Y].** Let `X` be a nonempty quasi-compact quasi-separated scheme with
> affine stratification number `n`. Then `Hᵖ(X, F) = 0` for every `p > n` and every quasi-coherent
> `𝒪_X`-module `F`.

```lean
theorem isZero_cohomology_of_affineStratificationNumber (X : Scheme.{u}) [Nonempty X]
    [CompactSpace X] [QuasiSeparatedSpace X] (F : X.Modules) [F.IsQuasicoherent] (p : ℕ)
    (hp : affineStratificationNumber X < p) :
    IsZero (Hgroup X.ringCatSheaf ⊤ p F)
```

## Tag 0F2Z, an example

[Tag 0F2Z](https://stacks.math.columbia.edu/tag/0F2Z) in the Stacks Project.

**`AlgebraicGeometry.affineStratificationNumber_proj_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/ProjectiveSpace.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/ProjectiveSpace.lean#L85). The attribute's comment: “the upper bound”.

> **[Stacks, Tag 0F2Z], the upper bound.** The affine stratification number of `ℙⁿ_k` is at
> most `n`: projective space is separated and the `n + 1` standard coordinate charts are an affine
> open covering.

```lean
theorem affineStratificationNumber_proj_le (k : Type u) [Field k] (n : ℕ) :
    affineStratificationNumber (Proj (polyGrading k n)) ≤ n
```

**`AlgebraicGeometry.le_affineStratificationNumber_proj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/ProjectiveSpace.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/ProjectiveSpace.lean#L154). The attribute's comment: “the lower bound”.

> **[Stacks, Tag 0F2Z], the lower bound.** The affine stratification number of `ℙⁿ_k` is at
> least `n`: `Hⁿ(ℙⁿ_k, 𝒪(-n-1))` is nonzero, while [Stacks, Tag 0F2Y] makes the cohomology of a
> quasi-coherent module vanish above the affine stratification number.

```lean
theorem le_affineStratificationNumber_proj (k : Type u) [Field k] (n : ℕ) :
    n ≤ affineStratificationNumber (Proj (polyGrading k n))
```

**`AlgebraicGeometry.affineStratificationNumber_proj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/ProjectiveSpace.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/AffineStratification/ProjectiveSpace.lean#L168). The attribute's comment: “the equality”.

> **[Stacks, Tag 0F2Z].** The affine stratification number of `n`-dimensional projective space
> over a field is exactly `n`.

```lean
theorem affineStratificationNumber_proj (k : Type u) [Field k] (n : ℕ) :
    affineStratificationNumber (Proj (polyGrading k n)) = n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.73, Tag 0F2R](https://stacks.math.columbia.edu/tag/0F2R)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

---
declaration: section
origin: cited
lean: topologicalKrullDim, topologicalKrullDimAt, AlgebraicGeometry.topologicalKrullDim_eq_iSup_krullDimOfRing_stalk, TopologicalSpace.topologicalKrullDim_eq_iSup_localKrullDim, TopologicalSpace.topologicalKrullDimAt_eq_localKrullDim, AlgebraicGeometry.codimension_eq_ringKrullDim_stalk, AlgebraicGeometry.isArtinianRing_stalk_of_topologicalKrullDim_le_zero, AlgebraicGeometry.isIso_sigmaFromSpecStalk_of_topologicalKrullDim_le_zero
statement: formalized
proof: formalized
---

# 28.10 Dimension

Section 28.10 of the Stacks Project, [Tag 04MS](https://stacks.math.columbia.edu/tag/04MS). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04MT, a definition

[Tag 04MT](https://stacks.math.columbia.edu/tag/04MT) in the Stacks Project.

Declarations registered for the tag:

- [`topologicalKrullDim`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=topologicalKrullDim#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean#L232) (StacksFrontier): “dimension of a scheme”. References: EGA 0 (14.1.2).
- [`topologicalKrullDimAt`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Dimension/Krull.lean#L49), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean#L234) (StacksFrontier): “dimension of a scheme at a point”.

## Tag 04MU, a lemma

[Tag 04MU](https://stacks.math.columbia.edu/tag/04MU) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDim_eq_iSup_krullDimOfRing_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean#L78). The attribute's comment: “dimension\_sup\_local\_rings”. References: EGA IV (5.1.4).

> The dimension of a scheme is the supremum of the Krull dimensions of its local rings.

```lean
theorem topologicalKrullDim_eq_iSup_krullDimOfRing_stalk (X : Scheme.{u}) :
    topologicalKrullDim X = ⨆ x : X, ringKrullDim (X.presheaf.stalk x)
```

Declarations registered for the tag:

- [`TopologicalSpace.topologicalKrullDim_eq_iSup_localKrullDim`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Dimension/LocalKrullDim.lean#L142), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean#L235) (StacksFrontier): “dimension\_sup\_at\_points”.
- [`TopologicalSpace.topologicalKrullDimAt_eq_localKrullDim`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Dimension/LocalKrullDim.lean#L81), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean#L237) (StacksFrontier): “dimension\_sup\_at\_points”.

## Tag 02IZ, a lemma

[Tag 02IZ](https://stacks.math.columbia.edu/tag/02IZ) in the Stacks Project.

**`AlgebraicGeometry.codimension_eq_ringKrullDim_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/CodimensionLocalRing.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/CodimensionLocalRing.lean#L67). References: EGA IV (21.6.2), “partial”; EGA IV (5.1.2); EGA IV (5.1.3), “special case”.

> **Stacks 02IZ**.
> Let `X` be a scheme, let `Y ⊆ X` be an irreducible closed subset and let `ξ` be the generic
> point of `Y`. Then the codimension of `Y` in `X`, in the sense of Stacks 02I3, is the Krull
> dimension of the local ring `𝒪_{X, ξ}`.

```lean
theorem codimension_eq_ringKrullDim_stalk {X : Scheme.{u}} (Y : IrreducibleCloseds X) (ξ : X)
    (hξ : IsGenericPoint ξ (Y : Set X)) :
    (codimension Y : WithBot ℕ∞) = ringKrullDim (X.presheaf.stalk ξ)
```

## Tag 0AAX, a lemma

[Tag 0AAX](https://stacks.math.columbia.edu/tag/0AAX) in the Stacks Project.

**`AlgebraicGeometry.isArtinianRing_stalk_of_topologicalKrullDim_le_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean#L95). The attribute's comment: “the summands are spectra of Artinian local rings”.

> The local rings of a locally Noetherian scheme of dimension at most zero are Artinian.

```lean
lemma isArtinianRing_stalk_of_topologicalKrullDim_le_zero
    (X : Scheme.{u}) [IsLocallyNoetherian X]
    (hX : topologicalKrullDim X ≤ 0) (x : X) :
    IsArtinianRing (X.presheaf.stalk x)
```

**`AlgebraicGeometry.isIso_sigmaFromSpecStalk_of_topologicalKrullDim_le_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean#L108). The attribute's comment: “the disjoint-union decomposition”.

> A locally Noetherian scheme of dimension at most zero is the coproduct of the spectra of its
> local rings.

```lean
lemma isIso_sigmaFromSpecStalk_of_topologicalKrullDim_le_zero
    (X : Scheme.{u}) [IsLocallyNoetherian X]
    (hX : topologicalKrullDim X ≤ 0) :
    IsIso (sigmaFromSpecStalk X)
```

## Tag 0CKV, a lemma

[Tag 0CKV](https://stacks.math.columbia.edu/tag/0CKV) in the Stacks Project.

**`AlgebraicGeometry.separation_tfae_of_topologicalKrullDim_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/DimensionZero.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/DimensionZero.lean#L195). The attribute's comment: “separation\_equivalences”.

> **Stacks Project, Tag 0CKV.** For a scheme of dimension zero, quasi-separatedness,
> separatedness, Hausdorffness of the underlying space, and closedness of every affine open are
> equivalent.

```lean
theorem separation_tfae_of_topologicalKrullDim_eq_zero (X : Scheme.{u})
    (hX : topologicalKrullDim X = 0) :
    List.TFAE [
      QuasiSeparatedSpace X,
      X.IsSeparated,
      T2Space X,
      ∀ U : X.Opens, IsAffineOpen U → IsClosed (U : Set X)]
```

**`AlgebraicGeometry.connectedComponent_eq_singleton_of_topologicalKrullDim_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/DimensionZero.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/DimensionZero.lean#L257). The attribute's comment: “connected\_components”.

> **Stacks Project, Tag 0CKV.** The connected components of a quasi-separated zero-dimensional
> scheme are its points.

```lean
theorem connectedComponent_eq_singleton_of_topologicalKrullDim_eq_zero (X : Scheme.{u})
    [QuasiSeparatedSpace X] (hX : topologicalKrullDim X = 0) (x : X) :
    connectedComponent x = {x}
```

**`AlgebraicGeometry.isAffineOpen_of_isCompact_of_topologicalKrullDim_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/DimensionZero.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/DimensionZero.lean#L343). The attribute's comment: “quasicompact\_open\_affine”.

> **Stacks Project, Tag 0CKV.** Every quasi-compact open subset of a quasi-separated scheme of
> dimension zero is affine.

```lean
theorem isAffineOpen_of_isCompact_of_topologicalKrullDim_eq_zero (X : Scheme.{u})
    [QuasiSeparatedSpace X] (hX : topologicalKrullDim X = 0) (U : X.Opens)
    (hU : IsCompact (U : Set X)) : IsAffineOpen U
```

**`AlgebraicGeometry.isAffine_of_topologicalKrullDim_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/DimensionZero.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/DimensionZero.lean#L352). The attribute's comment: “quasicompact\_affine”.

> **Stacks Project, Tag 0CKV.** A quasi-compact, quasi-separated scheme of dimension zero is
> affine.

```lean
theorem isAffine_of_topologicalKrullDim_eq_zero (X : Scheme.{u}) [CompactSpace X]
    [QuasiSeparatedSpace X] (hX : topologicalKrullDim X = 0) : IsAffine X
```

## Tag 0H7C, a lemma

[Tag 0H7C](https://stacks.math.columbia.edu/tag/0H7C) in the Stacks Project.

**`AlgebraicGeometry.topologicalKrullDimAt_eq_zero_iff_isIsolatedPoint`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Dimension.lean#L181). References: EGA 0 (14.1.10), “loc. Noetherian scheme”.

> A point of a locally Noetherian scheme has local dimension zero exactly when it is an
> isolated point.

```lean
public lemma topologicalKrullDimAt_eq_zero_iff_isIsolatedPoint
    (X : Scheme) [IsLocallyNoetherian X] (x : X) :
    topologicalKrullDimAt X x = 0 ↔ IsIsolatedPoint x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.10, Tag 04MS](https://stacks.math.columbia.edu/tag/04MS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

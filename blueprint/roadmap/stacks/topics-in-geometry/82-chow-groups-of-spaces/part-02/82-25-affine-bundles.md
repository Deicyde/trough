---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFlatPullbackSurjective_of_isQuasiCompact_of_hasAffineSpaceFibres, AlgebraicGeometry.Space.bijective_flatPullbackChowMapCanonical_vectorBundle
statement: formalized
proof: formalized
---

# 82.25 Affine bundles

Section 82.25 of the Stacks Project, [Tag 0ERF](https://stacks.math.columbia.edu/tag/0ERF). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ERG, a lemma

[Tag 0ERG](https://stacks.math.columbia.edu/tag/0ERG) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlatPullbackSurjective_of_isQuasiCompact_of_hasAffineSpaceFibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackSurjectiveAffineFibres.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullbackSurjectiveAffineFibres.lean#L132).

> **Stacks 0ERG.** In Situation 0EDT let `X, Y/B` be good and let `f : X → Y` be a
> quasi-compact morphism over the base, flat of relative dimension `r`, with
> `X_y ≅ 𝐀^r_{κ(y)}` for every `y ∈ |Y|`. Then `f^* : CH_k(Y) → CH_{k+r}(X)` is surjective: for
> every `k ∈ ℤ` and every `α ∈ Z_{k+r}(X)` there is `β ∈ Z_k(Y)` with `f^*β - α` rationally
> equivalent to zero, as a locally finite sum of principal divisors at the canonical embeddings of
> Stacks 0ENK.

```lean
theorem isFlatPullbackSurjective_of_isQuasiCompact_of_hasAffineSpaceFibres
    (hqc : IsQuasiCompact D.site D.base D.base_mem f) (hfib : HasAffineSpaceFibres D sY hY f r)
    (k : ℤ) : IsFlatPullbackSurjective D sX hX sY hY f hbase r hflat hr k
```

## Tag 0ERH, a lemma

[Tag 0ERH](https://stacks.math.columbia.edu/tag/0ERH) in the Stacks Project.

**`AlgebraicGeometry.Space.bijective_flatPullbackChowMapCanonical_vectorBundle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/LineBundleFlatPullbackChow.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/LineBundleFlatPullbackChow.lean#L340).

> **Stacks 0ERH.** In Situation 0EDT let `X/B` be good, let `ℒ` be a finite locally free
> `𝒪_X`-module of rank one and let `p : L = \underline{Spec}(Sym^*(ℒ)) → X` be its line bundle,
> flat of relative dimension one. Then the flat pullback `p^* : CH_k(X) → CH_{k+1}(L)` of
> Stacks 0EQB, on the Chow groups of Stacks 0EQ6 at the canonical embeddings of Stacks 0ENK, is an
> isomorphism for every `k`.

```lean
theorem bijective_flatPullbackChowMapCanonical_vectorBundle (k : ℤ) :
    Function.Bijective (flatPullbackChowMapCanonical.{u + 1} D _
      (isGood_vectorBundle D W F sW hW) sW hW
      (vectorBundleProjection D.site D.base D.base_mem W F).hom rfl 1
      (isFlat_vectorBundleProjection D.site D.base D.base_mem W F)
      (hasRelativeDimension_vectorBundleProjection D.site D.base D.base_mem W F 1) k (k + 1)
      (by push_cast; rfl))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.25, Tag 0ERF](https://stacks.math.columbia.edu/tag/0ERF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

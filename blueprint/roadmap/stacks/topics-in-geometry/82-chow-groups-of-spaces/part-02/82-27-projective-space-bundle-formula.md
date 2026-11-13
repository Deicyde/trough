---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.chowClassCanonical_properCyclePushforward_firstChernCapPow_flatPullback_projBundle_eq_zero, AlgebraicGeometry.Space.chowClassCanonical_properCyclePushforward_firstChernCapPow_flatPullback_projBundle, AlgebraicGeometry.Space.bijective_projectiveBundleFormulaMap, AlgebraicGeometry.Space.bijective_flatPullbackChowMapCanonical_vectorBundleProjection
statement: formalized
proof: formalized
---

# 82.27 Projective space bundle formula

Section 82.27 of the Stacks Project, [Tag 0ERT](https://stacks.math.columbia.edu/tag/0ERT). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ERU, a lemma

[Tag 0ERU](https://stacks.math.columbia.edu/tag/0ERU) in the Stacks Project.

**`AlgebraicGeometry.Space.chowClassCanonical_properCyclePushforward_firstChernCapPow_flatPullback_projBundle_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProjectiveBundleTopPower.lean, line 471](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProjectiveBundleTopPower.lean#L471). The attribute's comment: “the vanishing for s < r - 1, read on a cycle representing α, in the Chow group of Stacks 0EQ6 at the canonical embeddings”.

> **Stacks 0ERU, the vanishing, in the Chow group at the canonical embeddings.** Let `ℰ` be a
> finite locally free `𝒪_X`-module of rank `n + 1` on a good algebraic space `X/B` and
> `(π : P → X, 𝒪_P(1))` its projective bundle. For `s < n` and every `k`-cycle `α` on `X`, the class
> of `π_*(c₁(𝒪_P(1))^s ∩ π^*α)` in `CH_{k+n-s}(X)` is zero, the Chow group being that of Stacks 0EQ6
> at the canonical embeddings of Stacks 0ENK.

```lean
theorem chowClassCanonical_properCyclePushforward_firstChernCapPow_flatPullback_projBundle_eq_zero
    (s : ℕ) (hs : s < n) (k m : ℤ) (h : k + n = m + s) (α : CycleGroup D sX k) :
    chowClassCanonical.{u + 1} D sX hX m
        (properCyclePushforward D _ (isGood_projectiveBundleProj_comp D sX hX E hfree) sX hX rfl
          (isProper_projectiveBundleProj (X := ⟨X, hX.1⟩) E hfree).2.1.2 m
          (firstChernCapPowCycleMap D _ (isGood_projectiveBundleProj_comp D sX hX E hfree)
            (projectiveBundleTwist (X := ⟨X, hX.1⟩) E hfree).obj
            (isInvertibleModule_projectiveBundleTwist (X := ⟨X, hX.1⟩) E hfree) s m
            (flatPullbackMap D _ (isGood_projectiveBundleProj_comp D sX hX E hfree) sX hX
              (projectiveBundleProj (X := ⟨X, hX.1⟩) E hfree).hom rfl n
              (isFlat_projectiveBundleProj (X := ⟨X, hX.1⟩) E n hr hfree)
              (hasRelativeDimension_projectiveBundleProj (X := ⟨X, hX.1⟩) E n hr hfree) k
              (m + s) h α))) = 0
```

**`AlgebraicGeometry.Space.chowClassCanonical_properCyclePushforward_firstChernCapPow_flatPullback_projBundle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProjectiveBundleTopPower.lean, line 494](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProjectiveBundleTopPower.lean#L494). The attribute's comment: “the top power s = r - 1, read on a cycle representing α, in the Chow group of Stacks 0EQ6 at the canonical embeddings”.

> **Stacks 0ERU, the top power, in the Chow group at the canonical embeddings.** Let `ℰ` be a
> finite locally free `𝒪_X`-module of rank `n + 1` on a good algebraic space `X/B` and
> `(π : P → X, 𝒪_P(1))` its projective bundle. For every `k`-cycle `α` on `X`, the class of
> `π_*(c₁(𝒪_P(1))^n ∩ π^*α)` in `CH_k(X)` is the class of `α`, the Chow group being that of
> Stacks 0EQ6 at the canonical embeddings of Stacks 0ENK.

```lean
theorem chowClassCanonical_properCyclePushforward_firstChernCapPow_flatPullback_projBundle
    (k : ℤ) (α : CycleGroup D sX k) :
    chowClassCanonical.{u + 1} D sX hX k
        (properCyclePushforward D _ (isGood_projectiveBundleProj_comp D sX hX E hfree) sX hX rfl
          (isProper_projectiveBundleProj (X := ⟨X, hX.1⟩) E hfree).2.1.2 k
          (firstChernCapPowCycleMap D _ (isGood_projectiveBundleProj_comp D sX hX E hfree)
            (projectiveBundleTwist (X := ⟨X, hX.1⟩) E hfree).obj
            (isInvertibleModule_projectiveBundleTwist (X := ⟨X, hX.1⟩) E hfree) n k
            (flatPullbackMap D _ (isGood_projectiveBundleProj_comp D sX hX E hfree) sX hX
              (projectiveBundleProj (X := ⟨X, hX.1⟩) E hfree).hom rfl n
              (isFlat_projectiveBundleProj (X := ⟨X, hX.1⟩) E n hr hfree)
              (hasRelativeDimension_projectiveBundleProj (X := ⟨X, hX.1⟩) E n hr hfree) k
              (k + n) rfl α))) =
      chowClassCanonical.{u + 1} D sX hX k α
```

## Tag 0ERV, a lemma

[Tag 0ERV](https://stacks.math.columbia.edu/tag/0ERV) in the Stacks Project.

**`AlgebraicGeometry.Space.bijective_projectiveBundleFormulaMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProjectiveBundleFormulaBijective.lean, line 426](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProjectiveBundleFormulaBijective.lean#L426).

> **Stacks 0ERV: the projective space bundle formula.** Let `X` be a good algebraic space over
> the base of the theory of cycles, `ℰ` a finite locally free `𝒪_X`-module of rank `r` and
> `(π : P = 𝐏(ℰ) → X, 𝒪_P(1))` its projective bundle. The map
> `⊕_{i=0}^{r-1} CH_{k+i}(X) → CH_{k+r-1}(P)`,
> `(α_0, …, α_{r-1}) ↦ π^*α_0 + c₁(𝒪_P(1)) ∩ π^*α_1 + … + c₁(𝒪_P(1))^{r-1} ∩ π^*α_{r-1}`,
> is an isomorphism.

```lean
theorem bijective_projectiveBundleFormulaMap
    (F : Modules.{u, u} D.site D.base D.base_mem X.1 X.2) (r : ℕ)
    (hF : RingedSite.IsFiniteLocallyFreeOfRank
      (smallEtaleRingedSite D.site D.base D.base_mem X.1 X.2) F r) (k : ℤ) :
    Function.Bijective (projectiveBundleFormulaMap D sX hX F r hF k)
```

## Tag 0ERW, a lemma

[Tag 0ERW](https://stacks.math.columbia.edu/tag/0ERW) in the Stacks Project.

**`AlgebraicGeometry.Space.bijective_flatPullbackChowMapCanonical_vectorBundleProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/VectorBundleChowPullbackBijective.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/VectorBundleChowPullbackBijective.lean#L44).

> **Stacks 0ERW.** In Situation 0EDT let `X/B` be good, let `ℰ` be a finite locally free
> `𝒪_X`-module of rank `r` and let `p : E = Spec(Sym^*(ℰ)) → X` be the associated vector bundle.
> Then `p^* : CH_k(X) → CH_{k+r}(E)` is an isomorphism for all `k`.

```lean
theorem bijective_flatPullbackChowMapCanonical_vectorBundleProjection (k : ℤ) :
    letI := AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.isFiniteLocallyFree F r
    Function.Bijective (flatPullbackChowMapCanonical.{u + 1} D
      ((vectorBundleProjection D.site D.base D.base_mem W F).hom ≫ sW)
      (isGood_vectorBundle D W F sW hW) sW hW
      (vectorBundleProjection D.site D.base D.base_mem W F).hom
      rfl r (isFlat_vectorBundleProjection D.site D.base D.base_mem W F)
      (hasRelativeDimension_vectorBundleProjection D.site D.base D.base_mem W F r) k
      (k + (r : ℤ)) rfl)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.27, Tag 0ERT](https://stacks.math.columbia.edu/tag/0ERT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

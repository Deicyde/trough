---
declaration: section
origin: cited
lean: OAI.Problem358.one_third_stability, OAI.Problem358.one_third_exponent_is_sharp
statement: formalized
proof: formalized
---

# 374. Sharp one-third stability of Brenier maps

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For uniform source measure *ρ* on a compact convex body with interior in dimension at least two, quadratic optimal transport maps satisfy $\|T_\mu-T_\nu\|_{L^2(\rho)}\le C W_2(\mu,\nu)^{1/3}$ uniformly over targets in a fixed compact set. The exponent is sharp, even for three-atom targets, disproving Letrouit's conjectured square-root bound.

## Sharp One-Third Stability of Brenier Maps

For the uniform probability measure *ρ* on a compact convex body in ℝ$^{d}$, *d* ≥ 2, quadratic optimal transport maps are one-third Hölder continuous in $L^2(\rho)$ with respect to the target's 2-Wasserstein distance. The constant is uniform over all targets supported in a fixed compact set, and the exponent is optimal. A three-atom family on a fixed cube disproves Letrouit's conjectured uniform square-root estimate.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-One-Third-Stability-of-Brenier-Maps-September-25-2026/article.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves one-third Hölder stability of Brenier maps from the uniform measure on a compact convex body with nonempty interior in $\mathbb R^d$, for every $d\ge2$. For targets supported in one fixed nonempty compact set, the $L^2$ distance between the unique quadratic optimal maps is at most a constant times the one-third power of the targets' $2$-Wasserstein distance. The constant is uniform over those targets.

It also proves optimality of the exponent: on a fixed cube, pairs of three-atom target measures violate every analogous bound with exponent greater than $1/3$. In particular, the conjectured uniform square-root estimate fails.

## Lean: One-third stability of Brenier maps and sharpness

```lean
theorem one_third_stability :
    ∀ (dimension : ℕ) (source container : Set (E dimension)),
      2 ≤ dimension → IsCompact source → Convex ℝ source → (interior source).Nonempty →
      IsCompact container → container.Nonempty →
      ∃ constant : ℝ, 0 ≤ constant ∧
        ∀ (first second : Measure (E dimension)),
          IsProbabilityMeasure first → IsProbabilityMeasure second →
          IsSupported first container → IsSupported second container →
          ∃ firstMap secondMap : E dimension → E dimension,
            IsUniqueQuadraticOptimalMap (uniformMeasure source) first firstMap ∧
            IsUniqueQuadraticOptimalMap (uniformMeasure source) second secondMap ∧
            mapL2Dist (uniformMeasure source) firstMap secondMap ≤
              constant * Real.rpow (wasserstein2 first second) (1 / 3 : ℝ)
```

Stated in [Brenier.lean, line 73](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Brenier.lean#L73). Proved in [lean/OAI/Analysis/Brenier/Stability.lean, line 20](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Brenier/Stability.lean#L20).

```lean
theorem one_third_exponent_is_sharp :
    ∀ (dimension : ℕ), 2 ≤ dimension → ∀ exponent : ℝ, (1 / 3 : ℝ) < exponent →
      ∀ constant : ℝ, 0 < constant →
        ∃ (first second : Measure (E dimension)) (firstMap secondMap : E dimension → E dimension),
          IsProbabilityMeasure first ∧ IsProbabilityMeasure second ∧
          IsSupported first (cube dimension) ∧ IsSupported second (cube dimension) ∧
          HasExactlyThreeAtoms first (cube dimension) ∧
          HasExactlyThreeAtoms second (cube dimension) ∧
          first ≠ second ∧
          IsUniqueQuadraticOptimalMap (uniformMeasure (cube dimension)) first firstMap ∧
          IsUniqueQuadraticOptimalMap (uniformMeasure (cube dimension)) second secondMap ∧
          0 < wasserstein2 first second ∧
          constant * Real.rpow (wasserstein2 first second) exponent <
            mapL2Dist (uniformMeasure (cube dimension)) firstMap secondMap
```

Stated in [Brenier.lean, line 88](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Brenier.lean#L88). Proved in [lean/OAI/Analysis/Brenier/Stability.lean, line 48](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Brenier/Stability.lean#L48).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/374.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/374.md)

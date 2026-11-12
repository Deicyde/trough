---
declaration: section
origin: cited
lean: OAI.PlanarFPP.manuscriptMain, OAI.GammaFPP.gamma_differentiability
statement: formalized
proof: formalized
---

# 212. Planar first-passage geometry and the absence of bigeodesics

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that planar first-passage percolation has no doubly infinite geodesic for iid nonnegative nonatomic edge weights when the minimum of four weights has finite second moment. For exponential weights, the limit shape is strictly convex with $C^{1}$ boundary. Differentiability also holds for every Gamma law with positive shape and rate.

## No bigeodesics in planar first-passage percolation

We prove that planar first-passage percolation with independent identically distributed nonnegative nonatomic edge weights has almost surely no doubly infinite geodesic, provided the minimum of four independent weights has finite second moment. This resolves the planar no-bigeodesics conjecture under that moment assumption. The conclusion rules out all bigeodesics simultaneously, without any regularity assumption on the limit shape.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/No-bigeodesics-in-planar-first-passage-percolation-September-24-2026/main.pdf).

## Strict convexity and differentiability of the planar exponential first-passage limit shape

We prove that the limit shape of undirected nearest-neighbor first-passage percolation on ℤ$^{2}$ with independent exponential edge weights is strictly convex and has a $C^{1}$ boundary. This resolves the strict convexity and differentiability conjectures for the planar exponential model. More generally, we prove differentiability of the time-constant norm for every Gamma edge-weight law with positive shape and rate.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strict-convexity-and-differentiability-of-the-planar-exponential-first-passage-limit-shape-September-24-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves differentiability of the planar first-passage time-constant norm for independent Gamma edge weights of every positive shape and rate. The norm is differentiable away from the origin, and its unit sphere has a $C^1$ boundary. This includes the exponential model, for which the linked statement also gives a unique supporting line at every boundary point.

The paper also claims strict convexity for the exponential limit shape. Strict convexity is outside these selected differentiability statements.

## Lean: Differentiability of the exponential first-passage limit shape

Stated in [PlanarFirstPassage.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PlanarFirstPassage.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem manuscriptMain (Ω : Type) [MeasurableSpace Ω] (P : Measure Ω) (τ : Edge → Ω → ℝ)
    (henv : ExponentialEnvironment P τ) :
    ∃ μ : Plane → ℝ, TimeConstantNorm μ ∧ IsTimeConstant P τ μ ∧
      DifferentiableAwayFromOrigin μ ∧ UniqueNormalizedSupports μ ∧ C1UnitSphere μ ∧
      (∀ v ∈ frontier {z | μ z ≤ 1}, ∃! L : Set Plane,
        ∃ g : Plane →L[ℝ] ℝ, g ≠ 0 ∧ (∀ z, μ z ≤ 1 → g z ≤ g v) ∧ L={z | g z=g v}) ∧
      (∀ v ∈ frontier {z | μ z ≤ 1}, HasC1CurveChart (frontier {z | μ z ≤ 1}) v)
```

Proved in [lean/OAI/Probability/FirstPassage/BoundaryCurve.lean, line 65](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/FirstPassage/BoundaryCurve.lean#L65).

## Lean: Differentiability for every positive Gamma edge-weight law

Stated in [GammaPassage.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GammaPassage.lean).

```lean
theorem gamma_differentiability : GammaDifferentiabilityTarget
```

Proved in [lean/OAI/Probability/GammaPassage/Differentiability.lean, line 20](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/GammaPassage/Differentiability.lean#L20).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/212.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/212.md)

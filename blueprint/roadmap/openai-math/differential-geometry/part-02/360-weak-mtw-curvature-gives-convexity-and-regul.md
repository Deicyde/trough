---
declaration: section
origin: cited
lean: OAI.WeakMTWTransport.uniform_biHolder_transport
statement: formalized
---

# 360. Weak MTW curvature gives convexity and regular optimal transport

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

On every closed connected Riemannian manifold of dimension at least two satisfying weak Ma–Trudinger–Wang curvature, all tangent injectivity domains are convex, resolving Villani’s conjecture in this setting. For squared-distance transport between measurable probability densities bounded above and away from zero, the optimal map and its inverse are Hölder continuous.

## Global Support and Convex Injectivity Domains under Weak MTW

We prove that weak Ma–Trudinger–Wang curvature on a smooth, connected, compact Riemannian manifold of dimension at least two without boundary implies convexity of every tangent injectivity domain, resolving Villani's conjecture in this setting. Conjugate cut points are allowed. More generally, every ordinary subgradient of a squared-distance cost potential is a minimizing velocity with a global supporting mountain. No density hypothesis is used.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Global-Support-and-Convex-Injectivity-Domains-under-Weak-MTW-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## Uniform Bi-Holder Transport from Weak MTW

We prove that the weak Ma–Trudinger–Wang condition on a fixed smooth connected compact boundaryless Riemannian manifold of dimension at least two implies a common Hölder estimate for optimal transport maps and their inverses over the entire class of probability densities with fixed positive upper and lower bounds. The maps have homeomorphic representatives, conjugate cut points are allowed, and no density regularity is assumed.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Uniform-Bi-Holder-Transport-from-Weak-MTW-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

On a compact connected smooth Riemannian manifold of dimension at least two, the formalized result proves that weak MTW curvature implies convexity of every open tangent injectivity domain. Prior convexity or nonfocality is not assumed. Additional formalized results give global support at ordinary subgradients, compact convex lifted gap sections with the stated diameter bound, and scale and local-injectivity estimates for finite target families. The latter finite-family result does not cover the paper's arbitrary-potential local-injectivity assertion.

The formalized result gives uniform bi-Hölder optimal transport for squared-distance cost on each fixed compact connected smooth Riemannian manifold of dimension at least two satisfying weak MTW. For probability densities between fixed positive lower and finite upper bounds, one exponent and constant work for every pair of densities. The optimal map is a homeomorphism, is unique almost everywhere, and both it and its inverse satisfy the global Hölder bound. The constants are uniform over the density class on the fixed manifold, not over varying metrics.

## Lean: Convex injectivity domains under weak MTW

Stated in [WeakMTWGlobalSupport.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/WeakMTWGlobalSupport.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem current_main_convexity
    {n : ℕ} (hn : 2 ≤ n) {M : Type*}
    [MetricSpace M] [ChartedSpace (WeakMTW.Model n) M]
    [IsManifold (WeakMTW.model n) ∞ M]
    [CompactSpace M] [ConnectedSpace M]
    [RiemannianBundle (fun x : M => TangentSpace (WeakMTW.model n) x)]
    [IsContMDiffRiemannianBundle (WeakMTW.model n) ∞ (WeakMTW.Model n)
      (fun x : M => TangentSpace (WeakMTW.model n) x)]
    [IsRiemannianManifold (WeakMTW.model n) M]
    (hmtw : WeakMTW.HasWeakMTW (n := n) (M := M)) :
    WeakMTW.MainConvexity (n := n) (M := M)
```

Its proof is in [lean/OAI/Geometry/WeakMTW/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/WeakMTW/Main.lean) or a file it imports further down, which this chapter does not read.

## Lean: Uniform bi-Hölder optimal transport

Stated in [BiholderTransport.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BiholderTransport.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem uniform_biHolder_transport
    {n : ℕ} (hn : 2 ≤ n) {M : Type*}
    [MetricSpace M] [CompactSpace M] [ConnectedSpace M]
    [ChartedSpace (Model n) M] [IsManifold 𝓘(ℝ, Model n) ∞ M]
    [RiemannianBundle (fun x : M => TangentSpace 𝓘(ℝ, Model n) x)]
    [IsContMDiffRiemannianBundle 𝓘(ℝ, Model n) ∞ (Model n)
      (fun x : M => TangentSpace 𝓘(ℝ, Model n) x)]
    [IsRiemannianManifold 𝓘(ℝ, Model n) M]
    [MeasurableSpace M] [BorelSpace M]
    (hmtw : WeakMTW (n := n) (M := M))
    (lam cap : ℝ) (hlam : 0 < lam) (hcap : lam ≤ cap)
    (hclass : ∃ rho : M → ℝ, AdmissibleDensity (metricVolume n) lam cap rho) :
    ∃ alpha C : ℝ, 0 < alpha ∧ alpha ≤ 1 ∧ 0 ≤ C ∧
      ∀ rho0 rho1 : M → ℝ,
        AdmissibleDensity (metricVolume n) lam cap rho0 →
        AdmissibleDensity (metricVolume n) lam cap rho1 →
        ∃ T : M ≃ₜ M,
          IsOptimalMap (metricVolume n) rho0 rho1 T ∧
          (∀ S : M → M, IsOptimalMap (metricVolume n) rho0 rho1 S →
            S =ᵐ[densityMeasure (metricVolume n) rho0] T) ∧
          BiHolderEstimate alpha C T
```

Proved in [lean/OAI/Analysis/BiholderTransport/Main.lean, line 27](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/BiholderTransport/Main.lean#L27).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/360.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/360.md)

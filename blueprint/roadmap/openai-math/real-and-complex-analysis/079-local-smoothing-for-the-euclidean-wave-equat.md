---
declaration: section
origin: cited
lean: OAI.Analysis.Fourier.LocalSmoothing.Comparator.euclidean_local_smoothing, OAI.Analysis.Fourier.LocalSmoothing.Comparator.bochner_riesz, OAI.Analysis.Fourier.LocalSmoothing.Comparator.spherical_restriction, OAI.Analysis.Fourier.LocalSmoothing.Comparator.kakeya_maximal, OAI.Analysis.Fourier.LocalSmoothing.Comparator.kakeya, OAI.Analysis.Fourier.LocalSmoothing.Comparator.stein_square
statement: formalized
proof: formalized
---

# 079. Local smoothing for the Euclidean wave equation

2 manuscripts and 6 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Sogge’s local smoothing conjecture in every spatial dimension $n\ge2$, with arbitrarily small loss above the sharp Sobolev threshold. The wave estimate yields the Bochner–Riesz conjecture and, for $2\le p\lt\infty$, maximal bounds for these means and sharp bounds for Stein’s square function. It also gives Fourier restriction throughout the interior of the conjectured range for the sphere, compact paraboloid, and truncated cone, and local smoothing for the Schrödinger equation. The Kakeya and Nikodym maximal conjectures follow. In particular, every Euclidean Kakeya set has full Hausdorff dimension.

## Local smoothing for the Euclidean wave equation

We prove Sogge’s local smoothing conjecture for the Euclidean wave equation in every spatial dimension at least two. We deduce the Bochner–Riesz conjecture, maximal estimates for these means, and sharp bounds for Stein’s square function. We obtain Fourier restriction estimates for the sphere, the compact paraboloid, and the truncated cone throughout the interior of the conjectured range, as well as local smoothing for the Schrödinger equation. We also prove the Kakeya and Nikodym maximal conjectures. In particular, every Euclidean Kakeya set has full Hausdorff dimension.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Local-smoothing-for-the-Euclidean-wave-equation-October-25-2026/paper.pdf); the Lean below formalizes results from it.

## Critical local smoothing for the three-dimensional wave equation

We prove the critical $L^{3}$ local smoothing estimate for the wave equation in three spatial dimensions, with every positive Sobolev loss. This resolves Sogge's Euclidean local smoothing conjecture in dimension three.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Critical-local-smoothing-for-the-three-dimensional-wave-equation-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

For every dimension $n\ge 2$ and every $2\le p<\infty$, the formalization bounds the $L^p(\mathbb R^n\times[1,2])$ norm of the Euclidean half-wave by a constant times the $W^{s,p}(\mathbb R^n)$ norm of its Schwartz initial data. The Sobolev order is $s=\max(0,(n-1)/2-n/p)+\varepsilon$ for every $\varepsilon>0$, and $s=0$ is allowed at $p=2$. In dimension three this gives the critical $L^3$ estimate with arbitrarily small positive Sobolev loss.

The formalization also gives uniform Bochner–Riesz multiplier bounds, spherical extension estimates, and Stein square-function bounds in their strict ranges. The Kakeya maximal operator satisfies an $L^n$ bound with loss $\delta^{-\varepsilon}$ for every $\varepsilon>0$ at tube radii $0<\delta\le 1$. Every subset of $\mathbb R^n$ containing a unit segment in each direction has Hausdorff dimension $n$.

The development also proves a logarithmic lower bound for the volume occupied by tubes. In dimension three, at least $\delta^{-2}$ unit-length tubes of radius $\delta$ with $\delta$-separated directions have union volume at least $c/(1+\log(1/\delta))^{66}$, uniformly over their centers and $0<\delta\le 1$.

## Lean: Euclidean half-wave local smoothing

```lean
theorem euclidean_local_smoothing :
    ∀ n : ℕ, 2 ≤ n → ∀ p ε : ℝ, 2 ≤ p → (0 < ε ∨ (p = 2 ∧ ε = 0)) →
      ∃ C : ℝ, 0 < C ∧ ∀ f : SchwartzMap (Space n) ℂ,
        MemLp (besselPotential (max 0 (((n : ℝ) - 1) / 2 - n / p) + ε) f)
          (ENNReal.ofReal p) ∧
        MemLp (fun z : Space n × ℝ ↦ halfWaveIntegral z.2 f z.1)
          (ENNReal.ofReal p) (observationMeasure n) ∧
        eLpNorm (fun z : Space n × ℝ ↦ halfWaveIntegral z.2 f z.1)
          (ENNReal.ofReal p) (observationMeasure n) ≤
        ENNReal.ofReal C *
          eLpNorm (besselPotential (max 0 (((n : ℝ) - 1) / 2 - n / p) + ε) f)
            (ENNReal.ofReal p) volume
```

Stated in [LocalSmoothing.lean, line 84](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LocalSmoothing.lean#L84). Proved in [lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean, line 85](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean#L85). formalization.yaml lists it as one of the repository's main results.

## Lean: Bochner–Riesz multiplier bounds uniform in the radius

```lean
theorem bochner_riesz :
    ∀ n : ℕ, 2 ≤ n → ∀ p : ℝ≥0∞, 1 ≤ p → ∀ δ : ℝ,
      max ((n : ℝ) * |(p⁻¹).toReal - 1 / 2| - 1 / 2) 0 < δ →
      ∃ C : ℝ, 0 < C ∧ ∀ R : ℝ, 0 < R → ∀ f : SchwartzMap (Space n) ℂ,
        MemLp (bochnerRiesz δ R f) p ∧
        eLpNorm (bochnerRiesz δ R f) p volume ≤
          ENNReal.ofReal C * eLpNorm f p volume
```

Stated in [LocalSmoothing.lean, line 99](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LocalSmoothing.lean#L99). Proved in [lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean, line 100](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean#L100). formalization.yaml lists it as one of the repository's main results.

## Lean: Spherical restriction in extension form

```lean
theorem spherical_restriction :
    ∀ n : ℕ, 2 ≤ n → ∀ a : ℝ≥0∞, 1 < a → ∀ b : ℝ,
      2 * (n : ℝ) / (n - 1) < b →
      ((n : ℝ) + 1) / ((n : ℝ) - 1) * conjugateExponent a < b →
      ∃ C : ℝ, 0 < C ∧ ∀ g : Space n → ℂ, MemLp g a (sphereMeasure n) →
        MemLp (sphericalExtension g) (ENNReal.ofReal b) ∧
        eLpNorm (sphericalExtension g) (ENNReal.ofReal b) volume ≤
          ENNReal.ofReal C * eLpNorm g a (sphereMeasure n)
```

Stated in [LocalSmoothing.lean, line 109](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LocalSmoothing.lean#L109). Proved in [lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean, line 110](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean#L110). formalization.yaml lists it as one of the repository's main results.

## Lean: Kakeya maximal estimate

```lean
theorem kakeya_maximal :
    ∀ n : ℕ, 2 ≤ n → ∀ ε : ℝ, 0 < ε → ∃ C : ℝ, 0 < C ∧
      ∀ δ : ℝ, 0 < δ → δ ≤ 1 → ∀ f : Space n → ℂ, MemLp f n →
        MemLp (kakeyaMaximal δ f) n (sphereMeasure n) ∧
        eLpNorm (kakeyaMaximal δ f) n (sphereMeasure n) ≤
          ENNReal.ofReal (C * δ ^ (-ε)) * eLpNorm f n volume
```

Stated in [LocalSmoothing.lean, line 120](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LocalSmoothing.lean#L120). Proved in [lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean, line 121](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean#L121). formalization.yaml lists it as one of the repository's main results.

## Lean: Full Hausdorff dimension of Euclidean Kakeya sets

```lean
theorem kakeya :
    ∀ n : ℕ, 2 ≤ n → ∀ F : Set (Space n), IsKakeyaSet F → dimH F = n
```

Stated in [LocalSmoothing.lean, line 129](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LocalSmoothing.lean#L129). Proved in [lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean, line 130](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean#L130). formalization.yaml lists it as one of the repository's main results.

## Lean: Stein square-function estimate

```lean
theorem stein_square :
    ∀ n : ℕ, 2 ≤ n → ∀ p α : ℝ, 2 ≤ p →
      max (1 / 2) ((n : ℝ) * (1 / 2 - 1 / p)) < α →
      ∃ C : ℝ, 0 < C ∧ ∀ f : SchwartzMap (Space n) ℂ,
        MemLp (Stein.literalSteinSquareFunction α f) (ENNReal.ofReal p) volume ∧
        eLpNorm (Stein.literalSteinSquareFunction α f) (ENNReal.ofReal p) volume ≤
          ENNReal.ofReal C * eLpNorm f (ENNReal.ofReal p) volume
```

Stated in [LocalSmoothing.lean, line 134](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/LocalSmoothing.lean#L134). Proved in [lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean, line 135](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Fourier/LocalSmoothing/Comparator.lean#L135). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/079.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/079.md)

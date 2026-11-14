---
declaration: module
origin: cited
lean: KleinGordon.exists_bound_integrand, KleinGordon.norm_sineEvolution_slice_le, KleinGordon.continuous_sineEvolution_slice, KleinGordon.hasDerivAt_solution_radial
statement: formalized
proof: formalized
---

# Dimension raising for the retarded solution

The module `PhyslibAlpha.ClassicalFieldTheory.KleinGordon.DimensionRaising.Retarded`, [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Retarded.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Retarded.lean): 4 declarations, 4 with a docstring.

> The retarded solution in `d + 2` space dimensions is `-(1 / (2π ρ)) ∂ρ` of the one in `d` dimensions
> for sources that are radial in the extra variables.

## i. Overview

> The identity on the slices (`hasDerivAt_sineEvolution_radial`) passes through the Duhamel integral.
> The integrand is bounded uniformly in the time. It vanishes outside the compact time support of the
> source. So the derivative in the radius commutes with the time integral.

## ii. Key results

> - `norm_sineEvolution_slice_le` : the sine evolution of the slices is bounded uniformly in time.
> - `continuous_sineEvolution_slice` : the sine evolution of the slices is continuous in time.
> - `hasDerivAt_solution_radial` : dimension raising for the retarded solution.

## iv. References

> None.

## A. Bounds in time

> - `exists_bound_integrand` : the Fourier integrand is bounded uniformly in the time.
> - `norm_sineEvolution_slice_le` : the sine evolution of the slices is bounded uniformly in time.
> - `continuous_sineEvolution_slice` : the sine evolution of the slices is continuous in time.

## B. The retarded solution

> - `hasDerivAt_solution_radial` : dimension raising for the retarded solution.

**`KleinGordon.exists_bound_integrand`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Retarded.lean#L64).

> The Fourier integrand of the sine evolution of the slice at time `s` is bounded uniformly.

```lean
lemma exists_bound_integrand {μ : ℝ} (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (t : ℝ) :
    ∃ A : ℝ, 0 ≤ A ∧ ∀ (s : ℝ) (z ξ : E), ‖(𝐞 (inner ℝ ξ z) : ℂ) •
      (multiplier (t - s) μ ξ • 𝓕 (slice ℂ ψ s) ξ)‖ ≤
        A * (1 + ‖ξ‖) ^ (-((Module.finrank ℝ E + 1 : ℕ) : ℝ))
```

**`KleinGordon.norm_sineEvolution_slice_le`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Retarded.lean#L93).

> The sine evolution of the slices is bounded, and vanishes outside the time support.

```lean
lemma norm_sineEvolution_slice_le {μ : ℝ} (hμ : 0 ≤ μ) (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (t : ℝ) :
    ∃ B : ℝ, 0 ≤ B ∧ ∀ (s : ℝ) (z : E), ‖sineEvolution ℂ (t - s) μ (slice ℂ ψ s) z‖ ≤
      (Prod.fst '' tsupport ψ).indicator (fun _ => B) s
```

**`KleinGordon.continuous_sineEvolution_slice`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Retarded.lean#L111).

> The sine evolution of the slices is continuous in the time.

```lean
lemma continuous_sineEvolution_slice {μ : ℝ} (hμ : 0 ≤ μ) (ψ : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (t : ℝ)
    (z : E) : Continuous fun s : ℝ => sineEvolution ℂ (t - s) μ (slice ℂ ψ s) z
```

**`KleinGordon.hasDerivAt_solution_radial`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Retarded.lean#L146).

> **Dimension raising for the retarded solution.** Let `ψ'` be a source on `E × ℝ²` that is
> radial in the space variables at each time and let `ψb` be its integral over the plane. The
> retarded solution of `ψb` along a ray has the derivative `-(2π ρ)` times the retarded solution of
> `ψ'` at distance `ρ`. This is `G_{d+2} = -(1 / (2π r)) ∂ᵣ G_d` for every `d` and every mass.

```lean
lemma hasDerivAt_solution_radial {μ : ℝ} (hμ : 0 ≤ μ)
    (ψ' : 𝓓((⊤ : Opens (ℝ × WithLp 2 (E × EuclideanSpace ℝ (Fin 2)))), ℂ))
    (ψb : 𝓓((⊤ : Opens (ℝ × E)), ℂ)) (hrad : ∀ s, Function.IsRadial (slice ℂ ψ' s))
    (hψb : ∀ s x, ψb (s, x) = ∫ y : EuclideanSpace ℝ (Fin 2), ψ' (s, WithLp.toLp 2 (x, y)))
    {e : E} (he : ‖e‖ = 1) (t : ℝ) {ρ : ℝ} (hρ : 0 < ρ) :
    HasDerivAt (fun τ : ℝ => solution ℂ ψb μ t (τ • e))
      (-(2 * Real.pi * ρ : ℝ) • solution ℂ ψ' μ t (WithLp.toLp 2 (ρ • e, 0))) ρ
```

## Depends on

- [The retarded and advanced solution](../part-01/retardedsolution.md)

## Proof depends on

- [Dimension raising for the sine evolution](dimensionraising-sineevolution.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Retarded.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/KleinGordon/DimensionRaising/Retarded.lean)

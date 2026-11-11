---
declaration: theorem
origin: cited
lean: TauCeti.Contour.tendsto_realWindingIntegrand_at_crossing_of_contDiffAt
statement: formalized
proof: formalized
---

# Hungerbühler–Wasem Proposition 2.3, crossing value, under a `C²` hypothesis

For a curve
that is `C²` at the crossing parameter `t₀` with nonvanishing velocity there, the real winding
integrand about `z₀ = γ t₀` tends to `(ẋ ÿ - ẏ ẍ) / (2 (ẋ² + ẏ²))`, where `ẋ + i ẏ` and `ẍ + i ÿ`
are the first and second derivatives of `γ` at `t₀`.

```lean
TauCeti.Contour.tendsto_realWindingIntegrand_at_crossing_of_contDiffAt {γ : ℝ → ℂ} {t₀ : ℝ} {z₀ : ℂ}
  (hγ : ContDiffAt ℝ 2 γ t₀) (hcross : γ t₀ = z₀) (hL : deriv γ t₀ ≠ 0) :
  Filter.Tendsto (fun t => TauCeti.Contour.realWindingIntegrand (γ t - z₀) (deriv γ t))
    (nhdsWithin t₀ {t₀}ᶜ)
    (nhds
      (((deriv γ t₀).re * (deriv (deriv γ) t₀).im - (deriv γ t₀).im * (deriv (deriv γ) t₀).re) /
        (2 * ((deriv γ t₀).re ^ 2 + (deriv γ t₀).im ^ 2))))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.tendsto_realWindingIntegrand_at_crossing_of_contDiffAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Winding/CrossingValue/Curvature.html#TauCeti.Contour.tendsto_realWindingIntegrand_at_crossing_of_contDiffAt).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.tendsto_realWindingIntegrand_at_crossing_of_contDiffAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Winding/CrossingValue/Curvature.html#TauCeti.Contour.tendsto_realWindingIntegrand_at_crossing_of_contDiffAt)
- [Source of `TauCeti.Contour.tendsto_realWindingIntegrand_at_crossing_of_contDiffAt` in TauCeti/Analysis/Contour/Winding/CrossingValue/Curvature.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Contour/Winding/CrossingValue/Curvature.lean#L173)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ContourIntegration/STATUS.md)

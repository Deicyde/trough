---
declaration: theorem
origin: cited
lean: Quaternion.integral_cauchyFueterCutoff_density
statement: formalized
proof: formalized
---

# Quaternion.integral_cauchyFueterCutoff_density

The mass of the cutoff density: for every `ε > 0` and every pole `q₀`, the integral of
`ε⁻¹ ψ'(‖dq x - q₀‖ / ε) ‖dq x - q₀‖⁻³` over the coordinate space is `2π²`, where
`ψ = cauchyFueterCutoff`. This is the reciprocal of the normalization of the Cauchy–Fueter
formula.

```lean
Quaternion.integral_cauchyFueterCutoff_density (q₀ : Quaternion ℝ) {ε : ℝ} (hε : 0 < ε) :
  ∫ (x : Fin 4 → ℝ), TauCeti.cauchyFueterCutoffDensity ε (TauCeti.Quaternion.dq x) q₀ =
    2 * Real.pi ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Quaternion.integral_cauchyFueterCutoff_density`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Cutoff.html#Quaternion.integral_cauchyFueterCutoff_density).

## Sources

- [Tau Ceti documentation: `Quaternion.integral_cauchyFueterCutoff_density`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Cutoff.html#Quaternion.integral_cauchyFueterCutoff_density)
- [Source of `Quaternion.integral_cauchyFueterCutoff_density` in TauCeti/Analysis/Quaternion/Cutoff.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Quaternion/Cutoff.lean#L211)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)

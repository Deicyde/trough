---
declaration: theorem
origin: cited
lean: TauCeti.tendsto_integral_cutoff_smul_quantizeSchwartzValue
statement: formalized
proof: formalized
---

# The Kohn–Nirenberg quantization as a regularized double integral

If `ξ ↦ a(x, ξ)` is
a.e. strongly measurable and `‖a(x, ξ)‖ ≤ C ⟨ξ⟩ ^ m`, then for every continuous compactly
supported cutoff `χ` with `χ 0 = 1`,

`(2π)⁻ⁿ ∫∫ χ(εξ) exp(i ⟪x - y, ξ⟫) a(x, ξ) u(y) dy dξ → Op(a) u (x)` as `ε → 0`,

where `n = finrank ℝ E`.

```lean
TauCeti.tendsto_integral_cutoff_smul_quantizeSchwartzValue.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {W : Type u_2} [NormedAddCommGroup W] [NormedSpace ℂ W] {V : Type u_3}
  [NormedAddCommGroup V] [NormedSpace ℂ V] [CompleteSpace V] {a : E × E → V →L[ℂ] W} {x : E}
  {C m : ℝ} (hmeas : MeasureTheory.AEStronglyMeasurable (fun ξ => a (x, ξ)) MeasureTheory.volume)
  (hC : ∀ (ξ : E), ‖a (x, ξ)‖ ≤ C * (1 + ‖ξ‖ ^ 2) ^ (m / 2)) (u : SchwartzMap E V) {χ : E → ℂ}
  (hχ : Continuous χ) (hχs : HasCompactSupport χ) (hχ0 : χ 0 = 1) :
  Filter.Tendsto
    (fun ε =>
      ((2 * Real.pi) ^ Module.finrank ℝ E)⁻¹ •
        ∫ (p : E × E),
          χ (ε • p.2) • Complex.exp (↑(inner ℝ (x - p.1) p.2) * Complex.I) • (a (x, p.2)) (u p.1))
    (nhdsWithin 0 {0}ᶜ) (nhds (TauCeti.quantizeSchwartzValue a u x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.tendsto_integral_cutoff_smul_quantizeSchwartzValue`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/OscillatoryIntegral.html#TauCeti.tendsto_integral_cutoff_smul_quantizeSchwartzValue).

## Sources

- [Tau Ceti documentation: `TauCeti.tendsto_integral_cutoff_smul_quantizeSchwartzValue`](https://taucetiproject.org/docs/TauCeti/Analysis/Pseudodifferential/OscillatoryIntegral.html#TauCeti.tendsto_integral_cutoff_smul_quantizeSchwartzValue)
- [Source of `TauCeti.tendsto_integral_cutoff_smul_quantizeSchwartzValue` in TauCeti/Analysis/Pseudodifferential/OscillatoryIntegral.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Pseudodifferential/OscillatoryIntegral.lean#L295)
- [Tau Ceti roadmap status: Pseudodifferential operators and elliptic analysis on bundles](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudodifferentialOperators/STATUS.md)

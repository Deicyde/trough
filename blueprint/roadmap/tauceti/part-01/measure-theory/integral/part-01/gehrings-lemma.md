---
declaration: theorem
origin: cited
lean: TauCeti.exists_setLAverage_rpow_add_le, TauCeti.exists_setLAverage_rpow_add_le_of_rpow
statement: formalized
proof: formalized
---

# Gehring's lemma

Let `q > 1` and `b ≥ 0`. There is `δ₀ > 0` such that for every
`0 < δ ≤ δ₀` there is a constant `C`, independent of the functions, the centre and the radius, with
the following property. Let `g` and `h` be nonnegative and a.e. measurable on a ball `B(x₀, R)`,
and suppose that `g` satisfies the reverse Hölder inequality

`⨍_{B(y, ρ)} g ^ q ≤ b (⨍_{B(y, 2ρ)} g) ^ q + ⨍_{B(y, 2ρ)} h ^ q`

on every ball with `B(y, 2ρ) ⊆ B(x₀, R)`. Then

`⨍_{B(x₀, R/2)} g ^ (q + δ) ≤ C ((⨍_{B(x₀, R)} g ^ q) ^ ((q + δ) / q) + ⨍_{B(x₀, R)} h ^ (q + δ))`.

No integrability is assumed and the averages are extended-valued. If the integrals of `g ^ q` and
`h ^ (q + δ)` over `B(x₀, R)` are finite, the right-hand side is finite, so `g` is integrable to the
higher power `q + δ` on the half ball; otherwise the right-hand side is infinite.

```lean
TauCeti.exists_setLAverage_rpow_add_le.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {μ : MeasureTheory.Measure E}
  [μ.IsAddHaarMeasure] {q : ℝ} (hq : 1 < q) (b : NNReal) :
  ∃ δ₀,
    0 < δ₀ ∧
      ∀ (δ : ℝ),
        0 < δ →
          δ ≤ δ₀ →
            ∃ C,
              ∀ {g h : E → ENNReal} {x₀ : E} {R : ℝ},
                AEMeasurable g (μ.restrict (Metric.ball x₀ R)) →
                  AEMeasurable h (μ.restrict (Metric.ball x₀ R)) →
                    (∀ (y : E) (ρ : ℝ),
                        0 < ρ →
                          Metric.ball y (2 * ρ) ⊆ Metric.ball x₀ R →
                            ⨍⁻ (x : E) in Metric.ball y ρ, g x ^ q ∂μ ≤
                              ↑b * (⨍⁻ (x : E) in Metric.ball y (2 * ρ), g x ∂μ) ^ q +
                                ⨍⁻ (x : E) in Metric.ball y (2 * ρ), h x ^ q ∂μ) →
                      ⨍⁻ (x : E) in Metric.ball x₀ (R / 2), g x ^ (q + δ) ∂μ ≤
                        ↑C *
                          ((⨍⁻ (x : E) in Metric.ball x₀ R, g x ^ q ∂μ) ^ ((q + δ) / q) +
                            ⨍⁻ (x : E) in Metric.ball x₀ R, h x ^ (q + δ) ∂μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jensen's inequality for the square of a mean](jensens-inequality-for-the-square-of-a-mean.md)
- [Lebesgue's differentiation theorem](../../other-results/lebesgues-differentiation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_setLAverage_rpow_add_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Gehring.html#TauCeti.exists_setLAverage_rpow_add_le).

## Other forms

**Gehring's lemma for a reverse Hölder inequality between two exponents.** Formalized in Tau Ceti as [`TauCeti.exists_setLAverage_rpow_add_le_of_rpow`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Gehring.html#TauCeti.exists_setLAverage_rpow_add_le_of_rpow).

```lean
TauCeti.exists_setLAverage_rpow_add_le_of_rpow.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {s p : ℝ} (hs : 0 < s) (hsp : s < p)
  (b : NNReal) :
  ∃ ε₀,
    0 < ε₀ ∧
      ∀ (ε : ℝ),
        0 < ε →
          ε ≤ ε₀ →
            ∃ C,
              ∀ {f φ : E → ENNReal} {x₀ : E} {R : ℝ},
                AEMeasurable f (μ.restrict (Metric.ball x₀ R)) →
                  AEMeasurable φ (μ.restrict (Metric.ball x₀ R)) →
                    (∀ (y : E) (ρ : ℝ),
                        0 < ρ →
                          Metric.ball y (2 * ρ) ⊆ Metric.ball x₀ R →
                            ⨍⁻ (x : E) in Metric.ball y ρ, f x ^ p ∂μ ≤
                              ↑b * (⨍⁻ (x : E) in Metric.ball y (2 * ρ), f x ^ s ∂μ) ^ (p / s) +
                                ↑b * ⨍⁻ (x : E) in Metric.ball y (2 * ρ), φ x ^ p ∂μ) →
                      ⨍⁻ (x : E) in Metric.ball x₀ (R / 2), f x ^ (p + ε) ∂μ ≤
                        ↑C *
                          ((⨍⁻ (x : E) in Metric.ball x₀ R, f x ^ p ∂μ) ^ ((p + ε) / p) +
                            ⨍⁻ (x : E) in Metric.ball x₀ R, φ x ^ (p + ε) ∂μ)
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_setLAverage_rpow_add_le`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/Gehring.html#TauCeti.exists_setLAverage_rpow_add_le)
- [Source of `TauCeti.exists_setLAverage_rpow_add_le` in TauCeti/MeasureTheory/Integral/Gehring.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Integral/Gehring.lean#L835)

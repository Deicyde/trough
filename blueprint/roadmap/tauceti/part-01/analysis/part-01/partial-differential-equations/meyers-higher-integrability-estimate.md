---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_setLAverage_enorm_gradient_rpow_le_divergence
statement: formalized
proof: formalized
---

# Meyers' higher integrability estimate

Let `n ≥ 1` be the dimension and let `K` bound the
ellipticity ratio. There is `ε₀ > 0`, and for each `0 < ε ≤ ε₀` a constant `C`, both independent
of the domain, the coefficients, the solution, the datum and the ball, with the following
property. Let `a` be measurable and uniformly elliptic on `Ω` with constants `0 < λ ≤ Λ ≤ K λ`, let
`F ∈ L²(Ω; ℝⁿ)`, and let `u ∈ H¹(Ω)` satisfy `a(u, v) = -∫_Ω ⟪F, ∇v⟫` for every `v ∈ H¹₀(Ω)`.
For every ball `B = B(x₀, R) ⊆ Ω`, with `½B = B(x₀, R/2)`,

`⨍_{½B} ‖∇u‖ ^ (2 + ε) ≤ C ((⨍_B ‖∇u‖²) ^ ((2 + ε)/2) + ⨍_B (‖F‖/λ) ^ (2 + ε))`.

The averages are extended-valued. When `F` is `(2 + ε)`-integrable on `B(x₀, R)` the right-hand
side is finite, so `∇u` is `(2 + ε)`-integrable on `B(x₀, R/2)`.

```lean
TauCeti.PDE.exists_setLAverage_enorm_gradient_rpow_le_divergence.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  [Nonempty ι] (K : ℝ) :
  ∃ ε₀,
    0 < ε₀ ∧
      ∀ (ε : ℝ),
        0 < ε →
          ε ≤ ε₀ →
            ∃ C,
              ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
                {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {lam Lam : ℝ}
                {F : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {u : ↥(TauCeti.W1p mu Omega 2)}
                {x₀ : EuclideanSpace ℝ ι} {R : ℝ},
                TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
                  Lam ≤ K * lam →
                    MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
                      MeasureTheory.MemLp F 2 (mu.restrict ↑Omega) →
                        (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                            TauCeti.PDE.energyFormH1 a 0 0 u ↑v =
                              -∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
                                  inner ℝ (F x) (↑↑(TauCeti.W1p.gradient ↑v) x) ∂mu) →
                          Metric.ball x₀ R ⊆ ↑Omega →
                            ⨍⁻ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ (R / 2),
                                ‖↑↑(TauCeti.W1p.gradient u) x‖ₑ ^ (2 + ε) ∂mu ≤
                              ↑C *
                                ((⨍⁻ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ R,
                                      ‖↑↑(TauCeti.W1p.gradient u) x‖ₑ ^ 2 ∂mu) ^
                                    ((2 + ε) / 2) +
                                  ⨍⁻ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ R,
                                    (‖F x‖ₑ / ENNReal.ofReal lam) ^ (2 + ε) ∂mu)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gehring's lemma](../../../measure-theory/integral/part-01/gehrings-lemma.md)
- [The reverse Hölder inequality for the gradient of a weak solution](the-reverse-holder-inequality-for-the-gradient-o.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_setLAverage_enorm_gradient_rpow_le_divergence`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HigherIntegrability.html#TauCeti.PDE.exists_setLAverage_enorm_gradient_rpow_le_divergence).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_setLAverage_enorm_gradient_rpow_le_divergence`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HigherIntegrability.html#TauCeti.PDE.exists_setLAverage_enorm_gradient_rpow_le_divergence)
- [Source of `TauCeti.PDE.exists_setLAverage_enorm_gradient_rpow_le_divergence` in TauCeti/Analysis/PDE/Regularity/HigherIntegrability.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Regularity/HigherIntegrability.lean#L223)

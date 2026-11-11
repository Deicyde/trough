---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_setLAverage_enorm_gradient_sq_le_divergence
statement: formalized
proof: formalized
---

# The reverse Hölder inequality for the gradient of a weak solution

Let `n ≥ 1` be the
dimension, let `1 ≤ s ≤ 2` with `1/s - 1/2 < 1/n`, and let `K` bound the ellipticity ratio.
There is `b`, independent of the domain, the coefficients, the solution, the datum and the ball,
with the following property. Let `a` be measurable and uniformly elliptic on `Ω` with constants
`0 < λ ≤ Λ ≤ K λ`, let `F ∈ L²(Ω; ℝⁿ)`, and let `u ∈ H¹(Ω)` satisfy `a(u, v) = -∫_Ω ⟪F, ∇v⟫` for
every `v ∈ H¹₀(Ω)`. For every ball with `B(y, 2ρ) ⊆ Ω`,

`⨍_{B(y, ρ)} ‖∇u‖² ≤ b (⨍_{B(y, 2ρ)} ‖∇u‖ ^ s) ^ (2/s) + b ⨍_{B(y, 2ρ)} (‖F‖/λ)²`.

The averages are extended-valued.

```lean
TauCeti.PDE.exists_setLAverage_enorm_gradient_sq_le_divergence.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  [Nonempty ι] {s : NNReal} (hs1 : 1 ≤ s) (hs2 : s ≤ 2)
  (hsn : (↑s)⁻¹ - 2⁻¹ < (↑(Module.finrank ℝ (EuclideanSpace ℝ ι)))⁻¹) (K : ℝ) :
  ∃ b,
    ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)} {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
      {lam Lam : ℝ} {F : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {u : ↥(TauCeti.W1p mu Omega 2)}
      {y : EuclideanSpace ℝ ι} {ρ : ℝ},
      TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
        Lam ≤ K * lam →
          MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
            MeasureTheory.MemLp F 2 (mu.restrict ↑Omega) →
              (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                  TauCeti.PDE.energyFormH1 a 0 0 u ↑v =
                    -∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
                        inner ℝ (F x) (↑↑(TauCeti.W1p.gradient ↑v) x) ∂mu) →
                0 < ρ →
                  Metric.ball y (2 * ρ) ⊆ ↑Omega →
                    ⨍⁻ (x : EuclideanSpace ℝ ι) in Metric.ball y ρ,
                        ‖↑↑(TauCeti.W1p.gradient u) x‖ₑ ^ 2 ∂mu ≤
                      ↑b *
                          (⨍⁻ (x : EuclideanSpace ℝ ι) in Metric.ball y (2 * ρ),
                              ‖↑↑(TauCeti.W1p.gradient u) x‖ₑ ^ ↑s ∂mu) ^
                            (2 / ↑s) +
                        ↑b *
                          ⨍⁻ (x : EuclideanSpace ℝ ι) in Metric.ball y (2 * ρ),
                            (‖F x‖ₑ / ENNReal.ofReal lam) ^ 2 ∂mu
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Caccioppoli inequality](../../part-03/pde/part-01/the-caccioppoli-inequality.md)
- [The Sobolev–Poincaré inequality on `W^{1,p}(Ω)`](../../part-03/sobolev/part-02/the-sobolev-poincare-inequality-on-w-1-p.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_setLAverage_enorm_gradient_sq_le_divergence`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HigherIntegrability.html#TauCeti.PDE.exists_setLAverage_enorm_gradient_sq_le_divergence).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_setLAverage_enorm_gradient_sq_le_divergence`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HigherIntegrability.html#TauCeti.PDE.exists_setLAverage_enorm_gradient_sq_le_divergence)
- [Source of `TauCeti.PDE.exists_setLAverage_enorm_gradient_sq_le_divergence` in TauCeti/Analysis/PDE/Regularity/HigherIntegrability.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Regularity/HigherIntegrability.lean#L129)

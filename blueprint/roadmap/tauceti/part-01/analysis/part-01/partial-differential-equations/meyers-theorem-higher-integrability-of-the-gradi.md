---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_memLp_gradient_ball_divergence
statement: formalized
proof: formalized
---

# Meyers' theorem: higher integrability of the gradient

Let `n ≥ 1` be the dimension and
let `K` bound the ellipticity ratio. There is `ε₀ > 0`, depending only on `n` and `K`, with the
following property. Let `a` be measurable and uniformly elliptic on `Ω` with constants
`0 < λ ≤ Λ ≤ K λ`, let `F ∈ L²(Ω; ℝⁿ)`, and let `u ∈ H¹(Ω)` satisfy `a(u, v) = -∫_Ω ⟪F, ∇v⟫` for
every `v ∈ H¹₀(Ω)`. If `B(x₀, R) ⊆ Ω`, `0 < ε ≤ ε₀` and `F` lies in `L^{2 + ε}(B(x₀, R))`, then
`∇u` lies in `L^{2 + ε}(B(x₀, R/2))`.

```lean
TauCeti.PDE.exists_memLp_gradient_ball_divergence.{u_1} {ι : Type u_1} [Fintype ι] [DecidableEq ι]
  {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure] [Nonempty ι] (K : ℝ) :
  ∃ ε₀,
    0 < ε₀ ∧
      ∀ (ε : ℝ),
        0 < ε →
          ε ≤ ε₀ →
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
                          MeasureTheory.MemLp F (ENNReal.ofReal (2 + ε))
                              (mu.restrict (Metric.ball x₀ R)) →
                            MeasureTheory.MemLp (↑↑(TauCeti.W1p.gradient u))
                              (ENNReal.ofReal (2 + ε)) (mu.restrict (Metric.ball x₀ (R / 2)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Meyers' higher integrability estimate](meyers-higher-integrability-estimate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_memLp_gradient_ball_divergence`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HigherIntegrability.html#TauCeti.PDE.exists_memLp_gradient_ball_divergence).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_memLp_gradient_ball_divergence`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/HigherIntegrability.html#TauCeti.PDE.exists_memLp_gradient_ball_divergence)
- [Source of `TauCeti.PDE.exists_memLp_gradient_ball_divergence` in TauCeti/Analysis/PDE/Regularity/HigherIntegrability.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Regularity/HigherIntegrability.lean#L264)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PDE/STATUS.md)

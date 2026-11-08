---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral, TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral_drift, TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_add_of_memLp
statement: formalized
proof: formalized
---

# De Giorgi's interior oscillation estimate

Let `n ≥ 1` be the dimension. There are
`α ∈ (0, 1]` and `C > 0`, depending only on `λ`, `Λ`, the dimension and the normalization of the
additive Haar measure `mu`, such that the following holds. Let `a` be measurable and uniformly
elliptic on `Ω` with constants `λ, Λ`, and let `u ∈ H¹(Ω)` be a weak solution of
`-∂ᵢ(aⁱʲ ∂ⱼu) = 0`. If `B(x₀, R) ⊆ Ω` and `0 < r ≤ R/2`, then almost everywhere on `B(x₀, r)`
the function `u` takes values in an interval of length

`C (r / R)^α R^{-n/2} ‖u‖_{L²(B(x₀, R))}`.

This is the a-priori estimate behind the interior Hölder continuity of weak solutions, and the
case `b = 0` of
`TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral_drift`.

```lean
TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral.{u_1} {ι : Type u_1}
  [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] {lam Lam : ℝ} [Nonempty ι] :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
            {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {u : ↥(TauCeti.W1p mu Omega 2)}
            {x₀ : EuclideanSpace ℝ ι} {R r : ℝ},
            TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
              MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
                (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)), TauCeti.PDE.energyFormH1 a 0 0 u ↑v = 0) →
                  0 < r →
                    r ≤ R / 2 →
                      Metric.ball x₀ R ⊆ ↑Omega →
                        ∃ m',
                          ∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict (Metric.ball x₀ r),
                            ↑↑(TauCeti.W1p.value u) x ∈
                              Set.Icc m'
                                (m' +
                                  C * (r / R) ^ α *
                                    (R ^ (-↑(Fintype.card ι) / 2) *
                                      √(∫ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ R,
                                          ↑↑(TauCeti.W1p.value u) x ^ 2 ∂mu)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The `L²` Leibniz estimate](../../part-02/sobolev/part-01/the-l2-leibniz-estimate.md)
- [The Caccioppoli inequality](../../part-02/pde/part-01/the-caccioppoli-inequality.md)
- [De Giorgi's isoperimetric inequality](../../part-02/sobolev/part-01/de-giorgis-isoperimetric-inequality.md)
- [Hölder's inequality for Young's exponents](../../../measure-theory/euclidean-isoperimetry-sharp-inequalities-and-ri/part-02/holders-inequality-for-youngs-exponents.md)
- [The Sobolev inequality for functions of bounded variation](../geometric-measure-theory-rectifiability-bv-and-f/the-sobolev-inequality-for-functions-of-bounded.md)
- [Stampacchia's global bound](stampacchias-global-bound.md)
- [TauCeti.Wkp](tauceti-wkp.md)
- [The zero-forcing Caccioppoli inequality for a positive truncation of a weak subsolution](../../part-02/pde/part-02/the-zero-forcing-caccioppoli-inequality-for-a-po.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Oscillation.html#TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral).

## Other forms

**De Giorgi's interior oscillation estimate with a drift.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral_drift`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Oscillation.html#TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral_drift).

```lean
TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral_drift.{u_1}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] {lam Lam : ℝ} [Nonempty ι] (σ : ℝ) :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
            {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι}
            {beta : ℝ} {u : ↥(TauCeti.W1p mu Omega 2)} {x₀ : EuclideanSpace ℝ ι} {R r : ℝ},
            TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
              MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
                MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega) →
                  (∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) →
                    (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)), TauCeti.PDE.energyFormH1 a b 0 u ↑v = 0) →
                      0 < r →
                        r ≤ R / 2 →
                          Metric.ball x₀ R ⊆ ↑Omega →
                            beta * R ≤ σ * lam →
                              ∃ m',
                                ∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict (Metric.ball x₀ r),
                                  ↑↑(TauCeti.W1p.value u) x ∈
                                    Set.Icc m'
                                      (m' +
                                        C * (r / R) ^ α *
                                          (R ^ (-↑(Fintype.card ι) / 2) *
                                            √(∫ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ R,
                                                ↑↑(TauCeti.W1p.value u) x ^ 2 ∂mu)))
```

**De Giorgi's interior oscillation estimate with a right-hand side.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_add_of_memLp`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Inhomogeneous.html#TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_add_of_memLp).

```lean
TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_add_of_memLp.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  [Nonempty ι] {lam Lam : ℝ} {r : NNReal} (hr : 1 < r) (hrn : ↑(Fintype.card ι) < 2 * ↑r) :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
            {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {f : EuclideanSpace ℝ ι → ℝ}
            {u : ↥(TauCeti.W1p mu Omega 2)} {x₀ : EuclideanSpace ℝ ι} {R s : ℝ},
            TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
              MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
                MeasureTheory.MemLp f (↑r) (mu.restrict (Metric.ball x₀ R)) →
                  (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                      TauCeti.PDE.energyFormH1 a 0 0 u ↑v =
                        ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
                          f x * ↑↑(TauCeti.W1p.value ↑v) x ∂mu) →
                    0 < s →
                      s ≤ R / 2 →
                        Metric.ball x₀ R ⊆ ↑Omega →
                          ∃ m',
                            ∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict (Metric.ball x₀ s),
                              ↑↑(TauCeti.W1p.value u) x ∈
                                Set.Icc m'
                                  (m' +
                                    C * (s / R) ^ α *
                                      (R ^ (-↑(Fintype.card ι) / 2) *
                                          √(∫ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ R,
                                              ↑↑(TauCeti.W1p.value u) x ^ 2 ∂mu) +
                                        R ^ (2 - ↑(Fintype.card ι) / ↑r) *
                                            (MeasureTheory.eLpNorm f (↑r)
                                                (mu.restrict (Metric.ball x₀ R))).toReal /
                                          lam))
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Oscillation.html#TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral)
- [Source of `TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral` in TauCeti/Analysis/PDE/Regularity/Oscillation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Regularity/Oscillation.lean#L702)

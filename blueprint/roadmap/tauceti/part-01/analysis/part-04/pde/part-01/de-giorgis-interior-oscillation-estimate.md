---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral, TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_add_of_forall_ae_abs_sub_le, TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral_drift, TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_add_of_memLp_add_divergence
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

- [The `L²` Leibniz estimate](../../sobolev/part-01/the-l2-leibniz-estimate.md)
- [The Caccioppoli inequality](the-caccioppoli-inequality.md)
- [Chebyshev's inequality for truncations](../../../../measure-theory/integral/part-01/chebyshevs-inequality-for-truncations.md)
- [De Giorgi's isoperimetric inequality](../../sobolev/part-01/de-giorgis-isoperimetric-inequality.md)
- [Hölder's inequality with a bounded weight](../../../../measure-theory/integral/part-02/holders-inequality-with-a-bounded-weight.md)
- [The Sobolev inequality on `W^{1,p}_0` of a ball](../../sobolev/part-02/the-sobolev-inequality-on-w-1-p-0-of-a-ball.md)
- [Stampacchia's bound on a ball](../part-03/stampacchias-bound-on-a-ball.md)
- [Stampacchia's global bound](../part-03/stampacchias-global-bound.md)
- [The zero-forcing Caccioppoli inequality for a positive truncation of a weak subsolution](../part-04/the-zero-forcing-caccioppoli-inequality-for-a-po.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Oscillation.html#TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral).

## Other forms

**De Giorgi's interior oscillation estimate near solutions of the homogeneous equation.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_add_of_forall_ae_abs_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Inhomogeneous.html#TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_add_of_forall_ae_abs_sub_le).

```lean
TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_add_of_forall_ae_abs_sub_le.{u_1}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] [Nonempty ι] {lam Lam γ : ℝ} (hγ : 0 < γ) :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
            {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {u : ↥(TauCeti.W1p mu Omega 2)}
            {x₀ : EuclideanSpace ℝ ι} {R s A : ℝ},
            TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
              MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
                (∀ (ρ : ℝ),
                    0 < ρ →
                      ρ ≤ R →
                        ∃ g,
                          (∀
                              (v :
                                ↥(TauCeti.W1p0 mu { carrier := Metric.ball x₀ ρ, is_open' := ⋯ }
                                    2)),
                              TauCeti.PDE.energyFormH1 a 0 0 g ↑v = 0) ∧
                            ∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict (Metric.ball x₀ ρ),
                              |↑↑(TauCeti.W1p.value u) x - ↑↑(TauCeti.W1p.value g) x| ≤ ρ ^ γ * A) →
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
                                      R ^ γ * A))
```

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

**De Giorgi's interior oscillation estimate with a right-hand side `f + ∂ᵢFⁱ`.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_add_of_memLp_add_divergence`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Inhomogeneous.html#TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_add_of_memLp_add_divergence).

```lean
TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_add_of_memLp_add_divergence.{u_1}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)}
  [mu.IsAddHaarMeasure] [Nonempty ι] {lam Lam : ℝ} {r q : NNReal} (hr : 1 < r)
  (hrn : ↑(Fintype.card ι) < 2 * ↑r) (hq : 2 < ↑q) (hqn : ↑(Fintype.card ι) < ↑q) :
  ∃ α C,
    0 < α ∧
      α ≤ 1 ∧
        0 < C ∧
          ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
            {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {f : EuclideanSpace ℝ ι → ℝ}
            {F : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {u : ↥(TauCeti.W1p mu Omega 2)}
            {x₀ : EuclideanSpace ℝ ι} {R s : ℝ},
            TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
              MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
                MeasureTheory.MemLp f (↑r) (mu.restrict (Metric.ball x₀ R)) →
                  MeasureTheory.MemLp F (↑q) (mu.restrict (Metric.ball x₀ R)) →
                    (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                        TauCeti.PDE.energyFormH1 a 0 0 u ↑v =
                          ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
                              f x * ↑↑(TauCeti.W1p.value ↑v) x ∂mu -
                            ∫ (x : EuclideanSpace ℝ ι) in ↑Omega,
                              inner ℝ (F x) (↑↑(TauCeti.W1p.gradient ↑v) x) ∂mu) →
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
                                          (R ^ (2 - ↑(Fintype.card ι) / ↑r) *
                                                (MeasureTheory.eLpNorm f (↑r)
                                                    (mu.restrict (Metric.ball x₀ R))).toReal +
                                              R ^ (1 - ↑(Fintype.card ι) / ↑q) *
                                                (MeasureTheory.eLpNorm F (↑q)
                                                    (mu.restrict (Metric.ball x₀ R))).toReal) /
                                            lam))
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Oscillation.html#TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral)
- [Source of `TauCeti.PDE.exists_ae_value_mem_Icc_add_mul_rpow_mul_rpow_mul_sqrt_setIntegral` in TauCeti/Analysis/PDE/Regularity/Oscillation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Regularity/Oscillation.lean#L703)

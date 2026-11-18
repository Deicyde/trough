---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_setAverage_rpow_mul_setAverage_rpow_neg_le, TauCeti.PDE.exists_setAverage_rpow_mul_setAverage_rpow_neg_le_lowerOrder
statement: formalized
proof: formalized
---

# Moser's crossover estimate (`TauCeti.PDE.exists_setAverage_rpow_mul_setAverage_rpow_neg_le`)

There are constants `c > 0` and `K`, depending only on the
dimension `n ≥ 1`, with the following property. Let `a` be measurable and uniformly elliptic on
`Ω` with constants `0 < λ ≤ Λ`, and let `u ∈ H¹(Ω)` be a weak supersolution of
`-∂ᵢ(aⁱʲ ∂ⱼu) ≥ 0` with `u ≥ ε` almost everywhere for some `ε > 0`. Then for every ball with
`B(x₀, 4√n r) ⊆ Ω` and every exponent `|p| ≤ c λ/Λ`,

`⨍_{B(x₀, r)} u^p · ⨍_{B(x₀, r)} u^{-p} ≤ K`.

The bound is independent of `u`, `ε`, `λ`, `Λ` and the ball.

```lean
TauCeti.PDE.exists_setAverage_rpow_mul_setAverage_rpow_neg_le.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] [Nonempty ι] :
  ∃ c,
    0 < c ∧
      ∃ K,
        ∀ (mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)) [inst : mu.IsAddHaarMeasure]
          {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
          {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {lam Lam : ℝ} {u : ↥(TauCeti.W1p mu Omega 2)}
          {ε : ℝ} {x₀ : EuclideanSpace ℝ ι} {r p : ℝ},
          TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
            MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
              (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                  (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega,
                      0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
                    0 ≤ TauCeti.PDE.energyFormH1 a 0 0 u ↑v) →
                0 < ε →
                  (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, ε ≤ ↑↑(TauCeti.W1p.value u) x) →
                    Metric.ball x₀ (4 * √↑(Fintype.card ι) * r) ⊆ ↑Omega →
                      |p| ≤ c * (lam / Lam) →
                        (⨍ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ r,
                              ↑↑(TauCeti.W1p.value u) x ^ p ∂mu) *
                            ⨍ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ r,
                              ↑↑(TauCeti.W1p.value u) x ^ (-p) ∂mu ≤
                          K
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The logarithmic Caccioppoli inequality](the-logarithmic-caccioppoli-inequality.md)
- [Moser's crossover estimate (`TauCeti.exists_setLIntegral_exp_mul_mul_setLIntegral_exp_neg_mul_ball_le`)](../../../../measure-theory/integral/part-02/mosers-crossover-estimate-tauceti-exists-setlint.md)
- [The Poincaré–Wirtinger inequality on a ball](../../sobolev/part-02/the-poincare-wirtinger-inequality-on-a-ball.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_setAverage_rpow_mul_setAverage_rpow_neg_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Crossover.html#TauCeti.PDE.exists_setAverage_rpow_mul_setAverage_rpow_neg_le).

## Other forms

**Moser's crossover estimate with lower-order terms.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_setAverage_rpow_mul_setAverage_rpow_neg_le_lowerOrder`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Crossover.html#TauCeti.PDE.exists_setAverage_rpow_mul_setAverage_rpow_neg_le_lowerOrder).

```lean
TauCeti.PDE.exists_setAverage_rpow_mul_setAverage_rpow_neg_le_lowerOrder.{u_1} {ι : Type u_1}
  [Fintype ι] [DecidableEq ι] [Nonempty ι] :
  ∃ c₀,
    0 < c₀ ∧
      ∃ K,
        ∀ (mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)) [inst : mu.IsAddHaarMeasure]
          {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
          {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι}
          {c : EuclideanSpace ℝ ι → ℝ} {lam Lam beta gamma : ℝ} {u : ↥(TauCeti.W1p mu Omega 2)}
          {ε : ℝ} {x₀ : EuclideanSpace ℝ ι} {r p : ℝ},
          TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
            MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
              MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega) →
                MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega) →
                  (∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) →
                    (∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma) →
                      (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                          (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega,
                              0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
                            0 ≤ TauCeti.PDE.energyFormH1 a b c u ↑v) →
                        0 < ε →
                          (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega,
                              ε ≤ ↑↑(TauCeti.W1p.value u) x) →
                            Metric.ball x₀ (4 * √↑(Fintype.card ι) * r) ⊆ ↑Omega →
                              |p| *
                                    √((Lam / lam) ^ 2 + (beta * r / lam) ^ 2 +
                                        gamma * r ^ 2 / lam) ≤
                                  c₀ →
                                (⨍ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ r,
                                      ↑↑(TauCeti.W1p.value u) x ^ p ∂mu) *
                                    ⨍ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ r,
                                      ↑↑(TauCeti.W1p.value u) x ^ (-p) ∂mu ≤
                                  K
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_setAverage_rpow_mul_setAverage_rpow_neg_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Crossover.html#TauCeti.PDE.exists_setAverage_rpow_mul_setAverage_rpow_neg_le)
- [Source of `TauCeti.PDE.exists_setAverage_rpow_mul_setAverage_rpow_neg_le` in TauCeti/Analysis/PDE/Regularity/Crossover.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Regularity/Crossover.lean#L204)

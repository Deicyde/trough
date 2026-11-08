---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_ae_setAverage_rpow_rpow_inv_le_mul_value, TauCeti.PDE.exists_pos_ae_setAverage_rpow_rpow_inv_le_mul_value
statement: formalized
proof: formalized
---

# Moser's weak Harnack inequality

Let `n ≥ 1` be the dimension. For every exponent `s > 0`
with `(n - 2) s < n`, that is `s < n/(n - 2)` when `n ≥ 3` and `s` arbitrary when `n ≤ 2`, there
is `C > 0`, depending only on `λ`, `Λ`, `s`, the dimension and the normalization of the additive
Haar measure `mu`, with the following property. Let `a` be measurable and uniformly elliptic on
`Ω` with constants `λ, Λ`, and let `u ∈ H¹(Ω)` be a nonnegative weak supersolution of
`-∂ᵢ(aⁱʲ ∂ⱼu) ≥ 0`, that is `a(u, v) ≥ 0` for every nonnegative `v ∈ H¹₀(Ω)`. Then on every ball
with `B(x₀, 8√n r) ⊆ Ω`,

`(⨍_{B(x₀, r)} u^s)^{1/s} ≤ C u(x)` for almost every `x ∈ B(x₀, r)`,

and `u^s` is integrable on `B(x₀, r)`, so the left side is a genuine average even for `s > 2`.
The constant does not depend on `u` or the ball.

```lean
TauCeti.PDE.exists_ae_setAverage_rpow_rpow_inv_le_mul_value.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {lam Lam : ℝ} [Nonempty ι] {s : ℝ} (hs : 0 < s)
  (hsn : (↑(Fintype.card ι) - 2) * s < ↑(Fintype.card ι)) :
  ∃ C,
    0 < C ∧
      ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
        {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {u : ↥(TauCeti.W1p mu Omega 2)}
        {x₀ : EuclideanSpace ℝ ι} {r : ℝ},
        TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
          MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
            (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
                  0 ≤ TauCeti.PDE.energyFormH1 a 0 0 u ↑v) →
              (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value u) x) →
                Metric.ball x₀ (8 * √↑(Fintype.card ι) * r) ⊆ ↑Omega →
                  MeasureTheory.IntegrableOn (fun y => ↑↑(TauCeti.W1p.value u) y ^ s)
                      (Metric.ball x₀ r) mu ∧
                    ∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict (Metric.ball x₀ r),
                      (⨍ (y : EuclideanSpace ℝ ι) in Metric.ball x₀ r,
                            ↑↑(TauCeti.W1p.value u) y ^ s ∂mu) ^
                          s⁻¹ ≤
                        C * ↑↑(TauCeti.W1p.value u) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Moser's crossover estimate (`TauCeti.PDE.exists_setAverage_rpow_mul_setAverage_rpow_neg_le`)](mosers-crossover-estimate-tauceti-pde-exists-set.md)
- [Moser's lower bound from small negative powers](../../part-02/pde/part-01/mosers-lower-bound-from-small-negative-powers.md)
- [Moser's reverse Hölder inequality for powers of a positive supersolution](mosers-reverse-holder-inequality-for-powers-of-a.md)
- [The Sobolev inequality for functions of bounded variation](../geometric-measure-theory-rectifiability-bv-and-f/the-sobolev-inequality-for-functions-of-bounded.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_ae_setAverage_rpow_rpow_inv_le_mul_value`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Harnack.html#TauCeti.PDE.exists_ae_setAverage_rpow_rpow_inv_le_mul_value).

## Other forms

**Moser's weak Harnack inequality at a small exponent.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_pos_ae_setAverage_rpow_rpow_inv_le_mul_value`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Harnack.html#TauCeti.PDE.exists_pos_ae_setAverage_rpow_rpow_inv_le_mul_value).

```lean
TauCeti.PDE.exists_pos_ae_setAverage_rpow_rpow_inv_le_mul_value.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {lam Lam : ℝ} [Nonempty ι] :
  ∃ p₀,
    0 < p₀ ∧
      p₀ ≤ 2 ∧
        ∃ C,
          0 < C ∧
            ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
              {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {u : ↥(TauCeti.W1p mu Omega 2)}
              {x₀ : EuclideanSpace ℝ ι} {r : ℝ},
              TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
                MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
                  (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                      (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega,
                          0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
                        0 ≤ TauCeti.PDE.energyFormH1 a 0 0 u ↑v) →
                    (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega,
                        0 ≤ ↑↑(TauCeti.W1p.value u) x) →
                      Metric.ball x₀ (8 * √↑(Fintype.card ι) * r) ⊆ ↑Omega →
                        ∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict (Metric.ball x₀ r),
                          (⨍ (y : EuclideanSpace ℝ ι) in Metric.ball x₀ (2 * r),
                                ↑↑(TauCeti.W1p.value u) y ^ p₀ ∂mu) ^
                              p₀⁻¹ ≤
                            C * ↑↑(TauCeti.W1p.value u) x
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_ae_setAverage_rpow_rpow_inv_le_mul_value`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Harnack.html#TauCeti.PDE.exists_ae_setAverage_rpow_rpow_inv_le_mul_value)
- [Source of `TauCeti.PDE.exists_ae_setAverage_rpow_rpow_inv_le_mul_value` in TauCeti/Analysis/PDE/Regularity/Harnack.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Regularity/Harnack.lean#L272)

---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_eLpNorm_rpow_le_mul_eLpNorm_rpow_lowerOrder
statement: formalized
proof: formalized
---

# Moser's reverse Hölder inequality for powers of a positive supersolution, with lower-order terms

There is a constant `C ≥ 0`, depending only on the dimension, with the following property.
Let `a` be measurable and uniformly elliptic on `Ω` with constants `0 < λ ≤ Λ`, let `b` and `c` be
measurable with `‖b‖ ≤ β` and `|c| ≤ γ` on `Ω`, and suppose that `W^{1,2}_0(Ω)` satisfies the
Sobolev inequality `‖v‖_q ≤ S ‖∇v‖₂`. Let `u ∈ H¹(Ω)` be a weak supersolution of
`-∂ᵢ(aⁱʲ ∂ⱼu) + bⁱ ∂ᵢu + c u ≥ 0`, that is `a(u, v) ≥ 0` for every nonnegative `v ∈ H¹₀(Ω)` for the
energy form with drift `b` and mass coefficient `c`, with `u ≥ ε` almost everywhere for some
`ε > 0`. Then for every `p < 1` and all concentric balls `B(x₀, r) ⊂ B(x₀, ρ) ⊆ Ω`,

`‖u^{p/2}‖_{L^q(B(x₀, r))} ≤ S C (A / (ρ - r) + L) ‖u^{p/2}‖_{L²(B(x₀, ρ))}`, where
`A = 1 + |p| Λ / ((1 - p) λ)` and `L = |p| / ((1 - p) λ) · √(β² + (1 - p) λ γ)`.

No sign condition on `c` is needed. The constant depends on neither `u` nor `ε`.

```lean
TauCeti.PDE.exists_eLpNorm_rpow_le_mul_eLpNorm_rpow_lowerOrder.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] :
  ∃ C,
    0 ≤ C ∧
      ∀ (mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)) [inst : mu.IsAddHaarMeasure]
        {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
        {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι}
        {c : EuclideanSpace ℝ ι → ℝ} {lam Lam beta gamma : ℝ} {q : ENNReal} {S : NNReal}
        {u : ↥(TauCeti.W1p mu Omega 2)} {ε p : ℝ} {x₀ : EuclideanSpace ℝ ι} {r ρ : ℝ},
        TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
          MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
            MeasureTheory.AEStronglyMeasurable b (mu.restrict ↑Omega) →
              MeasureTheory.AEStronglyMeasurable c (mu.restrict ↑Omega) →
                (∀ x ∈ ↑Omega, ‖b x‖ ≤ beta) →
                  (∀ x ∈ ↑Omega, ‖c x‖ ≤ gamma) →
                    (∀ v ∈ TauCeti.w1p0Submodule mu Omega 2,
                        MeasureTheory.eLpNorm (↑↑(TauCeti.W1p.value v)) q (mu.restrict ↑Omega) ≤
                          ↑S * ‖TauCeti.W1p.gradient v‖ₑ) →
                      (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                          (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega,
                              0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
                            0 ≤ TauCeti.PDE.energyFormH1 a b c u ↑v) →
                        0 < ε →
                          (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega,
                              ε ≤ ↑↑(TauCeti.W1p.value u) x) →
                            p < 1 →
                              0 < r →
                                r < ρ →
                                  Metric.ball x₀ ρ ⊆ ↑Omega →
                                    MeasureTheory.eLpNorm
                                        (fun x => ↑↑(TauCeti.W1p.value u) x ^ (p / 2)) q
                                        (mu.restrict (Metric.ball x₀ r)) ≤
                                      ↑S *
                                          ENNReal.ofReal
                                            (C *
                                              ((1 + |p| * Lam / ((1 - p) * lam)) / (ρ - r) +
                                                |p| / ((1 - p) * lam) *
                                                  √(beta ^ 2 + (1 - p) * lam * gamma))) *
                                        MeasureTheory.eLpNorm
                                          (fun x => ↑↑(TauCeti.W1p.value u) x ^ (p / 2)) 2
                                          (mu.restrict (Metric.ball x₀ ρ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The `L²` Leibniz estimate](../../sobolev/part-01/the-l2-leibniz-estimate.md)
- [The Caccioppoli inequality](../part-01/the-caccioppoli-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_eLpNorm_rpow_le_mul_eLpNorm_rpow_lowerOrder`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/ReverseHolder.html#TauCeti.PDE.exists_eLpNorm_rpow_le_mul_eLpNorm_rpow_lowerOrder).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_eLpNorm_rpow_le_mul_eLpNorm_rpow_lowerOrder`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/ReverseHolder.html#TauCeti.PDE.exists_eLpNorm_rpow_le_mul_eLpNorm_rpow_lowerOrder)
- [Source of `TauCeti.PDE.exists_eLpNorm_rpow_le_mul_eLpNorm_rpow_lowerOrder` in TauCeti/Analysis/PDE/Regularity/ReverseHolder.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Regularity/ReverseHolder.lean#L286)

---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_eLpNorm_rpow_le_mul_eLpNorm_rpow
statement: formalized
proof: formalized
---

# Moser's reverse Hölder inequality for powers of a positive supersolution

There is a
constant `C ≥ 0`, depending only on the dimension, with the following property. Let `a` be
measurable and uniformly elliptic on `Ω` with constants `0 < λ ≤ Λ`, and suppose that
`W^{1,2}_0(Ω)` satisfies the Sobolev inequality `‖v‖_q ≤ S ‖∇v‖₂`. Let `u ∈ H¹(Ω)` be a weak
supersolution of `-∂ᵢ(aⁱʲ ∂ⱼu) ≥ 0`, that is `a(u, v) ≥ 0` for every nonnegative
`v ∈ H¹₀(Ω)`, with `u ≥ ε` almost everywhere for some `ε > 0`. Then for every `p < 1` and all
concentric balls `B(x₀, r) ⊂ B(x₀, ρ) ⊆ Ω`,

`‖u^{p/2}‖_{L^q(B(x₀, r))} ≤ S C (1 + |p| Λ / ((1 - p) λ)) / (ρ - r) · ‖u^{p/2}‖_{L²(B(x₀, ρ))}`.

The constant depends on neither `u` nor `ε`.

```lean
TauCeti.PDE.exists_eLpNorm_rpow_le_mul_eLpNorm_rpow.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] :
  ∃ C,
    0 ≤ C ∧
      ∀ (mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)) [inst : mu.IsAddHaarMeasure]
        {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
        {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {lam Lam : ℝ} {q : ENNReal} {S : NNReal}
        {u : ↥(TauCeti.W1p mu Omega 2)} {ε p : ℝ} {x₀ : EuclideanSpace ℝ ι} {r ρ : ℝ},
        TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
          MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
            (∀ v ∈ TauCeti.w1p0Submodule mu Omega 2,
                MeasureTheory.eLpNorm (↑↑(TauCeti.W1p.value v)) q (mu.restrict ↑Omega) ≤
                  ↑S * ‖TauCeti.W1p.gradient v‖ₑ) →
              (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                  (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega,
                      0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
                    0 ≤ TauCeti.PDE.energyFormH1 a 0 0 u ↑v) →
                0 < ε →
                  (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, ε ≤ ↑↑(TauCeti.W1p.value u) x) →
                    p < 1 →
                      0 < r →
                        r < ρ →
                          Metric.ball x₀ ρ ⊆ ↑Omega →
                            MeasureTheory.eLpNorm (fun x => ↑↑(TauCeti.W1p.value u) x ^ (p / 2)) q
                                (mu.restrict (Metric.ball x₀ r)) ≤
                              ↑S *
                                  ENNReal.ofReal (C * (1 + |p| * Lam / ((1 - p) * lam)) / (ρ - r)) *
                                MeasureTheory.eLpNorm (fun x => ↑↑(TauCeti.W1p.value u) x ^ (p / 2))
                                  2 (mu.restrict (Metric.ball x₀ ρ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The `L²` Leibniz estimate](../../part-03/sobolev/part-01/the-l2-leibniz-estimate.md)
- [The Caccioppoli inequality](../../part-03/pde/part-01/the-caccioppoli-inequality.md)
- [TauCeti.Wkp](tauceti-wkp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_eLpNorm_rpow_le_mul_eLpNorm_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/ReverseHolder.html#TauCeti.PDE.exists_eLpNorm_rpow_le_mul_eLpNorm_rpow).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_eLpNorm_rpow_le_mul_eLpNorm_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/ReverseHolder.html#TauCeti.PDE.exists_eLpNorm_rpow_le_mul_eLpNorm_rpow)
- [Source of `TauCeti.PDE.exists_eLpNorm_rpow_le_mul_eLpNorm_rpow` in TauCeti/Analysis/PDE/Regularity/ReverseHolder.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Regularity/ReverseHolder.lean#L151)

---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_ae_inv_value_le_mul_rpow_mul_setIntegral_rpow
statement: formalized
proof: formalized
---

# Moser's lower bound from small negative powers

For every `0 < p ≤ 2` and every
positive weak supersolution in any dimension `n ≥ 1`,
`u⁻¹ ≤ D R^{-n/p} (∫_{B(x₀, R)} u⁻ᵖ)^{1/p}` almost everywhere on `B(x₀, R/2)`.
The constant depends only on `λ`, `Λ`, `p`, the dimension and Haar normalization, not on the
positive lower bound for `u`. No boundary regularity is required.

```lean
TauCeti.PDE.exists_ae_inv_value_le_mul_rpow_mul_setIntegral_rpow.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  {lam Lam : ℝ} [Nonempty ι] {p : ℝ} (hp : 0 < p) (hp2 : p ≤ 2) :
  ∃ D,
    0 < D ∧
      ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
        {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {u : ↥(TauCeti.W1p mu Omega 2)} {m : ℝ}
        {x₀ : EuclideanSpace ℝ ι} {R : ℝ},
        TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
          MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
            (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)),
                (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value ↑v) x) →
                  0 ≤ TauCeti.PDE.energyFormH1 a 0 0 u ↑v) →
              0 < m →
                (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, m ≤ ↑↑(TauCeti.W1p.value u) x) →
                  0 < R →
                    Metric.ball x₀ R ⊆ ↑Omega →
                      ∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict (Metric.ball x₀ (R / 2)),
                        (↑↑(TauCeti.W1p.value u) x)⁻¹ ≤
                          D * R ^ (-↑(Fintype.card ι) / p) *
                            (∫ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ R,
                                (↑↑(TauCeti.W1p.value u) x)⁻¹ ^ p ∂mu) ^
                              p⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The `L²` Leibniz estimate](../../sobolev/part-01/the-l2-leibniz-estimate.md)
- [The Sobolev inequality for functions of bounded variation](../../../part-01/geometric-measure-theory-rectifiability-bv-and-f/the-sobolev-inequality-for-functions-of-bounded.md)
- [TauCeti.Wkp](../../../part-01/partial-differential-equations/tauceti-wkp.md)
- [The zero-forcing Caccioppoli inequality for a positive truncation of a weak subsolution](../part-02/the-zero-forcing-caccioppoli-inequality-for-a-po.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_ae_inv_value_le_mul_rpow_mul_setIntegral_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Supersolution/Lp.html#TauCeti.PDE.exists_ae_inv_value_le_mul_rpow_mul_setIntegral_rpow).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_ae_inv_value_le_mul_rpow_mul_setIntegral_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Supersolution/Lp.html#TauCeti.PDE.exists_ae_inv_value_le_mul_rpow_mul_setIntegral_rpow)
- [Source of `TauCeti.PDE.exists_ae_inv_value_le_mul_rpow_mul_setIntegral_rpow` in TauCeti/Analysis/PDE/Regularity/Supersolution/Lp.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Regularity/Supersolution/Lp.lean#L76)

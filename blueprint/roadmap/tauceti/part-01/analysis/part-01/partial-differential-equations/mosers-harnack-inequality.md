---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_ae_ae_value_le_mul_value
statement: formalized
proof: formalized
---

# Moser's Harnack inequality

Let `n ≥ 1` be the dimension. There is `C > 0`, depending
only on `λ`, `Λ`, the dimension and the normalization of the additive Haar measure `mu`, with the
following property. Let `a` be measurable and uniformly elliptic on `Ω` with constants `λ, Λ`,
and let `u ∈ H¹(Ω)` be a weak solution of `-∂ᵢ(aⁱʲ ∂ⱼu) = 0`, that is `a(u, v) = 0` for every
`v ∈ H¹₀(Ω)`, with `u ≥ 0` almost everywhere. Then on every ball with `B(x₀, 16√n r) ⊆ Ω`,

`u(y) ≤ C u(x)` for almost every `x, y ∈ B(x₀, r)`,

that is, `ess sup_{B(x₀, r)} u ≤ C ess inf_{B(x₀, r)} u`. The constant does not depend on `u`
or the ball.

```lean
TauCeti.PDE.exists_ae_ae_value_le_mul_value.{u_1} {ι : Type u_1} [Fintype ι] [DecidableEq ι]
  {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure] {lam Lam : ℝ}
  [Nonempty ι] :
  ∃ C,
    0 < C ∧
      ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
        {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {u : ↥(TauCeti.W1p mu Omega 2)}
        {x₀ : EuclideanSpace ℝ ι} {r : ℝ},
        TauCeti.PDE.UniformlyEllipticOn (↑Omega) a lam Lam →
          MeasureTheory.AEStronglyMeasurable a (mu.restrict ↑Omega) →
            (∀ (v : ↥(TauCeti.W1p0 mu Omega 2)), TauCeti.PDE.energyFormH1 a 0 0 u ↑v = 0) →
              (∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict ↑Omega, 0 ≤ ↑↑(TauCeti.W1p.value u) x) →
                Metric.ball x₀ (16 * √↑(Fintype.card ι) * r) ⊆ ↑Omega →
                  ∀ᵐ (x : EuclideanSpace ℝ ι) (y :
                    EuclideanSpace ℝ ι) ∂mu.restrict (Metric.ball x₀ r),
                    ↑↑(TauCeti.W1p.value u) y ≤ C * ↑↑(TauCeti.W1p.value u) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The `L²` Leibniz estimate](../../part-03/sobolev/part-01/the-l2-leibniz-estimate.md)
- [Chebyshev's inequality for truncations](../../../measure-theory/integral/part-01/chebyshevs-inequality-for-truncations.md)
- [Moser's weak Harnack inequality](mosers-weak-harnack-inequality.md)
- [The Sobolev inequality on `W^{1,p}_0` of a ball](../../part-03/sobolev/part-02/the-sobolev-inequality-on-w-1-p-0-of-a-ball.md)
- [TauCeti.Wkp](tauceti-wkp.md)
- [The zero-forcing Caccioppoli inequality for a positive truncation of a weak subsolution](../../part-03/pde/part-03/the-zero-forcing-caccioppoli-inequality-for-a-po.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_ae_ae_value_le_mul_value`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Harnack.html#TauCeti.PDE.exists_ae_ae_value_le_mul_value).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_ae_ae_value_le_mul_value`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Harnack.html#TauCeti.PDE.exists_ae_ae_value_le_mul_value)
- [Source of `TauCeti.PDE.exists_ae_ae_value_le_mul_value` in TauCeti/Analysis/PDE/Regularity/Harnack.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Regularity/Harnack.lean#L287)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PDE/STATUS.md)

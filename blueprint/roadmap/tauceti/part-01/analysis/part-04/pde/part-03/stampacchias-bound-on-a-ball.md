---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_forall_energyFormH1_eq_setIntegral_ae_abs_le
statement: formalized
proof: formalized
---

# Stampacchia's bound on a ball

Let `n ≥ 1` be the dimension and let `r > 1` with
`r > n/2`. There is `K > 0`, depending only on `n`, `r` and the normalization of `mu`, such that
the following holds. Let `a` be measurable and uniformly elliptic on `B = B(x₀, ρ)` with constants
`λ, Λ`, and let `f ∈ Lʳ(B)`. Then there is a weak solution `w ∈ H¹₀(B)` of the Dirichlet problem
`-∂ᵢ(aⁱʲ ∂ⱼw) = f` in `B`, that is `a(w, v) = ∫_B f v` for every `v ∈ H¹₀(B)`, with

`|w| ≤ K ρ^(2 - n/r) ‖f‖_{Lʳ(B)} / λ` almost everywhere on `B`.

This is `TauCeti.PDE.exists_ae_abs_value_le_mul_div_mul_rpow` on a ball, where
`|B|^(2/n - 1/r)` is a multiple of `ρ^(2 - n/r)`.

```lean
TauCeti.PDE.exists_forall_energyFormH1_eq_setIntegral_ae_abs_le.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {mu : MeasureTheory.Measure (EuclideanSpace ℝ ι)} [mu.IsAddHaarMeasure]
  [Nonempty ι] {r : NNReal} (hr : 1 < r) (hrn : ↑(Fintype.card ι) < 2 * ↑r) :
  ∃ K,
    0 < K ∧
      ∀ {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {lam Lam : ℝ} {f : EuclideanSpace ℝ ι → ℝ}
        {x₀ : EuclideanSpace ℝ ι} {ρ : ℝ},
        TauCeti.PDE.UniformlyEllipticOn (Metric.ball x₀ ρ) a lam Lam →
          MeasureTheory.AEStronglyMeasurable a (mu.restrict (Metric.ball x₀ ρ)) →
            MeasureTheory.MemLp f (↑r) (mu.restrict (Metric.ball x₀ ρ)) →
              0 < ρ →
                ∃ w,
                  (∀ (v : ↥(TauCeti.W1p0 mu { carrier := Metric.ball x₀ ρ, is_open' := ⋯ } 2)),
                      TauCeti.PDE.energyFormH1 a 0 0 ↑w ↑v =
                        ∫ (x : EuclideanSpace ℝ ι) in Metric.ball x₀ ρ,
                          f x * ↑↑(TauCeti.W1p.value ↑v) x ∂mu) ∧
                    ∀ᵐ (x : EuclideanSpace ℝ ι) ∂mu.restrict (Metric.ball x₀ ρ),
                      |↑↑(TauCeti.W1p.value ↑w) x| ≤
                        K * ρ ^ (2 - ↑(Fintype.card ι) / ↑r) *
                            (MeasureTheory.eLpNorm f (↑r) (mu.restrict (Metric.ball x₀ ρ))).toReal /
                          lam
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality with a bounded weight](../../../../measure-theory/integral/part-02/holders-inequality-with-a-bounded-weight.md)
- [The Sobolev inequality on `W^{1,p}_0` of a ball](../../sobolev/part-02/the-sobolev-inequality-on-w-1-p-0-of-a-ball.md)
- [Stampacchia's global bound](stampacchias-global-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_forall_energyFormH1_eq_setIntegral_ae_abs_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/GlobalBoundedness.html#TauCeti.PDE.exists_forall_energyFormH1_eq_setIntegral_ae_abs_le).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_forall_energyFormH1_eq_setIntegral_ae_abs_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/GlobalBoundedness.html#TauCeti.PDE.exists_forall_energyFormH1_eq_setIntegral_ae_abs_le)
- [Source of `TauCeti.PDE.exists_forall_energyFormH1_eq_setIntegral_ae_abs_le` in TauCeti/Analysis/PDE/MaximumPrinciple/GlobalBoundedness.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/MaximumPrinciple/GlobalBoundedness.lean#L597)

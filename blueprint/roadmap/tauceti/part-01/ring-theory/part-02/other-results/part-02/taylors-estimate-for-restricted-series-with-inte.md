---
declaration: theorem
origin: cited
lean: TauCeti.Huber.weightedEval_sub_weightedEval_sub_sum_mem_pow_smul
statement: formalized
proof: formalized
---

# Taylor's estimate for restricted series with integral coefficients

Let `ϖ ∈ A₀` be a
unit of `C`. If `x ≡ t mod ϖᵃ` and `x' ≡ x mod ϖᵇ` in `A₀^N` with `a ≤ b`, then the gradient of
`F` at `t` linearises `F` from `x` to `x'` up to an error in `ϖ^(a + b) A₀`.

```lean
TauCeti.Huber.weightedEval_sub_weightedEval_sub_sum_mem_pow_smul.{u_1} {C : Type u_1} [CommRing C]
  [UniformSpace C] [IsUniformAddGroup C] [IsTopologicalRing C] [CompleteSpace C]
  (P : TauCeti.Huber.PairOfDefinition C) {N : ℕ} {ϖ : ↥P.ringOfDefinition} (hϖ : IsUnit ↑ϖ)
  {F : MvPowerSeries (Fin N) C} (hF : TauCeti.Huber.IsWeightedRestricted (fun x => {1}) F)
  (hF₀ : ∀ (ν : Fin N →₀ ℕ), (MvPowerSeries.coeff ν) F ∈ P.ringOfDefinition)
  {t x x' : Fin N → ↥P.ringOfDefinition} {a b : ℕ} (hab : a ≤ b)
  (hx : ∀ (i : Fin N), ϖ ^ a ∣ x i - t i) (hxx' : ∀ (i : Fin N), ϖ ^ b ∣ x' i - x i) :
  TauCeti.Huber.weightedEval (RingHom.id C) (fun i => ↑(x' i)) F -
        TauCeti.Huber.weightedEval (RingHom.id C) (fun i => ↑(x i)) F -
      ∑ j,
        TauCeti.Huber.weightedEval (RingHom.id C) (fun i => ↑(t i)) ((MvPowerSeries.pderiv j) F) *
          (↑(x' j) - ↑(x j)) ∈
    ↑ϖ ^ (a + b) • ↑P.ringOfDefinition
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Taylor's estimate in several variables](../../../../algebra/part-02/other-results/taylors-estimate-in-several-variables.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.weightedEval_sub_weightedEval_sub_sum_mem_pow_smul`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/WeightedEval/Newton.html#TauCeti.Huber.weightedEval_sub_weightedEval_sub_sum_mem_pow_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.weightedEval_sub_weightedEval_sub_sum_mem_pow_smul`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/WeightedEval/Newton.html#TauCeti.Huber.weightedEval_sub_weightedEval_sub_sum_mem_pow_smul)
- [Source of `TauCeti.Huber.weightedEval_sub_weightedEval_sub_sum_mem_pow_smul` in TauCeti/RingTheory/Huber/WeightedEval/Newton.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Huber/WeightedEval/Newton.lean#L68)

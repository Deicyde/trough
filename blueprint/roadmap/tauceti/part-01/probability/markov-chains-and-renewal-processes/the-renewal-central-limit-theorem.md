---
declaration: theorem
origin: cited
lean: TauCeti.Probability.tendstoInDistribution_renewalCountNat_sub_div, TauCeti.Probability.tendstoInDistribution_renewalCountNat_sub_div_toReal_lintegral, TauCeti.Probability.tendstoInDistribution_renewalCountNat_toNNReal_sub_div
statement: formalized
proof: formalized
---

# The renewal central limit theorem

Let `T 0, T 1, …` be independent, identically distributed
nonnegative waiting times with nonzero variance `σ² = Var[T 0; P]` and expectation `μ = P[T 0]`. As
`t → ∞` in `ℝ≥0`, the standardized renewal count `((N_t : ℝ) - t / μ) / (σ * √(t / μ ^ 3))`
converges in distribution to any standard normal random variable `Z`. Precomposing with
`MeasureTheory.TendstoInDistribution.comp_tendsto` gives convergence along any time family (in
particular any sequence) tending to `atTop`.

```lean
TauCeti.Probability.tendstoInDistribution_renewalCountNat_sub_div.{u_1, u_2} {Ω : Type u_1}
  {Ω' : Type u_2} [MeasurableSpace Ω] [MeasurableSpace Ω'] {P : MeasureTheory.Measure Ω}
  [MeasureTheory.IsProbabilityMeasure P] {P' : MeasureTheory.Measure Ω'}
  [MeasureTheory.IsProbabilityMeasure P'] {T : ℕ → Ω → NNReal} {Z : Ω' → ℝ}
  (hZ : ProbabilityTheory.HasLaw Z (ProbabilityTheory.gaussianReal 0 1) P')
  (hindep : ProbabilityTheory.iIndepFun T P)
  (hid : ∀ (n : ℕ), ProbabilityTheory.IdentDistrib (T n) (T 0) P P)
  (hvar : ProbabilityTheory.variance (fun ω => ↑(T 0 ω)) P ≠ 0) :
  MeasureTheory.TendstoInDistribution
    (fun t ω =>
      (↑(TauCeti.Probability.renewalCountNat T t ω) - ↑t / ∫ (x : Ω), (fun ω => ↑(T 0 ω)) x ∂P) /
        (√(ProbabilityTheory.variance (fun ω => ↑(T 0 ω)) P) *
          √(↑t / (∫ (x : Ω), (fun ω => ↑(T 0 ω)) x ∂P) ^ 3)))
    Filter.atTop Z (fun x => P) P'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.tendstoInDistribution_renewalCountNat_sub_div`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/CentralLimitTheorem.html#TauCeti.Probability.tendstoInDistribution_renewalCountNat_sub_div).

## Other forms

**The renewal central limit theorem (extended-mean formulation).** Formalized in Tau Ceti as [`TauCeti.Probability.tendstoInDistribution_renewalCountNat_sub_div_toReal_lintegral`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/CentralLimitTheorem.html#TauCeti.Probability.tendstoInDistribution_renewalCountNat_sub_div_toReal_lintegral).

```lean
TauCeti.Probability.tendstoInDistribution_renewalCountNat_sub_div_toReal_lintegral.{u_1, u_2}
  {Ω : Type u_1} {Ω' : Type u_2} [MeasurableSpace Ω] [MeasurableSpace Ω']
  {P : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure P]
  {P' : MeasureTheory.Measure Ω'} [MeasureTheory.IsProbabilityMeasure P'] {T : ℕ → Ω → NNReal}
  {Z : Ω' → ℝ} (hZ : ProbabilityTheory.HasLaw Z (ProbabilityTheory.gaussianReal 0 1) P')
  (hindep : ProbabilityTheory.iIndepFun T P)
  (hid : ∀ (n : ℕ), ProbabilityTheory.IdentDistrib (T n) (T 0) P P)
  (hvar : ProbabilityTheory.variance (fun ω => ↑(T 0 ω)) P ≠ 0) :
  MeasureTheory.TendstoInDistribution
    (fun t ω =>
      (↑(TauCeti.Probability.renewalCountNat T t ω) - ↑t / (∫⁻ (ω : Ω), ↑(T 0 ω) ∂P).toReal) /
        (√(ProbabilityTheory.variance (fun ω => ↑(T 0 ω)) P) *
          √(↑t / (∫⁻ (ω : Ω), ↑(T 0 ω) ∂P).toReal ^ 3)))
    Filter.atTop Z (fun x => P) P'
```

**The renewal central limit theorem on the real time axis.** Formalized in Tau Ceti as [`TauCeti.Probability.tendstoInDistribution_renewalCountNat_toNNReal_sub_div`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/CentralLimitTheorem.html#TauCeti.Probability.tendstoInDistribution_renewalCountNat_toNNReal_sub_div).

```lean
TauCeti.Probability.tendstoInDistribution_renewalCountNat_toNNReal_sub_div.{u_1, u_2} {Ω : Type u_1}
  {Ω' : Type u_2} [MeasurableSpace Ω] [MeasurableSpace Ω'] {P : MeasureTheory.Measure Ω}
  [MeasureTheory.IsProbabilityMeasure P] {P' : MeasureTheory.Measure Ω'}
  [MeasureTheory.IsProbabilityMeasure P'] {T : ℕ → Ω → NNReal} {Z : Ω' → ℝ}
  (hZ : ProbabilityTheory.HasLaw Z (ProbabilityTheory.gaussianReal 0 1) P')
  (hindep : ProbabilityTheory.iIndepFun T P)
  (hid : ∀ (n : ℕ), ProbabilityTheory.IdentDistrib (T n) (T 0) P P)
  (hvar : ProbabilityTheory.variance (fun ω => ↑(T 0 ω)) P ≠ 0) :
  MeasureTheory.TendstoInDistribution
    (fun t ω =>
      (↑(TauCeti.Probability.renewalCountNat T t.toNNReal ω) -
          t / ∫ (x : Ω), (fun ω => ↑(T 0 ω)) x ∂P) /
        (√(ProbabilityTheory.variance (fun ω => ↑(T 0 ω)) P) *
          √(t / (∫ (x : Ω), (fun ω => ↑(T 0 ω)) x ∂P) ^ 3)))
    Filter.atTop Z (fun x => P) P'
```

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.tendstoInDistribution_renewalCountNat_sub_div`](https://taucetiproject.org/docs/TauCeti/Probability/Renewal/CentralLimitTheorem.html#TauCeti.Probability.tendstoInDistribution_renewalCountNat_sub_div)
- [Source of `TauCeti.Probability.tendstoInDistribution_renewalCountNat_sub_div` in TauCeti/Probability/Renewal/CentralLimitTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Renewal/CentralLimitTheorem.lean#L362)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)

---
declaration: theorem
origin: cited
lean: ProbabilityTheory.HasIndepIncrements.hasLaw_sub_poissonMeasure_iff_stationary_small_time
statement: formalized
proof: formalized
---

# The microscopic characterization of Poisson counts

For a count process starting at
zero with independent increments and pairwise almost-sure monotonicity, all increments have
rate-`r` Poisson laws if and only if they are stationary and satisfy the one- and
multiple-occurrence limits at zero. The rate may be zero.

```lean
ProbabilityTheory.HasIndepIncrements.hasLaw_sub_poissonMeasure_iff_stationary_small_time.{u_1}
  {Ω : Type u_1} [MeasurableSpace Ω] {P : MeasureTheory.Measure Ω} {N : NNReal → Ω → ℕ}
  (hN : ProbabilityTheory.HasIndepIncrements N P) (h0 : ∀ᵐ (ω : Ω) ∂P, N 0 ω = 0)
  (hmono : ∀ (s t : NNReal), s ≤ t → ∀ᵐ (ω : Ω) ∂P, N s ω ≤ N t ω) (r : NNReal) :
  (∀ (s t : NNReal),
      s ≤ t →
        ProbabilityTheory.HasLaw (fun ω => N t ω - N s ω)
          (ProbabilityTheory.poissonMeasure (r * (t - s))) P) ↔
    (∀ (s t : NNReal), ProbabilityTheory.IdentDistrib (fun ω => N (s + t) ω - N s ω) (N t) P P) ∧
      Filter.Tendsto (fun h => P.real {ω | N h ω = 1} / ↑h) (nhdsWithin 0 (Set.Ioi 0)) (nhds ↑r) ∧
        Filter.Tendsto (fun h => P.real {ω | 2 ≤ N h ω} / ↑h) (nhdsWithin 0 (Set.Ioi 0)) (nhds 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ProbabilityTheory.HasIndepIncrements.hasLaw_sub_poissonMeasure_iff_stationary_small_time`](https://taucetiproject.org/docs/TauCeti/Probability/Process/Poisson/Microscopic.html#ProbabilityTheory.HasIndepIncrements.hasLaw_sub_poissonMeasure_iff_stationary_small_time).

## Sources

- [Tau Ceti documentation: `ProbabilityTheory.HasIndepIncrements.hasLaw_sub_poissonMeasure_iff_stationary_small_time`](https://taucetiproject.org/docs/TauCeti/Probability/Process/Poisson/Microscopic.html#ProbabilityTheory.HasIndepIncrements.hasLaw_sub_poissonMeasure_iff_stationary_small_time)
- [Source of `ProbabilityTheory.HasIndepIncrements.hasLaw_sub_poissonMeasure_iff_stationary_small_time` in TauCeti/Probability/Process/Poisson/Microscopic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Process/Poisson/Microscopic.lean#L76)
- [Tau Ceti roadmap status: Markov chains and renewal processes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MarkovChainsAndRenewal/STATUS.md)

---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.not_differentiableOn_of_LSeriesHasSum_one
statement: formalized
proof: formalized
---

# TauCeti.LSeries.not_differentiableOn_of_LSeriesHasSum_one

Constant coefficients cannot have the analytic continuation required by the bounded
Dirichlet endpoint theorem: that would make the harmonic partial sums converge.

```lean
TauCeti.LSeries.not_differentiableOn_of_LSeriesHasSum_one {Ω : Set ℂ} {F : ℂ → ℂ} (hΩ : IsOpen Ω)
  (hcover : {s | 1 ≤ s.re} ⊆ Ω)
  (hseries : ∀ (s : ℂ), 1 < s.re → LSeriesHasSum (fun x => 1) s (F s)) : ¬DifferentiableOn ℂ F Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bounded Dirichlet series converge in order at `s = 1`](bounded-dirichlet-series-converge-in-order-at-s.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.not_differentiableOn_of_LSeriesHasSum_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/RejectionTests.html#TauCeti.LSeries.not_differentiableOn_of_LSeriesHasSum_one).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.not_differentiableOn_of_LSeriesHasSum_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/RejectionTests.html#TauCeti.LSeries.not_differentiableOn_of_LSeriesHasSum_one)
- [Source of `TauCeti.LSeries.not_differentiableOn_of_LSeriesHasSum_one` in TauCeti/NumberTheory/LSeries/BoundaryConvergence/RejectionTests.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/BoundaryConvergence/RejectionTests.lean#L112)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)

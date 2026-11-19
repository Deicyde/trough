---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.boundedDirichlet_tendsto_ordered_at_one
statement: formalized
proof: formalized
---

# Bounded Dirichlet series converge in order at `s = 1`

Let `a : ℕ → ℂ` be bounded from
`n = 1` on, and let `F` be holomorphic on an open set `Ω` containing the closed half-plane
`1 ≤ re s`, with `LSeriesHasSum a s (F s)` for `1 < re s`. Then the ordered partial sums
`∑ n ∈ Finset.Icc 1 N, a n / n` converge to `F 1`.

This is a limit of ordered cutoffs, not an unconditional sum: the Dirichlet series of `a` need not
converge absolutely at `s = 1`.

```lean
TauCeti.LSeries.boundedDirichlet_tendsto_ordered_at_one {a : ℕ → ℂ} {M : ℝ}
  (hbound : ∀ (n : ℕ), 1 ≤ n → ‖a n‖ ≤ M) {Ω : Set ℂ} (hΩ : IsOpen Ω) (hcover : {s | 1 ≤ s.re} ⊆ Ω)
  {F : ℂ → ℂ} (hF : DifferentiableOn ℂ F Ω)
  (hseries : ∀ (s : ℂ), 1 < s.re → LSeriesHasSum a s (F s)) :
  Filter.Tendsto (fun N => ∑ n ∈ Finset.Icc 1 N, a n / ↑n) Filter.atTop (nhds (F 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Newman's Tauberian theorem](newmans-tauberian-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.boundedDirichlet_tendsto_ordered_at_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/Endpoint.html#TauCeti.LSeries.boundedDirichlet_tendsto_ordered_at_one).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.boundedDirichlet_tendsto_ordered_at_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/Endpoint.html#TauCeti.LSeries.boundedDirichlet_tendsto_ordered_at_one)
- [Source of `TauCeti.LSeries.boundedDirichlet_tendsto_ordered_at_one` in TauCeti/NumberTheory/LSeries/BoundaryConvergence/Endpoint.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/BoundaryConvergence/Endpoint.lean#L139)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)

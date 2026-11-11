---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.tendsto_LSeries_nhdsGT_one
statement: formalized
proof: formalized
---

# Abelian theorem for Dirichlet series at `s = 1`

If the ordered partial sums
`∑ n ∈ Icc 1 N, a n / n` tend to `L` and the Dirichlet series of `a` converges absolutely at
every real `σ > 1`, then `LSeries a σ → L` as `σ` decreases to `1`.

```lean
TauCeti.LSeries.tendsto_LSeries_nhdsGT_one {a : ℕ → ℂ} {L : ℂ}
  (hlim : Filter.Tendsto (fun N => ∑ n ∈ Finset.Icc 1 N, a n / ↑n) Filter.atTop (nhds L))
  (hsum : ∀ (σ : ℝ), 1 < σ → LSeriesSummable a ↑σ) :
  Filter.Tendsto (fun σ => LSeries a ↑σ) (nhdsWithin 1 (Set.Ioi 1)) (nhds L)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.tendsto_LSeries_nhdsGT_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/Basic.html#TauCeti.LSeries.tendsto_LSeries_nhdsGT_one).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.tendsto_LSeries_nhdsGT_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/Basic.html#TauCeti.LSeries.tendsto_LSeries_nhdsGT_one)
- [Source of `TauCeti.LSeries.tendsto_LSeries_nhdsGT_one` in TauCeti/NumberTheory/LSeries/BoundaryConvergence/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LSeries/BoundaryConvergence/Basic.lean#L63)

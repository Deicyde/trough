---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.meromorphicOrderAt_lt_zero_of_eq_LSeries
statement: formalized
proof: formalized
---

# Meromorphic form of Landau's theorem

Let `F` be a meromorphic continuation of a
Dirichlet series with nonnegative coefficients to a neighborhood of its finite, actual abscissa
of absolute convergence. Then the meromorphic order of `F` at that abscissa is negative. In
particular, the singularity forced by `landau` is a pole, not a removable singularity.

Meromorphicity and meromorphic order depend only on the punctured germ, so no convention is
imposed on the value of `F` at the centre.

```lean
TauCeti.LSeries.meromorphicOrderAt_lt_zero_of_eq_LSeries {a : ℕ → ℂ} (ha : 0 ≤ a) {σ r : ℝ}
  (habs : LSeries.abscissaOfAbsConv a = ↑σ) (hr : 0 < r) {F : ℂ → ℂ} (hF : MeromorphicAt F ↑σ)
  (hFeq : ∀ s ∈ Metric.ball (↑σ) r, σ < s.re → F s = LSeries a s) : meromorphicOrderAt F ↑σ < 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Landau's theorem](landaus-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.meromorphicOrderAt_lt_zero_of_eq_LSeries`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Landau.html#TauCeti.LSeries.meromorphicOrderAt_lt_zero_of_eq_LSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.meromorphicOrderAt_lt_zero_of_eq_LSeries`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Landau.html#TauCeti.LSeries.meromorphicOrderAt_lt_zero_of_eq_LSeries)
- [Source of `TauCeti.LSeries.meromorphicOrderAt_lt_zero_of_eq_LSeries` in TauCeti/NumberTheory/LSeries/Landau.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LSeries/Landau.lean#L354)

---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.isBigO_sum_Icc_norm_id_of_boundary
statement: formalized
proof: formalized
---

# The Chebyshev bound

Nonnegative coefficients whose Dirichlet series is summable on
`Re s > 1` and has a boundary remainder `G = LSeries a - A / (s - 1)` continuous on `Re s ≥ 1`
satisfy `∑_{1 ≤ n ≤ t} ‖a n‖ = O(t)`.

```lean
TauCeti.LSeries.isBigO_sum_Icc_norm_id_of_boundary {a : ℕ → ℂ} {A : ℂ} {G : ℂ → ℂ} (ha : 0 ≤ a)
  (hG : ContinuousOn G {z | 1 ≤ z.re}) (hG' : ∀ (z : ℂ), 1 < z.re → G z = LSeries a z - A / (z - 1))
  (hsum : ∀ (sigma : ℝ), 1 < sigma → LSeriesSummable a ↑sigma) :
  (fun t => ∑ n ∈ Finset.Icc 1 ⌊t⌋₊, ‖a n‖) =O[Filter.atTop] fun t => t
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Riemann--Lebesgue on a vertical line](../../../analysis/part-02/fourier/riemann-lebesgue-on-a-vertical-line.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.isBigO_sum_Icc_norm_id_of_boundary`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/WienerIkehara/Chebyshev.html#TauCeti.LSeries.isBigO_sum_Icc_norm_id_of_boundary).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.isBigO_sum_Icc_norm_id_of_boundary`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/WienerIkehara/Chebyshev.html#TauCeti.LSeries.isBigO_sum_Icc_norm_id_of_boundary)
- [Source of `TauCeti.LSeries.isBigO_sum_Icc_norm_id_of_boundary` in TauCeti/NumberTheory/LSeries/WienerIkehara/Chebyshev.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LSeries/WienerIkehara/Chebyshev.lean#L159)

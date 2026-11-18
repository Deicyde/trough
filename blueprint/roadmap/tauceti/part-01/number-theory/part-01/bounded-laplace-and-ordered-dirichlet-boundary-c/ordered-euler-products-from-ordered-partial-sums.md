---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.tendsto_prod_primesLE_inv_of_tendsto_sum
statement: formalized
proof: formalized
---

# Ordered Euler products from ordered partial sums

If the ordered partial sums
`∑ n ∈ Icc 1 N, a n / n` converge to `L`, then the finite Euler products
`∏ p ≤ N, (1 - c p / p)⁻¹` converge to `exp L`; in particular, their limit is nonzero.

```lean
TauCeti.LSeries.tendsto_prod_primesLE_inv_of_tendsto_sum {a c : ℕ → ℂ}
  (hc : ∀ (p : ℕ), Nat.Prime p → ‖c p‖ ≤ 1) (ha : ∀ (n : ℕ), ¬IsPrimePow n → a n = 0)
  (ha_pow : ∀ (p k : ℕ), Nat.Prime p → k ≠ 0 → a (p ^ k) = c p ^ k / ↑k) {L : ℂ}
  (hL : Filter.Tendsto (fun N => ∑ n ∈ Finset.Icc 1 N, a n / ↑n) Filter.atTop (nhds L)) :
  Filter.Tendsto (fun N => ∏ p ∈ N.primesLE, (1 - c p / ↑p)⁻¹) Filter.atTop (nhds (Complex.exp L))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.tendsto_prod_primesLE_inv_of_tendsto_sum`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/OrderedEulerProduct.html#TauCeti.LSeries.tendsto_prod_primesLE_inv_of_tendsto_sum).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.tendsto_prod_primesLE_inv_of_tendsto_sum`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/OrderedEulerProduct.html#TauCeti.LSeries.tendsto_prod_primesLE_inv_of_tendsto_sum)
- [Source of `TauCeti.LSeries.tendsto_prod_primesLE_inv_of_tendsto_sum` in TauCeti/NumberTheory/LSeries/BoundaryConvergence/OrderedEulerProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/BoundaryConvergence/OrderedEulerProduct.lean#L126)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)

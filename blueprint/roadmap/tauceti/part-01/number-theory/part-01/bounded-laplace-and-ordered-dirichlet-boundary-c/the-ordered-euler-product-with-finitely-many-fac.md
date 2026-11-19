---
declaration: theorem
origin: cited
lean: DirichletCharacter.tendsto_prod_primesLE_filter_notMem_inv_LFunction_one
statement: formalized
proof: formalized
---

# The ordered Euler product with finitely many factors deleted

For a nontrivial Dirichlet
character `χ` of positive level and a finite set `S` of primes, the finite Euler products over
the primes `p ≤ B` outside `S` converge to `L(χ, 1) * ∏ p ∈ S, (1 - χ p / p)` as `B → ∞`.

```lean
DirichletCharacter.tendsto_prod_primesLE_filter_notMem_inv_LFunction_one {N : ℕ}
  (χ : DirichletCharacter ℂ N) [NeZero N] (hχ : χ ≠ 1) {S : Finset ℕ} (hS : ∀ p ∈ S, Nat.Prime p) :
  Filter.Tendsto (fun B => ∏ p ∈ B.primesLE with p ∉ S, (1 - χ ↑p / ↑p)⁻¹) Filter.atTop
    (nhds (DirichletCharacter.LFunction χ 1 * ∏ p ∈ S, (1 - χ ↑p / ↑p)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bounded Dirichlet series converge in order at `s = 1`](bounded-dirichlet-series-converge-in-order-at-s.md)
- [DirichletCharacter.eulerLogCoeff](dirichletcharacter-eulerlogcoeff.md)
- [The logarithm of a Dirichlet `L`-function continues across `re s = 1`](the-logarithm-of-a-dirichlet-l-function-continue.md)
- [Ordered Euler products from ordered partial sums](ordered-euler-products-from-ordered-partial-sums.md)

## Lean

Formalized in Tau Ceti as [`DirichletCharacter.tendsto_prod_primesLE_filter_notMem_inv_LFunction_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.html#DirichletCharacter.tendsto_prod_primesLE_filter_notMem_inv_LFunction_one).

## Sources

- [Tau Ceti documentation: `DirichletCharacter.tendsto_prod_primesLE_filter_notMem_inv_LFunction_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.html#DirichletCharacter.tendsto_prod_primesLE_filter_notMem_inv_LFunction_one)
- [Source of `DirichletCharacter.tendsto_prod_primesLE_filter_notMem_inv_LFunction_one` in TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.lean#L111)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)

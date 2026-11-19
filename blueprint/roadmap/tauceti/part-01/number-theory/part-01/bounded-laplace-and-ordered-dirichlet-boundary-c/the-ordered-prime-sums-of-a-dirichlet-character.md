---
declaration: theorem
origin: cited
lean: DirichletCharacter.exists_tendsto_sum_primesLE_div
statement: formalized
proof: formalized
---

# The ordered prime sums of a Dirichlet character at `s = 1`

For a nontrivial Dirichlet
character `χ` of positive level, the ordered sums `∑ p ≤ B, χ p / p` over the primes up to `B`
converge. Their limit `ℓ` satisfies `exp (ℓ + T) = L(χ, 1)`, where `T` is the absolutely
convergent sum of the higher-prime-power terms `χ p ^ (k + 2) / ((k + 2) * p ^ (k + 2))`.

This is a limit of ordered cutoffs; no unconditional sum of `χ p / p` over the primes is
asserted.

```lean
DirichletCharacter.exists_tendsto_sum_primesLE_div {N : ℕ} (χ : DirichletCharacter ℂ N) [NeZero N]
  (hχ : χ ≠ 1) :
  ∃ ℓ,
    Filter.Tendsto (fun B => ∑ p ∈ B.primesLE, χ ↑p / ↑p) Filter.atTop (nhds ℓ) ∧
      Complex.exp
          (ℓ + ∑' (q : Nat.Primes × ℕ), χ ↑↑q.1 ^ (q.2 + 2) / (↑(q.2 + 2) * ↑↑q.1 ^ (q.2 + 2))) =
        DirichletCharacter.LFunction χ 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bounded Dirichlet series converge in order at `s = 1`](bounded-dirichlet-series-converge-in-order-at-s.md)
- [DirichletCharacter.eulerLogCoeff](dirichletcharacter-eulerlogcoeff.md)
- [The logarithm of a Dirichlet `L`-function continues across `re s = 1`](the-logarithm-of-a-dirichlet-l-function-continue.md)

## Lean

Formalized in Tau Ceti as [`DirichletCharacter.exists_tendsto_sum_primesLE_div`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.html#DirichletCharacter.exists_tendsto_sum_primesLE_div).

## Sources

- [Tau Ceti documentation: `DirichletCharacter.exists_tendsto_sum_primesLE_div`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.html#DirichletCharacter.exists_tendsto_sum_primesLE_div)
- [Source of `DirichletCharacter.exists_tendsto_sum_primesLE_div` in TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.lean#L150)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)

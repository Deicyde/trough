---
declaration: theorem
origin: cited
lean: DirichletCharacter.not_tendsto_prod_primesLE_inv_one
statement: formalized
proof: formalized
---

# DirichletCharacter.not_tendsto_prod_primesLE_inv_one

For the trivial Dirichlet character `1` of positive level, the ordered Euler products
`∏ p ≤ B, (1 - 1 p / p)⁻¹` have no limit in `ℂ`. Thus the hypothesis `χ ≠ 1` of
`DirichletCharacter.tendsto_prod_primesLE_inv_LFunction_one` cannot be dropped.

```lean
DirichletCharacter.not_tendsto_prod_primesLE_inv_one {N : ℕ} [NeZero N] (L : ℂ) :
  ¬Filter.Tendsto (fun B => ∏ p ∈ B.primesLE, (1 - 1 ↑p / ↑p)⁻¹) Filter.atTop (nhds L)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`DirichletCharacter.not_tendsto_prod_primesLE_inv_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/TrivialCharacter.html#DirichletCharacter.not_tendsto_prod_primesLE_inv_one).

## Sources

- [Tau Ceti documentation: `DirichletCharacter.not_tendsto_prod_primesLE_inv_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/TrivialCharacter.html#DirichletCharacter.not_tendsto_prod_primesLE_inv_one)
- [Source of `DirichletCharacter.not_tendsto_prod_primesLE_inv_one` in TauCeti/NumberTheory/LSeries/BoundaryConvergence/TrivialCharacter.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/BoundaryConvergence/TrivialCharacter.lean#L104)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)

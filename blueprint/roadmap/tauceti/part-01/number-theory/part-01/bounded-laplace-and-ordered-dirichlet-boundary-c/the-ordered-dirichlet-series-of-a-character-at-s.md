---
declaration: theorem
origin: cited
lean: DirichletCharacter.tendsto_sum_Icc_div_LFunction_one
statement: formalized
proof: formalized
---

# The ordered Dirichlet series of a character at `s = 1`

For a nontrivial Dirichlet
character `χ` of positive level, the ordered partial sums `∑ n ∈ Icc 1 K, χ n / n` converge to
`L(χ, 1)`. This is a limit of ordered cutoffs: the series `∑ χ n / n` does not converge
absolutely (Mathlib's `DirichletCharacter.not_LSeriesSummable_at_one`), and no unconditional
`HasSum` is asserted.

```lean
DirichletCharacter.tendsto_sum_Icc_div_LFunction_one {N : ℕ} (χ : DirichletCharacter ℂ N) [NeZero N]
  (hχ : χ ≠ 1) :
  Filter.Tendsto (fun K => ∑ n ∈ Finset.Icc 1 K, χ ↑n / ↑n) Filter.atTop
    (nhds (DirichletCharacter.LFunction χ 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bounded Dirichlet series converge in order at `s = 1`](bounded-dirichlet-series-converge-in-order-at-s.md)

## Lean

Formalized in Tau Ceti as [`DirichletCharacter.tendsto_sum_Icc_div_LFunction_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.html#DirichletCharacter.tendsto_sum_Icc_div_LFunction_one).

## Sources

- [Tau Ceti documentation: `DirichletCharacter.tendsto_sum_Icc_div_LFunction_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.html#DirichletCharacter.tendsto_sum_Icc_div_LFunction_one)
- [Source of `DirichletCharacter.tendsto_sum_Icc_div_LFunction_one` in TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.lean#L85)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)

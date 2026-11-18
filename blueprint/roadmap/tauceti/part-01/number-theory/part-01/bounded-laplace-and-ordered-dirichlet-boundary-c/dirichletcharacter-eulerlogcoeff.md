---
declaration: def
origin: cited
lean: DirichletCharacter.eulerLogCoeff
statement: formalized
---

# DirichletCharacter.eulerLogCoeff

The coefficients `χ n * Λ n / log n` of the logarithm of the Euler product of the Dirichlet
`L`-function `L(χ, s)`: by `DirichletCharacter.eulerLogCoeff_prime_pow` they are `χ p ^ k / k` at a
prime power `p ^ k`, and they vanish elsewhere.

```lean
DirichletCharacter.eulerLogCoeff {N : ℕ} (χ : DirichletCharacter ℂ N) (n : ℕ) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`DirichletCharacter.eulerLogCoeff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/DirichletEulerLog.html#DirichletCharacter.eulerLogCoeff).

## Sources

- [Tau Ceti documentation: `DirichletCharacter.eulerLogCoeff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/DirichletEulerLog.html#DirichletCharacter.eulerLogCoeff)
- [Source of `DirichletCharacter.eulerLogCoeff` in TauCeti/NumberTheory/LSeries/DirichletEulerLog.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/DirichletEulerLog.lean#L56)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)

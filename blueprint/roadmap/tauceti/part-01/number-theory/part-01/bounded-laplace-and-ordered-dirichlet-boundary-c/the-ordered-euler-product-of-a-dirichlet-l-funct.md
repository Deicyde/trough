---
declaration: theorem
origin: cited
lean: DirichletCharacter.tendsto_prod_primesLE_inv_LFunction_one
statement: formalized
proof: formalized
---

# The ordered Euler product of a Dirichlet `L`-function at `s = 1`

For a nontrivial
Dirichlet character `χ` of positive level, the finite Euler products `∏ p ≤ B, (1 - χ p / p)⁻¹`
converge to `L(χ, 1)` as `B → ∞`. This is a limit of ordered cutoffs, not an unconditional
product.

```lean
DirichletCharacter.tendsto_prod_primesLE_inv_LFunction_one {N : ℕ} (χ : DirichletCharacter ℂ N)
  [NeZero N] (hχ : χ ≠ 1) :
  Filter.Tendsto (fun B => ∏ p ∈ B.primesLE, (1 - χ ↑p / ↑p)⁻¹) Filter.atTop
    (nhds (DirichletCharacter.LFunction χ 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The ordered Euler product with finitely many factors deleted](the-ordered-euler-product-with-finitely-many-fac.md)

## Lean

Formalized in Tau Ceti as [`DirichletCharacter.tendsto_prod_primesLE_inv_LFunction_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.html#DirichletCharacter.tendsto_prod_primesLE_inv_LFunction_one).

## Sources

- [Tau Ceti documentation: `DirichletCharacter.tendsto_prod_primesLE_inv_LFunction_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.html#DirichletCharacter.tendsto_prod_primesLE_inv_LFunction_one)
- [Source of `DirichletCharacter.tendsto_prod_primesLE_inv_LFunction_one` in TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LSeries/BoundaryConvergence/DirichletEulerProduct.lean#L125)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)

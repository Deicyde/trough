---
declaration: structure
origin: cited
lean: TauCeti.FiniteQuotientTower
statement: formalized
---

# TauCeti.FiniteQuotientTower

A **tower of finite quotients** of a topological group `Γ`: continuous surjective
homomorphisms `q n : Γ → A n` onto discrete groups, with transition homomorphisms
`t h : A n → A m` for `m ≤ n` compatible with the projections, such that the projections separate
the points of `Γ`.

The transition homomorphisms are determined by the projections (`FiniteQuotientTower.ext`).
When `Γ` is compact the groups `A n` are finite (`FiniteQuotientTower.finite`) and the kernels of
the projections are cofinal among the open subgroups
(`FiniteQuotientTower.exists_ker_le_of_isOpen`).

```lean
TauCeti.FiniteQuotientTower.{u_1, u_2} (Γ : Type u_1) [Group Γ] [TopologicalSpace Γ]
  (A : ℕ → Type u_2) [(n : ℕ) → Group (A n)] [(n : ℕ) → TopologicalSpace (A n)]
  [∀ (n : ℕ), DiscreteTopology (A n)] : Type (max u_1 u_2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteQuotientTower`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/QuotientTower.html#TauCeti.FiniteQuotientTower).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteQuotientTower`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/QuotientTower.html#TauCeti.FiniteQuotientTower)
- [Source of `TauCeti.FiniteQuotientTower` in TauCeti/Topology/Algebra/Group/Profinite/QuotientTower.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/QuotientTower.lean#L82)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)

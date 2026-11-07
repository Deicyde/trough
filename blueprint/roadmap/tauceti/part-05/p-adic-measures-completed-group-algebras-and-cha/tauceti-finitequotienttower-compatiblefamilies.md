---
declaration: def
origin: cited
lean: TauCeti.FiniteQuotientTower.compatibleFamilies
statement: formalized
---

# TauCeti.FiniteQuotientTower.compatibleFamilies

The **compatible families** along a tower: the families of finitely supported coefficients
`c n : A n →₀ R` such that pushing `c n` forward along the transition map to a level `m ≤ n`,
which sums the coefficients over each fibre, gives `c m`.

```lean
TauCeti.FiniteQuotientTower.compatibleFamilies.{u_1, u_2, u_4} {Γ : Type u_1} [Group Γ]
  [TopologicalSpace Γ] {A : ℕ → Type u_2} [(n : ℕ) → Group (A n)] [(n : ℕ) → TopologicalSpace (A n)]
  [∀ (n : ℕ), DiscreteTopology (A n)] (T : TauCeti.FiniteQuotientTower Γ A) (R : Type u_4)
  [Semiring R] : Submodule R ((n : ℕ) → A n →₀ R)
```

## Depends on

- [TauCeti.FiniteQuotientTower](tauceti-finitequotienttower.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteQuotientTower.compatibleFamilies`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/QuotientTower.html#TauCeti.FiniteQuotientTower.compatibleFamilies).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteQuotientTower.compatibleFamilies`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/QuotientTower.html#TauCeti.FiniteQuotientTower.compatibleFamilies)
- [Source of `TauCeti.FiniteQuotientTower.compatibleFamilies` in TauCeti/Topology/Algebra/Group/Profinite/QuotientTower.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/QuotientTower.lean#L341)
- [Tau Ceti roadmap status: P-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)

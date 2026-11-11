---
declaration: def
origin: cited
lean: TauCeti.Place.singularityDegree
statement: formalized
---

# TauCeti.Place.singularityDegree

The **singularity degree** `δ_P = dim_{k'} (𝒪'_P ⧸ 𝒪_P · k')` of `P` in `F' = F · k'`: the
total `k'`-dimensional normalization defect along the fiber over `P` of the curve of `F / k` after
extending the constants to `k'`. The fiber may consist of several points, and `δ_P` sums their
contributions. It is finite (`TauCeti.Place.finiteDimensional_singularityQuotient`), and the genus
drops by the sum of the singularity degrees (`TauCeti.genus_eq_genus_add_finsum_singularityDegree`).

```lean
TauCeti.Place.singularityDegree.{u, u', v, v'} {k : Type u} (k' : Type u') {F : Type v}
  (F' : Type v') [Field k] [Field k'] [Field F] [Field F'] [Algebra k k'] [Algebra k F]
  [Algebra k F'] [Algebra k' F'] [Algebra F F'] [IsScalarTower k k' F'] [IsScalarTower k F F']
  (P : TauCeti.Place k F) [Algebra.IsIntegral k k'] : ℕ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.singularityDegree`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/ConstantExtension/Genus/Change.html#TauCeti.Place.singularityDegree).

## Sources

- [Tau Ceti documentation: `TauCeti.Place.singularityDegree`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/ConstantExtension/Genus/Change.html#TauCeti.Place.singularityDegree)
- [Source of `TauCeti.Place.singularityDegree` in TauCeti/FieldTheory/FunctionField/ConstantExtension/Genus/Change.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/ConstantExtension/Genus/Change.lean#L120)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicCurves/STATUS.md)

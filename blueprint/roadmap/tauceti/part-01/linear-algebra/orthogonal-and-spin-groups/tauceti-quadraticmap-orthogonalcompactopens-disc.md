---
declaration: theorem
origin: cited
lean: TauCeti.QuadraticMap.OrthogonalCompactOpens.discreteTopology_range_fullAdelicSpinDiagonal
statement: formalized
proof: formalized
---

# TauCeti.QuadraticMap.OrthogonalCompactOpens.discreteTopology_range_fullAdelicSpinDiagonal

Rational Spin points of a nondegenerate rational quadratic space form a discrete subgroup
of the full adelic Spin group for every compatible compact-open reference family.

```lean
TauCeti.QuadraticMap.OrthogonalCompactOpens.discreteTopology_range_fullAdelicSpinDiagonal.{u_1}
  {V : Type u_1} [AddCommGroup V] [_root_.Module ℚ V] [FiniteDimensional ℚ V]
  {Q : QuadraticForm ℚ V} (U : TauCeti.QuadraticMap.OrthogonalCompactOpens Q)
  (hQ : QuadraticMap.Nondegenerate) : DiscreteTopology ↥U.fullAdelicSpinDiagonal.range
```

## Depends on

- [TauCeti.QuadraticMap.OrthogonalCompactOpens.fullAdelicSpin](tauceti-quadraticmap-orthogonalcompactopens-full.md)

## Proof depends on

- [TauCeti.restrictedProductMap](../../topology/restricted-products-of-topological-groups-and-ra/tauceti-restrictedproductmap.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.QuadraticMap.OrthogonalCompactOpens.discreteTopology_range_fullAdelicSpinDiagonal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/OrthogonalGroup/Diagonal/Discrete.html#TauCeti.QuadraticMap.OrthogonalCompactOpens.discreteTopology_range_fullAdelicSpinDiagonal).

## Sources

- [Tau Ceti documentation: `TauCeti.QuadraticMap.OrthogonalCompactOpens.discreteTopology_range_fullAdelicSpinDiagonal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/OrthogonalGroup/Diagonal/Discrete.html#TauCeti.QuadraticMap.OrthogonalCompactOpens.discreteTopology_range_fullAdelicSpinDiagonal)
- [Source of `TauCeti.QuadraticMap.OrthogonalCompactOpens.discreteTopology_range_fullAdelicSpinDiagonal` in TauCeti/NumberTheory/QuadraticForm/OrthogonalGroup/Diagonal/Discrete.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/QuadraticForm/OrthogonalGroup/Diagonal/Discrete.lean#L227)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OrthogonalSpinGroups/STATUS.md)

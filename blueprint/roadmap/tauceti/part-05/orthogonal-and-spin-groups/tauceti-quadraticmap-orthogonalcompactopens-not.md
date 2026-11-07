---
declaration: theorem
origin: cited
lean: TauCeti.QuadraticMap.OrthogonalCompactOpens.not_discreteTopology_range_finiteAdelicSpecialOrthogonalDiagonal
statement: formalized
proof: formalized
---

# TauCeti.QuadraticMap.OrthogonalCompactOpens.not\_discreteTopology\_range\_finiteAdelicSpecialOrthogonalDiagonal

For a nondegenerate isotropic rational quadratic space of dimension at least three, the
rational diagonal is not discrete in finite adelic `SO`. In dimension two the transvection
parameter quotient is zero, so the dimension hypothesis is essential to this argument.

```lean
TauCeti.QuadraticMap.OrthogonalCompactOpens.not_discreteTopology_range_finiteAdelicSpecialOrthogonalDiagonal.{u_1}
  {V : Type u_1} [AddCommGroup V] [_root_.Module ℚ V] [FiniteDimensional ℚ V]
  {Q : QuadraticForm ℚ V} (U : TauCeti.QuadraticMap.OrthogonalCompactOpens Q)
  (hQ : QuadraticMap.Nondegenerate) (hdim : 3 ≤ Module.finrank ℚ V) (hiso : ∃ u, u ≠ 0 ∧ Q u = 0) :
  ¬DiscreteTopology ↥U.finiteAdelicSpecialOrthogonalDiagonal.range
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.QuadraticMap.OrthogonalCompactOpens.not_discreteTopology_range_finiteAdelicSpecialOrthogonalDiagonal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/OrthogonalGroup/Diagonal/NonDiscrete/Basic.html#TauCeti.QuadraticMap.OrthogonalCompactOpens.not_discreteTopology_range_finiteAdelicSpecialOrthogonalDiagonal).

## Sources

- [Tau Ceti documentation: `TauCeti.QuadraticMap.OrthogonalCompactOpens.not_discreteTopology_range_finiteAdelicSpecialOrthogonalDiagonal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/OrthogonalGroup/Diagonal/NonDiscrete/Basic.html#TauCeti.QuadraticMap.OrthogonalCompactOpens.not_discreteTopology_range_finiteAdelicSpecialOrthogonalDiagonal)
- [Source of `TauCeti.QuadraticMap.OrthogonalCompactOpens.not_discreteTopology_range_finiteAdelicSpecialOrthogonalDiagonal` in TauCeti/NumberTheory/QuadraticForm/OrthogonalGroup/Diagonal/NonDiscrete/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/QuadraticForm/OrthogonalGroup/Diagonal/NonDiscrete/Basic.lean#L128)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/OrthogonalSpinGroups/STATUS.md)

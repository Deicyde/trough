---
declaration: theorem
origin: cited
lean: TauCeti.QuadraticMap.OrthogonalCompactOpens.not_discreteTopology_range_finiteAdelicSpecialOrthogonalDiagonal
statement: formalized
proof: formalized
---

# TauCeti.QuadraticMap.OrthogonalCompactOpens.not_discreteTopology_range_finiteAdelicSpecialOrthogonalDiagonal

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
- [Source of `TauCeti.QuadraticMap.OrthogonalCompactOpens.not_discreteTopology_range_finiteAdelicSpecialOrthogonalDiagonal` in TauCeti/NumberTheory/QuadraticForm/OrthogonalGroup/Diagonal/NonDiscrete/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/QuadraticForm/OrthogonalGroup/Diagonal/NonDiscrete/Basic.lean#L127)
- [Tau Ceti roadmap status: Orthogonal and spin groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OrthogonalSpinGroups/STATUS.md)

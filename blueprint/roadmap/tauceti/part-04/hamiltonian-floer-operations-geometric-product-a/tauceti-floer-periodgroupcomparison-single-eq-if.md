---
declaration: theorem
origin: cited
lean: TauCeti.Floer.periodGroupComparison_single_eq_iff
statement: formalized
proof: formalized
---

# TauCeti.Floer.periodGroupComparison_single_eq_iff

Monomial descent identifies precisely the joint periods, retaining equal-area classes
of different Chern number. The coefficient is assumed nonzero.

```lean
TauCeti.Floer.periodGroupComparison_single_eq_iff.{u_1, u_2} {R : Type u_1} {S : Type u_2}
  [AddCommGroup S] (ω : S →+ ℝ) (c : S →+ ℤ) [Semiring R] {r : R} (hr : r ≠ 0) (A B : S) :
  (TauCeti.Floer.periodGroupComparison ω c) (TauCeti.NovikovSeries.single A r) =
      (TauCeti.Floer.periodGroupComparison ω c) (TauCeti.NovikovSeries.single B r) ↔
    ω A = ω B ∧ c A = c B
```

## Depends on

- [TauCeti.Floer.coefficientComparison](tauceti-floer-coefficientcomparison.md)
- [TauCeti.Floer.PeriodGroup](tauceti-floer-periodgroup.md)

## Proof depends on

- [TauCeti.NovikovSeries.mapRingHom](../../part-05/morse-novikov-homology-and-dynamical-reidemeiste/tauceti-novikovseries-mapringhom.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Floer.periodGroupComparison_single_eq_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/CoefficientComparison.html#TauCeti.Floer.periodGroupComparison_single_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Floer.periodGroupComparison_single_eq_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/CoefficientComparison.html#TauCeti.Floer.periodGroupComparison_single_eq_iff)
- [Source of `TauCeti.Floer.periodGroupComparison_single_eq_iff` in TauCeti/Geometry/Symplectic/Floer/CoefficientComparison.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Floer/CoefficientComparison.lean#L174)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)

---
declaration: abbrev
origin: cited
lean: TauCeti.Floer.NovikovRing
statement: formalized
---

# TauCeti.Floer.NovikovRing

The Floer Novikov ring over `R`: Novikov series `∑ a_γ e^γ` over the period group, with
valuation `ν(γ) = -ω(γ)`, so that for every bound `C` only finitely many classes with nonzero
coefficient have area greater than `-C`. It is graded by `PeriodGroup.degree`.

```lean
TauCeti.Floer.NovikovRing.{u_1, u_2} {S : Type u_1} [AddGroup S] (R : Type u_2) (ω : S →+ ℝ)
  (c : S →+ ℤ) [Zero R] : Type (max u_1 u_2)
```

## Depends on

- [TauCeti.Floer.PeriodGroup](tauceti-floer-periodgroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Floer.NovikovRing`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/NovikovRing.html#TauCeti.Floer.NovikovRing).

## Sources

- [Tau Ceti documentation: `TauCeti.Floer.NovikovRing`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/NovikovRing.html#TauCeti.Floer.NovikovRing)
- [Source of `TauCeti.Floer.NovikovRing` in TauCeti/Geometry/Symplectic/Floer/NovikovRing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Floer/NovikovRing.lean#L88)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)

---
declaration: def
origin: cited
lean: TauCeti.Floer.coefficientComparison
statement: formalized
---

# TauCeti.Floer.coefficientComparison

The completed coefficient comparison `q^A ↦ e^(-q A)`, with source period `ω` and
target period `-Ω`. Area preservation makes it a unital ring homomorphism.

```lean
TauCeti.Floer.coefficientComparison.{u_1, u_2, u_3} {R : Type u_1} {S : Type u_2} {Γ : Type u_3}
  [AddMonoid S] [AddCommGroup Γ] {ω : S →+ ℝ} {Ω : Γ →+ ℝ} [Semiring R] (q : S →+ Γ)
  (hω : ∀ (A : S), Ω (q A) = ω A) : TauCeti.NovikovSeries R S ω →+* TauCeti.NovikovSeries R Γ (-Ω)
```

## Depends on

- [TauCeti.NovikovSeries.mapRingHom](../../../ring-theory/part-01/morse-novikov-homology-and-dynamical-reidemeiste/tauceti-novikovseries-mapringhom.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Floer.coefficientComparison`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/CoefficientComparison.html#TauCeti.Floer.coefficientComparison).

## Sources

- [Tau Ceti documentation: `TauCeti.Floer.coefficientComparison`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/CoefficientComparison.html#TauCeti.Floer.coefficientComparison)
- [Source of `TauCeti.Floer.coefficientComparison` in TauCeti/Geometry/Symplectic/Floer/CoefficientComparison.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Floer/CoefficientComparison.lean#L57)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)

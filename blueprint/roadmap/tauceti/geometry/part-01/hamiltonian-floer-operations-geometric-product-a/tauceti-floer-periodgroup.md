---
declaration: abbrev
origin: cited
lean: TauCeti.Floer.PeriodGroup
statement: formalized
---

# TauCeti.Floer.PeriodGroup

The period group `Γ = S ⧸ (ker ω ⊓ ker c)` of a group of spherical classes `S` with symplectic
area `ω` and first Chern number `c`, written as the quotient by the kernel of `s ↦ (ω s, c s)`.

It is an abbreviation so that the quotient group API of Mathlib applies to it directly.

```lean
TauCeti.Floer.PeriodGroup.{u_1} {S : Type u_1} [AddGroup S] (ω : S →+ ℝ) (c : S →+ ℤ) : Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Floer.PeriodGroup`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/PeriodGroup.html#TauCeti.Floer.PeriodGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.Floer.PeriodGroup`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/PeriodGroup.html#TauCeti.Floer.PeriodGroup)
- [Source of `TauCeti.Floer.PeriodGroup` in TauCeti/Geometry/Symplectic/Floer/PeriodGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Floer/PeriodGroup.lean#L77)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)

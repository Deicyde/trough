---
declaration: structure
origin: cited
lean: TauCeti.IntegralLattice
statement: formalized
---

# TauCeti.IntegralLattice

An integral symmetric lattice in a rational vector space.

The field `le_dual` says exactly that the form takes integer values on pairs of vectors in
`carrier`.

```lean
TauCeti.IntegralLattice.{u} (V : Type u) [AddCommGroup V] [_root_.Module ℚ V] : Type u
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Basic.html#TauCeti.IntegralLattice).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Basic.html#TauCeti.IntegralLattice)
- [Source of `TauCeti.IntegralLattice` in TauCeti/LinearAlgebra/IntegralLattice/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/Basic.lean#L59)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/IntegralLattices/STATUS.md)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/IntegralLattices/STATUS.md)

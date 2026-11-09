---
declaration: def
origin: cited
lean: TauCeti.SymplecticForm.IsSymplectic
statement: formalized
---

# TauCeti.SymplecticForm.IsSymplectic

A submodule is **symplectic** if it meets its symplectic complement only in zero,
equivalently (`isSymplectic_iff_nondegenerate_restrict`) `ω` restricts to it nondegenerately.

```lean
TauCeti.SymplecticForm.IsSymplectic.{u_1} {V : Type u_1} [AddCommGroup V] [_root_.Module ℝ V]
  (ω : TauCeti.SymplecticForm V) (L : Submodule ℝ V) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.IsSymplectic`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Lagrangian/Basic.html#TauCeti.SymplecticForm.IsSymplectic).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.IsSymplectic`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Lagrangian/Basic.html#TauCeti.SymplecticForm.IsSymplectic)
- [Source of `TauCeti.SymplecticForm.IsSymplectic` in TauCeti/Geometry/Symplectic/Lagrangian/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Lagrangian/Basic.lean#L229)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SymplecticGeometry/STATUS.md)

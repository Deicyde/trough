---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.isLagrangian_iff_maximal_isIsotropic
statement: formalized
proof: formalized
---

# TauCeti.SymplecticForm.isLagrangian_iff_maximal_isIsotropic

Lagrangian subspaces are exactly the maximal isotropic subspaces, in any dimension.

```lean
TauCeti.SymplecticForm.isLagrangian_iff_maximal_isIsotropic.{u_1} {V : Type u_1} [AddCommGroup V]
  [_root_.Module ℝ V] {ω : TauCeti.SymplecticForm V} {L : Submodule ℝ V} :
  ω.IsLagrangian L ↔ Maximal ω.IsIsotropic L
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.isLagrangian_iff_maximal_isIsotropic`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Lagrangian/Basic.html#TauCeti.SymplecticForm.isLagrangian_iff_maximal_isIsotropic).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.isLagrangian_iff_maximal_isIsotropic`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Lagrangian/Basic.html#TauCeti.SymplecticForm.isLagrangian_iff_maximal_isIsotropic)
- [Source of `TauCeti.SymplecticForm.isLagrangian_iff_maximal_isIsotropic` in TauCeti/Geometry/Symplectic/Lagrangian/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Lagrangian/Basic.lean#L224)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SymplecticGeometry/STATUS.md)

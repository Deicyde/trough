---
declaration: theorem
origin: cited
lean: TauCeti.CurvedDGRightModuleCat.homotopyIsTriangulated
statement: formalized
proof: formalized
---

# TauCeti.CurvedDGRightModuleCat.homotopyIsTriangulated

**The homotopy category of curved right modules is triangulated**, with the shift by one given
by the cohomological shift.

```lean
TauCeti.CurvedDGRightModuleCat.homotopyIsTriangulated.{u} {R A : Type u} [CommRing R] [Ring A]
  [Algebra R A] {𝒜 : ℤ → Submodule R A} [GradedAlgebra 𝒜] {d : A →ₗ[R] A} {w : A}
  {h : TauCeti.IsCurvedDGAlgebra 𝒜 d w} :
  CategoryTheory.IsTriangulated (TauCeti.DGHomotopyCategory R (TauCeti.CurvedDGRightModuleCat h))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Happel's theorem](happels-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CurvedDGRightModuleCat.homotopyIsTriangulated`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Curved/Module/Right/Triangulated.html#TauCeti.CurvedDGRightModuleCat.homotopyIsTriangulated).

## Sources

- [Tau Ceti documentation: `TauCeti.CurvedDGRightModuleCat.homotopyIsTriangulated`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Curved/Module/Right/Triangulated.html#TauCeti.CurvedDGRightModuleCat.homotopyIsTriangulated)
- [Source of `TauCeti.CurvedDGRightModuleCat.homotopyIsTriangulated` in TauCeti/Algebra/Homology/Curved/Module/Right/Triangulated.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/Curved/Module/Right/Triangulated.lean#L91)
- [Tau Ceti roadmap status: Stable, periodic, and curved homological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StablePeriodicCurved/STATUS.md)

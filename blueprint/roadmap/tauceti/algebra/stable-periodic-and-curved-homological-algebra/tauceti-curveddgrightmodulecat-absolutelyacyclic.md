---
declaration: def
origin: cited
lean: TauCeti.CurvedDGRightModuleCat.absolutelyAcyclic
statement: formalized
---

# TauCeti.CurvedDGRightModuleCat.absolutelyAcyclic

The **absolutely acyclic** curved right modules: the smallest thick triangulated subcategory
of the curved homotopy category containing all totalizations of short exact sequences.

```lean
TauCeti.CurvedDGRightModuleCat.absolutelyAcyclic.{u} (R : Type u) {A : Type u} [CommRing R] [Ring A]
  [Algebra R A] {𝒜 : ℤ → Submodule R A} [GradedAlgebra 𝒜] {d : A →ₗ[R] A} {w : A}
  (h : TauCeti.IsCurvedDGAlgebra 𝒜 d w) :
  CategoryTheory.ObjectProperty (TauCeti.DGHomotopyCategory R (TauCeti.CurvedDGRightModuleCat h))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Happel's theorem](happels-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CurvedDGRightModuleCat.absolutelyAcyclic`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Curved/Module/Right/Acyclic.html#TauCeti.CurvedDGRightModuleCat.absolutelyAcyclic).

## Sources

- [Tau Ceti documentation: `TauCeti.CurvedDGRightModuleCat.absolutelyAcyclic`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Curved/Module/Right/Acyclic.html#TauCeti.CurvedDGRightModuleCat.absolutelyAcyclic)
- [Source of `TauCeti.CurvedDGRightModuleCat.absolutelyAcyclic` in TauCeti/Algebra/Homology/Curved/Module/Right/Acyclic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/Curved/Module/Right/Acyclic.lean#L187)
- [Tau Ceti roadmap status: Stable, periodic, and curved homological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StablePeriodicCurved/STATUS.md)

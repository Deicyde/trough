---
declaration: abbrev
origin: cited
lean: TauCeti.fibrationLocalSystem
statement: formalized
---

# TauCeti.fibrationLocalSystem

The **DG local system of a map** `p : E → B` at `b`: the normalized cubical chains of the fibre
`F'` of the Moore-path replacement, a right DG module over `C_*(Ω_b B; R)` through the strict
action of the Moore loops.

```lean
TauCeti.fibrationLocalSystem.{u, u_1} {E B : Type u} [TopologicalSpace E] [TopologicalSpace B]
  (R : Type u_1) [CommRing R] (p : C(E, B)) (b : B) : TauCeti.DGLocalSystem B b R
```

## Depends on

- [TauCeti.loopChainAlgebra](tauceti-loopchainalgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.fibrationLocalSystem`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/DGLocalSystem/Fibration.html#TauCeti.fibrationLocalSystem).

## Sources

- [Tau Ceti documentation: `TauCeti.fibrationLocalSystem`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/DGLocalSystem/Fibration.html#TauCeti.fibrationLocalSystem)
- [Source of `TauCeti.fibrationLocalSystem` in TauCeti/AlgebraicTopology/DGLocalSystem/Fibration.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/DGLocalSystem/Fibration.lean#L63)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGFloer/STATUS.md)

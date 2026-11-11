---
declaration: def
origin: cited
lean: TauCeti.FiberInclusionPathFiber.loopHomotopyEquiv
statement: formalized
---

# The homotopy fibre of the fibre inclusion is the loop space of the base

For a Hurewicz
fibration `p`, the space of paths in `E` from the fibre through `e₀` to `e₀` is homotopy
equivalent to the loop space `Ω B (p e₀)`, by composing the paths with `p`.

```lean
TauCeti.FiberInclusionPathFiber.loopHomotopyEquiv.{u, v} {E : Type u} {B : Type v}
  [TopologicalSpace E] [TopologicalSpace B] {p : C(E, B)} (e₀ : E)
  (hp : TauCeti.IsHurewiczFibration ⇑p) :
  ContinuousMap.HomotopyEquiv (TauCeti.FiberInclusionPathFiber p e₀) (LoopSpace B (p e₀))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FiberInclusionPathFiber.loopHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/HurewiczFibration/FiberInclusion.html#TauCeti.FiberInclusionPathFiber.loopHomotopyEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.FiberInclusionPathFiber.loopHomotopyEquiv`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/HurewiczFibration/FiberInclusion.html#TauCeti.FiberInclusionPathFiber.loopHomotopyEquiv)
- [Source of `TauCeti.FiberInclusionPathFiber.loopHomotopyEquiv` in TauCeti/Topology/Homotopy/HurewiczFibration/FiberInclusion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Homotopy/HurewiczFibration/FiberInclusion.lean#L260)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)

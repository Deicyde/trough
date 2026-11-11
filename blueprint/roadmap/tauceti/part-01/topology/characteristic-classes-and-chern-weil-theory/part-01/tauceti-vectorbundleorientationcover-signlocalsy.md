---
declaration: def
origin: cited
lean: TauCeti.VectorBundleOrientationCover.signLocalSystem
statement: formalized
---

# TauCeti.VectorBundleOrientationCover.signLocalSystem

The orientation local system `o(E)` of a real vector bundle of rank `card ι`: the sign local
system of its orientation double cover with respect to the deck involution. Its fibre over `b` is
the module `TauCeti.signFiber` of functions on the orientations of `E_b` that change sign under
reversal (`TauCeti.VectorBundleOrientationCover.signLocalSystemObjEquiv`), and transport along a
path precomposes with path lifting in the cover.

```lean
TauCeti.VectorBundleOrientationCover.signLocalSystem.{u, uB, uE, uι, u_1} {B : Type uB}
  [TopologicalSpace B] (F : Type u_1) [NormedAddCommGroup F] [NormedSpace ℝ F] (E : B → Type uE)
  [TopologicalSpace (Bundle.TotalSpace F E)] [(b : B) → AddCommMonoid (E b)]
  [(b : B) → _root_.Module ℝ (E b)] [(b : B) → TopologicalSpace (E b)] [FiberBundle F E]
  [VectorBundle ℝ F E] {ι : Type uι} [Fintype ι] (R : Type u) [Ring R]
  (hι : Fintype.card ι = Module.finrank ℝ F) : TauCeti.LocalCoefficientSystem R ↧B
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.VectorBundleOrientationCover.signLocalSystem`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/LocalSystem.html#TauCeti.VectorBundleOrientationCover.signLocalSystem).

## Sources

- [Tau Ceti documentation: `TauCeti.VectorBundleOrientationCover.signLocalSystem`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/LocalSystem.html#TauCeti.VectorBundleOrientationCover.signLocalSystem)
- [Source of `TauCeti.VectorBundleOrientationCover.signLocalSystem` in TauCeti/Topology/VectorBundle/Orientation/LocalSystem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/VectorBundle/Orientation/LocalSystem.lean#L72)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CharacteristicClasses/STATUS.md)

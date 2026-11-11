---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.Chow.cyclesMap
statement: formalized
---

# TauCeti.AlgebraicGeometry.Chow.cyclesMap

The pushforward of `n`-cycles along a quasi-compact morphism over a field: Mathlib's
pushforward of cycles with height weights, `[V] ↦ [κ(V) : κ(f(V))] [f(V)]`.

```lean
TauCeti.AlgebraicGeometry.Chow.cyclesMap.{u} (k : Type u) [Field k] {X Y : AlgebraicGeometry.Scheme}
  [X.Over (AlgebraicGeometry.Spec ↧k)] [Y.Over (AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.LocallyOfFiniteType (X ↘ AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.LocallyOfFiniteType (Y ↘ AlgebraicGeometry.Spec ↧k)] (f : X ⟶ Y)
  [AlgebraicGeometry.Scheme.Hom.IsOver f (AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.QuasiCompact f] {n : ℤ} :
  ↥(TauCeti.AlgebraicGeometry.Chow.cyclesOfDimension X n) →+
    ↥(TauCeti.AlgebraicGeometry.Chow.cyclesOfDimension Y n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.Chow.cyclesMap`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Chow/Pushforward.html#TauCeti.AlgebraicGeometry.Chow.cyclesMap).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.Chow.cyclesMap`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Chow/Pushforward.html#TauCeti.AlgebraicGeometry.Chow.cyclesMap)
- [Source of `TauCeti.AlgebraicGeometry.Chow.cyclesMap` in TauCeti/AlgebraicGeometry/Chow/Pushforward.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Chow/Pushforward.lean#L63)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)

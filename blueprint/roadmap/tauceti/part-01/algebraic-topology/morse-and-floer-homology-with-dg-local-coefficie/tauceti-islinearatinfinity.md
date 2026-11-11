---
declaration: def
origin: cited
lean: TauCeti.IsLinearAtInfinity
statement: formalized
---

# TauCeti.IsLinearAtInfinity

A function `F` on a completion of the Liouville domain `W` with Liouville field `Z` is
**linear at infinity** with slope `a` when `F = a r + b` outside a compact set, for a constant `b`,
where `r` is the radial coordinate `TauCeti.liouvilleRadialCoordinate Z W`.

```lean
TauCeti.IsLinearAtInfinity.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] (Z : (x : M) → TangentSpace I x) (W : Set M) (F : M → ℝ)
  (a : ℝ) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsLinearAtInfinity`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Liouville/LinearAtInfinity.html#TauCeti.IsLinearAtInfinity).

## Sources

- [Tau Ceti documentation: `TauCeti.IsLinearAtInfinity`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Liouville/LinearAtInfinity.html#TauCeti.IsLinearAtInfinity)
- [Source of `TauCeti.IsLinearAtInfinity` in TauCeti/Geometry/Symplectic/Liouville/LinearAtInfinity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Liouville/LinearAtInfinity.lean#L119)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGFloer/STATUS.md)

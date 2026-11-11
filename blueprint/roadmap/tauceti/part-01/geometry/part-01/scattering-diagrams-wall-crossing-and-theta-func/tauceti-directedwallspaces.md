---
declaration: structure
origin: cited
lean: TauCeti.DirectedWallSpaces
statement: formalized
---

# TauCeti.DirectedWallSpaces

Homogeneous submodules with the normal and bracket laws of directed walls.
For a positive grading, containment in the homogeneous pieces automatically makes
all spaces outside the nonzero positive degrees vanish.

```lean
TauCeti.DirectedWallSpaces.{u_1, u_2, u_3, u_4} {Γ : Type u_1} {Λ : Type u_2} {R : Type u_3}
  {L : Type u_4} [AddCommMonoid Γ] [AddCommMonoid Λ] [CommRing R] [LieRing L] [LieAlgebra R L]
  (ρ : Γ →+ Λ) (ℒ : Γ → Submodule R L) : Type (max (max u_1 u_2) u_4)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DirectedWallSpaces`](https://taucetiproject.org/docs/TauCeti/Geometry/ScatteringDiagram/WallSpace/Basic.html#TauCeti.DirectedWallSpaces).

## Sources

- [Tau Ceti documentation: `TauCeti.DirectedWallSpaces`](https://taucetiproject.org/docs/TauCeti/Geometry/ScatteringDiagram/WallSpace/Basic.html#TauCeti.DirectedWallSpaces)
- [Source of `TauCeti.DirectedWallSpaces` in TauCeti/Geometry/ScatteringDiagram/WallSpace/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/ScatteringDiagram/WallSpace/Basic.lean#L75)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)

---
declaration: theorem
origin: cited
lean: TauCeti.DGTwistedObject.isTriangulated
statement: formalized
proof: formalized
---

# The homotopy category of twisted objects is triangulated

Every composable pair of
morphisms of the homotopy category is represented by closed morphisms `u : P ⟶ Q` and
`v : Q ⟶ S`, and the cone triangles of `u`, `v` and `u ≫ v` fit into the octahedron whose third
triangle is `TauCeti.DGTwistedObject.coneCompTriangle`.

```lean
TauCeti.DGTwistedObject.isTriangulated.{v, u} {R : Type v} [CommRing R] {C : Type u}
  [TauCeti.DGCategory R C] :
  CategoryTheory.IsTriangulated
    (TauCeti.DGHomotopyCategory R
      (TauCeti.DGTwistedObject R (TauCeti.DGAdditiveClosure (TauCeti.DGShiftClosure C))))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DGTwistedObject.isTriangulated`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/DG/Twisted/Triangulated.html#TauCeti.DGTwistedObject.isTriangulated).

## Sources

- [Tau Ceti documentation: `TauCeti.DGTwistedObject.isTriangulated`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/DG/Twisted/Triangulated.html#TauCeti.DGTwistedObject.isTriangulated)
- [Source of `TauCeti.DGTwistedObject.isTriangulated` in TauCeti/CategoryTheory/DG/Twisted/Triangulated.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/DG/Twisted/Triangulated.lean#L633)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGAInfinity/STATUS.md)

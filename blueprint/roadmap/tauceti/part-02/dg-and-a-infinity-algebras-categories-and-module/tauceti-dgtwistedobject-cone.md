---
declaration: abbrev
origin: cited
lean: TauCeti.DGTwistedObject.cone
statement: formalized
---

# TauCeti.DGTwistedObject.cone

The **cone** of a closed degree-zero morphism `u : P ⟶ Q` of twisted objects: the twisted
object `(Q ⊕ P⟦1⟧, δ)` whose twisting matrix has the twists of `Q` and `P⟦1⟧` on the diagonal
and the morphism `P⟦1⟧ ⟶ P ⟶ Q` underlying `u` in the block from `P⟦1⟧` to `Q`.

```lean
TauCeti.DGTwistedObject.cone.{v, u} {R : Type v} [CommRing R] {C : Type u} [TauCeti.DGCategory R C]
  {P Q : TauCeti.DGTwistedObject R (TauCeti.DGAdditiveClosure (TauCeti.DGShiftClosure C))}
  (u : TauCeti.DGHom R 0 P Q) (hu : (TauCeti.dgDifferential R 0) u = 0) :
  TauCeti.DGTwistedObject R (TauCeti.DGAdditiveClosure (TauCeti.DGShiftClosure C))
```

## Depends on

- [TauCeti.DGTwistedObject](tauceti-dgtwistedobject.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DGTwistedObject.cone`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/DG/Twisted/Cone.html#TauCeti.DGTwistedObject.cone).

## Sources

- [Tau Ceti documentation: `TauCeti.DGTwistedObject.cone`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/DG/Twisted/Cone.html#TauCeti.DGTwistedObject.cone)
- [Source of `TauCeti.DGTwistedObject.cone` in TauCeti/CategoryTheory/DG/Twisted/Cone.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/DG/Twisted/Cone.lean#L159)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGAInfinity/STATUS.md)

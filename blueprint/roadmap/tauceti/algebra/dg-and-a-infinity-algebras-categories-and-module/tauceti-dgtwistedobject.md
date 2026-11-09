---
declaration: structure
origin: cited
lean: TauCeti.DGTwistedObject
statement: formalized
---

# TauCeti.DGTwistedObject

A **twisted object** of a differential graded category: an object `obj` with a degree-one
endomorphism `twist` satisfying the Maurer–Cartan equation `d δ = dgComp δ δ`, which in Keller's
order is `d δ + δ ∘ δ = 0`.  The twisted objects form a differential graded category whose Hom
complexes carry the twisted differential; see `TauCeti.DGTwistedObject.homComplexData`.

```lean
TauCeti.DGTwistedObject.{v, u} (R : Type v) [CommRing R] (C : Type u) [TauCeti.DGCategory R C] :
  Type (max u v)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DGTwistedObject`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/DG/Twisted/Basic.html#TauCeti.DGTwistedObject).

## Sources

- [Tau Ceti documentation: `TauCeti.DGTwistedObject`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/DG/Twisted/Basic.html#TauCeti.DGTwistedObject)
- [Source of `TauCeti.DGTwistedObject` in TauCeti/CategoryTheory/DG/Twisted/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/DG/Twisted/Basic.lean#L84)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DGAInfinity/STATUS.md)

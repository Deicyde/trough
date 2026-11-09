---
declaration: theorem
origin: cited
lean: TauCeti.Khovanov.isFrobenius
statement: formalized
proof: formalized
---

# TauCeti.Khovanov.isFrobenius

The dual numbers with the Khovanov comultiplication satisfy the Frobenius equation.

```lean
TauCeti.Khovanov.isFrobenius.{u_1} (R : Type u_1) [CommSemiring R] :
  Coalgebra.IsFrobenius R (DualNumber R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Khovanov.isFrobenius`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Frobenius.html#TauCeti.Khovanov.isFrobenius).

## Sources

- [Tau Ceti documentation: `TauCeti.Khovanov.isFrobenius`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Frobenius.html#TauCeti.Khovanov.isFrobenius)
- [Source of `TauCeti.Khovanov.isFrobenius` in TauCeti/KnotTheory/Khovanov/Frobenius.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Khovanov/Frobenius.lean#L111)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/KhovanovHomology/STATUS.md)

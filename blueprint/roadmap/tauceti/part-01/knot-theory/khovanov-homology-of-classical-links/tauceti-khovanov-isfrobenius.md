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
- [Source of `TauCeti.Khovanov.isFrobenius` in TauCeti/KnotTheory/Khovanov/Frobenius.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/KnotTheory/Khovanov/Frobenius.lean#L111)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/KhovanovHomology/STATUS.md)

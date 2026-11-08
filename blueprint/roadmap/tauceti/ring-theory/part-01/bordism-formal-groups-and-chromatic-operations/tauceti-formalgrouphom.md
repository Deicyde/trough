---
declaration: structure
origin: cited
lean: TauCeti.FormalGroupHom
statement: formalized
---

# TauCeti.FormalGroupHom

A homomorphism of formal group laws is a series `f` with zero constant term such that
`f(F(X,Y)) = G(f(X),f(Y))`.

```lean
TauCeti.FormalGroupHom.{u_1} {R : Type u_1} [CommRing R] (F G : FormalGroup R) : Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FormalGroupHom`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Hom/Basic.html#TauCeti.FormalGroupHom).

## Sources

- [Tau Ceti documentation: `TauCeti.FormalGroupHom`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Hom/Basic.html#TauCeti.FormalGroupHom)
- [Source of `TauCeti.FormalGroupHom` in TauCeti/RingTheory/FormalGroup/Hom/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/FormalGroup/Hom/Basic.lean#L277)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BordismFormalGroups/STATUS.md)

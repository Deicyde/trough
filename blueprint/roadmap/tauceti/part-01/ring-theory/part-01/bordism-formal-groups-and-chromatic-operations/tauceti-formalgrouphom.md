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
- [Source of `TauCeti.FormalGroupHom` in TauCeti/RingTheory/FormalGroup/Hom/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/FormalGroup/Hom/Basic.lean#L274)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BordismFormalGroups/STATUS.md)

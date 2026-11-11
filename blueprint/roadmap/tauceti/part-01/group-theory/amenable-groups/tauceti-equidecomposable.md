---
declaration: def
origin: cited
lean: TauCeti.Equidecomposable
statement: formalized
---

# TauCeti.Equidecomposable

Two sets `A B : Set X` are *equidecomposable* using `G` when some equidecomposition has source
`A` and target `B`: `A` can be cut into finitely many pieces which, each moved by a single element
of `G`, reassemble into `B`.

```lean
TauCeti.Equidecomposable.{u_1, u_3} {X : Type u_1} (G : Type u_3) [SMul G X] (A B : Set X) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Equidecomposable`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Action/Equidecomp.html#TauCeti.Equidecomposable).

## Sources

- [Tau Ceti documentation: `TauCeti.Equidecomposable`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Action/Equidecomp.html#TauCeti.Equidecomposable)
- [Source of `TauCeti.Equidecomposable` in TauCeti/Algebra/Group/Action/Equidecomp.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Group/Action/Equidecomp.lean#L125)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AmenableGroups/STATUS.md)

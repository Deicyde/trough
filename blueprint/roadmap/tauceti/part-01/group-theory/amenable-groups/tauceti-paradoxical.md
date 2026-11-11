---
declaration: def
origin: cited
lean: TauCeti.Paradoxical
statement: formalized
---

# TauCeti.Paradoxical

A set `S : Set X` is *paradoxical* for the action of `G` when it is nonempty and is the union
of two disjoint sets `A` and `B`, each equidecomposable with `S` using `G`.

```lean
TauCeti.Paradoxical.{u_1, u_3} {X : Type u_1} (G : Type u_3) [SMul G X] (S : Set X) : Prop
```

## Depends on

- [TauCeti.Equidecomposable](tauceti-equidecomposable.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Paradoxical`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Action/Paradoxical.html#TauCeti.Paradoxical).

## Sources

- [Tau Ceti documentation: `TauCeti.Paradoxical`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Action/Paradoxical.html#TauCeti.Paradoxical)
- [Source of `TauCeti.Paradoxical` in TauCeti/Algebra/Group/Action/Paradoxical.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Group/Action/Paradoxical.lean#L62)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AmenableGroups/STATUS.md)

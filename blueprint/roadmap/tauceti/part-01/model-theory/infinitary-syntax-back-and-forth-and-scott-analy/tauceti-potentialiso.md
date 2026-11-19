---
declaration: def
origin: cited
lean: TauCeti.PotentialIso
statement: formalized
---

# TauCeti.PotentialIso

Two structures are potentially isomorphic if a nonempty set of finitely generated partial
equivalences admits extensions containing every element on either side.

```lean
TauCeti.PotentialIso.{u, v, w, w'} {L : FirstOrder.Language} (M : Type w) (N : Type w')
  [L.Structure M] [L.Structure N] : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PotentialIso`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/PotentialIso.html#TauCeti.PotentialIso).

## Sources

- [Tau Ceti documentation: `TauCeti.PotentialIso`](https://taucetiproject.org/docs/TauCeti/ModelTheory/BackAndForth/PotentialIso.html#TauCeti.PotentialIso)
- [Source of `TauCeti.PotentialIso` in TauCeti/ModelTheory/BackAndForth/PotentialIso.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/BackAndForth/PotentialIso.lean#L42)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/InfinitaryLogic/STATUS.md)

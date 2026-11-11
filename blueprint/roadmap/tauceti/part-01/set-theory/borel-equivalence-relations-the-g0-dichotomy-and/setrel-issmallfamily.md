---
declaration: def
origin: cited
lean: SetRel.IsSmallFamily
statement: formalized
---

# SetRel.IsSmallFamily

A family `Φ` of assignments `ι → X` is **small** for a relation `G` if countably many
measurable `G`-independent sets capture a value of every member of `Φ`.

```lean
SetRel.IsSmallFamily.{u_1, u_2} {X : Type u_1} {ι : Type u_2} [MeasurableSpace X] (G : SetRel X X)
  (Φ : Set (ι → X)) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SetRel.IsSmallFamily`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/SmallFamily/Basic.html#SetRel.IsSmallFamily).

## Sources

- [Tau Ceti documentation: `SetRel.IsSmallFamily`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/SmallFamily/Basic.html#SetRel.IsSmallFamily)
- [Source of `SetRel.IsSmallFamily` in TauCeti/SetTheory/Descriptive/SmallFamily/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/SetTheory/Descriptive/SmallFamily/Basic.lean#L88)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)

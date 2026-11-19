---
declaration: def
origin: cited
lean: TauCeti.strictInwardCone
statement: formalized
---

# TauCeti.strictInwardCone

The strict inward cone consists of directions along which balls of linearly increasing
radius remain in the set for all sufficiently small positive times.

```lean
TauCeti.strictInwardCone.{u_1} {E : Type u_1} [SeminormedAddCommGroup E] [NormedSpace ℝ E]
  (s : Set E) (x : E) : Set E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.strictInwardCone`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Cone/StrictInward.html#TauCeti.strictInwardCone).

## Sources

- [Tau Ceti documentation: `TauCeti.strictInwardCone`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Cone/StrictInward.html#TauCeti.strictInwardCone)
- [Source of `TauCeti.strictInwardCone` in TauCeti/Analysis/Convex/Cone/StrictInward.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Convex/Cone/StrictInward.lean#L47)
- [Tau Ceti roadmap status: Differential geometry, Part II — relative de Rham theory, fundamental classes and relative transversality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DeRhamCohomologyAndDuality/STATUS.md)

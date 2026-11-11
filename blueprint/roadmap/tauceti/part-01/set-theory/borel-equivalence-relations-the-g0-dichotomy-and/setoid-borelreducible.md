---
declaration: def
origin: cited
lean: Setoid.BorelReducible
statement: formalized
---

# Setoid.BorelReducible

`E` is **Borel reducible** to `F`: some measurable map `f : X → Y` satisfies
`E x y ↔ F (f x) (f y)` for all `x` and `y`.

```lean
Setoid.BorelReducible.{u, v} {X : Type u} {Y : Type v} [MeasurableSpace X] [MeasurableSpace Y]
  (E : Setoid X) (F : Setoid Y) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Setoid.BorelReducible`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/BorelReducibility.html#Setoid.BorelReducible).

## Sources

- [Tau Ceti documentation: `Setoid.BorelReducible`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/BorelReducibility.html#Setoid.BorelReducible)
- [Source of `Setoid.BorelReducible` in TauCeti/SetTheory/Descriptive/BorelReducibility.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/SetTheory/Descriptive/BorelReducibility.lean#L98)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)

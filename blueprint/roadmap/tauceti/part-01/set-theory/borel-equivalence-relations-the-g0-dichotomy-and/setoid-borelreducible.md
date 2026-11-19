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
- [Source of `Setoid.BorelReducible` in TauCeti/SetTheory/Descriptive/BorelReducibility.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/SetTheory/Descriptive/BorelReducibility.lean#L98)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)

---
declaration: theorem
origin: cited
lean: Setoid.isSmooth_iff_countablySeparated
statement: formalized
proof: formalized
---

# Smoothness is countable separation

`E` is smooth iff the quotient `Quotient E`, with
Mathlib's quotient σ-algebra, is countably separated: countably many `E`-invariant measurable sets
separate the classes of `E`.

```lean
Setoid.isSmooth_iff_countablySeparated.{u} {X : Type u} [MeasurableSpace X] {E : Setoid X} :
  E.IsSmooth ↔ MeasurableSpace.CountablySeparated (Quotient E)
```

## Depends on

- [Setoid.BorelReducible](setoid-borelreducible.md)

## Lean

Formalized in Tau Ceti as [`Setoid.isSmooth_iff_countablySeparated`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/BorelReducibility.html#Setoid.isSmooth_iff_countablySeparated).

## Sources

- [Tau Ceti documentation: `Setoid.isSmooth_iff_countablySeparated`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/BorelReducibility.html#Setoid.isSmooth_iff_countablySeparated)
- [Source of `Setoid.isSmooth_iff_countablySeparated` in TauCeti/SetTheory/Descriptive/BorelReducibility.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/SetTheory/Descriptive/BorelReducibility.lean#L250)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)

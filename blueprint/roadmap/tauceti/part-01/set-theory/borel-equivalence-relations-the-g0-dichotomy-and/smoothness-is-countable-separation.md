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
- [Source of `Setoid.isSmooth_iff_countablySeparated` in TauCeti/SetTheory/Descriptive/BorelReducibility.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/SetTheory/Descriptive/BorelReducibility.lean#L250)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)

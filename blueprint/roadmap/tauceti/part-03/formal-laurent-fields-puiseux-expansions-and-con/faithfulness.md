---
declaration: theorem
origin: cited
lean: TauCeti.puiseuxField.kummer_injective
statement: formalized
proof: formalized
---

# Faithfulness

Distinct points of the Tate module act by distinct automorphisms of the
Puiseux field: the automorphism attached to `ζ` sends `t ^ (1 / n)` to `ζₙ t ^ (1 / n)`.

```lean
TauCeti.puiseuxField.kummer_injective.{u_1} {K : Type u_1} [Field K] :
  Function.Injective ⇑(TauCeti.puiseuxField.kummer K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.puiseuxField.kummer_injective`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/Kummer.html#TauCeti.puiseuxField.kummer_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.puiseuxField.kummer_injective`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/Kummer.html#TauCeti.puiseuxField.kummer_injective)
- [Source of `TauCeti.puiseuxField.kummer_injective` in TauCeti/RingTheory/LaurentSeries/Puiseux/Kummer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/LaurentSeries/Puiseux/Kummer.lean#L161)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)

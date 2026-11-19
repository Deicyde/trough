---
declaration: theorem
origin: cited
lean: TauCeti.not_isSmooth_of_borelReducible_eZero
statement: formalized
proof: formalized
---

# The easy half of the Glimm–Effros dichotomy

An equivalence relation to which `E₀` is
Borel reducible is not smooth.

```lean
TauCeti.not_isSmooth_of_borelReducible_eZero.{u_1} {X : Type u_1} [MeasurableSpace X] {E : Setoid X}
  (h : TauCeti.eZero.BorelReducible E) : ¬E.IsSmooth
```

## Depends on

- [Setoid.BorelReducible](setoid-borelreducible.md)

## Proof depends on

- [`E₀` is not smooth](e0-is-not-smooth.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.not_isSmooth_of_borelReducible_eZero`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/EZero.html#TauCeti.not_isSmooth_of_borelReducible_eZero).

## Sources

- [Tau Ceti documentation: `TauCeti.not_isSmooth_of_borelReducible_eZero`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/EZero.html#TauCeti.not_isSmooth_of_borelReducible_eZero)
- [Source of `TauCeti.not_isSmooth_of_borelReducible_eZero` in TauCeti/SetTheory/Descriptive/EZero.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/SetTheory/Descriptive/EZero.lean#L206)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)

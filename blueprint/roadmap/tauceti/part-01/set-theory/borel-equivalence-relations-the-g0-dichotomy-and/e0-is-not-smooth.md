---
declaration: theorem
origin: cited
lean: TauCeti.not_isSmooth_eZero
statement: formalized
proof: formalized
---

# `E₀` is not smooth

no Borel map into Cantor space has the classes of `E₀` as its
fibres.

```lean
TauCeti.not_isSmooth_eZero : ¬TauCeti.eZero.IsSmooth
```

## Depends on

- [Setoid.BorelReducible](setoid-borelreducible.md)

## Proof depends on

- [Generic ergodicity of `E₀`](generic-ergodicity-of-e0.md)
- [Smoothness is countable separation](smoothness-is-countable-separation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.not_isSmooth_eZero`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/EZero.html#TauCeti.not_isSmooth_eZero).

## Sources

- [Tau Ceti documentation: `TauCeti.not_isSmooth_eZero`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/EZero.html#TauCeti.not_isSmooth_eZero)
- [Source of `TauCeti.not_isSmooth_eZero` in TauCeti/SetTheory/Descriptive/EZero.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/SetTheory/Descriptive/EZero.lean#L201)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)

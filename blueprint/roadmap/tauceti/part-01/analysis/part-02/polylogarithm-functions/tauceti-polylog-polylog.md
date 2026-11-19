---
declaration: def
origin: cited
lean: TauCeti.Polylog.polylog
statement: formalized
---

# TauCeti.Polylog.polylog

The principal polylogarithm in integer weight. For weights at least two, the
logarithmic radial integral collapses the iterated radial integrals. Nonpositive
weights are Euler derivatives of the rational function `z / (1 - z)`.
Values at poles are totalised and carry no regularity assertion.

```lean
TauCeti.Polylog.polylog : ℤ → ℂ → ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Polylog.polylog`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.html#TauCeti.Polylog.polylog).

## Sources

- [Tau Ceti documentation: `TauCeti.Polylog.polylog`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.html#TauCeti.Polylog.polylog)
- [Source of `TauCeti.Polylog.polylog` in TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Polylogarithm/Basic.lean#L38)
- [Tau Ceti roadmap status: Polylogarithm functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PolylogarithmFunctions/STATUS.md)

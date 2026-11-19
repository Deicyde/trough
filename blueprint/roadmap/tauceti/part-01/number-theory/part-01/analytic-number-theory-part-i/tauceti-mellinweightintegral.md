---
declaration: def
origin: cited
lean: TauCeti.mellinWeightIntegral
statement: formalized
---

# TauCeti.mellinWeightIntegral

The normalized Mellin weight integral `η ∫_{t > 1} t^(-1-η) f(t) dt`. For `η > 0` the
weight `η t^(-1-η)` is a probability density on `(1, ∞)` (`mellinWeightIntegral_const`).

```lean
TauCeti.mellinWeightIntegral.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] (η : ℝ)
  (f : ℝ → E) : E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mellinWeightIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Integrals/MellinWeight.html#TauCeti.mellinWeightIntegral).

## Sources

- [Tau Ceti documentation: `TauCeti.mellinWeightIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Integrals/MellinWeight.html#TauCeti.mellinWeightIntegral)
- [Source of `TauCeti.mellinWeightIntegral` in TauCeti/Analysis/SpecialFunctions/Integrals/MellinWeight.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Integrals/MellinWeight.lean#L53)
- [Tau Ceti roadmap status: Analytic number theory, Part I](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AnalyticNumberTheoryPartI/STATUS.md)

---
declaration: theorem
origin: cited
lean: TauCeti.hasSum_airyAi_gamma
statement: formalized
proof: formalized
---

# TauCeti.hasSum_airyAi_gamma

The everywhere convergent Gamma-denominator Maclaurin series of `Ai`.

```lean
TauCeti.hasSum_airyAi_gamma (z : ℂ) :
  HasSum
    (fun n =>
      3 ^ (-2 / 3) * ((z ^ 3 / 9) ^ n / (↑n.factorial * Complex.Gamma (2 / 3 + ↑n))) -
        3 ^ (-4 / 3) * z * ((z ^ 3 / 9) ^ n / (↑n.factorial * Complex.Gamma (4 / 3 + ↑n))))
    (TauCeti.airyAi z)
```

## Depends on

- [TauCeti.airyAi](tauceti-airyai.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasSum_airyAi_gamma`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Airy/Basic.html#TauCeti.hasSum_airyAi_gamma).

## Sources

- [Tau Ceti documentation: `TauCeti.hasSum_airyAi_gamma`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Airy/Basic.html#TauCeti.hasSum_airyAi_gamma)
- [Source of `TauCeti.hasSum_airyAi_gamma` in TauCeti/Analysis/SpecialFunctions/Airy/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Airy/Basic.lean#L76)
- [Tau Ceti roadmap status: Airy and Scorer functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsAiry/STATUS.md)

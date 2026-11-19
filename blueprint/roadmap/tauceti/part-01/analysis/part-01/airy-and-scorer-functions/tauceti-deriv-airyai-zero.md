---
declaration: theorem
origin: cited
lean: TauCeti.deriv_airyAi_zero
statement: formalized
proof: formalized
---

# TauCeti.deriv_airyAi_zero

DLMF 9.2.4: the first derivative of `Ai` at the origin.

```lean
TauCeti.deriv_airyAi_zero : deriv TauCeti.airyAi 0 = -3 ^ (-1 / 3) / Complex.Gamma (1 / 3)
```

## Depends on

- [TauCeti.airyAi](tauceti-airyai.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.deriv_airyAi_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Airy/Basic.html#TauCeti.deriv_airyAi_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.deriv_airyAi_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Airy/Basic.html#TauCeti.deriv_airyAi_zero)
- [Source of `TauCeti.deriv_airyAi_zero` in TauCeti/Analysis/SpecialFunctions/Airy/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Airy/Basic.lean#L134)
- [Tau Ceti roadmap status: Airy and Scorer functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsAiry/STATUS.md)

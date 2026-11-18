---
declaration: theorem
origin: cited
lean: TauCeti.mellinWeightIntegral_log_log_le
statement: formalized
proof: formalized
---

# Jensen's bound for the Mellin weight

`η ∫_{t > 1} t^(-1-η) log log(3t) dt` is at most
`log(log 3 + η⁻¹)`. After `t = exp u` this is Jensen's inequality for the concave `log` and the
exponential density, whose mean is `η⁻¹`.

```lean
TauCeti.mellinWeightIntegral_log_log_le {η : ℝ} (hη : 0 < η) :
  (TauCeti.mellinWeightIntegral η fun t => Real.log (Real.log (3 * t))) ≤
    Real.log (Real.log 3 + η⁻¹)
```

## Depends on

- [TauCeti.mellinWeightIntegral](tauceti-mellinweightintegral.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mellinWeightIntegral_log_log_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Integrals/MellinWeight.html#TauCeti.mellinWeightIntegral_log_log_le).

## Sources

- [Tau Ceti documentation: `TauCeti.mellinWeightIntegral_log_log_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Integrals/MellinWeight.html#TauCeti.mellinWeightIntegral_log_log_le)
- [Source of `TauCeti.mellinWeightIntegral_log_log_le` in TauCeti/Analysis/SpecialFunctions/Integrals/MellinWeight.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Integrals/MellinWeight.lean#L236)
- [Tau Ceti roadmap status: Analytic number theory, Part I](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AnalyticNumberTheoryPartI/STATUS.md)

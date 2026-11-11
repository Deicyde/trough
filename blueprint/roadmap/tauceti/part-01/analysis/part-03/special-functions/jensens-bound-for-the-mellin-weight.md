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

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mellinWeightIntegral_log_log_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Integrals/MellinWeight.html#TauCeti.mellinWeightIntegral_log_log_le).

## Sources

- [Tau Ceti documentation: `TauCeti.mellinWeightIntegral_log_log_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Integrals/MellinWeight.html#TauCeti.mellinWeightIntegral_log_log_le)
- [Source of `TauCeti.mellinWeightIntegral_log_log_le` in TauCeti/Analysis/SpecialFunctions/Integrals/MellinWeight.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/Integrals/MellinWeight.lean#L195)

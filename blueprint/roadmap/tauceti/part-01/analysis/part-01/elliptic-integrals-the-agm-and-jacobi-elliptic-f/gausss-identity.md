---
declaration: theorem
origin: cited
lean: TauCeti.Real.lemniscateConstant_eq_pi_div_agm
statement: formalized
proof: formalized
---

# Gauss's identity

the lemniscate constant is `ϖ = π / M(1, √2)`, where `M` is the
arithmetic-geometric mean `NNReal.agm`.

```lean
TauCeti.Real.lemniscateConstant_eq_pi_div_agm :
  TauCeti.Real.lemniscateConstant = Real.pi / ↑(NNReal.agm 1 (NNReal.sqrt 2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gauss's theorem](gausss-theorem.md)
- [TauCeti.agmIntegral](tauceti-agmintegral.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.lemniscateConstant_eq_pi_div_agm`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Lemniscate.html#TauCeti.Real.lemniscateConstant_eq_pi_div_agm).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.lemniscateConstant_eq_pi_div_agm`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Lemniscate.html#TauCeti.Real.lemniscateConstant_eq_pi_div_agm)
- [Source of `TauCeti.Real.lemniscateConstant_eq_pi_div_agm` in TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Lemniscate.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Lemniscate.lean#L157)
- [Tau Ceti roadmap status: Elliptic integrals, the AGM, and Jacobi elliptic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticIntegrals/STATUS.md)

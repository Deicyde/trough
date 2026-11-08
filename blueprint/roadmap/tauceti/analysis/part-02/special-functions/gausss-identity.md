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

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.lemniscateConstant_eq_pi_div_agm`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Lemniscate.html#TauCeti.Real.lemniscateConstant_eq_pi_div_agm).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.lemniscateConstant_eq_pi_div_agm`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Lemniscate.html#TauCeti.Real.lemniscateConstant_eq_pi_div_agm)
- [Source of `TauCeti.Real.lemniscateConstant_eq_pi_div_agm` in TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Lemniscate.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Lemniscate.lean#L157)

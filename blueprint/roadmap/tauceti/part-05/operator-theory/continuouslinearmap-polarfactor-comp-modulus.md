---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.polarFactor_comp_modulus
statement: formalized
proof: formalized
---

# ContinuousLinearMap.polarFactor\_comp\_modulus

**Polar decomposition** of a bounded operator: `U |T| = T`.

```lean
ContinuousLinearMap.polarFactor_comp_modulus.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [CompleteSpace E]
  [NormedAddCommGroup F] [InnerProductSpace 𝕜 F] [CompleteSpace F] (T : E →L[𝕜] F) :
  T.polarFactor ∘SL T.modulus = T
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Complexification](../one-parameter-semigroups-completely-monotone-and/tauceti-complexification.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.polarFactor_comp_modulus`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Polar/Bounded.html#ContinuousLinearMap.polarFactor_comp_modulus).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.polarFactor_comp_modulus`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Polar/Bounded.html#ContinuousLinearMap.polarFactor_comp_modulus)
- [Source of `ContinuousLinearMap.polarFactor_comp_modulus` in TauCeti/Analysis/InnerProductSpace/Polar/Bounded.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/Polar/Bounded.lean#L85)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorTheory/STATUS.md)

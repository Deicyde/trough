---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.polarFactor_comp_modulus
statement: formalized
proof: formalized
---

# Polar decomposition of a bounded operator

`U |T| = T`.

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
- [Source of `ContinuousLinearMap.polarFactor_comp_modulus` in TauCeti/Analysis/InnerProductSpace/Polar/Bounded.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/Polar/Bounded.lean#L88)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorTheory/STATUS.md)

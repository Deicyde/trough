---
declaration: abbrev
origin: cited
lean: TauCeti.AbsolutelySumming
statement: formalized
---

# TauCeti.AbsolutelySumming

The operator ideal `Πₚ(E, F)` of absolutely `p`-summing operators, normed by the
`p`-summing norm `πₚ`. It is a Banach space when `F` is complete, and its inclusion
`OperatorGauge.Carrier.toContinuousLinearMapL` into the bounded operators is a contraction.

```lean
TauCeti.AbsolutelySumming.{u_1, u_2, u_3} (𝕜 : Type u_1) [NontriviallyNormedField 𝕜] (p : ENNReal)
  [Fact (1 ≤ p)] (E : Type u_2) (F : Type u_3) [SeminormedAddCommGroup E] [NormedSpace 𝕜 E]
  [SeminormedAddCommGroup F] [NormedSpace 𝕜 F] : Type (max u_2 u_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AbsolutelySumming`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Basic.html#TauCeti.AbsolutelySumming).

## Sources

- [Tau Ceti documentation: `TauCeti.AbsolutelySumming`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Basic.html#TauCeti.AbsolutelySumming)
- [Source of `TauCeti.AbsolutelySumming` in TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/AbsolutelySumming/Basic.lean#L600)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)

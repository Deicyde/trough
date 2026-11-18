---
declaration: abbrev
origin: cited
lean: TauCeti.NuclearOperator
statement: formalized
---

# TauCeti.NuclearOperator

The normed space of **nuclear operators** from `E` to `F`, normed by the nuclear norm. It is a
Banach space, isometrically isomorphic to the quotient of `E* ⊗̂π F` by the kernel of the canonical
operator (`NuclearOperator.quotKerEquiv`), and its inclusion
`OperatorGauge.Carrier.toContinuousLinearMapL` into the bounded operators is a contraction.

```lean
TauCeti.NuclearOperator.{u_1, u_3, u_4} (𝕜 : Type u_1) (E : Type u_3) (F : Type u_4)
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [CompleteSpace F] : Type (max u_3 u_4)
```

## Depends on

- [TauCeti.CompletedProjectiveTensor](tauceti-completedprojectivetensor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NuclearOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nuclear.html#TauCeti.NuclearOperator).

## Sources

- [Tau Ceti documentation: `TauCeti.NuclearOperator`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nuclear.html#TauCeti.NuclearOperator)
- [Source of `TauCeti.NuclearOperator` in TauCeti/Analysis/Normed/Operator/Nuclear.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Operator/Nuclear.lean#L433)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)

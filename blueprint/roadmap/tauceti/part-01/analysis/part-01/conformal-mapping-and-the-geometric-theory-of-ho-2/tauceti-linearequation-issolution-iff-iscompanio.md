---
declaration: theorem
origin: cited
lean: TauCeti.LinearEquation.isSolution_iff_isCompanionSolution
statement: formalized
proof: formalized
---

# TauCeti.LinearEquation.isSolution_iff_isCompanionSolution

Scalar solutions are exactly those whose unscaled derivative vector solves the
companion system.

```lean
TauCeti.LinearEquation.isSolution_iff_isCompanionSolution {U : TopologicalSpace.Opens ℂ} {n : ℕ}
  {E : TauCeti.LinearEquation U n} {y : ℂ → ℂ} :
  E.IsSolution y ↔ TauCeti.LinearEquation.IsCompanionSolution fun z j => iteratedDeriv (↑j) y z
```

## Depends on

- [TauCeti.LinearEquation](tauceti-linearequation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LinearEquation.isSolution_iff_isCompanionSolution`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Complex/LinearEquation.html#TauCeti.LinearEquation.isSolution_iff_isCompanionSolution).

## Sources

- [Tau Ceti documentation: `TauCeti.LinearEquation.isSolution_iff_isCompanionSolution`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Complex/LinearEquation.html#TauCeti.LinearEquation.isSolution_iff_isCompanionSolution)
- [Source of `TauCeti.LinearEquation.isSolution_iff_isCompanionSolution` in TauCeti/Analysis/ODE/Complex/LinearEquation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/ODE/Complex/LinearEquation.lean#L282)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions, part II](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ConformalMappingPartII/STATUS.md)

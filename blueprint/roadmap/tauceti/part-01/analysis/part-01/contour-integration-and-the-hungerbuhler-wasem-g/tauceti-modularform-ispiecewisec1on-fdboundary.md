---
declaration: theorem
origin: cited
lean: TauCeti.ModularForm.isPiecewiseC1On_fdBoundary
statement: formalized
proof: formalized
---

# TauCeti.ModularForm.isPiecewiseC1On_fdBoundary

The fundamental-domain boundary contour is piecewise `C¹` on `[0, 5]`;
`contDiffOn_fdBoundary` certifies the three genuine corners as a breakpoint witness.

```lean
TauCeti.ModularForm.isPiecewiseC1On_fdBoundary (H : ℝ) :
  TauCeti.IsPiecewiseC1On (TauCeti.ModularForm.fdBoundary H) 0 5
```

## Depends on

- [Piecewise `C¹` on the interval between `a` and `b`](piecewise-c1-on-the-interval-between-a-and-b.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularForm.isPiecewiseC1On_fdBoundary`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/LevelOne/FundamentalDomainBoundary/Basic.html#TauCeti.ModularForm.isPiecewiseC1On_fdBoundary).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularForm.isPiecewiseC1On_fdBoundary`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/LevelOne/FundamentalDomainBoundary/Basic.html#TauCeti.ModularForm.isPiecewiseC1On_fdBoundary)
- [Source of `TauCeti.ModularForm.isPiecewiseC1On_fdBoundary` in TauCeti/NumberTheory/ModularForms/LevelOne/FundamentalDomainBoundary/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/LevelOne/FundamentalDomainBoundary/Basic.lean#L525)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ContourIntegration/STATUS.md)

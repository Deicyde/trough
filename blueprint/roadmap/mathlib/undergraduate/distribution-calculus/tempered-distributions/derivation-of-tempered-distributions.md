---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: TemperedDistribution.instLineDeriv
mathlib_file: Mathlib/Analysis/Distribution/TemperedDistribution.lean
---

# Derivation of tempered distributions

The partial derivative (or directional derivative) in the direction `m : E` as a
continuous linear map on tempered distributions.

```lean
TemperedDistribution.instLineDeriv.{u_3, u_4} {E : Type u_3} {F : Type u_4} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [AddCommGroup F] [_root_.Module ℂ F] [TopologicalSpace F]
  [IsTopologicalAddGroup F] [ContinuousConstSMul ℂ F] :
  LineDeriv E (TemperedDistribution E F) (TemperedDistribution E F)
```

## Depends on

- [Stability by derivation (Spaces $\mathcal{S}(\R^d)$)](../spaces-s-r-d/stability-by-derivation.md)
- [Tempered distributions](../../../overview/analysis/distribution-theory/tempered-distributions.md)

## Sources

- [Mathlib documentation: `TemperedDistribution.instLineDeriv`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Distribution/TemperedDistribution.html#TemperedDistribution.instLineDeriv)
- [Source of `TemperedDistribution.instLineDeriv` in Mathlib/Analysis/Distribution/TemperedDistribution.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Distribution/TemperedDistribution.lean#L361)
- [Mathlib undergraduate list: Distribution calculus › Tempered distributions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L615)

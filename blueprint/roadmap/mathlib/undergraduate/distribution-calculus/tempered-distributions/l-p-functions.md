---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Lp.toTemperedDistributionCLM
mathlib_file: Mathlib/Analysis/Distribution/TemperedDistribution.lean
---

# $L^p$ functions

The natural embedding of L^p into tempered distributions.

```lean
MeasureTheory.Lp.toTemperedDistributionCLM.{u_3, u_4} {E : Type u_3} (F : Type u_4)
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℂ F]
  [CompleteSpace F] [MeasurableSpace E] [BorelSpace E]
  (μ : MeasureTheory.Measure E := by volume_tac) [μ.HasTemperateGrowth] (p : ENNReal)
  [hp : Fact (1 ≤ p)] : ↥(MeasureTheory.Lp F p μ) →L[ℂ] TemperedDistribution E F
```

## Depends on

- [$L^p$ space](../../../overview/analysis/measures-and-integral-calculus/part-01/l-p-space.md)
- [Algebra of endomorphisms of a vector space](../../linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Borel sigma-algebra](../../../overview/analysis/measures-and-integral-calculus/part-01/borel-sigma-algebra.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Extension by continuity](../../../overview/topology/general-topology/part-01/extension-by-continuity.md)
- [Tempered distributions](../../../overview/analysis/distribution-theory/tempered-distributions.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)
- [Vector-valued integrable function (Bochner integral)](../../../overview/analysis/measures-and-integral-calculus/part-01/vector-valued-integrable-function-bochner-integr.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Lp.toTemperedDistributionCLM`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Distribution/TemperedDistribution.html#MeasureTheory.Lp.toTemperedDistributionCLM)
- [Source of `MeasureTheory.Lp.toTemperedDistributionCLM` in Mathlib/Analysis/Distribution/TemperedDistribution.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Distribution/TemperedDistribution.lean#L194)
- [Mathlib undergraduate list: Distribution calculus › Tempered distributions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L618)

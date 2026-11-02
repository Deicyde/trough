---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.integral
mathlib_file: Mathlib/MeasureTheory/Integral/Bochner/Basic.lean
---

# Bochner integral

The Bochner integral

```lean
MeasureTheory.integral.{u_1, u_5} {α : Type u_1} {G : Type u_5} [NormedAddCommGroup G]
  [NormedSpace ℝ G] {x✝ : MeasurableSpace α} (μ : MeasureTheory.Measure α) (f : α → G) : G
```

## Depends on

- [$L^p$ space](l-p-space.md)
- [Completeness](../../../topology/uniform-notions/completeness.md)
- [Extension by continuity](../../../topology/general-topology/part-01/extension-by-continuity.md)
- [Norm of a continuous linear map](../../normed-vector-spaces-banach-spaces/norm-of-a-continuous-linear-map.md)
- [Normed vector space over a normed field](../../normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Vector-valued integrable function (Bochner integral)](vector-valued-integrable-function-bochner-integr.md)

## Sources

- [Mathlib documentation: `MeasureTheory.integral`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/Bochner/Basic.html#MeasureTheory.integral)
- [Source of `MeasureTheory.integral` in Mathlib/MeasureTheory/Integral/Bochner/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/Bochner/Basic.lean#L157)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L353)
- [Mathlib undergraduate list: Probability Theory › Random variables and their laws](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L562)

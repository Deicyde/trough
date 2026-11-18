# Product of finitely many measures

`Measure.pi μ` is the finite product of the measures `{μ i | i : ι}`.
It is defined to be measure corresponding to `MeasureTheory.OuterMeasure.pi`.

```lean
MeasureTheory.Measure.pi.{u_1, u_3} {ι : Type u_1} {α : ι → Type u_3} [Fintype ι]
  [(i : ι) → MeasurableSpace (α i)] (μ : (i : ι) → MeasureTheory.Measure (α i)) :
  MeasureTheory.Measure ((i : ι) → α i)
```

## Depends on

- [Carathéodory's theorem (measure theory)](../../../../thousand-plus/analysis/28-measure-and-integration/caratheodorys-theorem-measure-theory.md)
- [Positive measure](../part-01/positive-measure.md)
- [Product of sigma-algebras](../../../../undergraduate/measures-and-integral-calculus/measure-theory/product-of-sigma-algebras.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Measure.pi`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Constructions/Pi.html#MeasureTheory.Measure.pi)
- [Source of `MeasureTheory.Measure.pi` in Mathlib/MeasureTheory/Constructions/Pi.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/MeasureTheory/Constructions/Pi.lean#L208)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L358)

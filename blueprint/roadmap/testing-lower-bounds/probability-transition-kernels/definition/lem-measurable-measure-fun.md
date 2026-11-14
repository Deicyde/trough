---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Measure.measurable_of_measurable_coe
---

# measurable_measure_fun

Let $\mathcal X, \mathcal Y$ be measurable spaces, and let $f : \mathcal X \to \mathcal M(\mathcal Y)$ such that for all measurable sets $s$ of $\mathcal X$, the function $x \mapsto f(x)(s)$ is measurable. Then $f$ is measurable.

## Depends on

- [Giry monad](../../../mathlib/overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)

## Lean

Formalized as [`MeasureTheory.Measure.measurable_of_measurable_coe`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/MeasureTheory.Measure.measurable_of_measurable_coe).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 25](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L25)

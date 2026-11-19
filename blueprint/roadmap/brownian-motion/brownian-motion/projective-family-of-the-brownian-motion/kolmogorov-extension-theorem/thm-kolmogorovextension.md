---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.projectiveLimit, MeasureTheory.IsProjectiveLimit.unique, MeasureTheory.isProjectiveLimit_projectiveLimit, MeasureTheory.isFiniteMeasure_projectiveLimit, MeasureTheory.isProbabilityMeasure_projectiveLimit
---

# Kolmogorov extension theorem

Let $\mathcal{X}$ be a Polish space, equipped with the Borel $\sigma$-algebra, and let $T$ be an index set. Let $P$ be a projective family of finite measures on $\mathcal{X}$. Then the projective limit $\mu$ of $P$ exists, is unique, and is a finite measure on $\mathcal{X}^T$. Moreover, if $P_I$ is a probability measure for every finite set $I \subseteq T$, then $\mu$ is a probability measure.

## Depends on

- [Projective limit](def-isprojectivelimit.md)
- [Projective family](def-isprojectivemeasurefamily.md)

## Lean

Formalized as [`MeasureTheory.projectiveLimit`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.projectiveLimit), [`MeasureTheory.IsProjectiveLimit.unique`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.IsProjectiveLimit.unique), [`MeasureTheory.isProjectiveLimit_projectiveLimit`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.isProjectiveLimit_projectiveLimit), [`MeasureTheory.isFiniteMeasure_projectiveLimit`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.isFiniteMeasure_projectiveLimit), [`MeasureTheory.isProbabilityMeasure_projectiveLimit`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.isProbabilityMeasure_projectiveLimit).

## Sources

- [Brownian motion blueprint: chapters/projective_family.tex, line 24](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/projective_family.tex#L24)

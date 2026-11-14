---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Kernel
---

# Kernel

Let $\mathcal X, \mathcal Y$ be two measurable spaces. A probability transition kernel (or simply kernel) from $\mathcal X$ to $\mathcal Y$ is a measurable map from $\mathcal X$ to $\mathcal M (\mathcal Y)$, the measurable space of measures on $\mathcal Y$. We write $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ for a kernel $\kappa$ from $\mathcal X$ to $\mathcal Y$.

## Depends on

- [Giry monad](../../../mathlib/overview/analysis/measures-and-integral-calculus/part-01/giry-monad.md)

## Lean

Formalized as [`ProbabilityTheory.Kernel`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.Kernel).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 40](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L40)

---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Kernel.parallelComp
---

# Parallel product

Let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ and $\eta : \mathcal X' \rightsquigarrow \mathcal Y'$ be two s-finite kernels. The parallel product of $\kappa$ and $\eta$ is the kernel $\kappa \parallel \eta : \mathcal X \times \mathcal X' \rightsquigarrow \mathcal Y \times \mathcal Y'$ such that for all measurable functions $f : \mathcal Y \times \mathcal Y' \to \mathbb{R}_{+,\infty}$ and all $x \in \mathcal X \times \mathcal X'$,

$$
\begin{aligned}
\int_{y,y'} f(y,y') \partial(\kappa \parallel \eta)(x,x') = \int_y \int_{y'} f(y,y') \partial\eta(x') \partial\kappa(x) \: .
\end{aligned}
$$

## Depends on

- [Kernel](../definition/def-kernel.md)
- [s-finite kernel](../classes-of-kernels/def-sfinite-kernel.md)

## Lean

Formalized as [`ProbabilityTheory.Kernel.parallelComp`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.Kernel.parallelComp).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 185](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L185)

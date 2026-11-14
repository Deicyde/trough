---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Kernel.prod
---

# Product

Let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ and $\eta : \mathcal X \rightsquigarrow \mathcal Z$ be two s-finite kernels. The product of $\kappa$ and $\eta$ is the kernel $\kappa \times \eta : \mathcal X \rightsquigarrow \mathcal Y \times \mathcal Z$ such that for all measurable functions $f : \mathcal Y \times \mathcal Z \to \mathbb{R}_{+,\infty}$ and all $x \in \mathcal X$,

$$
\begin{aligned}
\int_{y,z} f(y,z) \partial(\kappa \times \eta)(x) = \int_y \int_z f(y,z) \partial\eta(x) \partial\kappa(x) \: .
\end{aligned}
$$

## Depends on

- [Kernel](../definition/def-kernel.md)
- [s-finite kernel](../classes-of-kernels/def-sfinite-kernel.md)

## Lean

Formalized as [`ProbabilityTheory.Kernel.prod`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.Kernel.prod).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 170](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L170)

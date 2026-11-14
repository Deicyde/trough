---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Kernel.compProd
---

# Composition-product

Let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ and $\eta : (\mathcal X \times \mathcal Y) \rightsquigarrow \mathcal Z$ be two s-finite kernels. The composition-product of $\kappa$ and $\eta$ is a kernel $\kappa \otimes \eta : \mathcal X \rightsquigarrow (\mathcal Y \times \mathcal Z)$ such that for all measurable functions $f : \mathcal Y \times \mathcal Z \to \mathbb{R}_{+,\infty}$ and $x \in \mathcal X$ ,

$$
\begin{aligned}
\int_{y,z} f(y,z) \partial(\kappa \otimes \eta)(x) = \int_y \int_z f(y,z) \partial\eta(x,y) \partial\kappa(x) \: .
\end{aligned}
$$

## Depends on

- [Kernel](../definition/def-kernel.md)
- [s-finite kernel](../classes-of-kernels/def-sfinite-kernel.md)

## Lean

Formalized as [`ProbabilityTheory.Kernel.compProd`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.Kernel.compProd).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 122](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L122)

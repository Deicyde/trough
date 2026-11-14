---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Kernel.comp
---

# Composition

Let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ and $\eta : \mathcal Y \rightsquigarrow \mathcal Z$ be two kernels. The composition of $\kappa$ and $\eta$ is the kernel $\eta \circ \kappa : \mathcal X \rightsquigarrow \mathcal Z$ such that for all measurable functions $f : \mathcal Z \to \mathbb{R}_{+,\infty}$ and all $x \in \mathcal X$,

$$
\begin{aligned}
\int_z f(z) \partial(\eta \circ \kappa)(x) = \int_y \int_z f(z) \partial\eta(y) \partial\kappa(x) \: .
\end{aligned}
$$

## Depends on

- [Kernel](../definition/def-kernel.md)

## Lean

Formalized as [`ProbabilityTheory.Kernel.comp`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.Kernel.comp).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 156](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L156)

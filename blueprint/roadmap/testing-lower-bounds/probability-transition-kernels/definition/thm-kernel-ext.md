---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Kernel.ext_fun_iff
---

# kernel_ext

Two kernels $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ are equal iff for all measurable functions $f : \mathcal Y \to \mathbb{R}_{+,\infty}$ and all $x \in \mathcal X$,

$$
\begin{aligned}
\int_y f(y) \partial \kappa(x) = \int_y f(y) \partial \eta(x) \: .
\end{aligned}
$$

## Depends on

- [Kernel](def-kernel.md)

## Lean

Formalized as [`ProbabilityTheory.Kernel.ext_fun_iff`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.Kernel.ext_fun_iff).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 70](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L70)

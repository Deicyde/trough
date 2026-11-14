---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.IsFiniteKernel
---

# Finite kernel

A kernel $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ is said to be finite if there exists $C < +\infty$ such that for all $x \in \mathcal X$, $\kappa(x)(\mathcal Y) \le C$.

## Depends on

- [Kernel](../definition/def-kernel.md)

## Lean

Formalized as [`ProbabilityTheory.IsFiniteKernel`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.IsFiniteKernel).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 88](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L88)

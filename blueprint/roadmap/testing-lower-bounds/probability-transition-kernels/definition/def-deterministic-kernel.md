---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Kernel.deterministic
---

# Deterministic kernel

The deterministic kernel defined by a measurable function $f : \mathcal X \to \mathcal Y$ is the kernel $d_f: \mathcal X \rightsquigarrow \mathcal Y$ defined by $d_f(x) = \delta_{f(x)}$, where for any $y \in \mathcal Y$, $\delta_y$ is the Dirac probability measure at $y$.

## Depends on

- [Kernel](def-kernel.md)

## Lean

Formalized as [`ProbabilityTheory.Kernel.deterministic`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.Kernel.deterministic).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 53](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L53)

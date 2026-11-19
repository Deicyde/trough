---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Kernel.condKernel, ProbabilityTheory.Kernel.disintegrate
---

# Disintegration in standard Borel spaces

If either $\mathcal X$ is countable of $\mathcal Y$ has a countably generated $\sigma$-algebra, and $\mathcal Z$ is standard Borel, then for every s-finite kernel $\kappa : \mathcal X \rightsquigarrow \mathcal Y \times \mathcal Z$, there exists a Markov kernel $\kappa_{Z \mid Y} : \mathcal X \times \mathcal Y \rightsquigarrow \mathcal Z$ that disintegrates $\kappa$.

## Depends on

- [Kernel](../definition/def-kernel.md)
- [Markov kernel](../classes-of-kernels/def-markov-kernel.md)

## Lean

Formalized as [`ProbabilityTheory.Kernel.condKernel`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.Kernel.condKernel), [`ProbabilityTheory.Kernel.disintegrate`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.Kernel.disintegrate).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 244](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L244)

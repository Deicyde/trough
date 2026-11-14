---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Measure.compProd
---

# Composition-product of a measure and a kernel

Let $\mu \in \mathcal M(\mathcal X)$ be an s-finite measure and $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ be an s-finite kernel. Let $\mathcal U$ be a measurable space with a unique element $u$. Let $\mu_k : \mathcal U \rightsquigarrow \mathcal X$ be the constant kernel with value $\mu$. The composition-product of $\mu$ and $\kappa$ is the measure on $\mathcal M(\mathcal X \times \mathcal Y)$ defined by $(\mu_k \otimes \kappa) (u)$ .

## Depends on

- [Composition-product](def-kernel-compprod.md)

## Lean

Formalized as [`MeasureTheory.Measure.compProd`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/MeasureTheory.Measure.compProd).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kernels.tex, line 146](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kernels.tex#L146)

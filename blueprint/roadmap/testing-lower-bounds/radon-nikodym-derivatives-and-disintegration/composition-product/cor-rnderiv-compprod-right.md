---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.rnDeriv_measure_compProd_right
---

# rnDeriv_compProd_right

Let $\mu \in \mathcal M(\mathcal X)$ be a finite measure and $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two finite kernels, with either $\mathcal X$ countable or $\mathcal{Y}$ countably generated. Then $(\mu \otimes \eta)$-almost surely,

$$
\begin{aligned}
\frac{d (\mu \otimes \kappa)}{d (\mu \otimes \eta)} = \frac{d \kappa}{d \eta}
\: .
\end{aligned}
$$

## Depends on

- [kernel_rnDeriv](../kernel-radon-nikodym-derivative/def-kernel-rnderiv.md)

## Lean

Formalized as [`ProbabilityTheory.rnDeriv_measure_compProd_right`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.rnDeriv_measure_compProd_right).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/rn_deriv.tex, line 261](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/rn_deriv.tex#L261)

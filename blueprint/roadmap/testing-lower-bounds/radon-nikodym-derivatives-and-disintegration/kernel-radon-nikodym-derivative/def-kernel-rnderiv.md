---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Kernel.rnDeriv
---

# kernel_rnDeriv

Let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two finite kernels, with either $\mathcal X$ countable or $\mathcal{Y}$ countably generated. The Radon-Nikodym derivative of $\kappa$ with respect to $\eta$, denoted by $\frac{d \kappa}{d \eta}$, is a measurable function $\mathcal X \times \mathcal Y \to \mathbb{R}_{+, \infty}$ with $\kappa = \frac{d \kappa}{d \eta} \cdot \eta + \kappa_{\perp \eta}$, where for all $x$, $\kappa_{\perp \eta}(x) \perp \eta(x)$.

## Depends on

Its statement uses no other node that has an article here.

## Lean

Formalized as [`ProbabilityTheory.Kernel.rnDeriv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.Kernel.rnDeriv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/rn_deriv.tex, line 16](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/rn_deriv.tex#L16)

---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Kernel.eq_rnDeriv_measure
---

# rnDeriv_unique

Let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two finite kernels, with either $\mathcal X$ countable or $\mathcal{Y}$ countably generated. If for some $f$ and $\xi$, $\kappa = f \cdot \eta + \xi$ with $\xi(x) \perp \eta(x)$ for all $x$, then for all $x$, $f(x, y) = \frac{d \kappa(x)}{d \eta(x)}(y)$ for $\eta(x)$-almost all $y \in \mathcal Y$.

## Depends on

- [kernel_rnDeriv](def-kernel-rnderiv.md)

## Proof

Let $f$ and $\xi$ be such that $\kappa = f \cdot \eta + \xi$ with $\xi(x) \perp \eta(x)$ for all $x$. Then for all $x \in \mathcal X$, $\kappa(x) = f(x, \cdot) \cdot \eta(x) + \xi(x)$ with $\xi(x) \perp \eta(x)$. By the uniqueness result for the Radon-Nikodym derivative of measures, $f(x, \cdot) = \frac{d \kappa(x)}{d \eta(x)}$ almost everywhere.

## Lean

Formalized as [`ProbabilityTheory.Kernel.eq_rnDeriv_measure`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.Kernel.eq_rnDeriv_measure).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/rn_deriv.tex, line 25](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/rn_deriv.tex#L25)

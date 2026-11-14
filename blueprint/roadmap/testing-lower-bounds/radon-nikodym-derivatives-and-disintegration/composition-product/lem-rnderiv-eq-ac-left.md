---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.rnDeriv_compProd_withDensity_rnDeriv
---

# rnDeriv_eq_ac_left

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two finite kernels. Let $\mu_{\parallel \nu} = \left(\frac{\partial \mu}{\partial \nu}\right) \cdot \nu$. Then for $(\nu \otimes \eta)$-almost all $z$, $\frac{d (\mu_{\parallel \nu} \otimes \kappa)}{d (\nu \otimes \eta)}(z) = \frac{d (\mu \otimes \kappa)}{d (\nu \otimes \eta)}(z)$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ProbabilityTheory.rnDeriv_compProd_withDensity_rnDeriv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.rnDeriv_compProd_withDensity_rnDeriv).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/rn_deriv.tex, line 158](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/rn_deriv.tex#L158)

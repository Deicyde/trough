---
declaration: corollary
origin: cited
mathlib: true
mathlib_declaration: ProbabilityTheory.Kernel.rnDeriv_eq_rnDeriv_measure
---

# rnDeriv_value

For all $x \in \mathcal X$, for $\eta(x)$-almost all $y \in \mathcal Y$, $\frac{d \kappa}{d \eta}(x, y) = \frac{d \kappa(x)}{d \eta(x)}(y)$.

## Depends on

- [kernel_rnDeriv](def-kernel-rnderiv.md)

## Proof depends on

- [rnDeriv_unique](lem-rnderiv-unique.md)

## Proof

Apply Lemma [rnDeriv_unique](lem-rnderiv-unique.md).

## Lean

Formalized as [`ProbabilityTheory.Kernel.rnDeriv_eq_rnDeriv_measure`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.Kernel.rnDeriv_eq_rnDeriv_measure).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/rn_deriv.tex, line 38](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/rn_deriv.tex#L38)

---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Measure.rnDeriv_mul_rnDeriv, MeasureTheory.Measure.rnDeriv_mul_rnDeriv'
---

# rnDeriv_chain

Let $\mu, \nu, \xi$ be $\sigma$-finite measures on $\mathcal X$.

1. If $\mu \ll \nu$ then $\xi$-almost surely, $\frac{d \mu}{d \xi} = \frac{d \mu}{d \nu} \frac{d \nu}{d \xi}$.
2. If $\nu \ll \xi$ then $\nu$-almost surely, $\frac{d \mu}{d \xi} = \frac{d \mu}{d \nu} \frac{d \nu}{d \xi}$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MeasureTheory.Measure.rnDeriv_mul_rnDeriv`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/MeasureTheory.Measure.rnDeriv_mul_rnDeriv), [`MeasureTheory.Measure.rnDeriv_mul_rnDeriv'`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/MeasureTheory.Measure.rnDeriv_mul_rnDeriv').

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/rn_deriv.tex, line 206](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/rn_deriv.tex#L206)

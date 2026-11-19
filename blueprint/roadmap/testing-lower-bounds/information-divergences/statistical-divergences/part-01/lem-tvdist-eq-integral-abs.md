---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.tvDist_eq_integral_abs_rnDeriv_add_singularPart
---

# tvDist_eq_integral_abs

For finite measures $\mu, \nu$,

$$
\begin{aligned}
\vert \mu - \nu \vert(\mathcal X)
&= \nu\left[ x \mapsto \left\vert 1 - \frac{d \mu}{d\nu}(x) \right\vert \right] + \mu_{\perp \nu}(\mathcal X)
\: .
\end{aligned}
$$

## Depends on

- [Total variation distance of Mathlib](def-tvdist.md)

## Lean

Formalized as [`MeasureTheory.tvDist_eq_integral_abs_rnDeriv_add_singularPart`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/MeasureTheory.tvDist_eq_integral_abs_rnDeriv_add_singularPart).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 639](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L639)

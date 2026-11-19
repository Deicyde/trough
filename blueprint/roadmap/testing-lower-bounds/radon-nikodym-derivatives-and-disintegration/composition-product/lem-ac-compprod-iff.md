---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Measure.absolutelyContinuous_compProd_of_compProd, MeasureTheory.Measure.absolutelyContinuous_of_compProd
---

# ac_compProd_iff

Let $\mu, \nu$ be two $\sigma$-finite measures on $\mathcal X$ and let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two s-finite kernels. Then

- (1a) if $\mu \otimes \kappa \ll \nu \otimes \eta$ then $\mu \otimes \kappa \ll \mu \otimes \eta$,
- (1b) if $\mu \otimes \kappa \ll \nu \otimes \eta$ and $\kappa(x) \ne 0$ for all $x$ then $\mu \ll \nu$,
- (2) if $\mu \ll \nu$ and $\mu \otimes \kappa \ll \mu \otimes \eta$ then $\mu \otimes \kappa \ll \nu \otimes \eta$.

In particular,

- if $\kappa(x) \ne 0$ for all $x$ then $\mu \otimes \kappa \ll \nu \otimes \eta \iff \left( \mu \ll \nu \ \wedge \ \mu \otimes \kappa \ll \mu \otimes \eta \right)$ .
- If $\mu \ll \nu$ then $\mu \otimes \kappa \ll \nu \otimes \eta \iff \mu \otimes \kappa \ll \mu \otimes \eta$ .

## Depends on

Its statement uses no other node that has an article here.

## Lean

Formalized as [`MeasureTheory.Measure.absolutelyContinuous_compProd_of_compProd`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/MeasureTheory.Measure.absolutelyContinuous_compProd_of_compProd), [`MeasureTheory.Measure.absolutelyContinuous_of_compProd`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/MeasureTheory.Measure.absolutelyContinuous_of_compProd).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/rn_deriv.tex, line 57](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/rn_deriv.tex#L57)

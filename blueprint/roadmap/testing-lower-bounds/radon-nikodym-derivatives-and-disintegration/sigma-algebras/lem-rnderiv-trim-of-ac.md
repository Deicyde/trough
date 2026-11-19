---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.toReal_rnDeriv_trim
---

# rnDeriv_trim_of_ac

Let $\mu, \nu$ be two finite measures on $\mathcal X$ with $\mu \ll \nu$ and let $\mathcal A$ be a sub-$\sigma$-algebra of $\mathcal X$. Then $\frac{d \mu_{| \mathcal A}}{d \nu_{| \mathcal A}}$ is $\nu_{| \mathcal A}$-almost everywhere (hence also $\nu$-a.e.) equal to $\nu\left[ \frac{d \mu}{d \nu} \mid \mathcal A\right]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [rnDeriv_map_eq_condexp](../composition/lem-rnderiv-map-eq-condexp.md)

## Proof

The restriction $\mu_{| \mathcal A}$ is the map of $\mu$ by the identity, seen as a function from $\mathcal X$ with its $\sigma$-algebra to $\mathcal X$ with $\mathcal{A}$. We can thus apply Lemma [rnDeriv_map_eq_condexp](../composition/lem-rnderiv-map-eq-condexp.md).

## Lean

Formalized as [`MeasureTheory.toReal_rnDeriv_trim`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/MeasureTheory.toReal_rnDeriv_trim).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/rn_deriv.tex, line 439](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/rn_deriv.tex#L439)

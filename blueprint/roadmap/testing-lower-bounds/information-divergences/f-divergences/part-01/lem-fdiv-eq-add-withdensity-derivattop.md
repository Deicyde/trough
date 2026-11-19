---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_eq_add_withDensity_derivAtTop
statement: formalized
proof: formalized
---

# fDiv_eq_add_withDensity_derivAtTop

Let $\mu$ and $\nu$ be two finite measures on $\mathcal X$. Then $D_f(\mu, \nu) = D_f(\frac{d\mu}{d\nu}\cdot \nu, \nu) + f'(\infty) \mu_{\perp \nu}(\mathcal X)$.

## Depends on

- [f-divergence](def-fdiv.md)

## Proof depends on

- [fDiv_absolutelyContinuous_add_mutuallySingular](lem-fdiv-absolutelycontinuous-add-mutuallysingul.md)

## Proof

Apply Lemma [fDiv_absolutelyContinuous_add_mutuallySingular](lem-fdiv-absolutelycontinuous-add-mutuallysingul.md) to $\frac{d\mu}{d\nu}\cdot \nu$ and $\mu_{\perp \nu}$.

## Lean

Formalized as [`ProbabilityTheory.fDiv_eq_add_withDensity_derivAtTop`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_eq_add_withDensity_derivAtTop).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 280](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L280)

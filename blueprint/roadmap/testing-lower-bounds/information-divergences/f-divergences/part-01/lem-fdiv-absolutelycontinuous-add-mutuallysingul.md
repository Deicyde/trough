---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_absolutelyContinuous_add_mutuallySingular
statement: formalized
proof: formalized
---

# fDiv_absolutelyContinuous_add_mutuallySingular

Let $\mu_1, \mu_2$ and $\nu$ be finite measures on $\mathcal X$, with $\mu_1 \ll \nu$ and $\mu_2 \perp \nu$. Then $D_f(\mu_1 + \mu_2, \nu) = D_f(\mu_1, \nu) + \mu_2(\mathcal X) f'(\infty)$.

## Depends on

- [f-divergence](def-fdiv.md)

## Proof

$\frac{d(\mu_1 + \mu_2)}{d \nu} = \frac{d \mu_1}{d \nu}$ a.e. and $(\mu_1 + \mu_2)_{\perp \nu} = \mu_2$.

## Lean

Formalized as [`ProbabilityTheory.fDiv_absolutelyContinuous_add_mutuallySingular`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_absolutelyContinuous_add_mutuallySingular).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 220](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L220)

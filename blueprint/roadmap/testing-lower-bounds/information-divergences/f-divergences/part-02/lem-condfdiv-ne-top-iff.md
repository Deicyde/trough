---
declaration: lemma
origin: cited
lean: ProbabilityTheory.condFDiv_ne_top_iff
statement: formalized
proof: formalized
---

# condFDiv_ne_top_iff

Let $\mu$ be a finite measure on $\mathcal X$ and let $\kappa, \eta : \mathcal X \rightsquigarrow \mathcal Y$ be two finite kernels, where $\kappa$ is a Markov kernel. Then $D_f(\kappa, \eta \mid \mu) \ne \infty$ if and only if

- for $\mu$-almost all $x$, $y \mapsto f \left( \frac{d\kappa(x)}{d\eta(x)}(y) \right)$ is $\eta(x)$-integrable,
- $x \mapsto \int_y f \left( \frac{d\kappa(x)}{d\eta(x)}(y) \right) \partial \eta(x)$ is $\mu$-integrable,
- either $f'(\infty) < \infty$ or for $\mu$-almost all $x$, $\kappa(x) \ll \eta(x)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)
- [Conditional f-divergence](../part-01/def-condfdiv.md)

## Proof depends on

- [integrable_fDiv_compProd_iff](../part-01/lem-integrable-fdiv-compprod-iff.md)

## Lean

Formalized as [`ProbabilityTheory.condFDiv_ne_top_iff`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.condFDiv_ne_top_iff).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 462](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L462)

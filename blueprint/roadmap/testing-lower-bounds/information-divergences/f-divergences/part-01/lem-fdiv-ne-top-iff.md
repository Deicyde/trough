---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_ne_top_iff
statement: formalized
proof: formalized
---

# fDiv_ne_top_iff

For $\mu$ and $\nu$ two finite measures, $D_f(\mu, \nu)$ is finite if and only if $x \mapsto f\left(\frac{d \mu}{d \nu}(x)\right)$ is $\nu$-integrable and either $f'(\infty) < \infty$ or $\mu \ll \nu$.

## Depends on

- [f-divergence](def-fdiv.md)

## Lean

Formalized as [`ProbabilityTheory.fDiv_ne_top_iff`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_ne_top_iff).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 23](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L23)

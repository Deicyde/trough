---
declaration: lemma
origin: cited
lean: ProbabilityTheory.condFDiv_const
statement: formalized
proof: formalized
---

# condFDiv_const

Let $\mu, \nu$ be measures on $\mathcal X$, where $\mu$ is finite, and let $\xi$ be a finite measure on $\mathcal Y$. Then $D_f(x \mapsto \mu, x \mapsto \nu \mid \xi) = D_f(\mu, \nu) \xi (\mathcal X)$.

## Depends on

- [Conditional f-divergence](def-condfdiv.md)
- [f-divergence](def-fdiv.md)

## Proof

$$
D_f(x \mapsto \mu, x \mapsto \nu \mid \xi)
= \xi\left[x \mapsto D_f(\mu, \nu)\right]
= D_f(\mu, \nu) \xi\left[1\right]
= D_f(\mu, \nu) \xi (\mathcal X)
$$

## Lean

Formalized as [`ProbabilityTheory.condFDiv_const`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.condFDiv_const).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 418](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L418)

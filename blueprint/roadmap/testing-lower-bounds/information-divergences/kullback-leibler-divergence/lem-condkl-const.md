---
declaration: lemma
origin: cited
lean: ProbabilityTheory.condKL_const
statement: formalized
proof: formalized
---

# condKL_const

Let $\mu, \nu$ be finite measures on $\mathcal X$, $\xi$ be a finite measure on $\mathcal Y$. Then $\operatorname{KL}(x \mapsto \mu, x \mapsto \nu \mid \xi) = \operatorname{KL}(\mu, \nu) \xi (\mathcal X)$.

## Depends on

- [Kullback-Leibler divergence](def-kl.md)
- [Conditional Kullback-Leibler divergence](def-condkl.md)

## Proof depends on

- [kl_eq_fDiv](lem-kl-eq-fdiv.md)
- [condFDiv_const](../f-divergences/part-01/lem-condfdiv-const.md)
- [condKL_eq_condFDiv](lem-condkl-eq-condfdiv.md)

## Proof

KL is an f-divergence thanks to Lemma [kl_eq_fDiv](lem-kl-eq-fdiv.md) and Lemma [condKL_eq_condFDiv](lem-condkl-eq-condfdiv.md), then apply Lemma [condFDiv_const](../f-divergences/part-01/lem-condfdiv-const.md).

## Lean

Formalized as [`ProbabilityTheory.condKL_const`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.condKL_const).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 73](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L73)

---
declaration: theorem
origin: cited
lean: ProbabilityTheory.klDiv_fst_le, ProbabilityTheory.klDiv_snd_le
statement: formalized
proof: formalized
---

# Marginals

Let $\mu$ and $\nu$ be two measures on $\mathcal X \times \mathcal Y$, and let $\mu_X, \nu_X$ be their marginals on $\mathcal X$. Then $\operatorname{KL}(\mu_X, \nu_X) \le \operatorname{KL}(\mu, \nu)$. Similarly, for $\mu_Y, \nu_Y$ the marginals on $\mathcal Y$, $\operatorname{KL}(\mu_Y, \nu_Y) \le \operatorname{KL}(\mu, \nu)$.

## Depends on

- [Kullback-Leibler divergence](def-kl.md)

## Proof depends on

- [Marginals](../f-divergences/part-03/thm-fdiv-fst-le-2.md)
- [kl_eq_fDiv](lem-kl-eq-fdiv.md)

## Proof

Apply Theorem [Marginals](../f-divergences/part-03/thm-fdiv-fst-le-2.md).

## Lean

Formalized as [`ProbabilityTheory.klDiv_fst_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.klDiv_fst_le), [`ProbabilityTheory.klDiv_snd_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.klDiv_snd_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/kl_divergence.tex, line 88](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/kl_divergence.tex#L88)

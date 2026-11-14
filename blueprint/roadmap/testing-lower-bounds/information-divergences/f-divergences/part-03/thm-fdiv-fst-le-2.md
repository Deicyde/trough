---
declaration: theorem
origin: cited
lean: ProbabilityTheory.fDiv_fst_le', ProbabilityTheory.fDiv_snd_le'
statement: formalized
proof: formalized
---

# Marginals

Let $\mu$ and $\nu$ be two measures on $\mathcal X \times \mathcal Y$, and let $\mu_X, \nu_X$ be their marginals on $\mathcal X$. Then $D_f(\mu_X, \nu_X) \le D_f(\mu, \nu)$. Similarly, for $\mu_Y, \nu_Y$ the marginals on $\mathcal Y$, $D_f(\mu_Y, \nu_Y) \le D_f(\mu, \nu)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [Data-processing](thm-fdiv-data-proc-2.md)

## Proof

The measure $\mu_X$ is the composition of $\mu$ and the deterministic kernel for the function $(x,y) \mapsto x$, and similarly $\mu_Y$ is the composition of $\mu$ and a deterministic kernel. The results are both applications of the data-processing inequality, Theorem [Data-processing](thm-fdiv-data-proc-2.md).

## Lean

Formalized as [`ProbabilityTheory.fDiv_fst_le'`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_fst_le'), [`ProbabilityTheory.fDiv_snd_le'`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_snd_le').

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1302](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1302)

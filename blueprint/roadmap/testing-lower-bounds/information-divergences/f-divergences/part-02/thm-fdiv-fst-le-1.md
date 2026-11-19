---
declaration: theorem
origin: cited
lean: ProbabilityTheory.fDiv_fst_le
statement: formalized
proof: formalized
---

# Marginals

Let $\mu$ and $\nu$ be two measures on $\mathcal X \times \mathcal Y$ where $\mathcal Y$ is standard Borel, and let $\mu_X, \nu_X$ be their marginals on $\mathcal X$. Then $D_f(\mu_X, \nu_X) \le D_f(\mu, \nu)$. Similarly, for $\mathcal X$ standard Borel and $\mu_Y, \nu_Y$ the marginals on $\mathcal Y$, $D_f(\mu_Y, \nu_Y) \le D_f(\mu, \nu)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [fDiv_le_compProd_1](thm-fdiv-le-compprod-1.md)
- [fDiv_map_measurableEmbedding](../part-01/lem-fdiv-map-measurableembedding.md)

## Proof

We introduce conditional kernels and write $D(\mu, \nu) = D(\mu_X \otimes \mu_{Y|X}, \nu_X \otimes \nu_{Y|X})$. Then apply Theorem [fDiv_le_compProd_1](thm-fdiv-le-compprod-1.md). For the second statement, we need Lemma [fDiv_map_measurableEmbedding](../part-01/lem-fdiv-map-measurableembedding.md) to swap the role of the two coordinates.

## Lean

Formalized as [`ProbabilityTheory.fDiv_fst_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_fst_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1014](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1014)

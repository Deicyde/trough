---
declaration: theorem
origin: cited
lean: ProbabilityTheory.renyiDiv_comp_right_le
statement: formalized
proof: formalized
---

# Data-processing

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ be a Markov kernel. Then $R_\alpha(\kappa \circ \mu, \kappa \circ \nu) \le R_\alpha(\mu, \nu)$.

## Depends on

- [Rényi divergence](def-renyi.md)

## Proof depends on

- [Data-processing](../f-divergences/part-03/thm-fdiv-data-proc-2.md)

## Proof

The function $x \mapsto \frac{1}{\alpha - 1}\log (1 + (\alpha - 1)x)$ is non-decreasing and $D_f$ satisfies the DPI (Theorem [Data-processing](../f-divergences/part-03/thm-fdiv-data-proc-2.md)), hence we get the DPI for $R_\alpha$.

## Lean

Formalized as [`ProbabilityTheory.renyiDiv_comp_right_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.renyiDiv_comp_right_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/renyi_divergence.tex, line 150](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/renyi_divergence.tex#L150)

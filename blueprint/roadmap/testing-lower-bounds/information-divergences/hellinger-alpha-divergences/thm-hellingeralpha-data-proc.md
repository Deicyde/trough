---
declaration: theorem
origin: cited
lean: ProbabilityTheory.hellingerDiv_comp_right_le
statement: formalized
proof: formalized
---

# Data-processing

Let $\alpha > 0$, $\mu, \nu$ be two finite measures on $\mathcal X$ and let $\kappa : \mathcal X \rightsquigarrow \mathcal Y$ be a Markov kernel. Then $\operatorname{H}_\alpha(\kappa \circ \mu, \kappa \circ \nu) \le \operatorname{H}_\alpha(\mu, \nu)$.

## Depends on

- [Hellinger $\alpha$-divergence](def-hellingeralpha.md)

## Proof depends on

- [Data-processing](../f-divergences/part-03/thm-fdiv-data-proc-2.md)

## Proof

Apply Theorem [Data-processing](../f-divergences/part-03/thm-fdiv-data-proc-2.md).

## Lean

Formalized as [`ProbabilityTheory.hellingerDiv_comp_right_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.hellingerDiv_comp_right_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/hellinger_alpha.tex, line 110](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/hellinger_alpha.tex#L110)

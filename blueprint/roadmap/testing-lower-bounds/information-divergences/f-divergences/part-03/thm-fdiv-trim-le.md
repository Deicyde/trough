---
declaration: theorem
origin: cited
lean: ProbabilityTheory.fDiv_trim_le
statement: formalized
proof: formalized
---

# fDiv_trim_le

Let $\mu, \nu$ be two finite measures on $\mathcal X$ and let $\mathcal A$ be a sub-$\sigma$-algebra of $\mathcal X$. Then $D_f(\mu_{| \mathcal A}, \nu_{| \mathcal A}) \le D_f(\mu, \nu)$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [fDiv_map_le](../part-02/thm-fdiv-map-le.md)

## Proof

The measure $\mathcal \mu_{| \mathcal A}$ is equal to the map of $\mu$ by the identity, seen as a function to $\mathcal X$ with the $\sigma$-algebra $\mathcal A$. That function is measurable since $\mathcal A$ is a sub-sigma-algebra. We can apply Theorem [fDiv_map_le](../part-02/thm-fdiv-map-le.md).

## Lean

Formalized as [`ProbabilityTheory.fDiv_trim_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_trim_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1173](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1173)

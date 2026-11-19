---
declaration: corollary
origin: cited
lean: ProbabilityTheory.fDiv_boolMeasure_le
statement: formalized
proof: formalized
---

# data_proc_event

Let $\mu, \nu$ be two measures on $\mathcal X$ and let $E$ be an event. Then $D_f(\mu, \nu) \ge d_f(\mu(E), \nu(E))$.

## Depends on

- [f-divergence](../part-01/def-fdiv.md)

## Proof depends on

- [Data-processing](thm-fdiv-data-proc-2.md)

## Proof

Use the deterministic kernel $\kappa : \mathcal X \rightsquigarrow \{0, 1\}$ with $\kappa(x) = \delta_1 \mathbb{I}\{x \in E\} + \delta_0 \mathbb{I}\{x \notin E\}$ in Theorem [Data-processing](thm-fdiv-data-proc-2.md).

## Lean

Formalized as [`ProbabilityTheory.fDiv_boolMeasure_le`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_boolMeasure_le).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 1339](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L1339)

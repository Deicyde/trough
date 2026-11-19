---
declaration: corollary
origin: cited
lean: ProbabilityTheory.statInfo_boolMeasure_le_statInfo
statement: formalized
proof: formalized
---

# statInfo_data_proc_event

Let $\mu, \nu$ be two measures on $\mathcal X$, $\xi \in \mathcal M(\{0,1\})$ and let $E$ be an event on $\mathcal X$. Let $\mu_E$ and $\nu_E$ be the two Bernoulli distributions with respective means $\mu(E)$ and $\nu(E)$. Then $\mathcal I_\xi(\mu, \nu) \ge \mathcal I_\xi(\mu_E, \nu_E)$.

## Depends on

- [statInfo](def-statinfo.md)

## Proof depends on

- [Data-processing inequality](thm-data-proc-statinfo.md)

## Proof

Apply Theorem [Data-processing inequality](thm-data-proc-statinfo.md) to the deterministic kernel $\mathcal X \rightsquigarrow \{0,1\}$ given by the function $x \mapsto \mathbb{I}\{x \in E\}$.

## Lean

Formalized as [`ProbabilityTheory.statInfo_boolMeasure_le_statInfo`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.statInfo_boolMeasure_le_statInfo).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/stat_div.tex, line 100](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/stat_div.tex#L100)

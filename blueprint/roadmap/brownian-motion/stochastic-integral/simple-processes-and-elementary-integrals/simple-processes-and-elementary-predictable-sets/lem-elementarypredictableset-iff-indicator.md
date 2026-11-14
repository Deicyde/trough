---
declaration: lemma
origin: cited
lean: ProbabilityTheory.ElementaryPredictableSet.indicator
statement: formalized
---

# elementaryPredictableSet_iff_indicator

A set $A \subseteq T \times \Omega$ is an elementary predictable set if and only if the indicator function $\mathbb{1}_A$ is a simple process.

## Depends on

- [Elementary predictable set](def-elementarypredictableset.md)
- [Simple process](def-simpleprocess.md)

## Proof

Suppose that $A$ is an elementary predictable set; by Lemma [elementaryPredictableSets_asDisjointUnions](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L217), $A$ is a disjoint union of predictable rectangles. In other words, $\mathbb{1}_A$ is a sum of indicator functions of predictable rectangles, and thus a simple process.

In the other direction, suppose $\mathbb{1}_A$ is a simple process,

$$
\mathbb{1}_A(t,\cdot) = \eta_0 \mathbb{1}_{\{0\}}(t) + \sum_{k=1}^{n} \eta_k \mathbb{1}_{(s_k, t_k]}(t).
$$

By Lemma [simpleProcess_admitsDisjointIntervals](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L261), we can assume that $(s_k, t_k]$ are pairwise disjoint; then each of $\eta_1$, …, $\eta_n$ must be an indicator function,

$$
\eta_k = \mathbb{1}_{F_k}, \quad\text{with } F_k \in \mathcal{F}_{s_k},
$$

and $\eta_0 = \mathbb{1}_{F_0}$ for some $F_0 \in \mathcal{F}_0$ . This shows that $A$ is a finite union of predictable rectangles, and thus an elementary predictable set.

## Lean

Stated as [`ProbabilityTheory.ElementaryPredictableSet.indicator`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.ElementaryPredictableSet.indicator); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/elementary.tex, line 314](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/elementary.tex#L314)

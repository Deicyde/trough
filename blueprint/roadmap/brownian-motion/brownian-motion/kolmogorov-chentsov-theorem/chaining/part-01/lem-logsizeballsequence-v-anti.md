---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: PairReduction.finset_logSizeBallSeq_add_one_subset
---

# logSizeBallSequence_V_anti

The sets $V_i$ of a log-size ball sequence $(V_i, t_i, r_i)_{i \in \mathbb{N}}$ are a decreasing sequence of sets. That is, $V_{i+1} \subseteq V_i$ for all $i \in \mathbb{N}$.

## Depends on

- [Log-size ball sequence](def-logsizeballsequence.md)

## Proof

$V_{i+1} = V_i \setminus B_{V_i}(t_i, (r_i - 1)c)$ hence $V_{i+1} \subseteq V_i$.

## Lean

Formalized as [`PairReduction.finset_logSizeBallSeq_add_one_subset`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/PairReduction.finset_logSizeBallSeq_add_one_subset).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 554](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L554)

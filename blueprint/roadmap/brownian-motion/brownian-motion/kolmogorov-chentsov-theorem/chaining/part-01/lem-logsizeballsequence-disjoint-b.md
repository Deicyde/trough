---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: PairReduction.disjoint_smallBall_logSizeBallSeq
---

# logSizeBallSequence_disjoint_B

For $i \ne j$, the balls $B_{V_i}(t, (r_i-1)c)$ and $B_{V_j}(t_j, (r_j-1)c)$ of a log-size ball sequence $(V_i, t_i, r_i)_{i \in \mathbb{N}}$ are disjoint.

## Depends on

- [Log-size ball sequence](def-logsizeballsequence.md)

## Proof depends on

- [logSizeBallSequence_V_anti](lem-logsizeballsequence-v-anti.md)

## Proof

Assume w.l.o.g. that $i < j$. Then $B_{V_j}(t_j, (r_j-1)c) \subseteq V_j \subseteq V_{i+1}$. It suffices to show that $B_{V_i}(t_i, (r_i-1)c)$ and $V_{i+1}$ are disjoint. This follows from the definition of $V_{i+1} = V_i \setminus B_{V_i}(t_i, (r_i-1)c)$.

## Lean

Formalized as [`PairReduction.disjoint_smallBall_logSizeBallSeq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/PairReduction.disjoint_smallBall_logSizeBallSeq).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 581](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L581)

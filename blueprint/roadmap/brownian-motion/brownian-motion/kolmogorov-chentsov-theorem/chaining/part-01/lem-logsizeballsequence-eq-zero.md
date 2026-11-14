---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: PairReduction.card_finset_logSizeBallSeq_card_eq_zero
---

# logSizeBallSequence_eq_zero

For any log-size ball sequence $(V_i, t_i, r_i)_{i \in \mathbb{N}}$ for $(J, a, c, n)$, for all $k \ge \vert J \vert$, $V_k = \emptyset$.

## Depends on

- [Log-size ball sequence](def-logsizeballsequence.md)

## Proof depends on

- [logSizeBallSequence_V_anti](lem-logsizeballsequence-v-anti.md)

## Proof

$V_{i+1} = V_i \setminus B_{V_i}(t_i, (r_i - 1)c)$ and since $t_i \in B_{V_i}(t_i, (r_i - 1)c)$, we have $\vert V_{i+1} \vert < \vert V_i \vert$ and the cardinal eventually reaches $0$, in at most $\vert J \vert$ steps.

## Lean

Formalized as [`PairReduction.card_finset_logSizeBallSeq_card_eq_zero`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/PairReduction.card_finset_logSizeBallSeq_card_eq_zero).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 567](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L567)

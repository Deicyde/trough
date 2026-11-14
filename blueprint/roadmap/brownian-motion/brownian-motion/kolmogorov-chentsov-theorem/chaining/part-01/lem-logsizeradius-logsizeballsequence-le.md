---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: PairReduction.radius_logSizeBallSeq_le
---

# logSizeRadius_logSizeBallSequence_le

The radius of a log-size ball sequence $(V_i, t_i, r_i)_{i \in \mathbb{N}}$ for $(J, a, c, n)$ satisfies $r_i \le n$ for all $i \in \mathbb{N}$.

## Depends on

- [Log-size ball sequence](def-logsizeballsequence.md)

## Proof

Since $|J| \le a^n$, we have $\vert B_{V_i}(t_i, n c) \vert \le \vert J \vert \le a^{n}$.

## Lean

Formalized as [`PairReduction.radius_logSizeBallSeq_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/PairReduction.radius_logSizeBallSeq_le).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 541](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L541)

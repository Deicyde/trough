---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: PairReduction.pairSet
---

# pairSet

Let $(V_i, t_i, r_i)_{i \in \mathbb{N}}$ be a log-size ball sequence for $(J, a, c, n)$. For $i \in \mathbb{N}$, let $K_i = \{t_i\} \times B_{V_i}(t_i, r_i c)$ be the set of pairs $(t_i, s)$ for $s$ in the ball $B_{V_i}(t_i, r_i c)$. We define $K = \bigcup_{i=0}^{\vert J \vert-1} K_i$, set of all pairs from the log-size ball sequence.

## Depends on

- [Log-size ball sequence](def-logsizeballsequence.md)

## Lean

Formalized as [`PairReduction.pairSet`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/PairReduction.pairSet).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 598](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L598)

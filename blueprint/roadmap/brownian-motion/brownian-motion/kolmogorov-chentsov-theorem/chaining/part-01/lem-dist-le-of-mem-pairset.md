---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: PairReduction.edist_le_of_mem_pairSet
---

# dist_le_of_mem_pairSet

Let $(s, t)$ be a pair in the pair set $K$ of a log-size ball sequence for $(J, a, c, n)$. Then $d_T(s, t) \le c n$.

## Depends on

- [pairSet](def-pairset.md)

## Proof depends on

- [logSizeRadius_logSizeBallSequence_le](lem-logsizeradius-logsizeballsequence-le.md)

## Proof

A pair $(t, s) \in K$ is of the form $(t_i, s)$ for $s \in B_V(t_i, r_i c)$ and satisfies

$$
\begin{aligned}
d_T(t_i, s) \le c r_i \le c n \: .
\end{aligned}
$$

The last inequality is from Lemma [logSizeRadius_logSizeBallSequence_le](lem-logsizeradius-logsizeballsequence-le.md).

## Lean

Formalized as [`PairReduction.edist_le_of_mem_pairSet`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/PairReduction.edist_le_of_mem_pairSet).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 637](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L637)

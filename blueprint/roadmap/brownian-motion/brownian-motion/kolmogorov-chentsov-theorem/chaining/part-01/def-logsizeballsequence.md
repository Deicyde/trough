---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: PairReduction.logSizeBallSeq
---

# Log-size ball sequence

Let $(T,d_T)$ be a metric space and let $J \subseteq T$ be finite, $a,c \in \mathbb R_+$ with $a \ge 1$ and $n \in \{1, 2, ...\}$ such that $|J| \le a^n$. An log-size ball sequence for $(J, a, c, n)$ is a sequence of $(V_i, t_i, r_i)_{i \in \mathbb{N}}$ such that

- $V_0 = J$, $t_0$ is an arbitrary point in $J$,
- for all $i$, $r_i$ is the log-size radius of $t_i$ in $V_i$,
- $V_{i+1} = V_i \setminus B_{V_i}(t_i, (r_i - 1)c)$, $t_{i+1}$ is arbitrarily chosen in $V_{i+1}$.

## Depends on

- [logSizeRadius](def-logsizeradius.md)

## Lean

Formalized as [`PairReduction.logSizeBallSeq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/PairReduction.logSizeBallSeq).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 525](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L525)

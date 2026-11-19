---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: PairReduction.card_pairSet_le
---

# card_pairSet_le

The cardinal of the pair set $K$ of a log-size ball sequence for $(J, a, c, n)$ satisfies $|K| \le a |J|$.

## Depends on

- [pairSet](def-pairset.md)

## Proof depends on

- [card_logSizeRadius_ge](lem-card-logsizeradius-ge.md)
- [card_logSizeRadius_le](lem-card-logsizeradius-le.md)
- [logSizeBallSequence_disjoint_B](lem-logsizeballsequence-disjoint-b.md)

## Proof

Using Lemma [card_logSizeRadius_le](lem-card-logsizeradius-le.md), the cardinal of $K$ is bounded by

$$
\begin{aligned}
\vert K \vert
&\le \sum_{i=0}^{m-1} \vert K_i \vert
\le \sum_{i=0}^{m-1} a^{r_i}
\: .
\end{aligned}
$$

Since the sets $B_{V_i}(t_i, (r_i-1)c)$ are disjoint by Lemma [logSizeBallSequence_disjoint_B](lem-logsizeballsequence-disjoint-b.md), we can use Lemma [card_logSizeRadius_ge](lem-card-logsizeradius-ge.md) to get

$$
\begin{aligned}
\sum_{i=0}^{m-1} a^{r_i - 1}
\le \sum_{i=0}^{m-1} \vert B_{V_i}(t_i, (r_i-1)c) \vert
= \left\vert \bigcup_{i=0}^{m-1} B_{V_i}(t_i, (r_i-1)c) \right\vert
\le \vert J \vert
\: .
\end{aligned}
$$

We obtained the inequality $\vert K \vert \le a \vert J \vert$

## Lean

Formalized as [`PairReduction.card_pairSet_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/PairReduction.card_pairSet_le).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 608](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L608)

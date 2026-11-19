---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: EMetric.pair_reduction
---

# pair_reduction

Let $(T,d_T)$ be a metric space. Let $J \subseteq T$ be finite, $a > 1$, $c>0$ and $n \in \{1, 2, ...\}$ such that $|J| \le a^n$. Then, there is $K \subseteq J^2$ such that for any function $f : T \to E$ with $(E,d_E)$ a metric space,

$$
\begin{aligned}
|K|
& \le a |J|
\:,\qquad\text{(1)}\\
\forall (s,t) \in K,
&\:  d_T(s,t) \le c n
\:,\qquad\text{(2)}\\
\sup_{s,t\in J, d_T(s,t) \le c} d_E(f(s), f(t))
& \le 2 \sup_{(s,t) \in K} d_E(f(s), f(t))
\: .\qquad\text{(3)}\end{aligned}
$$

## Depends on

- [pairSet](../part-01/def-pairset.md)

## Proof depends on

- [card_pairSet_le](../part-01/lem-card-pairset-le.md)
- [dist_le_of_mem_pairSet](../part-01/lem-dist-le-of-mem-pairset.md)
- [sup_dist_le_two_mul_sup_dist_pairSet](lem-sup-dist-le-two-mul-sup-dist-pairset.md)

## Proof

Let $(V_i, t_i, r_i)_{i \in \mathbb{N}}$ be a log-size ball sequence for $(J, a, c, n)$. We show that its pair set satisfies the conditions of the lemma.

Equation (1) is given by Lemma [card_pairSet_le](../part-01/lem-card-pairset-le.md). The second property (2) is Lemma [dist_le_of_mem_pairSet](../part-01/lem-dist-le-of-mem-pairset.md). Equation (3) was proved in Lemma [sup_dist_le_two_mul_sup_dist_pairSet](lem-sup-dist-le-two-mul-sup-dist-pairset.md).

## Lean

Formalized as [`EMetric.pair_reduction`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/EMetric.pair_reduction).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 688](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L688)

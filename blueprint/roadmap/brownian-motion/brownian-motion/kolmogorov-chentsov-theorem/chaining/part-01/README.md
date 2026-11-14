---
navigation: transparent
---

# nearestPt to dist_le_of_mem_pairSet

- [nearestPt](def-nearestpt.md)
- [dist_nearestPt_le](lem-dist-nearestpt-le.md)
- [dist_nearestPt_of_isCover](lem-dist-nearestpt-of-iscover.md)
- [Chaining sequence](def-chainingsequence.md)
- [chainingSequence_mem](lem-chainingsequence-mem.md)
- [dist_chainingSequence_add_one](lem-dist-chainingsequence-add-one.md)
- [dist_chainingSequence_le_sum](lem-dist-chainingsequence-le-sum.md)
- [dist_chainingSequence_le](lem-dist-chainingsequence-le.md)
- [dist_chainingSequence_pow_two_le](cor-dist-chainingsequence-pow-two-le.md)

## A subset of pairs

We will be interested in bounding expressions of the form $\sup_{s,t\in J, d_T(s,t) \le c} d_E(f(s), f(t))$ for a finite set $J$ and some function $f : T \to E$. This is a supremum over pairs in $J$ and there could be $\vert J \vert^2$ such pairs. We will build a subset $K$ of $J^2$ which is much smaller, of size linear in $\vert J \vert$, such that its points are not too far apart and

$$
\begin{aligned}
\sup_{s,t\in J, d_T(s,t) \le c} d_E(f(s), f(t))
& \le 2 \sup_{(s,t) \in K} d_E(f(s), f(t))
\: .
\end{aligned}
$$

The pairs $(s, t) \in K$ will still be close together, in the sense that $d_T(s, t) \le c n$ for some $n$ that is logarithmic in the size of $J$.

For $t \in V \subseteq T$ and $u\ge 0$, we denote by $B_V(t, u)$ the closed ball with center $t$ and radius $u$ in $V$. That is, $B_V(t, u) = \{s \in V \mid d_T(s, t) \le u\}$.

We want to cover $J$ with balls that have radius logarithmic in the number of points of the ball.

- [logSizeRadius](def-logsizeradius.md)
- [card_logSizeRadius_ge](lem-card-logsizeradius-ge.md)
- [card_logSizeRadius_le](lem-card-logsizeradius-le.md)
- [Log-size ball sequence](def-logsizeballsequence.md)

A log-size ball sequence gives a partition of $J$ into sets which are contained in balls of radius $(r_i - 1)c$ around $t_i$, and satisfy cardinality constraints.

- [logSizeRadius_logSizeBallSequence_le](lem-logsizeradius-logsizeballsequence-le.md)
- [logSizeBallSequence_V_anti](lem-logsizeballsequence-v-anti.md)
- [logSizeBallSequence_eq_zero](lem-logsizeballsequence-eq-zero.md)
- [logSizeBallSequence_disjoint_B](lem-logsizeballsequence-disjoint-b.md)
- [pairSet](def-pairset.md)
- [card_pairSet_le](lem-card-pairset-le.md)
- [dist_le_of_mem_pairSet](lem-dist-le-of-mem-pairset.md)

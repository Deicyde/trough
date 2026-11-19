---
declaration: corollary
origin: cited
lean: ProbabilityTheory.finite_set_bound_of_edist_le
statement: formalized
proof: formalized
---

# finite_set_bound_of_dist_le

Suppose that $T$ is a finite set with bounded internal covering number with constant $c_1>0$ and exponent $d > 0$. Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$, with $q > d$ and $p > 0$. For all $\delta > 0$,

$$
\begin{aligned}
\mathbb{E}\left[ \sup_{s, t \in T; d_T(s, t) \le \delta} d_E(X_s, X_t)^p \right]
&\le 2^{2p+4q+1} M c_1 \delta^{q-d} \left(4^d \left(\max\left\{0, \log_2 \left(c_1 \delta^{-d} 4^d\right) \right\} \right)^q
+ C_p\right)
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](../part-01/def-iskolmogorovprocess.md)
- [Bounded internal covering number](../../covers-and-covering-numbers/part-01/def-hasboundedinternalcoveringnumber.md)

## Proof depends on

- [finite_set_bound_of_dist_le_of_le_diam_bis](cor-finite-set-bound-of-dist-le-of-le-diam-bis.md)
- [finite_set_bound_of_dist_le_of_diam_le](thm-finite-set-bound-of-dist-le-of-diam-le.md)

## Proof

We combine Corollary [finite_set_bound_of_dist_le_of_le_diam_bis](cor-finite-set-bound-of-dist-le-of-le-diam-bis.md) and Theorem [finite_set_bound_of_dist_le_of_diam_le](thm-finite-set-bound-of-dist-le-of-diam-le.md).

## Lean

Formalized as [`ProbabilityTheory.finite_set_bound_of_edist_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.finite_set_bound_of_edist_le).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1525](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1525)

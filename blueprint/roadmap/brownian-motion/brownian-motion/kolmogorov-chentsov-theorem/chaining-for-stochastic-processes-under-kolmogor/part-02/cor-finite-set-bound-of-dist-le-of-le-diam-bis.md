---
declaration: corollary
origin: cited
lean: ProbabilityTheory.finite_set_bound_of_edist_le_of_le_diam'
statement: formalized
proof: formalized
---

# finite_set_bound_of_dist_le_of_le_diam_bis

With the same assumptions and notations as in Theorem [finite_set_bound_of_dist_le_of_le_diam](thm-finite-set-bound-of-dist-le-of-le-diam.md), for all $\delta \in (0, 4\mathrm{diam}(T)]$,

$$
\begin{aligned}
\mathbb{E}\left[ \sup_{s, t \in T; d_T(s, t) \le \delta} d_E(X_s, X_t)^p \right]
&\le 2^{2p+4q+1} M c_1 \delta^{q-d} \left(4^d \left(\log_2 \left(c_1 \delta^{-d} 4^d \right) \right)^q
+ C_p\right)
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](../part-01/def-iskolmogorovprocess.md)
- [Bounded internal covering number](../../covers-and-covering-numbers/part-01/def-hasboundedinternalcoveringnumber.md)

## Proof depends on

- [finite_set_bound_of_dist_le_of_le_diam](thm-finite-set-bound-of-dist-le-of-le-diam.md)

## Proof

We apply Theorem [finite_set_bound_of_dist_le_of_le_diam](thm-finite-set-bound-of-dist-le-of-le-diam.md) and then remark that for $\delta \le 4\mathrm{diam}(T)$, we can use the bounded internal covering number hypothesis to bound $N^{int}_{\delta/4}(T)$ :

$$
\begin{aligned}
N^{int}_{\delta/4}(T) \le c_1 \left(\frac{\delta}{4}\right)^{-d} \: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.finite_set_bound_of_edist_le_of_le_diam'`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.finite_set_bound_of_edist_le_of_le_diam').

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1503](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1503)

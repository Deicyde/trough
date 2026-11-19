---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: PairReduction.iSup_edist_pairSet
---

# sup_dist_le_two_mul_sup_dist_pairSet

Let $K$ be the pair set of a log-size ball sequence $(V_i, t_i, r_i)_{i \in \mathbb{N}}$ for $(J, a, c, n)$. Then for any function $f : T \to E$ with $(E,d_E)$ a metric space,

$$
\begin{aligned}
\sup_{s,t\in J, d_T(s,t) \le c} d_E(f(s), f(t))
& \le 2 \sup_{(s,t) \in K} d_E(f(s), f(t))
\: .
\end{aligned}
$$

## Depends on

- [pairSet](../part-01/def-pairset.md)

## Proof

Let $(s, t) \in J^2$ such that $d_T(s, t) \le c$. Then there exists a largest $\ell \in \mathbb{N}$ such that $s, t \in V_\ell$. Assume w.l.o.g. that $s \notin V_{\ell + 1}$. Then $s \in B_{V_\ell}(t_\ell, (r_\ell-1)c)$ (since $V_{\ell + 1} = V_\ell \setminus B_{V_\ell}(t_\ell, (r_\ell-1)c)$), which implies $d_T(s, t_\ell) \le (r_\ell - 1)c$.

Since $d_T(s, t) \le c$, $d_T(t, t_\ell) \le d_T(t, s) + d_T(s, t_\ell) \le r_\ell c$, hence $t \in B_{V_\ell}(t_\ell, r_\ell c)$ and we have that both $s$ and $t$ are in $B_{V_\ell}(t_\ell, r_\ell c)$. Thus both $(t_\ell, s)$ and $(t_\ell, t)$ are in $K_\ell \subseteq K$. Finally

$$
\begin{aligned}
d_E(f(s), f(t))
&\le d_E(f(s), f(t_\ell)) + d_E(f(t_\ell), f(t))
\\
&\le 2\sup_{(s',t') \in K} d_E(f(s'), f(t'))
\: .
\end{aligned}
$$

## Lean

Formalized as [`PairReduction.iSup_edist_pairSet`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/PairReduction.iSup_edist_pairSet).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 656](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L656)

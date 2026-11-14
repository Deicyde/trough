---
declaration: theorem
origin: cited
lean: ProbabilityTheory.finite_set_bound_of_edist_le_of_diam_le
statement: formalized
proof: formalized
---

# finite_set_bound_of_dist_le_of_diam_le

Suppose that $T$ is a finite set with bounded internal covering number with constant $c_1>0$ and exponent $d > 0$. Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$, with $q > d$ and $p > 0$. For all $\delta \ge 4\mathrm{diam}(T)$,

$$
\begin{aligned}
\mathbb{E}\left[ \sup_{s, t \in T; d_T(s, t) \le \delta} d_E(X_s, X_t)^p \right]
\le 4^p 2^q M c_1 \delta^{q - d} C_p
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](../part-01/def-iskolmogorovprocess.md)
- [Bounded internal covering number](../../covers-and-covering-numbers/part-01/def-hasboundedinternalcoveringnumber.md)
- [Cp](def-cp.md)

## Proof depends on

- [second_term_bound](lem-second-term-bound.md)
- [scale_change_rpow](../part-01/cor-scale-change-rpow.md)
- [lintegral_sup_cover_eq_of_lt_iInf_dist](lem-lintegral-sup-cover-eq-of-lt-iinf-dist.md)

## Proof

Let $\varepsilon_0 = \mathrm{diam}(T)$. For all $n \in \mathbb{N}$, let $C_n$ a finite $\varepsilon_n$-cover of $T$ with $C_n \subseteq T$ for $\varepsilon_n = \varepsilon_0 2^{-n}$, with minimal cardinal.

Let $k$ be a natural number such that $\varepsilon_0 2^{-k} < \inf_{s, t \in T; d_T(s,t)>0} d_T(s, t)$, which exists since $T$ is finite. By Lemma [lintegral_sup_cover_eq_of_lt_iInf_dist](lem-lintegral-sup-cover-eq-of-lt-iinf-dist.md), the supremum over $T$ can be replaced by a supremum over $C_k$.

By Corollary [scale_change_rpow](../part-01/cor-scale-change-rpow.md),

$$
\begin{aligned}
&\mathbb{E}\left[ \sup_{s, t \in C_k; d_T(s, t) \le \delta} d_E(X_s, X_t)^p \right]
\\
&\le 2^p \mathbb{E}\left[ \sup_{s, t \in C_k; d_T(s, t) \le \delta} d_E(X_{\bar{s}_0}, X_{\bar{t}_0})^p \right]
+ 4^p \mathbb{E}\left[ \sup_{s \in C_k} d_E(X_s, X_{\bar{s}_0})^p \right]
\: .
\end{aligned}
$$

Since $\varepsilon_0 = \mathrm{diam}(T)$, $C_0$ is a singleton and $d_E(X_{\bar{s}_0}, X_{\bar{t}_0}) = 0$ for all $s, t$. We thus have

$$
\begin{aligned}
\mathbb{E} \left[ \sup_{s, t \in C_k; d_T(s, t) \le \delta} d_E(X_{\bar{s}_0}, X_{\bar{t}_0})^p \right]
&= 0
\: .
\end{aligned}
$$

By Lemma [second_term_bound](lem-second-term-bound.md),

$$
\begin{aligned}
\mathbb{E} \left[\sup_{t \in C_k} d_E(X_t, X_{\bar{t}_0})^p \right]
&\le 2^q M c_1 \varepsilon_0^{q - d} C_p
\le 2^q M c_1 \delta^{q - d} C_p
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.finite_set_bound_of_edist_le_of_diam_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.finite_set_bound_of_edist_le_of_diam_le).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1378](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1378)

---
declaration: theorem
origin: cited
lean: ProbabilityTheory.finite_set_bound_of_edist_le_of_le_diam
statement: formalized
proof: formalized
---

# finite_set_bound_of_dist_le_of_le_diam

Suppose that $T$ is a finite set with bounded internal covering number with constant $c_1>0$ and exponent $d > 0$. Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$, with $q > d$ and $p > 0$. For all $\delta \in (0, 4\mathrm{diam}(T)]$,

$$
\begin{aligned}
&\mathbb{E}\left[ \sup_{s, t \in T; d_T(s, t) \le \delta} d_E(X_s, X_t)^p \right]
\\
&\le 2^{2p+4q+1} M \delta^{q-d} \left(\delta^d \left(\log_2 N^{int}_{\delta/4}(T) \right)^q  N^{int}_{\delta/4}(T)
+ c_1 C_p\right)
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](../part-01/def-iskolmogorovprocess.md)
- [Bounded internal covering number](../../covers-and-covering-numbers/part-01/def-hasboundedinternalcoveringnumber.md)
- [Cp](def-cp.md)

## Proof depends on

- [second_term_bound](lem-second-term-bound.md)
- [integral_sup_rpow_dist_cover_rescale](../part-01/lem-integral-sup-rpow-dist-cover-rescale.md)
- [scale_change_rpow](../part-01/cor-scale-change-rpow.md)
- [lintegral_sup_cover_eq_of_lt_iInf_dist](lem-lintegral-sup-cover-eq-of-lt-iinf-dist.md)
- [IsKolmogorovProcess.lintegral_sup_rpow_edist_eq_zero](../part-01/lem-iskolmogorovprocess-lintegral-sup-rpow-edist.md)

## Proof

Let $\varepsilon_0 = \mathrm{diam}(T)$. For all $n \in \mathbb{N}$, let $C_n$ a finite $\varepsilon_n$-cover of $T$ with $C_n \subseteq T$ for $\varepsilon_n = \varepsilon_0 2^{-n}$, with minimal cardinal.

Let $k$ be a natural number such that $\varepsilon_0 2^{-k} < \inf_{s, t \in T; d_T(s,t)>0} d_T(s, t)$, which exists since $T$ is finite. If $\delta \le \varepsilon_0 2^{-k}$, then $\{(s, t) \in C_k; d_T(s, t) \le \delta\} = \{(s, t) \mid s,t \in C_k, d_T(s,t) = 0\}$ and the inequality holds trivially (by Lemma [IsKolmogorovProcess.lintegral_sup_rpow_edist_eq_zero](../part-01/lem-iskolmogorovprocess-lintegral-sup-rpow-edist.md)). We can thus assume $\delta > \varepsilon_0 2^{-k}$.

By Lemma [lintegral_sup_cover_eq_of_lt_iInf_dist](lem-lintegral-sup-cover-eq-of-lt-iinf-dist.md), the supremum over $T$ can be replaced by a supremum over $C_k$.

By Corollary [scale_change_rpow](../part-01/cor-scale-change-rpow.md), for any $m \le k$,

$$
\begin{aligned}
&\mathbb{E}\left[ \sup_{s, t \in C_k; d_T(s, t) \le \delta} d_E(X_s, X_t)^p \right]
\\
&\le 2^p \mathbb{E}\left[ \sup_{s, t \in C_k; d_T(s, t) \le \delta} d_E(X_{\bar{s}_m}, X_{\bar{t}_m})^p \right]
+ 4^p \mathbb{E}\left[ \sup_{s \in C_k} d_E(X_s, X_{\bar{s}_m})^p \right]
\: .
\end{aligned}
$$

*First term*

We have $\delta \le 4\varepsilon_0$ by assumption. Let $n_2 = \lfloor \log_2(4\varepsilon_0/\delta) \rfloor$ and $m = \min\{n_2, k\}$. If $m = n_2$ then $\varepsilon_0 2^{-m} = \varepsilon_0 2^{-n_2} < \delta/2$. Otherwise, $m = k$ and $\varepsilon_0 2^{-m} = \varepsilon_0 2^{-k} < \delta$ as argued at the start of the proof. We thus get $\varepsilon_0 2^{-m} \le \delta$. We can also verify that $\delta \le \varepsilon_0 2^{-n_2+2} \le \varepsilon_0 2^{-m+2}$. By Lemma [integral_sup_rpow_dist_cover_rescale](../part-01/lem-integral-sup-rpow-dist-cover-rescale.md),

$$
\begin{aligned}
\mathbb{E} \left[ \sup_{s, t \in C_k; d_T(s, t) \le \delta} d_E(X_{\bar{s}_m}, X_{\bar{t}_m})^p \right]
&\le 2^{p+1} M \left(16 \delta \log_2 N^{int}_{\delta/4}(T) \right)^q  N^{int}_{\delta/4}(T)
\: .
\end{aligned}
$$

*Second term*

By Lemma [second_term_bound](lem-second-term-bound.md) and then the inequality $\varepsilon_0 2^{-m} \le \delta$,

$$
\begin{aligned}
\mathbb{E} \left[\sup_{t \in C_k} d_E(X_t, X_{\bar{t}_m})^p \right]
&\le 2^d M c_1 (\varepsilon_0 2^{-m+1})^{q - d} C_p
\\
&\le 2^q M c_1 \delta^{q - d} C_p
\: .
\end{aligned}
$$

Putting the two terms together, we obtain

$$
\begin{aligned}
&\mathbb{E}\left[ \sup_{s, t \in C_k; d_T(s, t) \le \delta} d_E(X_s, X_t)^p \right]
\\
&\le 4^p M \left(4\left(16 \delta \log_2 N^{int}_{\delta/4}(T) \right)^q  N^{int}_{\delta/4}(T)
+ 2^q c_1 \delta^{q - d} C_p\right)
\\
&\le 2^{2p+4q+1} M \delta^{q-d} \left(\delta^d \left(\log_2 N^{int}_{\delta/4}(T) \right)^q  N^{int}_{\delta/4}(T)
+ c_1 C_p\right)
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.finite_set_bound_of_edist_le_of_le_diam`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.finite_set_bound_of_edist_le_of_le_diam).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1427](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1427)

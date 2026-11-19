---
declaration: lemma
origin: cited
lean: ProbabilityTheory.lintegral_sup_rpow_edist_cover_rescale
statement: formalized
proof: formalized
---

# integral_sup_rpow_dist_cover_rescale

Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$. For all $n \in \mathbb{N}$, let $C_n$ a finite $\varepsilon_n$-cover of $J \subseteq T$ with $C_n \subseteq J$ for $\varepsilon_n = \varepsilon_0 2^{-n}$, with minimal cardinal. Suppose $\varepsilon_0 < \infty$, let $\delta \in (0, 4 \varepsilon_0]$ and let $m$ be a natural number such that $\varepsilon_0 2^{-m} \le \delta$ and $\delta \le \varepsilon_0 2^{-m+2}$. Then for $k \ge m$,

$$
\begin{aligned}
\mathbb{E} \left[ \sup_{s, t \in C_k; d_T(s, t) \le \delta} d_E(X_{\bar{s}_m}, X_{\bar{t}_m})^p \right]
&\le 2^{p+1} M \left(16 \delta \log_2 N^{int}_{\delta/4}(J) \right)^q  N^{int}_{\delta/4}(J)
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](def-iskolmogorovprocess.md)
- [Chaining sequence](../../chaining/part-01/def-chainingsequence.md)

## Proof depends on

- [integral_sup_rpow_dist_cover_of_dist_le](lem-integral-sup-rpow-dist-cover-of-dist-le.md)
- [dist_chainingSequence_pow_two_le](../../chaining/part-01/cor-dist-chainingsequence-pow-two-le.md)

## Proof

By definition of $m$, $\delta \le \varepsilon_0 2^{-m+2}$. For $s, t \in C_k$ with $d_T(s, t) \le \delta$, $d_T(\bar{s}_m, \bar{t}_m) \le \delta + \varepsilon_0 2^{-m+2} \le \varepsilon_0 2^{-m+3}$ (Corollary [dist_chainingSequence_pow_two_le](../../chaining/part-01/cor-dist-chainingsequence-pow-two-le.md)). It thus suffices to get a bound on $\mathbb{E} \left[ \sup_{s, t \in C_m; d_T(s, t) \le \varepsilon_0 2^{-m+3}} d_E(X_s, X_t)^p \right]$.

We can apply Lemma [integral_sup_rpow_dist_cover_of_dist_le](lem-integral-sup-rpow-dist-cover-of-dist-le.md) with $\varepsilon = \varepsilon_m$, $c = \varepsilon_0 2^{-m+3}$. We obtain

$$
\begin{aligned}
\mathbb{E} \left[ \sup_{s, t \in C_m; d_T(s, t) \le \varepsilon_0 2^{-m+3}} d_E(X_s, X_t)^p \right]
&\le 2^{p+1} M \left(16 \varepsilon_0 2^{-m} \log_2 N^{int}_{\varepsilon_m}(J) \right)^q  N^{int}_{\varepsilon_m}(J)
\: .
\end{aligned}
$$

By definition of $m$, $\varepsilon_m = \varepsilon_0 2^{-m} \ge \delta/4$, hence $N^{int}_{\varepsilon_m}(J) \le N^{int}_{\delta / 4}(J)$.

Finally, by definition of $m$ we have $\varepsilon_0 2^{-m} \le \delta$.

## Lean

Formalized as [`ProbabilityTheory.lintegral_sup_rpow_edist_cover_rescale`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.lintegral_sup_rpow_edist_cover_rescale).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 992](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L992)

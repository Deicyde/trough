---
declaration: lemma
origin: cited
lean: ProbabilityTheory.lintegral_sup_rpow_edist_le_of_minimal_cover_of_le_one
statement: formalized
proof: formalized
---

# integral_sup_rpow_dist_le_of_minimal_cover_of_le_one

Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$. Let $(\varepsilon_n)_{n \in \mathbb{N}}$ be a sequence of positive numbers in $(0, \mathrm{diam}(T)]$ and $C_n$ a finite $\varepsilon_n$-cover of $T$ with $C_n \subseteq T$, and with minimal cardinality. Suppose that $T$ has bounded internal covering number with constant $c_1>0$ and exponent $d > 0$. Then for $p \le 1$ and $m \le k$,

$$
\begin{aligned}
\mathbb{E} \left[\sup_{t \in C_k} d_E(X_t, X_{\bar{t}_m})^p \right]
&\le M c_1 \sum_{j=m}^{k-1} \varepsilon_{j+1}^{-d} \varepsilon_j^{q}
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](def-iskolmogorovprocess.md)
- [Bounded internal covering number](../../covers-and-covering-numbers/part-01/def-hasboundedinternalcoveringnumber.md)

## Proof depends on

- [integral_sup_rpow_dist_le_sum_of_le_one](lem-integral-sup-rpow-dist-le-sum-of-le-one.md)

## Proof

By Lemma [integral_sup_rpow_dist_le_sum_of_le_one](lem-integral-sup-rpow-dist-le-sum-of-le-one.md), we have

$$
\begin{aligned}
\mathbb{E}\left[\sup_{t \in C_k} d_E(X_t, X_{\bar{t}_m})^p \right]
&\le M \sum_{i=m}^{k-1} \vert C_{j+1} \vert \varepsilon_j^{q}
\: .
\end{aligned}
$$

Then by the minimality of the cardinality of $C_n$ and the bounded internal covering number hypothesis, we have

$$
\begin{aligned}
\vert C_{j+1} \vert
&= N^{int}_{\varepsilon_{j+1}}(T)
\le c_1 \varepsilon_{j+1}^{-d}
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.lintegral_sup_rpow_edist_le_of_minimal_cover_of_le_one`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.lintegral_sup_rpow_edist_le_of_minimal_cover_of_le_one).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1239](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1239)

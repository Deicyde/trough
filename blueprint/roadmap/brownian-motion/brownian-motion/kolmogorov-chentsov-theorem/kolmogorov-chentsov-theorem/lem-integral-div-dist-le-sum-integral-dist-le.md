---
declaration: lemma
origin: cited
lean: ProbabilityTheory.lintegral_div_edist_le_sum_integral_edist_le
statement: formalized
proof: formalized
---

# integral_div_dist_le_sum_integral_dist_le

Let $J \subseteq T$ be a finite set and suppose that $T$ has finite diameter. For $k \in \mathbb{N}$, let $\eta_k = 2^{-k}(\mathrm{diam}(T) + 1)$. For $X : T \to \Omega \to E$ a stochastic process and $\beta \in(0, (q - d)/p)$,

$$
\begin{aligned}
\mathbb{E}\left[ \sup_{s, t \in J;\: s \ne t} \frac{d_E(X_s, X_t)^p}{d_T(s, t)^{\beta p}} \right]
&\le \sum_{k=0}^\infty 2^{k \beta p} \mathbb{E}\left[ \sup_{s, t \in J;\: s \ne t, \: d_T(s, t) \le 2 \eta_k} d_E(X_s, X_t)^p \right]
\: .
\end{aligned}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We introduce for each $k \in \mathbb{N}$ the set of pairs $(s, t)$ such that $\eta_k < d_T(s, t) \le 2 \eta_k$. Note that $\eta_k \ge 2^{-k}$.

$$
\begin{aligned}
\mathbb{E}\left[ \sup_{s, t \in J;\: s \ne t} \frac{d_E(X_s, X_t)^p}{d_T(s, t)^{\beta p}} \right]
&\le \sum_{k=0}^\infty \mathbb{E}\left[ \sup_{s, t \in J;\: s \ne t, \: \eta_k < d_T(s, t) \le 2 \eta_k} \frac{d_E(X_s, X_t)^p}{d_T(s, t)^{\beta p}} \right]
\\
&\le \sum_{k=0}^\infty \eta_k^{-\beta p} \mathbb{E}\left[ \sup_{s, t \in J;\: s \ne t, \: d_T(s, t) \le 2 \eta_k} d_E(X_s, X_t)^p \right]
\\
&\le \sum_{k=0}^\infty 2^{k \beta p} \mathbb{E}\left[ \sup_{s, t \in J;\: s \ne t, \: d_T(s, t) \le 2 \eta_k} d_E(X_s, X_t)^p \right]
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.lintegral_div_edist_le_sum_integral_edist_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.lintegral_div_edist_le_sum_integral_edist_le).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1556](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1556)

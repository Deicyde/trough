---
declaration: lemma
origin: cited
lean: ProbabilityTheory.lintegral_sup_rpow_edist_le_sum_rpow
statement: formalized
proof: formalized
---

# integral_sup_dist_le_sum_rpow

Let $X : T \to \Omega \to E$ be a stochastic process. Let $(\varepsilon_n)_{n \in \mathbb{N}}$ be a sequence of positive numbers and $C_n$ a finite $\varepsilon_n$-cover of $T$ with $C_n \subseteq T$. For $p \ge 1$ and $m \le k$,

$$
\begin{aligned}
\mathbb{E}\left[\sup_{t \in C_k} d_E(X_t, X_{\bar{t}_m})^p \right]
&\le \left(\sum_{i=m}^{k-1} \left( \mathbb{E}\left[\sup_{t \in C_k} d_E(X_{\bar{t}_i}, X_{\bar{t}_{i+1}})^p\right] \right)^{1/p}\right)^p
\: .
\end{aligned}
$$

## Depends on

- [Chaining sequence](../../chaining/part-01/def-chainingsequence.md)

## Proof

By the triangle inequality,

$$
\begin{aligned}
\sup_{t \in C_k} d_E(X_t, X_{\bar{t}_m})^p
&\le \sup_{t \in C_k} \left( \sum_{i=m}^{k-1} d_E(X_{\bar{t}_i}, X_{\bar{t}_{i+1}}) \right)^p
\\
&\le \left( \sum_{i=m}^{k-1} \sup_{t \in C_k} d_E(X_{\bar{t}_i}, X_{\bar{t}_{i+1}}) \right)^p
\: .
\end{aligned}
$$

We thus have

$$
\begin{aligned}
\left(\mathbb{E} \left[\sup_{t \in C_k} d_E(X_t, X_{\bar{t}_m})^p \right]\right)^{1/p}
&\le \left(\mathbb{E} \left[\left( \sum_{i=m}^{k-1} \sup_{t \in C_k} d_E(X_{\bar{t}_i}, X_{\bar{t}_{i+1}}) \right)^p\right]\right)^{1/p}
\: .
\end{aligned}
$$

And then, by Minkowski's inequality, since $p \ge 1$,

$$
\begin{aligned}
\left(\mathbb{E} \left[\sup_{t \in C_k} d_E(X_t, X_{\bar{t}_m})^p \right]\right)^{1/p}
&\le \sum_{i=m}^{k-1} \left( \mathbb{E}\left[\sup_{t \in C_k} d_E(X_{\bar{t}_i}, X_{\bar{t}_{i+1}})^p \right] \right)^{1/p}
\: .
\end{aligned}
$$

Finally, we raise to the $p$-th power to obtain the result.

## Lean

Formalized as [`ProbabilityTheory.lintegral_sup_rpow_edist_le_sum_rpow`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.lintegral_sup_rpow_edist_le_sum_rpow).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1059](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1059)

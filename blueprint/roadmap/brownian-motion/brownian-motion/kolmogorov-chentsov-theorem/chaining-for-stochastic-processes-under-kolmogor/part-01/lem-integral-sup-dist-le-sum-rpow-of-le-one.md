---
declaration: lemma
origin: cited
lean: ProbabilityTheory.lintegral_sup_rpow_edist_le_sum_rpow_of_le_one
statement: formalized
proof: formalized
---

# integral_sup_dist_le_sum_rpow_of_le_one

Let $X : T \to \Omega \to E$ be a stochastic process. Let $(\varepsilon_n)_{n \in \mathbb{N}}$ be a sequence of positive numbers and $C_n$ a finite $\varepsilon_n$-cover of $T$ with $C_n \subseteq T$. For $0 < p \le 1$ and $m \le k$,

$$
\begin{aligned}
\mathbb{E}\left[\sup_{t \in C_k} d_E(X_t, X_{\bar{t}_m})^p \right]
&\le \sum_{i=m}^{k-1} \mathbb{E}\left[\sup_{t \in C_k} d_E(X_{\bar{t}_i}, X_{\bar{t}_{i+1}})^p\right]
\: .
\end{aligned}
$$

## Depends on

- [Chaining sequence](../../chaining/part-01/def-chainingsequence.md)

## Proof

For $0 < p \le 1$, the power function is sub-additive, i.e. for $a, b \ge 0$,

$$
\begin{aligned}
(a + b)^p \le a^p + b^p
\: .
\end{aligned}
$$

We can thus apply the triangle inequality to obtain

$$
\begin{aligned}
\sup_{t \in C_k} d_E(X_t, X_{\bar{t}_m})^p
&\le \sup_{t \in C_k} \left(\sum_{i=m}^{k-1} d_E(X_{\bar{t}_i}, X_{\bar{t}_{i+1}})\right)^p
\\
&\le \sup_{t \in C_k} \sum_{i=m}^{k-1} d_E(X_{\bar{t}_i}, X_{\bar{t}_{i+1}})^p
\\
&\le \sum_{i=m}^{k-1} \sup_{t \in C_k} d_E(X_{\bar{t}_i}, X_{\bar{t}_{i+1}})^p
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.lintegral_sup_rpow_edist_le_sum_rpow_of_le_one`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.lintegral_sup_rpow_edist_le_sum_rpow_of_le_one).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1186](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1186)

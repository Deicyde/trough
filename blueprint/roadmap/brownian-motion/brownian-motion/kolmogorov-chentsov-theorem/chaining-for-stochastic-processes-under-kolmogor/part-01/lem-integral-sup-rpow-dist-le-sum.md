---
declaration: lemma
origin: cited
lean: ProbabilityTheory.lintegral_sup_rpow_edist_le_sum
statement: formalized
proof: formalized
---

# integral_sup_rpow_dist_le_sum

Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$. Let $(\varepsilon_n)_{n \in \mathbb{N}}$ be a sequence of positive numbers and $C_n$ a finite $\varepsilon_n$-cover of $T$ with $C_n \subseteq T$. Then for $p \ge 1$ and $m \le k$,

$$
\begin{aligned}
\mathbb{E} \left[\sup_{t \in C_k} d_E(X_t, X_{\bar{t}_m})^p \right]
&\le M \left( \sum_{j=m}^{k-1} \vert C_{j+1} \vert^{1/p} \varepsilon_j^{q/p} \right)^p
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](def-iskolmogorovprocess.md)

## Proof depends on

- [integral_sup_rpow_dist_succ](lem-integral-sup-rpow-dist-succ.md)
- [integral_sup_dist_le_sum_rpow](lem-integral-sup-dist-le-sum-rpow.md)

## Proof

Put together Lemma [integral_sup_rpow_dist_succ](lem-integral-sup-rpow-dist-succ.md) and Lemma [integral_sup_dist_le_sum_rpow](lem-integral-sup-dist-le-sum-rpow.md).

## Lean

Formalized as [`ProbabilityTheory.lintegral_sup_rpow_edist_le_sum`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.lintegral_sup_rpow_edist_le_sum).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1098](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1098)

---
declaration: lemma
origin: cited
lean: ProbabilityTheory.lintegral_sup_cover_eq_of_lt_iInf_dist
statement: formalized
proof: formalized
---

# lintegral_sup_cover_eq_of_lt_iInf_dist

Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$ and let $J$ be a finite subset of $T$. Let $C$ be an $\varepsilon$-cover of $J$ with $C \subseteq J$. If $\varepsilon < \inf_{s, t \in J; d_T(s, t)>0} d_T(s, t)$ then

$$
\begin{aligned}
\mathbb{E}\left[ \sup_{s, t \in C; d_T(s, t) \le \delta} d_E(X_s, X_t)^p \right]
&= \mathbb{E}\left[ \sup_{s, t \in J; d_T(s, t) \le \delta} d_E(X_s, X_t)^p \right]
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](../part-01/def-iskolmogorovprocess.md)
- [$\varepsilon$-cover](../../covers-and-covering-numbers/part-01/def-iscover.md)

## Proof depends on

- [IsKolmogorovProcess.edist_eq_zero](../part-01/lem-iskolmogorovprocess-edist-eq-zero.md)

## Proof

First, remark that $C$ is actually a $0$-cover of $J$. For $s, t \in J$, let $s', t' \in C$ be such that $d_T(s, s') = 0$ and $d_T(t, t') = 0$. Then by the triangle inequality,

$$
\begin{aligned}
d_E(X_s, X_t)
&\le d_E(X_s, X_{s'}) + d_E(X_{s'}, X_{t'}) + d_E(X_t, X_{t'})
\end{aligned}
$$

and by Lemma [IsKolmogorovProcess.edist_eq_zero](../part-01/lem-iskolmogorovprocess-edist-eq-zero.md), we have $d_E(X_s, X_{s'}) = 0$ and $d_E(X_t, X_{t'}) = 0$ almost surely, hence $d_E(X_s, X_t) \le d_E(X_{s'}, X_{t'})$. Since $J$ is finite, almost surely we have that inequality for all pairs $(s, t) \in J$ and their corresponding $(s', t') \in C$. Note that $d_T(s', t') = d_T(s, t)$, hence $d_T(s, t) \le \delta$ is equivalent to $d_T(s', t') \le \delta$. We obtain

$$
\begin{aligned}
\mathbb{E}\left[ \sup_{s, t \in J; d_T(s, t) \le \delta} d_E(X_s, X_t)^p \right]
&\le \mathbb{E}\left[ \sup_{s, t \in J; d_T(s, t) \le \delta} d_E(X_{s'}, X_{t'})^p \right]
\\
&= \mathbb{E}\left[ \sup_{s, t \in J; d_T(s', t') \le \delta} d_E(X_{s'}, X_{t'})^p \right]
\\
&\le \mathbb{E}\left[ \sup_{s, t \in C; d_T(s, t) \le \delta} d_E(X_s, X_t)^p \right]
\: .
\end{aligned}
$$

The reverse inequality holds because $C$ is a subset of $J$.

## Lean

Formalized as [`ProbabilityTheory.lintegral_sup_cover_eq_of_lt_iInf_dist`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.lintegral_sup_cover_eq_of_lt_iInf_dist).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1339](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1339)

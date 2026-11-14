---
declaration: lemma
origin: cited
lean: ProbabilityTheory.lintegral_sup_rpow_edist_cover_of_dist_le
statement: formalized
proof: formalized
---

# integral_sup_rpow_dist_cover_of_dist_le

Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$. Let $C$ be a finite $\varepsilon$-cover of $J \subseteq T$ with $C \subseteq J$, with minimal cardinal. Then for $c \ge 0$,

$$
\begin{aligned}
\mathbb{E} \left[ \sup_{s, t \in C; d_T(s, t) \le c} d_E(X_s, X_t)^p \right]
&\le 2^{p+1} M \left(2 c \log_2 N^{int}_{\varepsilon}(J) \right)^q  N^{int}_{\varepsilon}(J)
\: .
\end{aligned}
$$

Note the logarithm has base $2$.

## Depends on

- [Kolmogorov condition](def-iskolmogorovprocess.md)

## Proof depends on

- [integral_sup_rpow_dist_of_dist_le](lem-integral-sup-rpow-dist-of-dist-le.md)

## Proof

Let $\bar{r} = 1 + \log_2 N^{int}_{\varepsilon}(J)$. Then

$$
\begin{aligned}
\vert C \vert
= N^{int}_{\varepsilon}(J)
\le 2^{\bar{r}}
\: .
\end{aligned}
$$

By Lemma [integral_sup_rpow_dist_of_dist_le](lem-integral-sup-rpow-dist-of-dist-le.md) with $J = C$, $a = 2$, $c = c$, $n = \bar{r}$,

$$
\begin{aligned}
\mathbb{E} \left[ \sup_{s, t \in C; d_T(s, t) \le c} d_E(X_s, X_t)^p \right]
&\le 2^{p+1} |C| M (c \bar{r})^q
= 2^{p+1} M (c \bar{r})^q N^{int}_{\varepsilon}(J)
\: .
\end{aligned}
$$

Suppose $N^{int}_{\varepsilon}(J) \ge 2$ (if it equals one the result is trivial). Then $\bar{r} \le 2 \log_2 N^{int}_{\varepsilon}(J)$.

$$
\begin{aligned}
\mathbb{E} \left[ \sup_{s, t \in C; d_T(s, t) \le c} d_E(X_s, X_t)^p \right]
&\le 2^{p+1} M \left(2 c \log_2 N^{int}_{\varepsilon}(J) \right)^q  N^{int}_{\varepsilon}(J)
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.lintegral_sup_rpow_edist_cover_of_dist_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.lintegral_sup_rpow_edist_cover_of_dist_le).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 951](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L951)

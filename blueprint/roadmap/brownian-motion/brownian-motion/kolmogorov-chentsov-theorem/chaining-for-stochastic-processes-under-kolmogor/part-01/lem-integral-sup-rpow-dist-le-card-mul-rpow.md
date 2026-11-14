---
declaration: lemma
origin: cited
lean: ProbabilityTheory.lintegral_sup_rpow_edist_le_card_mul_rpow
statement: formalized
proof: formalized
---

# integral_sup_rpow_dist_le_card_mul_rpow

Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$. Let $\varepsilon > 0$ and $C \subseteq T^2$ be a finite set such that for all $(s, t) \in C$, $d_T(s, t) \le \varepsilon$. Then

$$
\begin{aligned}
\mathbb{E}\left[\sup_{(s,t) \in C} d_E(X_s, X_t)^p \right]
&\le \vert C \vert M \varepsilon^q
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](def-iskolmogorovprocess.md)

## Proof

$$
\begin{aligned}
\mathbb{E}\left[\sup_{(s,t) \in C} d_E(X_s, X_t)^p \right]
&\le \mathbb{E}\left[\sum_{(s,t) \in C} d_E(X_s, X_t)^p \right]
\\
&\le M \sum_{(s,t) \in C} d_T(s, t)^q
\\
&\le \vert C \vert M \varepsilon^q
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.lintegral_sup_rpow_edist_le_card_mul_rpow`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.lintegral_sup_rpow_edist_le_card_mul_rpow).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 812](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L812)

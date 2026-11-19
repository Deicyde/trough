---
declaration: lemma
origin: cited
lean: ProbabilityTheory.lintegral_sup_rpow_edist_succ
statement: formalized
proof: formalized
---

# integral_sup_rpow_dist_succ

Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$. Let $(\varepsilon_n)_{n \in \mathbb{N}}$ be a sequence of positive numbers and $C_n$ a finite $\varepsilon_n$-cover of $T$ with $C_n \subseteq T$. Then for $j < k$,

$$
\begin{aligned}
\mathbb{E}\left[\sup_{t \in C_k} d_E(X_{\bar{t}_j}, X_{\bar{t}_{j+1}})^p \right]
&\le \vert C_{j+1} \vert M \varepsilon_j^q
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](def-iskolmogorovprocess.md)

## Proof depends on

- [dist_chainingSequence_add_one](../../chaining/part-01/lem-dist-chainingsequence-add-one.md)
- [integral_sup_rpow_dist_le_card_mul_rpow](lem-integral-sup-rpow-dist-le-card-mul-rpow.md)

## Proof

$$
\begin{aligned}
\mathbb{E}\left[\sup_{t \in C_k} d_E(X_{\bar{t}_j}, X_{\bar{t}_{j+1}})^p \right]
&\le \mathbb{E}\left[\sup_{u \in C_{j+1}} d_E(X_{\bar{u}_j}, X_{u})^p \right]
\: .
\end{aligned}
$$

We then apply Lemma [integral_sup_rpow_dist_le_card_mul_rpow](lem-integral-sup-rpow-dist-le-card-mul-rpow.md) to the set $C = \{(\bar{u}_j, u) \mid u \in C_{j+1}\}$, which satisfies the condition $d_T(\bar{u}_j, u) \le \varepsilon_j$ and has cardinal $\vert C_{j+1} \vert$.

## Lean

Formalized as [`ProbabilityTheory.lintegral_sup_rpow_edist_succ`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.lintegral_sup_rpow_edist_succ).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1030](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1030)

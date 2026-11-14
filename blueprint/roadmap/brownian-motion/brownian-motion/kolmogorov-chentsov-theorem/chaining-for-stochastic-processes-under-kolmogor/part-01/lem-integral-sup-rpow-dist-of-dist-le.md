---
declaration: lemma
origin: cited
lean: ProbabilityTheory.lintegral_sup_rpow_edist_le_card_mul_rpow_of_dist_le
statement: formalized
proof: formalized
---

# integral_sup_rpow_dist_of_dist_le

Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$. Let $J \subseteq T$ be finite, $a, c \in \mathbb R_+$ with $a \ge 1$ and $n \in \{1, 2, ...\}$ such that $|J| \le a^n$. Then

$$
\begin{aligned}
\mathbb{E} \left[ \sup_{s, t \in J; d_T(s, t) \le c} d_E(X_s, X_t)^p \right]
&\le 2^p a |J| M (cn)^q
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](def-iskolmogorovprocess.md)

## Proof depends on

- [pair_reduction](../../chaining/part-02/lem-pair-reduction.md)
- [integral_sup_rpow_dist_le_card_mul_rpow](lem-integral-sup-rpow-dist-le-card-mul-rpow.md)

## Proof

By Lemma [pair_reduction](../../chaining/part-02/lem-pair-reduction.md), there exists $K \subseteq J^2$ such that

$$
\begin{aligned}
|K|
& \le a |J|
\:, \\
\forall (s,t) \in K,
& \ d_T(s,t) \le c n
\:, \\
\sup_{s,t\in J, d_T(s,t) \le c} d_E(X_s, X_t)
& \le 2 \sup_{(s,t) \in K} d_E(X_s, X_t)
\: .
\end{aligned}
$$

Hence for such a set $K$,

$$
\begin{aligned}
\mathbb{E} \left[ \sup_{s, t \in J; d_T(s, t) \le c} d_E(X_s, X_t)^p \right]
&\le 2^p \mathbb{E} \left[ \sup_{(s, t) \in K} d_E(X_s, X_t)^p \right]
\: .
\end{aligned}
$$

Then by Lemma [integral_sup_rpow_dist_le_card_mul_rpow](lem-integral-sup-rpow-dist-le-card-mul-rpow.md),

$$
\begin{aligned}
\mathbb{E} \left[ \sup_{(s, t) \in K} d_E(X_s, X_t)^p \right]
&\le |K| M (cn)^q
\le a |J| M (cn)^q
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.lintegral_sup_rpow_edist_le_card_mul_rpow_of_dist_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.lintegral_sup_rpow_edist_le_card_mul_rpow_of_dist_le).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 840](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L840)

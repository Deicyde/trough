---
declaration: theorem
origin: cited
lean: ProbabilityTheory.countable_kolmogorov_chentsov
statement: formalized
proof: formalized
---

# countable_set_bound

Suppose that $T$ has bounded internal covering number with constant $c_1>0$ and exponent $d > 0$. Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$, with $q > d$ and $p > 0$. Let $\beta \in(0, (q - d)/p)$. Then for every countable subset $T' \subseteq T$ with positive diameter,

$$
\begin{aligned}
\mathbb{E}\left[ \sup_{s, t \in T';\: s \ne t} \frac{d_E(X_s, X_t)^p}{d_T(s, t)^{\beta p}} \right]
\le M L(c_1, d, p, q, \beta)
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](../chaining-for-stochastic-processes-under-kolmogor/part-01/def-iskolmogorovprocess.md)
- [Bounded internal covering number](../covers-and-covering-numbers/part-01/def-hasboundedinternalcoveringnumber.md)

## Proof depends on

- [finite_set_bound](lem-finite-set-bound.md)

## Proof

Build a monotone sequence of finite sets $T_n \subseteq T'$, use Lemma [finite_set_bound](lem-finite-set-bound.md) to obtain a bound for each $T_n$ that does not depend on $T_n$, and then use monotone convergence.

## Lean

Formalized as [`ProbabilityTheory.countable_kolmogorov_chentsov`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.countable_kolmogorov_chentsov).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1672](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1672)

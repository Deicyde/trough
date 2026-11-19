---
declaration: lemma
origin: cited
lean: ProbabilityTheory.finite_kolmogorov_chentsov
statement: formalized
proof: formalized
---

# finite_set_bound

Suppose that $J \subseteq T$ is a finite set and that $T$ has bounded internal covering number with constant $c_1>0$ and exponent $d > 0$. Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$, with $q > d$ and $p > 0$. Let $\beta \in(0, (q - d)/p)$. Then

$$
\begin{aligned}
\mathbb{E}\left[ \sup_{s, t \in J;\: s \ne t} \frac{d_E(X_s, X_t)^p}{d_T(s, t)^{\beta p}} \right]
\le M L(c_1, d, p, q, \beta)
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](../chaining-for-stochastic-processes-under-kolmogor/part-01/def-iskolmogorovprocess.md)
- [Bounded internal covering number](../covers-and-covering-numbers/part-01/def-hasboundedinternalcoveringnumber.md)
- [L](def-l.md)

## Proof depends on

- [finite_set_bound_of_dist_le](../chaining-for-stochastic-processes-under-kolmogor/part-02/cor-finite-set-bound-of-dist-le.md)
- [integral_div_dist_le_sum_integral_dist_le](lem-integral-div-dist-le-sum-integral-dist-le.md)
- [hasBoundedInternalCoveringNumber_subset](../covers-and-covering-numbers/part-02/lem-hasboundedinternalcoveringnumber-subset.md)
- [hasBoundedInternalCoveringNumber_diam_le](../covers-and-covering-numbers/part-02/lem-hasboundedinternalcoveringnumber-diam-le.md)

## Proof

Since $J \subseteq T$, $J$ has bounded internal covering number with constant $2^d c_1$ and exponent $d$ (Lemma [hasBoundedInternalCoveringNumber_subset](../covers-and-covering-numbers/part-02/lem-hasboundedinternalcoveringnumber-subset.md)).

Let $\eta_k = 2^{-k}(\mathrm{diam}(T) + 1)$ for $k \in \mathbb{N}$. By Lemma [integral_div_dist_le_sum_integral_dist_le](lem-integral-div-dist-le-sum-integral-dist-le.md), we have

$$
\begin{aligned}
\mathbb{E}\left[ \sup_{s, t \in J;\: s \ne t} \frac{d_E(X_s, X_t)^p}{d_T(s, t)^{\beta p}} \right]
&\le \sum_{k=0}^\infty 2^{k \beta p} \mathbb{E}\left[ \sup_{s, t \in J;\: s \ne t, \: d_T(s, t) \le 2 \eta_k} d_E(X_s, X_t)^p \right]
\: .
\end{aligned}
$$

We apply Corollary [finite_set_bound_of_dist_le](../chaining-for-stochastic-processes-under-kolmogor/part-02/cor-finite-set-bound-of-dist-le.md) to bound each expectation in the sum.

$$
\begin{aligned}
&\mathbb{E}\left[ \sup_{s, t \in J;\: s \ne t, \: d_T(s, t) \le 2 \eta_k} d_E(X_s, X_t)^p \right]
\\
&\le 2^{2p+4q+1} M 2^d c_1 (2 \eta_k)^{q-d} \left(4^d \left(\max\left\{0, \log_2 \left(2^d c_1 (2 \eta_k)^{-d} 4^d \right) \right\} \right)^q
+ C_p\right)
\\
&\le 2^{2p+5q+1} M c_1 (\mathrm{diam}(T)+1)^{q-d} 2^{-k(q-d)} \left(4^d \left(\max\left\{0, \log_2 \left(c_1 2^{(k + 2)d} \right) \right\} \right)^q
+ C_p\right)
\\
&= 2^{2p+5q+1} M c_1 (\mathrm{diam}(T)+1)^{q-d} 2^{-k(q-d)} \left(4^d \left(\max\left\{0, \log_2(c_1) + (k + 2)d \right\} \right)^q
+ C_p\right)
\\
&\le 2^{2p+5q+1} M c_1 (c_1^{1/d}+1)^{q-d} 2^{-k(q-d)} \left(4^d \left(\max\left\{0, \log_2(c_1) + (k + 2)d \right\} \right)^q
+ C_p\right)
\: ,
\end{aligned}
$$

where the last inequality uses $\mathrm{diam}(T) \le c_1^{1/d}$ (Lemma [hasBoundedInternalCoveringNumber_diam_le](../covers-and-covering-numbers/part-02/lem-hasboundedinternalcoveringnumber-diam-le.md)). The sum is then less than $M$ times $L(c_1, d, p, q, \beta)$.

## Lean

Formalized as [`ProbabilityTheory.finite_kolmogorov_chentsov`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.finite_kolmogorov_chentsov).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1622](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1622)

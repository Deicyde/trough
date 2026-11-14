---
declaration: lemma
origin: cited
lean: ProbabilityTheory.second_term_bound
statement: formalized
proof: formalized
---

# second_term_bound

Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$. Let $C_n$ a finite $(\varepsilon_0 2^{-n})$-cover of $T$ for $\varepsilon_0 \le \mathrm{diam}(T)$ with $C_n \subseteq T$, and with minimal cardinality. Suppose that $T$ has bounded internal covering number with constant $c_1>0$ and exponent $d > 0$. Then for $m \le k$,

$$
\begin{aligned}
\mathbb{E} \left[\sup_{t \in C_k} d_E(X_t, X_{\bar{t}_m})^p \right]
&\le 2^d M c_1 (\varepsilon_0 2^{-m + 1})^{q - d} C_p
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](../part-01/def-iskolmogorovprocess.md)
- [Bounded internal covering number](../../covers-and-covering-numbers/part-01/def-hasboundedinternalcoveringnumber.md)
- [Cp](def-cp.md)

## Proof depends on

- [integral_sup_rpow_dist_le_of_minimal_cover_two_of_le_one](cor-integral-sup-rpow-dist-le-of-minimal-cover-t.md)
- [integral_sup_rpow_dist_le_of_minimal_cover_two](../part-01/cor-integral-sup-rpow-dist-le-of-minimal-cover-t.md)

## Proof

This is the max of the two bounds obtained $p \ge 1$ and $p \le 1$.

## Lean

Formalized as [`ProbabilityTheory.second_term_bound`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.second_term_bound).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1314](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1314)

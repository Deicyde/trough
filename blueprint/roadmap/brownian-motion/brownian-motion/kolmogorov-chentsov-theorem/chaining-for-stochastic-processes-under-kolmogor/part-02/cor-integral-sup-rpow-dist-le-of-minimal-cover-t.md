---
declaration: corollary
origin: cited
lean: ProbabilityTheory.lintegral_sup_rpow_edist_le_of_minimal_cover_two_of_le_one
statement: formalized
proof: formalized
---

# integral_sup_rpow_dist_le_of_minimal_cover_two_of_le_one

Under the assumptions of Lemma [integral_sup_rpow_dist_le_of_minimal_cover_of_le_one](../part-01/lem-integral-sup-rpow-dist-le-of-minimal-cover-o.md), for $\varepsilon_n = \varepsilon_0 2^{-n}$, then for $m \le k$,

$$
\begin{aligned}
\mathbb{E} \left[\sup_{t \in C_k} d_E(X_t, X_{\bar{t}_m})^p \right]
&\le 2^d M c_1 (\varepsilon_0 2^{-m + 1})^{q - d} \frac{1}{\left( 2^{(q -d)} - 1\right)}
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](../part-01/def-iskolmogorovprocess.md)
- [Bounded internal covering number](../../covers-and-covering-numbers/part-01/def-hasboundedinternalcoveringnumber.md)

## Proof depends on

- [integral_sup_rpow_dist_le_of_minimal_cover_of_le_one](../part-01/lem-integral-sup-rpow-dist-le-of-minimal-cover-o.md)

## Proof

Applying first Lemma [integral_sup_rpow_dist_le_of_minimal_cover_of_le_one](../part-01/lem-integral-sup-rpow-dist-le-of-minimal-cover-o.md), we get

$$
\begin{aligned}
\mathbb{E} \left[\sup_{t \in C_k} d_E(X_t, X_{\bar{t}_m})^p \right]
&\le 2^d M c_1 (\varepsilon_0 2^{-m})^{q-d}\sum_{j=0}^{k-m-1} 2^{- j (q - d)}
\\
&\le 2^d M c_1 (\varepsilon_0 2^{-m})^{q-d}\sum_{j=0}^{+\infty} 2^{- j (q - d)}
\\
&= 2^d M c_1 (\varepsilon_0 2^{-m})^{q-d} \frac{1}{1 - 2^{-(q - d)}}
\\
&= 2^d M c_1 (\varepsilon_0 2^{-m+1})^{q-d} \frac{1}{2^{(q - d)} - 1}
\: .
\end{aligned}
$$

## Lean

Formalized as [`ProbabilityTheory.lintegral_sup_rpow_edist_le_of_minimal_cover_two_of_le_one`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.lintegral_sup_rpow_edist_le_of_minimal_cover_two_of_le_one).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 1272](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L1272)

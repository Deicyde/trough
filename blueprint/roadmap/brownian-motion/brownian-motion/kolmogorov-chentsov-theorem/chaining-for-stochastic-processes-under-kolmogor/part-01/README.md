---
navigation: transparent
---

# Kolmogorov condition to integral_sup_rpow_dist_le_of_min…

- [Kolmogorov condition](def-iskolmogorovprocess.md)

Remark: the measurability condition on the pair would be implied by the measurability of $X_t$ for all $t \in T$ if we assumed that $E$ is separable (`SecondCountableTopology` in Lean), which implies that the Borel $\sigma$-algebra on the product is equal to the product of the Borel $\sigma$-algebras. We follow (kratschmer2023kolmogorov) and do not require separability.

- [IsKolmogorovProcess.edist_eq_zero](lem-iskolmogorovprocess-edist-eq-zero.md)
- [IsKolmogorovProcess.lintegral_sup_rpow_edist_eq_zero](lem-iskolmogorovprocess-lintegral-sup-rpow-edist.md)

Measurability

- [IsKolmogorovProcess.aemeasurable](lem-iskolmogorovprocess-aemeasurable.md)
- [aemeasurable_pair_of_aemeasurable](lem-aemeasurable-pair-of-aemeasurable.md)
- [IsKolmogorovProcess.aemeasurable_edist](lem-iskolmogorovprocess-aemeasurable-edist.md)

Distance bounds

- [integral_sup_rpow_dist_le_card_mul_rpow](lem-integral-sup-rpow-dist-le-card-mul-rpow.md)
- [integral_sup_rpow_dist_of_dist_le](lem-integral-sup-rpow-dist-of-dist-le.md)

## Bound for a set of points that are close together

For a finite index set $T$, we want to obtain a bound on

$$
\begin{aligned}
\mathbb{E}\left[ \sup_{s, t \in T; d_T(s, t) \le \delta} d_E(X_s, X_t)^p \right] \: .
\end{aligned}
$$

Note the condition that the supremum is taken over pairs $(s, t)$ such that $d_T(s, t) \le \delta$.

We consider covers of $T$ at different scales. $C_n$ is a finite $\varepsilon_n$-cover of $T$ with $\varepsilon_n = \varepsilon_0 2^{-n}$. $T$ is equal to $C_k$ for some $k$ large enough, so the supremum over $T$ is a supremum at that scale $k$. We will change scale to some $m \le k$ that depends on the distance bound $\delta$ ($m$ is of order $\log_2 \delta$) and consider the supremum over $C_m$ (plus a term due to the scale change). Then for the supremum over a set in $C_m$, we use the reduction in the number of pairs of Lemma [pair_reduction](../../chaining/part-02/lem-pair-reduction.md).

- [scale_change](lem-scale-change.md)
- [scale_change_rpow](cor-scale-change-rpow.md)

### First term

- [integral_sup_rpow_dist_cover_of_dist_le](lem-integral-sup-rpow-dist-cover-of-dist-le.md)
- [integral_sup_rpow_dist_cover_rescale](lem-integral-sup-rpow-dist-cover-rescale.md)

### Second term

- [integral_sup_rpow_dist_succ](lem-integral-sup-rpow-dist-succ.md)

Case $p \ge 1$

- [integral_sup_dist_le_sum_rpow](lem-integral-sup-dist-le-sum-rpow.md)
- [integral_sup_rpow_dist_le_sum](lem-integral-sup-rpow-dist-le-sum.md)
- [integral_sup_rpow_dist_le_of_minimal_cover](lem-integral-sup-rpow-dist-le-of-minimal-cover.md)
- [integral_sup_rpow_dist_le_of_minimal_cover_two](cor-integral-sup-rpow-dist-le-of-minimal-cover-t.md)

Case $p \le 1$

- [integral_sup_dist_le_sum_rpow_of_le_one](lem-integral-sup-dist-le-sum-rpow-of-le-one.md)
- [integral_sup_rpow_dist_le_sum_of_le_one](lem-integral-sup-rpow-dist-le-sum-of-le-one.md)
- [integral_sup_rpow_dist_le_of_minimal_cover_of_le_one](lem-integral-sup-rpow-dist-le-of-minimal-cover-o.md)

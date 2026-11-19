---
declaration: lemma
origin: cited
lean: MIPRE.sum_norm_charSum_sq, MIPRE.sum_sgn_trMul_eq_ite, MIPRE.sum_star_sgn_trMul, MIPRE.sum_star_sgn_trMul2, MIPRE.sum_norm_trSum_sq, MIPRE.sum_norm_trSum2_sq, MIPRE.sum_avg_norm_fibreSum_sq, MIPRE.StateModel.sum_avg_snorm_sq_fibre_eq, MIPRE.BipartiteModel.sum_avg_stateSqNorm_fibre_eq, MIPRE.BipartiteModel.sum_avg_xSqNorm_fibre_eq
statement: formalized
proof: formalized
---

# Parseval in a model

Let $E$ be a complex inner product space and $\mathbb{F}_q$ a finite field of characteristic two.

1. If the characters $\chi_r$ satisfy $\sum_r \overline{\chi_r(a)}\chi_r(b) = c\,[a = b]$, then $\sum_r \|\sum_a \chi_r(a) T_a\|^2 = c \sum_a \|T_a\|^2$ for every family $(T_a)$ in $E$. The characters $a \mapsto (-1)^{\mathrm{tr}(ar)}$ of $\mathbb{F}_q$ satisfy this with $c = q$, and their products on $\mathbb{F}_q \times \mathbb{F}_q$ with $c = q^2$.
2. A family $(U_p)_{p \in \mathbb{F}_q \times \mathbb{F}_q}$ in $E$ summing to zero has, on average over uniform $(\alpha, \beta) \in \mathbb{F}_q \times \mathbb{F}_q$, fibre sums under $(a, b) \mapsto \alpha a + \beta b$ of total squared norm $(1 - 1/q) \sum_p \|U_p\|^2$.
3. Consequently the same holds, in a bipartite model, for the state norms of a family of the represented algebra summing to zero, for those of a family of one player's operators summing to zero, and for the cross-party deviations of two families, one for each player, each summing to ${I}$.

## Depends on

- [Bipartite model](../part-02/def-bipartite-model.md)
- [Generalized Pauli observables in characteristic two](../../foundations/part-02/def-generalized-pauli.md)

## Proof

Item 1 expands the squared norms of the transform into a double sum over the family, of which the orthogonality of the characters keeps the diagonal. In item 2, two distinct points lie in a common fibre for a fraction $1/q$ of the coefficients $(\alpha, \beta)$, so the average is the sum of the squared norms plus $1/q$ times the off-diagonal sum, which the zero-sum hypothesis makes $-1/q$ times the diagonal; the formal proof writes the indicator of a fibre as an average of the characters of item 1. Item 3 applies item 2 to the vectors $\pi(T)\psi$; for the cross-party deviations, the differences of the two families' operators sum to ${I} - {I} = 0$.

## Lean

Formalized as [`MIPRE.sum_norm_charSum_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_norm_charSum_sq), [`MIPRE.sum_sgn_trMul_eq_ite`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_sgn_trMul_eq_ite), [`MIPRE.sum_star_sgn_trMul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_star_sgn_trMul), [`MIPRE.sum_star_sgn_trMul2`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_star_sgn_trMul2), [`MIPRE.sum_norm_trSum_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_norm_trSum_sq), [`MIPRE.sum_norm_trSum2_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_norm_trSum2_sq), [`MIPRE.sum_avg_norm_fibreSum_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.sum_avg_norm_fibreSum_sq), [`MIPRE.StateModel.sum_avg_snorm_sq_fibre_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.StateModel.sum_avg_snorm_sq_fibre_eq), [`MIPRE.BipartiteModel.sum_avg_stateSqNorm_fibre_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.sum_avg_stateSqNorm_fibre_eq), [`MIPRE.BipartiteModel.sum_avg_xSqNorm_fibre_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.sum_avg_xSqNorm_fibre_eq).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2692](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2692)

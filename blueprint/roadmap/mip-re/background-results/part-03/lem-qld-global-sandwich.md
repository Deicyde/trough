---
declaration: lemma
origin: cited
lean: MIPRE.QLD.sum_uniform_zBlk, MIPRE.QLD.sum_uniform_xBlk, MIPRE.QLD.sq_sub_two_mul_le_sq, MIPRE.QLD.one_sub_two_sqrt_le_sum_snorm_sq, MIPRE.QLD.marg_Z_ge, MIPRE.QLD.marg_X_ge, MIPRE.QLD.inconsistency_evalMarg_Z_le, MIPRE.QLD.inconsistency_evalMarg_X_le
statement: formalized
proof: formalized
---

# Sandwich estimates and the two marginals

Let $\Delta$ be the bound of Lemma [Ordered products with global outcome multipliers](lem-qld-global-products.md) and $\delta_G$ the weight of the outcomes that are not of the separated form. Then the evaluated $Z$ marginal of the completed pair measurement is consistent with Bob's expanded $(\mathtt{Point}, Z)$ measurement at a uniform $z \in \mathbb{F}_q^m$, with error at most $2\sqrt{\Delta} + 2/q + \delta_G$, and likewise the $X$ marginal with the $X$ measurement at a uniform $x$. The Lean proves it in any bipartite model in a unit state; the statement above is its tensor-product instance.

## Depends on

- [Completing the pair measurement projectively](lem-qld-global-complete.md)
- [Ordered products with global outcome multipliers](lem-qld-global-products.md)
- [Separating the two point variables](lem-qld-global-separate.md)
- [Cross-party state-dependent distance](../../foundations/part-02/def-cross-distance.md)

## Proof

Write $B_u(c)$ for the combination of the ordered products $\widehat M^X_a \widehat M^Z_b$ along $\alpha a + \beta b = c$. From $\sum_g \mathbb E_u \|(G_g \otimes ({I} - B_u(g(u))))\Phi\|^2 \leq \Delta$ and $\|(G_g \otimes {I})\Phi\| \leq \|(G_g \otimes B_u)\Phi\| + \|(G_g \otimes ({I} - B_u))\Phi\|$, one Cauchy–Schwarz over the pairs $(u, g)$ gives $\sum_g \mathbb E_u \|(G_g \otimes B_u(g(u)))\Phi\|^2 \geq 1 - 2\sqrt{\Delta}$. For a good outcome, the fibre analysis of Lemma [Separating the two point variables](lem-qld-global-separate.md) bounds the left-hand side above by $2/q \cdot \langle G_g \otimes {I} \rangle$ plus the diagonal weight $\mathbb E_{u_0} \langle G_g \otimes \widehat M^Z_{g_Z(z)}(z)\rangle$, and the outcomes that are not good contribute at most $\delta_G$ in total. The $z$ block of a uniform padded point is uniform, so what remains is exactly the $Z$ marginal, and rearranging gives the bound. The $X$ marginal is the same computation from the other product order. No complex intermediate appears: every quantity estimated here is a squared norm or a Born probability of a positive operator.

## Lean

Formalized as [`MIPRE.QLD.sum_uniform_zBlk`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_uniform_zBlk), [`MIPRE.QLD.sum_uniform_xBlk`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_uniform_xBlk), [`MIPRE.QLD.sq_sub_two_mul_le_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sq_sub_two_mul_le_sq), [`MIPRE.QLD.one_sub_two_sqrt_le_sum_snorm_sq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.one_sub_two_sqrt_le_sum_snorm_sq), [`MIPRE.QLD.marg_Z_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.marg_Z_ge), [`MIPRE.QLD.marg_X_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.marg_X_ge), [`MIPRE.QLD.inconsistency_evalMarg_Z_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.inconsistency_evalMarg_Z_le), [`MIPRE.QLD.inconsistency_evalMarg_X_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.inconsistency_evalMarg_X_le).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 4461](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L4461)

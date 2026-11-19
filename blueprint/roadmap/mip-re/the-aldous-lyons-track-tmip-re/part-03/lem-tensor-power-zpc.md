---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.slot, MIPRE.Tailored.isSignedPerm_slot, MIPRE.Tailored.isDiag_slot, MIPRE.Tailored.commute_slot_slot, MIPRE.Tailored.prod_slot_finRange, MIPRE.Tailored.PermStrategy.repeat, MIPRE.Tailored.PermStrategy.proj_repeat, MIPRE.Tailored.PermStrategy.proj_mul_eq_zero_of_value_eq_one, MIPRE.Tailored.PermStrategy.value_repeat_eq_one, MIPRE.Tailored.PermStrategy.comap, MIPRE.Tailored.PermStrategy.value_comap_eq_one, MIPRE.Tailored.TailoredGame.HasPerfectZPC.repeat_doubled
statement: formalized
proof: formalized
---

# Tensor powers of permutation strategies; II:3043

If a tailored game $\mathfrak{G}$ has a perfect Z-aligned permutation strategy commuting along edges, so does its $k$-fold product, and so does the doubled product when the doubled game has one.

## Depends on

- [The $k$-fold tailored product; II:11377, direct form](def-tailored-product.md)
- [The canonical decider of the product](lem-tailored-product-accepts.md)
- [Signed permutation matrices](../part-01/lem-signed-perm.md)
- [The Fourier transform; II:974–1006](../part-01/lem-fourier-pvm.md)
- [When a permutation strategy is perfect](../part-01/lem-perm-strategy-perfect.md)
- [Tensor powers of synchronous strategies](../../parallel-repetition/lem-tensor-power-pcc.md)

## Proof

The observable of the variable $(i, v)$ of $\bar{x}$ is $1 \otimes \ldots \otimes U(x_i, v) \otimes \ldots \otimes 1$, on the $k$-th tensor power of the space. A slot of a signed permutation is a signed permutation, of a diagonal matrix a diagonal matrix, and slots in two different factors commute, so the observables are involutive signed permutations, commuting at each question, diagonal at the readable variables, and commuting along the edges, which are edges in every coordinate. The factors of the Fourier transform at $\bar{x}$ commute; regrouped by coordinate they give the tensor product of the coordinates' measurements. In a perfect strategy a rejected pair of answers on an edge has $P^x_a P^y_b = 0$: its probability is zero, and $P^x_a P^y_b$, two commuting projections, is its own $X^* X$. A rejected pair of the product is rejected in some coordinate (Lemma [The canonical decider of the product](lem-tailored-product-accepts.md)), and a tensor product with a zero factor is zero, so the power is perfect (Lemma [When a permutation strategy is perfect](../part-01/lem-perm-strategy-perfect.md)). For the doubled product, the power of the strategy for the doubled game is read at $(t, \bar{x})$ on the questions $(t, x_1), \ldots, (t, x_k)$, a map of the questions that keeps the lengths, the edges and the constraints.

## Lean

Formalized as [`MIPRE.Tailored.slot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.slot), [`MIPRE.Tailored.isSignedPerm_slot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isSignedPerm_slot), [`MIPRE.Tailored.isDiag_slot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.isDiag_slot), [`MIPRE.Tailored.commute_slot_slot`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.commute_slot_slot), [`MIPRE.Tailored.prod_slot_finRange`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.prod_slot_finRange), [`MIPRE.Tailored.PermStrategy.repeat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.repeat), [`MIPRE.Tailored.PermStrategy.proj_repeat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.proj_repeat), [`MIPRE.Tailored.PermStrategy.proj_mul_eq_zero_of_value_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.proj_mul_eq_zero_of_value_eq_one), [`MIPRE.Tailored.PermStrategy.value_repeat_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.value_repeat_eq_one), [`MIPRE.Tailored.PermStrategy.comap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.comap), [`MIPRE.Tailored.PermStrategy.value_comap_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.value_comap_eq_one), [`MIPRE.Tailored.TailoredGame.HasPerfectZPC.repeat_doubled`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.HasPerfectZPC.repeat_doubled).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1162](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1162)

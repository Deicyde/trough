---
declaration: corollary
origin: cited
lean: MIPRE.LIDT.Co.Doubling.isSummedSdp_prod_iff, MIPRE.LIDT.Co.Doubling.isSummedSdp_map_iff_of_nonneg_iff, MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_loc, MIPRE.LIDT.Co.Doubling.isSummedSdp_L_iff, MIPRE.LIDT.Co.Doubling.isSummedSdp_R_iff, MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_model, MIPRE.LIDT.Co.Doubling.isSummedSdp_equivA_iff, MIPRE.LIDT.Co.Doubling.isSummedSdp_equivB_iff, MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_A, MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_B, MIPRE.LIDT.Co.Doubling.isSummedSdp_equiv_iff, MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_prod
statement: formalized
proof: formalized
---

# The summed semidefinite form in the doubled model

Let $M$ be a finite pair in a unit state, with doubled model $D(M)$ (Definition [The doubled model](../part-05/def-doubled-model.md)). For self-adjoint $A_1, \dots, A_m$ in its local algebra $\mathcal{P}$ there is a measurement $T$ in $\mathcal{P}$ such that $Z = \sum_i T_i A_i$ satisfies items 1–3 of Theorem [The summed semidefinite form, in a commutant with a vector trace](thm-summed-sdp.md) in $\mathcal{P}$, and so do the images of $A$, $T$ and $Z$ under each placement $L$ and $R$. When $\mathcal{A}$ and $\mathcal{B}$ are star-ordered, the summed form transfers in both directions between $\mathcal{A}$ and $\mathcal{A}_c$, between $\mathcal{B}$ and $\mathcal{B}_c$, and between $\mathcal{A} \times \mathcal{B}$ and $\mathcal{P}$. So the conclusion of Theorem [The summed semidefinite form, in a commutant with a vector trace](thm-summed-sdp.md) holds in $\mathcal{A}$, in $\mathcal{B}$ and in $\mathcal{A} \times \mathcal{B}$ themselves.

## Depends on

- [The summed semidefinite form, in a commutant with a vector trace](thm-summed-sdp.md)
- [The doubled model is a finite pair, with the order of its parts](lem-doubled-model-finite-pair.md)

## Proof

In a product with componentwise operations and order, the summed form holds exactly when it holds in each factor. Theorem [The summed semidefinite form, in a commutant with a vector trace](thm-summed-sdp.md) solves it in $\mathcal{A}_c$ and in $\mathcal{B}_c$, and the pair of solutions solves it in $\mathcal{P}$, with $Z = \sum_i T_i A_i$. A $*$-homomorphism between star-ordered rings that preserves and reflects nonnegativity is injective and an order embedding, so it carries the summed form both ways. This applies to $L$ and $R$ (Lemma [The doubled model is a finite pair, with the order of its parts](lem-doubled-model-finite-pair.md)) and to the isomorphisms of Lemma [The players' algebras of a finite pair, as commutants with their order](../part-05/lem-finite-pair-order.md) (`reports/c6b-paper-proofs.md`, Section 5, Corollary 12 and Lemma 13). Neither a trace on the doubled algebra nor its commutant is used.

## Lean

Formalized as [`MIPRE.LIDT.Co.Doubling.isSummedSdp_prod_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.isSummedSdp_prod_iff), [`MIPRE.LIDT.Co.Doubling.isSummedSdp_map_iff_of_nonneg_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.isSummedSdp_map_iff_of_nonneg_iff), [`MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_loc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_loc), [`MIPRE.LIDT.Co.Doubling.isSummedSdp_L_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.isSummedSdp_L_iff), [`MIPRE.LIDT.Co.Doubling.isSummedSdp_R_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.isSummedSdp_R_iff), [`MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_model`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_model), [`MIPRE.LIDT.Co.Doubling.isSummedSdp_equivA_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.isSummedSdp_equivA_iff), [`MIPRE.LIDT.Co.Doubling.isSummedSdp_equivB_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.isSummedSdp_equivB_iff), [`MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_A`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_A), [`MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_B`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_B), [`MIPRE.LIDT.Co.Doubling.isSummedSdp_equiv_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.isSummedSdp_equiv_iff), [`MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_prod`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.exists_isSummedSdp_prod).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3630](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3630)

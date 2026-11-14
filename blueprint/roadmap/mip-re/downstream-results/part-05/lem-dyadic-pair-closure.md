---
declaration: lemma
origin: cited
lean: MIPRE.BipartiteModel.IsDyadicPair.swap, MIPRE.BipartiteModel.IsDyadicPair.expand, MIPRE.BipartiteModel.IsDyadicPair.eq_zero_of_abelianA, MIPRE.BipartiteModel.IsDyadicPair.eq_zero_of_abelianB
statement: formalized
proof: formalized
---

# Dyadic pairs are closed under ancilla extensions

A dyadic pair with the players exchanged is a dyadic pair, and so is an ancilla extension of a dyadic pair (Definition [Ancilla extension of a bipartite model](../part-02/def-ancilla-extension.md)) with nonempty registers. Neither player's operators in a dyadic pair contain a nonzero abelian projection.

## Depends on

- [Dyadic pairs](def-dyadic-pair.md)
- [Finite pairs are closed under ancilla extensions](../part-04/lem-finite-pair-expand.md)
- [Transport of dyadic matrix units](lem-dyadic-units-closure.md)
- [Dyadic matrix units exclude abelian projections](thm-no-abelian-dyadic.md)

## Proof

Exchanging the players exchanges the two conditions. The players' algebras of an extension are the matrix algebras $M_\alpha({\mathscr{A}}_A)$ and $M_\beta({\mathscr{A}}_B)$ (Definition [Ancilla extension of a bipartite model](../part-02/def-ancilla-extension.md)), in which the scalar diagonals of the model's units are units (Lemma [Transport of dyadic matrix units](lem-dyadic-units-closure.md)), and the extension is a finite pair (Lemma [Finite pairs are closed under ancilla extensions](../part-04/lem-finite-pair-expand.md)). The last claim is Theorem [Dyadic matrix units exclude abelian projections](thm-no-abelian-dyadic.md) on each side. The full proof is `reports/c6b-paper-proofs.md`, Section 3, Theorem Cl (Lemma 7).

## Lean

Formalized as [`MIPRE.BipartiteModel.IsDyadicPair.swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsDyadicPair.swap), [`MIPRE.BipartiteModel.IsDyadicPair.expand`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsDyadicPair.expand), [`MIPRE.BipartiteModel.IsDyadicPair.eq_zero_of_abelianA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsDyadicPair.eq_zero_of_abelianA), [`MIPRE.BipartiteModel.IsDyadicPair.eq_zero_of_abelianB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsDyadicPair.eq_zero_of_abelianB).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2977](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2977)

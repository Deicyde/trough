---
declaration: lemma
origin: cited
lean: MIPRE.BipartiteModel.IsFinitePair.equivA, MIPRE.BipartiteModel.IsFinitePair.equivB, MIPRE.BipartiteModel.IsFinitePair.nonneg_iff_A, MIPRE.BipartiteModel.IsFinitePair.nonneg_iff_B, MIPRE.BipartiteModel.IsFinitePair.le_iff_A, MIPRE.BipartiteModel.IsFinitePair.le_iff_B, MIPRE.POVMIn.mapHom, MIPRE.isPVMIn_map_equiv_iff
statement: formalized
proof: formalized
---

# The players' algebras of a finite pair, as commutants with their order

Let $M$ be a finite pair (Definition [Finite pairs](../part-04/def-finite-pair.md)) with algebras $\mathcal{A}$ and $\mathcal{B}$ represented on $\mathcal{H}$, and let $\mathcal{A}_c$ and $\mathcal{B}_c$ be the commutants in $B(\mathcal{H})$ of the second and of the first player's operators. They are norm-closed $*$-subalgebras, hence C$^*$-algebras, and star-ordered by the operator order. The map $a \mapsto \pi(\pi_A(a))$ is a $*$-isomorphism of $\mathcal{A}$ onto $\mathcal{A}_c$, and $b \mapsto \pi(\pi_B(b))$ one of $\mathcal{B}$ onto $\mathcal{B}_c$. If $\mathcal{A}$ is a star-ordered ring, then $a \geq 0$ if and only if $\pi(\pi_A(a)) \geq 0$, and likewise for $\mathcal{B}$. So positive operator valued measurements transfer along these isomorphisms in both directions, and so do projective measurements.

## Depends on

- [Finite pairs](../part-04/def-finite-pair.md)
- [Finite pairs are closed under ancilla extensions](../part-04/lem-finite-pair-expand.md)

## Proof

The first player's operators commute with the second player's and with their adjoints, so they lie in $\mathcal{A}_c$. The commutant clause of a finite pair says that an operator commuting with the second player's operators is one of the first player's, so they are all of $\mathcal{A}_c$; and the representation is injective, so $a \mapsto \pi(\pi_A(a))$ is bijective onto $\mathcal{A}_c$. A commutant is norm closed, and it is star-ordered because a positive element of it is the square of its square root, which commutes with everything the element commutes with. A $*$-homomorphism between star-ordered rings is monotone, and both the isomorphism and its inverse are $*$-homomorphisms, so the two orders agree (`reports/c6b-paper-proofs.md`, Section 5.6, Lemma 13). The second player's statements are the first player's for the model with the players exchanged.

## Lean

Formalized as [`MIPRE.BipartiteModel.IsFinitePair.equivA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsFinitePair.equivA), [`MIPRE.BipartiteModel.IsFinitePair.equivB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsFinitePair.equivB), [`MIPRE.BipartiteModel.IsFinitePair.nonneg_iff_A`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsFinitePair.nonneg_iff_A), [`MIPRE.BipartiteModel.IsFinitePair.nonneg_iff_B`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsFinitePair.nonneg_iff_B), [`MIPRE.BipartiteModel.IsFinitePair.le_iff_A`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsFinitePair.le_iff_A), [`MIPRE.BipartiteModel.IsFinitePair.le_iff_B`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.IsFinitePair.le_iff_B), [`MIPRE.POVMIn.mapHom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.POVMIn.mapHom), [`MIPRE.isPVMIn_map_equiv_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.isPVMIn_map_equiv_iff).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3343](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3343)

---
declaration: lemma
origin: cited
lean: MIPRE.NoAbelianProj, MIPRE.noAbelianProj_diag2Set_iff, MIPRE.LIDT.Co.Doubling.noAbelianProj_iff, MIPRE.LIDT.Co.Doubling.noAbelianProj_opsA_of_isDyadicPair, MIPRE.LIDT.Co.Doubling.noAbelianProj_opsB_of_isDyadicPair
statement: formalized
proof: formalized
---

# No abelian projections in the doubled model

Let $M$ be a finite pair in a unit state. Both players' operators of the doubled model $D(M)$ (Definition [The doubled model](../part-05/def-doubled-model.md)) contain no nonzero abelian projection if and only if both players' operators of $M$ contain none. In particular this holds when $M$ is a dyadic pair. Here a projection $r$ of a set $s$ of operators is *abelian* when its corner $r s r$ is commutative, which is the hypothesis of Corollary [Orthonormalization in a finite pair without abelian projections](../part-05/cor-orthonormalization-finite-pair.md).

## Depends on

- [The doubled model](../part-05/def-doubled-model.md)

## Proof depends on

- [Dyadic pairs are closed under ancilla extensions](../part-05/lem-dyadic-pair-closure.md)

## Proof

The players' operators of $D(M)$ are the block-diagonal operators $u \oplus v$ with $u$ and $v$ in the players' operators of $M$ (Lemma [The doubled model is a finite pair, with the order of its parts](lem-doubled-model-finite-pair.md)). A projection $p \oplus q$ there is abelian exactly when $p$ and $q$ are, since its corner is the product of theirs. For a dyadic pair, neither player's operators contain a nonzero abelian projection (Lemma [Dyadic pairs are closed under ancilla extensions](../part-05/lem-dyadic-pair-closure.md)) (`reports/c6b-paper-proofs.md`, Section 4, Theorem F).

## Lean

Formalized as [`MIPRE.NoAbelianProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.NoAbelianProj), [`MIPRE.noAbelianProj_diag2Set_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.noAbelianProj_diag2Set_iff), [`MIPRE.LIDT.Co.Doubling.noAbelianProj_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.noAbelianProj_iff), [`MIPRE.LIDT.Co.Doubling.noAbelianProj_opsA_of_isDyadicPair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.noAbelianProj_opsA_of_isDyadicPair), [`MIPRE.LIDT.Co.Doubling.noAbelianProj_opsB_of_isDyadicPair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.noAbelianProj_opsB_of_isDyadicPair).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3476](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3476)

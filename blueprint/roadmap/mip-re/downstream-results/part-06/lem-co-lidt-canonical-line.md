---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.Bridge.soundness, MIPRE.LIDT.Co.Bridge.soundLidtIn_of_isDyadicPair
statement: formalized
proof: formalized
---

# The canonical-line theorem in a dyadic pair

Theorem [Quantum soundness of the canonical-line low individual degree test](../../background-results/part-01/thm-lidt-soundness.md) holds, for $d \geq 1$, for the projective strategies in every dyadic pair (Definition [Dyadic pairs](../part-05/def-dyadic-pair.md)), with the measurements $G^\textsc{A}$ and $G^\textsc{B}$ projective measurements in the two players' algebras and consistency measured by the inconsistency of the model.

## Depends on

- [The main theorem of the low individual degree test, in a dyadic pair](thm-co-main-formal.md)
- [Projective strategy in a bipartite model](../part-02/def-model-proj-strategy.md)
- [Canonical-line low individual degree test](../../background-results/part-01/def-lidt.md)

## Proof

The proof is the matrix one of Theorem [Quantum soundness of the canonical-line low individual degree test](../../background-results/part-01/thm-lidt-soundness.md), read in the model: the strategy is translated into the strategy container of the port, its failure surrogate is at most the rejection probability, Theorem [The main theorem of the low individual degree test, in a dyadic pair](thm-co-main-formal.md) applies, and its measurements and errors are read back into the vocabulary of the model.

## Lean

Formalized as [`MIPRE.LIDT.Co.Bridge.soundness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Bridge.soundness), [`MIPRE.LIDT.Co.Bridge.soundLidtIn_of_isDyadicPair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Bridge.soundLidtIn_of_isDyadicPair).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 4205](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L4205)

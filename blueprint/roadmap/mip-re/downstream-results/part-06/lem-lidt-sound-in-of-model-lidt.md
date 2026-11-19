---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.Chain.soundIn_of_soundLidtIn
statement: formalized
proof: formalized
---

# Soundness in a model from the canonical-line theorem in it

Let $M$ be a bipartite model whose players' algebras are star-ordered. If the conclusion of Theorem [Quantum soundness of the canonical-line low individual degree test](../../background-results/part-01/thm-lidt-soundness.md) holds for the projective strategies in $M$ whenever $d \geq 1$, with the measurements in the players' algebras, then the seeded CL test is sound in $M$ (Definition [The low-individual-degree test is sound in a model](../part-03/def-lidt-sound-in.md)).

## Depends on

- [The low-individual-degree test is sound in a model](../part-03/def-lidt-sound-in.md)

## Proof depends on

- [Embeddings](../part-04/lem-model-embedding.md)
- [Operations on projective strategies](../part-03/lem-model-proj-strategy.md)
- [The adapter's cost in the question distributions](../../background-results/part-01/lem-lidt-cl-adapter-weights.md)

## Proof

This is the route by which Lemma [The low-individual-degree test is sound in the tensor-product model](../part-03/lem-lidt-sound-in-tensor.md) reads Theorem [Quantum soundness of the seeded CL test](../../background-results/part-01/thm-lidt-cl-soundness.md) off Theorem [Quantum soundness of the canonical-line low individual degree test](../../background-results/part-01/thm-lidt-soundness.md), with the matrix Born rule replaced by the model's: the seeded strategy is reparametrized to a strategy for the canonical-line test with a single codeword, padded, and the tuple measurements are extracted from the measurements that the hypothesis provides, at the error $\delta_{\mathrm{CL}}$. When the padding is not possible the error is at least $1$, and constant measurements will do.

## Lean

Formalized as [`MIPRE.LIDT.Co.Chain.soundIn_of_soundLidtIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Chain.soundIn_of_soundLidtIn).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 4224](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L4224)

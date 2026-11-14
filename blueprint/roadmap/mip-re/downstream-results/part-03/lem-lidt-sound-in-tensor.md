---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Simul.soundIn_tensor, MIPRE.LIDT.Simul.tuplePOVMA_toTensor, MIPRE.LIDT.Simul.tuplePOVMB_toTensor, MIPRE.LIDT.Simul.evalTuplePOVM_toIn
statement: formalized
proof: formalized
---

# The low-individual-degree test is sound in the tensor-product model

The seeded CL test is sound in the tensor-product model of every state on $\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B}$.

## Depends on

- [The low-individual-degree test is sound in a model](def-lidt-sound-in.md)
- [Quantum soundness of the seeded CL test](../../background-results/part-01/thm-lidt-cl-soundness.md)
- [Projective strategies in the two models](lem-model-proj-strategy-values.md)

## Proof depends on

- [Operations on projective strategies](lem-model-proj-strategy.md)

## Proof

A projective strategy in that model is a tensor-product strategy (Lemma [Projective strategies in the two models](lem-model-proj-strategy-values.md)), to which Theorem [Quantum soundness of the seeded CL test](../../background-results/part-01/thm-lidt-cl-soundness.md) applies; its extracted measurements are projective measurements in the matrix algebras, and the matrix inconsistencies it bounds are the model's.

## Lean

Formalized as [`MIPRE.LIDT.Simul.soundIn_tensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.soundIn_tensor), [`MIPRE.LIDT.Simul.tuplePOVMA_toTensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.tuplePOVMA_toTensor), [`MIPRE.LIDT.Simul.tuplePOVMB_toTensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.tuplePOVMB_toTensor), [`MIPRE.LIDT.Simul.evalTuplePOVM_toIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.evalTuplePOVM_toIn).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1703](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1703)

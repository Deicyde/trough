---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.CL.Sample.swapTy, MIPRE.LIDT.CL.Sample.swapTyEquiv, MIPRE.LIDT.CL.subtests_swap, MIPRE.LIDT.CL.accepts_swap, MIPRE.LIDT.CL.clGame_μ_swap, MIPRE.LIDT.CL.clGame_D_swap, MIPRE.LIDT.Simul.tuplePOVMAIn_pushStrat, MIPRE.LIDT.Simul.tuplePOVMBIn_pushStrat, MIPRE.LIDT.Simul.evalTuplePOVMIn_symm_pushA, MIPRE.LIDT.Simul.evalTuplePOVMIn_symm_pushB, MIPRE.LIDT.Simul.SoundIn.of_iso, MIPRE.LIDT.Simul.SoundIn.iff_of_iso, MIPRE.LIDT.Simul.SoundIn.swap, MIPRE.LIDT.Simul.soundIn_tensor_fintype, MIPRE.LIDT.Simul.soundIn_expand_tensor, MIPRE.LIDT.Simul.soundIn_swap_expand, MIPRE.LIDT.Simul.soundIn_swap_expand_of_norm
statement: formalized
proof: formalized
---

# The seeded test, moved between models

The seeded CL test is symmetric in the players: its question distribution is invariant under the exchange of the two players' questions, exchanging the two sampled types being a bijection of the samples, and it accepts a pair of answers at a pair of questions exactly when it accepts the exchanged answers at the exchanged questions. Its soundness in a bipartite model (Definition [The low-individual-degree test is sound in a model](../part-03/def-lidt-sound-in.md)) passes along isomorphisms of models in both directions, and to the model with the players exchanged. Consequently it is sound in the tensor-product model of every state on $\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B}$, for all finite $d_A$ and $d_B$, and in every extension of a tensor-product model; and if it is sound in every extension of a model, or in every extension by a unit vector, then it is sound in the same extensions of the model with the players exchanged.

## Depends on

- [The low-individual-degree test is sound in a model](../part-03/def-lidt-sound-in.md)
- [Seeded CL low individual degree test](../../background-results/part-01/def-lidt-cl.md)
- [What an isomorphism carries over](lem-model-iso.md)
- [Isomorphisms between extensions](lem-extension-isos.md)
- [The low-individual-degree test is sound in the tensor-product model](../part-03/lem-lidt-sound-in-tensor.md)
- [The order of a matrix algebra over an ordered $*$-ring](../part-03/def-block-order.md)

## Proof

Every subtest is written in both orientations, and agreement is symmetric. Along an isomorphism a projective strategy is pushed forward with its value, the measurements extracted for its image are pulled back along the inverse, and the three inconsistencies are carried over (Lemma [What an isomorphism carries over](lem-model-iso.md)). In the exchanged model a projective strategy is one of the model for the game with the players exchanged, which is the seeded game itself, with the same value; the measurements extracted for it serve exchanged, with the first two inconsistencies exchanged and the third symmetric. Lemma [The low-individual-degree test is sound in the tensor-product model](../part-03/lem-lidt-sound-in-tensor.md) is the tensor-product case on numbered factors, and the others follow by numbering the factors and, for an extension, by the isomorphism with the tensor-product model of the expanded vector (Lemma [Isomorphisms between extensions](lem-extension-isos.md)); an extension of the exchanged model is the exchanged extension in the exchanged vector, read backwards.

## Lean

Formalized as [`MIPRE.LIDT.CL.Sample.swapTy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.Sample.swapTy), [`MIPRE.LIDT.CL.Sample.swapTyEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.Sample.swapTyEquiv), [`MIPRE.LIDT.CL.subtests_swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.subtests_swap), [`MIPRE.LIDT.CL.accepts_swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.accepts_swap), [`MIPRE.LIDT.CL.clGame_μ_swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.clGame_μ_swap), [`MIPRE.LIDT.CL.clGame_D_swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.CL.clGame_D_swap), [`MIPRE.LIDT.Simul.tuplePOVMAIn_pushStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.tuplePOVMAIn_pushStrat), [`MIPRE.LIDT.Simul.tuplePOVMBIn_pushStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.tuplePOVMBIn_pushStrat), [`MIPRE.LIDT.Simul.evalTuplePOVMIn_symm_pushA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.evalTuplePOVMIn_symm_pushA), [`MIPRE.LIDT.Simul.evalTuplePOVMIn_symm_pushB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.evalTuplePOVMIn_symm_pushB), [`MIPRE.LIDT.Simul.SoundIn.of_iso`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.SoundIn.of_iso), [`MIPRE.LIDT.Simul.SoundIn.iff_of_iso`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.SoundIn.iff_of_iso), [`MIPRE.LIDT.Simul.SoundIn.swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.SoundIn.swap), [`MIPRE.LIDT.Simul.soundIn_tensor_fintype`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.soundIn_tensor_fintype), [`MIPRE.LIDT.Simul.soundIn_expand_tensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.soundIn_expand_tensor), [`MIPRE.LIDT.Simul.soundIn_swap_expand`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.soundIn_swap_expand), [`MIPRE.LIDT.Simul.soundIn_swap_expand_of_norm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.soundIn_swap_expand_of_norm).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2450](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2450)

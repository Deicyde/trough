---
declaration: lemma
origin: cited
lean: MIPRE.QLD.soundIn_tensor, MIPRE.QLD.approxSoundIn_tensor, MIPRE.QLD.approxSoundIn_commuting, MIPRE.BipartiteModel.LocalIsometry.withStates
statement: formalized
proof: formalized
---

# The Pauli basis test is sound in the tensor-product model

The Pauli basis test is sound, with $\mathrm{val}^*$, in the tensor-product model of every state, and $\mathrm{val}^*$ is approached in models where the test is sound. If the test is sound in the commuting-operator model, then ${\omega^{\mathrm{co}}}$ is approached in models where it is sound. A local isometry from $M$ to $M'$ is also one from $M^{v}$ to $M'^{w}$, for all vectors $v$ and $w$: the states play no part in it.

## Depends on

- [The Pauli basis test is sound in a model](../part-03/def-qld-sound-in.md)
- [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md)
- [Domination and approximation in the two models](../part-03/lem-povm-domination.md)
- [Projective strategies in the two models](../part-03/lem-model-proj-strategy-values.md)
- [Local isometries of bipartite models](../part-03/def-local-isometry.md)

## Proof depends on

- [Isomorphisms between extensions](lem-extension-isos.md)
- [The seeded test, moved between models](lem-lidt-model-transport.md)
- [Reductions](../part-03/lem-povm-reduction.md)
- [What an isomorphism carries over](lem-model-iso.md)

## Proof

This is Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md) at the tensor-product model of $\psi$, with $\omega = \mathrm{val}^*$. An extension of that model by registers in a unit vector $e$ is, by an isomorphism of models, the tensor-product model of the expanded vector $e \otimes \psi$ (Lemma [Isomorphisms between extensions](lem-extension-isos.md)), in which the seeded test is sound (Lemma [The seeded test, moved between models](lem-lidt-model-transport.md)): that is the first hypothesis. For the second, the same isomorphism, with the state of the extension replaced by a unit vector $v$ and that of the tensor-product model by the image of $v$, is a local isometry whose homomorphisms are unital and which carries the state to the state, so the extension in the state $v$ reduces to the tensor-product model of a unit vector (Lemma [Reductions](../part-03/lem-povm-reduction.md)), whose POVM strategies $\mathrm{val}^*$ dominates (Lemma [Domination and approximation in the two models](../part-03/lem-povm-domination.md)). For the approximations, a tensor-product strategy of value near $\mathrm{val}^*$ is a projective strategy of its own tensor-product model, of the same value, and the commuting-operator strategies play that part for ${\omega^{\mathrm{co}}}$ (Lemma [Projective strategies in the two models](../part-03/lem-model-proj-strategy-values.md)).

## Lean

Formalized as [`MIPRE.QLD.soundIn_tensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.soundIn_tensor), [`MIPRE.QLD.approxSoundIn_tensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.approxSoundIn_tensor), [`MIPRE.QLD.approxSoundIn_commuting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.approxSoundIn_commuting), [`MIPRE.BipartiteModel.LocalIsometry.withStates`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.withStates).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2093](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2093)

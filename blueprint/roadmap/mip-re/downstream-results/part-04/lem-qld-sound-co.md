---
declaration: lemma
origin: cited
lean: MIPRE.QLD.soundCo_of_lidt
statement: formalized
proof: formalized
---

# The Pauli basis test is sound in the commuting-operator model, given the seeded test

If the seeded CL test is sound in the commuting-operator model (Definition [The low-individual-degree test is sound in a model](../part-03/def-lidt-sound-in.md)), then the Pauli basis test is sound in the commuting-operator model (Definition [The Pauli basis test is sound in a model](../part-03/def-qld-sound-in.md)): in the model of every commuting-operator strategy, with ${\omega^{\mathrm{co}}}$, at the error of Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md).

## Depends on

- [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md)
- [The Pauli basis test is sound in a model](../part-03/def-qld-sound-in.md)
- [The seeded test in the extensions of a commuting-operator model](lem-lidt-sound-co-expand.md)
- [Domination and approximation in the two models](../part-03/lem-povm-domination.md)

## Proof

Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md) in the model of a commuting-operator strategy, with $\omega = {\omega^{\mathrm{co}}}$. Its first hypothesis, the soundness of the seeded test in every extension of that model by a unit vector, is Lemma [The seeded test in the extensions of a commuting-operator model](lem-lidt-sound-co-expand.md). Its second, that ${\omega^{\mathrm{co}}}$ dominates the POVM strategies of every such extension in every unit state, holds because ${\omega^{\mathrm{co}}}$ dominates the POVM strategies of every model on a Hilbert space with a unit state (Lemma [Domination and approximation in the two models](../part-03/lem-povm-domination.md)).

## Lean

Formalized as [`MIPRE.QLD.soundCo_of_lidt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.soundCo_of_lidt).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2727](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2727)

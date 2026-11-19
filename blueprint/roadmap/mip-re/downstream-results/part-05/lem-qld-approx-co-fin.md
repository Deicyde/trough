---
declaration: lemma
origin: cited
lean: MIPRE.QLD.approxSoundIn_commuting_of_fin
statement: formalized
proof: formalized
---

# The Pauli basis test, given the seeded test in dyadic pairs

If ${\omega^{\mathrm{co}}}$ is approached in dyadic pairs (Definition [Dyadic pairs](def-dyadic-pair.md), Lemma [${\omega^{\mathrm{co}}}$ is approached in dyadic pairs](lem-co-value-finite-pair.md)) and the seeded CL test is sound in dyadic pairs (Definition [The low-individual-degree test is sound in dyadic pairs](def-lidt-sound-fin.md)), then ${\omega^{\mathrm{co}}}$ is approached by projective strategies of models in which the Pauli basis test is sound with ${\omega^{\mathrm{co}}}$ (Definition [The Pauli basis test is sound in a model](../part-03/def-qld-sound-in.md)).

## Depends on

- [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md)
- [The Pauli basis test is sound in a model](../part-03/def-qld-sound-in.md)
- [The low-individual-degree test is sound in dyadic pairs](def-lidt-sound-fin.md)
- [Dyadic pairs are closed under ancilla extensions](lem-dyadic-pair-closure.md)
- [Domination and approximation in the two models](../part-03/lem-povm-domination.md)

## Proof

Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md) applies in each dyadic pair approaching ${\omega^{\mathrm{co}}}$, with $\omega = {\omega^{\mathrm{co}}}$. Its first hypothesis holds because an extension of a dyadic pair by a unit vector has nonempty registers and so is a dyadic pair (Lemma [Dyadic pairs are closed under ancilla extensions](lem-dyadic-pair-closure.md)), in which the seeded test is sound. Its second holds because ${\omega^{\mathrm{co}}}$ dominates the POVM strategies of every model on a Hilbert space in a unit state (Lemma [Domination and approximation in the two models](../part-03/lem-povm-domination.md)).

## Lean

Formalized as [`MIPRE.QLD.approxSoundIn_commuting_of_fin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.approxSoundIn_commuting_of_fin).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3136](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3136)

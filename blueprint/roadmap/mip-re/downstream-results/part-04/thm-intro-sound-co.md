---
declaration: theorem
origin: cited
lean: MIPRE.Introspection.seven_soundIn, MIPRE.Introspection.seven_soundIn_commuting
statement: formalized
proof: formalized
---

# Introspection is sound in ${\omega^{\mathrm{co}}}$, given the Pauli basis test

The introspection of Lemma [Supplying ambient introspection](../../structure-of-the-proof/part-06/lem-introspection-supply.md) is sound (Definition [The stages' soundness clauses in a value model](../part-01/def-stage-sound-in.md)) in every value model approached in models where the Pauli basis test is sound and approached by projective strategies, at the constants $a$, $b$ of its soundness clause in $\mathrm{val}^*$. In particular, if the Pauli basis test is sound in the commuting-operator model, introspection is sound in ${\omega^{\mathrm{co}}}$; and the test is sound there as soon as the seeded low-individual-degree test is (Lemma [The Pauli basis test is sound in the commuting-operator model, given the seeded test](lem-qld-sound-co.md)).

## Depends on

- [Supplying ambient introspection](../../structure-of-the-proof/part-06/lem-introspection-supply.md)
- [The Pauli basis test is sound in a model](../part-03/def-qld-sound-in.md)
- [The Pauli basis test is sound in the tensor-product model](lem-qld-sound-in-tensor.md)
- [Domination and approximation in the two models](../part-03/lem-povm-domination.md)
- [The stages' soundness clauses in a value model](../part-01/def-stage-sound-in.md)

## Proof

Let the value of the output verifier exceed $1 - \varepsilon$, with $\varepsilon < 1$; otherwise the loss is at least $1$. The output rejects answers beyond its cutoff and agrees with the reference verifier, so the value of the reference game at the cutoff exceeds $1 - \varepsilon$, and a projective strategy of value above $1 - \varepsilon$ for it exists in a model where the Pauli basis test is sound. Restricted to the typed raw game, decoded to the canonical game and restricted to the Pauli block, it stays in that model, where the test supplies the extraction; the analysis of Lemma [Finite soundness from the valid-answer extraction interface](../../structure-of-the-proof/part-05/lem-intro-valid-isometric-soundness.md), stated for a strategy in any model, then bounds the value of the padded source game in every value model dominating the ancilla model, and removing the padding, which needs the approximation by projective strategies, bounds the source verifier's value. The constants are those of the clause in $\mathrm{val}^*$, which is the case of $\mathrm{val}^*$ (Lemma [The Pauli basis test is sound in the tensor-product model](lem-qld-sound-in-tensor.md) and Lemma [Domination and approximation in the two models](../part-03/lem-povm-domination.md)).

## Lean

Formalized as [`MIPRE.Introspection.seven_soundIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.seven_soundIn), [`MIPRE.Introspection.seven_soundIn_commuting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.seven_soundIn_commuting).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2124](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2124)

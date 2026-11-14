---
declaration: theorem
origin: cited
lean: MIPRE.ValueModel.tensor_oracularSound, MIPRE.ValueModel.commuting_oracularSound, MIPRE.ValueModel.OracularSound.typedGame_ge_ambient, MIPRE.SeededGame.val_typedGame_le, MIPRE.Verifier.val_ge_of_typed, MIPRE.Oracularization.typed_soundness_val, MIPRE.Oracularization.detyped_soundness_val
statement: formalized
proof: formalized
---

# Oracularization is sound in both models

Oracularization is sound in the models $\mathrm{val}^*$ and ${\omega^{\mathrm{co}}}$ (Definition [Oracularization is sound in a value model](def-oracular-sound-in.md)). In every value model $\omega$ in which it is sound, the two soundness clauses of Theorem [Oracularization](../../structure-of-the-proof/part-06/thm-oracularization.md) hold with $\mathrm{val}^*$ replaced by $\omega$: if $\omega$ of the typed oracularized game of $\mathsf{V}_n$ exceeds $1 - \varepsilon$, then $\omega(\mathsf{V}_n) \geq 1 - 24\sqrt\varepsilon$ at the parse cut, and if $\omega$ of the detyped oracularized verifier at index $n$ exceeds $1 - \varepsilon$ at the outer cut, then $\omega(\mathsf{V}_n) \geq 1 - 1536\sqrt\varepsilon$.

## Depends on

- [Oracularization is sound in a value model](def-oracular-sound-in.md)
- [Oracularization](../../structure-of-the-proof/part-06/thm-oracularization.md)
- [Soundness of oracularization, for bipartite strategies](../../structure-of-the-proof/part-06/lem-oracular-soundness-tensor.md)
- [Soundness of oracularization, in ${\omega^{\mathrm{co}}}$](lem-oracular-soundness-co.md)
- [Post-processing and detyping, in a model](lem-transports-model.md)
- [Value transfers of the typed oracularized game](../../structure-of-the-proof/part-06/lem-oracular-typed-transfers.md)
- [Strategy transfer for the executable detyping verifier](../../structure-of-the-proof/part-01/lem-detype-program-strategies.md)

## Proof

In $\mathrm{val}^*$ the three properties are Lemma [Soundness of oracularization, for bipartite strategies](../../structure-of-the-proof/part-06/lem-oracular-soundness-tensor.md) and the value forms of Lemma [Post-processing and detyping, in a model](lem-transports-model.md); in ${\omega^{\mathrm{co}}}$ they are Lemma [Soundness of oracularization, in ${\omega^{\mathrm{co}}}$](lem-oracular-soundness-co.md) and the same value forms. The two clauses are then the proofs of Lemma [Value transfers of the typed oracularized game](../../structure-of-the-proof/part-06/lem-oracular-typed-transfers.md) and of Theorem [Oracularization](../../structure-of-the-proof/part-06/thm-oracularization.md), read in $\omega$: the typed game's value is at most the oracularization's, by the monotonicity and the equality of the two distributions; the game-level soundness bounds the input verifier; and the detyped verifier's game is the finite detyped game up to the numbering of its coordinates (Lemma [Strategy transfer for the executable detyping verifier](../../structure-of-the-proof/part-01/lem-detype-program-strategies.md)), on which the detyping restriction gives the typed game at least $1 - 16^3\varepsilon$. The tensor-product clauses of Theorem [Oracularization](../../structure-of-the-proof/part-06/thm-oracularization.md) are the case $\omega = \mathrm{val}^*$.

## Lean

Formalized as [`MIPRE.ValueModel.tensor_oracularSound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.tensor_oracularSound), [`MIPRE.ValueModel.commuting_oracularSound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.commuting_oracularSound), [`MIPRE.ValueModel.OracularSound.typedGame_ge_ambient`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.OracularSound.typedGame_ge_ambient), [`MIPRE.SeededGame.val_typedGame_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.val_typedGame_le), [`MIPRE.Verifier.val_ge_of_typed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.val_ge_of_typed), [`MIPRE.Oracularization.typed_soundness_val`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Oracularization.typed_soundness_val), [`MIPRE.Oracularization.detyped_soundness_val`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Oracularization.detyped_soundness_val).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1551](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1551)

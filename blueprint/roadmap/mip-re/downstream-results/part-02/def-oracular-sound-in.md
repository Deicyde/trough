---
declaration: definition
origin: cited
lean: MIPRE.ValueModel.OracularSound
statement: formalized
---

# Oracularization is sound in a value model

Oracularization is *sound in the value model $\omega$* if $\omega$ has three properties of $\mathrm{val}^*$ that the value transfers of Theorem [Oracularization](../../structure-of-the-proof/part-06/thm-oracularization.md) use: the monotonicity of item 1 of Lemma [Post-processing and detyping, in a model](lem-transports-model.md); the game-level soundness of oracularization, that $\omega$ of the oracularization of a seeded game above $1 - \varepsilon$ puts $\omega$ of its game at least $1 - 24\sqrt\varepsilon$; and the detyping restriction of item 2 of Lemma [Post-processing and detyping, in a model](lem-transports-model.md), between the values of the typed and the detyped finite games.

## Depends on

- [Value models](../part-01/def-value-model.md)
- [The oracularized game](../../structure-of-the-proof/part-06/def-oracular-game.md)
- [Finite-game detyping soundness](../../structure-of-the-proof/part-02/lem-detype-game-soundness.md)

## Lean

Formalized as [`MIPRE.ValueModel.OracularSound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueModel.OracularSound).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1538](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1538)

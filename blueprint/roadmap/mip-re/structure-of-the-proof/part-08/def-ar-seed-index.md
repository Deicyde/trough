---
declaration: definition
origin: cited
lean: MIPRE.SeededGame.typedSeedEquiv, MIPRE.AnswerReduction.one_sub_povmValue_typed
statement: formalized
---

# Full-seed indexing for answer reduction

The common index $\xi$ is the full uniform oracle seed. Both questions $(x_A,x_B)$ and every auxiliary oracle coordinate are functions of $\xi$. Indexed measurements and all subsequent averages retain $\xi$. The image pair $(x_A,x_B)$ is not substituted as an index without proving injectivity or specifying its conditional seed distribution. In the Lean the typed seed is an ordered pair of roles with one common uniform seed (`SeededGame.typedSeedEquiv`), and every average in the soundness proof is a sum over that seed (`one_sub_povmValue_typed`).

## Depends on

- [Finite-game detyping soundness](../part-02/lem-detype-game-soundness.md)
- [The typed oracularized game](../part-06/def-oracular-typed-game.md)

## Lean

Formalized as [`MIPRE.SeededGame.typedSeedEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.typedSeedEquiv), [`MIPRE.AnswerReduction.one_sub_povmValue_typed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.one_sub_povmValue_typed).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5739](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5739)

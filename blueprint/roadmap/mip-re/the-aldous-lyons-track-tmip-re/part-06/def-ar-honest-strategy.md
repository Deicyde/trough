---
declaration: definition
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.arGraph, MIPRE.Tailored.AnsRed.Typed.arDt, MIPRE.Tailored.AnsRed.Typed.ArSampler, MIPRE.Tailored.AnsRed.Typed.arGame, MIPRE.Tailored.AnsRed.Typed.auxGame, MIPRE.Tailored.AnsRed.Typed.pullStrat, MIPRE.Tailored.AnsRed.Typed.inSync, MIPRE.Tailored.AnsRed.Typed.orStrat, MIPRE.Tailored.AnsRed.Typed.arStrat, MIPRE.Tailored.AnsRed.Typed.arCl, MIPRE.Tailored.AnsRed.Typed.arSampler_arCl
statement: formalized
---

# The honest strategy of the answer-reduced game

An answer-reduced sampler is a family of CL functions on the typed questions whose questions carry the oracularized input question of the seed's input part, in the type's role, and the question of the seeded low-degree test of the seed's low-degree part. One is the direct sum of the oracularized input sampler and the seeded test's presentation, downsized along the Shoup basis. The answer-reduced typed game samples a pair of types and a seed and accepts by the typed data. Its honest strategy is the oracularization of the input's synchronous strategy, pulled back to the typed questions along their roles and oracularized parts and pushed forward along the honest answers.

## Depends on

- [The honest answers](def-ar-honest-answers.md)
- [Completeness of oracularization, at the level of games](../../structure-of-the-proof/part-06/lem-oracular-completeness.md)
- [ZPC strategies are PCC strategies](../part-01/lem-zpc-pcc.md)
- [Finite-game detyping soundness](../../structure-of-the-proof/part-02/lem-detype-game-soundness.md)
- [The typed answer-reduced game](../../structure-of-the-proof/part-08/def-ar-typed-game.md)

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.arGraph`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.arGraph), [`MIPRE.Tailored.AnsRed.Typed.arDt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.arDt), [`MIPRE.Tailored.AnsRed.Typed.ArSampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ArSampler), [`MIPRE.Tailored.AnsRed.Typed.arGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.arGame), [`MIPRE.Tailored.AnsRed.Typed.auxGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.auxGame), [`MIPRE.Tailored.AnsRed.Typed.pullStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.pullStrat), [`MIPRE.Tailored.AnsRed.Typed.inSync`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.inSync), [`MIPRE.Tailored.AnsRed.Typed.orStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.orStrat), [`MIPRE.Tailored.AnsRed.Typed.arStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.arStrat), [`MIPRE.Tailored.AnsRed.Typed.arCl`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.arCl), [`MIPRE.Tailored.AnsRed.Typed.arSampler_arCl`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.arSampler_arCl).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3066](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3066)

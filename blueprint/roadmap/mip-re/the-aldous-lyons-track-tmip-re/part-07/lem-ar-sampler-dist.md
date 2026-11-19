---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.LdRoutine.arSampler_dist, MIPRE.Tailored.AnsRed.Typed.dist_arPresented
statement: formalized
proof: formalized
---

# The distribution of the answer-reduced sampler

Along the numbering of the detyped coordinates, the answer-reduced sampler's question distribution at $n$ is the detyped game's, and so the presented answer-reduced game's weights.

## Depends on

- [The answer-reduced sampler](def-ar-sampler.md)
- [The presented answer-reduced game, and meeting it](def-ar-meets.md)
- [Strategy transfer for the executable detyping verifier](../../structure-of-the-proof/part-01/lem-detype-program-strategies.md)
- [Finite-game detyping soundness](../../structure-of-the-proof/part-02/lem-detype-game-soundness.md)

## Proof

The numbered detyped sampler's distribution is the detyped CL distribution (Lemma [Strategy transfer for the executable detyping verifier](../../structure-of-the-proof/part-01/lem-detype-program-strategies.md)), which is the detyped game's weights (Lemma [Finite-game detyping soundness](../../structure-of-the-proof/part-02/lem-detype-game-soundness.md)); the presentation keeps the weights.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.LdRoutine.arSampler_dist`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.LdRoutine.arSampler_dist), [`MIPRE.Tailored.AnsRed.Typed.dist_arPresented`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.dist_arPresented).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3603](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3603)

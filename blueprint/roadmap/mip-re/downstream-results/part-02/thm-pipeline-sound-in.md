---
declaration: theorem
origin: cited
lean: MIPRE.GapCompression.ofPipeline_sound
statement: formalized
proof: formalized
---

# Compression is sound in every model in which its stages are

If introspection, answer reduction and parallel repetition are sound in the value model $\omega$, the gap compression that Theorem [Gap-preserving compression from ambient stage contracts](../../structure-of-the-proof/part-09/thm-compression.md) builds from them is sound in $\omega$ (Definition [Soundness of compression in a value model](../part-01/def-compression-co-sound.md)).

## Depends on

- [The soundness chain of compression, in a value model](../part-01/lem-compress-sound-in.md)
- [Soundness of compression in a value model](../part-01/def-compression-co-sound.md)
- [Gap-preserving compression from ambient stage contracts](../../structure-of-the-proof/part-09/thm-compression.md)

## Proof

The compressed verifier is within its budget, so its value at the answer bound of Definition [Soundness of compression in a value model](../part-01/def-compression-co-sound.md) is its value at the bound of Lemma [The soundness chain of compression, in a value model](../part-01/lem-compress-sound-in.md), which that lemma bounds.

## Lean

Formalized as [`MIPRE.GapCompression.ofPipeline_sound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.GapCompression.ofPipeline_sound).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 885](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L885)

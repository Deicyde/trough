---
declaration: theorem
origin: cited
lean: MIPRE.gapCompression
statement: formalized
proof: formalized
---

# Ambient compression inhabitation target

The type `MIPRE.GapCompression` is inhabited.

## Depends on

- [Supplying ambient introspection](../part-06/lem-introspection-supply.md)
- [Supplying ambient answer reduction](lem-answer-reduction-supply.md)
- [Gap-preserving compression from ambient stage contracts](thm-compression.md)
- [Answer reduction](thm-answer-reduction.md)

## Proof depends on

- [Compression, and $\mathrm{MIP}^* = \mathrm{RE}$, from answer reduction alone](cor-compression-from-answer-reduction.md)

## Proof

Corollary [Compression, and $\mathrm{MIP}^* = \mathrm{RE}$, from answer reduction alone](cor-compression-from-answer-reduction.md) at the answer reduction of Lemma [Supplying ambient answer reduction](lem-answer-reduction-supply.md): Theorem [Gap-preserving compression from ambient stage contracts](thm-compression.md) applied to the three supplied stages.

## Lean

Formalized as [`MIPRE.gapCompression`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.gapCompression).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 6388](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L6388)

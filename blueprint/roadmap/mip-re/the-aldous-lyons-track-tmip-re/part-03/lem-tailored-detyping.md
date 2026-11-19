---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.accepts_eq_edgeOf, MIPRE.Tailored.TypedData.typeOf_of_edgeOf, MIPRE.Tailored.TypedData.detype_len_of_edgeOf, MIPRE.Tailored.TypedData.detype_accepts_iff_of_edgeOf, MIPRE.Tailored.TypedData.detype_accepts_of_edgeOf_none, MIPRE.Tailored.TypedData.decD_of_edgeOf, MIPRE.Tailored.TypedData.encD_of_edgeOf, MIPRE.Tailored.TypedData.detype_accepts_dec, MIPRE.Tailored.TypedData.detype_accepts_enc
statement: formalized
proof: formalized
---

# Detyping tailored games

On the views of an edge the detyped tailored game accepts exactly what the typed data accepts, and off the edges it accepts every pair of the right lengths. Consequently, for a detyped game whose predicate calls a typed predicate $D$ on the edges and accepts off them: if, on every edge, a pair the typed data accepts decodes to one $D$ accepts, then every pair the detyped tailored game accepts decodes to one the detyped predicate accepts; and if, on every edge, a pair of encodable answers $D$ accepts encodes to one the typed data accepts, with the typed lengths, then every accepted pair of encodable detyped answers encodes to one the detyped tailored game accepts.

## Depends on

- [Detyping a tailored game](def-tailored-detyping.md)
- [Finite-game detyping PCC completeness](../../structure-of-the-proof/part-01/lem-detype-game-completeness.md)

## Proof

A view of an edge decodes to the edge's type, so the lengths and constraints are the typed ones there; off the edges there is no constraint. The two reductions follow case by case on whether the pair of questions is the pair of views of an edge.

## Lean

Formalized as [`MIPRE.Tailored.accepts_eq_edgeOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.accepts_eq_edgeOf), [`MIPRE.Tailored.TypedData.typeOf_of_edgeOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TypedData.typeOf_of_edgeOf), [`MIPRE.Tailored.TypedData.detype_len_of_edgeOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TypedData.detype_len_of_edgeOf), [`MIPRE.Tailored.TypedData.detype_accepts_iff_of_edgeOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TypedData.detype_accepts_iff_of_edgeOf), [`MIPRE.Tailored.TypedData.detype_accepts_of_edgeOf_none`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TypedData.detype_accepts_of_edgeOf_none), [`MIPRE.Tailored.TypedData.decD_of_edgeOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TypedData.decD_of_edgeOf), [`MIPRE.Tailored.TypedData.encD_of_edgeOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TypedData.encD_of_edgeOf), [`MIPRE.Tailored.TypedData.detype_accepts_dec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TypedData.detype_accepts_dec), [`MIPRE.Tailored.TypedData.detype_accepts_enc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TypedData.detype_accepts_enc).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1527](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1527)

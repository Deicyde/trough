---
declaration: definition
origin: cited
lean: MIPRE.Tailored.typeOf, MIPRE.Tailored.edgeOf, MIPRE.Tailored.TypedData, MIPRE.Tailored.TypedData.Accepts, MIPRE.Tailored.TypedData.detype, MIPRE.Tailored.TypedData.decD, MIPRE.Tailored.TypedData.encD
statement: formalized
---

# Detyping a tailored game

*Typed tailored data* on a finite set of types $T$ fixes, for each type, the numbers of readable and of linear answer bits, and, for each pair of typed questions, a list of controlled linear constraints. Its *detyping* is the tailored game on the detyped questions (a graph view followed by a content register, Lemma [Graph rejection sampling](../../structure-of-the-proof/part-01/lem-detype-graph.md)) in which a question has the lengths of the type its graph view decodes to, for either player, and none when it decodes to none; and a pair of questions has the typed constraints when the two views are Alice's and Bob's views of an edge, and no constraint otherwise. Answers are decoded and encoded through the type of their question.

## Depends on

- [Tailored game; II:1243](../part-01/def-tailored-game.md)

## Lean

Formalized as [`MIPRE.Tailored.typeOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.typeOf), [`MIPRE.Tailored.edgeOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.edgeOf), [`MIPRE.Tailored.TypedData`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TypedData), [`MIPRE.Tailored.TypedData.Accepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TypedData.Accepts), [`MIPRE.Tailored.TypedData.detype`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TypedData.detype), [`MIPRE.Tailored.TypedData.decD`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TypedData.decD), [`MIPRE.Tailored.TypedData.encD`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TypedData.encD).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1510](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1510)

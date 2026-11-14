---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.decodeQuestion_eq_some, MIPRE.Tailored.decodeQuestion_eq_none, MIPRE.Tailored.hasPerfectZPC_presented_typed
statement: formalized
proof: formalized
---

# Completeness of a presentation from a typed strategy

In Lemma [Presenting a detyped game by a detyped tailored game](lem-presentation.md), take for the detyped game's perfect PCC strategy the one the finite detyping builds from a typed perfect PCC strategy. Its hypotheses then become typed: the typed strategy charges only encodable answers, and its bit observables along the encoding are signed permutations, diagonal at the readable bits.

## Depends on

- [Presenting a detyped game by a detyped tailored game](lem-presentation.md)

## Proof

At a view decoding to a typed question the detyped measurement is the typed one there; at the other views the detyped tailored game has no answer bits, and the measurement is concentrated on a fixed answer.

## Lean

Formalized as [`MIPRE.Tailored.decodeQuestion_eq_some`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.decodeQuestion_eq_some), [`MIPRE.Tailored.decodeQuestion_eq_none`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.decodeQuestion_eq_none), [`MIPRE.Tailored.hasPerfectZPC_presented_typed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.hasPerfectZPC_presented_typed).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1874](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1874)

---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.Typed.prefixOK, MIPRE.Tailored.Intro.Typed.G, MIPRE.Tailored.Intro.Typed.pauliDir, MIPRE.Tailored.Intro.Typed.pauliAux, MIPRE.Tailored.Intro.Typed.consRaw, MIPRE.Tailored.Intro.Typed.consL, MIPRE.Tailored.Intro.Typed.lenR_le_len, MIPRE.Tailored.Intro.Typed.lenR, MIPRE.Tailored.Intro.Typed.len, MIPRE.Tailored.Intro.Typed.parsedT, MIPRE.Tailored.Intro.Typed.readOK, MIPRE.Tailored.Intro.Typed.pauliAux_iff, MIPRE.Tailored.Intro.Typed.AcceptsAsInput, MIPRE.Tailored.Intro.Typed.hD_of_acceptsAsInput, MIPRE.Tailored.Intro.Typed.consL_iff
statement: formalized
proof: formalized
---

# The typed tailored data of the introspection verifier

Let the normal form verifier $V$ accept at index $2^n$ as the tailored verifier $T$ does. At every ordered pair of labels of the introspection verifier there is a list of constraints on the two answers of the labels' lengths, from the question payloads and the readable answers: the Pauli basis test at two Pauli labels; Lemma [The auxiliary checks as linear constraints](lem-intro-aux-cons.md) at two auxiliary labels, with the input's split and constraints those of $T$ at the source questions; and at a Pauli label and an auxiliary one, the readable condition, the comparison of a $Z$-basis answer with the sampled register, and Lemma [The first hiding edge as linear constraints](lem-intro-pauli-hide.md). The constraints hold exactly when the readable conditions hold at both answers — the input's answer fits, the prefix condition at Read and Hide, the source output at Introspect — and the kernel's semantic check accepts the two parsed answers.

## Depends on

- [The auxiliary checks as linear constraints](lem-intro-aux-cons.md)
- [The first hiding edge as linear constraints](lem-intro-pauli-hide.md)
- [The Pauli basis test as linear constraints](lem-intro-pauli-cons.md)
- [The input's question at an auxiliary answer, and the Pauli labels](def-intro-source.md)

## Proof

Label pair by label pair: the semantic check is the format of the parsed answers (automatic), their equality at equal labels, the Pauli basis test at two Pauli labels and the directed checks in both orders, each of which is one of the families.

## Lean

Formalized as [`MIPRE.Tailored.Intro.Typed.prefixOK`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.prefixOK), [`MIPRE.Tailored.Intro.Typed.G`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.G), [`MIPRE.Tailored.Intro.Typed.pauliDir`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.pauliDir), [`MIPRE.Tailored.Intro.Typed.pauliAux`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.pauliAux), [`MIPRE.Tailored.Intro.Typed.consRaw`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.consRaw), [`MIPRE.Tailored.Intro.Typed.consL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.consL), [`MIPRE.Tailored.Intro.Typed.lenR_le_len`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.lenR_le_len), [`MIPRE.Tailored.Intro.Typed.lenR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.lenR), [`MIPRE.Tailored.Intro.Typed.len`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.len), [`MIPRE.Tailored.Intro.Typed.parsedT`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.parsedT), [`MIPRE.Tailored.Intro.Typed.readOK`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.readOK), [`MIPRE.Tailored.Intro.Typed.pauliAux_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.pauliAux_iff), [`MIPRE.Tailored.Intro.Typed.AcceptsAsInput`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.AcceptsAsInput), [`MIPRE.Tailored.Intro.Typed.hD_of_acceptsAsInput`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.hD_of_acceptsAsInput), [`MIPRE.Tailored.Intro.Typed.consL_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Typed.consL_iff).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1843](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1843)

---
declaration: definition
origin: cited
lean: Turing.Code, Turing.Code.toTM, Turing.encodeCode, Turing.decodeCode, Turing.codeSize
statement: formalized
---

# Machine codes

A *machine code* is first-order data: a header (number of work tapes, alphabet size, number of states, start state) and a dense transition table with one entry per observation, in a fixed canonical order. A well-formed code is interpreted as a multi-input machine, with binary input and output through two reserved alphabet symbols. Codes serialize exactly: the *description* $\alpha \in \{0,1\}^*$ of a code has size $\left\vert {\alpha} \right\vert$, and *total decoding* interprets every string — $[\alpha]_i$ denotes the coded machine with $i$ input tapes described by $\alpha$, with every malformed string denoting one fixed machine that immediately rejects.

## Depends on

- [Multi-input Turing machine](def-multiinput-tm.md)

## Lean

Formalized as [`Turing.Code`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/Turing.Code), [`Turing.Code.toTM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/Turing.Code.toTM), [`Turing.encodeCode`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/Turing.encodeCode), [`Turing.decodeCode`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/Turing.decodeCode), [`Turing.codeSize`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/Turing.codeSize).

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 35](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L35)

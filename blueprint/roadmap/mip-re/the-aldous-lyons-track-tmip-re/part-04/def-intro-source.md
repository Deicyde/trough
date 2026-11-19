---
declaration: definition
origin: cited
lean: MIPRE.Tailored.Intro.srcQuestion, MIPRE.Tailored.Intro.srcSplitR, MIPRE.Tailored.Intro.srcSplitL, MIPRE.Tailored.Intro.pauliLen, MIPRE.Tailored.Intro.pauliRead
statement: formalized
---

# The input's question at an auxiliary answer, and the Pauli labels

The introspection verifier runs the input's decider at index $2^n$ on the first $\dim$ bits of the registers $y$ of its two Introspect answers, and the honest strategy measures the input's strategy at the same question; a Read answer is compared with an Introspect answer at the same register, and a Sample answer at the seed $z$ with one at the register $L_w(z)$. So the input question at an auxiliary answer is the first $\dim$ bits of $y$, or of $L_w(z)$ at a Sample answer, and the layout splits the input's answer there by the lengths the input's answer-length calculator outputs. A Pauli label has $\mathrm{count} \cdot \mathrm{width}$ answer bits, readable at the $Z$-basis Pauli label only.

## Depends on

- [Tailored normal form verifier; II:1758](../part-01/def-tailored-verifier.md)
- [LCS instance](../../foundations/part-01/def-lcs-instance.md)
- [The Magic Square](../../foundations/part-01/def-magic-square.md)
- [Pauli basis test](../../background-results/part-01/def-qld-game.md)
- [Closure of CL functions](../../structure-of-the-proof/part-01/lem-cl-closure.md)
- [Register embeddings and detyped query routing](../../structure-of-the-proof/part-01/lem-detype-queries.md)

## Lean

Formalized as [`MIPRE.Tailored.Intro.srcQuestion`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.srcQuestion), [`MIPRE.Tailored.Intro.srcSplitR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.srcSplitR), [`MIPRE.Tailored.Intro.srcSplitL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.srcSplitL), [`MIPRE.Tailored.Intro.pauliLen`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.pauliLen), [`MIPRE.Tailored.Intro.pauliRead`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.pauliRead).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1598](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1598)

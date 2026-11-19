---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.eqsCons_iff, MIPRE.Tailored.AnsRed.Typed.ldCons_iff, MIPRE.Tailored.AnsRed.Typed.consCons_iff, MIPRE.Tailored.AnsRed.Typed.indCons_iff_a, MIPRE.Tailored.AnsRed.Typed.indCons_iff_b, MIPRE.Tailored.AnsRed.Typed.proofCons_iff_a, MIPRE.Tailored.AnsRed.Typed.proofCons_iff_b, MIPRE.Tailored.AnsRed.Typed.cons_iff, MIPRE.Tailored.AnsRed.Typed.accepts_iff
statement: formalized
proof: formalized
---

# Reading the answer-reduced constraints

For answers of their types' lengths, the constraints at a pair of typed questions hold exactly when the four checks hold of the field elements the answers carry: when the roles agree, the seeded low-degree test accepts the two answers read as answers of the test; when the low-degree types agree, the isolated codewords are the oracle's in the same slots; each answer at an axis-parallel line is indifferent along it; and each oracle point answer passes the thirteen checks at its point.

## Depends on

- [The answer-reduced game as typed tailored data; defn:combi_ans_red](def-ar-tailored-game.md)
- [Slot values and block-local polynomials](lem-ar-slots.md)

## Proof

An equation $E(z) = \kappa$ between field elements, $E$ an $\mathbb{F}_2$-linear map of the answer bits, holds exactly when the $t$ coordinate checks of its canonical bits do (Lemma [The Pauli basis test as linear constraints](../part-04/lem-intro-pauli-cons.md)), and a readable guard rejects exactly when its condition fails (Lemma [Linear forms on windows, and the input's constraints re-indexed](../part-04/lem-intro-forms.md)). Each check reads the bits of field elements lying inside their answers; the readable checks of the proof check read only readable values, which lie in the readable part.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.eqsCons_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.eqsCons_iff), [`MIPRE.Tailored.AnsRed.Typed.ldCons_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.ldCons_iff), [`MIPRE.Tailored.AnsRed.Typed.consCons_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.consCons_iff), [`MIPRE.Tailored.AnsRed.Typed.indCons_iff_a`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.indCons_iff_a), [`MIPRE.Tailored.AnsRed.Typed.indCons_iff_b`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.indCons_iff_b), [`MIPRE.Tailored.AnsRed.Typed.proofCons_iff_a`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.proofCons_iff_a), [`MIPRE.Tailored.AnsRed.Typed.proofCons_iff_b`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.proofCons_iff_b), [`MIPRE.Tailored.AnsRed.Typed.cons_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.cons_iff), [`MIPRE.Tailored.AnsRed.Typed.accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.accepts_iff).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2905](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2905)

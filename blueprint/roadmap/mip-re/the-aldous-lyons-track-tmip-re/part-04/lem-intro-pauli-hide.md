---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.PauliHide.answerBits_decodeBits_of_length, MIPRE.Tailored.Intro.PauliHide.pauliXProj, MIPRE.Tailored.Intro.PauliHide.pauliXProj_eq, MIPRE.Tailored.Intro.PauliHide.hideChecks, MIPRE.Tailored.Intro.PauliHide.hideChecks_iff, MIPRE.Tailored.Intro.PauliHide.pauliHideCons, MIPRE.Tailored.Intro.PauliHide.pauliHideConsRev, MIPRE.Tailored.Intro.PauliHide.pauliHideCons_iff, MIPRE.Tailored.Intro.PauliHide.pauliHideConsRev_iff
statement: formalized
proof: formalized
---

# The first hiding edge as linear constraints

A Pauli answer of the right length is the encoding of the answer it decodes to. The kernel's projection of a decoded $X$-basis Pauli answer is $\mathbb{F}_2$-linear in its bits. So the comparison of an $X$-basis Pauli answer with an answer at the first hiding level — equal dual readouts on the first factor, and equal coordinates off it — is a list of linear constraints on the two answers, in either order, given a list of vectors spanning the kernel of the first stage's linear map.

## Depends on

- [The Pauli basis test as linear constraints](lem-intro-pauli-cons.md)
- [Pauli mixing with a retained classical fibre](../../structure-of-the-proof/part-02/lem-pauli-mixing.md)

## Proof

The projection reads the self-dual coordinates of the field elements of the answer, each a fixed linear function of the $k$ bits encoding it. The dual readouts agree exactly when the difference is orthogonal to the kernel, as in Lemma [Comparisons of registers as linear constraints](lem-intro-register-cons.md).

## Lean

Formalized as [`MIPRE.Tailored.Intro.PauliHide.answerBits_decodeBits_of_length`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliHide.answerBits_decodeBits_of_length), [`MIPRE.Tailored.Intro.PauliHide.pauliXProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliHide.pauliXProj), [`MIPRE.Tailored.Intro.PauliHide.pauliXProj_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliHide.pauliXProj_eq), [`MIPRE.Tailored.Intro.PauliHide.hideChecks`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliHide.hideChecks), [`MIPRE.Tailored.Intro.PauliHide.hideChecks_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliHide.hideChecks_iff), [`MIPRE.Tailored.Intro.PauliHide.pauliHideCons`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliHide.pauliHideCons), [`MIPRE.Tailored.Intro.PauliHide.pauliHideConsRev`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliHide.pauliHideConsRev), [`MIPRE.Tailored.Intro.PauliHide.pauliHideCons_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliHide.pauliHideCons_iff), [`MIPRE.Tailored.Intro.PauliHide.pauliHideConsRev_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.PauliHide.pauliHideConsRev_iff).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1780](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1780)

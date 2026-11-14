---
declaration: definition
origin: cited
lean: MIPRE.Tailored.Intro.pad, MIPRE.Tailored.Intro.lenR, MIPRE.Tailored.Intro.lenL, MIPRE.Tailored.Intro.enc, MIPRE.Tailored.Intro.unpad, MIPRE.Tailored.Intro.dec, MIPRE.Tailored.Intro.Fits, MIPRE.Tailored.Intro.OkLayout, MIPRE.Tailored.Intro.decB
statement: formalized
---

# The padded answer layout of question reduction

The introspection verifier's answers are byte strings: a Pauli answer, or a tuple of self-delimiting fields whose last field may be the input's answer, of variable length at most $R$. The tailored question reduction re-encodes them with fixed lengths per label, readable bits first: a Pauli answer is kept, readable when it is a $Z$-basis answer and linear otherwise; an Introspect or Sample answer $(y, \alpha)$ becomes $y$, the input's readable answer bits padded with zeros to $R$, and its linear answer bits padded to $R$, the first two readable; a Read answer $(y, y', \alpha)$ becomes $y$ and the padded readable bits (readable), then $y'$ and the padded linear bits (linear); a Hide answer $(y, y', x)$ becomes $y$ (readable), $y'$ and $x$ (linear). The input's split of its answer into readable and linear bits is that at the question read off the readable register $y$ (a parameter here). Decoding strips the padding and re-forms the tuple.

## Depends on

- [The introspective verifier](../../structure-of-the-proof/part-02/def-intro-verifier.md)

## Lean

Formalized as [`MIPRE.Tailored.Intro.pad`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.pad), [`MIPRE.Tailored.Intro.lenR`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.lenR), [`MIPRE.Tailored.Intro.lenL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.lenL), [`MIPRE.Tailored.Intro.enc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.enc), [`MIPRE.Tailored.Intro.unpad`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.unpad), [`MIPRE.Tailored.Intro.dec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dec), [`MIPRE.Tailored.Intro.Fits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.Fits), [`MIPRE.Tailored.Intro.OkLayout`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.OkLayout), [`MIPRE.Tailored.Intro.decB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.decB).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1554](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1554)

---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Intro.length_pad, MIPRE.Tailored.Intro.take_pad, MIPRE.Tailored.Intro.take_take_pad, MIPRE.Tailored.Intro.unpad_pad, MIPRE.Tailored.Intro.enc_pair, MIPRE.Tailored.Intro.dec_enc_pair, MIPRE.Tailored.Intro.dec_enc_read, MIPRE.Tailored.Intro.dec_enc_hide, MIPRE.Tailored.Intro.dec_enc_pauli, MIPRE.Tailored.Intro.length_enc_pair, MIPRE.Tailored.Intro.length_enc_read, MIPRE.Tailored.Intro.length_enc_hide, MIPRE.Tailored.Intro.length_enc_pauli, MIPRE.Tailored.Intro.dec_enc_of_ok, MIPRE.Tailored.Intro.length_enc_of_ok, MIPRE.Tailored.Intro.decB_enc_of_ok
statement: formalized
proof: formalized
---

# The layout's round trip and lengths

On a well-formed answer whose registers have length $Q$ and whose input answer has the input's readable and linear lengths, both at most $R$, decoding the re-encoding gives the answer back, and the re-encoding has the label's lengths.

## Depends on

- [The padded answer layout of question reduction](def-intro-layout.md)

## Proof

The fields of a well-formed tuple are recovered by the parser (`pairParts`, `tripleParts`); the re-encoding lays them out at fixed offsets, so cutting at those offsets recovers them, and the first $s$ bits of a block padded from $s \le R$ bits are the block.

## Lean

Formalized as [`MIPRE.Tailored.Intro.length_pad`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.length_pad), [`MIPRE.Tailored.Intro.take_pad`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.take_pad), [`MIPRE.Tailored.Intro.take_take_pad`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.take_take_pad), [`MIPRE.Tailored.Intro.unpad_pad`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.unpad_pad), [`MIPRE.Tailored.Intro.enc_pair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.enc_pair), [`MIPRE.Tailored.Intro.dec_enc_pair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dec_enc_pair), [`MIPRE.Tailored.Intro.dec_enc_read`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dec_enc_read), [`MIPRE.Tailored.Intro.dec_enc_hide`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dec_enc_hide), [`MIPRE.Tailored.Intro.dec_enc_pauli`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dec_enc_pauli), [`MIPRE.Tailored.Intro.length_enc_pair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.length_enc_pair), [`MIPRE.Tailored.Intro.length_enc_read`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.length_enc_read), [`MIPRE.Tailored.Intro.length_enc_hide`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.length_enc_hide), [`MIPRE.Tailored.Intro.length_enc_pauli`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.length_enc_pauli), [`MIPRE.Tailored.Intro.dec_enc_of_ok`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.dec_enc_of_ok), [`MIPRE.Tailored.Intro.length_enc_of_ok`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.length_enc_of_ok), [`MIPRE.Tailored.Intro.decB_enc_of_ok`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.decB_enc_of_ok).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1574](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1574)

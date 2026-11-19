---
declaration: lemma
origin: cited
lean: MIPRE.SAT.binFieldGalois, MIPRE.SAT.nonempty_binField
statement: formalized
proof: formalized
---

# An admissible field with a bit representation

For every $k \geq 1$ there is a field of size $2^k$ together with a $k$-bit representation of its elements admitting a left inverse; that is, `MIPRE.SAT.BinField` $k$ is inhabited.

## Depends on

- [The bespoke PCP for deciders](../../structure-of-the-proof/part-07/thm-pcp-decider.md)

## Proof

Mathlib's `GaloisField 2 k` has $2^k$ elements and dimension $k$ over $\mathbb{F}_2$; take the coordinate vector in any basis.

## Lean

Formalized as [`MIPRE.SAT.binFieldGalois`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.binFieldGalois), [`MIPRE.SAT.nonempty_binField`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.nonempty_binField).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 7203](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L7203)

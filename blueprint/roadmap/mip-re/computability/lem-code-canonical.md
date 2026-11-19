---
declaration: lemma
origin: cited
lean: Turing.decodeCodeExact_encodeCode, Turing.encodeCode_injective, Turing.decodeCodeExact_sound
statement: formalized
proof: formalized
---

# Canonical serialization

Exact decoding inverts encoding, distinct codes have distinct descriptions, and every description accepted by the exact decoder is the canonical encoding of the code it parses to.

## Depends on

- [Machine codes](def-machine-code.md)

## Proof

Compositional, from paired prefix and soundness lemmas for each field of the description format.

## Lean

Formalized as [`Turing.decodeCodeExact_encodeCode`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/Turing.decodeCodeExact_encodeCode), [`Turing.encodeCode_injective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/Turing.encodeCode_injective), [`Turing.decodeCodeExact_sound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/Turing.decodeCodeExact_sound).

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 64](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L64)

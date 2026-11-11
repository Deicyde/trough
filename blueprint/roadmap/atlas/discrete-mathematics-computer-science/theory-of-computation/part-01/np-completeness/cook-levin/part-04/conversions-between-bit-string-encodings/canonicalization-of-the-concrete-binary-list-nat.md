---
declaration: section
origin: cited
lean: Cslib.Complexity.PolynomialEncoding.blocks_decode_sound, Cslib.Complexity.PolynomialEncoding.mapM_decode_nat, Cslib.Complexity.PolynomialEncoding.decode_list_nat, Cslib.Complexity.PolynomialEncoding.encode_decoded_nat_blocks, Cslib.Complexity.PolynomialEncoding.normalized_nat_blocks_length_le, Cslib.Complexity.PolynomialEncoding.decoded_list_nat_encode_length_le
statement: formalized
proof: formalized
---

# Canonicalization of the concrete binary List Nat codec

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonicalization-of-the-concrete-binary-list-nat/index.html).

## Successful block parsing reconstructs the input

Successful block parsing reconstructs the entire input.

Formalized by `Cslib.Complexity.PolynomialEncoding.blocks_decode_sound`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNat.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNat.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonicalization-of-the-concrete-binary-list-nat/index.html#blocks-decode-sound).

## Decoding natural-number payloads never fails

Nat payload decoding never fails, including on noncanonical bits.

Formalized by `Cslib.Complexity.PolynomialEncoding.mapM_decode_nat`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNat.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNat.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonicalization-of-the-concrete-binary-list-nat/index.html#map-m-decode-nat).

## Decoding a list of naturals is block parsing then number decoding

List Nat decoding is precisely framed-payload parsing followed by
the existing total Nat decoder.

Formalized by `Cslib.Complexity.PolynomialEncoding.decode_list_nat`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNat.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNat.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonicalization-of-the-concrete-binary-list-nat/index.html#decode-list-nat).

## Re-encoding decoded payloads normalizes each one

Canonical re-encoding normalizes each payload without changing
list order or multiplicity.

Formalized by `Cslib.Complexity.PolynomialEncoding.encode_decoded_nat_blocks`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNat.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNat.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonicalization-of-the-concrete-binary-list-nat/index.html#encode-decoded-nat-blocks).

## Normalizing framed number payloads at most triples the length

Normalizing every framed Nat payload increases length by at most
threefold, even for noncanonical input.

Formalized by `Cslib.Complexity.PolynomialEncoding.normalized_nat_blocks_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNat.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNat.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonicalization-of-the-concrete-binary-list-nat/index.html#normalized-nat-blocks-length-le).

## Re-encoded decoded list of naturals is linear in raw input

Re-encoding a successfully decoded List Nat is linear in the raw
input, not in the decoded numeric values.

Formalized by `Cslib.Complexity.PolynomialEncoding.decoded_list_nat_encode_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNat.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNat.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonicalization-of-the-concrete-binary-list-nat/index.html#decoded-list-nat-encode-length-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Canonicalization of the concrete binary List Nat codec](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonicalization-of-the-concrete-binary-list-nat/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonicalization-of-the-concrete-binary-list-nat)

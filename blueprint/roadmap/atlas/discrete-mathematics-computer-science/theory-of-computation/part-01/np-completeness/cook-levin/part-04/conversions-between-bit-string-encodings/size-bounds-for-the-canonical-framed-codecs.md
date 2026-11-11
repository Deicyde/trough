---
declaration: section
origin: cited
lean: Cslib.Complexity.PolynomialEncoding.blocks_length_le, Cslib.Complexity.PolynomialEncoding.decoded_list_length_le, Cslib.Complexity.PolynomialEncoding.decoded_pair_parts, Cslib.Complexity.PolynomialEncoding.decoded_fst_list_length_le, Cslib.Complexity.PolynomialEncoding.decoded_snd_list_length_le, Cslib.Complexity.PolynomialEncoding.decoded_middle_list_length_le, Cslib.Complexity.PolynomialEncoding.list_nat_encode_length_le, Cslib.Complexity.PolynomialEncoding.bounded_nat_list_encode_length_le
statement: formalized
proof: formalized
---

# Size bounds for the canonical framed codecs

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/size-bounds-for-the-canonical-framed-codecs/index.html).

## Decoded block count is at most the input length

Each decoded block consumes at least its delimiter bit.

Formalized by `Cslib.Complexity.PolynomialEncoding.blocks_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/size-bounds-for-the-canonical-framed-codecs/index.html#blocks-length-le).

## Decoded list has at most one element per input bit

A successfully decoded list has at most one element per input bit.
No canonicality assumption on the element payloads is needed.

Formalized by `Cslib.Complexity.PolynomialEncoding.decoded_list_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/size-bounds-for-the-canonical-framed-codecs/index.html#decoded-list-length-le).

## Decoded pair exposes its raw component payloads

Successful pair decoding exposes the exact raw component payloads.
This includes payloads which are not canonical encodings.

Formalized by `Cslib.Complexity.PolynomialEncoding.decoded_pair_parts`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/size-bounds-for-the-canonical-framed-codecs/index.html#decoded-pair-parts).

## Length bound for a list in the first field of a decoded pair

A list in the first field of a decoded pair is raw-input bounded.

Formalized by `Cslib.Complexity.PolynomialEncoding.decoded_fst_list_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/size-bounds-for-the-canonical-framed-codecs/index.html#decoded-fst-list-length-le).

## Length bound for a list in the second field of a decoded pair

A list in the second field of a decoded pair is raw-input bounded.

Formalized by `Cslib.Complexity.PolynomialEncoding.decoded_snd_list_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/size-bounds-for-the-canonical-framed-codecs/index.html#decoded-snd-list-length-le).

## Length bound for the middle list of a decoded triple

The middle list of a right-associated triple is raw-input bounded.
Used for TSP matrix rows and SET COVER set occurrences.

Formalized by `Cslib.Complexity.PolynomialEncoding.decoded_middle_list_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/size-bounds-for-the-canonical-framed-codecs/index.html#decoded-middle-list-length-le).

## Framed length bound for lists of $m$-bit naturals

A list of binary naturals with at most `m` bits per entry has the
stated framed length bound.

Formalized by `Cslib.Complexity.PolynomialEncoding.list_nat_encode_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/size-bounds-for-the-canonical-framed-codecs/index.html#list-nat-encode-length-le).

## Quadratic encoding bound for vertex lists below $n$

Lists of vertices below `n` have a quadratic certificate bound
when their length is at most `n`; no unary Nat encoding is used.

Formalized by `Cslib.Complexity.PolynomialEncoding.bounded_nat_list_encode_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/Bounds.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/size-bounds-for-the-canonical-framed-codecs/index.html#bounded-nat-list-encode-length-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Size bounds for the canonical framed codecs](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/size-bounds-for-the-canonical-framed-codecs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/size-bounds-for-the-canonical-framed-codecs)

---
declaration: section
origin: cited
lean: Cslib.Complexity.PolynomialEncoding.blocks_delimit, Cslib.Complexity.PolynomialEncoding.decode_list_delimit, Cslib.Complexity.PolynomialEncoding.decode_list_none_of_undelimit_none
statement: formalized
proof: formalized
---

# Structural laws for the existing framed list decoder

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/structural-laws-for-the-existing-framed-list-dec/index.html).

## Parsing a framed head leaves the raw remainder

Parsing a framed head leaves exactly the raw remainder, including
any later framing failure. The decoder's fuel does not alter this law.

Formalized by `Cslib.Complexity.PolynomialEncoding.blocks_delimit`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListParts.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListParts.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/structural-laws-for-the-existing-framed-list-dec/index.html#blocks-delimit).

## List decoder consumes one raw payload at a time

The canonical list decoder consumes one raw payload at a time.
Both element failure and later framing failure are retained exactly.

Formalized by `Cslib.Complexity.PolynomialEncoding.decode_list_delimit`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListParts.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListParts.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/structural-laws-for-the-existing-framed-list-dec/index.html#decode-list-delimit).

## Malformed first frame makes list decoding fail

A nonempty input with a malformed first frame fails list decoding.
Empty input is excluded because it is the valid empty list.

Formalized by `Cslib.Complexity.PolynomialEncoding.decode_list_none_of_undelimit_none`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListParts.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListParts.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/structural-laws-for-the-existing-framed-list-dec/index.html#decode-list-none-of-undelimit-none).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Structural laws for the existing framed list decoder](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/structural-laws-for-the-existing-framed-list-dec/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/structural-laws-for-the-existing-framed-list-dec)

---
declaration: section
origin: cited
lean: Cslib.Complexity.FramedCNF.normalizeNat, Cslib.Complexity.FramedCNF.normalizeNat_eq_encode_decode, Cslib.Complexity.FramedCNF.length_normalizeNat_le, Cslib.Complexity.FramedCNF.normalizeNat_encodeNat
statement: formalized
proof: formalized
---

# Normalizing the total binary natural-number decoder

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/normalizing-the-total-binary-natural-number-deco/index.html).

## Normalization of a raw binary natural-number payload

Canonicalize a raw payload without enumerating its decoded value.

Formalized by `Cslib.Complexity.FramedCNF.normalizeNat`, a definition declared in [CSLibExt/Computability/Complexity/FramedCNF/Normalize.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/FramedCNF/Normalize.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/normalizing-the-total-binary-natural-number-deco/index.html#normalize-nat).

## Payload normalization agrees with decode-then-encode

Normalization agrees with the existing total decoder on every
payload, not just canonical encodings.

Formalized by `Cslib.Complexity.FramedCNF.normalizeNat_eq_encode_decode`, a theorem declared in [CSLibExt/Computability/Complexity/FramedCNF/Normalize.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/FramedCNF/Normalize.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/normalizing-the-total-binary-natural-number-deco/index.html#normalize-nat-eq-encode-decode).

## Payload normalization adds at most one bit

Normalization adds at most one bit.

Formalized by `Cslib.Complexity.FramedCNF.length_normalizeNat_le`, a theorem declared in [CSLibExt/Computability/Complexity/FramedCNF/Normalize.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/FramedCNF/Normalize.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/normalizing-the-total-binary-natural-number-deco/index.html#length-normalize-nat-le).

## Payload normalization fixes canonical encodings

Canonical encodings are unchanged.

Formalized by `Cslib.Complexity.FramedCNF.normalizeNat_encodeNat`, a theorem declared in [CSLibExt/Computability/Complexity/FramedCNF/Normalize.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/FramedCNF/Normalize.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/normalizing-the-total-binary-natural-number-deco/index.html#normalize-nat-encode-nat).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Normalizing the total binary natural-number decoder](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/normalizing-the-total-binary-natural-number-deco/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/normalizing-the-total-binary-natural-number-deco)

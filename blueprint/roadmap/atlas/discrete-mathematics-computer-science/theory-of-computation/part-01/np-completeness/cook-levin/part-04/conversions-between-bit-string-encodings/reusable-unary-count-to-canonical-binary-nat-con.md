---
declaration: section
origin: cited
lean: Cslib.Complexity.PolynomialEncoding.UnaryNat.Lab, Cslib.Complexity.PolynomialEncoding.UnaryNat.labEquiv, Cslib.Complexity.PolynomialEncoding.UnaryNat.embedding, Cslib.Complexity.PolynomialEncoding.UnaryNat.emitLabel, Cslib.Complexity.PolynomialEncoding.UnaryNat.prog, Cslib.Complexity.PolynomialEncoding.UnaryNat.run_framed, Cslib.Complexity.PolynomialEncoding.UnaryNat.run_raw, Cslib.Complexity.PolynomialEncoding.UnaryNat.component
statement: formalized
proof: formalized
---

# Reusable unary-count to canonical binary Nat conversion

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reusable-unary-count-to-canonical-binary-nat-con/index.html).

## Control labels of the unary-to-binary converter

Existing emitter labels and the cleanup/unframing continuation.

Formalized by `Cslib.Complexity.PolynomialEncoding.UnaryNat.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reusable-unary-count-to-canonical-binary-nat-con/index.html#lab).

## Label enumeration of the unary-to-binary converter

The finite label enumeration uses the existing emitter enumeration
and two Boolean choices, without a noncomputable list conversion.

Formalized by `Cslib.Complexity.PolynomialEncoding.UnaryNat.labEquiv`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reusable-unary-count-to-canonical-binary-nat-con/index.html#lab-equiv).

## Emitter stack embedding in the unary-to-binary converter

The component retains the existing emitter's heterogeneous alphabets.

Formalized by `Cslib.Complexity.PolynomialEncoding.UnaryNat.embedding`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reusable-unary-count-to-canonical-binary-nat-con/index.html#embedding).

## Label map from the emitter halt to scratch cleanup

The actual emitter halt is followed by charged scratch cleanup.

Formalized by `Cslib.Complexity.PolynomialEncoding.UnaryNat.emitLabel`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reusable-unary-count-to-canonical-binary-nat-con/index.html#emit-label).

## Program of the unary-to-binary converter

`framed = true` keeps the new frame; otherwise only that frame is
removed, preserving any earlier output below it.

Formalized by `Cslib.Complexity.PolynomialEncoding.UnaryNat.prog`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reusable-unary-count-to-canonical-binary-nat-con/index.html#prog).

## Converter turns a unary count into a canonical binary frame

Emit one canonical Nat frame above any earlier output and restore
all conversion scratch. The old counter is consumed; unrelated stacks,
including `X`, are preserved. Cleanup is part of the charged run.

Formalized by `Cslib.Complexity.PolynomialEncoding.UnaryNat.run_framed`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reusable-unary-count-to-canonical-binary-nat-con/index.html#run-framed).

## Converter turns a unary count into a raw canonical binary payload

Convert a unary count to the canonical unframed Nat payload,
preserving an earlier output suffix and clearing every used work stack.

Formalized by `Cslib.Complexity.PolynomialEncoding.UnaryNat.run_raw`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reusable-unary-count-to-canonical-binary-nat-con/index.html#run-raw).

## Unary-to-binary converter as a host component

The adapter is a finite component of the existing Host. Its input
counter has `n` physical symbols; the bound is linear in that length,
not in the bit length of an arbitrary binary-encoded numeric input.

Formalized by `Cslib.Complexity.PolynomialEncoding.UnaryNat.component`, an abbreviation declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/UnaryNat.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reusable-unary-count-to-canonical-binary-nat-con/index.html#component).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reusable unary-count to canonical binary Nat conversion](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reusable-unary-count-to-canonical-binary-nat-con/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/reusable-unary-count-to-canonical-binary-nat-con)

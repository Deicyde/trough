---
declaration: section
origin: cited
lean: Cslib.Complexity.PolynomialEncoding.ListNatPairPair.K, Cslib.Complexity.PolynomialEncoding.ListNatPairPair.Lab, Cslib.Complexity.PolynomialEncoding.ListNatPairPair.splitEmb, Cslib.Complexity.PolynomialEncoding.ListNatPairPair.itemsEmb, Cslib.Complexity.PolynomialEncoding.ListNatPairPair.pairEmb, Cslib.Complexity.PolynomialEncoding.ListNatPairPair.splitLabel, Cslib.Complexity.PolynomialEncoding.ListNatPairPair.itemsLabel, Cslib.Complexity.PolynomialEncoding.ListNatPairPair.pairLabel
statement: formalized
proof: formalized
---

# Four canonical outputs from a Nat-pair list and a Nat pair

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html).

## Stacks of the four-output pair-list decoder

Two disjoint existing workspaces; the pair buffer also serves the
initial outer-frame split and is cleared before normalization starts.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.K`, an inductive type declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#k).

## Control labels of the four-output pair-list decoder

The existing split, list projector, and final pair normalizer.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#lab).

## Outer-splitter stack embedding in the four-output decoder

The outer splitter reuses the final pair's input and empty buffer.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.splitEmb`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#split-emb).

## List-projector stack embedding in the four-output decoder

The list projector has its own disjoint workspace.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.itemsEmb`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#items-emb).

## Final pair-projector stack embedding in the four-output decoder

The final pair projector has its own disjoint workspace.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.pairEmb`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#pair-emb).

## Label map from the outer splitter to the list projector

Successful outer framing enters the item-list projector.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.splitLabel`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#split-label).

## Label map from the list projector to the final pair decoder

Successful item projection enters the final pair decoder.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.itemsLabel`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#items-label).

## Label map from final pair halts to the decoder outcomes

The final pair's actual halts are the whole decoder's outcomes.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.pairLabel`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#pair-label).

## Program of the four-output pair-list decoder

The whole finite program is a composition of existing components.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.prog`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#prog).

## Stack invariant of the four-output pair-list decoder

Exact raw-field and four-output invariant, with empty private scratch.
At entry the item field is empty and the entire raw input is `pairRaw`.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.st`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#st).

## Four-output decoder emits four canonical outputs on success

The entire raw decoder emits four canonical outputs, preserving
caller suffixes and emptying all input and private scratch on success.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.run_some`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#run-some).

## Four-output decoder output is at most twice the input length

The combined newly emitted output size is at most twice raw input
length, independently of decoded magnitudes and caller output suffixes.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.output_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#output-length-le).

## Four-output decoder fails on malformed input

Every failed raw decode reaches `bad` within the same whole-input
bound. Failed owned workspace can be partial and must be discarded
or cleared.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.run_none`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#run-none).

## Four-output pair-list decoder as a host component

The fixed seventeen-stack decoder in the existing Host interface.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.component`, an abbreviation declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#component).

## Four-output decoder reaches exactly the canonical decoding outcome

Total raw decoder contract with four output suffixes. Exactly the
canonical decoder's success/failure label is reached, with empty
scratch on success.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#run).

## Embedded four-output decoder preserves outside stacks

Embedded execution preserves every outside stack on both outcomes.
Successful output suffixes survive and private scratch is empty. Failed
workspace may be partial. Callers establish continuation-label separation.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPairPair.run_embedded`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPairPair.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html#run-embedded).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Four canonical outputs from a Nat-pair list and a Nat pair](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/four-canonical-outputs-from-a-nat-pair-list-and)

---
declaration: section
origin: cited
lean: Cslib.Complexity.PolynomialEncoding.ListNatPair.projection_length_le, Cslib.Complexity.PolynomialEncoding.ListNatPair.K, Cslib.Complexity.PolynomialEncoding.ListNatPair.Lab, Cslib.Complexity.PolynomialEncoding.ListNatPair.pairEmb, Cslib.Complexity.PolynomialEncoding.ListNatPair.pairLabel, Cslib.Complexity.PolynomialEncoding.ListNatPair.prog, Cslib.Complexity.PolynomialEncoding.ListNatPair.st, Cslib.Complexity.PolynomialEncoding.ListNatPair.element_run
statement: formalized
proof: formalized
---

# Canonical projection of lists of binary Nat pairs

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html).

## Projected pair lists total at most four times the input length

Both projected canonical lists together are bounded by four times
the original raw list length, including noncanonical input payloads.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPair.projection_length_le`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html#projection-length-le).

## Stacks of the pair-list projector

Raw outer input, two reversed accumulators, two outputs, and the
existing Nat-pair component's workspace.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPair.K`, an inductive type declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html#k).

## Control labels of the pair-list projector

Read one outer frame, normalize its pair, emit both fields, repeat.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPair.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html#lab).

## Stack embedding of the pair normalizer in the pair-list projector

The Nat-pair component is embedded without changing its alphabets.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPair.pairEmb`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html#pair-emb).

## Pair-normalizer halt redirection in the pair-list projector

Only the pair component's actual halts are redirected.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPair.pairLabel`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html#pair-label).

## Program of the pair-list projector

Concrete outer parsing, pair normalization, and two framed streams.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPair.prog`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html#prog).

## Eleven-stack invariant of the pair-list projector

The exact eleven-stack invariant, with caller output suffixes.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPair.st`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html#st).

## Pair-list projector emits one weight and one value frame per item

One successfully decoded item contributes one canonical weight
frame and one canonical value frame, with pair scratch emptied again.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPair.element_run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html#element-run).

## Pair-list projector main loop emits both lists in reverse

The main loop emits both lists in reverse, ready for the two
final stack reversals. Order and multiplicity follow the decoded input.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPair.blocks_run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html#blocks-run).

## Pair-list projector yields canonical weight and value lists

Successful generic decoding yields the canonical weight and value
lists on separate stacks. All input and scratch stacks are emptied.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPair.run_some`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html#run-some).

## Pair-list projector fails on malformed input in linear time

Malformed outer framing or any malformed pair reaches `bad` in
linear time. Failed workspaces may contain partial data and need clearing.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPair.run_none`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html#run-none).

## Pair-list projector as a host component

The concrete eleven-stack projector uses the existing Host model.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPair.component`, an abbreviation declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html#component).

## Pair-list projector always terminates at the decoding outcome

Total decoder outcome. Success projects canonical lists with empty
scratch; failure promises termination, not reusable workspace contents.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPair.run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean, line 489](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean#L489). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html#run).

## Embedded pair-list projector preserves outside stacks

Any stack embedding preserves the external frame on both outcomes.
Only mapped-label reachability is promised: callers establish their own
continuation-label separation. Failed private workspace needs clearing.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListNatPair.run_embedded`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/PolynomialEncoding/ListNatPair.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html#run-embedded).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Canonical projection of lists of binary Nat pairs](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/canonical-projection-of-lists-of-binary-nat-pair)

---
declaration: section
origin: cited
lean: Cslib.Complexity.PolynomialEncoding.PairSplit.K, Cslib.Complexity.PolynomialEncoding.PairSplit.Lab, Cslib.Complexity.PolynomialEncoding.PairSplit.prog, Cslib.Complexity.PolynomialEncoding.PairSplit.st, Cslib.Complexity.PolynomialEncoding.PairSplit.run_delimit, Cslib.Complexity.PolynomialEncoding.PairSplit.run_some, Cslib.Complexity.PolynomialEncoding.PairSplit.run_none, Cslib.Complexity.PolynomialEncoding.PairSplit.component
statement: formalized
proof: formalized
---

# Raw projection of the canonical pair frame

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/raw-projection-of-the-canonical-pair-frame/index.html).

## Stacks of the raw pair-frame splitter

The original input becomes the second field; `left` holds the first.

Formalized by `Cslib.Complexity.PolynomialEncoding.PairSplit.K`, an inductive type declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/raw-projection-of-the-canonical-pair-frame/index.html#k).

## Control labels of the raw pair-frame splitter

Read one frame, restore its order, then report success or failure.

Formalized by `Cslib.Complexity.PolynomialEncoding.PairSplit.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/raw-projection-of-the-canonical-pair-frame/index.html#lab).

## Program of the raw pair-frame splitter

Pair framing is split using the existing delimiter and move kernels.

Formalized by `Cslib.Complexity.PolynomialEncoding.PairSplit.prog`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/raw-projection-of-the-canonical-pair-frame/index.html#prog).

## Stack layout of the raw pair-frame splitter

Explicit stack layout of the projection invariant.

Formalized by `Cslib.Complexity.PolynomialEncoding.PairSplit.st`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/raw-projection-of-the-canonical-pair-frame/index.html#st).

## Pair-frame splitter extracts both raw fields

Extract both raw fields, restore first-field order, and clear
scratch in exactly two steps per first-field bit plus two.

Formalized by `Cslib.Complexity.PolynomialEncoding.PairSplit.run_delimit`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/raw-projection-of-the-canonical-pair-frame/index.html#run-delimit).

## Pair-frame splitter projects every well-framed input in linear time

Every successful raw pair frame is projected within input length
plus one; its two payloads are left unnormalized.

Formalized by `Cslib.Complexity.PolynomialEncoding.PairSplit.run_some`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/raw-projection-of-the-canonical-pair-frame/index.html#run-some).

## Pair-frame splitter fails on malformed first-field framing

Malformed first-field framing reaches the actual failure label.
Scratch may contain a partial field and must be cleared before reuse.

Formalized by `Cslib.Complexity.PolynomialEncoding.PairSplit.run_none`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/raw-projection-of-the-canonical-pair-frame/index.html#run-none).

## Raw pair-frame splitter as a host component

The finite component interface used by fixed nested-codec callers.

Formalized by `Cslib.Complexity.PolynomialEncoding.PairSplit.component`, an abbreviation declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/raw-projection-of-the-canonical-pair-frame/index.html#component).

## Raw field projection agrees with the pair decoder

Raw field projection agrees with the existing pair decoder. This
is not a runtime assumption or implementation of either element codec.

Formalized by `Cslib.Complexity.PolynomialEncoding.PairSplit.run_decoded`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/raw-projection-of-the-canonical-pair-frame/index.html#run-decoded).

## Pair-frame splitter reaches the framing outcome

Total framing outcome, without prematurely accepting either field
as a value of its eventual element type.

Formalized by `Cslib.Complexity.PolynomialEncoding.PairSplit.run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/raw-projection-of-the-canonical-pair-frame/index.html#run).

## Embedded pair-frame splitter preserves caller stacks

Embedded projection preserves all caller stacks outside the
three-stack workspace, even when framing fails.

Formalized by `Cslib.Complexity.PolynomialEncoding.PairSplit.run_embedded`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/PairSplit.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/raw-projection-of-the-canonical-pair-frame/index.html#run-embedded).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Raw projection of the canonical pair frame](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/raw-projection-of-the-canonical-pair-frame/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/raw-projection-of-the-canonical-pair-frame)

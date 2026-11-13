---
declaration: section
origin: cited
lean: Cslib.Complexity.PolynomialEncoding.ListCount.K, Cslib.Complexity.PolynomialEncoding.ListCount.Lab, Cslib.Complexity.PolynomialEncoding.ListCount.prog, Cslib.Complexity.PolynomialEncoding.ListCount.st, Cslib.Complexity.PolynomialEncoding.ListCount.element_run, Cslib.Complexity.PolynomialEncoding.ListCount.blocks_run, Cslib.Complexity.PolynomialEncoding.ListCount.run_some, Cslib.Complexity.PolynomialEncoding.ListCount.run_none
statement: formalized
proof: formalized
---

# Counting frames of a concrete List Nat input

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/counting-frames-of-a-concrete-list-nat-input/index.html).

## Stacks of the frame counter for lists of naturals

Input, one-block scratch, and a unary element counter.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListCount.K`, an inductive type declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/counting-frames-of-a-concrete-list-nat-input/index.html#k).

## Control labels of the frame counter for lists of naturals

Each complete frame increments the counter and clears its scratch.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListCount.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/counting-frames-of-a-concrete-list-nat-input/index.html#lab).

## Program of the frame counter for lists of naturals

Count by repeated shared block reading and shared scratch cleanup.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListCount.prog`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/counting-frames-of-a-concrete-list-nat-input/index.html#prog).

## Stack contents of the frame counter for lists of naturals

The three actual stack contents.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListCount.st`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/counting-frames-of-a-concrete-list-nat-input/index.html#st).

## One frame adds one unary count bit

One complete frame contributes exactly one unary count bit and
leaves no payload scratch, independently of the decoded Nat's value.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListCount.element_run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/counting-frames-of-a-concrete-list-nat-input/index.html#element-run).

## Frame counter yields the number of raw frames in unary

Counting a sequence of raw frames yields its length in unary,
with the caller's counter suffix preserved and scratch empty.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListCount.blocks_run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/counting-frames-of-a-concrete-list-nat-input/index.html#blocks-run).

## Frame counter counts every successfully decoded list of naturals

Count every successfully decoded List Nat, including noncanonical
Nat payloads; the count suffix is preserved exactly.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListCount.run_some`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/counting-frames-of-a-concrete-list-nat-input/index.html#run-some).

## Frame counter fails on malformed list framing

Malformed List Nat framing reaches the failure endpoint. The
counter and scratch may be partial and must be cleared before reuse.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListCount.run_none`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/counting-frames-of-a-concrete-list-nat-input/index.html#run-none).

## Frame counter for lists of naturals as a host component

The frame counter is a finite component of the existing Host.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListCount.component`, an abbreviation declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/counting-frames-of-a-concrete-list-nat-input/index.html#component).

## Frame counter decides decodability and counts length in unary

Total List Nat decoding outcome and exact unary length on success.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListCount.run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/counting-frames-of-a-concrete-list-nat-input/index.html#run).

## Embedded frame counter preserves caller stacks

Embedded counting preserves every caller stack outside its
workspace on success and failure. Scratch is empty on success.

Formalized by `Cslib.Complexity.PolynomialEncoding.ListCount.run_embedded`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/ListCount.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/counting-frames-of-a-concrete-list-nat-input/index.html#run-embedded).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Counting frames of a concrete List Nat input](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/counting-frames-of-a-concrete-list-nat-input/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/counting-frames-of-a-concrete-list-nat-input)

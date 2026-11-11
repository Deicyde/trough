---
declaration: section
origin: cited
lean: Cslib.Complexity.FramedCNF.NormalizeMachine.K, Cslib.Complexity.FramedCNF.NormalizeMachine.Lab, Cslib.Complexity.FramedCNF.NormalizeMachine.prog, Cslib.Complexity.FramedCNF.NormalizeMachine.st, Cslib.Complexity.FramedCNF.NormalizeMachine.read_run, Cslib.Complexity.FramedCNF.NormalizeMachine.run, Cslib.Complexity.FramedCNF.NormalizeMachine.component, Cslib.Complexity.FramedCNF.NormalizeMachine.isPolyTime_normalizeNat
statement: formalized
proof: formalized
---

# A linear-time machine for total binary-payload normalization

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-linear-time-machine-for-total-binary-payload-n/index.html).

## Stacks of the payload normalizer machine

Input, reverse buffer, and output.

Formalized by `Cslib.Complexity.FramedCNF.NormalizeMachine.K`, an inductive type declared in [CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-linear-time-machine-for-total-binary-payload-n/index.html#k).

## Control labels of the payload normalizer machine

The reader records the last payload bit; `none` means empty input.

Formalized by `Cslib.Complexity.FramedCNF.NormalizeMachine.Lab`, an inductive type declared in [CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-linear-time-machine-for-total-binary-payload-n/index.html#lab).

## Program of the payload normalizer machine

Normalization using only Boolean stack symbols and finite control.

Formalized by `Cslib.Complexity.FramedCNF.NormalizeMachine.prog`, a definition declared in [CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-linear-time-machine-for-total-binary-payload-n/index.html#prog).

## Stack contents for the payload normalizer invariant

The three stack contents used in the run invariant.

Formalized by `Cslib.Complexity.FramedCNF.NormalizeMachine.st`, a definition declared in [CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-linear-time-machine-for-total-binary-payload-n/index.html#st).

## Read phase of the payload normalizer consumes each bit once

The read phase consumes each input bit once and optionally adds the
implicit terminal one. The prefix records already-consumed input.

Formalized by `Cslib.Complexity.FramedCNF.NormalizeMachine.read_run`, a theorem declared in [CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-linear-time-machine-for-total-binary-payload-n/index.html#read-run).

## Linear step bound for the payload normalizer machine

The whole component runs in at most `2 |x| + 3` steps.

Formalized by `Cslib.Complexity.FramedCNF.NormalizeMachine.run`, a theorem declared in [CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-linear-time-machine-for-total-binary-payload-n/index.html#run).

## Payload normalizer as a host component

The normalizer in the canonical component interface.

Formalized by `Cslib.Complexity.FramedCNF.NormalizeMachine.component`, an abbreviation declared in [CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-linear-time-machine-for-total-binary-payload-n/index.html#component).

## Payload normalization is polynomial-time

Total binary-payload normalization is polynomial-time in the
canonical encoded machine model.

Formalized by `Cslib.Complexity.FramedCNF.NormalizeMachine.isPolyTime_normalizeNat`, a theorem declared in [CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Complexity/FramedCNF/NormalizeMachine.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-linear-time-machine-for-total-binary-payload-n/index.html#is-poly-time-normalize-nat).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: A linear-time machine for total binary-payload normalization](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-linear-time-machine-for-total-binary-payload-n/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/a-linear-time-machine-for-total-binary-payload-n)

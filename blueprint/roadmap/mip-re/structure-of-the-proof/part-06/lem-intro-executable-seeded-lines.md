---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.SeedProgram.selector_eq_bits, MIPRE.Introspection.SeedProgram.card_selector_fiber, MIPRE.Introspection.SeedProgram.selectorProg_correct, MIPRE.Introspection.SeedProgram.selectorProg_runs, MIPRE.Introspection.SeededLineProgram.axisRepresentativeProg_correct, MIPRE.Introspection.SeededLineProgram.selectedDirectionProg_correct, MIPRE.Introspection.SeededLineProgram.diagonalRepresentativeProg_correct, MIPRE.Introspection.SeededLineProgram.axisRepresentativeProg_runs, MIPRE.Introspection.SeededLineProgram.diagonalRepresentativeProg_runs, MIPRE.QLD.PauliCL.ExplicitSeed.presentation_exactlyOn, MIPRE.QLD.PauliCL.ExplicitSeed.binaryPresentation_exactlyOn, MIPRE.QLD.PauliCL.ExplicitSeed.decode_presentation, MIPRE.QLD.PauliCL.ExplicitSeed.chi_seedPermutation, MIPRE.QLD.PauliCL.ExplicitSeed.qldGame_mu_selector_binary, MIPRE.QLD.PauliCL.axisRepresentativeProg_legacy, MIPRE.QLD.PauliCL.diagonalRepresentativeProg_legacy
statement: formalized
proof: formalized
---

# An executable balanced seed selector and line stages

For $m=2^j$ and a field of size $2^k$ with $j\leq k$, a uniform program computes the direction selector from canonical field bits; every index has exactly $2^{k-j}$ seeds. Uniform axis and diagonal programs compute the selected coordinate erasure, truncated direction, and canonical line point, and halt polynomially on all raw inputs. Replacing the old arbitrary field enumeration by this selector gives explicit three-level field and binary CL families. A proved seed permutation identifies their decoded question distribution exactly with the existing QLD game.

## Depends on

- [Executable canonical lines and explicit binary coordinates](../part-05/lem-intro-executable-lines.md)

## Proof

Number field elements by their canonical bit value and select the high $j$ bits. Splitting the bit index into quotient and remainder gives the equal fibre sizes. Compose this program with coordinate masks and the canonical-line routine. Relabel only the seed in the uniform content space to compare with the old field enumeration; all decoded question fields then agree literally. Transport the uniform distribution through that permutation.

## Lean

Formalized as [`MIPRE.Introspection.SeedProgram.selector_eq_bits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SeedProgram.selector_eq_bits), [`MIPRE.Introspection.SeedProgram.card_selector_fiber`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SeedProgram.card_selector_fiber), [`MIPRE.Introspection.SeedProgram.selectorProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SeedProgram.selectorProg_correct), [`MIPRE.Introspection.SeedProgram.selectorProg_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SeedProgram.selectorProg_runs), [`MIPRE.Introspection.SeededLineProgram.axisRepresentativeProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SeededLineProgram.axisRepresentativeProg_correct), [`MIPRE.Introspection.SeededLineProgram.selectedDirectionProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SeededLineProgram.selectedDirectionProg_correct), [`MIPRE.Introspection.SeededLineProgram.diagonalRepresentativeProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SeededLineProgram.diagonalRepresentativeProg_correct), [`MIPRE.Introspection.SeededLineProgram.axisRepresentativeProg_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SeededLineProgram.axisRepresentativeProg_runs), [`MIPRE.Introspection.SeededLineProgram.diagonalRepresentativeProg_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.SeededLineProgram.diagonalRepresentativeProg_runs), [`MIPRE.QLD.PauliCL.ExplicitSeed.presentation_exactlyOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.ExplicitSeed.presentation_exactlyOn), [`MIPRE.QLD.PauliCL.ExplicitSeed.binaryPresentation_exactlyOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.ExplicitSeed.binaryPresentation_exactlyOn), [`MIPRE.QLD.PauliCL.ExplicitSeed.decode_presentation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.ExplicitSeed.decode_presentation), [`MIPRE.QLD.PauliCL.ExplicitSeed.chi_seedPermutation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.ExplicitSeed.chi_seedPermutation), [`MIPRE.QLD.PauliCL.ExplicitSeed.qldGame_mu_selector_binary`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.ExplicitSeed.qldGame_mu_selector_binary), [`MIPRE.QLD.PauliCL.axisRepresentativeProg_legacy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.axisRepresentativeProg_legacy), [`MIPRE.QLD.PauliCL.diagonalRepresentativeProg_legacy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.PauliCL.diagonalRepresentativeProg_legacy).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 3638](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3638)

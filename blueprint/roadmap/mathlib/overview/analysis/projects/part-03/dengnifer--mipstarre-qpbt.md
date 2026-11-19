---
declaration: theorem
origin: cited
lean: MIPStarRE.QPBT.exists_spcc_value_one, MIPStarRE.QPBT.exists_ld_soundness, MIPStarRE.QPBT.pauli_soundness, MIPStarRE.QPBT.pauli_soundness_qubit
statement: formalized
proof: formalized
---

# Quantum Pauli basis test

[Dengnifer/MIPStarRE-QPBT](https://github.com/Dengnifer/MIPStarRE-QPBT) at commit [cd250994](https://github.com/Dengnifer/MIPStarRE-QPBT/tree/cd2509945687ecb2e708222df3e4281c6e0f5138), 2026-11-15.

## Depends on

- [MIPStarRE](../../../probability-theory/projects/lionsr--mipstarre.md)

## Proof depends on

- [Distributions](../../distribution-theory/distributions.md)
- [Matrix representation](../../../linear-algebra/bilinear-and-quadratic-forms/matrix-representation.md)
- [Power functions](../../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/power-functions.md)
- [Rank of a matrix](../../../../undergraduate/linear-algebra/matrices/rank-of-a-matrix.md)
- [Ring-valued matrix](../../../linear-algebra/matrices/ring-valued-matrix.md)
- [Unitary group](../../../../undergraduate/group-theory/classical-automorphism-groups/unitary-group.md)
- [Characteristic p](../../../general-algebra/field-theory/characteristic-p.md)
- [The Triangle Inequality](../../../../hundred-theorems/part-04/the-triangle-inequality.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`MIPStarRE.QPBT.exists_spcc_value_one`](https://github.com/Dengnifer/MIPStarRE-QPBT/blob/cd2509945687ecb2e708222df3e4281c6e0f5138/QPBT/Test/Completeness.lean#L271) (theorem)
- [`MIPStarRE.QPBT.exists_ld_soundness`](https://github.com/Dengnifer/MIPStarRE-QPBT/blob/cd2509945687ecb2e708222df3e4281c6e0f5138/QPBT/Test/LowDegreeGameTheorems.lean#L88) (theorem)
- [`MIPStarRE.QPBT.pauli_soundness`](https://github.com/Dengnifer/MIPStarRE-QPBT/blob/cd2509945687ecb2e708222df3e4281c6e0f5138/QPBT/Test/Soundness.lean#L115) (theorem)
- [`MIPStarRE.QPBT.pauli_soundness_qubit`](https://github.com/Dengnifer/MIPStarRE-QPBT/blob/cd2509945687ecb2e708222df3e4281c6e0f5138/QPBT/Test/QubitForm.lean#L467) (theorem)

No file its headlines import, directly or not (320 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 354 .lean files; its Lean libraries `QPBT`, `Challenge`, `Solution` hold 354, declaring 3,913 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/Dengnifer/MIPStarRE-QPBT/blob/cd2509945687ecb2e708222df3e4281c6e0f5138/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- [MIPStarRE](../../../probability-theory/projects/lionsr--mipstarre.md) at `5fc363bc`.

## Placement

Of its imports of Mathlib modules in an overview area, 3 of 4 are in Analysis, 2.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (3 of 4 imports, 2.8×), General algebra (1 of 4 imports, 0.7×). *Proof depends on* lists 8 of the 30 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [Dengnifer/MIPStarRE-QPBT at cd250994](https://github.com/Dengnifer/MIPStarRE-QPBT/tree/cd2509945687ecb2e708222df3e4281c6e0f5138)

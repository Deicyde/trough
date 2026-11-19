---
declaration: theorem
origin: cited
lean: IntermediateField.finrank_lt_finrank_of_lt, NumberField.absMulHeight₁_mul_le, NumberField.absMulHeight₁_inv, NumberField.mem_realField, NumberField.finite_of_finrank_le, NumberField.finite_setOf_not_isPseudoPisot, NumberField.absMulHeight₁_map
statement: formalized
proof: formalized
---

# Subspace-Theorems

[rwst/Subspace-Theorems](https://github.com/rwst/Subspace-Theorems) at commit [2fc7bea1](https://github.com/rwst/Subspace-Theorems/tree/2fc7bea12d398fbc8ea758ecb8516efe8e3ef33d), 2026-11-06.

> A working repository for **three roadmaps**, each standing on the one before.

*Quoted from [README.md](https://github.com/rwst/Subspace-Theorems/blob/2fc7bea12d398fbc8ea758ecb8516efe8e3ef33d/README.md), Apache-2.0.*

## Depends on

- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Field](../../../general-algebra/field-theory/field.md)
- [Finite-dimensionality](../../finite-dimensional-vector-spaces/finite-dimensionality.md)
- [9.7 Finite extensions](../../../../../stacks/preliminaries/part-01/9-fields/part-01/9-7-finite-extensions.md)
- [Finite set](../../../data-structures/sets/finite-set.md)
- [Set](../../../data-structures/sets/set.md)
- [Characteristic zero](../../../general-algebra/field-theory/characteristic-zero.md)

## Proof depends on

- [The Irrationality of the Square Root of 2](../../../../hundred-theorems/part-01/the-irrationality-of-the-square-root-of-2.md)
- [Splitting field](../../../general-algebra/field-theory/splitting-field.md)
- [Algebraic elements](../../../../undergraduate/ring-theory/field-theory/algebraic-elements.md)
- [Infinite](../../../combinatorics/pigeonhole-principles/infinite.md)
- [Vector subspace](../../../../undergraduate/linear-algebra/fundamentals/vector-subspace.md)
- [Rank of a set of vectors](../../../../undergraduate/linear-algebra/finite-dimensional-vector-spaces/rank-of-a-set-of-vectors.md)
- [Dual vector space](../../duality/dual-vector-space.md)
- [Transcendental elements](../../../../undergraduate/ring-theory/field-theory/transcendental-elements.md)

## Main results

Its Lean names are the theorems of its top-level module named Main, MainTheorem(s) or Statement(s):

- [`IntermediateField.finrank_lt_finrank_of_lt`](https://github.com/rwst/Subspace-Theorems/blob/2fc7bea12d398fbc8ea758ecb8516efe8e3ef33d/CorvajaZannier2004/MainTheorem.lean#L54) (theorem)
- [`NumberField.absMulHeight₁_mul_le`](https://github.com/rwst/Subspace-Theorems/blob/2fc7bea12d398fbc8ea758ecb8516efe8e3ef33d/CorvajaZannier2004/MainTheorem.lean#L70) (theorem)
- [`NumberField.absMulHeight₁_inv`](https://github.com/rwst/Subspace-Theorems/blob/2fc7bea12d398fbc8ea758ecb8516efe8e3ef33d/CorvajaZannier2004/MainTheorem.lean#L79) (theorem)
- [`NumberField.mem_realField`](https://github.com/rwst/Subspace-Theorems/blob/2fc7bea12d398fbc8ea758ecb8516efe8e3ef33d/CorvajaZannier2004/MainTheorem.lean#L89) (theorem)
- [`NumberField.finite_of_finrank_le`](https://github.com/rwst/Subspace-Theorems/blob/2fc7bea12d398fbc8ea758ecb8516efe8e3ef33d/CorvajaZannier2004/MainTheorem.lean#L101) (theorem)
- [`NumberField.finite_setOf_not_isPseudoPisot`](https://github.com/rwst/Subspace-Theorems/blob/2fc7bea12d398fbc8ea758ecb8516efe8e3ef33d/CorvajaZannier2004/MainTheorem.lean#L196) (theorem)
- [`NumberField.absMulHeight₁_map`](https://github.com/rwst/Subspace-Theorems/blob/2fc7bea12d398fbc8ea758ecb8516efe8e3ef33d/CorvajaZannier2004/MainTheorem.lean#L237) (theorem)

No file its headlines import, directly or not (156 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc3, Mathlib at [5e0c4e52](https://github.com/leanprover-community/mathlib4/tree/5e0c4e5239cb0a2d86d68a884bf52cfd963fce22).
- 547 .lean files; its Lean libraries `ArithmeticHeights`, `DiophantineApproximation`, `QuantitativeSubspace`, `STForMathlib`, `CorvajaZannier2004`, `AdamczewskiBugeaud2007` and 21 more hold 542, declaring 6,908 names, with `sorry` in 27 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/rwst/Subspace-Theorems/blob/2fc7bea12d398fbc8ea758ecb8516efe8e3ef33d/LICENSE)).

## Builds on

- Mathlib, at [5e0c4e52](https://github.com/leanprover-community/mathlib4/tree/5e0c4e5239cb0a2d86d68a884bf52cfd963fce22).
- `comparator` (https://github.com/leanprover/comparator) at `fd5d5bcf`.

## Placement

Of its imports of Mathlib modules in an overview area, 365 of 2286 are in Linear algebra, 2.7 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Linear algebra (365 of 2286 imports, 2.7×), General algebra (1300 of 2286 imports, 1.6×), Analysis (387 of 2286 imports, 0.6×). *Proof depends on* lists 8 of the 113 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [rwst/Subspace-Theorems at 2fc7bea1](https://github.com/rwst/Subspace-Theorems/tree/2fc7bea12d398fbc8ea758ecb8516efe8e3ef33d)

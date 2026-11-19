---
declaration: module
origin: cited
lean: CycleCutoff
statement: formalized
---

# CycleCutoff

*Cutoff for the Adjacent Transposition Shuffle on a Cycle*

[AxiomMath/CycleCutoff](https://github.com/AxiomMath/CycleCutoff) at commit [543a6bbd](https://github.com/AxiomMath/CycleCutoff/tree/543a6bbd5c5f784bdacb09d8318aaccabab0b532), 2026-09-29.

> This is a Lean formalization of total-variation cutoff for the adjacent transposition shuffle on the cycle of length `n`, at time `n² log n / (8π²)` with a window of order `n² log log n`.

*Quoted from [README.md](https://github.com/AxiomMath/CycleCutoff/blob/543a6bbd5c5f784bdacb09d8318aaccabab0b532/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Formula for the Number of Combinations](../../../../hundred-theorems/part-03/formula-for-the-number-of-combinations.md)
- [Matrix exponential](../../../../undergraduate/linear-algebra/exponential/matrix-exponential.md)
- [Permutation group of a type](../../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Finite set](../../../data-structures/sets/finite-set.md)
- [Logarithm](../../special-functions/logarithm.md)
- [Real number](../../../general-algebra/numbers/real-number.md)
- [Ring-valued matrix](../../../linear-algebra/matrices/ring-valued-matrix.md)
- [Exponential](../../special-functions/exponential.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`CycleCutoff`](https://github.com/AxiomMath/CycleCutoff/blob/543a6bbd5c5f784bdacb09d8318aaccabab0b532/CycleCutoff.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `Challenge/Basic.lean` holds `sorry` or `admit`.

## Project

- Lean v4.33.0, Mathlib at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).
- 149 .lean files; its Lean libraries `CycleCutoff`, `Challenge`, `Solution` hold 149, declaring 616 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/CycleCutoff/blob/543a6bbd5c5f784bdacb09d8318aaccabab0b532/LICENSE)).

## Builds on

- Mathlib, at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).

## Placement

Of its imports of Mathlib modules in an overview area, 71 of 123 are in Analysis, 2.1 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (71 of 123 imports, 2.1×), General algebra (27 of 123 imports, 0.6×). *Proof depends on* names 8 of the 22 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [AxiomMath/CycleCutoff at 543a6bbd](https://github.com/AxiomMath/CycleCutoff/tree/543a6bbd5c5f784bdacb09d8318aaccabab0b532)

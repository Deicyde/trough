---
declaration: module
origin: cited
lean: SSA, SSA.Projects.CIRCT.CIRCT, SSA.Projects.ISL.ISL
statement: formalized
---

# lean-mlir

[opencompl/lean-mlir](https://github.com/opencompl/lean-mlir) at commit [b8c4a771](https://github.com/opencompl/lean-mlir/tree/b8c4a771319a044854a4bbb49b8821381ef86ff8), 2026-07-28.

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Stream](../../list-like-structures/stream.md)
- [Integer](../../../general-algebra/numbers/integer.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [List](../../list-like-structures/list.md)
- [Polynomial in one indeterminate](../../../general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Ring](../../../general-algebra/rings/ring.md)
- [Array](../../list-like-structures/array.md)
- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`SSA`](https://github.com/opencompl/lean-mlir/blob/b8c4a771319a044854a4bbb49b8821381ef86ff8/SSA.lean), [`SSA.Projects.CIRCT.CIRCT`](https://github.com/opencompl/lean-mlir/blob/b8c4a771319a044854a4bbb49b8821381ef86ff8/SSA/Projects/CIRCT/CIRCT.lean), [`SSA.Projects.ISL.ISL`](https://github.com/opencompl/lean-mlir/blob/b8c4a771319a044854a4bbb49b8821381ef86ff8/SSA/Projects/ISL/ISL.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `SSA/Projects/CIRCT/Comb/Comb.lean`, `SSA/Projects/CIRCT/DCxComb/DCxCombFunctor.lean`, `SSA/Projects/CIRCT/HSxComb/HSxCombFunctor.lean`, `SSA/Projects/CIRCT/Register/Basic.lean`, `SSA/Projects/CIRCT/Stream/Basic.lean`, `SSA/Projects/CIRCT/Stream/Lemmas.lean`, `SSA/Projects/InstCombine/AliveStatements.lean`, `SSA/Projects/InstCombine/AliveStatements_sorry.lean`, `SSA/Projects/InstCombine/HackersDelight/ch2_1DeMorgan.lean`, `SSA/Projects/InstCombine/HackersDelight/ch2_2AdditionAndLogicalOps.lean` hold `sorry` or `admit`.

## Project

- Lean nightly-2025-12-01, Mathlib at [2100ee66](https://github.com/leanprover-community/mathlib4/tree/2100ee662d0d4b3233534f70716a04f15f74c300).
- 9,449 .lean files; its Lean libraries `SSA`, `AliveExamples`, `AliveStatements`, `AliveScaling`, `CIRCT`, `ISL` hold 5,000 (the first read), declaring 16,139 names, with `sorry` in 4936 files and 2 axioms, read without Lean.
- Its own CI at this commit: passing.
- License files: `LICENSE`; facts only.

## Builds on

- Mathlib, at [2100ee66](https://github.com/leanprover-community/mathlib4/tree/2100ee662d0d4b3233534f70716a04f15f74c300).
- `Blase`.
- `LeanMLIR`.
- `leanwuzla` (https://github.com/hargoniX/Leanwuzla.git) at `9d2639b7`.
- `SailRV64` (https://github.com/opencompl/riscv-lean.git) at `99b86fee`.
- `SexprPBV`.
- `TacBench`.

## Placement

Of its imports of Mathlib modules in an overview area, 10 of 20 are in Data structures, 3.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (10 of 20 imports, 3.5×), General algebra (10 of 20 imports, 1.4×). *Proof depends on* lists 8 of the 9 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [opencompl/lean-mlir at b8c4a771](https://github.com/opencompl/lean-mlir/tree/b8c4a771319a044854a4bbb49b8821381ef86ff8)

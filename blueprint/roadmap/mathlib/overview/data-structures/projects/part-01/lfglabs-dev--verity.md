---
declaration: module
origin: cited
lean: Compiler, Compiler.SolidityImport.AbiByteLanes, Compiler.SolidityImport.AbiMemory
statement: formalized
---

# Guarantees

[lfglabs-dev/verity](https://github.com/lfglabs-dev/verity) at commit [42cbb5de](https://github.com/lfglabs-dev/verity/tree/42cbb5de217c89538fc231a8f4b2ac423457e0ec), 2026-11-18.

> A formally verified smart contract compiler for Ethereum, written in [Lean 4](https://lean-lang.org/). Write a contract in an embedded DSL (or import it from Solidity), prove properties about it, and compile it to EVM bytecode through a compiler whose layers are themselves proved. Documentation: [veritylang.com](https://veritylang.com) · Paper: [verity.pdf](https://lfglabs.dev/papers/verity.pdf) · MIT licensed.

*Quoted from [README.md](https://github.com/lfglabs-dev/verity/blob/42cbb5de217c89538fc231a8f4b2ac423457e0ec/README.md), MIT, Copyright (c) 2025 Thomas Marchand.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Finite map](../../maps/finite-map.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [List](../../list-like-structures/list.md)
- [Array](../../list-like-structures/array.md)
- [Field](../../../general-algebra/field-theory/field.md)
- [Integer](../../../general-algebra/numbers/integer.md)
- [Hash map](../../maps/hash-map.md)
- [Closure](../../../topology/general-topology/part-01/closure.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Compiler`](https://github.com/lfglabs-dev/verity/blob/42cbb5de217c89538fc231a8f4b2ac423457e0ec/Compiler.lean), [`Compiler.SolidityImport.AbiByteLanes`](https://github.com/lfglabs-dev/verity/blob/42cbb5de217c89538fc231a8f4b2ac423457e0ec/Compiler/SolidityImport/AbiByteLanes.lean), [`Compiler.SolidityImport.AbiMemory`](https://github.com/lfglabs-dev/verity/blob/42cbb5de217c89538fc231a8f4b2ac423457e0ec/Compiler/SolidityImport/AbiMemory.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `scripts/.assurance_fixtures/UnionAxiomsFixture/NativeAndAttrs.lean` holds `sorry` or `admit`.

## Project

- Lean v4.31.0, Mathlib at [fabf563a](https://github.com/leanprover-community/mathlib4/tree/fabf563a7c95a166b8d7b6efca11c8b4dc9d911f).
- 793 .lean files; its Lean libraries `Verity`, `Contracts`, `SolidityImportSmoke`, `Compiler`, `AssuranceFixtures`, `Assurance` and 3 more hold 766, declaring 16,200 names, with `sorry` in 1 file and 8 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: MIT ([LICENSE.md](https://github.com/lfglabs-dev/verity/blob/42cbb5de217c89538fc231a8f4b2ac423457e0ec/LICENSE.md)).

## Builds on

- Mathlib, at [fabf563a](https://github.com/leanprover-community/mathlib4/tree/fabf563a7c95a166b8d7b6efca11c8b4dc9d911f).
- `evmyul` (https://github.com/lfglabs-dev/EVMYulLean.git) at `eb0b6ddf`.

## Placement

Of its imports of Mathlib modules in an overview area, 3 of 11 are in Data structures, 1.9 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (3 of 11 imports, 1.9×), General algebra (6 of 11 imports, 1.5×), Analysis (2 of 11 imports, 0.7×). *Proof depends on* names 8 of the 10 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [lfglabs-dev/verity at 42cbb5de](https://github.com/lfglabs-dev/verity/tree/42cbb5de217c89538fc231a8f4b2ac423457e0ec)

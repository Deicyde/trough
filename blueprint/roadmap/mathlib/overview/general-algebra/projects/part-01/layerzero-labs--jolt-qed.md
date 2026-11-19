---
declaration: module
origin: cited
lean: JoltBytecode, JoltConstraints, LeanRV64D
statement: formalized
---

# Jolt Qed: Formally Verifying The Jolt Zk-VM

[LayerZero-Labs/jolt-qed](https://github.com/LayerZero-Labs/jolt-qed) at commit [abd88dfd](https://github.com/LayerZero-Labs/jolt-qed/tree/abd88dfdf64833469c5bfc9b3a0f9647b2d61633), 2026-11-17.

> This repository contains proofs written using the Lean theorem proving assistant, towards formally verifying the completeness and soundness of the [Jolt zk-VM](https://github.com/a16z/jolt). The project is _still on-going_, and as Jolt is relatively complex, we logically decompose the task of formally verifying Jolt into the components shown below. Blocks in green are complete. Blocks in yellow are in-progress and, greyed out boxes are not yet started. Explicit details about each component, trust assumptions, and current progress can be found [here](https://randomwalks.xyz/blog/jolt-qed/).

*Quoted from [README.md](https://github.com/LayerZero-Labs/jolt-qed/blob/abd88dfdf64833469c5bfc9b3a0f9647b2d61633/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Characteristic of a ring](../../field-theory/characteristic-of-a-ring.md)
- [Integer](../../numbers/integer.md)
- [Field](../../field-theory/field.md)
- [Natural number](../../numbers/natural-number.md)
- [Array](../../../data-structures/list-like-structures/array.md)
- [List](../../../data-structures/list-like-structures/list.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`JoltBytecode`](https://github.com/LayerZero-Labs/jolt-qed/blob/abd88dfdf64833469c5bfc9b3a0f9647b2d61633/JoltBytecode.lean), [`JoltConstraints`](https://github.com/LayerZero-Labs/jolt-qed/blob/abd88dfdf64833469c5bfc9b3a0f9647b2d61633/JoltConstraints.lean), [`LeanRV64D`](https://github.com/LayerZero-Labs/jolt-qed/blob/abd88dfdf64833469c5bfc9b3a0f9647b2d61633/LeanRV64D.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `JoltBytecode/InstructionEquivalence/Instructions/System/Mret.lean`, `JoltBytecode/RiscvInstruction.lean`, `JoltConstraints/theorems/Completeness/RamAddrEqRs1PlusImmMinusLookupIfLoadStore.lean`, `JoltConstraints/theorems/Completeness/RamValEqInitialPlusPrefixRamInc.lean`, `JoltConstraints/theorems/Completeness/RamValFinalEqInitialPlusRamInc.lean`, `JoltConstraints/theorems/Completeness/RightLookupAdd.lean`, `JoltConstraints/theorems/Completeness/RightLookupEqRightInputOtherwise.lean` hold `sorry` or `admit`.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 726 .lean files; its Lean libraries `JoltBytecode`, `JoltConstraints`, `LeanRV64D` hold 725, declaring 8,122 names, with `sorry` in 7 files and 75 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/LayerZero-Labs/jolt-qed/blob/abd88dfdf64833469c5bfc9b3a0f9647b2d61633/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- `Sail` (https://github.com/rems-project/lean-sail) at `1e5b216b`.

## Placement

Of its imports of Mathlib modules in an overview area, 116 of 129 are in General algebra, 2.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (116 of 129 imports, 2.5×). *Proof depends on* names 6 of the 6 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [LayerZero-Labs/jolt-qed at abd88dfd](https://github.com/LayerZero-Labs/jolt-qed/tree/abd88dfdf64833469c5bfc9b3a0f9647b2d61633)

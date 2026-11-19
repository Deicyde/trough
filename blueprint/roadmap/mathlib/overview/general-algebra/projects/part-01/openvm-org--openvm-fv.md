---
declaration: module
origin: cited
lean: OpenvmFv
statement: formalized
proof: formalized
---

# Formal verification of the OpenVM RISC-V zkVM

[openvm-org/openvm-fv](https://github.com/openvm-org/openvm-fv) at commit [7523c23a](https://github.com/openvm-org/openvm-fv/tree/7523c23a3148100a0f201b33385c0f8e01b2c858), 2026-07-15.

> This repository contains an infrastructure for formal verification of OpenVM RISC-V chips in Lean (v4.26.0), together with Lean proofs that the OpenVM implementations of all 45 of the RISC-V RV32IM opcodes satisfy their RISC-V specifications, as per the [Official Lean RISC-V specification](https://github.com/opencompl/sail-riscv-lean).

*Quoted from [README.md](https://github.com/openvm-org/openvm-fv/blob/7523c23a3148100a0f201b33385c0f8e01b2c858/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Field](../../field-theory/field.md)
- [List](../../../data-structures/list-like-structures/list.md)
- [Integer](../../numbers/integer.md)
- [Natural number](../../numbers/natural-number.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`OpenvmFv`](https://github.com/openvm-org/openvm-fv/blob/7523c23a3148100a0f201b33385c0f8e01b2c858/OpenvmFv.lean): the root of a Lean library its lakefile builds, not a theorem. No file it imports, directly or not (164 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.26.0, Mathlib at [2df2f015](https://github.com/leanprover-community/mathlib4/tree/2df2f0150c275ad53cb3c90f7c98ec15a56a1a67).
- 345 .lean files; its Lean libraries `OpenvmFv` hold 166, declaring 1,593 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE-APACHE](https://github.com/openvm-org/openvm-fv/blob/7523c23a3148100a0f201b33385c0f8e01b2c858/LICENSE-APACHE)).

## Builds on

- Mathlib, at [2df2f015](https://github.com/leanprover-community/mathlib4/tree/2df2f0150c275ad53cb3c90f7c98ec15a56a1a67).
- `LeanRV` (https://github.com/NethermindEth/sail-riscv-lean) at `a0bf6df1`.
- `LeanZKCircuit` (https://github.com/NethermindEth/leanzkcircuit.git) at `8631b11d`.

## Placement

Of its imports of Mathlib modules in an overview area, 17 of 17 are in General algebra, 2.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (17 of 17 imports, 2.8×). *Proof depends on* names 4 of the 4 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [openvm-org/openvm-fv at 7523c23a](https://github.com/openvm-org/openvm-fv/tree/7523c23a3148100a0f201b33385c0f8e01b2c858)

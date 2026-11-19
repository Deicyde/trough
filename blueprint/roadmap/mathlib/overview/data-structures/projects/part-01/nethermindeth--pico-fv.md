---
declaration: module
origin: cited
lean: PicoFV32, PicoFV64
statement: formalized
proof: formalized
---

# Formal verification of the Brevis Pico RISC-V zkVM

[NethermindEth/pico-fv](https://github.com/NethermindEth/pico-fv) at commit [a7f9a097](https://github.com/NethermindEth/pico-fv/tree/a7f9a0976e245aeef89c3f02c51ae85023207b53), 2026-06-11.

> This repository contains a Lean 4 (v4.28.0-rc1) formalisation of the Brevis Pico RISC-V zkVM and end-to-end equivalence proofs between every Pico chip's constraint system and the corresponding [Official Lean RISC-V specification](https://github.com/NethermindEth/sail-riscv-lean/tree/v4.28.0-rc1).

*Quoted from [README.md](https://github.com/NethermindEth/pico-fv/blob/a7f9a0976e245aeef89c3f02c51ae85023207b53/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Field](../../../general-algebra/field-theory/field.md)
- [List](../../list-like-structures/list.md)
- [Integer](../../../general-algebra/numbers/integer.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`PicoFV32`](https://github.com/NethermindEth/pico-fv/blob/a7f9a0976e245aeef89c3f02c51ae85023207b53/PicoFV32.lean), [`PicoFV64`](https://github.com/NethermindEth/pico-fv/blob/a7f9a0976e245aeef89c3f02c51ae85023207b53/PicoFV64.lean): the root of a Lean library its lakefile builds, not a theorem. No file they import, directly or not (272 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.28.0-rc1, Mathlib at [5352afcc](https://github.com/leanprover-community/mathlib4/tree/5352afccd6866369be9de43f5b7ec47203555f44).
- 274 .lean files; its Lean libraries `PicoFV`, `PicoFV32`, `PicoFV64` hold 274, declaring 3,106 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE-APACHE](https://github.com/NethermindEth/pico-fv/blob/a7f9a0976e245aeef89c3f02c51ae85023207b53/LICENSE-APACHE)).

## Builds on

- Mathlib, at [5352afcc](https://github.com/leanprover-community/mathlib4/tree/5352afccd6866369be9de43f5b7ec47203555f44).
- `LeanRV` (https://github.com/NethermindEth/sail-riscv-lean) at `bb1e7d45`.
- `LeanZKCircuit_Plonky3` (https://github.com/NethermindEth/LeanZKCircuit-Plonky3.git) at `d1f15357`.

## Placement

Of its imports of Mathlib modules in an overview area, 37 of 37 are in Data structures, 7.0 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (37 of 37 imports, 7.0×). *Proof depends on* names 4 of the 4 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [NethermindEth/pico-fv at a7f9a097](https://github.com/NethermindEth/pico-fv/tree/a7f9a0976e245aeef89c3f02c51ae85023207b53)

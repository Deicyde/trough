---
declaration: module
origin: cited
lean: EvmAsm
statement: formalized
proof: formalized
---

# evm-asm

*evm.asm: A Verified Macro Assembler for building zkEVM in Lean 4 (early experiment)*

[Verified-zkEVM/evm-asm](https://github.com/Verified-zkEVM/evm-asm) at commit [7e65e4d0](https://github.com/Verified-zkEVM/evm-asm/tree/7e65e4d024718f704226cd795f3d03d4e9aafe13), 2026-09-04.

> The formally verified [Pancake compiler looks promising](https://github.com/pirapira/stateless-pancaketh/tree/e86464f606c7afced09c67be058fc28147a27aa8). In light of that work, we are reconsidering the overall approach of this project. The current code and future contributions to **evm.asm** may not ultimately be used in the final implementation, so please treat ongoing work here as exploratory until the direction is settled.

*Quoted from [README.md](https://github.com/Verified-zkEVM/evm-asm/blob/7e65e4d024718f704226cd795f3d03d4e9aafe13/README.md), MIT, Copyright (c) 2026 ZkSecurity.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Euler’s Generalization of Fermat’s Little Theorem](../../../../hundred-theorems/part-01/eulers-generalization-of-fermats-little-theorem.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [List](../../list-like-structures/list.md)
- [Integer](../../../general-algebra/numbers/integer.md)
- [Array](../../list-like-structures/array.md)
- [Field](../../../general-algebra/field-theory/field.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`EvmAsm`](https://github.com/Verified-zkEVM/evm-asm/blob/7e65e4d024718f704226cd795f3d03d4e9aafe13/EvmAsm.lean): the root of a Lean library its lakefile builds, not a theorem. No file it imports, directly or not (3104 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.33.0, Mathlib at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).
- 3,120 .lean files; its Lean libraries `EvmAsm` hold 3,104, declaring 40,295 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: MIT ([LICENSE](https://github.com/Verified-zkEVM/evm-asm/blob/7e65e4d024718f704226cd795f3d03d4e9aafe13/LICENSE)).

## Builds on

- Mathlib, at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).
- `«riscv-zkvm»` (https://github.com/Verified-zkEVM/riscv-zkvm) at `afcbc45e`.

## Placement

Of its imports of Mathlib modules in an overview area, 11 of 27 are in Data structures, 2.9 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (11 of 27 imports, 2.9×), Combinatorics (3 of 27 imports, 2.6×), General algebra (13 of 27 imports, 1.4×). *Proof depends on* lists 6 of the 6 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [Verified-zkEVM/evm-asm at 7e65e4d0](https://github.com/Verified-zkEVM/evm-asm/tree/7e65e4d024718f704226cd795f3d03d4e9aafe13)

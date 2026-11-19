---
declaration: module
origin: cited
lean: MachineChecked
statement: formalized
proof: formalized
---

# MachineChecked

[Verified-zkEVM/machine-checked](https://github.com/Verified-zkEVM/machine-checked) at commit [68314c8f](https://github.com/Verified-zkEVM/machine-checked/tree/68314c8f378d3b5406da80d312e8763b66a3f033), 2026-11-17.

> Formally verify machine code directly in Lean.

*Quoted from [README.md](https://github.com/Verified-zkEVM/machine-checked/blob/68314c8f378d3b5406da80d312e8763b66a3f033/README.md), Apache-2.0.*

## Depends on

- [code-verification](../../../analysis/projects/part-01/google-deepmind--code-verification.md)

## Proof depends on

- [Fermat's little theorem](../../../../thousand-plus/number-theory/part-01/fermats-little-theorem.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [List](../../list-like-structures/list.md)
- [Array](../../list-like-structures/array.md)
- [Hash map](../../maps/hash-map.md)
- [Closure](../../../topology/general-topology/part-01/closure.md)
- [Multiset](../../sets/multiset.md)
- [Field](../../../general-algebra/field-theory/field.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`MachineChecked`](https://github.com/Verified-zkEVM/machine-checked/blob/68314c8f378d3b5406da80d312e8763b66a3f033/MachineChecked.lean): the root of a Lean library its lakefile builds, not a theorem. No file it imports, directly or not (71 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.36.0-rc2, Mathlib at [9d581dff](https://github.com/leanprover-community/mathlib4/tree/9d581dfff2e41de989072ea63abf3daf69311520).
- 1,230 .lean files; its Lean libraries `MachineChecked`, `Tools`, `Cases` hold 1,207, declaring 17,118 names, with `sorry` in 7 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/Verified-zkEVM/machine-checked/blob/68314c8f378d3b5406da80d312e8763b66a3f033/LICENSE)).

## Builds on

- Mathlib, at [9d581dff](https://github.com/leanprover-community/mathlib4/tree/9d581dfff2e41de989072ea63abf3daf69311520).
- [arm64](../../../analysis/projects/part-01/google-deepmind--code-verification.md) at `b0f729ac`.
- `Flapjack` (https://github.com/pirapira/flapjack) at `af5c59c5`.
- `Kraken` (https://github.com/AeneasVerif/kraken) at `ebd10ebd`.
- `lprog`.
- `«lprog-riscv»`.
- `«riscv-zkvm»` (https://github.com/Verified-zkEVM/riscv-zkvm) at `d81a9103`.

## Placement

Of its imports of Mathlib modules in an overview area, 21 of 51 are in Data structures, 2.9 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (21 of 51 imports, 2.9×), General algebra (23 of 51 imports, 1.3×). *Proof depends on* names 8 of the 13 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [Verified-zkEVM/machine-checked at 68314c8f](https://github.com/Verified-zkEVM/machine-checked/tree/68314c8f378d3b5406da80d312e8763b66a3f033)

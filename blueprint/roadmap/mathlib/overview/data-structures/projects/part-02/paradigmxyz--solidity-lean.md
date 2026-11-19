---
declaration: module
origin: cited
lean: SolidCore, SolidCore.Solidity.Interface.Statements
statement: formalized
---

# solidity-lean

*solidity-lean — a machine-checked Solidity semantics (SolidCore)*

[paradigmxyz/solidity-lean](https://github.com/paradigmxyz/solidity-lean) at commit [3db5032a](https://github.com/paradigmxyz/solidity-lean/tree/3db5032a35a104dec14602169aea927936f82f19), 2026-11-15.

> **SolidCore** is an executable, machine-checked semantics of Solidity written in [Lean 4](https://lean-lang.org/). It typechecks, lowers, and *runs* real single-contract Solidity programs inside Lean, and its behavior is continuously validated against the reference toolchain: **pinned `solc` 0.8.35 + the real EVM** (via [Foundry](https://github.com/foundry-rs/foundry)).

*Quoted from [README.md](https://github.com/paradigmxyz/solidity-lean/blob/3db5032a35a104dec14602169aea927936f82f19/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [List](../../list-like-structures/list.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [Integer](../../../general-algebra/numbers/integer.md)
- [Hash map](../../maps/hash-map.md)
- [Array](../../list-like-structures/array.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`SolidCore`](https://github.com/paradigmxyz/solidity-lean/blob/3db5032a35a104dec14602169aea927936f82f19/SolidCore.lean), [`SolidCore.Solidity.Interface.Statements`](https://github.com/paradigmxyz/solidity-lean/blob/3db5032a35a104dec14602169aea927936f82f19/SolidCore/Solidity/Interface/Statements.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `SolidCore/Solidity/Interface/Expressions.lean`, `SolidCore/Solidity/Interface/Foundation.lean` hold `sorry` or `admit`.

## Project

- Lean v4.28.0, Mathlib at [8f9d9cff](https://github.com/leanprover-community/mathlib4/tree/8f9d9cff6bd728b17a24e163c9402775d9e6a365).
- 231 .lean files; its Lean libraries `SolidCore`, `SolidCoreStatementLowering`, `SolidCoreWitness` hold 224, declaring 11,442 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE-APACHE](https://github.com/paradigmxyz/solidity-lean/blob/3db5032a35a104dec14602169aea927936f82f19/LICENSE-APACHE)).

## Builds on

- Mathlib, at [8f9d9cff](https://github.com/leanprover-community/mathlib4/tree/8f9d9cff6bd728b17a24e163c9402775d9e6a365).
- `evmyul` (https://github.com/danrobinson/EVMYulLean.git) at `b08573c6`.
- `«evm-interaction»` (https://github.com/danrobinson/evm-interaction.git) at `c939817c`.

## Placement

3 of the 5 Mathlib concepts its files name are in Data structures.

## Mathlib use

*Proof depends on* lists 5 of the 5 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [paradigmxyz/solidity-lean at 3db5032a](https://github.com/paradigmxyz/solidity-lean/tree/3db5032a35a104dec14602169aea927936f82f19)

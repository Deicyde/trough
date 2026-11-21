---
declaration: module
origin: cited
lean: Zcash, Zcash.CensusCheck, Zcash.Security.Ledger.BridgeTests
statement: formalized
proof: formalized
---

# Formalizing Ironwood

[zcash/ironwood](https://github.com/zcash/ironwood) at commit [ab5d90f5](https://github.com/zcash/ironwood/tree/ab5d90f510a4d1bc9833c139600caeac4dbd19dd), 2026-11-09.

> $\textsf{Ironwood}$ is a project to deploy a new shielded pool, built to restore confidence for all Zcash'rs in the supply integrity of Zcash.

*Quoted from [README.md](https://github.com/zcash/ironwood/blob/ab5d90f510a4d1bc9833c139600caeac4dbd19dd/README.md), Apache-2.0.*

## Depends on

- [Development](../../data-structures/projects/part-01/verified-zkevm--clean.md)

## Proof depends on

- [Lagrange interpolation](../../../undergraduate/numerical-analysis/approximation-of-numerical-functions/lagrange-interpolation.md)
- [Discrete law](../../probability-theory/random-variables-and-their-laws/discrete-law.md)
- [Module](../fundamentals/module.md)
- [Fermat's little theorem](../../../thousand-plus/number-theory/part-01/fermats-little-theorem.md)
- [Multiset](../../data-structures/sets/multiset.md)
- [List](../../data-structures/list-like-structures/list.md)
- [Formula for the Number of Combinations](../../../hundred-theorems/part-03/formula-for-the-number-of-combinations.md)
- [Field](../../general-algebra/field-theory/field.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Zcash`](https://github.com/zcash/ironwood/blob/ab5d90f510a4d1bc9833c139600caeac4dbd19dd/Zcash.lean), [`Zcash.CensusCheck`](https://github.com/zcash/ironwood/blob/ab5d90f510a4d1bc9833c139600caeac4dbd19dd/Zcash/CensusCheck.lean), [`Zcash.Security.Ledger.BridgeTests`](https://github.com/zcash/ironwood/blob/ab5d90f510a4d1bc9833c139600caeac4dbd19dd/Zcash/Security/Ledger/BridgeTests.lean): the root of a Lean library its lakefile builds, not a theorem. No file they import, directly or not (462 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.30.0, Mathlib at [c5ea0035](https://github.com/leanprover-community/mathlib4/tree/c5ea00351c28e24afc9f0f84379aa41082b1188f).
- 489 .lean files; its Lean libraries `Zcash`, `MetaCheck`, `FixtureCheck`, `CircuitCheck`, `SecurityCheck`, `CensusCheck` hold 489, declaring 9,438 names, with `sorry` in 0 files and 4 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE-APACHE](https://github.com/zcash/ironwood/blob/ab5d90f510a4d1bc9833c139600caeac4dbd19dd/LICENSE-APACHE)).

## Builds on

- Mathlib, at [c5ea0035](https://github.com/leanprover-community/mathlib4/tree/c5ea00351c28e24afc9f0f84379aa41082b1188f).
- [Clean](../../data-structures/projects/part-01/verified-zkevm--clean.md) at `e4f973bf`.
- `CompElliptic` (https://github.com/daira/CompElliptic) at `2c044403`.

## Placement

Of its imports of Mathlib modules in an overview area, 10 of 72 are in Linear algebra, 2.4 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Linear algebra (10 of 72 imports, 2.4×), Data structures (14 of 72 imports, 1.4×), General algebra (34 of 72 imports, 1.3×). *Proof depends on* lists 8 of the 21 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [zcash/ironwood at ab5d90f5](https://github.com/zcash/ironwood/tree/ab5d90f510a4d1bc9833c139600caeac4dbd19dd)

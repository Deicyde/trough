---
declaration: module
origin: cited
lean: Abs, AuthzSpecs, Check
statement: formalized
proof: formalized
---

# h5i

[h5i-dev/h5i](https://github.com/h5i-dev/h5i) at commit [cc54fa89](https://github.com/h5i-dev/h5i/tree/cc54fa89690c2d3c630b5ba670b30d8dbd93d88e), 2026-11-17.

> **h5i** (pronounced *high-five*) is an Axum-based Rust web framework built around application kernels that can be formally verified with Lean 4 and executed on servers, bare-metal embedded devices, and GPUs. It also provides integrated development infrastructure for red-teaming, security regression testing, and sandboxed AI agents.

*Quoted from [README.md](https://github.com/h5i-dev/h5i/blob/cc54fa89690c2d3c630b5ba670b30d8dbd93d88e/README.md), Apache-2.0.*

## Depends on

- [Aeneas](aeneasverif--aeneas.md)

## Proof depends on

- [List](../../list-like-structures/list.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [Array](../../list-like-structures/array.md)
- [Integer](../../../general-algebra/numbers/integer.md)
- [Field](../../../general-algebra/field-theory/field.md)
- [Filter](../../../topology/general-topology/part-01/filter.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Abs`](https://github.com/h5i-dev/h5i/blob/cc54fa89690c2d3c630b5ba670b30d8dbd93d88e/crates/h5i-app-pgsql/proofs/Abs.lean), [`AuthzSpecs`](https://github.com/h5i-dev/h5i/blob/cc54fa89690c2d3c630b5ba670b30d8dbd93d88e/crates/h5i-app-std/proofs/AuthzSpecs.lean), [`Check`](https://github.com/h5i-dev/h5i/blob/cc54fa89690c2d3c630b5ba670b30d8dbd93d88e/crates/h5i-app-std/proofs/Check.lean): the root of a Lean library its lakefile builds, not a theorem. No file they import, directly or not (56 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.31.0, Mathlib at [fabf563a](https://github.com/leanprover-community/mathlib4/tree/fabf563a7c95a166b8d7b6efca11c8b4dc9d911f).
- 119 .lean files; its Lean libraries `H5iAppLib`, `H5iAppStdGenerated`, `H5iAppStdProofs`, `H5iAppJsonGenerated`, `H5iAppJsonProofs`, `H5iAppTokenGenerated` and 7 more hold 56, declaring 1,948 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/h5i-dev/h5i/blob/cc54fa89690c2d3c630b5ba670b30d8dbd93d88e/LICENSE)).

## Builds on

- Mathlib, at [fabf563a](https://github.com/leanprover-community/mathlib4/tree/fabf563a7c95a166b8d7b6efca11c8b4dc9d911f).
- [aeneas](aeneasverif--aeneas.md) at `b86120db`.

## Placement

Of its imports of Mathlib modules in an overview area, 1 of 2 are in Data structures, 3.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (1 of 2 imports, 3.5×), General algebra (1 of 2 imports, 1.4×). *Proof depends on* lists 6 of the 6 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [h5i-dev/h5i at cc54fa89](https://github.com/h5i-dev/h5i/tree/cc54fa89690c2d3c630b5ba670b30d8dbd93d88e)

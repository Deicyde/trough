---
declaration: theorem
origin: cited
lean: Ix.CompileCert.UniversePipeline.TablesSound.primary
statement: formalized
proof: formalized
---

# Ix: a zero-knowledge proof-carrying code platform

[argumentcomputer/ix](https://github.com/argumentcomputer/ix) at commit [bdd4304f](https://github.com/argumentcomputer/ix/tree/bdd4304fa7db1404fd897927f1647db6ad8b300f), 2026-11-07.

> The Ix platform enables the compilation of [Lean 4](https://github.com/leanprover/lean4) programs into zero-knowledge succinct non-interactive arguments of knowledge (zk-SNARKs). This allows the execution and typechecking of any Lean program to be verified by performing a sub-100-millisecond operation against an approximately 1 kilobyte certificate, regardless of the size of the original Lean program.

*Quoted from [README.md](https://github.com/argumentcomputer/ix/blob/bdd4304fa7db1404fd897927f1647db6ad8b300f/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [Closure](../../../mathlib/overview/topology/general-topology/part-01/closure.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Distributions](../../../mathlib/overview/analysis/distribution-theory/distributions.md)
- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [Group](../../../mathlib/overview/general-algebra/group-theory/part-01/group.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Ix.CompileCert.UniversePipeline.TablesSound.primary`](https://github.com/argumentcomputer/ix/blob/bdd4304fa7db1404fd897927f1647db6ad8b300f/Ix/CompileCert/UniversePipeline.lean#L96) (theorem)

No file its headlines import, directly or not (85 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.1.
- 1,616 .lean files; its Lean libraries `MultiStark`, `Ix`, `Tests`, `EntryCaseFixtures`, `TruthMinesSpec`, `Apps` and 2 more hold 812, declaring 16,041 names, with `sorry` in 10 files and 8 axioms, read without Lean.
- Its own CI at this commit: failing.
- License: Apache-2.0 ([LICENSE-APACHE](https://github.com/argumentcomputer/ix/blob/bdd4304fa7db1404fd897927f1647db6ad8b300f/LICENSE-APACHE)).

## Builds on

- `Blake3` (https://github.com/argumentcomputer/Blake3.lean) at `3f8b8056`.
- `LSpec` (https://github.com/argumentcomputer/LSpec) at `d8eb3e0d`.
- `«ix-kernel»`.

## Placement

It requires neither Mathlib nor another library mapped here; 10 files of the project import Batteries modules.

## Mathlib use

*Proof depends on* names 8 of the 11 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [argumentcomputer/ix at bdd4304f](https://github.com/argumentcomputer/ix/tree/bdd4304fa7db1404fd897927f1647db6ad8b300f)

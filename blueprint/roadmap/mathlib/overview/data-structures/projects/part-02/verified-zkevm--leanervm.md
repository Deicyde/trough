---
declaration: theorem
origin: cited
lean: LeanerVM.Arithmetization.constraintSoundness, LeanerVM.Arithmetization.traceOf_valid, LeanerVM.Arithmetization.constraintCompleteness, LeanerVM.Arithmetization.satisfiable_iff_valid
statement: formalized
proof: formalized
---

# leanerVM

[Verified-zkEVM/leanerVM](https://github.com/Verified-zkEVM/leanerVM) at commit [4bdd4e5a](https://github.com/Verified-zkEVM/leanerVM/tree/4bdd4e5a4c6e19536508fc9b9ca4038f6d979999), 2026-11-17.

> `leanerVM` is a Lean 4 implementation and formalization of [leanVM](https://github.com/leanEthereum/leanVM), leanEthereum's minimal hash-based SNARK virtual machine for post-quantum signature aggregation. Current leanVM uses binary fields and BLAKE2s; the historical KoalaBear/Poseidon implementation remains available on its `koalabear` branch.

*Quoted from [README.md](https://github.com/Verified-zkEVM/leanerVM/blob/4bdd4e5a4c6e19536508fc9b9ca4038f6d979999/README.md), Apache-2.0.*

## Depends on

- [Development](../part-01/verified-zkevm--clean.md)

## Proof depends on

- [Lagrange interpolation](../../../../undergraduate/numerical-analysis/approximation-of-numerical-functions/lagrange-interpolation.md)
- [Roots of a polynomial](../../../general-algebra/polynomials-and-power-series/roots-of-a-polynomial.md)
- [Characteristic p](../../../general-algebra/field-theory/characteristic-p.md)
- [Hash map](../../maps/hash-map.md)
- [Array](../../list-like-structures/array.md)
- [Tree](../../trees/tree.md)
- [Rupture field](../../../general-algebra/field-theory/rupture-field.md)
- [List](../../list-like-structures/list.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`LeanerVM.Arithmetization.constraintSoundness`](https://github.com/Verified-zkEVM/leanerVM/blob/4bdd4e5a4c6e19536508fc9b9ca4038f6d979999/LeanerVM/Arithmetization/Soundness.lean#L322) (theorem)
- [`LeanerVM.Arithmetization.traceOf_valid`](https://github.com/Verified-zkEVM/leanerVM/blob/4bdd4e5a4c6e19536508fc9b9ca4038f6d979999/LeanerVM/Arithmetization/Soundness.lean#L271) (theorem)
- [`LeanerVM.Arithmetization.constraintCompleteness`](https://github.com/Verified-zkEVM/leanerVM/blob/4bdd4e5a4c6e19536508fc9b9ca4038f6d979999/LeanerVM/Arithmetization/Completeness/Theorem.lean#L402) (theorem)
- [`LeanerVM.Arithmetization.satisfiable_iff_valid`](https://github.com/Verified-zkEVM/leanerVM/blob/4bdd4e5a4c6e19536508fc9b9ca4038f6d979999/LeanerVM/Arithmetization/Equivalence.lean#L89) (theorem)

No file its headlines import, directly or not (49 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 436 .lean files; its Lean libraries `LeanerVM`, `LeanerVMTests`, `LeanerVMBench` hold 431, declaring 6,663 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/Verified-zkEVM/leanerVM/blob/4bdd4e5a4c6e19536508fc9b9ca4038f6d979999/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- `Arklib` (https://github.com/Verified-zkEVM/ArkLib) at `011391e5`.
- [Clean](../part-01/verified-zkevm--clean.md) at `6a2e7bb9`.
- `CompPoly` (https://github.com/Verified-zkEVM/CompPoly) at `e28da348`.
- `PolyFun` (https://github.com/Verified-zkEVM/PolyFun) at `d3ec3a41`.
- `VCVio` (https://github.com/Verified-zkEVM/VCVio) at `fc54dd3d`.

## Placement

Of its imports of Mathlib modules in an overview area, 22 of 78 are in Data structures, 2.0 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (22 of 78 imports, 2.0×), General algebra (49 of 78 imports, 1.8×). *Proof depends on* lists 8 of the 31 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [Verified-zkEVM/leanerVM at 4bdd4e5a](https://github.com/Verified-zkEVM/leanerVM/tree/4bdd4e5a4c6e19536508fc9b9ca4038f6d979999)

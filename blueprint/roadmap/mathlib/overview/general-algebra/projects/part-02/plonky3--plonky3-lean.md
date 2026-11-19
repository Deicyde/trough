---
declaration: module
origin: cited
lean: Blake3Crate, HaxExt, P3Air
statement: formalized
proof: formalized
---

# Plonky3-lean

[Plonky3/Plonky3-lean](https://github.com/Plonky3/Plonky3-lean) at commit [ba6bc178](https://github.com/Plonky3/Plonky3-lean/tree/ba6bc178838b324bbcbc4acdaaf10cbc7e48a2b2), 2026-10-25.

> Formal models and machine-checked proofs for [Plonky3](https://github.com/Plonky3/Plonky3), in Lean 4.

*Quoted from [README.md](https://github.com/Plonky3/Plonky3-lean/blob/ba6bc178838b324bbcbc4acdaaf10cbc7e48a2b2/README.md), MIT, Copyright (c) 2026 Plonky3.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Lagrange interpolation](../../../../undergraduate/numerical-analysis/approximation-of-numerical-functions/lagrange-interpolation.md)
- [Rupture field](../../field-theory/rupture-field.md)
- [Fermat's little theorem](../../../../thousand-plus/number-theory/part-01/fermats-little-theorem.md)
- [Roots of a polynomial](../../polynomials-and-power-series/roots-of-a-polynomial.md)
- [Order of an element](../../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Characteristic p](../../field-theory/characteristic-p.md)
- [Polynomial functions](../../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md)
- [Congruence in $\Z$](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Blake3Crate`](https://github.com/Plonky3/Plonky3-lean/blob/ba6bc178838b324bbcbc4acdaaf10cbc7e48a2b2/crates/blake3-crate/stub/Blake3Crate.lean), [`HaxExt`](https://github.com/Plonky3/Plonky3-lean/blob/ba6bc178838b324bbcbc4acdaaf10cbc7e48a2b2/HaxExt.lean), [`P3Air`](https://github.com/Plonky3/Plonky3-lean/blob/ba6bc178838b324bbcbc4acdaaf10cbc7e48a2b2/crates/air/extraction/P3Air.lean): the root of a Lean library its lakefile builds, not a theorem. No file they import, directly or not (998 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 1,058 .lean files; its Lean libraries `HaxExt`, `ToCompPoly`, `Plonky3Lean`, `P3BabyBear`, `P3Commit`, `P3Dft` and 43 more hold 1,058, declaring 16,107 names, with `sorry` in 0 files and 20 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: MIT ([LICENSE](https://github.com/Plonky3/Plonky3-lean/blob/ba6bc178838b324bbcbc4acdaaf10cbc7e48a2b2/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- `aeneas` (https://github.com/cryspen/aeneas) at `41977a5c`.
- `CompPoly` (https://github.com/Verified-zkEVM/CompPoly) at `06686e4c`.
- `hax` (https://github.com/cryspen/hax-lean) at `5da920be`.

## Placement

Of its imports of Mathlib modules in an overview area, 165 of 227 are in General algebra, 2.0 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (165 of 227 imports, 2.0×), Data structures (42 of 227 imports, 1.3×). *Proof depends on* names 8 of the 36 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [Plonky3/Plonky3-lean at ba6bc178](https://github.com/Plonky3/Plonky3-lean/tree/ba6bc178838b324bbcbc4acdaaf10cbc7e48a2b2)

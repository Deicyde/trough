---
declaration: module
origin: cited
lean: Clean, Clean.Specs.BLAKE3.ChunkProcessingTests, Clean.Test
statement: formalized
---

# Development

[Verified-zkEVM/clean](https://github.com/Verified-zkEVM/clean) at commit [71cd9a32](https://github.com/Verified-zkEVM/clean/tree/71cd9a32ce2aa35a14115fa6b7a42377c58fb602), 2026-11-13.

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Array](../../list-like-structures/array.md)
- [Characteristic of a ring](../../../general-algebra/field-theory/characteristic-of-a-ring.md)
- [Hash map](../../maps/hash-map.md)
- [List](../../list-like-structures/list.md)
- [Ring](../../../general-algebra/rings/ring.md)
- [Module](../../../linear-algebra/fundamentals/module.md)
- [Field](../../../general-algebra/field-theory/field.md)
- [Polynomial in several indeterminates](../../../general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Clean`](https://github.com/Verified-zkEVM/clean/blob/71cd9a32ce2aa35a14115fa6b7a42377c58fb602/Clean.lean), [`Clean.Specs.BLAKE3.ChunkProcessingTests`](https://github.com/Verified-zkEVM/clean/blob/71cd9a32ce2aa35a14115fa6b7a42377c58fb602/Clean/Specs/BLAKE3/ChunkProcessingTests.lean), [`Clean.Test`](https://github.com/Verified-zkEVM/clean/blob/71cd9a32ce2aa35a14115fa6b7a42377c58fb602/Clean/Test.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Clean/Utils/Test/TestCircuitProofStart.lean` holds `sorry` or `admit`.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 221 .lean files; its Lean libraries `Clean`, `CleanTests` hold 220, declaring 3,967 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: MIT ([LICENSE](https://github.com/Verified-zkEVM/clean/blob/71cd9a32ce2aa35a14115fa6b7a42377c58fb602/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- `CompPoly` (https://github.com/Verified-zkEVM/CompPoly.git) at `06686e4c`.

## Placement

Of its imports of Mathlib modules in an overview area, 11 of 39 are in Data structures, 2.0 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (11 of 39 imports, 2.0×), General algebra (22 of 39 imports, 1.6×). *Proof depends on* names 8 of the 12 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [Verified-zkEVM/clean at 71cd9a32](https://github.com/Verified-zkEVM/clean/tree/71cd9a32ce2aa35a14115fa6b7a42377c58fb602)

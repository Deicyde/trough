---
declaration: module
origin: cited
lean: Curve25519Dalek, Utils
statement: formalized
---

# curve25519-dalek-lean-verify

*Verify Dalek elliptic curve cryptography using Lean*

[Beneficial-AI-Foundation/curve25519-dalek-lean-verify](https://github.com/Beneficial-AI-Foundation/curve25519-dalek-lean-verify) at commit [52cad87d](https://github.com/Beneficial-AI-Foundation/curve25519-dalek-lean-verify/tree/52cad87d054943c96c984d99d9ea9e5d043b0d65), 2026-11-05.

> ⚠️ The latest development is now happening at https://github.com/Beneficial-AI-Foundation/curve25519-dalek-fork/ (because that's a fork and this repo isn't). When the upstreaming work is finalized this repo will be updated and then archived.

*Quoted from [README.md](https://github.com/Beneficial-AI-Foundation/curve25519-dalek-lean-verify/blob/52cad87d054943c96c984d99d9ea9e5d043b0d65/README.md), Apache-2.0.*

## Depends on

- [Aeneas](../../../data-structures/projects/part-01/aeneasverif--aeneas.md)

## Proof depends on

- [Fermat's little theorem](../../../../thousand-plus/number-theory/part-01/fermats-little-theorem.md)
- [Array](../../../data-structures/list-like-structures/array.md)
- [Invertible elements](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Characteristic of a ring](../../field-theory/characteristic-of-a-ring.md)
- [Order of an element](../../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Integer](../../numbers/integer.md)
- [Natural number](../../numbers/natural-number.md)
- [List](../../../data-structures/list-like-structures/list.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Curve25519Dalek`](https://github.com/Beneficial-AI-Foundation/curve25519-dalek-lean-verify/blob/52cad87d054943c96c984d99d9ea9e5d043b0d65/Curve25519Dalek.lean), [`Utils`](https://github.com/Beneficial-AI-Foundation/curve25519-dalek-lean-verify/blob/52cad87d054943c96c984d99d9ea9e5d043b0d65/Utils.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Curve25519Dalek/Math/Edwards/Curve.lean`, `Curve25519Dalek/Math/Ristretto/Representation.lean`, `Curve25519Dalek/Specs/Montgomery/MontgomeryPoint/Mul.lean`, `Utils/Lib/Analysis.lean` hold `sorry` or `admit`.

## Project

- Lean v4.31.0, Mathlib at [fabf563a](https://github.com/leanprover-community/mathlib4/tree/fabf563a7c95a166b8d7b6efca11c8b4dc9d911f).
- 244 .lean files; its Lean libraries `Curve25519Dalek`, `Utils`, `Tests` hold 244, declaring 1,450 names, with `sorry` in 4 files and 18 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/Beneficial-AI-Foundation/curve25519-dalek-lean-verify/blob/52cad87d054943c96c984d99d9ea9e5d043b0d65/LICENSE)).

## Builds on

- Mathlib, at [fabf563a](https://github.com/leanprover-community/mathlib4/tree/fabf563a7c95a166b8d7b6efca11c8b4dc9d911f).
- [aeneas](../../../data-structures/projects/part-01/aeneasverif--aeneas.md) at `6e167c9b`.
- `PrimeCert` (https://github.com/b-mehta/PrimeCert.git) at `f699a3e5`.

## Placement

Of its imports of Mathlib modules in an overview area, 18 of 21 are in General algebra, 2.4 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (18 of 21 imports, 2.4×). *Proof depends on* names 8 of the 9 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [Beneficial-AI-Foundation/curve25519-dalek-lean-verify at 52cad87d](https://github.com/Beneficial-AI-Foundation/curve25519-dalek-lean-verify/tree/52cad87d054943c96c984d99d9ea9e5d043b0d65)

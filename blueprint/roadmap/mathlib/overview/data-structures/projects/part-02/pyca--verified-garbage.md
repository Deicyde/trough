---
declaration: module
origin: cited
lean: VerifiedGarbage.Impl.AArch64Instrs, VerifiedGarbage.Impl.NatPairs, VerifiedGarbage.Impl.Scrub.X86_64
statement: formalized
---

# Verified Garbage

[pyca/verified-garbage](https://github.com/pyca/verified-garbage) at commit [5ee6568f](https://github.com/pyca/verified-garbage/tree/5ee6568fdfb7a61cd44738810ea7ae644662a279), 2026-11-18.

> Verified Garbage is an experimental cryptography library, implemented entirely by LLMs. All of the cryptography primitives are formally verified using Lean.

*Quoted from [README.md](https://github.com/pyca/verified-garbage/blob/5ee6568fdfb7a61cd44738810ea7ae644662a279/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [List](../../list-like-structures/list.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [Integer](../../../general-algebra/numbers/integer.md)
- [Cross product](../../../../undergraduate/bilinear-and-quadratic-forms-over-a-vector-space/low-dimensions/cross-product.md)
- [Field](../../../general-algebra/field-theory/field.md)
- [Group](../../../general-algebra/group-theory/part-01/group.md)
- [Array](../../list-like-structures/array.md)
- [Polynomial in one indeterminate](../../../general-algebra/polynomials-and-power-series/polynomial-in-one-indeterminate.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`VerifiedGarbage.Impl.AArch64Instrs`](https://github.com/pyca/verified-garbage/blob/5ee6568fdfb7a61cd44738810ea7ae644662a279/lean/VerifiedGarbage/Impl/AArch64Instrs.lean), [`VerifiedGarbage.Impl.NatPairs`](https://github.com/pyca/verified-garbage/blob/5ee6568fdfb7a61cd44738810ea7ae644662a279/lean/VerifiedGarbage/Impl/NatPairs.lean), [`VerifiedGarbage.Impl.Scrub.X86_64`](https://github.com/pyca/verified-garbage/blob/5ee6568fdfb7a61cd44738810ea7ae644662a279/lean/VerifiedGarbage/Impl/Scrub/X86_64.lean): the root of a Lean library its lakefile builds, not a theorem. Not every file of the project was read.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 21,807 .lean files; its Lean libraries `VerifiedGarbage`, `VerifiedGarbageTest`, `NativeSpec`, `NativeTactics`, `NativeAuditRecords`, `NativeTCB` and 10 more hold 5,000 (the first read), declaring 73,579 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE.APACHE](https://github.com/pyca/verified-garbage/blob/5ee6568fdfb7a61cd44738810ea7ae644662a279/LICENSE.APACHE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

Of its imports of Mathlib modules in an overview area, 117 of 239 are in Data structures, 3.4 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (117 of 239 imports, 3.4×), General algebra (122 of 239 imports, 1.4×). *Proof depends on* names 8 of the 8 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [pyca/verified-garbage at 5ee6568f](https://github.com/pyca/verified-garbage/tree/5ee6568fdfb7a61cd44738810ea7ae644662a279)

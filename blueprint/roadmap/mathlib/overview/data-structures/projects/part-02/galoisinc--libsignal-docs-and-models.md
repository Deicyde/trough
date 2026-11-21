---
declaration: module
origin: cited
lean: Book, PQXDH, PQXDHDocs
statement: formalized
---

# LibSignal Documentation

[GaloisInc/libsignal-docs-and-models](https://github.com/GaloisInc/libsignal-docs-and-models) at commit [e82e566f](https://github.com/GaloisInc/libsignal-docs-and-models/tree/e82e566ff4f1db69b2638c5813249a4d4497b14f), 2026-08-12.

## Depends on

- [Aeneas](../part-01/aeneasverif--aeneas.md)

## Proof depends on

- [Module](../../../linear-algebra/fundamentals/module.md)
- [Representation](../../../general-algebra/representation-theory/representation.md)
- [Array](../../list-like-structures/array.md)
- [Field](../../../general-algebra/field-theory/field.md)
- [List](../../list-like-structures/list.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [Set](../../sets/set.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Book`](https://github.com/GaloisInc/libsignal-docs-and-models/blob/e82e566ff4f1db69b2638c5813249a4d4497b14f/docs/annotated/Book.lean), [`PQXDH`](https://github.com/GaloisInc/libsignal-docs-and-models/blob/e82e566ff4f1db69b2638c5813249a4d4497b14f/PQXDH.lean), [`PQXDHDocs`](https://github.com/GaloisInc/libsignal-docs-and-models/blob/e82e566ff4f1db69b2638c5813249a4d4497b14f/docs/PQXDHDocs.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `PQXDH/Aeneas/Full/UAKE/Assumptions.lean`, `PQXDH/Aeneas/Simplified/UAKE/Assumptions.lean`, `PQXDH/Spec/UAKE/SecurityLemmas/DHHops.lean`, `PQXDH/Spec/UAKE/SecurityLemmas/PQHops.lean`, `PQXDH/Spec/UAKE/SecurityLemmas/SharedHops.lean`, `ToVCVio/CryptoFoundations/AEAD.lean`, `docs/PQXDHDocs/Chapters/Aeneas/Defs.lean` hold `sorry` or `admit`.

## Project

- Lean v4.30.0, Mathlib at [c5ea0035](https://github.com/leanprover-community/mathlib4/tree/c5ea00351c28e24afc9f0f84379aa41082b1188f).
- 109 .lean files; its Lean libraries `ToVCVio`, `PQXDH`, `PQXDHDocs`, `Book` hold 107, declaring 1,668 names, with `sorry` in 7 files and 349 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/GaloisInc/libsignal-docs-and-models/blob/e82e566ff4f1db69b2638c5813249a4d4497b14f/LICENSE)).

## Builds on

- Mathlib, at [c5ea0035](https://github.com/leanprover-community/mathlib4/tree/c5ea00351c28e24afc9f0f84379aa41082b1188f).
- [aeneas](../part-01/aeneasverif--aeneas.md) at `45061fa1`.
- `VCVio` (https://github.com/Verified-zkEVM/VCV-io) at `8f5dc4f2`.

## Placement

Of its imports of Mathlib modules in an overview area, 1 of 1 are in Data structures, 7.0 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (1 of 1 imports, 7.0×). *Proof depends on* lists 7 of the 7 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [GaloisInc/libsignal-docs-and-models at e82e566f](https://github.com/GaloisInc/libsignal-docs-and-models/tree/e82e566ff4f1db69b2638c5813249a4d4497b14f)

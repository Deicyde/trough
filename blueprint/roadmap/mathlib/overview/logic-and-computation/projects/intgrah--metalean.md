---
declaration: module
origin: cited
lean: Metalean
statement: formalized
---

# metalean

[intgrah/metalean](https://github.com/intgrah/metalean) at commit [017c4e32](https://github.com/intgrah/metalean/tree/017c4e329c82b28d41f7cb536e74fb1ac3e1e5f6), 2026-10-31.

> Verified typechecker for idealised type theory of Lean.

*Quoted from [README.md](https://github.com/intgrah/metalean/blob/017c4e329c82b28d41f7cb536e74fb1ac3e1e5f6/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Kleene fixed-point theorem](../../../thousand-plus/combinatorics-and-ordered-structures/06-order-lattices-ordered-algebraic-structures/kleene-fixed-point-theorem.md)
- [W type](../../data-structures/trees/w-type.md)
- [Natural transformation](../../general-algebra/category-theory/natural-transformation.md)
- [Model of ZFC](../set-theory/model-of-zfc.md)
- [Yoneda embedding](../../general-algebra/category-theory/yoneda-embedding.md)
- [Cardinal](../set-theory/cardinals/cardinal.md)
- [Small category](../../general-algebra/category-theory/small-category.md)
- [Functor](../../general-algebra/category-theory/functor.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`Metalean`](https://github.com/intgrah/metalean/blob/017c4e329c82b28d41f7cb536e74fb1ac3e1e5f6/Metalean.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `Metalean/Syntax/Inductive/Ctor.lean` holds `sorry` or `admit`.

## Project

- Lean v4.36.0-rc2, Mathlib at [9d581dff](https://github.com/leanprover-community/mathlib4/tree/9d581dfff2e41de989072ea63abf3daf69311520).
- 287 .lean files; its Lean libraries `Metalean` hold 286, declaring 4,945 names, with `sorry` in 1 file and 1 axiom, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/intgrah/metalean/blob/017c4e329c82b28d41f7cb536e74fb1ac3e1e5f6/LICENSE)).

## Builds on

- Mathlib, at [9d581dff](https://github.com/leanprover-community/mathlib4/tree/9d581dfff2e41de989072ea63abf3daf69311520).

## Placement

Of its imports of Mathlib modules in an overview area, 9 of 85 are in Logic and computation, 9.9 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Logic and computation (9 of 85 imports, 9.9×), Topology (26 of 85 imports, 4.1×), General algebra (40 of 85 imports, 1.3×). *Proof depends on* lists 8 of the 19 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [intgrah/metalean at 017c4e32](https://github.com/intgrah/metalean/tree/017c4e329c82b28d41f7cb536e74fb1ac3e1e5f6)

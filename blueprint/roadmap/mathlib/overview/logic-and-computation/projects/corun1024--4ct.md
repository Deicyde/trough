---
declaration: theorem
origin: cited
lean: FourColor.fourColorTheorem, FourColor.isOpenRegion_iff, FourColor.regionClosure_eq, FourColor.isConnectedRegion_iff_isPreconnected, FourColor.simpleMap_iff, FourColor.Hypermap.Scycle.simple
statement: formalized
proof: formalized
---

# The Four Colour Theorem in Lean 4

[corun1024/4ct](https://github.com/corun1024/4ct) at commit [3db71e0a](https://github.com/corun1024/4ct/tree/3db71e0a786a1f19be04c5266fe3d06fed216885), 2026-09-16.

> A complete formalisation of the Four Colour Theorem in Lean 4 and Mathlib, following the architecture of Georges Gonthier and Benjamin Werner's Coq proof ([rocq-community/fourcolor](https://github.com/rocq-community/fourcolor)).

*Quoted from [README.md](https://github.com/corun1024/4ct/blob/3db71e0a786a1f19be04c5266fe3d06fed216885/README.md), MIT, Copyright (c) 2026 Chris Emery.*

## Depends on

- [Closure](../../topology/general-topology/part-01/closure.md)
- [List](../../data-structures/list-like-structures/list.md)

## Proof depends on

- [Fixed points](../../dynamics/general-theory/fixed-points.md)
- [Periodic points](../../dynamics/general-theory/periodic-points.md)
- [Finite](../../combinatorics/pigeonhole-principles/finite.md)
- [Signature](../../../undergraduate/group-theory/permutation-group/signature.md)
- [Permutation group of a type](../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Order of an element](../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md)
- [Ring](../../general-algebra/rings/ring.md)
- [Group](../../general-algebra/group-theory/part-01/group.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`FourColor.fourColorTheorem`](https://github.com/corun1024/4ct/blob/3db71e0a786a1f19be04c5266fe3d06fed216885/FourColor/Complete.lean#L43) (theorem)
- [`FourColor.isOpenRegion_iff`](https://github.com/corun1024/4ct/blob/3db71e0a786a1f19be04c5266fe3d06fed216885/FourColor/RealPlane.lean#L87) (theorem)
- [`FourColor.regionClosure_eq`](https://github.com/corun1024/4ct/blob/3db71e0a786a1f19be04c5266fe3d06fed216885/FourColor/RealPlane.lean#L104) (theorem)
- [`FourColor.isConnectedRegion_iff_isPreconnected`](https://github.com/corun1024/4ct/blob/3db71e0a786a1f19be04c5266fe3d06fed216885/FourColor/RealPlaneMathlib.lean#L37) (theorem)
- [`FourColor.simpleMap_iff`](https://github.com/corun1024/4ct/blob/3db71e0a786a1f19be04c5266fe3d06fed216885/FourColor/RealPlaneMathlib.lean#L51) (theorem)
- [`FourColor.Hypermap.Scycle.simple`](https://github.com/corun1024/4ct/blob/3db71e0a786a1f19be04c5266fe3d06fed216885/FourColor/Geometry.lean#L664) (theorem)

No file its headlines import, directly or not (467 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.0-rc2, Mathlib at [141f6b64](https://github.com/leanprover-community/mathlib4/tree/141f6b6455959bfeb0b2a6b04118031191d62683).
- 498 .lean files; its Lean libraries `FourColor` hold 496, declaring 64,434 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: MIT ([LICENSE](https://github.com/corun1024/4ct/blob/3db71e0a786a1f19be04c5266fe3d06fed216885/LICENSE)).

## Builds on

- Mathlib, at [141f6b64](https://github.com/leanprover-community/mathlib4/tree/141f6b6455959bfeb0b2a6b04118031191d62683).

## Placement

Of its imports of Mathlib modules in an overview area, 5 of 34 are in Logic and computation, 13.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Logic and computation (5 of 34 imports, 13.8×), Topology (7 of 34 imports, 2.8×), General algebra (13 of 34 imports, 1.1×). *Proof depends on* lists 8 of the 14 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [corun1024/4ct at 3db71e0a](https://github.com/corun1024/4ct/tree/3db71e0a786a1f19be04c5266fe3d06fed216885)

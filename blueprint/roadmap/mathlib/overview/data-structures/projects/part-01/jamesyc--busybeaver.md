---
declaration: module
origin: cited
lean: ExactCore, FixActualBridge, FixTemplateBridge
statement: formalized
---

# BusyBeaver

*Nonhalting and PA-independence for a 196-state Turing machine*

[jamesyc/BusyBeaver](https://github.com/jamesyc/BusyBeaver) at commit [407cdc35](https://github.com/jamesyc/BusyBeaver/tree/407cdc356f6b586635e71ac92be394255f4bfea4), 2026-11-12.

> PA196 is an explicit binary Turing machine that searches for a contradiction in ordinary first-order Peano arithmetic (PA). Lean 4 proves that it runs forever from a blank tape and that PA proves neither its exact arithmetic halting sentence nor its negation.

*Quoted from [README.md](https://github.com/jamesyc/BusyBeaver/blob/407cdc356f6b586635e71ac92be394255f4bfea4/README.md), MIT, Copyright (c) 2026 James Chang.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Ordinal](../../../logic-and-computation/set-theory/ordinals/ordinal.md)
- [Language](../../../logic-and-computation/formal-languages/language.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [List](../../list-like-structures/list.md)
- [Multiset](../../sets/multiset.md)
- [Array](../../list-like-structures/array.md)
- [Closure](../../../topology/general-topology/part-01/closure.md)
- [Integer](../../../general-algebra/numbers/integer.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`ExactCore`](https://github.com/jamesyc/BusyBeaver/blob/407cdc356f6b586635e71ac92be394255f4bfea4/ExactCore.lean), [`FixActualBridge`](https://github.com/jamesyc/BusyBeaver/blob/407cdc356f6b586635e71ac92be394255f4bfea4/FixActualBridge.lean), [`FixTemplateBridge`](https://github.com/jamesyc/BusyBeaver/blob/407cdc356f6b586635e71ac92be394255f4bfea4/FixTemplateBridge.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Challenge.lean` holds `sorry` or `admit`.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 2,113 .lean files; its Lean libraries `M6`, `M6PA`, `Challenge`, `PA196Bridge`, `PA196` hold 1,968, declaring 11,801 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: MIT ([LICENSE](https://github.com/jamesyc/BusyBeaver/blob/407cdc356f6b586635e71ac92be394255f4bfea4/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- `Foundation`.

## Placement

Of its imports of Mathlib modules in an overview area, 4 of 4 are in Data structures, 7.0 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (4 of 4 imports, 7.0×). *Proof depends on* lists 8 of the 9 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [jamesyc/BusyBeaver at 407cdc35](https://github.com/jamesyc/BusyBeaver/tree/407cdc356f6b586635e71ac92be394255f4bfea4)

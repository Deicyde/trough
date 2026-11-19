---
declaration: module
origin: cited
lean: YesMetaZFC
statement: formalized
---

# BMS 良序性证明的 Lean 形式化

[EgoFakeFantasy/BMS-Well-Ordering-Lean](https://github.com/EgoFakeFantasy/BMS-Well-Ordering-Lean) at commit [3a4a945f](https://github.com/EgoFakeFantasy/BMS-Well-Ordering-Lean/tree/3a4a945fd8dfc32e608189aa1d70d7e42912d353), 2026-10-28.

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)
- [Ordinal](../../../mathlib/overview/logic-and-computation/set-theory/ordinals/ordinal.md)
- [Closure](../../../mathlib/overview/topology/general-topology/part-01/closure.md)
- [Set](../../../mathlib/overview/data-structures/sets/set.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`YesMetaZFC`](https://github.com/EgoFakeFantasy/BMS-Well-Ordering-Lean/blob/3a4a945fd8dfc32e608189aa1d70d7e42912d353/YesMetaZFC.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `YesMetaZFC/Automation/HostFirstOrder/Backend.lean`, `YesMetaZFC/Automation/HostHigherOrder.lean`, `YesMetaZFC/Automation/HostRules/Backend.lean`, `YesMetaZFC/Automation/Request.lean`, `YesMetaZFC/SetTheory/Automation/Context.lean` hold `sorry` or `admit`.

## Project

- Lean v4.33.1.
- 3,229 .lean files; its Lean libraries `YesMetaZFC` hold 834, declaring 13,490 names, with `sorry` in 6 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/EgoFakeFantasy/BMS-Well-Ordering-Lean/blob/3a4a945fd8dfc32e608189aa1d70d7e42912d353/LICENSE)).

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core alone.

## Mathlib use

*Proof depends on* names 7 of the 7 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [EgoFakeFantasy/BMS-Well-Ordering-Lean at 3a4a945f](https://github.com/EgoFakeFantasy/BMS-Well-Ordering-Lean/tree/3a4a945fd8dfc32e608189aa1d70d7e42912d353)

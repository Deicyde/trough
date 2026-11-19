---
declaration: module
origin: cited
lean: AbsAssumedTests, AccountGuarantees, AsmTimeout
statement: formalized
---

# qedsvm

[QEDGen/qedsvm](https://github.com/QEDGen/qedsvm) at commit [89885959](https://github.com/QEDGen/qedsvm/tree/898859599c83c436365c10ae1b0802ede014ca5b), 2026-11-06.

> **Verify what runs on Solana, not what you wrote.**

*Quoted from [README.md](https://github.com/QEDGen/qedsvm/blob/898859599c83c436365c10ae1b0802ede014ca5b/README.md), MIT, Copyright (c) 2025 QEDGen.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`AbsAssumedTests`](https://github.com/QEDGen/qedsvm/blob/898859599c83c436365c10ae1b0802ede014ca5b/examples/lean/AbsAssumedTests.lean), [`AccountGuarantees`](https://github.com/QEDGen/qedsvm/blob/898859599c83c436365c10ae1b0802ede014ca5b/examples/lean/AccountGuarantees.lean), [`AsmTimeout`](https://github.com/QEDGen/qedsvm/blob/898859599c83c436365c10ae1b0802ede014ca5b/examples/lean/AsmTimeout.lean): the root of a Lean library its lakefile builds, not a theorem. The files they import declare 19 axioms.

## Project

- Lean v4.30.0.
- 366 .lean files; its Lean libraries `SVM`, `ExamplesCpi`, `Examples` hold 235, declaring 3,514 names, with `sorry` in 0 files and 19 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: MIT ([LICENSE](https://github.com/QEDGen/qedsvm/blob/898859599c83c436365c10ae1b0802ede014ca5b/LICENSE)).

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core alone.

## Mathlib use

*Proof depends on* names 5 of the 5 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [QEDGen/qedsvm at 89885959](https://github.com/QEDGen/qedsvm/tree/898859599c83c436365c10ae1b0802ede014ca5b)

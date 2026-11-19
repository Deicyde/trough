---
declaration: module
origin: cited
lean: Lynx, LynxTest
statement: formalized
---

# LYNX

[josevalim/lynx](https://github.com/josevalim/lynx) at commit [99a6db76](https://github.com/josevalim/lynx/tree/99a6db764c154207cf3b28c35409d9b56c463357), 2026-11-16.

> Write proofs about Erlang/Elixir programs using Lean.

*Quoted from [README.md](https://github.com/josevalim/lynx/blob/99a6db764c154207cf3b28c35409d9b56c463357/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Rational number](../../../mathlib/overview/general-algebra/numbers/rational-number.md)
- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Lynx`](https://github.com/josevalim/lynx/blob/99a6db764c154207cf3b28c35409d9b56c463357/Lean/Lynx.lean), [`LynxTest`](https://github.com/josevalim/lynx/blob/99a6db764c154207cf3b28c35409d9b56c463357/Lean/LynxTest.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Lean/LynxTest/Counterexample.lean` holds `sorry` or `admit`.

## Project

- Lean toolchain not given.
- 276 .lean files; its Lean libraries `Lynx`, `LynxTest` hold 65, declaring 1,359 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/josevalim/lynx/blob/99a6db764c154207cf3b28c35409d9b56c463357/LICENSE)).

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core alone.

## Mathlib use

*Proof depends on* names 6 of the 6 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [josevalim/lynx at 99a6db76](https://github.com/josevalim/lynx/tree/99a6db764c154207cf3b28c35409d9b56c463357)

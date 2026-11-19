---
declaration: module
origin: cited
lean: CIL, CIL.Observe, Tests.AggregateArrayStorage
statement: formalized
---

# LeanCIL: Formal Verification for .NET

[NethermindEth/LeanCIL](https://github.com/NethermindEth/LeanCIL) at commit [27953edb](https://github.com/NethermindEth/LeanCIL/tree/27953edb6f415d81362dda7e99c461ce73ff097c), 2026-11-13.

> LeanCIL uses Lean 4 to prove properties of compiled .NET code. It extracts Common Intermediate Language (CIL) from assemblies written in C#, F# and other .NET languages, then checks proofs against an explicit model of those instructions.

*Quoted from [README.md](https://github.com/NethermindEth/LeanCIL/blob/27953edb6f415d81362dda7e99c461ce73ff097c/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`CIL`](https://github.com/NethermindEth/LeanCIL/blob/27953edb6f415d81362dda7e99c461ce73ff097c/CIL.lean), [`CIL.Observe`](https://github.com/NethermindEth/LeanCIL/blob/27953edb6f415d81362dda7e99c461ce73ff097c/CIL/Observe.lean), [`Tests.AggregateArrayStorage`](https://github.com/NethermindEth/LeanCIL/blob/27953edb6f415d81362dda7e99c461ce73ff097c/Tests/AggregateArrayStorage.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `CIL/Interface/Closure.lean`, `CIL/Observe.lean` hold `sorry` or `admit`.

## Project

- Lean v4.35.0.
- 588 .lean files; its Lean libraries `CIL`, `LeanCILEditor`, `Tests.Support`, `Tests.Semantics`, `Tests.LiteralDisplay`, `Tests.Automation` and 97 more hold 436, declaring 5,999 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE-APACHE](https://github.com/NethermindEth/LeanCIL/blob/27953edb6f415d81362dda7e99c461ce73ff097c/LICENSE-APACHE)).

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core alone.

## Mathlib use

*Proof depends on* names 5 of the 5 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [NethermindEth/LeanCIL at 27953edb](https://github.com/NethermindEth/LeanCIL/tree/27953edb6f415d81362dda7e99c461ce73ff097c)

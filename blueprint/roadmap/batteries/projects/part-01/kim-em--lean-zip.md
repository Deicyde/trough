---
declaration: module
origin: cited
lean: Zip, ZipTest
statement: formalized
proof: formalized
---

# lean-zip

[kim-em/lean-zip](https://github.com/kim-em/lean-zip) at commit [2f7a63f3](https://github.com/kim-em/lean-zip/tree/2f7a63f38195bc667a926881b55d10c9f8a88eeb), 2026-09-23.

> **A formally verified DEFLATE implementation in Lean 4.**

*Quoted from [README.md](https://github.com/kim-em/lean-zip/blob/2f7a63f38195bc667a926881b55d10c9f8a88eeb/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Zip`](https://github.com/kim-em/lean-zip/blob/2f7a63f38195bc667a926881b55d10c9f8a88eeb/Zip.lean), [`ZipTest`](https://github.com/kim-em/lean-zip/blob/2f7a63f38195bc667a926881b55d10c9f8a88eeb/ZipTest.lean): the root of a Lean library its lakefile builds, not a theorem. No file they import, directly or not (98 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc2.
- 112 .lean files; its Lean libraries `Zip`, `ZipTest` hold 98, declaring 2,113 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/kim-em/lean-zip/blob/2f7a63f38195bc667a926881b55d10c9f8a88eeb/LICENSE)).

## Builds on

- `zipCommon` (https://github.com/kim-em/lean-zip-common) at `a9ffa91f`.

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core and packages not mapped here.

## Mathlib use

*Proof depends on* lists 3 of the 3 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import. It requires no Mathlib, so only the articles whose Lean names Lean core or Std declares are kept.

## Sources

- [kim-em/lean-zip at 2f7a63f3](https://github.com/kim-em/lean-zip/tree/2f7a63f38195bc667a926881b55d10c9f8a88eeb)

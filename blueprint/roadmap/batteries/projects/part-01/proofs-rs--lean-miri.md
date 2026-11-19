---
declaration: module
origin: cited
lean: Miri, MiriTests, NativeStdioHost
statement: formalized
---

# lean-miri

[proofs-rs/lean-miri](https://github.com/proofs-rs/lean-miri) at commit [b7881385](https://github.com/proofs-rs/lean-miri/tree/b78813856467c99d8cb9e47d6f7ba6fae2dc1973), 2026-11-18.

> A port of [Miri](https://github.com/rust-lang/miri), Rust's undefined-behavior checker, to Lean 4. The goal is to prove that Rust programs are free of undefined behavior under Miri's execution model.

*Quoted from [README.md](https://github.com/proofs-rs/lean-miri/blob/b78813856467c99d8cb9e47d6f7ba6fae2dc1973/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Miri`](https://github.com/proofs-rs/lean-miri/blob/b78813856467c99d8cb9e47d6f7ba6fae2dc1973/Miri.lean), [`MiriTests`](https://github.com/proofs-rs/lean-miri/blob/b78813856467c99d8cb9e47d6f7ba6fae2dc1973/MiriTests.lean), [`NativeStdioHost`](https://github.com/proofs-rs/lean-miri/blob/b78813856467c99d8cb9e47d6f7ba6fae2dc1973/tools/NativeStdioHost.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Miri/DataStructures/DedupRangeMap.lean`, `Miri/DataStructures/RangeObjectMap.lean`, `Miri/Memory/AllocAddresses/AddressGenerator.lean` hold `sorry` or `admit`.

## Project

- Lean v4.35.0.
- 1,227 .lean files; its Lean libraries `NativeRunnerSupport`, `Miri`, `MiriTests` hold 743, declaring 7,237 names, with `sorry` in 3 files and 0 axioms, read without Lean.
- Its own CI at this commit: pending.
- License: Apache-2.0 ([LICENSE-APACHE](https://github.com/proofs-rs/lean-miri/blob/b78813856467c99d8cb9e47d6f7ba6fae2dc1973/LICENSE-APACHE)).

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core alone.

## Mathlib use

*Proof depends on* lists 5 of the 5 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import. It requires no Mathlib, so only the articles whose Lean names Lean core or Std declares are kept.

## Sources

- [proofs-rs/lean-miri at b7881385](https://github.com/proofs-rs/lean-miri/tree/b78813856467c99d8cb9e47d6f7ba6fae2dc1973)

---
declaration: module
origin: cited
lean: AWSLCELFTests, Arm, Benchmarks
statement: formalized
---

# LNSym: Native Code Symbolic Simulator in Lean

[leanprover/LNSym](https://github.com/leanprover/LNSym) at commit [49f8a1d9](https://github.com/leanprover/LNSym/tree/49f8a1d9e46f8dcfc345f4bc15d35b0ba845ff5c), 2026-11-06.

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`AWSLCELFTests`](https://github.com/leanprover/LNSym/blob/49f8a1d9e46f8dcfc345f4bc15d35b0ba845ff5c/AWSLCELFTests.lean), [`Arm`](https://github.com/leanprover/LNSym/blob/49f8a1d9e46f8dcfc345f4bc15d35b0ba845ff5c/Arm.lean), [`Benchmarks`](https://github.com/leanprover/LNSym/blob/49f8a1d9e46f8dcfc345f4bc15d35b0ba845ff5c/Benchmarks.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Benchmarks/SHA512_150.lean`, `Benchmarks/SHA512_150_noKernel_noLint.lean`, `Benchmarks/SHA512_225.lean`, `Benchmarks/SHA512_225_noKernel_noLint.lean`, `Benchmarks/SHA512_400.lean`, `Benchmarks/SHA512_400_noKernel_noLint.lean`, `Benchmarks/SHA512_75.lean`, `Benchmarks/SHA512_75_noKernel_noLint.lean` hold `sorry` or `admit`.

## Project

- Lean v4.35.0.
- 201 .lean files; its Lean libraries `Arm`, `Correctness`, `Specs`, `Tests`, `AWSLCELFTests`, `Proofs` and 3 more hold 200, declaring 2,056 names, with `sorry` in 23 files and 1 axiom, read without Lean.
- Its own CI at this commit: passing.
- License files: `LICENSE`; facts only.

## Builds on

- `ELFSage` (https://github.com/shigoel/ELFSage.git) at `5820b10f`.

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core and packages not mapped here.

## Mathlib use

*Proof depends on* names 5 of the 5 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [leanprover/LNSym at 49f8a1d9](https://github.com/leanprover/LNSym/tree/49f8a1d9e46f8dcfc345f4bc15d35b0ba845ff5c)

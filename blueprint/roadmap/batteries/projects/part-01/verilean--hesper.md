---
declaration: module
origin: cited
lean: Hesper
statement: formalized
---

# Hesper

[Verilean/hesper](https://github.com/Verilean/hesper) at commit [38fba720](https://github.com/Verilean/hesper/tree/38fba72000a0d39a0421c5911378df9d28f6aca9), 2026-08-30.

> **Write GPU programs in Lean 4. Prove them correct. Run on WebGPU or CUDA.**

*Quoted from [README.md](https://github.com/Verilean/hesper/blob/38fba72000a0d39a0421c5911378df9d28f6aca9/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`Hesper`](https://github.com/Verilean/hesper/blob/38fba72000a0d39a0421c5911378df9d28f6aca9/Hesper.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `Hesper/Inference/Sampling.lean` holds `sorry` or `admit`.

## Project

- Lean v4.28.0.
- 441 .lean files; its Lean libraries `Hesper` hold 174, declaring 2,270 names, with `sorry` in 1 file and 2 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/Verilean/hesper/blob/38fba72000a0d39a0421c5911378df9d28f6aca9/LICENSE)).

## Builds on

- `LSpec` (https://github.com/argumentcomputer/LSpec.git) at `fdf848d6`.

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core and packages not mapped here.

## Mathlib use

*Proof depends on* lists 5 of the 5 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import. It requires no Mathlib, so only the articles whose Lean names Lean core or Std declares are kept.

## Sources

- [Verilean/hesper at 38fba720](https://github.com/Verilean/hesper/tree/38fba72000a0d39a0421c5911378df9d28f6aca9)

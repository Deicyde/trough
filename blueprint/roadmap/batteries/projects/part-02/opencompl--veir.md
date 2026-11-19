---
declaration: module
origin: cited
lean: Veir
statement: formalized
---

# Verified Intermediate Representation

[opencompl/veir](https://github.com/opencompl/veir) at commit [6d939bcb](https://github.com/opencompl/veir/tree/6d939bcb034bfd5ef2bb42b00de18423dc813028), 2026-11-17.

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Hash map](../../../mathlib/overview/data-structures/maps/hash-map.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)
- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [Rational number](../../../mathlib/overview/general-algebra/numbers/rational-number.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`Veir`](https://github.com/opencompl/veir/blob/6d939bcb034bfd5ef2bb42b00de18423dc813028/Veir.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `UnitTest/CTreePuddle.lean`, `Veir/Benchmarks.lean`, `Veir/Parser/Lexer.lean`, `Veir/Rewriter/InlineBlock.lean`, `Veir/Rewriter/WellFormed/Operation.lean`, `Veir/Rewriter/WellFormed/Value.lean` hold `sorry` or `admit`.

## Project

- Lean v4.35.0-rc4.
- 445 .lean files; its Lean libraries `Veir`, `UnitTest` hold 374, declaring 10,114 names, with `sorry` in 7 files and 8 axioms, read without Lean.
- Its own CI at this commit: pending.
- License files: `LICENSE`; facts only.

## Builds on

- `ExArray`.
- `«lean-ctrees»`.

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core and packages not mapped here.

## Mathlib use

*Proof depends on* lists 6 of the 6 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import. It requires no Mathlib, so only the articles whose Lean names Lean core or Std declares are kept.

## Sources

- [opencompl/veir at 6d939bcb](https://github.com/opencompl/veir/tree/6d939bcb034bfd5ef2bb42b00de18423dc813028)

---
declaration: module
origin: cited
lean: Lampe
statement: formalized
---

# Lampe

[reilabs/lampe](https://github.com/reilabs/lampe) at commit [3d7668f7](https://github.com/reilabs/lampe/tree/3d7668f749711083425e1905d4dd1850c0b39f52), 2026-10-21.

> This project contains a model of [Noir's](https://noir-lang.org) semantics in the [Lean](https://lean-lang.org) programming language and theorem prover. The aim is to support the formal verification of both the Noir language semantics and the properties of programs written in Noir.

*Quoted from [README.md](https://github.com/reilabs/lampe/blob/3d7668f749711083425e1905d4dd1850c0b39f52/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Finite map](../../../data-structures/maps/finite-map.md)
- [Prime numbers](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Array](../../../data-structures/list-like-structures/array.md)
- [Characteristic of a ring](../../field-theory/characteristic-of-a-ring.md)
- [Natural number](../../numbers/natural-number.md)
- [Integer](../../numbers/integer.md)
- [Field](../../field-theory/field.md)
- [List](../../../data-structures/list-like-structures/list.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`Lampe`](https://github.com/reilabs/lampe/blob/3d7668f749711083425e1905d4dd1850c0b39f52/Lampe/Lampe.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `Lampe/Lampe/Syntax/Builders.lean` holds `sorry` or `admit`.

## Project

- Lean v4.29.1, Mathlib at [5e932f97](https://github.com/leanprover-community/mathlib4/tree/5e932f97dd25535344f80f9dd8da3aab83df0fe6).
- 365 .lean files; its Lean libraries `Lampe`, `Tests` hold 100, declaring 1,208 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/reilabs/lampe/blob/3d7668f749711083425e1905d4dd1850c0b39f52/LICENSE)).

## Builds on

- Mathlib, at [5e932f97](https://github.com/leanprover-community/mathlib4/tree/5e932f97dd25535344f80f9dd8da3aab83df0fe6).

## Placement

Of its imports of Mathlib modules in an overview area, 11 of 17 are in General algebra, 1.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (11 of 17 imports, 1.8×), Data structures (3 of 17 imports, 1.2×). *Proof depends on* names 8 of the 8 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [reilabs/lampe at 3d7668f7](https://github.com/reilabs/lampe/tree/3d7668f749711083425e1905d4dd1850c0b39f52)

---
declaration: module
origin: cited
lean: DefinableSaturated.Challenge, DefinableSaturated.Solution, Scotts
statement: formalized
---

# definable-saturated

[elliotglazer/definable-saturated](https://github.com/elliotglazer/definable-saturated) at commit [e683bba9](https://github.com/elliotglazer/definable-saturated/tree/e683bba9e758323b43dd1d6206ed2f6fc9510f06), 2026-09-19.

> This repository formalizes the relative consistency of the following statement.

*Quoted from [README.md](https://github.com/elliotglazer/definable-saturated/blob/e683bba9e758323b43dd1d6206ed2f6fc9510f06/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Elementary embedding](../model-theory/elementary-embedding.md)
- [First-order formula](../model-theory/first-order-formula.md)
- [Aleph numbers](../set-theory/cardinals/aleph-numbers.md)
- [Cardinal](../set-theory/cardinals/cardinal.md)
- [Model of ZFC](../set-theory/model-of-zfc.md)
- [Quotient space (Basic definitions)](../../../undergraduate/group-theory/basic-definitions/quotient-space.md)
- [Language](../formal-languages/language.md)
- [Ordinal](../set-theory/ordinals/ordinal.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`DefinableSaturated.Challenge`](https://github.com/elliotglazer/definable-saturated/blob/e683bba9e758323b43dd1d6206ed2f6fc9510f06/DefinableSaturated/Challenge.lean), [`DefinableSaturated.Solution`](https://github.com/elliotglazer/definable-saturated/blob/e683bba9e758323b43dd1d6206ed2f6fc9510f06/DefinableSaturated/Solution.lean), [`Scotts`](https://github.com/elliotglazer/definable-saturated/blob/e683bba9e758323b43dd1d6206ed2f6fc9510f06/Scotts.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `DefinableSaturated/Challenge.lean` holds `sorry` or `admit`.

## Project

- Lean v4.34.0-rc1, Mathlib at [355bc1e0](https://github.com/leanprover-community/mathlib4/tree/355bc1e0ed1d36e49525121e1a280ca13a058a92).
- 699 .lean files; its Lean libraries `Scotts`, `DefinableSaturatedChallenge`, `DefinableSaturatedSolution` hold 698, declaring 6,159 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/elliotglazer/definable-saturated/blob/e683bba9e758323b43dd1d6206ed2f6fc9510f06/LICENSE)).

## Builds on

- Mathlib, at [355bc1e0](https://github.com/leanprover-community/mathlib4/tree/355bc1e0ed1d36e49525121e1a280ca13a058a92).
- `erdos501` (https://github.com/elliotglazer/erdos501.git) at `218d1c1e`.

## Placement

Of its imports of Mathlib modules in an overview area, 31 of 89 are in Logic and computation, 32.7 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Logic and computation (31 of 89 imports, 32.7×), Topology (24 of 89 imports, 3.6×), Data structures (13 of 89 imports, 1.0×). *Proof depends on* names 8 of the 22 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [elliotglazer/definable-saturated at e683bba9](https://github.com/elliotglazer/definable-saturated/tree/e683bba9e758323b43dd1d6206ed2f6fc9510f06)

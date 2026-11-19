---
declaration: module
origin: cited
lean: DynExpr
statement: formalized
proof: formalized
---

# Formalizing Julia in Lean

[MilesCranmer/julia-in-lean](https://github.com/MilesCranmer/julia-in-lean) at commit [de862b56](https://github.com/MilesCranmer/julia-in-lean/tree/de862b56ffbf2dd2ea210b82b3c235b0550624ec), 2026-11-07.

> Julia source code modelled in Lean 4. Each modelled function has a Lean definition following the Julia source. Properties taken from a docstring, the manual, or an invariant are recorded as proven, refuted, or open. A refutation proves the negation of a property in the model; runtime evidence in the associated report establishes whether it is also a Julia bug.

*Quoted from [README.md](https://github.com/MilesCranmer/julia-in-lean/blob/de862b56ffbf2dd2ea210b82b3c235b0550624ec/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Rational number](../../../mathlib/overview/general-algebra/numbers/rational-number.md)
- [Gradient vector](../../../mathlib/undergraduate/multivariable-calculus/differential-calculus/gradient-vector.md)
- [Natural number](../../../mathlib/overview/general-algebra/numbers/natural-number.md)
- [List](../../../mathlib/overview/data-structures/list-like-structures/list.md)
- [Integer](../../../mathlib/overview/general-algebra/numbers/integer.md)
- [Array](../../../mathlib/overview/data-structures/list-like-structures/array.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`DynExpr`](https://github.com/MilesCranmer/julia-in-lean/blob/de862b56ffbf2dd2ea210b82b3c235b0550624ec/dynamicexpressions/DynExpr.lean): the root of a Lean library its lakefile builds, not a theorem. No file it imports, directly or not (178 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.1.
- 1,821 .lean files; its Lean libraries `DynExpr` hold 182, declaring 2,909 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/MilesCranmer/julia-in-lean/blob/de862b56ffbf2dd2ea210b82b3c235b0550624ec/LICENSE)).

## Placement

It requires neither Mathlib nor another library mapped here, and imports no Batteries module: it builds on Lean core alone.

## Mathlib use

*Proof depends on* names 6 of the 6 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [MilesCranmer/julia-in-lean at de862b56](https://github.com/MilesCranmer/julia-in-lean/tree/de862b56ffbf2dd2ea210b82b3c235b0550624ec)

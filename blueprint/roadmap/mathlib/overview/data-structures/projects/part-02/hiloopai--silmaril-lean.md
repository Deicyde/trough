---
declaration: module
origin: cited
lean: Silmaril, Silmaril.Calculi, Silmaril.Cli
statement: formalized
---

# Silmaril

[hiloopai/silmaril-lean](https://github.com/hiloopai/silmaril-lean) at commit [f5cf7d91](https://github.com/hiloopai/silmaril-lean/tree/f5cf7d914c50d51cc677d86f1f29c4aae38ebc13), 2026-11-18.

> Silmaril uses Lean 4 to model programs and prove properties about them. It includes a WebAssembly toolkit with Binaryen-style commands and a library of logics, models, lambda calculi and verified translations.

*Quoted from [README.md](https://github.com/hiloopai/silmaril-lean/blob/f5cf7d914c50d51cc677d86f1f29c4aae38ebc13/README.md), MIT, Copyright (c) 2026 Silmaril contributors.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Fixed points](../../../dynamics/general-theory/fixed-points.md)
- [Finite map](../../maps/finite-map.md)
- [Language](../../../logic-and-computation/formal-languages/language.md)
- [List](../../list-like-structures/list.md)
- [Cartesian closed](../../../general-algebra/category-theory/cartesian-closed.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [Integer](../../../general-algebra/numbers/integer.md)
- [Array](../../list-like-structures/array.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Silmaril`](https://github.com/hiloopai/silmaril-lean/blob/f5cf7d914c50d51cc677d86f1f29c4aae38ebc13/Silmaril.lean), [`Silmaril.Calculi`](https://github.com/hiloopai/silmaril-lean/blob/f5cf7d914c50d51cc677d86f1f29c4aae38ebc13/Silmaril/Calculi.lean), [`Silmaril.Cli`](https://github.com/hiloopai/silmaril-lean/blob/f5cf7d914c50d51cc677d86f1f29c4aae38ebc13/Silmaril/Cli.lean): the root of a Lean library its lakefile builds, not a theorem. Not every file of the project was read.

## Project

- Lean nightly-2026-11-05, Mathlib at [569134c2](https://github.com/leanprover-community/mathlib4/tree/569134c2fc750d92baa85d50cd925a7e20a93dd2).
- 23,123 .lean files; its Lean libraries `Silmaril`, `SilmarilSpecTec`, `SilmarilLogicGraphData`, `SilmarilSpecTecMeta`, `SilmarilWasmProject`, `SilmarilWasiWit` and 6 more hold 5,000 (the first read), declaring 381,318 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- License: MIT ([LICENSE](https://github.com/hiloopai/silmaril-lean/blob/f5cf7d914c50d51cc677d86f1f29c4aae38ebc13/LICENSE)).

## Builds on

- Mathlib, at [569134c2](https://github.com/leanprover-community/mathlib4/tree/569134c2fc750d92baa85d50cd925a7e20a93dd2).
- `cslib` (https://github.com/leanprover/downstream-lean4) at `569134c2`.
- `iris` (https://github.com/hiloopai/iris-lean) at `8b7e85de`.

## Placement

Of its imports of Mathlib modules in an overview area, 47 of 114 are in Data structures, 2.9 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (47 of 114 imports, 2.9×), General algebra (48 of 114 imports, 1.2×). *Proof depends on* names 8 of the 21 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [hiloopai/silmaril-lean at f5cf7d91](https://github.com/hiloopai/silmaril-lean/tree/f5cf7d914c50d51cc677d86f1f29c4aae38ebc13)

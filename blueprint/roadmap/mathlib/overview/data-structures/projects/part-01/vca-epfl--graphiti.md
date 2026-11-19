---
declaration: module
origin: cited
lean: Graphiti, Graphiti.Projects
statement: formalized
---

# How to build

[VCA-EPFL/graphiti](https://github.com/VCA-EPFL/graphiti) at commit [6fde142e](https://github.com/VCA-EPFL/graphiti/tree/6fde142e1ded3b7ff214f1ecaa816b140e4ecb9a), 2026-10-04.

> The following commands should successfully build the project.

*Quoted from [README.md](https://github.com/VCA-EPFL/graphiti/blob/6fde142e1ded3b7ff214f1ecaa816b140e4ecb9a/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Hash map](../../maps/hash-map.md)
- [Module](../../../linear-algebra/fundamentals/module.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [List](../../list-like-structures/list.md)
- [Array](../../list-like-structures/array.md)
- [Differentiable functions](../../../../undergraduate/multivariable-calculus/differential-calculus/differentiable-functions.md)
- [Integer](../../../general-algebra/numbers/integer.md)
- [Real number](../../../general-algebra/numbers/real-number.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`Graphiti`](https://github.com/VCA-EPFL/graphiti/blob/6fde142e1ded3b7ff214f1ecaa816b140e4ecb9a/Graphiti.lean), [`Graphiti.Projects`](https://github.com/VCA-EPFL/graphiti/blob/6fde142e1ded3b7ff214f1ecaa816b140e4ecb9a/Graphiti/Projects.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Graphiti/Core/Dataflow/Rewrites/JoinRewrite.lean`, `Graphiti/Core/Graph/Environment.lean`, `Graphiti/Core/Graph/ExprLowLemmas.lean`, `Graphiti/Core/Graph/ModuleLemmas.lean`, `Graphiti/Projects/DeadlockRefinement.lean`, `Graphiti/Projects/Flushability/ConfluentModule.lean`, `Graphiti/Projects/Flushability/FlushedModule.lean`, `Graphiti/Projects/Flushability/JoinRewriteCorrect.lean`, `Graphiti/Projects/Flushability/ModuleRefinement.lean` hold `sorry` or `admit`.

## Project

- Lean v4.34.1, Mathlib at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).
- 150 .lean files; its Lean libraries `Graphiti`, `GraphitiCore`, `GraphitiProjects`, `GraphitiTest` hold 149, declaring 2,701 names, with `sorry` in 27 files and 1 axiom, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/VCA-EPFL/graphiti/blob/6fde142e1ded3b7ff214f1ecaa816b140e4ecb9a/LICENSE)).

## Builds on

- Mathlib, at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).

## Placement

Of its imports of Mathlib modules in an overview area, 2 of 5 are in Data structures, 2.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Data structures (2 of 5 imports, 2.8×), General algebra (2 of 5 imports, 1.1×), Analysis (1 of 5 imports, 0.7×). *Proof depends on* names 8 of the 8 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [VCA-EPFL/graphiti at 6fde142e](https://github.com/VCA-EPFL/graphiti/tree/6fde142e1ded3b7ff214f1ecaa816b140e4ecb9a)

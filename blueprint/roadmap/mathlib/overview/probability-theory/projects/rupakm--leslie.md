---
declaration: module
origin: cited
lean: Leslie
statement: formalized
proof: formalized
---

# Leslie: TLA in Lean 4

[rupakm/leslie](https://github.com/rupakm/leslie) at commit [58e58b25](https://github.com/rupakm/leslie/tree/58e58b2502b2a570e4ce4fdb6b40748c3cb30e5d), 2026-06-08.

> Leslie is a shallow embedding of the Temporal Logic of Actions (TLA) in Lean 4. It provides a framework for specifying and verifying concurrent and distributed systems with machine-checked proofs.

*Quoted from [README.md](https://github.com/rupakm/leslie/blob/58e58b2502b2a570e4ce4fdb6b40748c3cb30e5d/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Ionescu-Tulcea theorem](../../../thousand-plus/probability-and-statistics/ionescu-tulcea-theorem.md)
- [Lagrange interpolation](../../../undergraduate/numerical-analysis/approximation-of-numerical-functions/lagrange-interpolation.md)
- [Discrete law](../random-variables-and-their-laws/discrete-law.md)
- [Ackermann function](../../logic-and-computation/computability/ackermann-function.md)
- [Probability measure](../definitions-in-probability-theory/probability-measure.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Polynomial functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md)
- [Sigma-algebra](../../analysis/measures-and-integral-calculus/part-01/sigma-algebra.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`Leslie`](https://github.com/rupakm/leslie/blob/58e58b2502b2a570e4ce4fdb6b40748c3cb30e5d/Leslie.lean): the root of a Lean library its lakefile builds, not a theorem. No file it imports, directly or not (1 file), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.27.0, Mathlib at [a3a10db0](https://github.com/leanprover-community/mathlib4/tree/a3a10db0e9d66acbebf76c5e6a135066525ac900).
- 166 .lean files; its Lean libraries `Leslie` hold 166, declaring 3,312 names, with `sorry` in 3 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/rupakm/leslie/blob/58e58b2502b2a570e4ce4fdb6b40748c3cb30e5d/LICENSE)).

## Builds on

- Mathlib, at [a3a10db0](https://github.com/leanprover-community/mathlib4/tree/a3a10db0e9d66acbebf76c5e6a135066525ac900).
- `lintLlmProofs` (https://github.com/jessealama/lint-llm-proofs) at `d1d57fbc`.

## Placement

Of its imports of Mathlib modules in an overview area, 14 of 50 are in Probability Theory, 14.7 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (14 of 50 imports, 14.7×), Combinatorics (21 of 50 imports, 9.8×), Data structures (10 of 50 imports, 1.4×). *Proof depends on* lists 8 of the 21 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [rupakm/leslie at 58e58b25](https://github.com/rupakm/leslie/tree/58e58b2502b2a570e4ce4fdb6b40748c3cb30e5d)

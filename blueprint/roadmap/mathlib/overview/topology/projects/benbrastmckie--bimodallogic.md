---
declaration: theorem
origin: cited
lean: FormalSystem.Metalogic.strongCompletenessBase, FormalSystem.Metalogic.strongCompletenessDense, FormalSystem.Metalogic.notStrongCompletenessZTime, FormalSystem.Metalogic.notStrongCompletenessRTime, FormalSystem.Metalogic.WeakCanonical.countermodel_discrete, FormalSystem.Metalogic.notCompactZTime, FormalSystem.Metalogic.compactBase, FormalSystem.Metalogic.compactDense
statement: formalized
proof: formalized
---

# A Bimodal Logic for Tense and Modality

[benbrastmckie/BimodalLogic](https://github.com/benbrastmckie/BimodalLogic) at commit [d9e708cc](https://github.com/benbrastmckie/BimodalLogic/tree/d9e708cc96be6e49f3f9629d00c919a9e52cc50e), 2026-11-17.

> This repository implements the **bimodal fragment** of the [Logos](https://logos-labs.ai/) in Lean 4, establishing soundness and completeness for a logic designed for reasoning about future contingency in non-deterministic dynamical systems. The **task semantics** evaluates formulas at both a history and a time, where histories are functions from times to world-states constrained by the task relation which encodes the possible transitions between world-states over a duration of time.

*Quoted from [README.md](https://github.com/benbrastmckie/BimodalLogic/blob/d9e708cc96be6e49f3f9629d00c919a9e52cc50e/README.md), Apache-2.0.*

## Depends on

- [Set](../../data-structures/sets/set.md)

## Proof depends on

- [Cantor's isomorphism theorem](../../../thousand-plus/combinatorics-and-ordered-structures/06-order-lattices-ordered-algebraic-structures/cantors-isomorphism-theorem.md)
- [Boolean prime ideal theorem](../../../thousand-plus/general-topics-history-and-foundations/boolean-prime-ideal-theorem.md)
- [Cantor's intersection theorem](../../../thousand-plus/analysis/26-real-functions/part-01/cantors-intersection-theorem.md)
- [The Irrationality of the Square Root of 2](../../../hundred-theorems/part-01/the-irrationality-of-the-square-root-of-2.md)
- [Finite](../../combinatorics/pigeonhole-principles/finite.md)
- [The Number of Subsets of a Set](../../../hundred-theorems/part-02/the-number-of-subsets-of-a-set.md)
- [Order topology](../topological-algebra/order-topology.md)
- [Infinite](../../combinatorics/pigeonhole-principles/infinite.md)

## Main results

Its Lean names are 8 of the 57 theorems its README names in code:

- [`FormalSystem.Metalogic.strongCompletenessBase`](https://github.com/benbrastmckie/BimodalLogic/blob/d9e708cc96be6e49f3f9629d00c919a9e52cc50e/FormalSystem/Metalogic/Compactness.lean#L216) (theorem)
- [`FormalSystem.Metalogic.strongCompletenessDense`](https://github.com/benbrastmckie/BimodalLogic/blob/d9e708cc96be6e49f3f9629d00c919a9e52cc50e/FormalSystem/Metalogic/Compactness.lean#L225) (theorem)
- [`FormalSystem.Metalogic.notStrongCompletenessZTime`](https://github.com/benbrastmckie/BimodalLogic/blob/d9e708cc96be6e49f3f9629d00c919a9e52cc50e/FormalSystem/Metalogic/DiscreteNonCompactness.lean#L292) (theorem)
- [`FormalSystem.Metalogic.notStrongCompletenessRTime`](https://github.com/benbrastmckie/BimodalLogic/blob/d9e708cc96be6e49f3f9629d00c919a9e52cc50e/FormalSystem/Metalogic/DedekindNonCompactness.lean#L489) (theorem)
- [`FormalSystem.Metalogic.WeakCanonical.countermodel_discrete`](https://github.com/benbrastmckie/BimodalLogic/blob/d9e708cc96be6e49f3f9629d00c919a9e52cc50e/FormalSystem/Metalogic/WeakCanonical/GroupModel/CountermodelBase.lean#L146) (theorem)
- [`FormalSystem.Metalogic.notCompactZTime`](https://github.com/benbrastmckie/BimodalLogic/blob/d9e708cc96be6e49f3f9629d00c919a9e52cc50e/FormalSystem/Metalogic/DiscreteNonCompactness.lean#L270) (theorem)
- [`FormalSystem.Metalogic.compactBase`](https://github.com/benbrastmckie/BimodalLogic/blob/d9e708cc96be6e49f3f9629d00c919a9e52cc50e/FormalSystem/Metalogic/Compactness.lean#L198) (theorem)
- [`FormalSystem.Metalogic.compactDense`](https://github.com/benbrastmckie/BimodalLogic/blob/d9e708cc96be6e49f3f9629d00c919a9e52cc50e/FormalSystem/Metalogic/Compactness.lean#L204) (theorem)

No file its headlines import, directly or not (344 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.33.0-rc1, Mathlib at [79d0395a](https://github.com/leanprover-community/mathlib4/tree/79d0395a1825a6264ad5d269e35e60537518955e).
- 1,150 .lean files; its Lean libraries `FormalSystem`, `BimodalTest`, `BimodalTools`, `BimodalToolsTest` hold 881, declaring 17,971 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- License: Apache-2.0 ([LICENSE](https://github.com/benbrastmckie/BimodalLogic/blob/d9e708cc96be6e49f3f9629d00c919a9e52cc50e/LICENSE)).

## Builds on

- Mathlib, at [79d0395a](https://github.com/leanprover-community/mathlib4/tree/79d0395a1825a6264ad5d269e35e60537518955e).

## Placement

Of its imports of Mathlib modules in an overview area, 69 of 265 are in Topology, 3.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Topology (69 of 265 imports, 3.5×), Data structures (69 of 265 imports, 1.8×), General algebra (101 of 265 imports, 1.1×). *Proof depends on* names 8 of the 39 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [benbrastmckie/BimodalLogic at d9e708cc](https://github.com/benbrastmckie/BimodalLogic/tree/d9e708cc96be6e49f3f9629d00c919a9e52cc50e)

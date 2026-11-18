---
declaration: theorem
origin: cited
lean: IntervalExchange.UniqueErgodicity.masurVeech_ae_unique_invariant, IntervalExchange.Pair.masurVeech, IntervalExchange.UniqueErgodicity.uniformBirkhoff_of_uniqueErgodic, IntervalExchange.Pair.veechRigidity, IntervalExchange.UniqueErgodicity.exists_uniform_birkhoff, IntervalExchange.RauzyVeech.colSumInt_cast, IntervalExchange.Pair.ae_diophantine, IntervalExchange.Pair.evalWord_eventually_eq_one
statement: formalized
proof: formalized
---

# Almost Every Pair of Interval Exchange Transformations Does Not Generate a Free…

[sgouezel/IETFree](https://github.com/sgouezel/IETFree) at commit [94c4455c](https://github.com/sgouezel/IETFree/tree/94c4455c3243ff4229cd5e0c58af6f97879777b7), 2026-11-09.

## Depends on

- [Positive measure](../../analysis/measures-and-integral-calculus/part-01/positive-measure.md)
- [Permutation group of a type](../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Set](../../data-structures/sets/set.md)
- [Free group](../../general-algebra/group-theory/part-01/free-group.md)

## Proof depends on

- [Urysohn's lemma](../../topology/general-topology/part-02/urysohns-lemma.md)
- [Affine space](../../geometry/affine-and-euclidean-geometry/affine-space.md)
- [Convergence in distribution](../convergence-of-a-sequence-of-random-variables/convergence-in-distribution.md)
- [Events](../../../undergraduate/probability-theory/definitions-of-a-probability-space/events.md)
- [Measurable function](../../analysis/measures-and-integral-calculus/part-01/measurable-function.md)
- [Lebesgue measure (Measure theory)](../../../undergraduate/measures-and-integral-calculus/measure-theory/lebesgue-measure.md)
- [Filter](../../topology/general-topology/part-01/filter.md)
- [Irreducible element](../../general-algebra/divisibility-in-integral-domains/irreducible-element.md)

## Main results

Its Lean names are 8 of the 30 theorems its README names in code:

- [`IntervalExchange.UniqueErgodicity.masurVeech_ae_unique_invariant`](https://github.com/sgouezel/IETFree/blob/94c4455c3243ff4229cd5e0c58af6f97879777b7/IETFree/UniqueErgodicity/MainTheorem.lean#L97) (theorem)
- [`IntervalExchange.Pair.masurVeech`](https://github.com/sgouezel/IETFree/blob/94c4455c3243ff4229cd5e0c58af6f97879777b7/IETFree/Pair/Irreducible.lean#L60) (theorem)
- [`IntervalExchange.UniqueErgodicity.uniformBirkhoff_of_uniqueErgodic`](https://github.com/sgouezel/IETFree/blob/94c4455c3243ff4229cd5e0c58af6f97879777b7/IETFree/UniqueErgodicity/Theorem2.lean#L502) (theorem)
- [`IntervalExchange.Pair.veechRigidity`](https://github.com/sgouezel/IETFree/blob/94c4455c3243ff4229cd5e0c58af6f97879777b7/IETFree/Pair/Irreducible.lean#L71) (theorem)
- [`IntervalExchange.UniqueErgodicity.exists_uniform_birkhoff`](https://github.com/sgouezel/IETFree/blob/94c4455c3243ff4229cd5e0c58af6f97879777b7/IETFree/UniqueErgodicity/Theorem2.lean#L523) (theorem)
- [`IntervalExchange.RauzyVeech.colSumInt_cast`](https://github.com/sgouezel/IETFree/blob/94c4455c3243ff4229cd5e0c58af6f97879777b7/IETFree/RauzyVeech/MeshShrink.lean#L83) (theorem)
- [`IntervalExchange.Pair.ae_diophantine`](https://github.com/sgouezel/IETFree/blob/94c4455c3243ff4229cd5e0c58af6f97879777b7/IETFree/Pair/Diophantine.lean#L971) (theorem)
- [`IntervalExchange.Pair.evalWord_eventually_eq_one`](https://github.com/sgouezel/IETFree/blob/94c4455c3243ff4229cd5e0c58af6f97879777b7/IETFree/Pair/RobustRelation/Robustness.lean#L39) (theorem)

No file its headlines import, directly or not (103 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 122 .lean files; its Lean libraries `IETFree`, `Challenge` hold 122, declaring 2,331 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/sgouezel/IETFree/blob/94c4455c3243ff4229cd5e0c58af6f97879777b7/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

Of its imports of Mathlib modules in an overview area, 4 of 29 are in Probability Theory, 7.3 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (4 of 29 imports, 7.3×), Linear algebra (3 of 29 imports, 1.8×), Analysis (12 of 29 imports, 1.5×). *Proof depends on* names 8 of the 37 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [sgouezel/IETFree at 94c4455c](https://github.com/sgouezel/IETFree/tree/94c4455c3243ff4229cd5e0c58af6f97879777b7)

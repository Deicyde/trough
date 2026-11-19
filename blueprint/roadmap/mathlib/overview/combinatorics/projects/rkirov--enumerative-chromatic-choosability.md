---
declaration: theorem
origin: cited
lean: SimpleGraph.eccAt_of_maxDegree_bound, SimpleGraph.eccAt_of_degree_le_three_eleven, SimpleGraph.eccAt_of_degree_le_four_sixteen, GridGen.Four.ecc_boxProd_pathG_three, GridGen.Five.ecc_boxProd_pathG_four, GridGen.Six.ecc_boxProd_pathG_five, ListColoring.ecc_boxProd_pathG_of_seven, SimpleGraph.KN5.exists_choosable_not_ecc_of_two_le
statement: formalized
proof: formalized
---

# enumerative-chromatic-choosability

*List coloring and enumeratively chromatic-choosable graphs — a Lean 4 formalization*

[rkirov/enumerative-chromatic-choosability](https://github.com/rkirov/enumerative-chromatic-choosability) at commit [5ae30add](https://github.com/rkirov/enumerative-chromatic-choosability/tree/5ae30add62b88ec085dc76f78b1b2dbe121dd70e), 2026-11-13.

## Depends on

- [Simple graph](../graph-theory/simple-graph.md)

## Proof depends on

- [Convexity inequalities](../../analysis/convexity/convexity-inequalities.md)
- [Hall's marriage theorem](../transversals/halls-marriage-theorem.md)
- [Arithmetic Mean/Geometric Mean](../../../hundred-theorems/part-02/arithmetic-mean-geometric-mean.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [The Number of Subsets of a Set](../../../hundred-theorems/part-02/the-number-of-subsets-of-a-set.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [List](../../data-structures/list-like-structures/list.md)
- [Hyperbolic trigonometric functions](../../analysis/special-functions/hyperbolic-trigonometric-functions.md)

## Main results

Its Lean names are 8 of the 36 theorems its README names in code:

- [`SimpleGraph.eccAt_of_maxDegree_bound`](https://github.com/rkirov/enumerative-chromatic-choosability/blob/5ae30add62b88ec085dc76f78b1b2dbe121dd70e/GridGen/MaximumDegree.lean#L48) (theorem)
- [`SimpleGraph.eccAt_of_degree_le_three_eleven`](https://github.com/rkirov/enumerative-chromatic-choosability/blob/5ae30add62b88ec085dc76f78b1b2dbe121dd70e/GridGen/PeelDegree.lean#L104) (theorem)
- [`SimpleGraph.eccAt_of_degree_le_four_sixteen`](https://github.com/rkirov/enumerative-chromatic-choosability/blob/5ae30add62b88ec085dc76f78b1b2dbe121dd70e/GridGen/PeelDegree.lean#L117) (theorem)
- [`GridGen.Four.ecc_boxProd_pathG_three`](https://github.com/rkirov/enumerative-chromatic-choosability/blob/5ae30add62b88ec085dc76f78b1b2dbe121dd70e/GridGen/Four/Main.lean#L42) (theorem)
- [`GridGen.Five.ecc_boxProd_pathG_four`](https://github.com/rkirov/enumerative-chromatic-choosability/blob/5ae30add62b88ec085dc76f78b1b2dbe121dd70e/GridGen/Five/Main.lean#L28) (theorem)
- [`GridGen.Six.ecc_boxProd_pathG_five`](https://github.com/rkirov/enumerative-chromatic-choosability/blob/5ae30add62b88ec085dc76f78b1b2dbe121dd70e/GridGen/Six/Main.lean#L28) (theorem)
- [`ListColoring.ecc_boxProd_pathG_of_seven`](https://github.com/rkirov/enumerative-chromatic-choosability/blob/5ae30add62b88ec085dc76f78b1b2dbe121dd70e/GridGen/Gauge/Seven/Assemble7.lean#L44) (theorem)
- [`SimpleGraph.KN5.exists_choosable_not_ecc_of_two_le`](https://github.com/rkirov/enumerative-chromatic-choosability/blob/5ae30add62b88ec085dc76f78b1b2dbe121dd70e/ListColoring/Section5.lean#L635) (theorem)

No file its headlines import, directly or not (421 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 1,316 .lean files; its Lean libraries `ListColoring`, `OpenProblems`, `Cacti`, `NonPersistence`, `ProductCounterexample`, `Ladder` and 5 more hold 1,290, declaring 72,535 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/rkirov/enumerative-chromatic-choosability/blob/5ae30add62b88ec085dc76f78b1b2dbe121dd70e/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

Of its imports of Mathlib modules in an overview area, 29 of 92 are in Combinatorics, 7.3 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Combinatorics (29 of 92 imports, 7.3×), General algebra (31 of 92 imports, 0.9×), Data structures (10 of 92 imports, 0.8×). *Proof depends on* names 8 of the 24 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [rkirov/enumerative-chromatic-choosability at 5ae30add](https://github.com/rkirov/enumerative-chromatic-choosability/tree/5ae30add62b88ec085dc76f78b1b2dbe121dd70e)

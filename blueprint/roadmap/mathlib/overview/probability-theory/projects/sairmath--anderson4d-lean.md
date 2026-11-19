---
declaration: theorem
origin: cited
lean: Anderson4D.latticeChainSum_le_treeSum, Anderson4D.sum_eq_sum_paired_tree_incidence_div, Anderson4D.PositiveAssignment.card_le_two_pow, Anderson4D.pairedWordSum_le_paperSum, Anderson4D.primitivePairedWordSum_le_paperSumFiltered, Anderson4D.packing_lemma, Anderson4D.toy_injTuple_bound, Anderson4D.toy_permSum_bound
statement: formalized
proof: formalized
---

# anderson4d

[sairmath/anderson4d_lean](https://github.com/sairmath/anderson4d_lean) at commit [e828ac5d](https://github.com/sairmath/anderson4d_lean/tree/e828ac5d5f1855941939718668394e9d439aebdb), 2026-08-27.

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Permutation group of a type](../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)

## Proof depends on

- [Product of finitely many measures](../../analysis/measures-and-integral-calculus/part-02/product-of-finitely-many-measures.md)
- [Lévy continuity theorem](../../../thousand-plus/probability-and-statistics/levy-continuity-theorem.md)
- [Fubini's theorem](../../analysis/measures-and-integral-calculus/part-02/fubinis-theorem.md)
- [Characteristic function](../definitions-in-probability-theory/characteristic-function.md)
- [Absolutely convergent series in Banach spaces](../../analysis/normed-vector-spaces-banach-spaces/absolutely-convergent-series-in-banach-spaces.md)
- [Vector-valued integrable function (Bochner integral)](../../analysis/measures-and-integral-calculus/part-01/vector-valued-integrable-function-bochner-integr.md)
- [Continuity of the sum of a series of functions](../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/continuity-of-the-sum-of-a-series-of-functions.md)
- [Gaussian processes](../stochastic-processes/gaussian-processes.md)

## Main results

Its Lean names are 8 of the 12 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`Anderson4D.latticeChainSum_le_treeSum`](https://github.com/sairmath/anderson4d_lean/blob/e828ac5d5f1855941939718668394e9d439aebdb/Anderson4D/HeppTree/Decomposition.lean#L1338) (theorem)
- [`Anderson4D.sum_eq_sum_paired_tree_incidence_div`](https://github.com/sairmath/anderson4d_lean/blob/e828ac5d5f1855941939718668394e9d439aebdb/Anderson4D/HeppTree/PairedIncidence.lean#L202) (theorem)
- [`Anderson4D.PositiveAssignment.card_le_two_pow`](https://github.com/sairmath/anderson4d_lean/blob/e828ac5d5f1855941939718668394e9d439aebdb/Anderson4D/Combinatorics/MultiplicityCount.lean#L119) (theorem)
- [`Anderson4D.pairedWordSum_le_paperSum`](https://github.com/sairmath/anderson4d_lean/blob/e828ac5d5f1855941939718668394e9d439aebdb/Anderson4D/Combinatorics/AcrossPairing.lean#L214) (theorem)
- [`Anderson4D.primitivePairedWordSum_le_paperSumFiltered`](https://github.com/sairmath/anderson4d_lean/blob/e828ac5d5f1855941939718668394e9d439aebdb/Anderson4D/Combinatorics/PrimitiveWord.lean#L284) (theorem)
- [`Anderson4D.packing_lemma`](https://github.com/sairmath/anderson4d_lean/blob/e828ac5d5f1855941939718668394e9d439aebdb/Anderson4D/PermSum/Toy.lean#L240) (theorem)
- [`Anderson4D.toy_injTuple_bound`](https://github.com/sairmath/anderson4d_lean/blob/e828ac5d5f1855941939718668394e9d439aebdb/Anderson4D/PermSum/Toy.lean#L526) (theorem)
- [`Anderson4D.toy_permSum_bound`](https://github.com/sairmath/anderson4d_lean/blob/e828ac5d5f1855941939718668394e9d439aebdb/Anderson4D/PermSum/Toy.lean#L623) (theorem)

No file its headlines import, directly or not (22 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.32.1, Mathlib at [520045ab](https://github.com/leanprover-community/mathlib4/tree/520045ab14e26149ee970e2e617ca04b09bde5d6).
- 819 .lean files; its Lean libraries `Anderson4D` hold 818, declaring 13,094 names, with `sorry` in 5 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/sairmath/anderson4d_lean/blob/e828ac5d5f1855941939718668394e9d439aebdb/LICENSE)).

## Builds on

- Mathlib, at [520045ab](https://github.com/leanprover-community/mathlib4/tree/520045ab14e26149ee970e2e617ca04b09bde5d6).

## Placement

Of its imports of Mathlib modules in an overview area, 11 of 84 are in Probability Theory, 6.9 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Probability Theory (11 of 84 imports, 6.9×), Combinatorics (11 of 84 imports, 3.0×), Analysis (44 of 84 imports, 1.9×). *Proof depends on* lists 8 of the 75 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [sairmath/anderson4d_lean at e828ac5d](https://github.com/sairmath/anderson4d_lean/tree/e828ac5d5f1855941939718668394e9d439aebdb)

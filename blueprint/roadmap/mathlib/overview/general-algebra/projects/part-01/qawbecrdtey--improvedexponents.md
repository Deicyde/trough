---
declaration: theorem
origin: cited
lean: ImprovedExponents.threeSum_paper, ImprovedExponents.threeSum_exact, ImprovedExponents.threeSum_full, ImprovedExponents.apsp_allEdges, ImprovedExponents.minPlus_allEdges, ImprovedExponents.allSolved_paper, ImprovedExponents.allSolved_exact, ImprovedExponents.allSolved_full
statement: formalized
proof: formalized
---

# ImprovedExponents

[qawbecrdtey/ImprovedExponents](https://github.com/qawbecrdtey/ImprovedExponents) at commit [0725f247](https://github.com/qawbecrdtey/ImprovedExponents/tree/0725f2477587d67212936777b8a264c9793ac7bb), 2026-10-07.

> A Lean 4 formalization of improved running-time exponents for 3SUM, Exact Triangle, the (min,+)-product and all-pairs shortest paths (APSP), with the accompanying paper *Improved exponents for 3SUM and APSP from triangles in sparse lopsided graphs* (`papers/improved-exponents/`).

*Quoted from [README.md](https://github.com/qawbecrdtey/ImprovedExponents/blob/0725f2477587d67212936777b8a264c9793ac7bb/README.md), Apache-2.0.*

## Depends on

- [Logarithm](../../../analysis/special-functions/logarithm.md)

## Proof depends on

- [Congruence in $\Z$](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/congruence-in-z.md)
- [Finite](../../../combinatorics/pigeonhole-principles/finite.md)
- [Formula for the Number of Combinations](../../../../hundred-theorems/part-03/formula-for-the-number-of-combinations.md)
- [The Binomial Theorem](../../../../hundred-theorems/part-02/the-binomial-theorem.md)
- [Prime numbers](../../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Ordered ring](../../rings/ordered-ring.md)
- [Rupture field](../../field-theory/rupture-field.md)
- [List](../../../data-structures/list-like-structures/list.md)

## Main results

Its Lean names are 8 of the 25 theorems its README names in code:

- [`ImprovedExponents.threeSum_paper`](https://github.com/qawbecrdtey/ImprovedExponents/blob/0725f2477587d67212936777b8a264c9793ac7bb/ImprovedExponents/Statements.lean#L167) (theorem)
- [`ImprovedExponents.threeSum_exact`](https://github.com/qawbecrdtey/ImprovedExponents/blob/0725f2477587d67212936777b8a264c9793ac7bb/ImprovedExponents/Statements.lean#L196) (theorem)
- [`ImprovedExponents.threeSum_full`](https://github.com/qawbecrdtey/ImprovedExponents/blob/0725f2477587d67212936777b8a264c9793ac7bb/ImprovedExponents/Statements.lean#L225) (theorem)
- [`ImprovedExponents.apsp_allEdges`](https://github.com/qawbecrdtey/ImprovedExponents/blob/0725f2477587d67212936777b8a264c9793ac7bb/ImprovedExponents/Statements.lean#L378) (theorem)
- [`ImprovedExponents.minPlus_allEdges`](https://github.com/qawbecrdtey/ImprovedExponents/blob/0725f2477587d67212936777b8a264c9793ac7bb/ImprovedExponents/Statements.lean#L374) (theorem)
- [`ImprovedExponents.allSolved_paper`](https://github.com/qawbecrdtey/ImprovedExponents/blob/0725f2477587d67212936777b8a264c9793ac7bb/ImprovedExponents/Pipeline/General.lean#L50) (theorem)
- [`ImprovedExponents.allSolved_exact`](https://github.com/qawbecrdtey/ImprovedExponents/blob/0725f2477587d67212936777b8a264c9793ac7bb/ImprovedExponents/Pipeline/General.lean#L78) (theorem)
- [`ImprovedExponents.allSolved_full`](https://github.com/qawbecrdtey/ImprovedExponents/blob/0725f2477587d67212936777b8a264c9793ac7bb/ImprovedExponents/Pipeline/General.lean#L256) (theorem)

No file its headlines import, directly or not (450 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 522 .lean files; its Lean libraries `EndStatement`, `PaperStatements`, `ThreeSumApsp`, `ImprovedExponents`, `ImprovedChallenge`, `ImprovedSolution` hold 522, declaring 11,690 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/qawbecrdtey/ImprovedExponents/blob/0725f2477587d67212936777b8a264c9793ac7bb/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).

## Placement

Of its imports of Mathlib modules in an overview area, 87 of 148 are in General algebra, 1.7 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (87 of 148 imports, 1.7×), Data structures (22 of 148 imports, 1.0×), Analysis (24 of 148 imports, 0.6×). *Proof depends on* lists 8 of the 34 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [qawbecrdtey/ImprovedExponents at 0725f247](https://github.com/qawbecrdtey/ImprovedExponents/tree/0725f2477587d67212936777b8a264c9793ac7bb)

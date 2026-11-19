---
declaration: module
origin: cited
lean: BenderGlauberman, BenderSuzuki, FeitThompson
statement: formalized
---

# CFSG

*Formalization of the Classification of Finite Simple Groups*

[Qiuzhen-CFSG/CFSG](https://github.com/Qiuzhen-CFSG/CFSG) at commit [0c663552](https://github.com/Qiuzhen-CFSG/CFSG/tree/0c6635528a02dd46f2e93e2ade0c4ac647ad1eb7), 2026-10-28.

> Work in progress.

*Quoted from [README.md](https://github.com/Qiuzhen-CFSG/CFSG/blob/0c6635528a02dd46f2e93e2ade0c4ac647ad1eb7/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Algebra of endomorphisms of a vector space](../../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Lie's theorem](../../../../thousand-plus/algebra/17-nonassociative-rings-and-algebras/lies-theorem.md)
- [Adjacency matrix](../../../combinatorics/graph-theory/adjacency-matrix.md)
- [Cauchy-Schwarz inequality](../../../analysis/hilbert-spaces/cauchy-schwarz-inequality.md)
- [Lie algebra](../../../general-algebra/algebras-over-a-ring/lie-algebra.md)
- [Schur–Zassenhaus theorem](../../../../thousand-plus/algebra/20-group-theory-and-generalizations/schur-zassenhaus-theorem.md)
- [Invariant subspaces of an endomorphism](../../../../undergraduate/linear-algebra/structure-theory-of-endomorphisms/invariant-subspaces-of-an-endomorphism.md)
- [Rank of a linear map](../../../../undergraduate/linear-algebra/finite-dimensional-vector-spaces/rank-of-a-linear-map.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`BenderGlauberman`](https://github.com/Qiuzhen-CFSG/CFSG/blob/0c6635528a02dd46f2e93e2ade0c4ac647ad1eb7/BenderGlauberman.lean), [`BenderSuzuki`](https://github.com/Qiuzhen-CFSG/CFSG/blob/0c6635528a02dd46f2e93e2ade0c4ac647ad1eb7/BenderSuzuki.lean), [`FeitThompson`](https://github.com/Qiuzhen-CFSG/CFSG/blob/0c6635528a02dd46f2e93e2ade0c4ac647ad1eb7/FeitThompson.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Challenge.lean`, `GorensteinWalter/Suzuki/SylowThreeJoin.lean`, `Theory/AlgebraicGroup/Automorphisms/Classification/theorem_1_15_2.lean`, `Theory/AlgebraicGroup/Automorphisms/Classification/theorem_1_15_4.lean`, `Theory/AlgebraicGroup/Automorphisms/Classification/theorem_1_15_6.lean`, `Theory/AlgebraicGroup/Automorphisms/Classification/theorem_1_15_7.lean`, `Theory/AlgebraicGroup/Automorphisms/Classification/theorem_1_15_8.lean`, `Theory/AlgebraicGroup/Automorphisms/Classification/theorem_1_15_9.lean`, `Theory/AlgebraicGroup/Automorphisms/Lang/theorem_2_1_1.lean`, `Theory/AlgebraicGroup/Automorphisms/Lang/theorem_2_1_11.lean`, `Theory/AlgebraicGroup/Automorphisms/Lang/theorem_2_1_12.lean`, `Theory/AlgebraicGroup/Automorphisms/Lang/theorem_2_1_2_d.lean`, `Theory/AlgebraicGroup/Automorphisms/Lang/theorem_2_1_2_e.lean`, `Theory/AlgebraicGroup/Automorphisms/Lang/theorem_2_1_2_f.lean`, `Theory/AlgebraicGroup/Automorphisms/Lang/theorem_2_1_2_g.lean`, `Theory/AlgebraicGroup/Automorphisms/Lang/theorem_2_1_4.lean`, `Theory/AlgebraicGroup/Automorphisms/Lang/theorem_2_1_6.lean`, `Theory/AlgebraicGroup/Automorphisms/Lang/theorem_2_1_8.lean`, `Theory/AlgebraicGroup/Borel/Conjugation/theorem_1_6_2_b.lean`, `Theory/AlgebraicGroup/Borel/Conjugation/theorem_1_6_3.lean` hold `sorry` or `admit`.

## Project

- Lean v4.33.0, Mathlib at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).
- 93,940 .lean files; its Lean libraries `Challenge`, `Solution`, `FeitThompson`, `BenderSuzuki`, `GorensteinWalter`, `BenderGlauberman` and 3 more hold 5,000 (the first read), declaring 34,977 names, with `sorry` in 62 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/Qiuzhen-CFSG/CFSG/blob/0c6635528a02dd46f2e93e2ade0c4ac647ad1eb7/LICENSE)).

## Builds on

- Mathlib, at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).
- `Comparator` (https://github.com/leanprover/comparator.git) at `3927ad38`.

## Placement

Of its imports of Mathlib modules in an overview area, 593 of 3293 are in Linear algebra, 3.1 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Linear algebra (593 of 3293 imports, 3.1×), General algebra (2332 of 3293 imports, 2.0×). *Proof depends on* names 8 of the 150 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [Qiuzhen-CFSG/CFSG at 0c663552](https://github.com/Qiuzhen-CFSG/CFSG/tree/0c6635528a02dd46f2e93e2ade0c4ac647ad1eb7)

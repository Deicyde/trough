---
declaration: theorem
origin: cited
lean: OddMath.QuiverHecke.nondegeneracy_of_symmetrizer, OddMath.QuiverHecke.bwwLowerDegreeNondegeneracy, OddMath.QuiverHecke.bwwGradedNondegeneracy, OddMath.QuiverHecke.bwwPolynomials_evenNondegeneracy, OddMath.QuiverHecke.quadSum_bwwPolynomials, OddMath.QuiverHecke.integral_nondegeneracy_of_symmetrizer, OddMath.Diagrams.OddNilHecke.compatible, OddMath.Diagrams.OddNilHecke.d_x
statement: formalized
proof: formalized
---

# odd-lean

[apellis/odd-lean](https://github.com/apellis/odd-lean) at commit [14d6b27c](https://github.com/apellis/odd-lean/tree/14d6b27c0f50659705e1da508076752530c1bae2), 2026-11-17.

> A Lean 4 / Mathlib formalization of odd symmetric functions, the odd nilHecke algebra and the odd Littlewood–Richardson rule, together with machine-checked errata to the source papers.

*Quoted from [README.md](https://github.com/apellis/odd-lean/blob/14d6b27c0f50659705e1da508076752530c1bae2/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Quotient ring](../../general-algebra/ideals-and-quotients/quotient-ring.md)
- [Wilson’s Lemma](../../../hundred-theorems/part-02/wilsons-lemma.md)
- [Free algebra of a commutative ring](../../general-algebra/algebras-over-a-ring/free-algebra-of-a-commutative-ring.md)
- [Direct sum](../../../undergraduate/linear-algebra/fundamentals/direct-sum.md)
- [Isomorphism](../../general-algebra/category-theory/isomorphism.md)
- [Sum of an arithmetic series](../../../hundred-theorems/part-03/sum-of-an-arithmetic-series.md)
- [Tensor product](../fundamentals/tensor-product.md)
- [Multiset](../../data-structures/sets/multiset.md)

## Main results

Its Lean names are 8 of the 1419 theorems its README names in code:

- [`OddMath.QuiverHecke.nondegeneracy_of_symmetrizer`](https://github.com/apellis/odd-lean/blob/14d6b27c0f50659705e1da508076752530c1bae2/OddMath/QuiverHecke/VacuumRouteSwappedRightNegative.lean#L65) (theorem)
- [`OddMath.QuiverHecke.bwwLowerDegreeNondegeneracy`](https://github.com/apellis/odd-lean/blob/14d6b27c0f50659705e1da508076752530c1bae2/OddMath/QuiverHecke/BWWNondegeneracy.lean#L106) (theorem)
- [`OddMath.QuiverHecke.bwwGradedNondegeneracy`](https://github.com/apellis/odd-lean/blob/14d6b27c0f50659705e1da508076752530c1bae2/OddMath/QuiverHecke/BWWNondegeneracy.lean#L118) (theorem)
- [`OddMath.QuiverHecke.bwwPolynomials_evenNondegeneracy`](https://github.com/apellis/odd-lean/blob/14d6b27c0f50659705e1da508076752530c1bae2/OddMath/QuiverHecke/BWWEvenSpecialization.lean#L73) (theorem)
- [`OddMath.QuiverHecke.quadSum_bwwPolynomials`](https://github.com/apellis/odd-lean/blob/14d6b27c0f50659705e1da508076752530c1bae2/OddMath/QuiverHecke/BWWEvenSpecialization.lean#L114) (theorem)
- [`OddMath.QuiverHecke.integral_nondegeneracy_of_symmetrizer`](https://github.com/apellis/odd-lean/blob/14d6b27c0f50659705e1da508076752530c1bae2/OddMath/QuiverHecke/IntegralNondegeneracy.lean#L30) (theorem)
- [`OddMath.Diagrams.OddNilHecke.compatible`](https://github.com/apellis/odd-lean/blob/14d6b27c0f50659705e1da508076752530c1bae2/OddMath/Diagrams/OddNilHecke/Differential.lean#L367) (theorem)
- [`OddMath.Diagrams.OddNilHecke.d_x`](https://github.com/apellis/odd-lean/blob/14d6b27c0f50659705e1da508076752530c1bae2/OddMath/Diagrams/OddNilHecke/Differential.lean#L405) (theorem)

No file its headlines import, directly or not (1260 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.34.1, Mathlib at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).
- 2,410 .lean files; its Lean libraries `OddMath`, `NonVacuity` hold 2,409, declaring 41,672 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/apellis/odd-lean/blob/14d6b27c0f50659705e1da508076752530c1bae2/LICENSE)).

## Builds on

- Mathlib, at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).
- `Categorification` (https://github.com/apellis/categorification-lean.git) at `777be9ef`.
- `DG` (https://github.com/apellis/dg-lean.git) at `161db4ed`.
- `LieLean` (https://github.com/apellis/lie-lean.git) at `b4e8b45c`.
- `StringDiagrams` (https://github.com/apellis/string-diagrams-lean.git) at `8ae261b1`.

## Placement

Of its imports of Mathlib modules in an overview area, 172 of 638 are in Linear algebra, 4.6 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Linear algebra (172 of 638 imports, 4.6×), General algebra (385 of 638 imports, 1.7×). *Proof depends on* names 8 of the 93 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [apellis/odd-lean at 14d6b27c](https://github.com/apellis/odd-lean/tree/14d6b27c0f50659705e1da508076752530c1bae2)

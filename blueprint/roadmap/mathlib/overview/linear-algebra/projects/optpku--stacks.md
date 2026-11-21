---
declaration: module
origin: cited
lean: ReasLib
statement: formalized
---

# Formalizing the Stacks Project in Lean

[optpku/stacks](https://github.com/optpku/stacks) at commit [e2299cf9](https://github.com/optpku/stacks/tree/e2299cf97f975b08e7b5b59202ed00adc80ff6b7), 2026-11-06.

> We are formalizing the [Stacks Project](https://stacks.math.columbia.edu/) in Lean 4, building on Mathlib, and organizing the resulting mathematical definitions, statements, and proofs into **ReasLib**, a shared and reusable library. The Stacks Project is a comprehensive open-source reference that systematically organizes knowledge in algebraic geometry. We have completed an initial large-scale formalization of its mathematical statements in Lean 4 and integrated the results into ReasLib.

*Quoted from [README.md](https://github.com/optpku/stacks/blob/e2299cf97f975b08e7b5b59202ed00adc80ff6b7/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Perfect closure](../../general-algebra/field-theory/perfect-closure.md)
- [Tensor algebra of a commutative ring](../../general-algebra/algebras-over-a-ring/tensor-algebra-of-a-commutative-ring.md)
- [Tensor product of algebras](../../general-algebra/algebras-over-a-ring/tensor-product-of-algebras.md)
- [Functorial homology](../../general-algebra/homological-algebra/functorial-homology.md)
- [The category of rings](../../general-algebra/rings/the-category-of-rings.md)
- [Lie algebra](../../general-algebra/algebras-over-a-ring/lie-algebra.md)
- [Grothendieck topology](../../general-algebra/category-theory/grothendieck-topology.md)
- [Cartesian closed](../../general-algebra/category-theory/cartesian-closed.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`ReasLib`](https://github.com/optpku/stacks/blob/e2299cf97f975b08e7b5b59202ed00adc80ff6b7/ReasLib.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `ReasLib/Algebra/Category/CommAlgCat/FilteredColimit/FinitelyGenerated.lean`, `ReasLib/Algebra/Category/CommAlgCat/FilteredColimit/Representatives.lean`, `ReasLib/Algebra/Category/CommAlgCat/Over/Etale.lean`, `ReasLib/Algebra/Category/CommAlgCat/Over/Etale/Localization.lean`, `ReasLib/Algebra/Category/CommAlgCat/Over/Etale/Neighborhood.lean`, `ReasLib/Algebra/Category/CommAlgCat/Over/Target.lean`, `ReasLib/Algebra/Category/CommAlgCat/Over/Target/Localization.lean`, `ReasLib/Algebra/Category/CommAlgCat/Over/Target/Localization/SeparableClosure.lean`, `ReasLib/Algebra/Category/CommAlgCat/Over/Target/ResidueField.lean`, `ReasLib/Algebra/Category/CommRingCat/FilteredColimit/Algebra.lean`, `ReasLib/Algebra/Category/CommRingCat/FilteredColimit/Representatives.lean`, `ReasLib/Algebra/Category/CommRingCat/PolynomialResolution/AlternatingFace.lean`, `ReasLib/Algebra/Category/CommRingCat/PolynomialResolution/Construction.lean`, `ReasLib/Algebra/Category/CommRingCat/PolynomialResolution/Contraction/FreeResolution.lean`, `ReasLib/Algebra/Category/CommRingCat/PolynomialResolution/Contraction/UnderlyingSet.lean`, `ReasLib/Algebra/Category/CommRingCat/PolynomialResolution/Generators.lean`, `ReasLib/Algebra/Category/CommRingCat/Under/FreeAlgebra.lean`, `ReasLib/Algebra/Category/CommRingCat/Under/Module.lean`, `ReasLib/Algebra/Category/DifferentialGraded/Admissible.lean`, `ReasLib/Algebra/Category/DifferentialGraded/AdmissibleCone.lean` hold `sorry` or `admit`.

## Project

- Lean v4.32.0, Mathlib at [81a5d257](https://github.com/leanprover-community/mathlib4/tree/81a5d257c8e410db227a6665ed08f64fea08e997).
- 47,466 .lean files; its Lean libraries `ReasLib`, `stacks_project`, `stacks` hold 5,000 (the first read), declaring 49,158 names, with `sorry` in 4246 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/optpku/stacks/blob/e2299cf97f975b08e7b5b59202ed00adc80ff6b7/LICENSE)).

## Builds on

- Mathlib, at [81a5d257](https://github.com/leanprover-community/mathlib4/tree/81a5d257c8e410db227a6665ed08f64fea08e997).
- `check_recall_tag` (https://github.com/imathwy/check_recall_tag.git) at `7c6d64d3`.

## Placement

Of its imports of Mathlib modules in an overview area, 1249 of 5657 are in Linear algebra, 3.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Linear algebra (1249 of 5657 imports, 3.8×), General algebra (3822 of 5657 imports, 1.9×). *Proof depends on* lists 8 of the 104 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [optpku/stacks at e2299cf9](https://github.com/optpku/stacks/tree/e2299cf97f975b08e7b5b59202ed00adc80ff6b7)

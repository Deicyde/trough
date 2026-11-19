---
declaration: module
origin: cited
lean: BondalThomsen
statement: formalized
---

# Exceptional Bondal–Thomsen Collections

[AxiomMath/BondalThomsen](https://github.com/AxiomMath/BondalThomsen) at commit [9a2bdcdc](https://github.com/AxiomMath/BondalThomsen/tree/9a2bdcdcf6b25710459f7f476c9c62de3039b7bb), 2026-10-03.

> This is a Lean formalization of the main results of Reginald Anderson, *Exceptionality, strongness, and asymptotic rarity for the Bondal–Thomsen collection* (preprint). Theorem numbers refer to that paper.

*Quoted from [README.md](https://github.com/AxiomMath/BondalThomsen/blob/9a2bdcdcf6b25710459f7f476c9c62de3039b7bb/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Salient cone](../convex-geometry/salient-cone.md)
- [Dual cone](../convex-geometry/dual-cone.md)
- [Hahn embedding theorem](../../../thousand-plus/combinatorics-and-ordered-structures/06-order-lattices-ordered-algebraic-structures/hahn-embedding-theorem.md)
- [Pointed cone](../convex-geometry/pointed-cone.md)
- [Orthogonal complement](../../analysis/hilbert-spaces/orthogonal-complement.md)
- [Convex cone](../convex-geometry/convex-cone.md)
- [Isomorphism](../../general-algebra/category-theory/isomorphism.md)
- [Basis](../../linear-algebra/fundamentals/basis.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`BondalThomsen`](https://github.com/AxiomMath/BondalThomsen/blob/9a2bdcdcf6b25710459f7f476c9c62de3039b7bb/BondalThomsen.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `Challenge/Basic.lean`, `Challenge/Defs/Collection/BondalThomsenClasses.lean`, `Challenge/Defs/Fan/Basic.lean`, `Challenge/Defs/Fan/CompleteFanGlobalFunctions.lean`, `Challenge/Defs/Fan/Completeness.lean`, `Challenge/Defs/Ports/MiyaokaMori/AmpleLineBundle.lean`, `Challenge/Defs/Ports/MiyaokaMori/LineBundleNonvanishingLocus.lean`, `Challenge/Defs/Ports/MiyaokaMori/ModulesTensorPower.lean`, `Challenge/Defs/Ports/TauCeti/Algebra/Category/ModuleCat/Sheaf/Invertible/Basic.lean`, `Challenge/Defs/Ports/TauCeti/Algebra/Category/ModuleCat/Sheaf/Invertible/TensorProduct/Closure.lean`, `Challenge/Defs/Ports/TauCeti/Algebra/Category/ModuleCat/Sheaf/TensorProduct/Associator.lean`, `Challenge/Defs/Ports/TauCeti/Algebra/Module/Primitive.lean`, `Challenge/Defs/Ports/TauCeti/AlgebraicGeometry/CartierDivisor/Basic.lean`, `Challenge/Defs/Ports/TauCeti/AlgebraicGeometry/CartierDivisor/Picard.lean`, `Challenge/Defs/Ports/TauCeti/AlgebraicGeometry/CartierDivisor/Representation.lean`, `Challenge/Defs/Ports/TauCeti/AlgebraicGeometry/CartierDivisor/Sheaf.lean`, `Challenge/Defs/Ports/TauCeti/AlgebraicGeometry/LineBundle/Basic.lean`, `Challenge/Defs/Ports/TauCeti/AlgebraicGeometry/LineBundle/Class.lean`, `Challenge/Defs/Ports/TauCeti/AlgebraicGeometry/LineBundle/TensorProduct.lean`, `Challenge/Defs/Ports/TauCeti/AlgebraicGeometry/Modules/GlobalSections.lean` hold `sorry` or `admit`.

## Project

- Lean v4.35.0-rc2, Mathlib at [b9be95a0](https://github.com/leanprover-community/mathlib4/tree/b9be95a02e0ca7f70ae4099c426ccdfdfb898dd2).
- 674 .lean files; its Lean libraries `BondalThomsen`, `Challenge`, `Solution` hold 674, declaring 5,652 names, with `sorry` in 36 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/BondalThomsen/blob/9a2bdcdcf6b25710459f7f476c9c62de3039b7bb/LICENSE)).

## Builds on

- Mathlib, at [b9be95a0](https://github.com/leanprover-community/mathlib4/tree/b9be95a02e0ca7f70ae4099c426ccdfdfb898dd2).

## Placement

Of its imports of Mathlib modules in an overview area, 681 of 5267 are in Geometry, 5.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (681 of 5267 imports, 5.5×), Linear algebra (1333 of 5267 imports, 4.3×), General algebra (2175 of 5267 imports, 1.2×). *Proof depends on* lists 8 of the 91 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [AxiomMath/BondalThomsen at 9a2bdcdc](https://github.com/AxiomMath/BondalThomsen/tree/9a2bdcdcf6b25710459f7f476c9c62de3039b7bb)

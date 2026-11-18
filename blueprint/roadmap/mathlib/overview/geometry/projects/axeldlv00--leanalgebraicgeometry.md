---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.fgaPicardRepresentability, AlgebraicGeometry.Scheme.picSchemeOfHasRationalPoint, AlgebraicGeometry.pullback_preservesFiniteLimits, AlgebraicGeometry.pullback_preservesMonomorphisms, AlgebraicGeometry.Scheme.PicScheme.picEt_isSheaf_forget, AlgebraicGeometry.Scheme.Pic0Et.geometricallyReduced, AlgebraicGeometry.Scheme.Pic0Et.universallyClosed, AlgebraicGeometry.smoothOfRelativeDimension_genus_pic0Et
statement: formalized
---

# LeanAlgebraicGeometry-Horizon

[AxelDlv00/LeanAlgebraicGeometry](https://github.com/AxelDlv00/LeanAlgebraicGeometry) at commit [8b42f4c3](https://github.com/AxelDlv00/LeanAlgebraicGeometry/tree/8b42f4c3410e1ebf3ef450be3c784e50951b6231), 2026-10-13.

> Lean 4 and Mathlib formalizations in algebraic geometry, coordinated with [Archon Horizon](https://github.com/frenzymath/Archon-Horizon). The main objective is the Algebraic Jacobian challenge: construct the Jacobian of a smooth proper geometrically integral curve and verify its universal, geometric, functorial, and base-change properties.

*Quoted from [README.md](https://github.com/AxelDlv00/LeanAlgebraicGeometry/blob/8b42f4c3410e1ebf3ef450be3c784e50951b6231/README.md), Apache-2.0.*

## Depends on

- [33.9 Geometrically integral schemes](../../../../stacks/schemes/33-varieties/part-01/33-9-geometrically-integral-schemes.md)
- [29.42 Proper morphisms](../../../../stacks/schemes/29-morphisms-of-schemes/part-03/29-42-proper-morphisms.md)
- [26.21 Separation axioms](../../../../stacks/schemes/26-schemes/part-02/26-21-separation-axioms.md)
- [29.15 Morphisms of finite type](../../../../stacks/schemes/29-morphisms-of-schemes/part-01/29-15-morphisms-of-finite-type.md)
- [26.18 Base change in algebraic geometry](../../../../stacks/schemes/26-schemes/part-01/26-18-base-change-in-algebraic-geometry.md)
- [Field](../../general-algebra/field-theory/field.md)
- [4.2 Definitions](../../../../stacks/preliminaries/part-01/4-categories/part-01/4-2-definitions.md)
- [29.26 Flat morphisms](../../../../stacks/schemes/29-morphisms-of-schemes/part-02/29-26-flat-morphisms.md)
- [59.11 Sheaves](../../../../stacks/topics-in-scheme-theory/part-01/59-etale-cohomology/part-01/59-11-sheaves.md)
- [26.20 Valuative criterion for universal closedness](../../../../stacks/schemes/26-schemes/part-01/26-20-valuative-criterion-for-universal-closedne.md)
- [44.6 The Picard scheme of a curve](../../../../stacks/topics-in-scheme-theory/part-01/44-picard-schemes-of-curves/44-6-the-picard-scheme-of-a-curve.md)

## Proof depends on

- [Yoneda embedding](../../general-algebra/category-theory/yoneda-embedding.md)
- [Principal ideal domain](../../general-algebra/divisibility-in-integral-domains/principal-ideal-domain.md)
- [Adjunction](../../general-algebra/category-theory/adjunction.md)
- [Cramer’s Rule](../../../hundred-theorems/part-04/cramers-rule.md)
- [Prime spectrum](../algebraic-geometry/prime-spectrum.md)
- [The category of rings](../../general-algebra/rings/the-category-of-rings.md)
- [Scheme](../algebraic-geometry/scheme.md)
- [Existence of bases](../../../undergraduate/linear-algebra/fundamentals/existence-of-bases.md)

## Main results

Its Lean names are 8 of the 13 theorems its README names in code:

- [`AlgebraicGeometry.Scheme.fgaPicardRepresentability`](https://github.com/AxelDlv00/LeanAlgebraicGeometry/blob/8b42f4c3410e1ebf3ef450be3c784e50951b6231/MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Picard/FGAPicRepresentability.lean#L955) (theorem, its text holds `sorry`)
- [`AlgebraicGeometry.Scheme.picSchemeOfHasRationalPoint`](https://github.com/AxelDlv00/LeanAlgebraicGeometry/blob/8b42f4c3410e1ebf3ef450be3c784e50951b6231/MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Picard/FGAPicRepresentability.lean#L1212) (theorem)
- [`AlgebraicGeometry.pullback_preservesFiniteLimits`](https://github.com/AxelDlv00/LeanAlgebraicGeometry/blob/8b42f4c3410e1ebf3ef450be3c784e50951b6231/MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Cohomology/CechHigherDirectImageUnconditional.lean#L974) (theorem)
- [`AlgebraicGeometry.pullback_preservesMonomorphisms`](https://github.com/AxelDlv00/LeanAlgebraicGeometry/blob/8b42f4c3410e1ebf3ef450be3c784e50951b6231/MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Cohomology/CechHigherDirectImageUnconditional.lean#L953) (theorem, its text holds `sorry`)
- [`AlgebraicGeometry.Scheme.PicScheme.picEt_isSheaf_forget`](https://github.com/AxelDlv00/LeanAlgebraicGeometry/blob/8b42f4c3410e1ebf3ef450be3c784e50951b6231/MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Picard/PicEtSheaf.lean#L290) (theorem)
- [`AlgebraicGeometry.Scheme.Pic0Et.geometricallyReduced`](https://github.com/AxelDlv00/LeanAlgebraicGeometry/blob/8b42f4c3410e1ebf3ef450be3c784e50951b6231/MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Picard/Pic0Et.lean#L170) (theorem, its text holds `sorry`)
- [`AlgebraicGeometry.Scheme.Pic0Et.universallyClosed`](https://github.com/AxelDlv00/LeanAlgebraicGeometry/blob/8b42f4c3410e1ebf3ef450be3c784e50951b6231/MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Picard/Pic0Et.lean#L223) (theorem, its text holds `sorry`)
- [`AlgebraicGeometry.smoothOfRelativeDimension_genus_pic0Et`](https://github.com/AxelDlv00/LeanAlgebraicGeometry/blob/8b42f4c3410e1ebf3ef450be3c784e50951b6231/MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Jacobian.lean#L548) (theorem, its text holds `sorry`)

Of the files its headlines import, directly or not, `MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Albanese/AlbaneseUP.lean`, `MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Cohomology/CechHigherDirectImageUnconditional.lean`, `MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Jacobian.lean`, `MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Picard/FGAPicRepresentability.lean`, `MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Picard/IdentityComponent.lean`, `MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Picard/Pic0AbelianVariety.lean`, `MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Picard/Pic0Et.lean`, `MainProjects/Algebraic-Jacobian-Challenge/AlgebraicJacobian/Picard/QuotFunctorDef.lean` hold `sorry` or `admit`.

## Project

- Lean v4.31.0, Mathlib at [fabf563a](https://github.com/leanprover-community/mathlib4/tree/fabf563a7c95a166b8d7b6efca11c8b4dc9d911f).
- 2,452 .lean files; its Lean libraries `AlgebraicJacobian` hold 409, declaring 6,394 names, with `sorry` in 11 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/AxelDlv00/LeanAlgebraicGeometry/blob/8b42f4c3410e1ebf3ef450be3c784e50951b6231/LICENSE)).

## Builds on

- Mathlib, at [fabf563a](https://github.com/leanprover-community/mathlib4/tree/fabf563a7c95a166b8d7b6efca11c8b4dc9d911f).

## Placement

Of its imports of Mathlib modules in an overview area, 81 of 393 are in Geometry, 8.7 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (81 of 393 imports, 8.7×), Linear algebra (47 of 393 imports, 2.0×), General algebra (216 of 393 imports, 1.5×). *Proof depends on* names 8 of the 71 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [AxelDlv00/LeanAlgebraicGeometry at 8b42f4c3](https://github.com/AxelDlv00/LeanAlgebraicGeometry/tree/8b42f4c3410e1ebf3ef450be3c784e50951b6231)

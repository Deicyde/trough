---
declaration: theorem
origin: cited
lean: RRC.GrothendieckRiemannRoch, RRC.GrothendieckRiemannRoch_smooth, SchemeKTheory.TF7.grr_chow_intrinsic, RRC.fShriek_eq_alternatingSum_directImages, RRC.adamsRiemannRoch, RRC.adamsRiemannRoch_smooth, CAN.adamsRiemannRoch_forall, M1.adamsRiemannRoch_baseRing
statement: formalized
proof: formalized
---

# Grothendieck–Riemann–Roch, Formalized in Lean 4

[vaca22/grothendieck-riemann-roch](https://github.com/vaca22/grothendieck-riemann-roch) at commit [053ea2fb](https://github.com/vaca22/grothendieck-riemann-roch/tree/053ea2fbd24c2f675a28393a4e7b7af9fe4ae626), 2026-10-07.

> **A machine-checked formalization of the Grothendieck–Riemann–Roch theorem for projective morphisms of projective varieties, together with Adams–Riemann–Roch, a truncated form of the SGA 6 γ-graded theorem, the lci (possibly singular source) case, and a Baum–Fulton–MacPherson singular Todd transformation — built on Lean 4 and Mathlib.** The precise scope (projective schemes, rational coefficients, an infinite base field on the Chow side) is stated in §4 and §5.

*Quoted from [README.md](https://github.com/vaca22/grothendieck-riemann-roch/blob/053ea2fbd24c2f675a28393a4e7b7af9fe4ae626/README.md), Apache-2.0.*

## Depends on

- [29.42 Proper morphisms](../../../../stacks/schemes/29-morphisms-of-schemes/part-03/29-42-proper-morphisms.md)
- [12.3 Preadditive and additive categories](../../../../stacks/preliminaries/part-01/12-homological-algebra/part-01/12-3-preadditive-and-additive-categories.md)
- [28.3 Integral, irreducible, and reduced schemes](../../../../stacks/schemes/28-properties-of-schemes/part-01/28-3-integral-irreducible-and-reduced-schemes.md)
- [26.17 Fibre products of schemes](../../../../stacks/schemes/26-schemes/part-01/26-17-fibre-products-of-schemes.md)

## Proof depends on

- [Vieta's formulas](../../../thousand-plus/algebra/13-commutative-algebra/vietas-formulas.md)
- [Noetherian module](../../linear-algebra/fundamentals/noetherian-module.md)
- [Principal ideal domain](../../general-algebra/divisibility-in-integral-domains/principal-ideal-domain.md)
- [Scheme](../algebraic-geometry/scheme.md)
- [First isomorphism theorem for commutative rings](../../general-algebra/ideals-and-quotients/first-isomorphism-theorem-for-commutative-rings.md)
- [Isomorphism](../../general-algebra/category-theory/isomorphism.md)
- [The category of rings](../../general-algebra/rings/the-category-of-rings.md)
- [Krull's principal ideal theorem](../../../thousand-plus/algebra/13-commutative-algebra/krulls-principal-ideal-theorem.md)

## Main results

Its Lean names are 8 of the 39 theorems its README names in code:

- [`RRC.GrothendieckRiemannRoch`](https://github.com/vaca22/grothendieck-riemann-roch/blob/053ea2fbd24c2f675a28393a4e7b7af9fe4ae626/RiemannRoch/GRRHeadline.lean#L210) (theorem)
- [`RRC.GrothendieckRiemannRoch_smooth`](https://github.com/vaca22/grothendieck-riemann-roch/blob/053ea2fbd24c2f675a28393a4e7b7af9fe4ae626/RiemannRoch/Foundations/SmoothRegularStalksCorollaries.lean#L96) (theorem)
- [`SchemeKTheory.TF7.grr_chow_intrinsic`](https://github.com/vaca22/grothendieck-riemann-roch/blob/053ea2fbd24c2f675a28393a4e7b7af9fe4ae626/RiemannRoch/RelativeRiemannRoch/TangentVirtualTF7.lean#L135) (theorem)
- [`RRC.fShriek_eq_alternatingSum_directImages`](https://github.com/vaca22/grothendieck-riemann-roch/blob/053ea2fbd24c2f675a28393a4e7b7af9fe4ae626/RiemannRoch/GRRHeadline.lean#L245) (theorem)
- [`RRC.adamsRiemannRoch`](https://github.com/vaca22/grothendieck-riemann-roch/blob/053ea2fbd24c2f675a28393a4e7b7af9fe4ae626/RiemannRoch/GRRHeadline.lean#L232) (theorem)
- [`RRC.adamsRiemannRoch_smooth`](https://github.com/vaca22/grothendieck-riemann-roch/blob/053ea2fbd24c2f675a28393a4e7b7af9fe4ae626/RiemannRoch/Foundations/SmoothRegularHeadlines.lean#L51) (theorem)
- [`CAN.adamsRiemannRoch_forall`](https://github.com/vaca22/grothendieck-riemann-roch/blob/053ea2fbd24c2f675a28393a4e7b7af9fe4ae626/RiemannRoch/RelativeRiemannRoch/GRRCanonicalCAN.lean#L88) (theorem)
- [`M1.adamsRiemannRoch_baseRing`](https://github.com/vaca22/grothendieck-riemann-roch/blob/053ea2fbd24c2f675a28393a4e7b7af9fe4ae626/RiemannRoch/RelativeRiemannRoch/AdamsRRBaseRingM1.lean#L108) (theorem)

No file its headlines import, directly or not (1401 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.32.0-rc1, Mathlib at [38ddc377](https://github.com/leanprover-community/mathlib4/tree/38ddc37712cd7d933337d25033ab2197f48895a1).
- 1,718 .lean files; its Lean libraries `RiemannRoch`, `GRR` hold 1,718, declaring 29,794 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/vaca22/grothendieck-riemann-roch/blob/053ea2fbd24c2f675a28393a4e7b7af9fe4ae626/LICENSE)).

## Builds on

- Mathlib, at [38ddc377](https://github.com/leanprover-community/mathlib4/tree/38ddc37712cd7d933337d25033ab2197f48895a1).

## Placement

Of its imports of Mathlib modules in an overview area, 185 of 979 are in Geometry, 8.0 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (185 of 979 imports, 8.0×), Linear algebra (144 of 979 imports, 2.5×), General algebra (606 of 979 imports, 1.7×). *Proof depends on* lists 8 of the 97 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [vaca22/grothendieck-riemann-roch at 053ea2fb](https://github.com/vaca22/grothendieck-riemann-roch/tree/053ea2fbd24c2f675a28393a4e7b7af9fe4ae626)

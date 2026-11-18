---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.HasIntegratedByPartsFormula, ClassicalFieldTheory.Local.HasTermwiseIntegratedByPartsFormula, ClassicalFieldTheory.Local.integral_mul_iteratedDeriv_eq_sign, ClassicalFieldTheory.Local.hasTermwiseIntegratedByPartsFormula_of_contDiff_coordDeriv, ClassicalFieldTheory.Local.hasTermwiseIntegratedByPartsFormula_of_regular, ClassicalFieldTheory.Local.hasIntegratedByPartsFormula_of_termwise
statement: formalized
proof: formalized
---

# First variation integration by parts

The module `PhyslibAlpha.ClassicalFieldTheory.Local.FirstVariation.IntegrationByParts`, [PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/IntegrationByParts.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/IntegrationByParts.lean): 6 declarations, 4 with a docstring; 4 private, not shown.

> Repeated integration by parts for the local first-variation formula.

## i. Overview

> This module contains the repeated integration-by-parts step needed for the local first-variation
> formula, together with the termwise and summed packaged versions used later in the
> Euler-Lagrange criterion.

## ii. Key results

> - `ClassicalFieldTheory.Local.integral_mul_iteratedDeriv_eq_sign`
> - `ClassicalFieldTheory.Local.hasTermwiseIntegratedByPartsFormula_of_regular`
> - `ClassicalFieldTheory.Local.hasIntegratedByPartsFormula_of_termwise`

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics, Chapter 5,
>   Theorem 5.2. [ref: cortes\_haupt\_2016]

## A. Repeated integration by parts

**`ClassicalFieldTheory.Local.HasIntegratedByPartsFormula`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/IntegrationByParts.lean#L53).

> The integration-by-parts step sending the linearized density to the Euler-Lagrange pairing.

```lean
def HasIntegratedByPartsFormula (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Prop
```

**`ClassicalFieldTheory.Local.HasTermwiseIntegratedByPartsFormula`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/IntegrationByParts.lean#L59).

> Termwise integration-by-parts data for the linearized first-variation density.

```lean
def HasTermwiseIntegratedByPartsFormula (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Prop
```

**`ClassicalFieldTheory.Local.integral_mul_iteratedDeriv_eq_sign`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/IntegrationByParts.lean#L123).

> Repeated integration by parts for iterated coordinate derivatives against a test function.

```lean
lemma integral_mul_iteratedDeriv_eq_sign {g h : Space d → ℝ} (I : MultiIndex d)
    (hg : ContDiff ℝ ∞ g) (hh : IsTestFunction h) :
    ∫ x, g x * ∂^[I] h x =
      ∫ x, (((-1 : ℝ) ^ I.order) * ∂^[I] g x) * h x
```

## B. Termwise formulas

**`ClassicalFieldTheory.Local.hasTermwiseIntegratedByPartsFormula_of_contDiff_coordDeriv`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/IntegrationByParts.lean#L137).

> Concrete termwise integration by parts for the first-variation density, assuming the jet
> coordinate coefficient functions are smooth along the field.

```lean
lemma hasTermwiseIntegratedByPartsFormula_of_contDiff_coordDeriv
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (hcoeff : ∀ I : DerivativeIndex d k, ∀ a : Fin m,
      ContDiff ℝ ∞ (fun x => L.coordDeriv I a (jetAt k f x))) :
    HasTermwiseIntegratedByPartsFormula L f
```

**`ClassicalFieldTheory.Local.hasTermwiseIntegratedByPartsFormula_of_regular`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/IntegrationByParts.lean#L165).

```lean
lemma hasTermwiseIntegratedByPartsFormula_of_regular
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (hcoeff : Lagrangian.ContDiffCoordDerivAlongField L f) :
    HasTermwiseIntegratedByPartsFormula L f
```

**`ClassicalFieldTheory.Local.hasIntegratedByPartsFormula_of_termwise`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/IntegrationByParts.lean#L234).

```lean
lemma hasIntegratedByPartsFormula_of_termwise (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (hterm : HasTermwiseIntegratedByPartsFormula L f) :
    HasIntegratedByPartsFormula L f
```

## Depends on

- [First variation core objects](firstvariation-basic.md)

## Proof depends on

- [First variation support lemmas](firstvariation-support.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/IntegrationByParts.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/IntegrationByParts.lean)

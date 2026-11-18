---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.isCritical_iff_eulerLagrange_zero, ClassicalFieldTheory.Local.AllVariationsHaveFiniteAction, ClassicalFieldTheory.Local.HasFirstVariationFormula, ClassicalFieldTheory.Local.isCritical_of_eulerLagrange_zero, ClassicalFieldTheory.Local.eulerLagrange_zero_of_isCritical, ClassicalFieldTheory.Local.isCritical_iff_eulerLagrange_zero_of_hasFiniteAction_and_continuousInCoordinates
statement: formalized
proof: formalized
---

# First variation criteria

The module `PhyslibAlpha.ClassicalFieldTheory.Local.FirstVariation.Criterion`, [PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Criterion.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Criterion.lean): 6 declarations, 3 with a docstring, 1 listed as significant; 16 private, not shown.

> Assembles the first-variation formula into Euler-Lagrange criteria for critical fields.

## i. Overview

> This module assembles the analytic ingredients of the local first-variation proof into the
> packaged first-variation formula and the internal Euler-Lagrange criteria used by the public
> facade.

## ii. Key results

> - `ClassicalFieldTheory.Local.
>   isCritical\_iff\_eulerLagrange\_zero\_of\_hasFiniteAction\_and\_continuousInCoordinates`

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics, Chapter 5,
>   Theorem 5.2. [ref: cortes\_haupt\_2016]

## A. First-variation assembly

**`ClassicalFieldTheory.Local.AllVariationsHaveFiniteAction`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Criterion.lean#L54).

> Explicit global finiteness hypothesis for all admissible variations.

```lean
def AllVariationsHaveFiniteAction (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Prop
```

**`ClassicalFieldTheory.Local.HasFirstVariationFormula`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Criterion.lean#L59).

> The first-variation formula for the local action, packaged as a reusable hypothesis.

```lean
def HasFirstVariationFormula (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Prop
```

**`ClassicalFieldTheory.Local.isCritical_of_eulerLagrange_zero`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Criterion.lean#L64).

```lean
lemma isCritical_of_eulerLagrange_zero (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (hfirst : HasFirstVariationFormula L f) (hEuler : eulerLagrangeOp L f = 0) :
    IsCritical L f
```

**`ClassicalFieldTheory.Local.eulerLagrange_zero_of_isCritical`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Criterion.lean#L75).

```lean
lemma eulerLagrange_zero_of_isCritical (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (hfirst : HasFirstVariationFormula L f)
    (hfin : AllVariationsHaveFiniteAction L f)
    (hcont : Continuous (eulerLagrangeOp L f))
    (hcrit : IsCritical L f) :
    eulerLagrangeOp L f = 0
```

**`ClassicalFieldTheory.Local.isCritical_iff_eulerLagrange_zero`**, a theorem, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Criterion.lean#L94). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A criterion for a field to be critical in terms of the Euler-Lagrange operator.

```lean
theorem isCritical_iff_eulerLagrange_zero (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (hfirst : HasFirstVariationFormula L f)
    (hfin : AllVariationsHaveFiniteAction L f)
    (hcont : Continuous (eulerLagrangeOp L f)) :
    IsCritical L f ↔ eulerLagrangeOp L f = 0
```

## B. Intermediate Euler-Lagrange criteria

**`ClassicalFieldTheory.Local.isCritical_iff_eulerLagrange_zero_of_hasFiniteAction_and_continuousInCoordinates`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Criterion.lean#L288).

```lean
lemma isCritical_iff_eulerLagrange_zero_of_hasFiniteAction_and_continuousInCoordinates
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m)) (hf : ContDiff ℝ ∞ f)
    (hcoord : Lagrangian.ContDiffCoordDerivInCoordinates L)
    (hcontL : Lagrangian.ContinuousInCoordinates L)
    (hbase : HasFiniteAction L f) :
    IsCritical L f ↔ eulerLagrangeOp L f = 0
```

## Depends on

- [Local action functionals](action.md)
- [First variation core objects](firstvariation-basic.md)

## Proof depends on

- [Fundamental lemma of the calculus of variations](../../../physlib/mathematics/variationalcalculus/basic.md)
- [First variation density formulas](firstvariation-density.md)
- [First variation integration by parts](firstvariation-integrationbyparts.md)
- [First variation regularity](firstvariation-regularity.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Criterion.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Criterion.lean)

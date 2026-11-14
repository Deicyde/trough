---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.hasSmoothEulerLagrangeRegularity_of_smoothInCoordinates, ClassicalFieldTheory.Local.isCritical_iff_eulerLagrange_zero_of_contDiff_and_smoothInCoordinates, ClassicalFieldTheory.Local.isCritical_iff_eulerLagrange_zero_of_admissibleForAction_and_smoothInCoordinates
statement: formalized
proof: formalized
---

# First variation and the Euler-Lagrange criterion

The module `PhyslibAlpha.ClassicalFieldTheory.Local.FirstVariation`, [PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation.lean): 3 declarations, none with a docstring.

> Public entry point: a field is critical iff its local Euler-Lagrange operator vanishes.

## i. Overview

> This module is the public entry point for the local first-variation theory. The core linearized
> density objects live in `FirstVariation.Basic`, the analytic derivation tools and packaged
> hypotheses live in `FirstVariation.Density`, `FirstVariation.IntegrationByParts`,
> `FirstVariation.Regularity`, and `FirstVariation.Criterion`, and this file exposes the cleanest
> surface-level statements of the local Euler-Lagrange criterion.

## ii. Key results

> - `ClassicalFieldTheory.Local.hasSmoothEulerLagrangeRegularity_of_smoothInCoordinates`
> - `ClassicalFieldTheory.Local.isCritical_iff_eulerLagrange_zero_of_contDiff_and_smoothInCoordinates`
> - `ClassicalFieldTheory.Local.
>   isCritical\_iff\_eulerLagrange\_zero\_of\_admissibleForAction\_and\_smoothInCoordinates`

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics, Chapter 5,
>   Theorem 5.2. [ref: cortes\_haupt\_2016]

## A. Smooth-coordinate regularity

**`ClassicalFieldTheory.Local.hasSmoothEulerLagrangeRegularity_of_smoothInCoordinates`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation.lean#L52).

```lean
lemma hasSmoothEulerLagrangeRegularity_of_smoothInCoordinates
    (L : Lagrangian d m k) (hL : Lagrangian.SmoothInCoordinates L) :
    HasSmoothEulerLagrangeRegularity L
```

## B. Final Euler-Lagrange criteria

**`ClassicalFieldTheory.Local.isCritical_iff_eulerLagrange_zero_of_contDiff_and_smoothInCoordinates`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation.lean#L62).

```lean
lemma isCritical_iff_eulerLagrange_zero_of_contDiff_and_smoothInCoordinates
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m)) (hf : ContDiff ℝ ∞ f)
    (hL : Lagrangian.SmoothInCoordinates L)
    (hbase : HasFiniteAction L f) :
    IsCritical L f ↔ eulerLagrangeOp L f = 0
```

**`ClassicalFieldTheory.Local.isCritical_iff_eulerLagrange_zero_of_admissibleForAction_and_smoothInCoordinates`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation.lean#L71).

```lean
lemma isCritical_iff_eulerLagrange_zero_of_admissibleForAction_and_smoothInCoordinates
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (hLf : IsAdmissibleForAction L f)
    (hL : Lagrangian.SmoothInCoordinates L) :
    IsCritical L f ↔ eulerLagrangeOp L f = 0
```

## Depends on

- [First variation regularity](firstvariation-regularity.md)

## Proof depends on

- [First variation criteria](firstvariation-criterion.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation.lean)

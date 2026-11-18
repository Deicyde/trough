---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.HasEulerLagrangeRegularityAt, ClassicalFieldTheory.Local.HasSmoothEulerLagrangeRegularity, ClassicalFieldTheory.Local.continuous_eulerLagrangeTerm_of_regular, ClassicalFieldTheory.Local.continuous_eulerLagrangeComponent_of_regular, ClassicalFieldTheory.Local.continuous_eulerLagrangeOp_of_regular, ClassicalFieldTheory.Local.hasSmoothEulerLagrangeRegularity_of_contDiffCoordDerivInCoordinates
statement: formalized
proof: formalized
---

# First variation regularity

The module `PhyslibAlpha.ClassicalFieldTheory.Local.FirstVariation.Regularity`, [PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Regularity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Regularity.lean): 6 declarations, 2 with a docstring.

> Continuity of the Euler-Lagrange operator and smooth regularity from coordinate regularity.

## i. Overview

> This module contains regularity consequences used in the local Euler-Lagrange criterion: continuity
> of the Euler-Lagrange operator from coefficient regularity, and the bridge from coordinate
> regularity of the local Lagrangian to the packaged smooth-regularity statement.

## ii. Key results

> - `ClassicalFieldTheory.Local.continuous_eulerLagrangeOp_of_regular`
> - `ClassicalFieldTheory.Local.hasSmoothEulerLagrangeRegularity_of_contDiffCoordDerivInCoordinates`

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics, Chapter 5,
>   Theorem 5.2. [ref: cortes\_haupt\_2016]

## A. Continuity of the Euler-Lagrange operator

**`ClassicalFieldTheory.Local.HasEulerLagrangeRegularityAt`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Regularity.lean#L54).

> The combined regularity package currently needed to derive the local Euler-Lagrange
> criterion for a field `f`: smooth coefficient functions along `f`, and continuity of the
> corresponding coefficient families along every admissible varied-field family based at `f`.

```lean
def HasEulerLagrangeRegularityAt (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Prop
```

**`ClassicalFieldTheory.Local.HasSmoothEulerLagrangeRegularity`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Regularity.lean#L62).

> A local Lagrangian has smooth Euler-Lagrange regularity if every smooth field satisfies the
> regularity package currently needed by the local first-variation proof.

```lean
def HasSmoothEulerLagrangeRegularity (L : Lagrangian d m k) : Prop
```

**`ClassicalFieldTheory.Local.continuous_eulerLagrangeTerm_of_regular`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Regularity.lean#L66).

```lean
lemma continuous_eulerLagrangeTerm_of_regular
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (hcoeff : Lagrangian.ContDiffCoordDerivAlongField L f)
    (I : DerivativeIndex d k) (a : Fin m) :
    Continuous (eulerLagrangeTerm L I a f)
```

**`ClassicalFieldTheory.Local.continuous_eulerLagrangeComponent_of_regular`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Regularity.lean#L80).

```lean
lemma continuous_eulerLagrangeComponent_of_regular
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (hcoeff : Lagrangian.ContDiffCoordDerivAlongField L f)
    (a : Fin m) :
    Continuous (eulerLagrangeComponent L a f)
```

**`ClassicalFieldTheory.Local.continuous_eulerLagrangeOp_of_regular`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Regularity.lean#L89).

```lean
lemma continuous_eulerLagrangeOp_of_regular
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (hcoeff : Lagrangian.ContDiffCoordDerivAlongField L f) :
    Continuous (eulerLagrangeOp L f)
```

## B. Smooth regularity in coordinates

**`ClassicalFieldTheory.Local.hasSmoothEulerLagrangeRegularity_of_contDiffCoordDerivInCoordinates`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Regularity.lean#L104).

```lean
lemma hasSmoothEulerLagrangeRegularity_of_contDiffCoordDerivInCoordinates
    (L : Lagrangian d m k) (hcoord : Lagrangian.ContDiffCoordDerivInCoordinates L) :
    HasSmoothEulerLagrangeRegularity L
```

## Depends on

- [Local action functionals](action.md)
- [Local Euler-Lagrange operators](eulerlagrange.md)

## Proof depends on

- [First variation support lemmas](firstvariation-support.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Regularity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Regularity.lean)

---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.SatisfiesEulerLagrange, ClassicalFieldTheory.Local.satisfiesEulerLagrange_iff, ClassicalFieldTheory.Local.SatisfiesEulerLagrange.eulerLagrangeOp_eq_zero, ClassicalFieldTheory.Local.SatisfiesEulerLagrange.of_eulerLagrangeOp_eq_zero, ClassicalFieldTheory.Local.isCritical_iff_satisfiesEulerLagrange_of_contDiff_and_smoothInCoordinates, ClassicalFieldTheory.Local.isCritical_iff_satisfiesEulerLagrange_of_admissibleForAction_and_smoothInCoordinates
statement: formalized
proof: formalized
---

# Local Euler-Lagrange equations

The module `PhyslibAlpha.ClassicalFieldTheory.Local.EulerLagrangeEquation`, [PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrangeEquation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrangeEquation.lean): 6 declarations, 1 with a docstring.

> A named predicate for the local Euler-Lagrange equations and the criticality criteria using it.

## i. Overview

> This module gives a named predicate for fields satisfying the local Euler-Lagrange equations.
>
> The equation itself is still the existing local coordinate equation
>
> `eulerLagrangeOp L f = 0`.
>
> The purpose of this file is only to expose that condition as a reusable API point and to restate
> the already-proved criticality criteria using this named predicate. It does not introduce a new
> Euler-Lagrange operator or any new analytic hypotheses.

## ii. Key results

> - `ClassicalFieldTheory.Local.SatisfiesEulerLagrange`
> - `ClassicalFieldTheory.Local.
>   isCritical\_iff\_satisfiesEulerLagrange\_of\_contDiff\_and\_smoothInCoordinates`
> - `ClassicalFieldTheory.Local.
>   isCritical\_iff\_satisfiesEulerLagrange\_of\_admissibleForAction\_and\_smoothInCoordinates`

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics,
>   arXiv:1612.03100v2, Chapter 5, Theorem 5.2. [ref: cortes\_haupt\_2016]

## A. Euler-Lagrange equation predicate

**`ClassicalFieldTheory.Local.SatisfiesEulerLagrange`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrangeEquation.lean#L59).

> A field satisfies the local Euler-Lagrange equations for a local lagrangian when the
> Euler-Lagrange operator vanishes along that field.

```lean
def SatisfiesEulerLagrange (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Prop
```

**`ClassicalFieldTheory.Local.satisfiesEulerLagrange_iff`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrangeEquation.lean#L64).

```lean
lemma satisfiesEulerLagrange_iff (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) :
    SatisfiesEulerLagrange L f ↔ eulerLagrangeOp L f = 0
```

**`ClassicalFieldTheory.Local.SatisfiesEulerLagrange.eulerLagrangeOp_eq_zero`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrangeEquation.lean#L69).

```lean
lemma SatisfiesEulerLagrange.eulerLagrangeOp_eq_zero
    {L : Lagrangian d m k} {f : Space d → EuclideanSpace ℝ (Fin m)}
    (h : SatisfiesEulerLagrange L f) :
    eulerLagrangeOp L f = 0
```

**`ClassicalFieldTheory.Local.SatisfiesEulerLagrange.of_eulerLagrangeOp_eq_zero`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrangeEquation.lean#L75).

```lean
lemma SatisfiesEulerLagrange.of_eulerLagrangeOp_eq_zero
    {L : Lagrangian d m k} {f : Space d → EuclideanSpace ℝ (Fin m)}
    (h : eulerLagrangeOp L f = 0) :
    SatisfiesEulerLagrange L f
```

## B. Criticality criteria

**`ClassicalFieldTheory.Local.isCritical_iff_satisfiesEulerLagrange_of_contDiff_and_smoothInCoordinates`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrangeEquation.lean#L86).

```lean
lemma isCritical_iff_satisfiesEulerLagrange_of_contDiff_and_smoothInCoordinates
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m)) (hf : ContDiff ℝ ∞ f)
    (hL : Lagrangian.SmoothInCoordinates L)
    (hbase : HasFiniteAction L f) :
    IsCritical L f ↔ SatisfiesEulerLagrange L f
```

**`ClassicalFieldTheory.Local.isCritical_iff_satisfiesEulerLagrange_of_admissibleForAction_and_smoothInCoordinates`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrangeEquation.lean#L93).

```lean
lemma isCritical_iff_satisfiesEulerLagrange_of_admissibleForAction_and_smoothInCoordinates
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (hLf : IsAdmissibleForAction L f)
    (hL : Lagrangian.SmoothInCoordinates L) :
    IsCritical L f ↔ SatisfiesEulerLagrange L f
```

## Depends on

- [Local action functionals](action.md)
- [Local Euler-Lagrange operators](eulerlagrange.md)

## Proof depends on

- [First variation and the Euler-Lagrange criterion](firstvariation.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrangeEquation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrangeEquation.lean)

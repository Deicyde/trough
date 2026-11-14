---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.HasTotalDivergenceDifference, ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent, ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.refl, ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.symm, ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.trans, ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.eulerLagrangeOp_eq, ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.eulerLagrangeOp_eq_zero_iff, ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.isCritical_iff
statement: formalized
proof: formalized
---

# Lagrangian equivalence up to total divergences

The module `PhyslibAlpha.ClassicalFieldTheory.Local.TotalDivergenceEquivalence`, [PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean): 17 declarations, 3 with a docstring.

> Lagrangians differing by a total divergence have the same Euler-Lagrange equations.

## i. Overview

> This module adds the local coordinate API for lagrangians that differ by a total divergence.
>
> In the current Alpha stack, local lagrangians carry their jet-coordinate derivatives explicitly.
> Consequently, this module does not construct the modified lagrangian by adding a current
> divergence syntactically. Instead, it packages the data needed by later equivalence results:
>
> - two local lagrangians of the same order,
> - a total-divergence lagrangian witnessing the density difference,
> - and equality of the corresponding Euler-Lagrange operators.
>
> This is the field-theory analogue of the classical fact that adding a total derivative or total
> divergence does not change the variational equations, while keeping the current API honest about
> which facts are data and which facts are proved.

## ii. Key results

> - `ClassicalFieldTheory.Local.HasTotalDivergenceDifference`
> - `ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent`
> - `ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.eulerLagrangeOp_eq_zero_iff`
> - `ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.isCritical_iff`
> - `ClassicalFieldTheory.Local.TotalDivergenceEquivalence`
> - `ClassicalFieldTheory.Local.TotalDivergenceEquivalence.isCritical_iff`

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics,
>   arXiv:1612.03100v2, Chapter 5. [ref: cortes\_haupt\_2016]

## A. Equivalence predicates

**`ClassicalFieldTheory.Local.HasTotalDivergenceDifference`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L65).

> A lagrangian `target` differs from `source` by the density of a packaged total divergence.
>
> The total divergence has current order `k`, hence its associated lagrangian and both compared
> lagrangians have order `k + 1`.

```lean
def HasTotalDivergenceDifference (source target : Lagrangian d m (k + 1))
    (T : TotalDivergence d m k) : Prop
```

**`ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L73).

> Two local lagrangians are Euler-Lagrange equivalent when they determine the same local
> Euler-Lagrange operator along every field.

```lean
def IsEulerLagrangeEquivalent (source target : Lagrangian d m k) : Prop
```

## B. Euler-Lagrange equivalence API

**`ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.refl`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L86).

```lean
lemma refl (L : Lagrangian d m k) : IsEulerLagrangeEquivalent L L
```

**`ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.symm`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L90).

```lean
lemma symm {L1 L2 : Lagrangian d m k} (h : IsEulerLagrangeEquivalent L1 L2) :
    IsEulerLagrangeEquivalent L2 L1
```

**`ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.trans`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L95).

```lean
lemma trans {L1 L2 L3 : Lagrangian d m k}
    (h12 : IsEulerLagrangeEquivalent L1 L2) (h23 : IsEulerLagrangeEquivalent L2 L3) :
    IsEulerLagrangeEquivalent L1 L3
```

**`ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.eulerLagrangeOp_eq`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L101).

```lean
lemma eulerLagrangeOp_eq {source target : Lagrangian d m k}
    (h : IsEulerLagrangeEquivalent source target)
    (f : Space d → EuclideanSpace ℝ (Fin m)) :
    eulerLagrangeOp target f = eulerLagrangeOp source f
```

**`ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.eulerLagrangeOp_eq_zero_iff`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L107).

```lean
lemma eulerLagrangeOp_eq_zero_iff {source target : Lagrangian d m k}
    (h : IsEulerLagrangeEquivalent source target)
    (f : Space d → EuclideanSpace ℝ (Fin m)) :
    eulerLagrangeOp target f = 0 ↔ eulerLagrangeOp source f = 0
```

**`ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.isCritical_iff`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L113).

```lean
lemma isCritical_iff {source target : Lagrangian d m k}
    (h : IsEulerLagrangeEquivalent source target)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (hsourcef : IsAdmissibleForAction source f)
    (htargetf : IsAdmissibleForAction target f)
    (hsource : Lagrangian.SmoothInCoordinates source)
    (htarget : Lagrangian.SmoothInCoordinates target) :
    IsCritical target f ↔ IsCritical source f
```

**`ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.isCritical_target_of_source`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L127).

```lean
lemma isCritical_target_of_source {source target : Lagrangian d m k}
    (h : IsEulerLagrangeEquivalent source target)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (hsourcef : IsAdmissibleForAction source f)
    (htargetf : IsAdmissibleForAction target f)
    (hsource : Lagrangian.SmoothInCoordinates source)
    (htarget : Lagrangian.SmoothInCoordinates target)
    (hcrit : IsCritical source f) :
    IsCritical target f
```

**`ClassicalFieldTheory.Local.IsEulerLagrangeEquivalent.isCritical_source_of_target`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L138).

```lean
lemma isCritical_source_of_target {source target : Lagrangian d m k}
    (h : IsEulerLagrangeEquivalent source target)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (hsourcef : IsAdmissibleForAction source f)
    (htargetf : IsAdmissibleForAction target f)
    (hsource : Lagrangian.SmoothInCoordinates source)
    (htarget : Lagrangian.SmoothInCoordinates target)
    (hcrit : IsCritical target f) :
    IsCritical source f
```

## C. Packaged total-divergence equivalences

**`ClassicalFieldTheory.Local.TotalDivergenceEquivalence`**, a structure, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L162).

> A packaged equivalence between two local lagrangians whose densities differ by a total
> divergence.
>
> The field `sameEulerLagrangeOp` records the variational consequence in the current Alpha API. It
> will become a theorem once the stack has enough symbolic calculus for coordinate derivatives of
> total divergences.

```lean
structure TotalDivergenceEquivalence (d m k : ℕ) where
  /-- The original local lagrangian. -/
  source : Lagrangian d m (k + 1)
  /-- The modified local lagrangian. -/
  target : Lagrangian d m (k + 1)
  /-- The total divergence giving the density difference. -/
  divergence : TotalDivergence d m k
  /-- The target density is the source density plus the total-divergence density. -/
  hasTotalDivergenceDifference :
    HasTotalDivergenceDifference source target divergence
  /-- The two lagrangians have the same Euler-Lagrange operator. -/
  sameEulerLagrangeOp : IsEulerLagrangeEquivalent source target
```

**`ClassicalFieldTheory.Local.TotalDivergenceEquivalence.actionDensity_eq`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L180).

```lean
lemma actionDensity_eq (E : TotalDivergenceEquivalence d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) :
    actionDensity E.target f =
      fun x => actionDensity E.source f x + actionDensity E.divergence.lagrangian f x
```

**`ClassicalFieldTheory.Local.TotalDivergenceEquivalence.eulerLagrangeOp_eq`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L186).

```lean
lemma eulerLagrangeOp_eq (E : TotalDivergenceEquivalence d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) :
    eulerLagrangeOp E.target f = eulerLagrangeOp E.source f
```

**`ClassicalFieldTheory.Local.TotalDivergenceEquivalence.eulerLagrangeOp_eq_zero_iff`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L191).

```lean
lemma eulerLagrangeOp_eq_zero_iff (E : TotalDivergenceEquivalence d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) :
    eulerLagrangeOp E.target f = 0 ↔ eulerLagrangeOp E.source f = 0
```

**`ClassicalFieldTheory.Local.TotalDivergenceEquivalence.isCritical_iff`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L196).

```lean
lemma isCritical_iff (E : TotalDivergenceEquivalence d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (hsourcef : IsAdmissibleForAction E.source f)
    (htargetf : IsAdmissibleForAction E.target f)
    (hsource : Lagrangian.SmoothInCoordinates E.source)
    (htarget : Lagrangian.SmoothInCoordinates E.target) :
    IsCritical E.target f ↔ IsCritical E.source f
```

**`ClassicalFieldTheory.Local.TotalDivergenceEquivalence.isCritical_target_of_source`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L205).

```lean
lemma isCritical_target_of_source (E : TotalDivergenceEquivalence d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (hsourcef : IsAdmissibleForAction E.source f)
    (htargetf : IsAdmissibleForAction E.target f)
    (hsource : Lagrangian.SmoothInCoordinates E.source)
    (htarget : Lagrangian.SmoothInCoordinates E.target)
    (hcrit : IsCritical E.source f) :
    IsCritical E.target f
```

**`ClassicalFieldTheory.Local.TotalDivergenceEquivalence.isCritical_source_of_target`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean#L215).

```lean
lemma isCritical_source_of_target (E : TotalDivergenceEquivalence d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (hsourcef : IsAdmissibleForAction E.source f)
    (htargetf : IsAdmissibleForAction E.target f)
    (hsource : Lagrangian.SmoothInCoordinates E.source)
    (htarget : Lagrangian.SmoothInCoordinates E.target)
    (hcrit : IsCritical E.target f) :
    IsCritical E.source f
```

## Depends on

- [Total divergences in local classical field theory](totaldivergence.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergenceEquivalence.lean)

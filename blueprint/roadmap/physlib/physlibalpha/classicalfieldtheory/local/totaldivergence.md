---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.HasTotalDivergenceDensity, ClassicalFieldTheory.Local.IsEulerLagrangeTrivial, ClassicalFieldTheory.Local.TotalDivergence, ClassicalFieldTheory.Local.TotalDivergence.actionDensity_eq, ClassicalFieldTheory.Local.TotalDivergence.eulerLagrangeOp_eq_zero, ClassicalFieldTheory.Local.TotalDivergence.isCritical
statement: formalized
proof: formalized
---

# Total divergences in local classical field theory

The module `PhyslibAlpha.ClassicalFieldTheory.Local.TotalDivergence`, [PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergence.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergence.lean): 7 declarations (1 instance with no name), 3 with a docstring.

> Packaged total-divergence Lagrangians and the Euler-Lagrange-triviality property.

## i. Overview

> This module introduces the local coordinate API for total-divergence lagrangians.
>
> If `Bᵢ` is a jet-dependent current of order `k`, its total divergence
>
> `∑ i, Dᵢ Bᵢ`
>
> is naturally a lagrangian density of order `k + 1`. In the current Alpha stack, local lagrangians
> carry their jet-coordinate derivatives as explicit data, so this module does not try to construct
> that lagrangian automatically from the current. Instead, it packages the data needed by later
> equivalence results:
>
> - a local lagrangian of order `k + 1`,
> - a current whose total divergence agrees with the lagrangian density along every field,
> - and the Euler-Lagrange-triviality property of that lagrangian.
>
> This keeps the API faithful to the standard total-divergence principle while avoiding premature
> symbolic calculus for coordinate derivatives of total derivatives.

## ii. Key results

> - `ClassicalFieldTheory.Local.HasTotalDivergenceDensity`
> - `ClassicalFieldTheory.Local.IsEulerLagrangeTrivial`
> - `ClassicalFieldTheory.Local.TotalDivergence`

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics,
>   arXiv:1612.03100v2, Chapter 5. [ref: cortes\_haupt\_2016]

## A. Total-divergence predicates

**`ClassicalFieldTheory.Local.HasTotalDivergenceDensity`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergence.lean#L67).

> A lagrangian density has total-divergence form if, along every field, it is the sum of the
> total derivatives of a jet-dependent current. A current of order `k` gives a density of order
> `k + 1`.

```lean
def HasTotalDivergenceDensity (L : Lagrangian d m (k + 1))
    (current : Fin d → JetPoint d m k → ℝ) : Prop
```

**`ClassicalFieldTheory.Local.IsEulerLagrangeTrivial`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergence.lean#L74).

> A local lagrangian is Euler-Lagrange-trivial if its Euler-Lagrange operator vanishes along
> every field.

```lean
def IsEulerLagrangeTrivial (L : Lagrangian d m k) : Prop
```

## B. Packaged total-divergence lagrangians

**`ClassicalFieldTheory.Local.TotalDivergence`**, a structure, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergence.lean#L87).

> A packaged local total divergence.
>
> The current has order `k`, while the associated lagrangian has order `k + 1`, matching the
> coordinate expression `L = ∑ i, Dᵢ Bᵢ`. The Euler-Lagrange-triviality field records the
> variationally trivial direction needed by later equivalence results.

```lean
structure TotalDivergence (d m k : ℕ) where
  /-- The lagrangian represented by the total divergence of the current. -/
  lagrangian : Lagrangian d m (k + 1)
  /-- The current whose total divergence gives the lagrangian density. -/
  current : Fin d → JetPoint d m k → ℝ
  /-- The density agrees with the total divergence of the current along every field. -/
  hasTotalDivergenceDensity : HasTotalDivergenceDensity lagrangian current
  /-- The associated lagrangian is recorded as Euler-Lagrange-trivial. -/
  isEulerLagrangeTrivial : IsEulerLagrangeTrivial lagrangian
```

**An instance with no name**, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergence.lean#L101).

```lean
instance : CoeFun (TotalDivergence d m k) (fun _ => Lagrangian d m (k + 1))
```

**`ClassicalFieldTheory.Local.TotalDivergence.actionDensity_eq`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergence.lean#L105).

```lean
lemma actionDensity_eq (T : TotalDivergence d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) :
    actionDensity T.lagrangian f =
      fun x => ∑ i : Fin d, totalDerivative k i (T.current i) f x
```

**`ClassicalFieldTheory.Local.TotalDivergence.eulerLagrangeOp_eq_zero`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergence.lean#L111).

```lean
lemma eulerLagrangeOp_eq_zero (T : TotalDivergence d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) :
    eulerLagrangeOp T.lagrangian f = 0
```

**`ClassicalFieldTheory.Local.TotalDivergence.isCritical`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergence.lean#L116).

```lean
lemma isCritical (T : TotalDivergence d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (hTf : IsAdmissibleForAction T.lagrangian f)
    (hT : Lagrangian.SmoothInCoordinates T.lagrangian) :
    IsCritical T.lagrangian f
```

## Depends on

- [Local action functionals](action.md)
- [Local Euler-Lagrange operators](eulerlagrange.md)

## Proof depends on

- [First variation and the Euler-Lagrange criterion](firstvariation.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergence.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDivergence.lean)

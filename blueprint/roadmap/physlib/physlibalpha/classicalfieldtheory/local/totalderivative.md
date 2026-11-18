---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.evalOnJet, ClassicalFieldTheory.Local.totalDerivative, ClassicalFieldTheory.Local.iteratedTotalDerivative, ClassicalFieldTheory.Local.evalOnJet_apply, ClassicalFieldTheory.Local.totalDerivative_eq, ClassicalFieldTheory.Local.iteratedTotalDerivative_eq, ClassicalFieldTheory.Local.iteratedTotalDerivative_zero, ClassicalFieldTheory.Local.iteratedTotalDerivative_single
statement: formalized
proof: formalized
---

# Total derivatives on local jet-dependent functions

The module `PhyslibAlpha.ClassicalFieldTheory.Local.TotalDerivative`, [PhyslibAlpha/ClassicalFieldTheory/Local/TotalDerivative.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDerivative.lean): 8 declarations, 3 with a docstring.

> Total derivatives of jet-dependent functions, defined via evaluation along fields.

## i. Overview

> This module defines total derivatives of local jet-dependent functions by differentiating their
> evaluation along jets of fields.
>
> For the first local stage, this keeps the operator close to the use made in the Euler-Lagrange
> formula, without yet introducing a separate coordinate-level derivative calculus on `JetPoint`.

## ii. Key results

> - `ClassicalFieldTheory.Local.evalOnJet` : evaluate a jet-dependent function along a field.
> - `ClassicalFieldTheory.Local.totalDerivative` : total derivative in one coordinate direction.
> - `ClassicalFieldTheory.Local.iteratedTotalDerivative` : iterated total derivative indexed by a
>   multi-index.

## iv. References

> * None.

## A. Evaluation on jets

**`ClassicalFieldTheory.Local.evalOnJet`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDerivative.lean#L52).

> Evaluate a local jet-dependent function along the `k`-jet of a field.

```lean
noncomputable def evalOnJet (k : ℕ) (F : JetPoint d m k → ℝ)
    (f : Space d → EuclideanSpace ℝ (Fin m)) :
    Space d → ℝ
```

## B. Total derivatives

**`ClassicalFieldTheory.Local.totalDerivative`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDerivative.lean#L63).

> The total derivative of a jet-dependent function in the coordinate direction `i`.

```lean
noncomputable def totalDerivative (k : ℕ) (i : Fin d) (F : JetPoint d m k → ℝ)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Space d → ℝ
```

**`ClassicalFieldTheory.Local.iteratedTotalDerivative`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDerivative.lean#L68).

> The iterated total derivative indexed by a multi-index.

```lean
noncomputable def iteratedTotalDerivative (k : ℕ) (I : MultiIndex d) (F : JetPoint d m k → ℝ)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Space d → ℝ
```

**`ClassicalFieldTheory.Local.evalOnJet_apply`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDerivative.lean#L73).

```lean
lemma evalOnJet_apply (k : ℕ) (F : JetPoint d m k → ℝ)
    (f : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d) :
    evalOnJet k F f x = F (jetAt k f x)
```

**`ClassicalFieldTheory.Local.totalDerivative_eq`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDerivative.lean#L78).

```lean
lemma totalDerivative_eq (k : ℕ) (i : Fin d) (F : JetPoint d m k → ℝ)
    (f : Space d → EuclideanSpace ℝ (Fin m)) :
    totalDerivative k i F f = ∂[i] (fun x => F (jetAt k f x))
```

**`ClassicalFieldTheory.Local.iteratedTotalDerivative_eq`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDerivative.lean#L83).

```lean
lemma iteratedTotalDerivative_eq (k : ℕ) (I : MultiIndex d) (F : JetPoint d m k → ℝ)
    (f : Space d → EuclideanSpace ℝ (Fin m)) :
    iteratedTotalDerivative k I F f = ∂^[I] (fun x => F (jetAt k f x))
```

**`ClassicalFieldTheory.Local.iteratedTotalDerivative_zero`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDerivative.lean#L87).

```lean
lemma iteratedTotalDerivative_zero (k : ℕ) (F : JetPoint d m k → ℝ)
    (f : Space d → EuclideanSpace ℝ (Fin m)) :
    iteratedTotalDerivative k (0 : MultiIndex d) F f = evalOnJet k F f
```

**`ClassicalFieldTheory.Local.iteratedTotalDerivative_single`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDerivative.lean#L92).

```lean
lemma iteratedTotalDerivative_single (k : ℕ) (i : Fin d) (F : JetPoint d m k → ℝ)
    (f : Space d → EuclideanSpace ℝ (Fin m)) :
    iteratedTotalDerivative k (Physlib.MultiIndex.increment 0 i) F f =
      totalDerivative k i F f
```

## Depends on

- [Coordinate-level jet points](jetpoint.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/TotalDerivative.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/TotalDerivative.lean)

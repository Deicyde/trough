---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.AdmissibleVariation, ClassicalFieldTheory.Local.AdmissibleVariation.hasCompactSupport, ClassicalFieldTheory.Local.AdmissibleVariation.toCompactlySupportedContinuousMap, ClassicalFieldTheory.Local.AdmissibleVariation.zero_apply, ClassicalFieldTheory.Local.AdmissibleVariation.neg_apply, ClassicalFieldTheory.Local.AdmissibleVariation.add_apply, ClassicalFieldTheory.Local.AdmissibleVariation.sub_apply, ClassicalFieldTheory.Local.AdmissibleVariation.smul_apply
statement: formalized
proof: formalized
---

# Admissible local variations

The module `Physlib.ClassicalFieldTheory.Local.Variation`, [Physlib/ClassicalFieldTheory/Local/Variation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean): 15 declarations (6 instances with no name), 3 with a docstring.

## i. Overview

> This module packages the admissible variations used in the local first-variation problem.
>
> For the first local stage, a variation is admissible if it is a smooth compactly supported map
> `Space d → U` for a real normed vector space `U`. This reuses the existing `IsTestFunction`
> predicate rather than introducing a second support calculus.

## ii. Key results

> - `ClassicalFieldTheory.Local.AdmissibleVariation` : compactly supported smooth variations.

## iv. References

> * None.

## A. Admissible variations

**`ClassicalFieldTheory.Local.AdmissibleVariation`**, a structure, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L48).

> An admissible local variation is a smooth compactly supported map `Space d → U`.

```lean
structure AdmissibleVariation (d : ℕ) (U : Type*) [NormedAddCommGroup U] [NormedSpace ℝ U] where
  /-- The underlying variation function. -/
  toFun : Space d → U
  /-- Smoothness and compact support of the variation. -/
  isTestFunction : IsTestFunction toFun
```

## B. Basic operations on admissible variations

**An instance with no name**, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L63).

```lean
instance : CoeFun (AdmissibleVariation d U) (fun _ => Space d → U)
```

**`ClassicalFieldTheory.Local.AdmissibleVariation.hasCompactSupport`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L69).

> An admissible variation has compact support.

```lean
lemma hasCompactSupport (η : AdmissibleVariation d U) : HasCompactSupport (η.toFun)
```

**`ClassicalFieldTheory.Local.AdmissibleVariation.toCompactlySupportedContinuousMap`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L73).

> View an admissible variation as a compactly supported continuous map.

```lean
noncomputable def toCompactlySupportedContinuousMap (η : AdmissibleVariation d U) :
    CompactlySupportedContinuousMap (Space d) U
```

**An instance with no name**, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L77).

```lean
noncomputable instance : Zero (AdmissibleVariation d U)
```

**`ClassicalFieldTheory.Local.AdmissibleVariation.zero_apply`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L83).

```lean
lemma zero_apply (x : Space d) : (0 : AdmissibleVariation d U) x = 0
```

**An instance with no name**, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L85).

```lean
noncomputable instance : Neg (AdmissibleVariation d U)
```

**`ClassicalFieldTheory.Local.AdmissibleVariation.neg_apply`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L91).

```lean
lemma neg_apply (η : AdmissibleVariation d U) (x : Space d) : (-η) x = -η x
```

**An instance with no name**, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L93).

```lean
noncomputable instance : Add (AdmissibleVariation d U)
```

**`ClassicalFieldTheory.Local.AdmissibleVariation.add_apply`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L99).

```lean
lemma add_apply (η ξ : AdmissibleVariation d U) (x : Space d) : (η + ξ) x = η x + ξ x
```

**An instance with no name**, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L101).

```lean
noncomputable instance : Sub (AdmissibleVariation d U)
```

**`ClassicalFieldTheory.Local.AdmissibleVariation.sub_apply`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L107).

```lean
lemma sub_apply (η ξ : AdmissibleVariation d U) (x : Space d) : (η - ξ) x = η x - ξ x
```

**An instance with no name**, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L109).

```lean
noncomputable instance : SMul ℝ (AdmissibleVariation d U)
```

**`ClassicalFieldTheory.Local.AdmissibleVariation.smul_apply`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L116).

```lean
lemma smul_apply (c : ℝ) (η : AdmissibleVariation d U) (x : Space d) :
    (c • η) x = c • η x
```

**`ClassicalFieldTheory.Local.AdmissibleVariation.coord`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean#L120).

```lean
lemma coord {m : ℕ} (η : AdmissibleVariation d (Space m)) (a : Fin m) :
    IsTestFunction (fun x => (η.toFun x).coord a)
```

## Depends on

- [Test functions](../../mathematics/variationalcalculus/istestfunction.md)

## Sources

- [Physlib/ClassicalFieldTheory/Local/Variation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalFieldTheory/Local/Variation.lean)

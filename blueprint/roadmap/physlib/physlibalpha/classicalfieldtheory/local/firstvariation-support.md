---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.variedField_zero, ClassicalFieldTheory.Local.variedField_variedField, ClassicalFieldTheory.Local.contDiff_space_deriv, ClassicalFieldTheory.Local.isTestFunction_space_deriv, ClassicalFieldTheory.Local.iteratedDerivList_contDiff, ClassicalFieldTheory.Local.iteratedDerivList_isTestFunction, ClassicalFieldTheory.Local.iteratedDerivList_commute_deriv, ClassicalFieldTheory.Local.iteratedDeriv_coord_isTestFunction
statement: formalized
proof: formalized
---

# First variation support lemmas

The module `PhyslibAlpha.ClassicalFieldTheory.Local.FirstVariation.Support`, [PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Support.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Support.lean): 10 declarations, 0 with a docstring.

> Support lemmas for the first variation: varied fields, test functions, varied jet coordinates.

## i. Overview

> This module collects the reusable support lemmas used by the analytic part of the local
> first-variation proof: basic identities for varied fields, iterated derivative regularity for
> test functions, and continuity of the varied local-jet coordinate map.

## ii. Key results

> - `ClassicalFieldTheory.Local.variedField_zero`
> - `ClassicalFieldTheory.Local.variedField_variedField`

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics, Chapter 5,
>   Theorem 5.2. [ref: cortes\_haupt\_2016]

## A. Varied fields

**`ClassicalFieldTheory.Local.variedField_zero`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Support.lean#L53).

```lean
lemma variedField_zero (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) :
    variedField f η 0 = f
```

**`ClassicalFieldTheory.Local.variedField_variedField`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Support.lean#L60).

```lean
lemma variedField_variedField (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m)))
    (s t : ℝ) :
    variedField (variedField f η s) η t = variedField f η (s + t)
```

## B. Iterated derivative support lemmas

**`ClassicalFieldTheory.Local.contDiff_space_deriv`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Support.lean#L72).

```lean
lemma contDiff_space_deriv {g : Space d → ℝ} (hg : ContDiff ℝ ∞ g)
    (i : Fin d) : ContDiff ℝ ∞ (∂[i] g)
```

**`ClassicalFieldTheory.Local.isTestFunction_space_deriv`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Support.lean#L78).

```lean
lemma isTestFunction_space_deriv {g : Space d → ℝ} (hg : IsTestFunction g) (i : Fin d) :
    IsTestFunction (∂[i] g)
```

**`ClassicalFieldTheory.Local.iteratedDerivList_contDiff`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Support.lean#L82).

```lean
lemma iteratedDerivList_contDiff (L : List (Fin d)) {g : Space d → ℝ}
    (hg : ContDiff ℝ ∞ g) :
    ContDiff ℝ ∞ (L.foldr (fun i h => ∂[i] h) g)
```

**`ClassicalFieldTheory.Local.iteratedDerivList_isTestFunction`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Support.lean#L92).

```lean
lemma iteratedDerivList_isTestFunction (L : List (Fin d)) {g : Space d → ℝ}
    (hg : IsTestFunction g) :
    IsTestFunction (L.foldr (fun i h => ∂[i] h) g)
```

**`ClassicalFieldTheory.Local.iteratedDerivList_commute_deriv`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Support.lean#L102).

```lean
lemma iteratedDerivList_commute_deriv (L : List (Fin d)) (i : Fin d)
    {g : Space d → ℝ} (hg : ContDiff ℝ ∞ g) :
    L.foldr (fun j h => ∂[j] h) (∂[i] g) = ∂[i] (L.foldr (fun j h => ∂[j] h) g)
```

**`ClassicalFieldTheory.Local.iteratedDeriv_coord_isTestFunction`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Support.lean#L117).

```lean
lemma iteratedDeriv_coord_isTestFunction (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m)))
    (I : DerivativeIndex d k) (a : Fin m) :
    IsTestFunction (fun x => ∂^[I.1] (fun y => (η y) a) x)
```

**`ClassicalFieldTheory.Local.firstVariationDensityTerm_integrable_of_continuous_coordDeriv`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Support.lean#L123).

```lean
lemma firstVariationDensityTerm_integrable_of_continuous_coordDeriv
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m)))
    (I : DerivativeIndex d k) (a : Fin m)
    (hcont : Continuous (fun x : Space d =>
      L.coordDeriv I a (jetAt k f x))) :
    Integrable (firstVariationDensityTerm L f η I a)
```

## C. Varied local-jet coordinates

**`ClassicalFieldTheory.Local.continuous_jetBaseCoordinates_variedField`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Support.lean#L145).

```lean
lemma continuous_jetBaseCoordinates_variedField
    (k : ℕ) (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m)))
    (hf : ContDiff ℝ ∞ f) :
    Continuous
      (fun p : ℝ × Space d => (p.2, jetCoordinatesAt k (variedField f η p.1) p.2))
```

## Depends on

- [Local action functionals](action.md)
- [First variation core objects](firstvariation-basic.md)

## Proof depends on

- [Alpha extensions for admissible local variations](variation.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Support.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Support.lean)

---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.firstVariationDensityTerm, ClassicalFieldTheory.Local.firstVariationDensity, ClassicalFieldTheory.Local.firstVariationValue, ClassicalFieldTheory.Local.firstVariationDensityTerm_apply, ClassicalFieldTheory.Local.firstVariationDensity_apply, ClassicalFieldTheory.Local.firstVariationValue_eq_integral, ClassicalFieldTheory.Local.firstVariationValue_eq_zero_of_eulerLagrange_zero
statement: formalized
proof: formalized
---

# First variation core objects

The module `PhyslibAlpha.ClassicalFieldTheory.Local.FirstVariation.Basic`, [PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Basic.lean): 7 declarations, 3 with a docstring.

> The linearized first-variation density and its Euler-Lagrange pairing.

## i. Overview

> This module contains the basic objects used throughout the local first-variation theory:
> the linearized density before integration by parts and its Euler-Lagrange pairing.

## ii. Key results

> - `ClassicalFieldTheory.Local.firstVariationDensityTerm`
> - `ClassicalFieldTheory.Local.firstVariationDensity`
> - `ClassicalFieldTheory.Local.firstVariationValue`

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics, Chapter 5,
>   Theorem 5.2. [ref: cortes\_haupt\_2016]

## A. First-variation values

**`ClassicalFieldTheory.Local.firstVariationDensityTerm`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Basic.lean#L52).

> A single term in the linearized first-variation density before integration by parts.

```lean
noncomputable def firstVariationDensityTerm (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) (I : DerivativeIndex d k)
    (a : Fin m) :
    Space d → ℝ
```

**`ClassicalFieldTheory.Local.firstVariationDensity`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Basic.lean#L60).

> The pointwise linearized first-variation density before integration by parts.

```lean
noncomputable def firstVariationDensity (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) : Space d → ℝ
```

**`ClassicalFieldTheory.Local.firstVariationValue`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Basic.lean#L66).

> The value predicted by the first-variation formula for an admissible variation.

```lean
noncomputable def firstVariationValue (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) : ℝ
```

**`ClassicalFieldTheory.Local.firstVariationDensityTerm_apply`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Basic.lean#L72).

```lean
lemma firstVariationDensityTerm_apply (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) (I : DerivativeIndex d k)
    (a : Fin m) (x : Space d) :
    firstVariationDensityTerm L f η I a x =
      L.coordDeriv I a (jetAt k f x) * ∂^[I.1] (fun y => (η y) a) x
```

**`ClassicalFieldTheory.Local.firstVariationDensity_apply`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Basic.lean#L80).

```lean
lemma firstVariationDensity_apply (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) (x : Space d) :
    firstVariationDensity L f η x =
      ∑ I : DerivativeIndex d k, ∑ a : Fin m, firstVariationDensityTerm L f η I a x
```

**`ClassicalFieldTheory.Local.firstVariationValue_eq_integral`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Basic.lean#L87).

```lean
lemma firstVariationValue_eq_integral (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) :
    firstVariationValue L f η = ∫ x, ⟪eulerLagrangeOp L f x, η x⟫_ℝ
```

**`ClassicalFieldTheory.Local.firstVariationValue_eq_zero_of_eulerLagrange_zero`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Basic.lean#L92).

```lean
lemma firstVariationValue_eq_zero_of_eulerLagrange_zero
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) (hEuler : eulerLagrangeOp L f = 0) :
    firstVariationValue L f η = 0
```

## Depends on

- [Admissible local variations](../../../physlib/classicalfieldtheory/local/variation.md)
- [Local Euler-Lagrange operators](eulerlagrange.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstVariation/Basic.lean)

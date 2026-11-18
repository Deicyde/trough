---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.actionDensity, ClassicalFieldTheory.Local.HasFiniteAction, ClassicalFieldTheory.Local.IsAdmissibleForAction, ClassicalFieldTheory.Local.action, ClassicalFieldTheory.Local.actionDensity_apply, ClassicalFieldTheory.Local.action_eq_integral, ClassicalFieldTheory.Local.variedField, ClassicalFieldTheory.Local.variedField_contDiff
statement: formalized
proof: formalized
---

# Local action functionals

The module `PhyslibAlpha.ClassicalFieldTheory.Local.Action`, [PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean): 18 declarations, 11 with a docstring.

> The local action of a field, its value under admissible variations, and critical fields.

## i. Overview

> This module defines the local action functional associated with a local Lagrangian, together with
> the first notions needed to talk about variational criticality.
>
> For the first implementation pass, the action is defined directly as the integral of a local
> Lagrangian evaluated along jets of a field. The integrability conditions needed for this action and
> for its variations are kept explicit in the API.

## ii. Key results

> - `ClassicalFieldTheory.Local.actionDensity` : the density associated with a field.
> - `ClassicalFieldTheory.Local.action` : the action of a field.
> - `ClassicalFieldTheory.Local.HasFiniteAction` : finiteness of the action integral.
> - `ClassicalFieldTheory.Local.IsAdmissibleForAction` : symmetric admissibility of a lagrangian and
>   field pair for the action functional.
> - `ClassicalFieldTheory.Local.actionVariation` : the action under an admissible variation.
> - `ClassicalFieldTheory.Local.IsCritical` : vanishing first derivative of the varied action.

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics, Chapter 5.
>   [ref: cortes\_haupt\_2016]

## A. Action densities and action

**`ClassicalFieldTheory.Local.actionDensity`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L62).

> The action density determined by a local Lagrangian and a field.

```lean
noncomputable def actionDensity (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Space d → ℝ
```

**`ClassicalFieldTheory.Local.HasFiniteAction`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L67).

> The integrability condition for the action density of a field.

```lean
def HasFiniteAction (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m)) : Prop
```

**`ClassicalFieldTheory.Local.IsAdmissibleForAction`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L72).

> Symmetric admissibility predicate for the action functional: the pair `(L, f)` is admissible
> when the field is smooth and the corresponding action density is integrable.

```lean
def IsAdmissibleForAction (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Prop
```

**`ClassicalFieldTheory.Local.action`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L77).

> The action associated with a local Lagrangian.

```lean
noncomputable def action (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : ℝ
```

**`ClassicalFieldTheory.Local.actionDensity_apply`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L82).

```lean
lemma actionDensity_apply (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d) :
    actionDensity L f x = L (jetAt k f x)
```

**`ClassicalFieldTheory.Local.action_eq_integral`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L87).

```lean
lemma action_eq_integral (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m)) :
    action L f = ∫ x, actionDensity L f x
```

## B. Action under variation

**`ClassicalFieldTheory.Local.variedField`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L96).

> The field obtained by varying `f` in the direction `η` with parameter `s`.

```lean
noncomputable def variedField (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m)))
    (s : ℝ) :
    Space d → EuclideanSpace ℝ (Fin m)
```

**`ClassicalFieldTheory.Local.variedField_contDiff`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L103).

> Smoothness of the varied field for smooth `f` and admissible `η`.

```lean
lemma variedField_contDiff (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m)))
    (s : ℝ)
    (hf : ContDiff ℝ ∞ f) :
    ContDiff ℝ ∞ (variedField f η s)
```

**`ClassicalFieldTheory.Local.actionVariation`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L111).

> The action of a field under an admissible variation.

```lean
noncomputable def actionVariation (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) : ℝ → ℝ
```

**`ClassicalFieldTheory.Local.HasFiniteActionVariation`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L117).

> Explicit integrability condition for the family of varied action densities.

```lean
def HasFiniteActionVariation (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) : Prop
```

**`ClassicalFieldTheory.Local.HasCompactlySupportedActionVariationDifference`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L125).

> Locality package for the action density under compactly supported variations: for every
> variation parameter `s`, the change in the action density is a continuous compactly supported
> function. Combined with finiteness of the base action, this implies finiteness of the varied
> action.

```lean
def HasCompactlySupportedActionVariationDifference (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) : Prop
```

**`ClassicalFieldTheory.Local.hasFiniteActionVariation_of_hasFiniteAction_of_compactlySupportedDifference`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L134).

> If the base action is finite and every varied action density differs from the base density by
> a continuous compactly supported function, then the whole varied family has finite action.

```lean
lemma hasFiniteActionVariation_of_hasFiniteAction_of_compactlySupportedDifference
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m)))
    (hbase : HasFiniteAction L f)
    (hdiff : HasCompactlySupportedActionVariationDifference L f η) :
    HasFiniteActionVariation L f η
```

**`ClassicalFieldTheory.Local.variedField_apply`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L155).

```lean
lemma variedField_apply (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) (s : ℝ)
    (x : Space d) :
    variedField f η s x = f x + s • η x
```

**`ClassicalFieldTheory.Local.actionVariation_apply`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L161).

```lean
lemma actionVariation_apply (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) (s : ℝ) :
    actionVariation L f η s = action L (variedField f η s)
```

**`ClassicalFieldTheory.Local.jetAt_variedField_eq_of_notMem_tsupport`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L165).

```lean
lemma jetAt_variedField_eq_of_notMem_tsupport
    (k : ℕ) (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) (s : ℝ)
    {x : Space d}
    (hf : ContDiff ℝ ∞ f) (hx : x ∉ tsupport η.toFun) :
    jetAt k (variedField f η s) x = jetAt k f x
```

**`ClassicalFieldTheory.Local.actionDensity_variedField_eq_of_notMem_tsupport`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L179).

```lean
lemma actionDensity_variedField_eq_of_notMem_tsupport
    (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m)))
    (s : ℝ)
    {x : Space d} (hf : ContDiff ℝ ∞ f) (hx : x ∉ tsupport η.toFun) :
    actionDensity L (variedField f η s) x = actionDensity L f x
```

**`ClassicalFieldTheory.Local.hasCompactlySupportedActionVariationDifference_of_continuousInCoordinates`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L187).

```lean
lemma hasCompactlySupportedActionVariationDifference_of_continuousInCoordinates
    (L : Lagrangian d m k) (hcontL : Lagrangian.ContinuousInCoordinates L)
    (f : Space d → EuclideanSpace ℝ (Fin m)) (hf : ContDiff ℝ ∞ f)
    (η : AdmissibleVariation d (EuclideanSpace ℝ (Fin m))) :
    HasCompactlySupportedActionVariationDifference L f η
```

## C. Critical fields

**`ClassicalFieldTheory.Local.IsCritical`**, a def, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean#L219).

> A field is critical for a local action if every admissible compactly supported variation has
> vanishing first derivative at `s = 0`, under the explicit finite-action hypothesis for the varied
> family.

```lean
def IsCritical (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m)) : Prop
```

## Depends on

- [Admissible local variations](../../../physlib/classicalfieldtheory/local/variation.md)
- [Local Lagrangians](lagrangian.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Action.lean)

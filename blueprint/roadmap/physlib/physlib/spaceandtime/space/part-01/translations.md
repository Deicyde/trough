---
declaration: module
origin: cited
lean: Space.translateSchwartz, Space.translateSchwartz_apply, Space.translateSchwartz_coe_eq, Space.translateSchwartz_single_apply, Space.distTranslate, Space.distTranslate_apply, Space.distTranslate_distGrad, Space.distTranslate_ofFunction
statement: formalized
proof: formalized
---

# Translations on space

The module `Physlib.SpaceAndTime.Space.Translations`, [Physlib/SpaceAndTime/Space/Translations.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Translations.lean): 9 declarations, 3 with a docstring.

> We define translations on space, and how translations act on distributions.
> Translations for part of the Poincaré group.

## Translations of distributions

**`Space.translateSchwartz`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Translations.lean#L42).

> The continuous linear map translating Schwartz maps.

```lean
noncomputable def translateSchwartz {d : ℕ} (a : EuclideanSpace ℝ (Fin d)) :
    𝓢(Space d, X) →L[ℝ] 𝓢(Space d, X)
```

**`Space.translateSchwartz_apply`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Translations.lean#L83).

```lean
lemma translateSchwartz_apply {d : ℕ} (a : EuclideanSpace ℝ (Fin d))
    (η : 𝓢(Space d, X)) (x : Space d) :
    translateSchwartz a η x = η (x - basis.repr.symm a)
```

**`Space.translateSchwartz_coe_eq`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Translations.lean#L87).

```lean
lemma translateSchwartz_coe_eq {d : ℕ} (a : EuclideanSpace ℝ (Fin d))
    (η : 𝓢(Space d, X)) :
    (translateSchwartz a η : Space d → X) = fun x => η (x - basis.repr.symm a)
```

**`Space.translateSchwartz_single_apply`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Translations.lean#L94).

> In one dimension, translating by `a` subtracts the point `a` from the argument.

```lean
lemma translateSchwartz_single_apply (a : ℝ) (η : 𝓢(Space 1, X)) (x : Space 1) :
    translateSchwartz (EuclideanSpace.single 0 a) η x = η (x - oneEquiv.symm a)
```

**`Space.distTranslate`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Translations.lean#L103).

> The continuous linear map translating distributions.

```lean
noncomputable def distTranslate {d : ℕ} (a : EuclideanSpace ℝ (Fin d)) :
    ((Space d) →d[ℝ] X) →ₗ[ℝ] ((Space d) →d[ℝ] X)
```

**`Space.distTranslate_apply`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Translations.lean#L112).

```lean
lemma distTranslate_apply {d : ℕ} (a : EuclideanSpace ℝ (Fin d))
    (T : (Space d) →d[ℝ] X) (η : 𝓢(Space d, ℝ)) :
    distTranslate a T η = T (translateSchwartz (-a) η)
```

**`Space.distTranslate_distGrad`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Translations.lean#L119).

```lean
lemma distTranslate_distGrad {d : ℕ} (a : EuclideanSpace ℝ (Fin d))
    (T : (Space d) →d[ℝ] ℝ) :
    distGrad (distTranslate a T) = distTranslate a (distGrad T)
```

**`Space.distTranslate_ofFunction`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Translations.lean#L137).

```lean
lemma distTranslate_ofFunction {d : ℕ} (a : EuclideanSpace ℝ (Fin d))
    (f : Space d → X) (hf : IsDistBounded f) :
    distTranslate a (distOfFunction f hf) =
    distOfFunction (fun x => f (x - basis.repr.symm a))
    (IsDistBounded.comp_add_right hf (- basis.repr.symm a))
```

**`Space.distDiv_distTranslate`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Translations.lean#L155).

```lean
lemma distDiv_distTranslate {d : ℕ} (a : EuclideanSpace ℝ (Fin d))
    (T : (Space d) →d[ℝ] EuclideanSpace ℝ (Fin d)) :
    distDiv (distTranslate a T) = distTranslate a (distDiv T)
```

## Depends on

- [Divergence on Space](derivatives-div.md)

## Sources

- [Physlib/SpaceAndTime/Space/Translations.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/Space/Translations.lean)

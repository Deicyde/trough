---
declaration: module
origin: cited
lean: Space.translateSchwartz, Space.translateSchwartz_apply, Space.translateSchwartz_coe_eq, Space.distTranslate, Space.distTranslate_apply, Space.distTranslate_distGrad, Space.distTranslate_ofFunction, Space.distDiv_distTranslate
statement: formalized
proof: formalized
---

# Translations on space

The module `Physlib.SpaceAndTime.Space.Translations`, [Physlib/SpaceAndTime/Space/Translations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Translations.lean): 8 declarations, 2 with a docstring.

> We define translations on space, and how translations act on distributions.
> Translations for part of the Poincaré group.

## Translations of distributions

**`Space.translateSchwartz`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Translations.lean#L42).

> The continuous linear map translating Schwartz maps.

```lean
noncomputable def translateSchwartz {d : ℕ} (a : EuclideanSpace ℝ (Fin d)) :
    𝓢(Space d, X) →L[ℝ] 𝓢(Space d, X)
```

**`Space.translateSchwartz_apply`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Translations.lean#L83).

```lean
lemma translateSchwartz_apply {d : ℕ} (a : EuclideanSpace ℝ (Fin d))
    (η : 𝓢(Space d, X)) (x : Space d) :
    translateSchwartz a η x = η (x - basis.repr.symm a)
```

**`Space.translateSchwartz_coe_eq`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Translations.lean#L87).

```lean
lemma translateSchwartz_coe_eq {d : ℕ} (a : EuclideanSpace ℝ (Fin d))
    (η : 𝓢(Space d, X)) :
    (translateSchwartz a η : Space d → X) = fun x => η (x - basis.repr.symm a)
```

**`Space.distTranslate`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Translations.lean#L94).

> The continuous linear map translating distributions.

```lean
noncomputable def distTranslate {d : ℕ} (a : EuclideanSpace ℝ (Fin d)) :
    ((Space d) →d[ℝ] X) →ₗ[ℝ] ((Space d) →d[ℝ] X)
```

**`Space.distTranslate_apply`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Translations.lean#L103).

```lean
lemma distTranslate_apply {d : ℕ} (a : EuclideanSpace ℝ (Fin d))
    (T : (Space d) →d[ℝ] X) (η : 𝓢(Space d, ℝ)) :
    distTranslate a T η = T (translateSchwartz (-a) η)
```

**`Space.distTranslate_distGrad`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Translations.lean#L110).

```lean
lemma distTranslate_distGrad {d : ℕ} (a : EuclideanSpace ℝ (Fin d))
    (T : (Space d) →d[ℝ] ℝ) :
    distGrad (distTranslate a T) = distTranslate a (distGrad T)
```

**`Space.distTranslate_ofFunction`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Translations.lean#L128).

```lean
lemma distTranslate_ofFunction {d : ℕ} (a : EuclideanSpace ℝ (Fin d))
    (f : Space d → X) (hf : IsDistBounded f) :
    distTranslate a (distOfFunction f hf) =
    distOfFunction (fun x => f (x - basis.repr.symm a))
    (IsDistBounded.comp_add_right hf (- basis.repr.symm a))
```

**`Space.distDiv_distTranslate`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Translations.lean#L146).

```lean
lemma distDiv_distTranslate {d : ℕ} (a : EuclideanSpace ℝ (Fin d))
    (T : (Space d) →d[ℝ] EuclideanSpace ℝ (Fin d)) :
    distDiv (distTranslate a T) = distTranslate a (distDiv T)
```

## Depends on

- [Divergence on Space](derivatives-div.md)

## Sources

- [Physlib/SpaceAndTime/Space/Translations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Translations.lean)

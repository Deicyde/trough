---
declaration: module
origin: cited
lean: FieldSpecification.FieldOpFreeAlgebra.timeOrderF, FieldSpecification.FieldOpFreeAlgebra.timeOrderF_ofCrAnListF, FieldSpecification.FieldOpFreeAlgebra.timeOrderF_timeOrderF_mid, FieldSpecification.FieldOpFreeAlgebra.timeOrderF_timeOrderF_right, FieldSpecification.FieldOpFreeAlgebra.timeOrderF_timeOrderF_left, FieldSpecification.FieldOpFreeAlgebra.timeOrderF_ofFieldOpListF, FieldSpecification.FieldOpFreeAlgebra.timeOrderF_ofFieldOpListF_nil, FieldSpecification.FieldOpFreeAlgebra.timeOrderF_ofFieldOpListF_singleton
statement: formalized
proof: formalized
---

# Time Ordering in the FieldOpFreeAlgebra

The module `Physlib.QFT.PerturbationTheory.FieldOpFreeAlgebra.TimeOrder`, [Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean): 22 declarations, 3 with a docstring.

## Time order

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L45).

> For a field specification `𝓕`, `timeOrderF` is the linear map
>
> `FieldOpFreeAlgebra 𝓕 →ₗ[ℂ] FieldOpFreeAlgebra 𝓕`
>
> defined by its action on the basis `ofCrAnListF φs`, taking
> `ofCrAnListF φs` to
>
> `crAnTimeOrderSign φs • ofCrAnListF (crAnTimeOrderList φs)`.
>
> That is, `timeOrderF` time-orders the field operators and multiplies by the sign of the
> time order.
>
> The notation `𝓣ᶠ(a)` is used for `timeOrderF a`

```lean
def timeOrderF : FieldOpFreeAlgebra 𝓕 →ₗ[ℂ] FieldOpFreeAlgebra 𝓕
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_ofCrAnListF`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L52).

```lean
lemma timeOrderF_ofCrAnListF (φs : List 𝓕.CrAnFieldOp) :
    𝓣ᶠ(ofCrAnListF φs) = crAnTimeOrderSign φs • ofCrAnListF (crAnTimeOrderList φs)
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_timeOrderF_mid`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L57).

```lean
lemma timeOrderF_timeOrderF_mid (a b c : 𝓕.FieldOpFreeAlgebra) :
    𝓣ᶠ(a * b * c) = 𝓣ᶠ(a * 𝓣ᶠ(b) * c)
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_timeOrderF_right`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L107).

```lean
lemma timeOrderF_timeOrderF_right (a b : 𝓕.FieldOpFreeAlgebra) : 𝓣ᶠ(a * b) = 𝓣ᶠ(a * 𝓣ᶠ(b))
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_timeOrderF_left`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L113).

```lean
lemma timeOrderF_timeOrderF_left (a b : 𝓕.FieldOpFreeAlgebra) : 𝓣ᶠ(a * b) = 𝓣ᶠ(𝓣ᶠ(a) * b)
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_ofFieldOpListF`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L119).

```lean
lemma timeOrderF_ofFieldOpListF (φs : List 𝓕.FieldOp) :
    𝓣ᶠ(ofFieldOpListF φs) = timeOrderSign φs • ofFieldOpListF (timeOrderList φs)
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_ofFieldOpListF_nil`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L131).

```lean
lemma timeOrderF_ofFieldOpListF_nil : timeOrderF (𝓕 := 𝓕) (ofFieldOpListF []) = 1
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_ofFieldOpListF_singleton`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L136).

```lean
lemma timeOrderF_ofFieldOpListF_singleton (φ : 𝓕.FieldOp) :
    𝓣ᶠ(ofFieldOpListF [φ]) = ofFieldOpListF [φ]
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_ofFieldOpF_ofFieldOpF_ordered`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L140).

```lean
lemma timeOrderF_ofFieldOpF_ofFieldOpF_ordered {φ ψ : 𝓕.FieldOp} (h : timeOrderRel φ ψ) :
    𝓣ᶠ(ofFieldOpF φ * ofFieldOpF ψ) = ofFieldOpF φ * ofFieldOpF ψ
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_ofFieldOpF_ofFieldOpF_not_ordered`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L148).

```lean
lemma timeOrderF_ofFieldOpF_ofFieldOpF_not_ordered {φ ψ : 𝓕.FieldOp} (h : ¬ timeOrderRel φ ψ) :
    𝓣ᶠ(ofFieldOpF φ * ofFieldOpF ψ) = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ψ) • ofFieldOpF ψ * ofFieldOpF φ
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_ofFieldOpF_ofFieldOpF_not_ordered_eq_timeOrderF`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L156).

```lean
lemma timeOrderF_ofFieldOpF_ofFieldOpF_not_ordered_eq_timeOrderF {φ ψ : 𝓕.FieldOp}
    (h : ¬ timeOrderRel φ ψ) :
    𝓣ᶠ(ofFieldOpF φ * ofFieldOpF ψ) = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ψ) • 𝓣ᶠ(ofFieldOpF ψ * ofFieldOpF φ)
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_superCommuteF_ofCrAnOpF_ofCrAnOpF_not_crAnTimeOrderRel`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L165).

```lean
lemma timeOrderF_superCommuteF_ofCrAnOpF_ofCrAnOpF_not_crAnTimeOrderRel
    {φ ψ : 𝓕.CrAnFieldOp} (h : ¬ crAnTimeOrderRel φ ψ) :
    𝓣ᶠ([ofCrAnOpF φ, ofCrAnOpF ψ]ₛF) = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_superCommuteF_ofCrAnOpF_ofCrAnOpF_not_crAnTimeOrderRel_right`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L183).

```lean
lemma timeOrderF_superCommuteF_ofCrAnOpF_ofCrAnOpF_not_crAnTimeOrderRel_right
    {φ ψ : 𝓕.CrAnFieldOp} (h : ¬ crAnTimeOrderRel φ ψ) (a : 𝓕.FieldOpFreeAlgebra) :
    𝓣ᶠ(a * [ofCrAnOpF φ, ofCrAnOpF ψ]ₛF) = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_superCommuteF_ofCrAnOpF_ofCrAnOpF_not_crAnTimeOrderRel_left`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L190).

```lean
lemma timeOrderF_superCommuteF_ofCrAnOpF_ofCrAnOpF_not_crAnTimeOrderRel_left
    {φ ψ : 𝓕.CrAnFieldOp} (h : ¬ crAnTimeOrderRel φ ψ) (a : 𝓕.FieldOpFreeAlgebra) :
    𝓣ᶠ([ofCrAnOpF φ, ofCrAnOpF ψ]ₛF * a) = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_superCommuteF_ofCrAnOpF_ofCrAnOpF_not_crAnTimeOrderRel_mid`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L197).

```lean
lemma timeOrderF_superCommuteF_ofCrAnOpF_ofCrAnOpF_not_crAnTimeOrderRel_mid
    {φ ψ : 𝓕.CrAnFieldOp} (h : ¬ crAnTimeOrderRel φ ψ) (a b : 𝓕.FieldOpFreeAlgebra) :
    𝓣ᶠ(a * [ofCrAnOpF φ, ofCrAnOpF ψ]ₛF * b) = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_superCommuteF_superCommuteF_ofCrAnOpF_not_crAnTimeOrderRel`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L204).

```lean
lemma timeOrderF_superCommuteF_superCommuteF_ofCrAnOpF_not_crAnTimeOrderRel
    {φ1 φ2 : 𝓕.CrAnFieldOp} (h : ¬ crAnTimeOrderRel φ1 φ2) (a : 𝓕.FieldOpFreeAlgebra) :
    𝓣ᶠ([a, [ofCrAnOpF φ1, ofCrAnOpF φ2]ₛF]ₛF) = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_superCommuteF_ofCrAnOpF_superCommuteF_not_crAnTimeOrderRel`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L227).

```lean
lemma timeOrderF_superCommuteF_ofCrAnOpF_superCommuteF_not_crAnTimeOrderRel
    {φ1 φ2 φ3 : 𝓕.CrAnFieldOp} (h12 : ¬ crAnTimeOrderRel φ1 φ2)
    (h13 : ¬ crAnTimeOrderRel φ1 φ3) :
    𝓣ᶠ([ofCrAnOpF φ1, [ofCrAnOpF φ2, ofCrAnOpF φ3]ₛF]ₛF) = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_superCommuteF_ofCrAnOpF_superCommuteF_not_crAnTimeOrderRel'`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L243).

```lean
lemma timeOrderF_superCommuteF_ofCrAnOpF_superCommuteF_not_crAnTimeOrderRel'
    {φ1 φ2 φ3 : 𝓕.CrAnFieldOp} (h12 : ¬ crAnTimeOrderRel φ2 φ1)
    (h13 : ¬ crAnTimeOrderRel φ3 φ1) :
    𝓣ᶠ([ofCrAnOpF φ1, [ofCrAnOpF φ2, ofCrAnOpF φ3]ₛF]ₛF) = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_superCommuteF_ofCrAnOpF_superCommuteF_all_not_crAnTimeOrderRel`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L259).

```lean
lemma timeOrderF_superCommuteF_ofCrAnOpF_superCommuteF_all_not_crAnTimeOrderRel
    (φ1 φ2 φ3 : 𝓕.CrAnFieldOp) (h : ¬
      (crAnTimeOrderRel φ1 φ2 ∧ crAnTimeOrderRel φ1 φ3 ∧
      crAnTimeOrderRel φ2 φ1 ∧ crAnTimeOrderRel φ2 φ3 ∧
      crAnTimeOrderRel φ3 φ1 ∧ crAnTimeOrderRel φ3 φ2)) :
    𝓣ᶠ([ofCrAnOpF φ1, [ofCrAnOpF φ2, ofCrAnOpF φ3]ₛF]ₛF) = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_superCommuteF_ofCrAnOpF_ofCrAnOpF_eq_time`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L297).

```lean
lemma timeOrderF_superCommuteF_ofCrAnOpF_ofCrAnOpF_eq_time
    {φ ψ : 𝓕.CrAnFieldOp} (h1 : crAnTimeOrderRel φ ψ) (h2 : crAnTimeOrderRel ψ φ) :
    𝓣ᶠ([ofCrAnOpF φ, ofCrAnOpF ψ]ₛF) = [ofCrAnOpF φ, ofCrAnOpF ψ]ₛF
```

## Interaction with maxTimeField

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_eq_maxTimeField_mul`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L318).

> In the state algebra time, ordering obeys `T(φ₀φ₁…φₙ) = s * φᵢ * T(φ₀φ₁…φᵢ₋₁φᵢ₊₁…φₙ)`
> where `φᵢ` is the state
> which has maximum time and `s` is the exchange sign of `φᵢ` and `φ₀φ₁…φᵢ₋₁`.

```lean
lemma timeOrderF_eq_maxTimeField_mul (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    𝓣ᶠ(ofFieldOpListF (φ :: φs)) =
    𝓢(𝓕 |>ₛ maxTimeField φ φs, 𝓕 |>ₛ (φ :: φs).take (maxTimeFieldPos φ φs)) •
    ofFieldOpF (maxTimeField φ φs) * 𝓣ᶠ(ofFieldOpListF (eraseMaxTimeField φ φs))
```

**`FieldSpecification.FieldOpFreeAlgebra.timeOrderF_eq_maxTimeField_mul_finset`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean#L334).

> In the state algebra time, ordering obeys `T(φ₀φ₁…φₙ) = s * φᵢ * T(φ₀φ₁…φᵢ₋₁φᵢ₊₁…φₙ)`
> where `φᵢ` is the state
> which has maximum time and `s` is the exchange sign of `φᵢ` and `φ₀φ₁…φᵢ₋₁`.
> Here `s` is written using finite sets.

```lean
lemma timeOrderF_eq_maxTimeField_mul_finset (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    𝓣ᶠ(ofFieldOpListF (φ :: φs)) = 𝓢(𝓕 |>ₛ maxTimeField φ φs, 𝓕 |>ₛ ⟨(eraseMaxTimeField φ φs).get,
      (Finset.filter (fun x =>
        (maxTimeFieldPosFin φ φs).succAbove x < maxTimeFieldPosFin φ φs) Finset.univ)⟩) •
      ofFieldOpF (maxTimeField φ φs) * 𝓣ᶠ(ofFieldOpListF (eraseMaxTimeField φ φs))
```

## Depends on

- [Super Commute](fieldopfreealgebra-supercommute.md)
- [Time ordering of states](fieldspecification-timeorder.md)
- [Field statistics of a finite set.](fieldstatistics-offinset.md)

## Sources

- [Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/TimeOrder.lean)

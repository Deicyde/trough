---
declaration: module
origin: cited
lean: FieldSpecification.WickAlgebra.ι_timeOrderF_superCommuteF_superCommuteF_eq_time_ofCrAnListF, FieldSpecification.WickAlgebra.ι_timeOrderF_superCommuteF_superCommuteF_ofCrAnListF, FieldSpecification.WickAlgebra.ι_timeOrderF_superCommuteF_superCommuteF, FieldSpecification.WickAlgebra.ι_timeOrderF_superCommuteF_eq_time, FieldSpecification.WickAlgebra.ι_timeOrderF_superCommuteF_ne_time, FieldSpecification.WickAlgebra.ι_timeOrderF_zero_of_mem_ideal, FieldSpecification.WickAlgebra.ι_timeOrderF_eq_of_equiv, FieldSpecification.WickAlgebra.timeOrder
statement: formalized
proof: formalized
---

# Time Ordering on Field operator algebra

The module `Physlib.QFT.PerturbationTheory.WickAlgebra.TimeOrder`, [Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean): 23 declarations, 4 with a docstring.

**`FieldSpecification.WickAlgebra.ι_timeOrderF_superCommuteF_superCommuteF_eq_time_ofCrAnListF`**, a lemma, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L26).

```lean
lemma ι_timeOrderF_superCommuteF_superCommuteF_eq_time_ofCrAnListF {φ1 φ2 φ3 : 𝓕.CrAnFieldOp}
    (φs1 φs2 : List 𝓕.CrAnFieldOp) (h :
      crAnTimeOrderRel φ1 φ2 ∧ crAnTimeOrderRel φ1 φ3 ∧
      crAnTimeOrderRel φ2 φ1 ∧ crAnTimeOrderRel φ2 φ3 ∧
      crAnTimeOrderRel φ3 φ1 ∧ crAnTimeOrderRel φ3 φ2) :
    ι 𝓣ᶠ(ofCrAnListF φs1 * [ofCrAnOpF φ1, [ofCrAnOpF φ2, ofCrAnOpF φ3]ₛF]ₛF *
    ofCrAnListF φs2) = 0
```

**`FieldSpecification.WickAlgebra.ι_timeOrderF_superCommuteF_superCommuteF_ofCrAnListF`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L120).

```lean
lemma ι_timeOrderF_superCommuteF_superCommuteF_ofCrAnListF {φ1 φ2 φ3 : 𝓕.CrAnFieldOp}
    (φs1 φs2 : List 𝓕.CrAnFieldOp) :
    ι 𝓣ᶠ(ofCrAnListF φs1 * [ofCrAnOpF φ1, [ofCrAnOpF φ2, ofCrAnOpF φ3]ₛF]ₛF * ofCrAnListF φs2)
    = 0
```

**`FieldSpecification.WickAlgebra.ι_timeOrderF_superCommuteF_superCommuteF`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L133).

```lean
lemma ι_timeOrderF_superCommuteF_superCommuteF {φ1 φ2 φ3 : 𝓕.CrAnFieldOp}
    (a b : 𝓕.FieldOpFreeAlgebra) :
    ι 𝓣ᶠ(a * [ofCrAnOpF φ1, [ofCrAnOpF φ2, ofCrAnOpF φ3]ₛF]ₛF * b) = 0
```

**`FieldSpecification.WickAlgebra.ι_timeOrderF_superCommuteF_eq_time`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L162).

```lean
lemma ι_timeOrderF_superCommuteF_eq_time {φ ψ : 𝓕.CrAnFieldOp}
    (hφψ : crAnTimeOrderRel φ ψ) (hψφ : crAnTimeOrderRel ψ φ) (a b : 𝓕.FieldOpFreeAlgebra) :
    ι 𝓣ᶠ(a * [ofCrAnOpF φ, ofCrAnOpF ψ]ₛF * b) =
    ι ([ofCrAnOpF φ, ofCrAnOpF ψ]ₛF * 𝓣ᶠ(a * b))
```

**`FieldSpecification.WickAlgebra.ι_timeOrderF_superCommuteF_ne_time`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L280).

```lean
lemma ι_timeOrderF_superCommuteF_ne_time {φ ψ : 𝓕.CrAnFieldOp}
    (hφψ : ¬ (crAnTimeOrderRel φ ψ ∧ crAnTimeOrderRel ψ φ)) (a b : 𝓕.FieldOpFreeAlgebra) :
    ι 𝓣ᶠ(a * [ofCrAnOpF φ, ofCrAnOpF ψ]ₛF * b) = 0
```

## Defining time order for `FieldOpFreeAlgebra`.

**`FieldSpecification.WickAlgebra.ι_timeOrderF_zero_of_mem_ideal`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L295).

```lean
lemma ι_timeOrderF_zero_of_mem_ideal (a : 𝓕.FieldOpFreeAlgebra)
    (h : a ∈ TwoSidedIdeal.span 𝓕.fieldOpIdealSet) : ι 𝓣ᶠ(a) = 0
```

**`FieldSpecification.WickAlgebra.ι_timeOrderF_eq_of_equiv`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L326).

```lean
lemma ι_timeOrderF_eq_of_equiv (a b : 𝓕.FieldOpFreeAlgebra) (h : a ≈ b) :
    ι 𝓣ᶠ(a) = ι 𝓣ᶠ(b)
```

**`FieldSpecification.WickAlgebra.timeOrder`**, a def, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L341).

> For a field specification `𝓕`, `timeOrder` is the linear map
>
> `WickAlgebra 𝓕 →ₗ[ℂ] WickAlgebra 𝓕`
>
> defined as the descent of `ι ∘ₗ timeOrderF : FieldOpFreeAlgebra 𝓕 →ₗ[ℂ] WickAlgebra 𝓕` from
> `FieldOpFreeAlgebra 𝓕` to `WickAlgebra 𝓕`.
> This descent exists because `ι ∘ₗ timeOrderF` is well-defined on equivalence classes.
>
> The notation `𝓣(a)` is used for `timeOrder a`.

```lean
noncomputable def timeOrder : WickAlgebra 𝓕 →ₗ[ℂ] WickAlgebra 𝓕
```

## Properties of time ordering

**`FieldSpecification.WickAlgebra.timeOrder_eq_ι_timeOrderF`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L365).

```lean
lemma timeOrder_eq_ι_timeOrderF (a : 𝓕.FieldOpFreeAlgebra) :
    𝓣(ι a) = ι 𝓣ᶠ(a)
```

**`FieldSpecification.WickAlgebra.timeOrder_ofFieldOp_ofFieldOp_ordered`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L368).

```lean
lemma timeOrder_ofFieldOp_ofFieldOp_ordered {φ ψ : 𝓕.FieldOp} (h : timeOrderRel φ ψ) :
    𝓣(ofFieldOp φ * ofFieldOp ψ) = ofFieldOp φ * ofFieldOp ψ
```

**`FieldSpecification.WickAlgebra.timeOrder_ofFieldOp_ofFieldOp_not_ordered`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L373).

```lean
lemma timeOrder_ofFieldOp_ofFieldOp_not_ordered {φ ψ : 𝓕.FieldOp} (h : ¬ timeOrderRel φ ψ) :
    𝓣(ofFieldOp φ * ofFieldOp ψ) = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ψ) • ofFieldOp ψ * ofFieldOp φ
```

**`FieldSpecification.WickAlgebra.timeOrder_ofFieldOp_ofFieldOp_not_ordered_eq_timeOrder`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L379).

```lean
lemma timeOrder_ofFieldOp_ofFieldOp_not_ordered_eq_timeOrder {φ ψ : 𝓕.FieldOp}
    (h : ¬ timeOrderRel φ ψ) :
    𝓣(ofFieldOp φ * ofFieldOp ψ) = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ψ) • 𝓣(ofFieldOp ψ * ofFieldOp φ)
```

**`FieldSpecification.WickAlgebra.timeOrder_ofFieldOpList_nil`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L386).

```lean
lemma timeOrder_ofFieldOpList_nil : 𝓣(ofFieldOpList (𝓕 := 𝓕) []) = 1
```

**`FieldSpecification.WickAlgebra.timeOrder_ofFieldOpList_singleton`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L390).

```lean
lemma timeOrder_ofFieldOpList_singleton (φ : 𝓕.FieldOp) :
    𝓣(ofFieldOpList [φ]) = ofFieldOpList [φ]
```

**`FieldSpecification.WickAlgebra.timeOrder_eq_maxTimeField_mul_finset`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L400).

> For a field specification `𝓕`, the time order operator acting on a
> list of `𝓕.FieldOp`, `𝓣(φ₀…φₙ)`, is equal to
> `𝓢(φᵢ,φ₀…φᵢ₋₁) • φᵢ * 𝓣(φ₀…φᵢ₋₁φᵢ₊₁φₙ)` where `φᵢ` is the maximal time field
> operator in `φ₀…φₙ`.
>
> The proof of this result ultimately relies on basic properties of ordering and signs.

```lean
lemma timeOrder_eq_maxTimeField_mul_finset (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    𝓣(ofFieldOpList (φ :: φs)) = 𝓢(𝓕 |>ₛ maxTimeField φ φs, 𝓕 |>ₛ ⟨(eraseMaxTimeField φ φs).get,
      (Finset.univ.filter (fun x =>
        (maxTimeFieldPosFin φ φs).succAbove x < maxTimeFieldPosFin φ φs))⟩) •
      ofFieldOp (maxTimeField φ φs) * 𝓣(ofFieldOpList (eraseMaxTimeField φ φs))
```

**`FieldSpecification.WickAlgebra.timeOrder_superCommute_eq_time_mid`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L408).

```lean
lemma timeOrder_superCommute_eq_time_mid {φ ψ : 𝓕.CrAnFieldOp}
    (hφψ : crAnTimeOrderRel φ ψ) (hψφ : crAnTimeOrderRel ψ φ) (a b : 𝓕.WickAlgebra) :
    𝓣(a * [ofCrAnOp φ, ofCrAnOp ψ]ₛ * b) =
    [ofCrAnOp φ, ofCrAnOp ψ]ₛ * 𝓣(a * b)
```

**`FieldSpecification.WickAlgebra.timeOrder_superCommute_eq_time_left`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L418).

```lean
lemma timeOrder_superCommute_eq_time_left {φ ψ : 𝓕.CrAnFieldOp}
    (hφψ : crAnTimeOrderRel φ ψ) (hψφ : crAnTimeOrderRel ψ φ) (b : 𝓕.WickAlgebra) :
    𝓣([ofCrAnOp φ, ofCrAnOp ψ]ₛ * b) =
    [ofCrAnOp φ, ofCrAnOp ψ]ₛ * 𝓣(b)
```

**`FieldSpecification.WickAlgebra.timeOrder_superCommute_ne_time`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L424).

```lean
lemma timeOrder_superCommute_ne_time {φ ψ : 𝓕.CrAnFieldOp}
    (hφψ : ¬ (crAnTimeOrderRel φ ψ ∧ crAnTimeOrderRel ψ φ)) :
    𝓣([ofCrAnOp φ, ofCrAnOp ψ]ₛ) = 0
```

**`FieldSpecification.WickAlgebra.timeOrder_superCommute_anPart_ofFieldOp_ne_time`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L430).

```lean
lemma timeOrder_superCommute_anPart_ofFieldOp_ne_time {φ ψ : 𝓕.FieldOp}
    (hφψ : ¬ (timeOrderRel φ ψ ∧ timeOrderRel ψ φ)) :
    𝓣([anPart φ,ofFieldOp ψ]ₛ) = 0
```

**`FieldSpecification.WickAlgebra.timeOrder_timeOrder_mid`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L445).

> For a field specification `𝓕`, and `a`, `b`, `c` in `𝓕.WickAlgebra`, then
> `𝓣(a * b * c) = 𝓣(a * 𝓣(b) * c)`.

```lean
lemma timeOrder_timeOrder_mid (a b c : 𝓕.WickAlgebra) :
    𝓣(a * b * c) = 𝓣(a * 𝓣(b) * c)
```

**`FieldSpecification.WickAlgebra.timeOrder_timeOrder_left`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L453).

```lean
lemma timeOrder_timeOrder_left (b c : 𝓕.WickAlgebra) :
    𝓣(b * c) = 𝓣(𝓣(b) * c)
```

**`FieldSpecification.WickAlgebra.timeOrder_timeOrder_right`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L457).

```lean
lemma timeOrder_timeOrder_right (a b : 𝓕.WickAlgebra) :
    𝓣(a * b) = 𝓣(a * 𝓣(b))
```

**`FieldSpecification.WickAlgebra.timeOrder_timeOrder`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean#L462).

> Time ordering is a projection.

```lean
lemma timeOrder_timeOrder (a : 𝓕.WickAlgebra) :
    𝓣(𝓣(a)) = 𝓣(a)
```

## Depends on

- [Time Ordering in the FieldOpFreeAlgebra](../part-01/fieldopfreealgebra-timeorder.md)
- [SuperCommute on Field operator algebra](wickalgebra-supercommute.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/TimeOrder.lean)

---
declaration: module
origin: cited
lean: FieldSpecification.WickAlgebra.ι_superCommuteF_eq_zero_of_ι_right_zero, FieldSpecification.WickAlgebra.ι_superCommuteF_eq_zero_of_ι_left_zero, FieldSpecification.WickAlgebra.ι_superCommuteF_right_zero_of_mem_ideal, FieldSpecification.WickAlgebra.ι_superCommuteF_eq_of_equiv_right, FieldSpecification.WickAlgebra.superCommuteRight, FieldSpecification.WickAlgebra.superCommuteRight_apply_ι, FieldSpecification.WickAlgebra.superCommuteRight_apply_quot, FieldSpecification.WickAlgebra.superCommuteRight_eq_of_equiv
statement: formalized
proof: formalized
---

# SuperCommute on Field operator algebra

The module `Physlib.QFT.PerturbationTheory.WickAlgebra.SuperCommute`, [Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean): 51 declarations, 2 with a docstring.

**`FieldSpecification.WickAlgebra.ι_superCommuteF_eq_zero_of_ι_right_zero`**, a lemma, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L25).

```lean
lemma ι_superCommuteF_eq_zero_of_ι_right_zero (a b : 𝓕.FieldOpFreeAlgebra) (h : ι b = 0) :
    ι [a, b]ₛF = 0
```

**`FieldSpecification.WickAlgebra.ι_superCommuteF_eq_zero_of_ι_left_zero`**, a lemma, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L30).

```lean
lemma ι_superCommuteF_eq_zero_of_ι_left_zero (a b : 𝓕.FieldOpFreeAlgebra) (h : ι a = 0) :
    ι [a, b]ₛF = 0
```

## Defining normal order for `FiedOpAlgebra`.

**`FieldSpecification.WickAlgebra.ι_superCommuteF_right_zero_of_mem_ideal`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L41).

```lean
lemma ι_superCommuteF_right_zero_of_mem_ideal (a b : 𝓕.FieldOpFreeAlgebra)
    (h : b ∈ TwoSidedIdeal.span 𝓕.fieldOpIdealSet) : ι [a, b]ₛF = 0
```

**`FieldSpecification.WickAlgebra.ι_superCommuteF_eq_of_equiv_right`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L45).

```lean
lemma ι_superCommuteF_eq_of_equiv_right (a b1 b2 : 𝓕.FieldOpFreeAlgebra) (h : b1 ≈ b2) :
    ι [a, b1]ₛF = ι [a, b2]ₛF
```

**`FieldSpecification.WickAlgebra.superCommuteRight`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L52).

> The super commutator on the `WickAlgebra` defined as a linear map `[a,_]ₛ`.

```lean
noncomputable def superCommuteRight (a : 𝓕.FieldOpFreeAlgebra) :
  WickAlgebra 𝓕 →ₗ[ℂ] WickAlgebra 𝓕
```

**`FieldSpecification.WickAlgebra.superCommuteRight_apply_ι`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L69).

```lean
lemma superCommuteRight_apply_ι (a b : 𝓕.FieldOpFreeAlgebra) :
    superCommuteRight a (ι b) = ι [a, b]ₛF
```

**`FieldSpecification.WickAlgebra.superCommuteRight_apply_quot`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L72).

```lean
lemma superCommuteRight_apply_quot (a b : 𝓕.FieldOpFreeAlgebra) :
    superCommuteRight a ⟦b⟧= ι [a, b]ₛF
```

**`FieldSpecification.WickAlgebra.superCommuteRight_eq_of_equiv`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L75).

```lean
lemma superCommuteRight_eq_of_equiv (a1 a2 : 𝓕.FieldOpFreeAlgebra) (h : a1 ≈ a2) :
    superCommuteRight a1 = superCommuteRight a2
```

**`FieldSpecification.WickAlgebra.superCommute`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L96).

> For a field specification `𝓕`, `superCommute` is the linear map
>
> `WickAlgebra 𝓕 →ₗ[ℂ] WickAlgebra 𝓕 →ₗ[ℂ] WickAlgebra 𝓕`
>
> defined as the descent of `ι ∘ superCommuteF` in both arguments.
> In particular for `φs` and `φs'` lists of `𝓕.CrAnFieldOp` in `WickAlgebra 𝓕` the following
> relation holds:
>
> `superCommute φs φs' = φs * φs' - 𝓢(φs, φs') • φs' * φs`
>
> The notation `[a, b]ₛ` is used for `superCommute a b`.

```lean
noncomputable def superCommute : WickAlgebra 𝓕 →ₗ[ℂ]
    WickAlgebra 𝓕 →ₗ[ℂ] WickAlgebra 𝓕
```

**`FieldSpecification.WickAlgebra.superCommute_eq_ι_superCommuteF`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L121).

```lean
lemma superCommute_eq_ι_superCommuteF (a b : 𝓕.FieldOpFreeAlgebra) :
    [ι a, ι b]ₛ = ι [a, b]ₛF
```

## Properties of `superCommute`.

## Properties from the definition of WickAlgebra

**`FieldSpecification.WickAlgebra.superCommute_create_create`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L136).

```lean
lemma superCommute_create_create {φ φ' : 𝓕.CrAnFieldOp}
    (h : 𝓕 |>ᶜ φ = .create) (h' : 𝓕 |>ᶜ φ' = .create) :
    [ofCrAnOp φ, ofCrAnOp φ']ₛ = 0
```

**`FieldSpecification.WickAlgebra.superCommute_annihilate_annihilate`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L141).

```lean
lemma superCommute_annihilate_annihilate {φ φ' : 𝓕.CrAnFieldOp}
    (h : 𝓕 |>ᶜ φ = .annihilate) (h' : 𝓕 |>ᶜ φ' = .annihilate) :
    [ofCrAnOp φ, ofCrAnOp φ']ₛ = 0
```

**`FieldSpecification.WickAlgebra.superCommute_diff_statistic`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L146).

```lean
lemma superCommute_diff_statistic {φ φ' : 𝓕.CrAnFieldOp} (h : (𝓕 |>ₛ φ) ≠ 𝓕 |>ₛ φ') :
    [ofCrAnOp φ, ofCrAnOp φ']ₛ = 0
```

**`FieldSpecification.WickAlgebra.superCommute_ofCrAnOp_ofFieldOp_diff_stat_zero`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L151).

```lean
lemma superCommute_ofCrAnOp_ofFieldOp_diff_stat_zero (φ : 𝓕.CrAnFieldOp) (ψ : 𝓕.FieldOp)
    (h : (𝓕 |>ₛ φ) ≠ (𝓕 |>ₛ ψ)) : [ofCrAnOp φ, ofFieldOp ψ]ₛ = 0
```

**`FieldSpecification.WickAlgebra.superCommute_anPart_ofFieldOpF_diff_grade_zero`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L158).

```lean
lemma superCommute_anPart_ofFieldOpF_diff_grade_zero (φ ψ : 𝓕.FieldOp)
    (h : (𝓕 |>ₛ φ) ≠ (𝓕 |>ₛ ψ)) : [anPart φ, ofFieldOp ψ]ₛ = 0
```

**`FieldSpecification.WickAlgebra.superCommute_ofCrAnOp_ofCrAnOp_mem_center`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L165).

```lean
lemma superCommute_ofCrAnOp_ofCrAnOp_mem_center (φ φ' : 𝓕.CrAnFieldOp) :
    [ofCrAnOp φ, ofCrAnOp φ']ₛ ∈ Subalgebra.center ℂ (WickAlgebra 𝓕)
```

**`FieldSpecification.WickAlgebra.superCommute_ofCrAnOp_ofCrAnOp_commute`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L169).

```lean
lemma superCommute_ofCrAnOp_ofCrAnOp_commute (φ φ' : 𝓕.CrAnFieldOp)
    (a : WickAlgebra 𝓕) :
    a * [ofCrAnOp φ, ofCrAnOp φ']ₛ = [ofCrAnOp φ, ofCrAnOp φ']ₛ * a
```

**`FieldSpecification.WickAlgebra.superCommute_ofCrAnOp_ofFieldOp_mem_center`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L174).

```lean
lemma superCommute_ofCrAnOp_ofFieldOp_mem_center (φ : 𝓕.CrAnFieldOp) (φ' : 𝓕.FieldOp) :
    [ofCrAnOp φ, ofFieldOp φ']ₛ ∈ Subalgebra.center ℂ (WickAlgebra 𝓕)
```

**`FieldSpecification.WickAlgebra.superCommute_ofCrAnOp_ofFieldOp_commute`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L179).

```lean
lemma superCommute_ofCrAnOp_ofFieldOp_commute (φ : 𝓕.CrAnFieldOp) (φ' : 𝓕.FieldOp)
    (a : WickAlgebra 𝓕) : a * [ofCrAnOp φ, ofFieldOp φ']ₛ =
    [ofCrAnOp φ, ofFieldOp φ']ₛ * a
```

**`FieldSpecification.WickAlgebra.superCommute_anPart_ofFieldOp_mem_center`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L184).

```lean
lemma superCommute_anPart_ofFieldOp_mem_center (φ φ' : 𝓕.FieldOp) :
    [anPart φ, ofFieldOp φ']ₛ ∈ Subalgebra.center ℂ (WickAlgebra 𝓕)
```

### `superCommute` on different constructors.

**`FieldSpecification.WickAlgebra.superCommute_ofCrAnList_ofCrAnList`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L196).

```lean
lemma superCommute_ofCrAnList_ofCrAnList (φs φs' : List 𝓕.CrAnFieldOp) :
    [ofCrAnList φs, ofCrAnList φs']ₛ =
    ofCrAnList (φs ++ φs') - 𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs') • ofCrAnList (φs' ++ φs)
```

**`FieldSpecification.WickAlgebra.superCommute_ofCrAnOp_ofCrAnOp`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L201).

```lean
lemma superCommute_ofCrAnOp_ofCrAnOp (φ φ' : 𝓕.CrAnFieldOp) :
    [ofCrAnOp φ, ofCrAnOp φ']ₛ = ofCrAnOp φ * ofCrAnOp φ' -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • ofCrAnOp φ' * ofCrAnOp φ
```

**`FieldSpecification.WickAlgebra.superCommute_ofCrAnList_ofFieldOpList`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L206).

```lean
lemma superCommute_ofCrAnList_ofFieldOpList (φcas : List 𝓕.CrAnFieldOp)
    (φs : List 𝓕.FieldOp) :
    [ofCrAnList φcas, ofFieldOpList φs]ₛ = ofCrAnList φcas * ofFieldOpList φs -
    𝓢(𝓕 |>ₛ φcas, 𝓕 |>ₛ φs) • ofFieldOpList φs * ofCrAnList φcas
```

**`FieldSpecification.WickAlgebra.superCommute_ofFieldOpList_ofFieldOpList`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L212).

```lean
lemma superCommute_ofFieldOpList_ofFieldOpList (φs φs' : List 𝓕.FieldOp) :
    [ofFieldOpList φs, ofFieldOpList φs']ₛ = ofFieldOpList φs * ofFieldOpList φs' -
    𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs') • ofFieldOpList φs' * ofFieldOpList φs
```

**`FieldSpecification.WickAlgebra.superCommute_ofFieldOp_ofFieldOpList`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L217).

```lean
lemma superCommute_ofFieldOp_ofFieldOpList (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    [ofFieldOp φ, ofFieldOpList φs]ₛ = ofFieldOp φ * ofFieldOpList φs -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs) • ofFieldOpList φs * ofFieldOp φ
```

**`FieldSpecification.WickAlgebra.superCommute_ofFieldOpList_ofFieldOp`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L222).

```lean
lemma superCommute_ofFieldOpList_ofFieldOp (φs : List 𝓕.FieldOp) (φ : 𝓕.FieldOp) :
    [ofFieldOpList φs, ofFieldOp φ]ₛ = ofFieldOpList φs * ofFieldOp φ -
    𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φ) • ofFieldOp φ * ofFieldOpList φs
```

**`FieldSpecification.WickAlgebra.superCommute_anPart_crPart`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L227).

```lean
lemma superCommute_anPart_crPart (φ φ' : 𝓕.FieldOp) :
    [anPart φ, crPart φ']ₛ = anPart φ * crPart φ' -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • crPart φ' * anPart φ
```

**`FieldSpecification.WickAlgebra.superCommute_crPart_anPart`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L232).

```lean
lemma superCommute_crPart_anPart (φ φ' : 𝓕.FieldOp) :
    [crPart φ, anPart φ']ₛ = crPart φ * anPart φ' -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • anPart φ' * crPart φ
```

**`FieldSpecification.WickAlgebra.superCommute_crPart_crPart`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L239).

```lean
lemma superCommute_crPart_crPart (φ φ' : 𝓕.FieldOp) : [crPart φ, crPart φ']ₛ = 0
```

**`FieldSpecification.WickAlgebra.superCommute_anPart_anPart`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L245).

```lean
lemma superCommute_anPart_anPart (φ φ' : 𝓕.FieldOp) : [anPart φ, anPart φ']ₛ = 0
```

**`FieldSpecification.WickAlgebra.superCommute_crPart_ofFieldOpList`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L249).

```lean
lemma superCommute_crPart_ofFieldOpList (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    [crPart φ, ofFieldOpList φs]ₛ = crPart φ * ofFieldOpList φs -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs) • ofFieldOpList φs * crPart φ
```

**`FieldSpecification.WickAlgebra.superCommute_anPart_ofFieldOpList`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L254).

```lean
lemma superCommute_anPart_ofFieldOpList (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    [anPart φ, ofFieldOpList φs]ₛ = anPart φ * ofFieldOpList φs -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs) • ofFieldOpList φs * anPart φ
```

**`FieldSpecification.WickAlgebra.superCommute_crPart_ofFieldOp`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L259).

```lean
lemma superCommute_crPart_ofFieldOp (φ φ' : 𝓕.FieldOp) :
    [crPart φ, ofFieldOp φ']ₛ = crPart φ * ofFieldOp φ' -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • ofFieldOp φ' * crPart φ
```

**`FieldSpecification.WickAlgebra.superCommute_anPart_ofFieldOp`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L264).

```lean
lemma superCommute_anPart_ofFieldOp (φ φ' : 𝓕.FieldOp) :
    [anPart φ, ofFieldOp φ']ₛ = anPart φ * ofFieldOp φ' -
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • ofFieldOp φ' * anPart φ
```

## Mul equal superCommute

> Lemmas which rewrite a multiplication of two elements of the algebra as their commuted
> multiplication with a sign plus the super commutator.

**`FieldSpecification.WickAlgebra.ofCrAnList_mul_ofCrAnList_eq_superCommute`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L278).

```lean
lemma ofCrAnList_mul_ofCrAnList_eq_superCommute (φs φs' : List 𝓕.CrAnFieldOp) :
    ofCrAnList φs * ofCrAnList φs' =
    𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs') • ofCrAnList φs' * ofCrAnList φs
    + [ofCrAnList φs, ofCrAnList φs']ₛ
```

**`FieldSpecification.WickAlgebra.ofCrAnOp_mul_ofCrAnList_eq_superCommute`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L284).

```lean
lemma ofCrAnOp_mul_ofCrAnList_eq_superCommute (φ : 𝓕.CrAnFieldOp)
    (φs' : List 𝓕.CrAnFieldOp) : ofCrAnOp φ * ofCrAnList φs' =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs') • ofCrAnList φs' * ofCrAnOp φ
    + [ofCrAnOp φ, ofCrAnList φs']ₛ
```

**`FieldSpecification.WickAlgebra.ofFieldOpList_mul_ofFieldOpList_eq_superCommute`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L291).

```lean
lemma ofFieldOpList_mul_ofFieldOpList_eq_superCommute (φs φs' : List 𝓕.FieldOp) :
    ofFieldOpList φs * ofFieldOpList φs' =
    𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs') • ofFieldOpList φs' * ofFieldOpList φs
    + [ofFieldOpList φs, ofFieldOpList φs']ₛ
```

**`FieldSpecification.WickAlgebra.ofFieldOp_mul_ofFieldOpList_eq_superCommute`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L297).

```lean
lemma ofFieldOp_mul_ofFieldOpList_eq_superCommute (φ : 𝓕.FieldOp) (φs' : List 𝓕.FieldOp) :
    ofFieldOp φ * ofFieldOpList φs' = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs') • ofFieldOpList φs' * ofFieldOp φ
    + [ofFieldOp φ, ofFieldOpList φs']ₛ
```

**`FieldSpecification.WickAlgebra.ofFieldOp_mul_ofFieldOp_eq_superCommute`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L302).

```lean
lemma ofFieldOp_mul_ofFieldOp_eq_superCommute (φ φ' : 𝓕.FieldOp) :
    ofFieldOp φ * ofFieldOp φ' = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • ofFieldOp φ' * ofFieldOp φ
    + [ofFieldOp φ, ofFieldOp φ']ₛ
```

**`FieldSpecification.WickAlgebra.ofFieldOpList_mul_ofFieldOp_eq_superCommute`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L308).

```lean
lemma ofFieldOpList_mul_ofFieldOp_eq_superCommute (φs : List 𝓕.FieldOp) (φ : 𝓕.FieldOp) :
    ofFieldOpList φs * ofFieldOp φ = 𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φ) • ofFieldOp φ * ofFieldOpList φs
    + [ofFieldOpList φs, ofFieldOp φ]ₛ
```

**`FieldSpecification.WickAlgebra.ofCrAnList_mul_ofFieldOpList_eq_superCommute`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L313).

```lean
lemma ofCrAnList_mul_ofFieldOpList_eq_superCommute (φs : List 𝓕.CrAnFieldOp)
    (φs' : List 𝓕.FieldOp) : ofCrAnList φs * ofFieldOpList φs' =
    𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs') • ofFieldOpList φs' * ofCrAnList φs
    + [ofCrAnList φs, ofFieldOpList φs']ₛ
```

**`FieldSpecification.WickAlgebra.crPart_mul_anPart_eq_superCommute`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L319).

```lean
lemma crPart_mul_anPart_eq_superCommute (φ φ' : 𝓕.FieldOp) :
    crPart φ * anPart φ' = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • anPart φ' * crPart φ
    + [crPart φ, anPart φ']ₛ
```

**`FieldSpecification.WickAlgebra.anPart_mul_crPart_eq_superCommute`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L324).

```lean
lemma anPart_mul_crPart_eq_superCommute (φ φ' : 𝓕.FieldOp) :
    anPart φ * crPart φ' = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • crPart φ' * anPart φ
    + [anPart φ, crPart φ']ₛ
```

**`FieldSpecification.WickAlgebra.crPart_mul_crPart_swap`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L329).

```lean
lemma crPart_mul_crPart_swap (φ φ' : 𝓕.FieldOp) :
    crPart φ * crPart φ' = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • crPart φ' * crPart φ
```

**`FieldSpecification.WickAlgebra.anPart_mul_anPart_swap`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L334).

```lean
lemma anPart_mul_anPart_swap (φ φ' : 𝓕.FieldOp) :
    anPart φ * anPart φ' = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • anPart φ' * anPart φ
```

## Symmetry of the super commutator.

**`FieldSpecification.WickAlgebra.superCommute_ofCrAnList_ofCrAnList_symm`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L345).

```lean
lemma superCommute_ofCrAnList_ofCrAnList_symm (φs φs' : List 𝓕.CrAnFieldOp) :
    [ofCrAnList φs, ofCrAnList φs']ₛ =
    (- 𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs')) • [ofCrAnList φs', ofCrAnList φs]ₛ
```

**`FieldSpecification.WickAlgebra.superCommute_ofCrAnOp_ofCrAnOp_symm`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L350).

```lean
lemma superCommute_ofCrAnOp_ofCrAnOp_symm (φ φ' : 𝓕.CrAnFieldOp) :
    [ofCrAnOp φ, ofCrAnOp φ']ₛ =
    (- 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ')) • [ofCrAnOp φ', ofCrAnOp φ]ₛ
```

## splitting the super commute into sums

**`FieldSpecification.WickAlgebra.superCommute_ofCrAnList_ofCrAnList_eq_sum`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L361).

```lean
lemma superCommute_ofCrAnList_ofCrAnList_eq_sum (φs φs' : List 𝓕.CrAnFieldOp) :
    [ofCrAnList φs, ofCrAnList φs']ₛ =
    ∑ (n : Fin φs'.length), 𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs'.take n) •
    ofCrAnList (φs'.take n) * [ofCrAnList φs, ofCrAnOp (φs'.get n)]ₛ *
    ofCrAnList (φs'.drop (n + 1))
```

**`FieldSpecification.WickAlgebra.superCommute_ofCrAnOp_ofCrAnList_eq_sum`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L370).

```lean
lemma superCommute_ofCrAnOp_ofCrAnList_eq_sum (φ : 𝓕.CrAnFieldOp)
    (φs' : List 𝓕.CrAnFieldOp) : [ofCrAnOp φ, ofCrAnList φs']ₛ =
    ∑ (n : Fin φs'.length), 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs'.take n) •
    [ofCrAnOp φ, ofCrAnOp (φs'.get n)]ₛ * ofCrAnList (φs'.eraseIdx n)
```

**`FieldSpecification.WickAlgebra.superCommute_ofCrAnList_ofFieldOpList_eq_sum`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L379).

```lean
lemma superCommute_ofCrAnList_ofFieldOpList_eq_sum (φs : List 𝓕.CrAnFieldOp)
    (φs' : List 𝓕.FieldOp) : [ofCrAnList φs, ofFieldOpList φs']ₛ =
    ∑ (n : Fin φs'.length), 𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs'.take n) •
    ofFieldOpList (φs'.take n) * [ofCrAnList φs, ofFieldOp (φs'.get n)]ₛ *
    ofFieldOpList (φs'.drop (n + 1))
```

**`FieldSpecification.WickAlgebra.superCommute_ofCrAnOp_ofFieldOpList_eq_sum`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean#L388).

```lean
lemma superCommute_ofCrAnOp_ofFieldOpList_eq_sum (φ : 𝓕.CrAnFieldOp) (φs' : List 𝓕.FieldOp) :
    [ofCrAnOp φ, ofFieldOpList φs']ₛ =
    ∑ (n : Fin φs'.length), 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs'.take n) •
    [ofCrAnOp φ, ofFieldOp (φs'.get n)]ₛ * ofFieldOpList (φs'.eraseIdx n)
```

## Depends on

- [The Wick Algebra](wickalgebra-basic.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/SuperCommute.lean)

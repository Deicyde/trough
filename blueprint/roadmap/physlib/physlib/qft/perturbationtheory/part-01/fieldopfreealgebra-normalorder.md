---
declaration: module
origin: cited
lean: FieldSpecification.FieldOpFreeAlgebra.normalOrderF, FieldSpecification.FieldOpFreeAlgebra.normalOrderF_ofCrAnListF, FieldSpecification.FieldOpFreeAlgebra.ofCrAnListF_eq_normalOrderF, FieldSpecification.FieldOpFreeAlgebra.normalOrderF_one, FieldSpecification.FieldOpFreeAlgebra.normalOrderF_normalOrderF_mid, FieldSpecification.FieldOpFreeAlgebra.normalOrderF_normalOrderF_right, FieldSpecification.FieldOpFreeAlgebra.normalOrderF_normalOrderF_left, FieldSpecification.FieldOpFreeAlgebra.normalOrderF_ofCrAnListF_cons_create
statement: formalized
proof: formalized
---

# Normal Ordering in the FieldOpFreeAlgebra

The module `Physlib.QFT.PerturbationTheory.FieldOpFreeAlgebra.NormalOrder`, [Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean): 34 declarations, 1 with a docstring.

> In the module
> `Physlib.QFT.PerturbationTheory.FieldSpecification.NormalOrder`
> we defined the normal ordering of a list of `CrAnFieldOp`.
> In this module we extend the normal ordering to a linear map on `FieldOpFreeAlgebra`.
>
> We derive properties of this normal ordering.

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L46).

> For a field specification `𝓕`, `normalOrderF` is the linear map
>
> `FieldOpFreeAlgebra 𝓕 →ₗ[ℂ] FieldOpFreeAlgebra 𝓕`
>
> defined by its action on the basis `ofCrAnListF φs`, taking `ofCrAnListF φs` to
>
> `normalOrderSign φs • ofCrAnListF (normalOrderList φs)`.
>
> That is, `normalOrderF` normal-orders the field operators and multiplies by the sign of the
> normal order.
>
> The notation `𝓝ᶠ(a)` is used for `normalOrderF a` for `a` an element of
> `FieldOpFreeAlgebra 𝓕`.

```lean
def normalOrderF : FieldOpFreeAlgebra 𝓕 →ₗ[ℂ] FieldOpFreeAlgebra 𝓕
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_ofCrAnListF`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L53).

```lean
lemma normalOrderF_ofCrAnListF (φs : List 𝓕.CrAnFieldOp) :
    𝓝ᶠ(ofCrAnListF φs) = normalOrderSign φs • ofCrAnListF (normalOrderList φs)
```

**`FieldSpecification.FieldOpFreeAlgebra.ofCrAnListF_eq_normalOrderF`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L57).

```lean
lemma ofCrAnListF_eq_normalOrderF (φs : List 𝓕.CrAnFieldOp) :
    ofCrAnListF (normalOrderList φs) = normalOrderSign φs • 𝓝ᶠ(ofCrAnListF φs)
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_one`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L62).

```lean
lemma normalOrderF_one : normalOrderF (𝓕 := 𝓕) 1 = 1
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_normalOrderF_mid`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L66).

```lean
lemma normalOrderF_normalOrderF_mid (a b c : 𝓕.FieldOpFreeAlgebra) :
    𝓝ᶠ(a * b * c) = 𝓝ᶠ(a * 𝓝ᶠ(b) * c)
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_normalOrderF_right`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L116).

```lean
lemma normalOrderF_normalOrderF_right (a b : 𝓕.FieldOpFreeAlgebra) :
    𝓝ᶠ(a * b) = 𝓝ᶠ(a * 𝓝ᶠ(b))
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_normalOrderF_left`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L120).

```lean
lemma normalOrderF_normalOrderF_left (a b : 𝓕.FieldOpFreeAlgebra) :
    𝓝ᶠ(a * b) = 𝓝ᶠ(𝓝ᶠ(a) * b)
```

## Normal ordering with a creation operator on the left or annihilation on the right

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_ofCrAnListF_cons_create`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L130).

```lean
lemma normalOrderF_ofCrAnListF_cons_create (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.create) (φs : List 𝓕.CrAnFieldOp) :
    𝓝ᶠ(ofCrAnListF (φ :: φs)) = ofCrAnOpF φ * 𝓝ᶠ(ofCrAnListF φs)
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_create_mul`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L137).

```lean
lemma normalOrderF_create_mul (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.create) (a : FieldOpFreeAlgebra 𝓕) :
    𝓝ᶠ(ofCrAnOpF φ * a) = ofCrAnOpF φ * 𝓝ᶠ(a)
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_ofCrAnListF_append_annihilate`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L147).

```lean
lemma normalOrderF_ofCrAnListF_append_annihilate (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.annihilate) (φs : List 𝓕.CrAnFieldOp) :
    𝓝ᶠ(ofCrAnListF (φs ++ [φ])) = 𝓝ᶠ(ofCrAnListF φs) * ofCrAnOpF φ
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_mul_annihilate`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L154).

```lean
lemma normalOrderF_mul_annihilate (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.annihilate)
    (a : FieldOpFreeAlgebra 𝓕) : 𝓝ᶠ(a * ofCrAnOpF φ) = 𝓝ᶠ(a) * ofCrAnOpF φ
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_crPartF_mul`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L165).

```lean
lemma normalOrderF_crPartF_mul (φ : 𝓕.FieldOp) (a : FieldOpFreeAlgebra 𝓕) :
    𝓝ᶠ(crPartF φ * a) =
    crPartF φ * 𝓝ᶠ(a)
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_mul_anPartF`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L172).

```lean
lemma normalOrderF_mul_anPartF (φ : 𝓕.FieldOp) (a : FieldOpFreeAlgebra 𝓕) :
    𝓝ᶠ(a * anPartF φ) =
    𝓝ᶠ(a) * anPartF φ
```

## Normal ordering for an adjacent creation and annihilation state

> The main result of this section is `normalOrderF_superCommuteF_annihilate_create`.

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_swap_create_annihilate_ofCrAnListF_ofCrAnListF`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L186).

```lean
lemma normalOrderF_swap_create_annihilate_ofCrAnListF_ofCrAnListF (φc φa : 𝓕.CrAnFieldOp)
    (hφc : 𝓕 |>ᶜ φc = CreateAnnihilate.create) (hφa : 𝓕 |>ᶜ φa = CreateAnnihilate.annihilate)
    (φs φs' : List 𝓕.CrAnFieldOp) :
    𝓝ᶠ(ofCrAnListF φs' * ofCrAnOpF φc * ofCrAnOpF φa * ofCrAnListF φs) = 𝓢(𝓕 |>ₛ φc, 𝓕 |>ₛ φa) •
    𝓝ᶠ(ofCrAnListF φs' * ofCrAnOpF φa * ofCrAnOpF φc * ofCrAnListF φs)
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_swap_create_annihilate_ofCrAnListF`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L197).

```lean
lemma normalOrderF_swap_create_annihilate_ofCrAnListF (φc φa : 𝓕.CrAnFieldOp)
    (hφc : 𝓕 |>ᶜ φc = CreateAnnihilate.create) (hφa : 𝓕 |>ᶜ φa = CreateAnnihilate.annihilate)
    (φs : List 𝓕.CrAnFieldOp) (a : 𝓕.FieldOpFreeAlgebra) :
    𝓝ᶠ(ofCrAnListF φs * ofCrAnOpF φc * ofCrAnOpF φa * a) = 𝓢(𝓕 |>ₛ φc, 𝓕 |>ₛ φa) •
    𝓝ᶠ(ofCrAnListF φs * ofCrAnOpF φa * ofCrAnOpF φc * a)
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_swap_create_annihilate`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L211).

```lean
lemma normalOrderF_swap_create_annihilate (φc φa : 𝓕.CrAnFieldOp)
    (hφc : 𝓕 |>ᶜ φc = CreateAnnihilate.create) (hφa : 𝓕 |>ᶜ φa = CreateAnnihilate.annihilate)
    (a b : 𝓕.FieldOpFreeAlgebra) :
    𝓝ᶠ(a * ofCrAnOpF φc * ofCrAnOpF φa * b) = 𝓢(𝓕 |>ₛ φc, 𝓕 |>ₛ φa) •
    𝓝ᶠ(a * ofCrAnOpF φa * ofCrAnOpF φc * b)
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_superCommuteF_create_annihilate`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L226).

```lean
lemma normalOrderF_superCommuteF_create_annihilate (φc φa : 𝓕.CrAnFieldOp)
    (hφc : 𝓕 |>ᶜ φc = CreateAnnihilate.create) (hφa : 𝓕 |>ᶜ φa = CreateAnnihilate.annihilate)
    (a b : 𝓕.FieldOpFreeAlgebra) :
    𝓝ᶠ(a * [ofCrAnOpF φc, ofCrAnOpF φa]ₛF * b) = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_superCommuteF_annihilate_create`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L235).

```lean
lemma normalOrderF_superCommuteF_annihilate_create (φc φa : 𝓕.CrAnFieldOp)
    (hφc : 𝓕 |>ᶜ φc = CreateAnnihilate.create) (hφa : 𝓕 |>ᶜ φa = CreateAnnihilate.annihilate)
    (a b : 𝓕.FieldOpFreeAlgebra) :
    𝓝ᶠ(a * [ofCrAnOpF φa, ofCrAnOpF φc]ₛF * b) = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_swap_crPartF_anPartF`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L242).

```lean
lemma normalOrderF_swap_crPartF_anPartF (φ φ' : 𝓕.FieldOp) (a b : FieldOpFreeAlgebra 𝓕) :
    𝓝ᶠ(a * (crPartF φ) * (anPartF φ') * b) =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') •
    𝓝ᶠ(a * (anPartF φ') * (crPartF φ) * b)
```

## Normal ordering for an anPartF and crPartF

> Using the results from above.

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_swap_anPartF_crPartF`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L261).

```lean
lemma normalOrderF_swap_anPartF_crPartF (φ φ' : 𝓕.FieldOp) (a b : FieldOpFreeAlgebra 𝓕) :
    𝓝ᶠ(a * (anPartF φ) * (crPartF φ') * b) =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • 𝓝ᶠ(a * (crPartF φ') *
      (anPartF φ) * b)
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_superCommuteF_crPartF_anPartF`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L267).

```lean
lemma normalOrderF_superCommuteF_crPartF_anPartF (φ φ' : 𝓕.FieldOp) (a b : FieldOpFreeAlgebra 𝓕) :
    𝓝ᶠ(a * superCommuteF
      (crPartF φ) (anPartF φ') * b) = 0
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_superCommuteF_anPartF_crPartF`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L277).

```lean
lemma normalOrderF_superCommuteF_anPartF_crPartF (φ φ' : 𝓕.FieldOp) (a b : FieldOpFreeAlgebra 𝓕) :
    𝓝ᶠ(a * superCommuteF
    (anPartF φ) (crPartF φ') * b) = 0
```

## The normal ordering of a product of two states

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_crPartF_mul_crPartF`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L294).

```lean
lemma normalOrderF_crPartF_mul_crPartF (φ φ' : 𝓕.FieldOp) :
    𝓝ᶠ(crPartF φ * crPartF φ') =
    crPartF φ * crPartF φ'
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_anPartF_mul_anPartF`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L301).

```lean
lemma normalOrderF_anPartF_mul_anPartF (φ φ' : 𝓕.FieldOp) :
    𝓝ᶠ(anPartF φ * anPartF φ') =
    anPartF φ * anPartF φ'
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_crPartF_mul_anPartF`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L308).

```lean
lemma normalOrderF_crPartF_mul_anPartF (φ φ' : 𝓕.FieldOp) :
    𝓝ᶠ(crPartF φ * anPartF φ') =
    crPartF φ * anPartF φ'
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_anPartF_mul_crPartF`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L315).

```lean
lemma normalOrderF_anPartF_mul_crPartF (φ φ' : 𝓕.FieldOp) :
    𝓝ᶠ(anPartF φ * crPartF φ') =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') •
    (crPartF φ' * anPartF φ)
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_ofFieldOpF_mul_ofFieldOpF`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L321).

```lean
lemma normalOrderF_ofFieldOpF_mul_ofFieldOpF (φ φ' : 𝓕.FieldOp) :
    𝓝ᶠ(ofFieldOpF φ * ofFieldOpF φ') =
    crPartF φ * crPartF φ' +
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') •
    (crPartF φ' * anPartF φ) +
    crPartF φ * anPartF φ' +
    anPartF φ * anPartF φ'
```

## Normal order with super commutators

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_superCommuteF_ofCrAnListF_create_create_ofCrAnListF`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L341).

```lean
lemma normalOrderF_superCommuteF_ofCrAnListF_create_create_ofCrAnListF
    (φc φc' : 𝓕.CrAnFieldOp) (hφc : 𝓕 |>ᶜ φc = CreateAnnihilate.create)
    (hφc' : 𝓕 |>ᶜ φc' = CreateAnnihilate.create) (φs φs' : List 𝓕.CrAnFieldOp) :
    (𝓝ᶠ(ofCrAnListF φs * [ofCrAnOpF φc, ofCrAnOpF φc']ₛF * ofCrAnListF φs')) =
      normalOrderSign (φs ++ φc' :: φc :: φs') •
    (ofCrAnListF (createFilter φs) * [ofCrAnOpF φc, ofCrAnOpF φc']ₛF *
      ofCrAnListF (createFilter φs') * ofCrAnListF (annihilateFilter (φs ++ φs')))
```

**`FieldSpecification.FieldOpFreeAlgebra.normalOrderF_superCommuteF_ofCrAnListF_annihilate_annihilate_ofCrAnListF`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L400).

```lean
lemma normalOrderF_superCommuteF_ofCrAnListF_annihilate_annihilate_ofCrAnListF
    (φa φa' : 𝓕.CrAnFieldOp)
    (hφa : 𝓕 |>ᶜ φa = CreateAnnihilate.annihilate)
    (hφa' : 𝓕 |>ᶜ φa' = CreateAnnihilate.annihilate)
    (φs φs' : List 𝓕.CrAnFieldOp) :
    𝓝ᶠ(ofCrAnListF φs * [ofCrAnOpF φa, ofCrAnOpF φa']ₛF * ofCrAnListF φs') =
      normalOrderSign (φs ++ φa' :: φa :: φs') •
    (ofCrAnListF (createFilter (φs ++ φs'))
      * ofCrAnListF (annihilateFilter φs) * [ofCrAnOpF φa, ofCrAnOpF φa']ₛF
      * ofCrAnListF (annihilateFilter φs'))
```

## Super commutators involving a normal order.

**`FieldSpecification.FieldOpFreeAlgebra.ofCrAnListF_superCommuteF_normalOrderF_ofCrAnListF`**, a lemma, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L474).

```lean
lemma ofCrAnListF_superCommuteF_normalOrderF_ofCrAnListF (φs φs' : List 𝓕.CrAnFieldOp) :
    [ofCrAnListF φs, 𝓝ᶠ(ofCrAnListF φs')]ₛF =
    ofCrAnListF φs * 𝓝ᶠ(ofCrAnListF φs') -
    𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs') • 𝓝ᶠ(ofCrAnListF φs') * ofCrAnListF φs
```

**`FieldSpecification.FieldOpFreeAlgebra.ofCrAnListF_superCommuteF_normalOrderF_ofFieldOpListF`**, a lemma, [line 482](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L482).

```lean
lemma ofCrAnListF_superCommuteF_normalOrderF_ofFieldOpListF (φs : List 𝓕.CrAnFieldOp)
    (φs' : List 𝓕.FieldOp) : [ofCrAnListF φs, 𝓝ᶠ(ofFieldOpListF φs')]ₛF =
    ofCrAnListF φs * 𝓝ᶠ(ofFieldOpListF φs') -
    𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs') • 𝓝ᶠ(ofFieldOpListF φs') * ofCrAnListF φs
```

## Multiplications with normal order written in terms of super commute.

**`FieldSpecification.FieldOpFreeAlgebra.ofCrAnListF_mul_normalOrderF_ofFieldOpListF_eq_superCommuteF`**, a lemma, [line 499](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L499).

```lean
lemma ofCrAnListF_mul_normalOrderF_ofFieldOpListF_eq_superCommuteF (φs : List 𝓕.CrAnFieldOp)
    (φs' : List 𝓕.FieldOp) :
    ofCrAnListF φs * 𝓝ᶠ(ofFieldOpListF φs') =
    𝓢(𝓕 |>ₛ φs, 𝓕 |>ₛ φs') • 𝓝ᶠ(ofFieldOpListF φs') * ofCrAnListF φs
    + [ofCrAnListF φs, 𝓝ᶠ(ofFieldOpListF φs')]ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.ofCrAnOpF_mul_normalOrderF_ofFieldOpListF_eq_superCommuteF`**, a lemma, [line 506](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L506).

```lean
lemma ofCrAnOpF_mul_normalOrderF_ofFieldOpListF_eq_superCommuteF (φ : 𝓕.CrAnFieldOp)
    (φs' : List 𝓕.FieldOp) : ofCrAnOpF φ * 𝓝ᶠ(ofFieldOpListF φs') =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs') • 𝓝ᶠ(ofFieldOpListF φs') * ofCrAnOpF φ
    + [ofCrAnOpF φ, 𝓝ᶠ(ofFieldOpListF φs')]ₛF
```

**`FieldSpecification.FieldOpFreeAlgebra.anPartF_mul_normalOrderF_ofFieldOpListF_eq_superCommuteF`**, a lemma, [line 513](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean#L513).

```lean
lemma anPartF_mul_normalOrderF_ofFieldOpListF_eq_superCommuteF (φ : 𝓕.FieldOp)
    (φs' : List 𝓕.FieldOp) :
    anPartF φ * 𝓝ᶠ(ofFieldOpListF φs') =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs') • 𝓝ᶠ(ofFieldOpListF φs' * anPartF φ)
    + [anPartF φ, 𝓝ᶠ(ofFieldOpListF φs')]ₛF
```

## Depends on

- [Super Commute](fieldopfreealgebra-supercommute.md)
- [Normal Ordering of states](fieldspecification-normalorder.md)

## Sources

- [Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormalOrder.lean)

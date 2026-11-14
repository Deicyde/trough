---
declaration: module
origin: cited
lean: FieldSpecification.WickAlgebra.normalOrder_eq_ι_normalOrderF, FieldSpecification.WickAlgebra.normalOrder_ofCrAnList, FieldSpecification.WickAlgebra.normalOrder_one_eq_one, FieldSpecification.WickAlgebra.normalOrder_ofFieldOpList_nil, FieldSpecification.WickAlgebra.normalOrder_ofCrAnList_nil, FieldSpecification.WickAlgebra.ofCrAnList_eq_normalOrder, FieldSpecification.WickAlgebra.normalOrder_normalOrder_mid, FieldSpecification.WickAlgebra.normalOrder_normalOrder_left
statement: formalized
proof: formalized
---

# Basic properties of normal ordering

The module `Physlib.QFT.PerturbationTheory.WickAlgebra.NormalOrder.Lemmas`, [Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean): 36 declarations, 8 with a docstring.

## Properties of normal ordering.

**`FieldSpecification.WickAlgebra.normalOrder_eq_ι_normalOrderF`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L32).

```lean
lemma normalOrder_eq_ι_normalOrderF (a : 𝓕.FieldOpFreeAlgebra) :
    𝓝(ι a) = ι 𝓝ᶠ(a)
```

**`FieldSpecification.WickAlgebra.normalOrder_ofCrAnList`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L35).

```lean
lemma normalOrder_ofCrAnList (φs : List 𝓕.CrAnFieldOp) :
    𝓝(ofCrAnList φs) = normalOrderSign φs • ofCrAnList (normalOrderList φs)
```

**`FieldSpecification.WickAlgebra.normalOrder_one_eq_one`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L41).

```lean
lemma normalOrder_one_eq_one : normalOrder (𝓕 := 𝓕) 1 = 1
```

**`FieldSpecification.WickAlgebra.normalOrder_ofFieldOpList_nil`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L48).

```lean
lemma normalOrder_ofFieldOpList_nil : normalOrder (𝓕 := 𝓕) (ofFieldOpList []) = 1
```

**`FieldSpecification.WickAlgebra.normalOrder_ofCrAnList_nil`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L56).

```lean
lemma normalOrder_ofCrAnList_nil : normalOrder (𝓕 := 𝓕) (ofCrAnList []) = 1
```

**`FieldSpecification.WickAlgebra.ofCrAnList_eq_normalOrder`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L61).

```lean
lemma ofCrAnList_eq_normalOrder (φs : List 𝓕.CrAnFieldOp) :
    ofCrAnList (normalOrderList φs) = normalOrderSign φs • 𝓝(ofCrAnList φs)
```

**`FieldSpecification.WickAlgebra.normalOrder_normalOrder_mid`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L66).

```lean
lemma normalOrder_normalOrder_mid (a b c : 𝓕.WickAlgebra) :
    𝓝(a * b * c) = 𝓝(a * 𝓝(b) * c)
```

**`FieldSpecification.WickAlgebra.normalOrder_normalOrder_left`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L77).

```lean
lemma normalOrder_normalOrder_left (a b : 𝓕.WickAlgebra) :
    𝓝(a * b) = 𝓝(𝓝(a) * b)
```

**`FieldSpecification.WickAlgebra.normalOrder_normalOrder_right`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L87).

```lean
lemma normalOrder_normalOrder_right (a b : 𝓕.WickAlgebra) :
    𝓝(a * b) = 𝓝(a * 𝓝(b))
```

**`FieldSpecification.WickAlgebra.normalOrder_normalOrder`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L97).

```lean
lemma normalOrder_normalOrder (a : 𝓕.WickAlgebra) : 𝓝(𝓝(a)) = 𝓝(a)
```

## mul anpart and crpart

**`FieldSpecification.WickAlgebra.normalOrder_mul_anPart`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L108).

```lean
lemma normalOrder_mul_anPart (φ : 𝓕.FieldOp) (a : 𝓕.WickAlgebra) :
    𝓝(a * anPart φ) = 𝓝(a) * anPart φ
```

**`FieldSpecification.WickAlgebra.crPart_mul_normalOrder`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L114).

```lean
lemma crPart_mul_normalOrder (φ : 𝓕.FieldOp) (a : 𝓕.WickAlgebra) :
    𝓝(crPart φ * a) = crPart φ * 𝓝(a)
```

### Normal order and super commutes

**`FieldSpecification.WickAlgebra.normalOrder_superCommute_eq_zero`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L129).

> For a field specification `𝓕`, and `a` and `b` in `𝓕.WickAlgebra` the normal ordering
> of the super commutator of `a` and `b` vanishes, i.e. `𝓝([a,b]ₛ) = 0`.

```lean
lemma normalOrder_superCommute_eq_zero (a b : 𝓕.WickAlgebra) :
    𝓝([a, b]ₛ) = 0
```

**`FieldSpecification.WickAlgebra.normalOrder_superCommute_left_eq_zero`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L137).

```lean
lemma normalOrder_superCommute_left_eq_zero (a b c: 𝓕.WickAlgebra) :
    𝓝([a, b]ₛ * c) = 0
```

**`FieldSpecification.WickAlgebra.normalOrder_superCommute_right_eq_zero`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L146).

```lean
lemma normalOrder_superCommute_right_eq_zero (a b c: 𝓕.WickAlgebra) :
    𝓝(c * [a, b]ₛ) = 0
```

**`FieldSpecification.WickAlgebra.normalOrder_superCommute_mid_eq_zero`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L155).

```lean
lemma normalOrder_superCommute_mid_eq_zero (a b c d : 𝓕.WickAlgebra) :
    𝓝(a * [c, d]ₛ * b) = 0
```

### Swapping terms in a normal order.

**`FieldSpecification.WickAlgebra.normalOrder_ofFieldOp_ofFieldOp_swap`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L170).

```lean
lemma normalOrder_ofFieldOp_ofFieldOp_swap (φ φ' : 𝓕.FieldOp) :
    𝓝(ofFieldOp φ * ofFieldOp φ') = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • 𝓝(ofFieldOp φ' * ofFieldOp φ)
```

**`FieldSpecification.WickAlgebra.normalOrder_ofCrAnOp_ofCrAnList`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L175).

```lean
lemma normalOrder_ofCrAnOp_ofCrAnList (φ : 𝓕.CrAnFieldOp)
    (φs : List 𝓕.CrAnFieldOp) : 𝓝(ofCrAnOp φ * ofCrAnList φs) =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs) • 𝓝(ofCrAnList φs * ofCrAnOp φ)
```

**`FieldSpecification.WickAlgebra.normalOrder_ofCrAnOp_ofFieldOpList_swap`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L181).

```lean
lemma normalOrder_ofCrAnOp_ofFieldOpList_swap (φ : 𝓕.CrAnFieldOp) (φ' : List 𝓕.FieldOp) :
    𝓝(ofCrAnOp φ * ofFieldOpList φ') = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') •
    𝓝(ofFieldOpList φ' * ofCrAnOp φ)
```

**`FieldSpecification.WickAlgebra.normalOrder_anPart_ofFieldOpList_swap`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L188).

```lean
lemma normalOrder_anPart_ofFieldOpList_swap (φ : 𝓕.FieldOp) (φ' : List 𝓕.FieldOp) :
    𝓝(anPart φ * ofFieldOpList φ') = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • 𝓝(ofFieldOpList φ' * anPart φ)
```

**`FieldSpecification.WickAlgebra.normalOrder_ofFieldOpList_anPart_swap`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L203).

```lean
lemma normalOrder_ofFieldOpList_anPart_swap (φ : 𝓕.FieldOp) (φ' : List 𝓕.FieldOp) :
    𝓝(ofFieldOpList φ' * anPart φ) = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • 𝓝(anPart φ * ofFieldOpList φ')
```

**`FieldSpecification.WickAlgebra.normalOrder_ofFieldOpList_mul_anPart_swap`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L209).

```lean
lemma normalOrder_ofFieldOpList_mul_anPart_swap (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    𝓝(ofFieldOpList φs) * anPart φ = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs) • 𝓝(anPart φ * ofFieldOpList φs)
```

**`FieldSpecification.WickAlgebra.anPart_mul_normalOrder_ofFieldOpList_eq_superCommute`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L214).

```lean
lemma anPart_mul_normalOrder_ofFieldOpList_eq_superCommute (φ : 𝓕.FieldOp)
    (φs' : List 𝓕.FieldOp) : anPart φ * 𝓝(ofFieldOpList φs') =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs') • 𝓝(ofFieldOpList φs' * anPart φ) +
    [anPart φ, 𝓝(ofFieldOpList φs')]ₛ
```

## Super commutators with a normal ordered term as sums

**`FieldSpecification.WickAlgebra.ofCrAnOp_superCommute_normalOrder_ofCrAnList_sum`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L245).

> For a field specification `𝓕`, an element `φ` of `𝓕.CrAnFieldOp`, a list `φs` of `𝓕.CrAnFieldOp`,
>   the following relation holds
>
> `[φ, 𝓝(φ₀…φₙ)]ₛ = ∑ i, 𝓢(φ, φ₀…φᵢ₋₁) • [φ, φᵢ]ₛ * 𝓝(φ₀…φᵢ₋₁φᵢ₊₁…φₙ)`.
>
> The proof of this result ultimately goes as follows
> - The definition of `normalOrder` is used to rewrite `𝓝(φ₀…φₙ)` as a scalar multiple of
>   a `ofCrAnList φsn` where `φsn` is the normal ordering of `φ₀…φₙ`.
> - `superCommuteF_ofCrAnListF_ofCrAnListF_eq_sum` is used to rewrite the super commutator of `φ`
>   (considered as a list with one element) with
>   `ofCrAnList φsn` as a sum of super commutators, one for each element of `φsn`.
> - The fact that super-commutators are in the center of `𝓕.WickAlgebra` is used to rearrange
>   terms.
> - Properties of ordered lists, and `normalOrderSign_eraseIdx` are then used to complete the proof.

```lean
lemma ofCrAnOp_superCommute_normalOrder_ofCrAnList_sum (φ : 𝓕.CrAnFieldOp)
    (φs : List 𝓕.CrAnFieldOp) : [ofCrAnOp φ, 𝓝(ofCrAnList φs)]ₛ = ∑ n : Fin φs.length,
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ (φs.take n)) • [ofCrAnOp φ, ofCrAnOp φs[n]]ₛ
    * 𝓝(ofCrAnList (φs.eraseIdx n))
```

**`FieldSpecification.WickAlgebra.ofCrAnOp_superCommute_normalOrder_ofFieldOpList_sum`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L271).

```lean
lemma ofCrAnOp_superCommute_normalOrder_ofFieldOpList_sum (φ : 𝓕.CrAnFieldOp)
    (φs : List 𝓕.FieldOp) :
    [ofCrAnOp φ, 𝓝(ofFieldOpList φs)]ₛ = ∑ n : Fin φs.length, 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ (φs.take n)) •
    [ofCrAnOp φ, ofFieldOp φs[n]]ₛ * 𝓝(ofFieldOpList (φs.eraseIdx n))
```

**`FieldSpecification.WickAlgebra.anPart_superCommute_normalOrder_ofFieldOpList_sum`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L299).

> The commutator of the annihilation part of a field operator with a normal ordered list of field
> operators can be decomposed into the sum of the commutators of the annihilation part with each
> element of the list of field operators, i.e.
> `[anPart φ, 𝓝(φ₀…φₙ)]ₛ= ∑ i, 𝓢(φ, φ₀…φᵢ₋₁) • [anPart φ, φᵢ]ₛ * 𝓝(φ₀…φᵢ₋₁φᵢ₊₁…φₙ)`.

```lean
lemma anPart_superCommute_normalOrder_ofFieldOpList_sum (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    [anPart φ, 𝓝(ofFieldOpList φs)]ₛ = ∑ n : Fin φs.length, 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ (φs.take n)) •
    [anPart φ, ofFieldOpF φs[n]]ₛ * 𝓝(ofFieldOpList (φs.eraseIdx n))
```

## Multiplying with normal ordered terms

**`FieldSpecification.WickAlgebra.anPart_mul_normalOrder_ofFieldOpList_eq_superCommute_reorder`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L332).

> Within a proto-operator algebra we have that
> `anPartF φ * 𝓝(φ₀φ₁…φₙ) = 𝓝((anPart φ)φ₀φ₁…φₙ) + [anpart φ, 𝓝(φ₀φ₁…φₙ)]ₛ`.

```lean
lemma anPart_mul_normalOrder_ofFieldOpList_eq_superCommute_reorder (φ : 𝓕.FieldOp)
    (φs : List 𝓕.FieldOp) : anPart φ * 𝓝(ofFieldOpList φs) =
    𝓝(anPart φ * ofFieldOpList φs) + [anPart φ, 𝓝(ofFieldOpList φs)]ₛ
```

**`FieldSpecification.WickAlgebra.ofFieldOp_mul_normalOrder_ofFieldOpList_eq_superCommute`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L343).

> Within a proto-operator algebra we have that
> `φ * 𝓝ᶠ(φ₀φ₁…φₙ) = 𝓝ᶠ(φφ₀φ₁…φₙ) + [anpart φ, 𝓝ᶠ(φ₀φ₁…φₙ)]ₛF`.

```lean
lemma ofFieldOp_mul_normalOrder_ofFieldOpList_eq_superCommute (φ : 𝓕.FieldOp)
    (φs : List 𝓕.FieldOp) : ofFieldOp φ * 𝓝(ofFieldOpList φs) =
    𝓝(ofFieldOp φ * ofFieldOpList φs) + [anPart φ, 𝓝(ofFieldOpList φs)]ₛ
```

**`FieldSpecification.WickAlgebra.contractStateAtIndex`**, a def, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L355).

> In the expansion of `ofFieldOpF φ * normalOrderF (ofFieldOpListF φs)` the element
> of `𝓞.A` associated with contracting `φ` with the (optional) `n`th element of `φs`.

```lean
noncomputable def contractStateAtIndex (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (n : Option (Fin φs.length)) : 𝓕.WickAlgebra
```

**`FieldSpecification.WickAlgebra.ofFieldOp_mul_normalOrder_ofFieldOpList_eq_sum`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L384).

> For a field specification `𝓕`, a `φ` in `𝓕.FieldOp` and a list `φs` of `𝓕.FieldOp`
> then `φ * 𝓝(φ₀φ₁…φₙ)` is equal to
>
> `𝓝(φφ₀φ₁…φₙ) + ∑ i, (𝓢(φ,φ₀φ₁…φᵢ₋₁) • [anPart φ, φᵢ]ₛ) * 𝓝(φ₀…φᵢ₋₁φᵢ₊₁…φₙ)`.
>
> The proof ultimately goes as follows:
> - `ofFieldOp_eq_crPart_add_anPart` is used to split `φ` into its creation and annihilation parts.
> - The following relation is then used
>
>   `crPart φ * 𝓝(φ₀φ₁…φₙ) = 𝓝(crPart φ * φ₀φ₁…φₙ)`.
>
> - It used that `anPart φ * 𝓝(φ₀φ₁…φₙ)` is equal to
>
>   `𝓢(φ, φ₀φ₁…φₙ) 𝓝(φ₀φ₁…φₙ) * anPart φ + [anPart φ, 𝓝(φ₀φ₁…φₙ)]`
>
> - Then it is used that
>
>   `𝓢(φ, φ₀φ₁…φₙ) 𝓝(φ₀φ₁…φₙ) * anPart φ = 𝓝(anPart φ * φ₀φ₁…φₙ)`
>
> - The result `ofCrAnOp_superCommute_normalOrder_ofCrAnList_sum` is used
>   to expand `[anPart φ, 𝓝(φ₀φ₁…φₙ)]` as a sum.

```lean
lemma ofFieldOp_mul_normalOrder_ofFieldOpList_eq_sum (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) :
    ofFieldOp φ * 𝓝(ofFieldOpList φs) =
    ∑ n : Option (Fin φs.length), contractStateAtIndex φ φs n *
    𝓝(ofFieldOpList (optionEraseZ φs φ n))
```

## Cons vs insertIdx for a normal ordered term.

**`FieldSpecification.WickAlgebra.ofFieldOpList_normalOrder_insert`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L404).

> Within a proto-operator algebra, `N(φφ₀φ₁…φₙ) = s • N(φ₀…φₖ₋₁φφₖ…φₙ)`, where
> `s` is the exchange sign for `φ` and `φ₀…φₖ₋₁`.

```lean
lemma ofFieldOpList_normalOrder_insert (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (k : Fin φs.length.succ) : 𝓝(ofFieldOpList (φ :: φs)) =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs.take k) • 𝓝(ofFieldOpList (φs.insertIdx k φ))
```

## The normal ordering of a product of two states

**`FieldSpecification.WickAlgebra.normalOrder_crPart_mul_crPart`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L426).

```lean
lemma normalOrder_crPart_mul_crPart (φ φ' : 𝓕.FieldOp) :
    𝓝(crPart φ * crPart φ') = crPart φ * crPart φ'
```

**`FieldSpecification.WickAlgebra.normalOrder_anPart_mul_anPart`**, a lemma, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L431).

```lean
lemma normalOrder_anPart_mul_anPart (φ φ' : 𝓕.FieldOp) :
    𝓝(anPart φ * anPart φ') = anPart φ * anPart φ'
```

**`FieldSpecification.WickAlgebra.normalOrder_crPart_mul_anPart`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L436).

```lean
lemma normalOrder_crPart_mul_anPart (φ φ' : 𝓕.FieldOp) :
    𝓝(crPart φ * anPart φ') = crPart φ * anPart φ'
```

**`FieldSpecification.WickAlgebra.normalOrder_anPart_mul_crPart`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L441).

```lean
lemma normalOrder_anPart_mul_crPart (φ φ' : 𝓕.FieldOp) :
    𝓝(anPart φ * crPart φ') = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • crPart φ' * anPart φ
```

**`FieldSpecification.WickAlgebra.normalOrder_ofFieldOp_mul_ofFieldOp`**, a lemma, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean#L446).

```lean
lemma normalOrder_ofFieldOp_mul_ofFieldOp (φ φ' : 𝓕.FieldOp) : 𝓝(ofFieldOp φ * ofFieldOp φ') =
    crPart φ * crPart φ' + 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φ') • (crPart φ' * anPart φ) +
    crPart φ * anPart φ' + anPart φ * anPart φ'
```

## Depends on

- [Normal Ordering on Field operator algebra](wickalgebra-normalorder-basic.md)
- [SuperCommute on Field operator algebra](wickalgebra-supercommute.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickAlgebra/NormalOrder/Lemmas.lean)

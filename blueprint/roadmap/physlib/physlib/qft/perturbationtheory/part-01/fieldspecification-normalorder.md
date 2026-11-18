---
declaration: module
origin: cited
lean: FieldSpecification.normalOrderRel, FieldSpecification.normalOrderSign, FieldSpecification.normalOrderSign_mul_self, FieldSpecification.koszulSignInsert_create, FieldSpecification.normalOrderSign_cons_create, FieldSpecification.normalOrderSign_singleton, FieldSpecification.normalOrderSign_nil, FieldSpecification.koszulSignInsert_append_annihilate
statement: formalized
proof: formalized
---

# Normal Ordering of states

The module `Physlib.QFT.PerturbationTheory.FieldSpecification.NormalOrder`, [Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean): 38 declarations (3 instances with no name), 8 with a docstring.

**`FieldSpecification.normalOrderRel`**, a def, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L30).

> For a field specification `𝓕`, `𝓕.normalOrderRel` is a relation on `𝓕.CrAnFieldOp`
> representing normal ordering. It is defined such that `𝓕.normalOrderRel φ₀ φ₁`
> is true if one of the following is true
> - `φ₀` is a field creation operator
> - `φ₁` is a field annihilation operator.
>
> Thus, colloquially `𝓕.normalOrderRel φ₀ φ₁` says the creation operators are less than
> annihilation operators.

```lean
def normalOrderRel : 𝓕.CrAnFieldOp → 𝓕.CrAnFieldOp → Prop
```

**An instance with no name**, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L34).

> Normal ordering is total.

```lean
instance : Std.Total 𝓕.normalOrderRel
```

**An instance with no name**, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L38).

> Normal ordering is transitive.

```lean
instance : IsTrans 𝓕.CrAnFieldOp 𝓕.normalOrderRel
```

**An instance with no name**, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L42).

> A decidable instance on the normal ordering relation.

```lean
instance (φ φ' : 𝓕.CrAnFieldOp) : Decidable (normalOrderRel φ φ')
```

## Normal order sign.

**`FieldSpecification.normalOrderSign`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L54).

> For a field specification `𝓕`, and a list `φs` of `𝓕.CrAnFieldOp`, `𝓕.normalOrderSign φs` is the
> sign corresponding to the number of `fermionic`-`fermionic` exchanges undertaken to normal-order
> `φs` using the insertion sort algorithm.

```lean
def normalOrderSign (φs : List 𝓕.CrAnFieldOp) : ℂ
```

**`FieldSpecification.normalOrderSign_mul_self`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L58).

```lean
lemma normalOrderSign_mul_self (φs : List 𝓕.CrAnFieldOp) :
    normalOrderSign φs * normalOrderSign φs = 1
```

**`FieldSpecification.koszulSignInsert_create`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L62).

```lean
lemma koszulSignInsert_create (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.create) : (φs : List 𝓕.CrAnFieldOp) →
    Wick.koszulSignInsert 𝓕.crAnStatistics normalOrderRel φ φs = 1
```

**`FieldSpecification.normalOrderSign_cons_create`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L74).

```lean
lemma normalOrderSign_cons_create (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.create) (φs : List 𝓕.CrAnFieldOp) :
    normalOrderSign (φ :: φs) = normalOrderSign φs
```

**`FieldSpecification.normalOrderSign_singleton`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L80).

```lean
lemma normalOrderSign_singleton (φ : 𝓕.CrAnFieldOp) : normalOrderSign [φ] = 1
```

**`FieldSpecification.normalOrderSign_nil`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L84).

```lean
lemma normalOrderSign_nil : normalOrderSign (𝓕 := 𝓕) [] = 1
```

**`FieldSpecification.koszulSignInsert_append_annihilate`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L86).

```lean
lemma koszulSignInsert_append_annihilate (φ' φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.annihilate) :
    (φs : List 𝓕.CrAnFieldOp) →
    Wick.koszulSignInsert 𝓕.crAnStatistics normalOrderRel φ' (φs ++ [φ]) =
    Wick.koszulSignInsert 𝓕.crAnStatistics normalOrderRel φ' φs
```

**`FieldSpecification.normalOrderSign_append_annihilate`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L99).

```lean
lemma normalOrderSign_append_annihilate (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.annihilate) :
    (φs : List 𝓕.CrAnFieldOp) →
    normalOrderSign (φs ++ [φ]) = normalOrderSign φs
```

**`FieldSpecification.koszulSignInsert_annihilate_cons_create`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L110).

```lean
lemma koszulSignInsert_annihilate_cons_create (φc φa : 𝓕.CrAnFieldOp)
    (hφc : 𝓕 |>ᶜ φc = CreateAnnihilate.create)
    (hφa : 𝓕 |>ᶜ φa = CreateAnnihilate.annihilate)
    (φs : List 𝓕.CrAnFieldOp) :
    Wick.koszulSignInsert 𝓕.crAnStatistics normalOrderRel φa (φc :: φs)
    = FieldStatistic.exchangeSign (𝓕.crAnStatistics φc) (𝓕.crAnStatistics φa) *
    Wick.koszulSignInsert 𝓕.crAnStatistics normalOrderRel φa φs
```

**`FieldSpecification.normalOrderSign_swap_create_annihilate_fst`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L125).

```lean
lemma normalOrderSign_swap_create_annihilate_fst (φc φa : 𝓕.CrAnFieldOp)
    (hφc : 𝓕 |>ᶜ φc = CreateAnnihilate.create)
    (hφa : 𝓕 |>ᶜ φa = CreateAnnihilate.annihilate)
    (φs : List 𝓕.CrAnFieldOp) :
    normalOrderSign (φc :: φa :: φs) =
    FieldStatistic.exchangeSign (𝓕.crAnStatistics φc) (𝓕.crAnStatistics φa) *
    normalOrderSign (φa :: φc :: φs)
```

**`FieldSpecification.koszulSignInsert_swap`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L140).

```lean
lemma koszulSignInsert_swap (φ φc φa : 𝓕.CrAnFieldOp) (φs φs' : List 𝓕.CrAnFieldOp) :
    Wick.koszulSignInsert 𝓕.crAnStatistics normalOrderRel φ (φs ++ φa :: φc :: φs')
    = Wick.koszulSignInsert 𝓕.crAnStatistics normalOrderRel φ (φs ++ φc :: φa :: φs')
```

**`FieldSpecification.normalOrderSign_swap_create_annihilate`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L145).

```lean
lemma normalOrderSign_swap_create_annihilate (φc φa : 𝓕.CrAnFieldOp)
    (hφc : 𝓕 |>ᶜ φc = CreateAnnihilate.create) (hφa : 𝓕 |>ᶜ φa = CreateAnnihilate.annihilate) :
    (φs φs' : List 𝓕.CrAnFieldOp) → normalOrderSign (φs ++ φc :: φa :: φs') =
    FieldStatistic.exchangeSign (𝓕.crAnStatistics φc) (𝓕.crAnStatistics φa) *
    normalOrderSign (φs ++ φa :: φc :: φs')
```

**`FieldSpecification.normalOrderSign_swap_create_create_fst`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L163).

```lean
lemma normalOrderSign_swap_create_create_fst (φc φc' : 𝓕.CrAnFieldOp)
    (hφc : 𝓕 |>ᶜ φc = CreateAnnihilate.create) (hφc' : 𝓕 |>ᶜ φc' = CreateAnnihilate.create)
    (φs : List 𝓕.CrAnFieldOp) :
    normalOrderSign (φc :: φc' :: φs) = normalOrderSign (φc' :: φc :: φs)
```

**`FieldSpecification.normalOrderSign_swap_create_create`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L170).

```lean
lemma normalOrderSign_swap_create_create (φc φc' : 𝓕.CrAnFieldOp)
    (hφc : 𝓕 |>ᶜ φc = CreateAnnihilate.create) (hφc' : 𝓕 |>ᶜ φc' = CreateAnnihilate.create) :
    (φs φs' : List 𝓕.CrAnFieldOp) →
    normalOrderSign (φs ++ φc :: φc' :: φs') = normalOrderSign (φs ++ φc' :: φc :: φs')
```

**`FieldSpecification.normalOrderSign_swap_annihilate_annihilate_fst`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L186).

```lean
lemma normalOrderSign_swap_annihilate_annihilate_fst (φa φa' : 𝓕.CrAnFieldOp)
    (hφa : 𝓕 |>ᶜ φa = CreateAnnihilate.annihilate)
    (hφa' : 𝓕 |>ᶜ φa' = CreateAnnihilate.annihilate)
    (φs : List 𝓕.CrAnFieldOp) :
    normalOrderSign (φa :: φa' :: φs) =
    normalOrderSign (φa' :: φa :: φs)
```

**`FieldSpecification.normalOrderSign_swap_annihilate_annihilate`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L204).

```lean
lemma normalOrderSign_swap_annihilate_annihilate (φa φa' : 𝓕.CrAnFieldOp)
    (hφa : 𝓕 |>ᶜ φa = CreateAnnihilate.annihilate)
    (hφa' : 𝓕 |>ᶜ φa' = CreateAnnihilate.annihilate) : (φs φs' : List 𝓕.CrAnFieldOp) →
    normalOrderSign (φs ++ φa :: φa' :: φs') = normalOrderSign (φs ++ φa' :: φa :: φs')
```

> ## Normal order of lists

**`FieldSpecification.normalOrderList`**, a def, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L237).

> For a field specification `𝓕`, and a list `φs` of `𝓕.CrAnFieldOp`,
> `𝓕.normalOrderList φs` is the list `φs` normal-ordered using the
> insertion sort algorithm. It puts creation operators on the left and annihilation operators on
> the right. For example:
>
> `𝓕.normalOrderList [φ1c, φ1a, φ2c, φ2a] = [φ1c, φ2c, φ1a, φ2a]`

```lean
def normalOrderList (φs : List 𝓕.CrAnFieldOp) : List 𝓕.CrAnFieldOp
```

**`FieldSpecification.normalOrderList_nil`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L241).

```lean
lemma normalOrderList_nil : normalOrderList (𝓕 := 𝓕) [] = []
```

**`FieldSpecification.normalOrderList_statistics`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L245).

```lean
lemma normalOrderList_statistics (φs : List 𝓕.CrAnFieldOp) :
    (𝓕 |>ₛ (normalOrderList φs)) = 𝓕 |>ₛ φs
```

**`FieldSpecification.orderedInsert_create`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L249).

```lean
lemma orderedInsert_create (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.create) :
    (φs : List 𝓕.CrAnFieldOp) → List.orderedInsert normalOrderRel φ φs = φ :: φs
```

**`FieldSpecification.normalOrderList_cons_create`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L260).

```lean
lemma normalOrderList_cons_create (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.create) (φs : List 𝓕.CrAnFieldOp) :
    normalOrderList (φ :: φs) = φ :: normalOrderList φs
```

**`FieldSpecification.orderedInsert_append_annihilate`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L266).

```lean
lemma orderedInsert_append_annihilate (φ' φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.annihilate) :
    (φs : List 𝓕.CrAnFieldOp) → List.orderedInsert normalOrderRel φ' (φs ++ [φ]) =
    List.orderedInsert normalOrderRel φ' φs ++ [φ]
```

**`FieldSpecification.normalOrderList_append_annihilate`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L280).

```lean
lemma normalOrderList_append_annihilate (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.annihilate) :
    (φs : List 𝓕.CrAnFieldOp) →
    normalOrderList (φs ++ [φ]) = normalOrderList φs ++ [φ]
```

**`FieldSpecification.normalOrder_swap_create_annihilate_fst`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L292).

```lean
lemma normalOrder_swap_create_annihilate_fst (φc φa : 𝓕.CrAnFieldOp)
    (hφc : 𝓕 |>ᶜ φc = CreateAnnihilate.create)
    (hφa : 𝓕 |>ᶜ φa = CreateAnnihilate.annihilate)
    (φs : List 𝓕.CrAnFieldOp) :
    normalOrderList (φc :: φa :: φs) = normalOrderList (φa :: φc :: φs)
```

**`FieldSpecification.normalOrderList_swap_create_annihilate`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L310).

```lean
lemma normalOrderList_swap_create_annihilate (φc φa : 𝓕.CrAnFieldOp)
    (hφc : 𝓕 |>ᶜ φc = CreateAnnihilate.create)
    (hφa : 𝓕 |>ᶜ φa = CreateAnnihilate.annihilate) :
    (φs φs' : List 𝓕.CrAnFieldOp) →
    normalOrderList (φs ++ φc :: φa :: φs') = normalOrderList (φs ++ φa :: φc :: φs')
```

**`FieldSpecification.normalOrderEquiv`**, a def, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L329).

> For a list of creation and annihilation states, the equivalence between
> `Fin φs.length` and `Fin (normalOrderList φs).length` taking each position in `φs`
> to it's corresponding position in the normal ordered list. This assumes that
> we are using the insertion sort method.
> For example:
> - For `[φ1c, φ1a, φ2c, φ2a]` this equivalence sends `0 ↦ 0`, `1 ↦ 2`, `2 ↦ 1`, `3 ↦ 3`.

```lean
def normalOrderEquiv {φs : List 𝓕.CrAnFieldOp} : Fin φs.length ≃ Fin (normalOrderList φs).length
```

**`FieldSpecification.sum_normalOrderList_length`**, a lemma, [line 332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L332).

```lean
lemma sum_normalOrderList_length {M : Type} [AddCommMonoid M]
    (φs : List 𝓕.CrAnFieldOp) (f : Fin (normalOrderList φs).length → M) :
    ∑ (n : Fin (normalOrderList φs).length), f n = ∑ (n : Fin φs.length), f (normalOrderEquiv n)
```

**`FieldSpecification.normalOrderList_get_normalOrderEquiv`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L339).

```lean
lemma normalOrderList_get_normalOrderEquiv {φs : List 𝓕.CrAnFieldOp} (n : Fin φs.length) :
    (normalOrderList φs)[(normalOrderEquiv n).val] = φs[n.val]
```

**`FieldSpecification.normalOrderList_eraseIdx_normalOrderEquiv`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L348).

```lean
lemma normalOrderList_eraseIdx_normalOrderEquiv {φs : List 𝓕.CrAnFieldOp} (n : Fin φs.length) :
    (normalOrderList φs).eraseIdx (normalOrderEquiv n).val =
    normalOrderList (φs.eraseIdx n.val)
```

**`FieldSpecification.normalOrderSign_eraseIdx`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L362).

> For a field specification `𝓕`, a list `φs = φ₀…φₙ` of `𝓕.CrAnFieldOp` and an `i < φs.length`,
> then
> `normalOrderSign (φ₀…φᵢ₋₁φᵢ₊₁…φₙ)` is equal to the product of
> - `normalOrderSign φ₀…φₙ`,
> - `𝓢(φᵢ, φ₀…φᵢ₋₁)` i.e. the sign needed to remove `φᵢ` from `φ₀…φₙ`,
> - `𝓢(φᵢ, _)` where `_` is the list of elements appearing before `φᵢ` after normal ordering,
>   i.e.
>   the sign needed to insert `φᵢ` back into the normal-ordered list at the correct place.

```lean
lemma normalOrderSign_eraseIdx (φs : List 𝓕.CrAnFieldOp) (i : Fin φs.length) :
    normalOrderSign (φs.eraseIdx i) = normalOrderSign φs *
    𝓢(𝓕 |>ₛ (φs.get i), 𝓕 |>ₛ (φs.take i)) *
    𝓢(𝓕 |>ₛ (φs.get i), 𝓕 |>ₛ ((normalOrderList φs).take (normalOrderEquiv i)))
```

**`FieldSpecification.orderedInsert_createFilter_append_annihilate`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L369).

```lean
lemma orderedInsert_createFilter_append_annihilate (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.annihilate) : (φs φs' : List 𝓕.CrAnFieldOp) →
    List.orderedInsert normalOrderRel φ (createFilter φs ++ φs') =
    createFilter φs ++ List.orderedInsert normalOrderRel φ φs'
```

**`FieldSpecification.orderedInsert_annihilateFilter`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L382).

```lean
lemma orderedInsert_annihilateFilter (φ : 𝓕.CrAnFieldOp) : (φs : List 𝓕.CrAnFieldOp) →
    List.orderedInsert normalOrderRel φ (annihilateFilter φs) =
    φ :: annihilateFilter φs
```

**`FieldSpecification.orderedInsert_createFilter_append_annihilateFilter_annihilate`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L400).

```lean
lemma orderedInsert_createFilter_append_annihilateFilter_annihilate (φ : 𝓕.CrAnFieldOp)
    (hφ : 𝓕 |>ᶜ φ = CreateAnnihilate.annihilate) (φs : List 𝓕.CrAnFieldOp) :
    List.orderedInsert normalOrderRel φ (createFilter φs ++ annihilateFilter φs) =
    createFilter φs ++ φ :: annihilateFilter φs
```

**`FieldSpecification.normalOrderList_eq_createFilter_append_annihilateFilter`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean#L406).

```lean
lemma normalOrderList_eq_createFilter_append_annihilateFilter : (φs : List 𝓕.CrAnFieldOp) →
    normalOrderList φs = createFilter φs ++ annihilateFilter φs
```

## Depends on

- [Filters of lists of CrAnFieldOp](fieldspecification-filters.md)
- [Koszul sign](koszul-koszulsign.md)

## Sources

- [Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldSpecification/NormalOrder.lean)

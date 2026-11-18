---
declaration: module
origin: cited
lean: WickContraction.signFinset_insertAndContract_none, WickContraction.signInsertNone, WickContraction.sign_insert_none_eq_signInsertNone_mul_sign, WickContraction.signInsertNone_eq_mul_fst_snd, WickContraction.signInsertNone_eq_prod_prod, WickContraction.signInsertNone_eq_prod_getDual?_Some, WickContraction.signInsertNone_eq_filter_map, WickContraction.signInsertNone_eq_filterset
statement: formalized
proof: formalized
---

# Sign on inserting and not contracting

The module `Physlib.QFT.PerturbationTheory.WickContraction.Sign.InsertNone`, [Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertNone.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertNone.lean): 10 declarations, 4 with a docstring.

**`WickContraction.signFinset_insertAndContract_none`**, a lemma, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertNone.lean#L27).

```lean
lemma signFinset_insertAndContract_none (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (i1 i2 : Fin φs.length) :
    (φsΛ ↩Λ φ i none).signFinset (Fin.cast (insertIdx_length_fin φ φs i).symm
    (i.succAbove i1)) (Fin.cast (insertIdx_length_fin φ φs i).symm (i.succAbove i2)) =
    if i.succAbove i1 < i ∧ i < i.succAbove i2 then
      Insert.insert (finCongr (insertIdx_length_fin φ φs i).symm i)
      (insertAndContractLiftFinset φ i (φsΛ.signFinset i1 i2))
    else
      (insertAndContractLiftFinset φ i (φsΛ.signFinset i1 i2))
```

**`WickContraction.signInsertNone`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertNone.lean#L88).

> Given a Wick contraction `φsΛ` associated with a list of states `φs`
> and an `i : Fin φs.length.succ`, the change in sign of the contraction associated with
> inserting `φ` into `φs` at position `i` without contracting it.
>
> For each contracted pair `{a1, a2}` in `φsΛ` if `a1 < a2` such that `i` is within the range
> `a1 < i < a2` we pick up a sign equal to `𝓢(φ, φs[a2])`.

```lean
def signInsertNone (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) (φsΛ : WickContraction φs.length)
    (i : Fin φs.length.succ) : ℂ
```

**`WickContraction.sign_insert_none_eq_signInsertNone_mul_sign`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertNone.lean#L95).

```lean
lemma sign_insert_none_eq_signInsertNone_mul_sign (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) :
    (φsΛ ↩Λ φ i none).sign = (φsΛ.signInsertNone φ φs i) * φsΛ.sign
```

**`WickContraction.signInsertNone_eq_mul_fst_snd`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertNone.lean#L116).

```lean
lemma signInsertNone_eq_mul_fst_snd (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) :
  φsΛ.signInsertNone φ φs i = ∏ (a : φsΛ.1),
    (if i.succAbove (φsΛ.fstFieldOfContract a) < i then
      𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs[φsΛ.sndFieldOfContract a])
    else 1) *
    (if i.succAbove (φsΛ.sndFieldOfContract a) < i then
      𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs[φsΛ.sndFieldOfContract a])
    else 1)
```

**`WickContraction.signInsertNone_eq_prod_prod`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertNone.lean#L150).

```lean
lemma signInsertNone_eq_prod_prod (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (hG : GradingCompliant φs φsΛ) :
    φsΛ.signInsertNone φ φs i = ∏ (a : φsΛ.1), ∏ (x : a),
      (if i.succAbove x < i then 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs[x.1]) else 1)
```

**`WickContraction.signInsertNone_eq_prod_getDual?_Some`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertNone.lean#L164).

```lean
lemma signInsertNone_eq_prod_getDual?_Some (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (hG : GradingCompliant φs φsΛ) :
    φsΛ.signInsertNone φ φs i = ∏ (x : Fin φs.length),
      if (φsΛ.getDual? x).isSome then
        (if i.succAbove x < i then 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs[x.1]) else 1)
      else 1
```

**`WickContraction.signInsertNone_eq_filter_map`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertNone.lean#L191).

```lean
lemma signInsertNone_eq_filter_map (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (hG : GradingCompliant φs φsΛ) :
    φsΛ.signInsertNone φ φs i =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ((List.filter (fun x => (φsΛ.getDual? x).isSome ∧ i.succAbove x < i)
    (List.finRange φs.length)).map φs.get))
```

**`WickContraction.signInsertNone_eq_filterset`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertNone.lean#L227).

> The following signs for a grading compliant Wick contraction are equal:
> - The sign `φsΛ.signInsertNone φ φs i` which is given by the following: For each
>   contracted pair `{a1, a2}` in `φsΛ` if `a1 < a2`
>   such that `i` is within the range `a1 < i < a2` we pick up a sign equal to `𝓢(φ, φs[a2])`.
> - The sign got by moving `φ` through `φ₀…φᵢ₋₁` and only picking up a sign when `φᵢ` has a dual.
> These are equal since: Both ignore uncontracted fields, and for a contracted pair `{a1, a2}`
> with `a1 < a2`
> - if `i < a1 < a2` then we don't pick up a sign from either `φₐ₁` or `φₐ₂`.
> - if `a1 < i < a2` then we pick up a sign from `φₐ₁` cases which is equal to `𝓢(φ, φs[a2])`
> (since `φsΛ` is grading compliant).
> - if `a1 < a2 < i` then we pick up a sign from both `φₐ₁` and `φₐ₂` which cancel each other out.

```lean
lemma signInsertNone_eq_filterset (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (hG : GradingCompliant φs φsΛ) :
    φsΛ.signInsertNone φ φs i = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, Finset.univ.filter
    (fun x => (φsΛ.getDual? x).isSome ∧ i.succAbove x < i)⟩)
```

**`WickContraction.sign_insert_none`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertNone.lean#L253).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a graded compliant Wick contraction `φsΛ` of `φs`,
> an `i ≤ φs.length`, and a `φ` in `𝓕.FieldOp`, then
> `(φsΛ ↩Λ φ i none).sign = s * φsΛ.sign`
> where `s` is the sign arrived at by moving `φ` through the elements of `φ₀…φᵢ₋₁` which
> are contracted with some element.
>
> The proof of this result involves a careful consideration of the contributions of different
> `FieldOp`s in `φs` to the sign of `φsΛ ↩Λ φ i none`.

```lean
lemma sign_insert_none (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (hG : GradingCompliant φs φsΛ) :
    (φsΛ ↩Λ φ i none).sign = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, Finset.univ.filter
    (fun x => (φsΛ.getDual? x).isSome ∧ i.succAbove x < i)⟩) * φsΛ.sign
```

**`WickContraction.sign_insert_none_zero`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertNone.lean#L265).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a graded compliant Wick contraction `φsΛ` of `φs`,
> and a `φ` in `𝓕.FieldOp`, then `(φsΛ ↩Λ φ 0 none).sign = φsΛ.sign`.
>
> This is a direct corollary of `sign_insert_none`.

```lean
lemma sign_insert_none_zero (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) : (φsΛ ↩Λ φ 0 none).sign = φsΛ.sign
```

## Depends on

- [Inserting an element into a contraction based on a list](../part-02/wickcontraction-insertandcontract.md)
- [Sign associated with a contraction](wickcontraction-sign-basic.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertNone.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertNone.lean)

---
declaration: module
origin: cited
lean: WickContraction.stat_ofFinset_eq_one_of_gradingCompliant, WickContraction.signFinset_insertAndContract_some, WickContraction.signInsertSomeProd, WickContraction.signInsertSomeCoef, WickContraction.signInsertSome, WickContraction.sign_insert_some, WickContraction.signInsertSomeProd_eq_one_if, WickContraction.signInsertSomeProd_eq_prod_prod
statement: formalized
proof: formalized
---

# Sign on inserting and contracting

The module `Physlib.QFT.PerturbationTheory.WickContraction.Sign.InsertSome`, [Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean): 19 declarations, 8 with a docstring.

> The main results of this file are `sign_insert_some_of_lt` and `sign_insert_some_of_not_lt` which
> write the sign of `(φsΛ ↩Λ φ i (some k)).sign` in terms of the sign of `φsΛ`.

## Sign insert some

**`WickContraction.stat_ofFinset_eq_one_of_gradingCompliant`**, a lemma, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L36).

```lean
lemma stat_ofFinset_eq_one_of_gradingCompliant (φs : List 𝓕.FieldOp)
    (a : Finset (Fin φs.length)) (φsΛ : WickContraction φs.length) (hg : GradingCompliant φs φsΛ)
    (hnon : ∀ i, φsΛ.getDual? i = none → i ∉ a)
    (hsom : ∀ i, (h : (φsΛ.getDual? i).isSome) → i ∈ a → (φsΛ.getDual? i).get h ∈ a) :
    (𝓕 |>ₛ ⟨φs.get, a⟩) = 1
```

**`WickContraction.signFinset_insertAndContract_some`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L56).

```lean
lemma signFinset_insertAndContract_some (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (i1 i2 : Fin φs.length)
    (j : φsΛ.uncontracted) :
    (φsΛ ↩Λ φ i (some j)).signFinset (Fin.cast (insertIdx_length_fin φ φs i).symm
    (i.succAbove i1)) (Fin.cast (insertIdx_length_fin φ φs i).symm (i.succAbove i2)) =
    if i.succAbove i1 < i ∧ i < i.succAbove i2 ∧ (i1 < j) then
      Insert.insert (finCongr (insertIdx_length_fin φ φs i).symm i)
      (insertAndContractLiftFinset φ i (φsΛ.signFinset i1 i2))
    else
      if i1 < j ∧ j < i2 ∧ ¬ i.succAbove i1 < i then
        (insertAndContractLiftFinset φ i (φsΛ.signFinset i1 i2)).erase
        (finCongr (insertIdx_length_fin φ φs i).symm (i.succAbove j))
      else
        (insertAndContractLiftFinset φ i (φsΛ.signFinset i1 i2))
```

**`WickContraction.signInsertSomeProd`**, a def, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L200).

> Given a Wick contraction `φsΛ` the sign defined in the following way,
> related to inserting a field `φ` at position `i` and contracting it with `j : φsΛ.uncontracted`.
> - For each contracted pair `{a1, a2}` in `φsΛ` with `a1 < a2` the sign
>   `𝓢(φ, φₐ₂)` if `a₁ < i ≤ a₂` and `a₁ < j`.
> - For each contracted pair `{a1, a2}` in `φsΛ` with `a1 < a2` the sign
>   `𝓢(φⱼ, φₐ₂)` if `a₁ < j < a₂` and `i < a₁`.

```lean
def signInsertSomeProd (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) (φsΛ : WickContraction φs.length)
    (i : Fin φs.length.succ) (j : φsΛ.uncontracted) : ℂ
```

**`WickContraction.signInsertSomeCoef`**, a def, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L219).

> Given a Wick contraction `φsΛ` the sign defined in the following way,
> related to inserting a field `φ` at position `i` and contracting it with `j : φsΛ.uncontracted`.
> - If `j < i`, for each field `φₐ` in `φⱼ₊₁…φᵢ₋₁` without a dual at position `< j`
>   the sign `𝓢(φₐ, φᵢ)`.
> - Else, for each field `φₐ` in `φᵢ…φⱼ₋₁` of `φs` without dual at position `< i` the sign
>   `𝓢(φₐ, φⱼ)`.

```lean
def signInsertSomeCoef (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) (φsΛ : WickContraction φs.length)
    (i : Fin φs.length.succ) (j : φsΛ.uncontracted) : ℂ
```

**`WickContraction.signInsertSome`**, a def, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L231).

> Given a Wick contraction `φsΛ` associated with a list of states `φs`
> and an `i : Fin φs.length.succ`, the change in sign of the contraction associated with
> inserting `φ` into `φs` at position `i` and contracting it with `j : c.uncontracted`.

```lean
def signInsertSome (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) (φsΛ : WickContraction φs.length)
    (i : Fin φs.length.succ) (j : φsΛ.uncontracted) : ℂ
```

**`WickContraction.sign_insert_some`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L235).

```lean
lemma sign_insert_some (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) (φsΛ : WickContraction φs.length)
    (i : Fin φs.length.succ) (j : φsΛ.uncontracted) :
    (φsΛ ↩Λ φ i (some j)).sign = (φsΛ.signInsertSome φ φs i j) * φsΛ.sign
```

**`WickContraction.signInsertSomeProd_eq_one_if`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L269).

```lean
lemma signInsertSomeProd_eq_one_if (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : φsΛ.uncontracted)
    (hφj : (𝓕 |>ₛ φ) = (𝓕 |>ₛ φs[j.1])) :
  φsΛ.signInsertSomeProd φ φs i j =
  ∏ (a : φsΛ.1),
    if (φsΛ.fstFieldOfContract a) < j
      ∧ (i.succAbove (φsΛ.fstFieldOfContract a) < i ∧ i < i.succAbove (φsΛ.sndFieldOfContract a)
      ∨ j < (φsΛ.sndFieldOfContract a) ∧ ¬ i.succAbove (φsΛ.fstFieldOfContract a) < i)
    then
      𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs[φsΛ.sndFieldOfContract a])
    else
      1
```

**`WickContraction.signInsertSomeProd_eq_prod_prod`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L290).

```lean
lemma signInsertSomeProd_eq_prod_prod (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length)
    (i : Fin φs.length.succ) (j : φsΛ.uncontracted) (hφj : (𝓕 |>ₛ φ) = (𝓕 |>ₛ φs[j.1]))
    (hg : GradingCompliant φs φsΛ) :
  φsΛ.signInsertSomeProd φ φs i j =
  ∏ (a : φsΛ.1), ∏ (x : a.1), if x.1 < j
      ∧ (i.succAbove x.1 < i ∧
      i < i.succAbove ((φsΛ.getDual? x.1).get (getDual?_isSome_of_mem φsΛ a x))
      ∨ j < ((φsΛ.getDual? x.1).get (getDual?_isSome_of_mem φsΛ a x)) ∧ ¬ i.succAbove x < i)
    then
      𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs[x.1])
    else
      1
```

**`WickContraction.signInsertSomeProd_eq_prod_fin`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L315).

```lean
lemma signInsertSomeProd_eq_prod_fin (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length)
    (i : Fin φs.length.succ) (j : φsΛ.uncontracted) (hφj : (𝓕 |>ₛ φ) = (𝓕 |>ₛ φs[j.1]))
    (hg : GradingCompliant φs φsΛ) :
  φsΛ.signInsertSomeProd φ φs i j =
    ∏ (x : Fin φs.length),
      if h : (φsΛ.getDual? x).isSome then
          if x < j ∧ (i.succAbove x < i ∧ i < i.succAbove ((φsΛ.getDual? x).get h)
            ∨ j < ((φsΛ.getDual? x).get h) ∧ ¬ i.succAbove x < i)
          then 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ φs[x.1])
          else 1
      else 1
```

**`WickContraction.signInsertSomeProd_eq_finset`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L333).

```lean
lemma signInsertSomeProd_eq_finset (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length)
    (i : Fin φs.length.succ) (j : φsΛ.uncontracted) (hφj : (𝓕 |>ₛ φ) = (𝓕 |>ₛ φs[j.1]))
    (hg : GradingCompliant φs φsΛ) :
    φsΛ.signInsertSomeProd φ φs i j =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, (Finset.univ.filter (fun x => (φsΛ.getDual? x).isSome ∧
      ∀ (h : (φsΛ.getDual? x).isSome),
      x < j ∧ (i.succAbove x < i ∧ i < i.succAbove ((φsΛ.getDual? x).get h)
      ∨ j < ((φsΛ.getDual? x).get h) ∧ ¬ i.succAbove x < i)))⟩)
```

**`WickContraction.signInsertSomeCoef_if`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L351).

```lean
lemma signInsertSomeCoef_if (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) (φsΛ : WickContraction φs.length)
    (i : Fin φs.length.succ) (j : φsΛ.uncontracted) (hφj : (𝓕 |>ₛ φ) = (𝓕 |>ₛ φs[j.1])) :
    φsΛ.signInsertSomeCoef φ φs i j =
    if i < i.succAbove j then
      𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨(φs.insertIdx i φ).get,
      (signFinset (φsΛ ↩Λ φ i (some j)) (finCongr (insertIdx_length_fin φ φs i).symm i)
      (finCongr (insertIdx_length_fin φ φs i).symm (i.succAbove j)))⟩)
    else
      𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨(φs.insertIdx i φ).get,
      signFinset (φsΛ ↩Λ φ i (some j))
      (finCongr (insertIdx_length_fin φ φs i).symm (i.succAbove j))
      (finCongr (insertIdx_length_fin φ φs i).symm i)⟩)
```

**`WickContraction.stat_signFinset_insert_some_self_fst`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L368).

```lean
lemma stat_signFinset_insert_some_self_fst
    (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp) (φsΛ : WickContraction φs.length)
    (i : Fin φs.length.succ) (j : φsΛ.uncontracted) :
  (𝓕 |>ₛ ⟨(φs.insertIdx i φ).get,
    (signFinset (φsΛ ↩Λ φ i (some j)) (finCongr (insertIdx_length_fin φ φs i).symm i)
      (finCongr (insertIdx_length_fin φ φs i).symm (i.succAbove j)))⟩) =
  𝓕 |>ₛ ⟨φs.get,
    (Finset.univ.filter (fun x => i < i.succAbove x ∧ x < j ∧ ((φsΛ.getDual? x = none) ∨
      ∀ (h : (φsΛ.getDual? x).isSome), i < i.succAbove ((φsΛ.getDual? x).get h))))⟩
```

**`WickContraction.stat_signFinset_insert_some_self_snd`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L400).

```lean
lemma stat_signFinset_insert_some_self_snd (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : φsΛ.uncontracted) :
    (𝓕 |>ₛ ⟨(φs.insertIdx i φ).get,
    (signFinset (φsΛ ↩Λ φ i (some j))
      (finCongr (insertIdx_length_fin φ φs i).symm (i.succAbove j))
      (finCongr (insertIdx_length_fin φ φs i).symm i))⟩) =
    𝓕 |>ₛ ⟨φs.get,
    (Finset.univ.filter (fun x => j < x ∧ i.succAbove x < i ∧ ((φsΛ.getDual? x = none) ∨
      ∀ (h : (φsΛ.getDual? x).isSome), j < ((φsΛ.getDual? x).get h))))⟩
```

**`WickContraction.signInsertSomeCoef_eq_finset`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L432).

```lean
lemma signInsertSomeCoef_eq_finset (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : φsΛ.uncontracted)
    (hφj : (𝓕 |>ₛ φ) = (𝓕 |>ₛ φs[j.1])) : φsΛ.signInsertSomeCoef φ φs i j =
    if i < i.succAbove j then
      𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get,
      (Finset.univ.filter (fun x => i < i.succAbove x ∧ x < j ∧ ((φsΛ.getDual? x = none) ∨
        ∀ (h : (φsΛ.getDual? x).isSome), i < i.succAbove ((φsΛ.getDual? x).get h))))⟩)
    else
      𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get,
        (Finset.univ.filter (fun x => j < x ∧ i.succAbove x < i ∧ ((φsΛ.getDual? x = none) ∨
        ∀ (h : (φsΛ.getDual? x).isSome), j < ((φsΛ.getDual? x).get h))))⟩)
```

**`WickContraction.signInsertSome_mul_filter_contracted_of_lt`**, a lemma, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L474).

> The following two signs are equal for `i.succAbove k < i`. The sign `signInsertSome φ φs φsΛ i k`
> which is constructed as follows:
> 1a. For each contracted pair `{a1, a2}` in `φsΛ` with `a1 < a2` the sign
>   `𝓢(φ, φₐ₂)` if `a₁ < i ≤ a₂` and `a₁ < k`.
> 1b. For each contracted pair `{a1, a2}` in `φsΛ` with `a1 < a2` the sign
>   `𝓢(φⱼ, φₐ₂)` if `a₁ < k < a₂` and `i < a₁`.
> 1c. For each field `φₐ` in `φₖ₊₁…φᵢ₋₁` without a dual at position `< k`
>   the sign `𝓢(φₐ, φᵢ)`.
> and the sign constructed as follows:
> 2a. For each uncontracted field `φₐ` in `φ₀…φₖ` in `φsΛ` the sign `𝓢(φ, φₐ)`
> 2b. For each field in `φₐ` in `φ₀…φᵢ₋₁` the sign `𝓢(φ, φₐ)`.
>
> The outline of why this is true can be got by considering contributions of fields.
> - `φₐ`, `i ≤ a`. No contributions.
> - `φₖ`, `k -> 2a`, `k -> 2b`
> - `φₐ`, `a ≤ k` uncontracted `a -> 2a`, `a -> 2b`.
> - `φₐ`, `k < a < i` uncontracted `a -> 1c`, `a -> 2b`.
>
> For contracted fields `{a₁, a₂}` in `φsΛ` with `a₁ < a₂` we have the following cases:
> - `φₐ₁` `φₐ₂` `a₁ < a₂ < k < i`, `a₁ -> 2b`, `a₂ -> 2b`,
> - `φₐ₁` `φₐ₂` `a₁ < k < a₂ < i`, `a₁ -> 2b`, `a₂ -> 2b`,
> - `φₐ₁` `φₐ₂` `a₁ < k < i ≤ a₂`, `a₁ -> 2b`, `a₂ -> 1a`
> - `φₐ₁` `φₐ₂` `k < a₁ < a₂ < i`, `a₁ -> 2b`, `a₂ -> 2b`, `a₁ -> 1c`, `a₂ -> 1c`
> - `φₐ₁` `φₐ₂` `k < a₁ < i ≤ a₂ `,`a₁ -> 2b`, `a₁ -> 1c`
> - `φₐ₁` `φₐ₂` `k < i ≤ a₁ < a₂ `, No contributions.

```lean
lemma signInsertSome_mul_filter_contracted_of_lt (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (k : φsΛ.uncontracted)
    (hk : i.succAbove k < i) (hg : GradingCompliant φs φsΛ ∧ (𝓕 |>ₛ φ) = 𝓕 |>ₛ φs[k.1]) :
    signInsertSome φ φs φsΛ i k *
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, φsΛ.uncontracted.filter (fun x => x ≤ ↑k)⟩)
    = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, Finset.univ.filter (fun x => i.succAbove x < i)⟩)
```

**`WickContraction.signInsertSome_mul_filter_contracted_of_not_lt`**, a lemma, [line 603](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L603).

> The following two signs are equal for `i < i.succAbove k`.
> The sign `signInsertSome φ φs φsΛ i k` which is constructed
> as follows:
> 1a. For each contracted pair `{a1, a2}` in `φsΛ` with `a1 < a2` the sign
>   `𝓢(φ, φₐ₂)` if `a₁ < i ≤ a₂` and `a₁ < k`.
> 1b. For each contracted pair `{a1, a2}` in `φsΛ` with `a1 < a2` the sign
>   `𝓢(φⱼ, φₐ₂)` if `a₁ < k < a₂` and `i < a₁`.
> 1c. For each field `φₐ` in `φᵢ…φₖ₋₁` of `φs` without dual at position `< i` the sign
>   `𝓢(φₐ, φⱼ)`.
> and the sign constructed as follows:
> 2a. For each uncontracted field `φₐ` in `φ₀…φₖ₋₁` in `φsΛ` the sign `𝓢(φ, φₐ)`
> 2b. For each field in `φₐ` in `φ₀…φᵢ₋₁` the sign `𝓢(φ, φₐ)`.
>
> The outline of why this is true can be got by considering contributions of fields.
> - `φₐ`, `k < a`. No contributions.
> - `φₖ`, No Contributes
> - `φₐ`, `a < i` uncontracted `a -> 2a`, `a -> 2b`.
> - `φₐ`, `i ≤ a < k` uncontracted `a -> 1c`, `a -> 2a`.
>
> For contracted fields `{a₁, a₂}` in `φsΛ` with `a₁ < a₂` we have the following cases:
> - `φₐ₁` `φₐ₂` `a₁ < a₂ < i ≤ k`, `a₁ -> 2b`, `a₂ -> 2b`
> - `φₐ₁` `φₐ₂` `a₁ < i ≤ a₂ < k`, `a₁ -> 2b`, `a₂ -> 1a`
> - `φₐ₁` `φₐ₂` `a₁ < i ≤ k < a₂`, `a₁ -> 2b`, `a₂ -> 1a`
> - `φₐ₁` `φₐ₂` `i ≤ a₁ < a₂ < k`, `a₂ -> 1c`, `a₁ -> 1c`
> - `φₐ₁` `φₐ₂` `i ≤ a₁ < k < a₂ `, `a₁ -> 1c`, `a₁ -> 1b`
> - `φₐ₁` `φₐ₂` `i ≤ k ≤ a₁ < a₂ `, No contributions

```lean
lemma signInsertSome_mul_filter_contracted_of_not_lt (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (k : φsΛ.uncontracted)
    (hk : ¬ i.succAbove k < i) (hg : GradingCompliant φs φsΛ ∧ (𝓕 |>ₛ φ) = 𝓕 |>ₛ φs[k.1]) :
    signInsertSome φ φs φsΛ i k *
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, φsΛ.uncontracted.filter (fun x => x < ↑k)⟩)
    = 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, Finset.univ.filter (fun x => i.succAbove x < i)⟩)
```

**`WickContraction.sign_insert_some_of_lt`**, a lemma, [line 711](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L711).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
>   `𝓕.FieldOp`, a `i ≤ φs.length` and a `k` in `φsΛ.uncontracted` such that `k<i`,
> the sign of `φsΛ ↩Λ φ i (some k)` is equal to the product of
> - the sign associated with moving `φ` through the `φsΛ`-uncontracted `FieldOp` in `φ₀…φₖ`,
> - the sign associated with moving `φ` through all `FieldOp` in `φ₀…φᵢ₋₁`,
> - the sign of `φsΛ`.
>
> The proof of this result involves a careful consideration of the contributions of different
> `FieldOp` in `φs` to the sign of `φsΛ ↩Λ φ i (some k)`.

```lean
lemma sign_insert_some_of_lt (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (k : φsΛ.uncontracted)
    (hk : i.succAbove k < i) (hg : GradingCompliant φs φsΛ ∧ (𝓕 |>ₛ φ) = 𝓕 |>ₛ φs[k.1]) :
    (φsΛ ↩Λ φ i (some k)).sign =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, φsΛ.uncontracted.filter (fun x => x ≤ ↑k)⟩)
    * 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, Finset.univ.filter (fun x => i.succAbove x < i)⟩)
    * φsΛ.sign
```

**`WickContraction.sign_insert_some_of_not_lt`**, a lemma, [line 733](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L733).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
>   `𝓕.FieldOp`, a `i ≤ φs.length` and a `k` in `φsΛ.uncontracted` such that `i ≤ k`,
> the sign of `φsΛ ↩Λ φ i (some k)` is equal to the product of
> - the sign associated with moving `φ` through the `φsΛ`-uncontracted `FieldOp` in `φ₀…φₖ₋₁`,
> - the sign associated with moving `φ` through all the `FieldOp` in `φ₀…φᵢ₋₁`,
> - the sign of `φsΛ`.
>
> The proof of this result involves a careful consideration of the contributions of different
> `FieldOp` in `φs` to the sign of `φsΛ ↩Λ φ i (some k)`.

```lean
lemma sign_insert_some_of_not_lt (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (k : φsΛ.uncontracted)
    (hk : ¬ i.succAbove k < i) (hg : GradingCompliant φs φsΛ ∧ (𝓕 |>ₛ φ) = 𝓕 |>ₛ φs[k.1]) :
    (φsΛ ↩Λ φ i (some k)).sign =
    𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, φsΛ.uncontracted.filter (fun x => x < ↑k)⟩)
    * 𝓢(𝓕 |>ₛ φ, 𝓕 |>ₛ ⟨φs.get, Finset.univ.filter (fun x => i.succAbove x < i)⟩) *
    φsΛ.sign
```

**`WickContraction.sign_insert_some_zero`**, a lemma, [line 753](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean#L753).

> For a list `φs = φ₀…φₙ` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
>   `𝓕.FieldOp`, and a `k` in `φsΛ.uncontracted`,
> the sign of `φsΛ ↩Λ φ 0 (some k)` is equal to the product of
> - the sign associated with moving `φ` through the `φsΛ`-uncontracted `FieldOp` in `φ₀…φₖ₋₁`,
> - the sign of `φsΛ`.
>
> This is a direct corollary of `sign_insert_some_of_not_lt`.

```lean
lemma sign_insert_some_zero (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (k : φsΛ.uncontracted)
    (hn : GradingCompliant φs φsΛ ∧ (𝓕|>ₛφ) = 𝓕|>ₛφs[k.1]) :
    (φsΛ ↩Λ φ 0 k).sign = 𝓢(𝓕|>ₛφ, 𝓕 |>ₛ ⟨φs.get, (φsΛ.uncontracted.filter (fun x => x < ↑k))⟩) *
    φsΛ.sign
```

## Depends on

- [Inserting an element into a contraction based on a list](../part-02/wickcontraction-insertandcontract.md)
- [Sign associated with a contraction](wickcontraction-sign-basic.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Sign/InsertSome.lean)

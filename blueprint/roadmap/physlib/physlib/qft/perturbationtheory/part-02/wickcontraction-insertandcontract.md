---
declaration: module
origin: cited
lean: WickContraction.insertAndContract, WickContraction.insertAndContract_fstFieldOfContract, WickContraction.insertAndContract_sndFieldOfContract, WickContraction.insertAndContract_fstFieldOfContract_some_incl, WickContraction.insertAndContract_none_getDual?_self, WickContraction.insertAndContract_isSome_getDual?_self, WickContraction.insertAndContract_some_getDual?_self_not_none, WickContraction.insertAndContract_some_getDual?_self_eq
statement: formalized
proof: formalized
---

# Inserting an element into a contraction based on a list

The module `Physlib.QFT.PerturbationTheory.WickContraction.InsertAndContract`, [Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean): 24 declarations, 3 with a docstring.

## Inserting an element into a list

**`WickContraction.insertAndContract`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L47).

> Given a Wick contraction `φsΛ` for a list `φs` of `𝓕.FieldOp`,
> an element `φ` of `𝓕.FieldOp`, an `i ≤ φs.length` and a `k`
> in `Option φsΛ.uncontracted` i.e. is either `none` or
> some element of `φsΛ.uncontracted`, the new Wick contraction
> `φsΛ.insertAndContract φ i k` is defined by inserting `φ` into `φs` after
> the first `i`-elements and moving the values representing the contracted pairs in `φsΛ`
> accordingly.
> If `k` is not `none`, but rather `some k`, to this contraction is added the contraction
> of `φ` (at position `i`) with the new position of `k` after `φ` is added.
>
> In other words, `φsΛ.insertAndContract φ i k` is formed by adding `φ` to `φs` at position `i`,
> and contracting `φ` with the field originally at position `k` if `k` is not `none`.
> It is a Wick contraction of the list `φs.insertIdx φ i` corresponding to `φs` with `φ` inserted at
> position `i`.
>
> The notation `φsΛ ↩Λ φ i k` is used to denote `φsΛ.insertAndContract φ i k`.

```lean
def insertAndContract {φs : List 𝓕.FieldOp} (φ : 𝓕.FieldOp) (φsΛ : WickContraction φs.length)
    (i : Fin φs.length.succ) (k : Option φsΛ.uncontracted) :
    WickContraction (φs.insertIdx i φ).length
```

**`WickContraction.insertAndContract_fstFieldOfContract`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L56).

```lean
lemma insertAndContract_fstFieldOfContract (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : Option φsΛ.uncontracted)
    (a : φsΛ.1) : (φsΛ ↩Λ φ i j).fstFieldOfContract
    (congrLift (insertIdx_length_fin φ φs i).symm (insertLift i j a)) =
    finCongr (insertIdx_length_fin φ φs i).symm (i.succAbove (φsΛ.fstFieldOfContract a))
```

**`WickContraction.insertAndContract_sndFieldOfContract`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L64).

```lean
lemma insertAndContract_sndFieldOfContract (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : Option (φsΛ.uncontracted))
    (a : φsΛ.1) : (φsΛ ↩Λ φ i j).sndFieldOfContract
    (congrLift (insertIdx_length_fin φ φs i).symm (insertLift i j a)) =
    finCongr (insertIdx_length_fin φ φs i).symm (i.succAbove (φsΛ.sndFieldOfContract a))
```

**`WickContraction.insertAndContract_fstFieldOfContract_some_incl`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L72).

```lean
lemma insertAndContract_fstFieldOfContract_some_incl (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : φsΛ.uncontracted) :
      (insertAndContract φ φsΛ i (some j)).fstFieldOfContract
      (congrLift (insertIdx_length_fin φ φs i).symm ⟨{i, i.succAbove j}, by
        simp [insertAndContractNat]⟩) =
      if i < i.succAbove j.1 then
      finCongr (insertIdx_length_fin φ φs i).symm i else
      finCongr (insertIdx_length_fin φ φs i).symm (i.succAbove j.1)
```

## insertAndContract and getDual?

**`WickContraction.insertAndContract_none_getDual?_self`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L111).

```lean
lemma insertAndContract_none_getDual?_self (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) :
    (φsΛ ↩Λ φ i none).getDual? (Fin.cast (insertIdx_length_fin φ φs i).symm i) = none
```

**`WickContraction.insertAndContract_isSome_getDual?_self`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L118).

```lean
lemma insertAndContract_isSome_getDual?_self (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : φsΛ.uncontracted) :
    ((φsΛ ↩Λ φ i (some j)).getDual?
    (Fin.cast (insertIdx_length_fin φ φs i).symm i)).isSome
```

**`WickContraction.insertAndContract_some_getDual?_self_not_none`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L124).

```lean
lemma insertAndContract_some_getDual?_self_not_none (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : φsΛ.uncontracted) :
    ¬ ((φsΛ ↩Λ φ i (some j)).getDual?
    (Fin.cast (insertIdx_length_fin φ φs i).symm i)) = none
```

**`WickContraction.insertAndContract_some_getDual?_self_eq`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L131).

```lean
lemma insertAndContract_some_getDual?_self_eq (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : φsΛ.uncontracted) :
    ((φsΛ ↩Λ φ i (some j)).getDual? (Fin.cast (insertIdx_length_fin φ φs i).symm i))
    = some (Fin.cast (insertIdx_length_fin φ φs i).symm (i.succAbove j))
```

**`WickContraction.insertAndContract_some_getDual?_some_eq`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L138).

```lean
lemma insertAndContract_some_getDual?_some_eq (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : φsΛ.uncontracted) :
    ((φsΛ ↩Λ φ i (some j)).getDual?
      (Fin.cast (insertIdx_length_fin φ φs i).symm (i.succAbove j)))
    = some (Fin.cast (insertIdx_length_fin φ φs i).symm i)
```

**`WickContraction.insertAndContract_none_succAbove_getDual?_eq_none_iff`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L149).

```lean
lemma insertAndContract_none_succAbove_getDual?_eq_none_iff (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : Fin φs.length) :
    (φsΛ ↩Λ φ i none).getDual? (Fin.cast (insertIdx_length_fin φ φs i).symm
      (i.succAbove j)) = none ↔ φsΛ.getDual? j = none
```

**`WickContraction.insertAndContract_some_succAbove_getDual?_eq_option`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L156).

```lean
lemma insertAndContract_some_succAbove_getDual?_eq_option (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : Fin φs.length)
    (k : φsΛ.uncontracted) (hkj : j ≠ k.1) :
    (φsΛ ↩Λ φ i (some k)).getDual? (Fin.cast (insertIdx_length_fin φ φs i).symm
    (i.succAbove j)) = Option.map (Fin.cast (insertIdx_length_fin φ φs i).symm ∘ i.succAbove)
    (φsΛ.getDual? j)
```

**`WickContraction.insertAndContract_none_succAbove_getDual?_isSome_iff`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L168).

```lean
lemma insertAndContract_none_succAbove_getDual?_isSome_iff (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : Fin φs.length) :
    ((φsΛ ↩Λ φ i none).getDual? (Fin.cast (insertIdx_length_fin φ φs i).symm
      (i.succAbove j))).isSome ↔ (φsΛ.getDual? j).isSome
```

**`WickContraction.insertAndContract_none_getDual?_get_eq`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L176).

```lean
lemma insertAndContract_none_getDual?_get_eq (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : Fin φs.length)
    (h : ((φsΛ ↩Λ φ i none).getDual? (Fin.cast (insertIdx_length_fin φ φs i).symm
    (i.succAbove j))).isSome) :
    ((φsΛ ↩Λ φ i none).getDual? (Fin.cast (insertIdx_length_fin φ φs i).symm
    (i.succAbove j))).get h = Fin.cast (insertIdx_length_fin φ φs i).symm
    (i.succAbove ((φsΛ.getDual? j).get (by simpa using h)))
```

**`WickContraction.insertAndContract_sndFieldOfContract_some_incl`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L187).

```lean
lemma insertAndContract_sndFieldOfContract_some_incl (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : φsΛ.uncontracted) :
    (φsΛ ↩Λ φ i (some j)).sndFieldOfContract
    (congrLift (insertIdx_length_fin φ φs i).symm ⟨{i, i.succAbove j}, by
      simp [insertAndContractNat]⟩) =
    if i < i.succAbove j.1 then
    finCongr (insertIdx_length_fin φ φs i).symm (i.succAbove j.1) else
    finCongr (insertIdx_length_fin φ φs i).symm i
```

**`WickContraction.insertAndContract_none_prod_contractions`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L219).

```lean
lemma insertAndContract_none_prod_contractions (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ)
    (f : (φsΛ ↩Λ φ i none).1 → M) [CommMonoid M] :
    ∏ a, f a = ∏ (a : φsΛ.1), f (congrLift (insertIdx_length_fin φ φs i).symm
      (insertLift i none a))
```

**`WickContraction.insertAndContract_some_prod_contractions`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L231).

```lean
lemma insertAndContract_some_prod_contractions (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) (j : φsΛ.uncontracted)
    (f : (φsΛ ↩Λ φ i (some j)).1 → M) [CommMonoid M] :
    ∏ a, f a = f (congrLift (insertIdx_length_fin φ φs i).symm
      ⟨{i, i.succAbove j}, by simp [insertAndContractNat]⟩) *
    ∏ (a : φsΛ.1), f (congrLift (insertIdx_length_fin φ φs i).symm (insertLift i (some j) a))
```

**`WickContraction.insertAndContractLiftFinset`**, a def, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L249).

> Given a finite set of `Fin φs.length` the finite set of `(φs.insertIdx i φ).length`
> formed by mapping elements using `i.succAboveEmb` and `finCongr`.

```lean
def insertAndContractLiftFinset (φ : 𝓕.FieldOp) {φs : List 𝓕.FieldOp}
    (i : Fin φs.length.succ) (a : Finset (Fin φs.length)) :
    Finset (Fin (φs.insertIdx i φ).length)
```

**`WickContraction.self_not_mem_insertAndContractLiftFinset`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L255).

```lean
lemma self_not_mem_insertAndContractLiftFinset (φ : 𝓕.FieldOp) {φs : List 𝓕.FieldOp}
    (i : Fin φs.length.succ) (a : Finset (Fin φs.length)) :
    Fin.cast (insertIdx_length_fin φ φs i).symm i ∉ insertAndContractLiftFinset φ i a
```

**`WickContraction.succAbove_mem_insertAndContractLiftFinset`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L264).

```lean
lemma succAbove_mem_insertAndContractLiftFinset (φ : 𝓕.FieldOp) {φs : List 𝓕.FieldOp}
    (i : Fin φs.length.succ) (a : Finset (Fin φs.length)) (j : Fin φs.length) :
    Fin.cast (insertIdx_length_fin φ φs i).symm (i.succAbove j)
    ∈ insertAndContractLiftFinset φ i a ↔ j ∈ a
```

**`WickContraction.insert_fin_eq_self`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L279).

```lean
lemma insert_fin_eq_self (φ : 𝓕.FieldOp) {φs : List 𝓕.FieldOp}
    (i : Fin φs.length.succ) (j : Fin (List.insertIdx φs i φ).length) :
    j = Fin.cast (insertIdx_length_fin φ φs i).symm i
    ∨ ∃ k, j = Fin.cast (insertIdx_length_fin φ φs i).symm (i.succAbove k)
```

**`WickContraction.insertLift_sum`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L308).

> For a list `φs` of `𝓕.FieldOp`, a Wick contraction `φsΛ` of `φs`, an element `φ` of
> `𝓕.FieldOp` and a `i ≤ φs.length` then a sum over
> Wick contractions of `φs` with `φ` inserted at `i` is equal to the sum over Wick contractions
> `φsΛ` of just `φs` and the sum over optional uncontracted elements of the `φsΛ`.
>
> In other words,
>
> `∑ (φsΛ : WickContraction (φs.insertIdx i φ).length), f φsΛ`
>
> where `(φs.insertIdx i φ)` is `φs` with `φ` inserted at position `i`. is equal to
>
> `∑ (φsΛ : WickContraction φs.length), ∑ k, f (φsΛ ↩Λ φ i k) `.
>
> where the sum over `k` is over all `k` in `Option φsΛ.uncontracted`.

```lean
lemma insertLift_sum (φ : 𝓕.FieldOp) {φs : List 𝓕.FieldOp}
    (i : Fin φs.length.succ) [AddCommMonoid M] (f : WickContraction (φs.insertIdx i φ).length → M) :
    ∑ c, f c =
    ∑ (φsΛ : WickContraction φs.length), ∑ (k : Option φsΛ.uncontracted), f (φsΛ ↩Λ φ i k)
```

## Uncontracted list

**`WickContraction.insertAndContract_uncontractedList_none_map`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L321).

```lean
lemma insertAndContract_uncontractedList_none_map (φ : 𝓕.FieldOp) {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length) (i : Fin φs.length.succ) :
    [φsΛ ↩Λ φ i none]ᵘᶜ = List.insertIdx [φsΛ]ᵘᶜ (φsΛ.uncontractedListOrderPos i) φ
```

**`WickContraction.insertAndContract_uncontractedList_none_zero`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L334).

```lean
lemma insertAndContract_uncontractedList_none_zero (φ : 𝓕.FieldOp) {φs : List 𝓕.FieldOp}
    (φsΛ : WickContraction φs.length) :
    [φsΛ ↩Λ φ 0 none]ᵘᶜ = φ :: [φsΛ]ᵘᶜ
```

**`WickContraction.stat_ofFinset_of_insertAndContractLiftFinset`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean#L341).

```lean
lemma stat_ofFinset_of_insertAndContractLiftFinset (φ : 𝓕.FieldOp) (φs : List 𝓕.FieldOp)
    (i : Fin φs.length.succ) (a : Finset (Fin φs.length)) :
    (𝓕 |>ₛ ⟨(φs.insertIdx i φ).get, insertAndContractLiftFinset φ i a⟩) = 𝓕 |>ₛ ⟨φs.get, a⟩
```

## Depends on

- [List lemmas (InsertIdx)](../../../mathematics/formathlib/list-insertidx.md)
- [Field statistics of a finite set.](../part-01/fieldstatistics-offinset.md)
- [List of uncontracted elements of a Wick contraction](../part-03/wickcontraction-uncontractedlist.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/InsertAndContract.lean)

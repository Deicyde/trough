---
declaration: module
origin: cited
lean: WickContraction.fin_list_sorted_monotone_sorted, WickContraction.fin_list_sorted_succAboveEmb_sorted, WickContraction.fin_finset_sort_map_monotone, WickContraction.fin_list_sorted_split, WickContraction.fin_list_sorted_indexOf_filter_le_mem, WickContraction.fin_list_sorted_indexOf_mem, WickContraction.orderedInsert_of_fin_list_sorted, WickContraction.orderedInsert_eq_insertIdx_of_fin_list_sorted
statement: formalized
proof: formalized
---

# List of uncontracted elements of a Wick contraction

The module `Physlib.QFT.PerturbationTheory.WickContraction.UncontractedList`, [Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean): 58 declarations, 6 with a docstring.

## Some properties of lists of fin

**`WickContraction.fin_list_sorted_monotone_sorted`**, a lemma, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L31).

```lean
lemma fin_list_sorted_monotone_sorted {n m : ℕ} (l: List (Fin n)) (hl : l.Pairwise (· ≤ ·))
    (f : Fin n → Fin m) (hf : StrictMono f) : (List.map f l).Pairwise (· ≤ ·)
```

**`WickContraction.fin_list_sorted_succAboveEmb_sorted`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L35).

```lean
lemma fin_list_sorted_succAboveEmb_sorted (l: List (Fin n)) (hl : l.Pairwise (· ≤ ·))
    (i : Fin n.succ) : ((List.map i.succAboveEmb l)).Pairwise (· ≤ ·)
```

**`WickContraction.fin_finset_sort_map_monotone`**, a lemma, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L40).

```lean
lemma fin_finset_sort_map_monotone {n m : ℕ} (a : Finset (Fin n)) (f : Fin n ↪ Fin m)
    (hf : StrictMono f) : (a.sort (· ≤ ·)).map f =
    ((a.map f).sort (· ≤ ·))
```

**`WickContraction.fin_list_sorted_split`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L52).

```lean
lemma fin_list_sorted_split :
    (l : List (Fin n)) → (hl : l.Pairwise (· ≤ ·)) → (i : ℕ) →
    l = l.filter (fun x => x.1 < i) ++ l.filter (fun x => i ≤ x.1)
```

**`WickContraction.fin_list_sorted_indexOf_filter_le_mem`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L84).

```lean
lemma fin_list_sorted_indexOf_filter_le_mem :
    (l : List (Fin n)) → (hl : l.Pairwise (· ≤ ·)) → (i : Fin n) →
    (hl : i ∈ l) →
    List.idxOf i (List.filter (fun x => decide (↑i ≤ ↑x)) l) = 0
```

**`WickContraction.fin_list_sorted_indexOf_mem`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L108).

```lean
lemma fin_list_sorted_indexOf_mem :
    (l : List (Fin n)) → (hl : l.Pairwise (· ≤ ·)) → (i : Fin n) →
    (hi : i ∈ l) →
    l.idxOf i = (l.filter (fun x => x.1 < i.1)).length
```

**`WickContraction.orderedInsert_of_fin_list_sorted`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L118).

```lean
lemma orderedInsert_of_fin_list_sorted :
    (l : List (Fin n)) → (hl : l.Pairwise (· ≤ ·)) → (i : Fin n) →
    List.orderedInsert (· ≤ ·) i l = l.filter (fun x => x.1 < i.1) ++
    i :: l.filter (fun x => i.1 ≤ x.1)
```

**`WickContraction.orderedInsert_eq_insertIdx_of_fin_list_sorted`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L145).

```lean
lemma orderedInsert_eq_insertIdx_of_fin_list_sorted (l : List (Fin n)) (hl : l.Pairwise (· ≤ ·))
    (i : Fin n) :
    List.orderedInsert (· ≤ ·) i l = l.insertIdx (l.filter (fun x => x.1 < i.1)).length i
```

## Uncontracted List

**`WickContraction.uncontractedList`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L170).

> Given a Wick contraction `c`, the ordered list of elements of `Fin n` which are not contracted,
> i.e. do not appear anywhere in `c.1`.

```lean
def uncontractedList : List (Fin n)
```

**`WickContraction.uncontractedList_mem_iff`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L172).

```lean
lemma uncontractedList_mem_iff (i : Fin n) :
    i ∈ c.uncontractedList ↔ i ∈ c.uncontracted
```

**`WickContraction.uncontractedList_empty`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L177).

```lean
lemma uncontractedList_empty : (empty (n := n)).uncontractedList = List.finRange n
```

**`WickContraction.nil_zero_uncontractedList`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L180).

```lean
lemma nil_zero_uncontractedList : (empty (n := 0)).uncontractedList = []
```

**`WickContraction.congr_uncontractedList`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L183).

```lean
lemma congr_uncontractedList {n m : ℕ} (h : n = m) (c : WickContraction n) :
    ((congr h) c).uncontractedList = List.map (finCongr h) c.uncontractedList
```

**`WickContraction.uncontractedList_get_mem_uncontracted`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L188).

```lean
lemma uncontractedList_get_mem_uncontracted (i : Fin c.uncontractedList.length) :
    c.uncontractedList.get i ∈ c.uncontracted
```

**`WickContraction.uncontractedList_sorted`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L192).

```lean
lemma uncontractedList_sorted : List.Pairwise (· ≤ ·) c.uncontractedList
```

**`WickContraction.uncontractedList_sorted_lt`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L198).

```lean
lemma uncontractedList_sorted_lt : List.Pairwise (· < ·) c.uncontractedList
```

**`WickContraction.uncontractedList_nodup`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L204).

```lean
lemma uncontractedList_nodup : c.uncontractedList.Nodup
```

**`WickContraction.uncontractedList_toFinset`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L208).

```lean
lemma uncontractedList_toFinset (c : WickContraction n) :
    c.uncontractedList.toFinset = c.uncontracted
```

**`WickContraction.uncontractedList_eq_sort`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L212).

```lean
lemma uncontractedList_eq_sort (c : WickContraction n) :
    c.uncontractedList = c.uncontracted.sort (· ≤ ·)
```

**`WickContraction.uncontractedList_length_eq_card`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L219).

```lean
lemma uncontractedList_length_eq_card (c : WickContraction n) :
    c.uncontractedList.length = c.uncontracted.card
```

**`WickContraction.filter_uncontractedList`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L223).

```lean
lemma filter_uncontractedList (c : WickContraction n) (p : Fin n → Prop) [DecidablePred p] :
    (c.uncontractedList.filter p) = (c.uncontracted.filter p).sort (· ≤ ·)
```

## uncontractedIndexEquiv

**`WickContraction.uncontractedIndexEquiv`**, a def, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L244).

> The equivalence between the positions of `c.uncontractedList` i.e. elements of
> `Fin (c.uncontractedList).length` and the finite set `c.uncontracted` considered as a finite type.

```lean
def uncontractedIndexEquiv (c : WickContraction n) :
    Fin (c.uncontractedList).length ≃ c.uncontracted
```

**`WickContraction.uncontractedList_getElem_uncontractedIndexEquiv_symm`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L257).

```lean
lemma uncontractedList_getElem_uncontractedIndexEquiv_symm (k : c.uncontracted) :
    c.uncontractedList[(c.uncontractedIndexEquiv.symm k).val] = k
```

**`WickContraction.uncontractedIndexEquiv_symm_eq_filter_length`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L261).

```lean
lemma uncontractedIndexEquiv_symm_eq_filter_length (k : c.uncontracted) :
    (c.uncontractedIndexEquiv.symm k).val =
    (List.filter (fun i => i < k.val) c.uncontractedList).length
```

**`WickContraction.take_uncontractedIndexEquiv_symm`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L269).

```lean
lemma take_uncontractedIndexEquiv_symm (k : c.uncontracted) :
    c.uncontractedList.take (c.uncontractedIndexEquiv.symm k).val =
    c.uncontractedList.filter (fun i => i < k.val)
```

## Uncontracted List get

**`WickContraction.uncontractedListGet`**, a def, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L288).

> Given a Wick Contraction `φsΛ` of a list `φs` of `𝓕.FieldOp`. The list
> `φsΛ.uncontractedListGet` of `𝓕.FieldOp` is defined as the list `φs` with
> all contracted positions removed, leaving the uncontracted `𝓕.FieldOp`.
>
> The notation `[φsΛ]ᵘᶜ` is used for `φsΛ.uncontractedListGet`.

```lean
def uncontractedListGet {φs : List 𝓕.FieldOp} (φsΛ : WickContraction φs.length) :
    List 𝓕.FieldOp
```

**`WickContraction.uncontractedListGet_empty`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L295).

```lean
lemma uncontractedListGet_empty {φs : List 𝓕.FieldOp} :
    (empty (n := φs.length)).uncontractedListGet = φs
```

## uncontractedFieldOpEquiv

**`WickContraction.uncontractedFieldOpEquiv`**, a def, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L308).

> The equivalence between the type `Option c.uncontracted` for `WickContraction φs.length` and
> `Option (Fin (c.uncontractedList.map φs.get).length)`, that is optional positions of
> `c.uncontractedList.map φs.get` induced by `uncontractedIndexEquiv`.

```lean
def uncontractedFieldOpEquiv (φs : List 𝓕.FieldOp) (φsΛ : WickContraction φs.length) :
    Option φsΛ.uncontracted ≃ Option (Fin [φsΛ]ᵘᶜ.length)
```

**`WickContraction.uncontractedFieldOpEquiv_none`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L314).

```lean
lemma uncontractedFieldOpEquiv_none (φs : List 𝓕.FieldOp) (φsΛ : WickContraction φs.length) :
    (uncontractedFieldOpEquiv φs φsΛ).toFun none = none
```

**`WickContraction.uncontractedFieldOpEquiv_list_sum`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L318).

```lean
lemma uncontractedFieldOpEquiv_list_sum [AddCommMonoid α] (φs : List 𝓕.FieldOp)
    (φsΛ : WickContraction φs.length) (f : Option (Fin [φsΛ]ᵘᶜ.length) → α) :
    ∑ (i : Option (Fin [φsΛ]ᵘᶜ.length)), f i =
    ∑ (i : Option φsΛ.uncontracted), f (φsΛ.uncontractedFieldOpEquiv φs i)
```

## uncontractedListEmd

**`WickContraction.uncontractedListEmd`**, a def, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L331).

> The embedding of `Fin [φsΛ]ᵘᶜ.length` into `Fin φs.length`.

```lean
def uncontractedListEmd {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length} :
    Fin [φsΛ]ᵘᶜ.length ↪ Fin φs.length
```

**`WickContraction.uncontractedListEmd_congr`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L336).

```lean
lemma uncontractedListEmd_congr {φs : List 𝓕.FieldOp} {φsΛ φsΛ' : WickContraction φs.length}
    (h : φsΛ = φsΛ') : φsΛ.uncontractedListEmd =
    (finCongr (by simp [h])).toEmbedding.trans φsΛ'.uncontractedListEmd
```

**`WickContraction.uncontractedListEmd_toFun_eq_get`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L342).

```lean
lemma uncontractedListEmd_toFun_eq_get (φs : List 𝓕.FieldOp) (φsΛ : WickContraction φs.length) :
    (uncontractedListEmd (φsΛ := φsΛ)).toFun =
    φsΛ.uncontractedList.get ∘ (finCongr (by simp [uncontractedListGet]))
```

**`WickContraction.uncontractedListEmd_strictMono`**, a lemma, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L347).

```lean
lemma uncontractedListEmd_strictMono {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    {i j : Fin [φsΛ]ᵘᶜ.length} (h : i < j) : uncontractedListEmd i < uncontractedListEmd j
```

**`WickContraction.uncontractedListEmd_mem_uncontracted`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L354).

```lean
lemma uncontractedListEmd_mem_uncontracted {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    (i : Fin [φsΛ]ᵘᶜ.length) : uncontractedListEmd i ∈ φsΛ.uncontracted
```

**`WickContraction.uncontractedListEmd_surjective_mem_uncontracted`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L358).

```lean
lemma uncontractedListEmd_surjective_mem_uncontracted {φs : List 𝓕.FieldOp}
    {φsΛ : WickContraction φs.length} (i : Fin φs.length) (hi : i ∈ φsΛ.uncontracted) :
    ∃ j, φsΛ.uncontractedListEmd j = i
```

**`WickContraction.uncontractedListEmd_finset_disjoint_left`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L372).

```lean
lemma uncontractedListEmd_finset_disjoint_left {φs : List 𝓕.FieldOp}
    {φsΛ : WickContraction φs.length} (a : Finset (Fin [φsΛ]ᵘᶜ.length))
    (b : Finset (Fin φs.length)) (hb : b ∈ φsΛ.1) : Disjoint (a.map uncontractedListEmd) b
```

**`WickContraction.uncontractedListEmd_finset_not_mem`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L383).

```lean
lemma uncontractedListEmd_finset_not_mem {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    (a : Finset (Fin [φsΛ]ᵘᶜ.length)) :
    a.map uncontractedListEmd ∉ φsΛ.1
```

**`WickContraction.getElem_uncontractedListEmd`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L393).

```lean
lemma getElem_uncontractedListEmd {φs : List 𝓕.FieldOp} {φsΛ : WickContraction φs.length}
    (k : Fin [φsΛ]ᵘᶜ.length) : φs[(uncontractedListEmd k).1] = [φsΛ]ᵘᶜ[k.1]
```

**`WickContraction.uncontractedListEmd_empty`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L399).

```lean
lemma uncontractedListEmd_empty {φs : List 𝓕.FieldOp} :
    (empty (n := φs.length)).uncontractedListEmd = (finCongr (by simp)).toEmbedding
```

## Uncontracted List for extractEquiv symm none

**`WickContraction.uncontractedList_succAboveEmb_sorted`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L410).

```lean
lemma uncontractedList_succAboveEmb_sorted (c : WickContraction n) (i : Fin n.succ) :
    ((List.map i.succAboveEmb c.uncontractedList)).Pairwise (· ≤ ·)
```

**`WickContraction.uncontractedList_succAboveEmb_nodup`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L414).

```lean
lemma uncontractedList_succAboveEmb_nodup (c : WickContraction n) (i : Fin n.succ) :
    ((List.map i.succAboveEmb c.uncontractedList)).Nodup
```

**`WickContraction.uncontractedList_succAbove_orderedInsert_nodup`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L418).

```lean
lemma uncontractedList_succAbove_orderedInsert_nodup (c : WickContraction n) (i : Fin n.succ) :
    (List.orderedInsert (· ≤ ·) i (List.map i.succAboveEmb c.uncontractedList)).Nodup
```

**`WickContraction.uncontractedList_succAbove_orderedInsert_sorted`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L424).

```lean
lemma uncontractedList_succAbove_orderedInsert_sorted (c : WickContraction n) (i : Fin n.succ) :
    (List.orderedInsert (· ≤ ·) i
      (List.map i.succAboveEmb c.uncontractedList)).Pairwise (· ≤ ·)
```

**`WickContraction.uncontractedList_succAbove_orderedInsert_toFinset`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L429).

```lean
lemma uncontractedList_succAbove_orderedInsert_toFinset (c : WickContraction n) (i : Fin n.succ) :
    (List.orderedInsert (· ≤ ·) i (List.map i.succAboveEmb c.uncontractedList)).toFinset =
    (Insert.insert i (Finset.map i.succAboveEmb c.uncontracted))
```

**`WickContraction.uncontractedList_succAbove_orderedInsert_eq_sort`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L436).

```lean
lemma uncontractedList_succAbove_orderedInsert_eq_sort (c : WickContraction n) (i : Fin n.succ) :
    (List.orderedInsert (· ≤ ·) i (List.map i.succAboveEmb c.uncontractedList)) =
    (Insert.insert i (Finset.map i.succAboveEmb c.uncontracted)).sort (· ≤ ·)
```

**`WickContraction.uncontractedList_extractEquiv_symm_none`**, a lemma, [line 444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L444).

```lean
lemma uncontractedList_extractEquiv_symm_none (c : WickContraction n) (i : Fin n.succ) :
    ((extractEquiv i).symm ⟨c, none⟩).uncontractedList =
    List.orderedInsert (· ≤ ·) i (List.map i.succAboveEmb c.uncontractedList)
```

## Uncontracted List for extractEquiv symm some

**`WickContraction.uncontractedList_succAboveEmb_eraseIdx_toFinset`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L456).

```lean
lemma uncontractedList_succAboveEmb_eraseIdx_toFinset (c : WickContraction n) (i : Fin n.succ)
    (k : ℕ) (hk : k < c.uncontractedList.length) :
    ((List.map i.succAboveEmb c.uncontractedList).eraseIdx k).toFinset =
    (c.uncontracted.map i.succAboveEmb).erase (i.succAboveEmb c.uncontractedList[k])
```

**`WickContraction.uncontractedList_succAboveEmb_eraseIdx_sorted`**, a lemma, [line 468](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L468).

```lean
lemma uncontractedList_succAboveEmb_eraseIdx_sorted (c : WickContraction n) (i : Fin n.succ)
    (k: ℕ) : ((List.map i.succAboveEmb c.uncontractedList).eraseIdx k).Pairwise (· ≤ ·)
```

**`WickContraction.uncontractedList_succAboveEmb_eraseIdx_nodup`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L473).

```lean
lemma uncontractedList_succAboveEmb_eraseIdx_nodup (c : WickContraction n) (i : Fin n.succ) (k: ℕ) :
    ((List.map i.succAboveEmb c.uncontractedList).eraseIdx k).Nodup
```

**`WickContraction.uncontractedList_succAboveEmb_eraseIdx_eq_sort`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L477).

```lean
lemma uncontractedList_succAboveEmb_eraseIdx_eq_sort (c : WickContraction n) (i : Fin n.succ)
    (k : ℕ) (hk : k < c.uncontractedList.length) :
    ((List.map i.succAboveEmb c.uncontractedList).eraseIdx k) =
    ((c.uncontracted.map i.succAboveEmb).erase
    (i.succAboveEmb c.uncontractedList[k])).sort (· ≤ ·)
```

**`WickContraction.uncontractedList_extractEquiv_symm_some`**, a lemma, [line 487](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L487).

```lean
lemma uncontractedList_extractEquiv_symm_some (c : WickContraction n) (i : Fin n.succ)
    (k : c.uncontracted) : ((extractEquiv i).symm ⟨c, some k⟩).uncontractedList =
    ((c.uncontractedList).map i.succAboveEmb).eraseIdx (c.uncontractedIndexEquiv.symm k)
```

**`WickContraction.uncontractedList_succAboveEmb_toFinset`**, a lemma, [line 500](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L500).

```lean
lemma uncontractedList_succAboveEmb_toFinset (c : WickContraction n) (i : Fin n.succ) :
    (List.map i.succAboveEmb c.uncontractedList).toFinset =
    (Finset.map i.succAboveEmb c.uncontracted)
```

## uncontractedListOrderPos

**`WickContraction.uncontractedListOrderPos`**, a def, [line 517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L517).

> Given a Wick contraction `c : WickContraction n` and a `Fin n.succ`, the number of elements
> of `c.uncontractedList` which are less than `i`.
> Suppose we want to insert into `c` at position `i`, then this is the position we would
> need to insert into `c.uncontractedList`.

```lean
def uncontractedListOrderPos (c : WickContraction n) (i : Fin n.succ) : ℕ
```

**`WickContraction.uncontractedListOrderPos_le_length`**, a lemma, [line 521](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L521).

```lean
lemma uncontractedListOrderPos_le_length (c : WickContraction n) (i : Fin n.succ) :
    c.uncontractedListOrderPos i ≤ c.uncontractedList.length
```

**`WickContraction.take_uncontractedListOrderPos_eq_filter`**, a lemma, [line 526](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L526).

```lean
lemma take_uncontractedListOrderPos_eq_filter (c : WickContraction n) (i : Fin n.succ) :
    (c.uncontractedList.take (c.uncontractedListOrderPos i)) =
    c.uncontractedList.filter (fun x => x.1 < i.1)
```

**`WickContraction.take_uncontractedListOrderPos_eq_filter_sort`**, a lemma, [line 532](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L532).

```lean
lemma take_uncontractedListOrderPos_eq_filter_sort (c : WickContraction n) (i : Fin n.succ) :
    (c.uncontractedList.take (c.uncontractedListOrderPos i)) =
    (c.uncontracted.filter (fun x => x.1 < i.1)).sort (· ≤ ·)
```

**`WickContraction.orderedInsert_succAboveEmb_uncontractedList_eq_insertIdx`**, a lemma, [line 539](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean#L539).

```lean
lemma orderedInsert_succAboveEmb_uncontractedList_eq_insertIdx (c : WickContraction n)
    (i : Fin n.succ) :
    (List.orderedInsert (· ≤ ·) i (List.map i.succAboveEmb c.uncontractedList)) =
    (List.map i.succAboveEmb c.uncontractedList).insertIdx (uncontractedListOrderPos c i) i
```

## Depends on

- [Equivalence extracting element from contraction](../part-02/wickcontraction-extractequiv.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/UncontractedList.lean)

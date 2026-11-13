---
declaration: module
origin: cited
lean: Wick.koszulSign, Wick.koszulSign_singleton, Wick.koszulSign_mul_self, Wick.koszulSign_freeMonoid_of, Wick.koszulSignInsert_erase_boson, Wick.koszulSign_erase_boson, Wick.koszulSign_insertIdx, Wick.insertIdx_eraseIdx
statement: formalized
proof: formalized
---

# Koszul sign

The module `Physlib.QFT.PerturbationTheory.Koszul.KoszulSign`, [Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean): 20 declarations, 1 with a docstring.

**`Wick.koszulSign`**, a def, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L27).

> Gives a factor of `- 1` for every fermion-fermion (`q` is `1`) crossing that occurs when sorting
> a list of based on `r`.

```lean
def koszulSign (q : 𝓕 → FieldStatistic) (le : 𝓕 → 𝓕 → Prop) [DecidableRel le] :
    List 𝓕 → ℂ
```

**`Wick.koszulSign_singleton`**, a lemma, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L33).

```lean
lemma koszulSign_singleton (q : 𝓕 → FieldStatistic) (le : 𝓕 → 𝓕 → Prop) [DecidableRel le] (φ : 𝓕) :
    koszulSign q le [φ] = 1
```

**`Wick.koszulSign_mul_self`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L37).

```lean
lemma koszulSign_mul_self (l : List 𝓕) : koszulSign q le l * koszulSign q le l = 1
```

**`Wick.koszulSign_freeMonoid_of`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L48).

```lean
lemma koszulSign_freeMonoid_of (φ : 𝓕) : koszulSign q le (FreeMonoid.of φ) = 1
```

**`Wick.koszulSignInsert_erase_boson`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L53).

```lean
lemma koszulSignInsert_erase_boson {𝓕 : Type} (q : 𝓕 → FieldStatistic)
    (le : 𝓕 → 𝓕 → Prop) [DecidableRel le] (φ : 𝓕) :
    (φs : List 𝓕) → (n : Fin φs.length) → (heq : q (φs.get n) = bosonic) →
    koszulSignInsert q le φ (φs.eraseIdx n) = koszulSignInsert q le φ φs
```

**`Wick.koszulSign_erase_boson`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L70).

```lean
lemma koszulSign_erase_boson {𝓕 : Type} (q : 𝓕 → FieldStatistic) (le : 𝓕 → 𝓕 → Prop)
    [DecidableRel le] :
    (φs : List 𝓕) → (n : Fin φs.length) → (heq : q (φs.get n) = bosonic) →
    koszulSign q le (φs.eraseIdx n) = koszulSign q le φs
```

**`Wick.koszulSign_insertIdx`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L91).

```lean
lemma koszulSign_insertIdx [Std.Total le] [IsTrans 𝓕 le] (φ : 𝓕) :
    (φs : List 𝓕) → (n : ℕ) → (hn : n ≤ φs.length) →
    koszulSign q le (List.insertIdx φs n φ) = 𝓢(q φ, ofList q (φs.take n)) * koszulSign q le φs *
      𝓢(q φ, ofList q ((List.insertionSort le (List.insertIdx φs n φ)).take
      (insertionSortEquiv le (List.insertIdx φs n φ) ⟨n, by
        rw [List.length_insertIdx]
        simp only [hn, ↓reduceIte]
        omega⟩)))
```

**`Wick.insertIdx_eraseIdx`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L197).

```lean
lemma insertIdx_eraseIdx {I : Type} : (n : ℕ) → (r : List I) → (hn : n < r.length) →
    List.insertIdx (r.eraseIdx n) n (r.get ⟨n, hn⟩) = r
```

**`Wick.koszulSign_eraseIdx`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L208).

```lean
lemma koszulSign_eraseIdx [Std.Total le] [IsTrans 𝓕 le] (φs : List 𝓕) (n : Fin φs.length) :
    koszulSign q le (φs.eraseIdx n) = koszulSign q le φs * 𝓢(q (φs.get n), ofList q (φs.take n)) *
    𝓢(q (φs.get n), ofList q (List.take (↑(insertionSortEquiv le φs n))
    (List.insertionSort le φs)))
```

**`Wick.koszulSign_eraseIdx_insertionSortMinPos`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L249).

```lean
lemma koszulSign_eraseIdx_insertionSortMinPos [Std.Total le] [IsTrans 𝓕 le] (φ : 𝓕) (φs : List 𝓕) :
    koszulSign q le ((φ :: φs).eraseIdx (insertionSortMinPos le φ φs)) = koszulSign q le (φ :: φs)
    * 𝓢(q (insertionSortMin le φ φs), ofList q ((φ :: φs).take (insertionSortMinPos le φ φs)))
```

**`Wick.koszulSign_swap_eq_rel_cons`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L263).

```lean
lemma koszulSign_swap_eq_rel_cons {ψ φ : 𝓕}
    (h1 : le φ ψ) (h2 : le ψ φ) (φs' : List 𝓕) :
    koszulSign q le (φ :: ψ :: φs') = koszulSign q le (ψ :: φ :: φs')
```

**`Wick.koszulSign_swap_eq_rel`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L271).

```lean
lemma koszulSign_swap_eq_rel {ψ φ : 𝓕} (h1 : le φ ψ) (h2 : le ψ φ) : (φs φs' : List 𝓕) →
    koszulSign q le (φs ++ φ :: ψ :: φs') = koszulSign q le (φs ++ ψ :: φ :: φs')
```

**`Wick.koszulSign_eq_rel_eq_stat_append`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L283).

```lean
lemma koszulSign_eq_rel_eq_stat_append {ψ φ : 𝓕} [IsTrans 𝓕 le]
    (h1 : le φ ψ) (h2 : le ψ φ) (hq : q ψ = q φ) : (φs : List 𝓕) →
    koszulSign q le (φ :: ψ :: φs) = koszulSign q le φs
```

**`Wick.koszulSign_eq_rel_eq_stat`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L297).

```lean
lemma koszulSign_eq_rel_eq_stat {ψ φ : 𝓕} [IsTrans 𝓕 le]
    (h1 : le φ ψ) (h2 : le ψ φ) (hq : q ψ = q φ) : (φs' φs : List 𝓕) →
    koszulSign q le (φs' ++ φ :: ψ :: φs) = koszulSign q le (φs' ++ φs)
```

**`Wick.koszulSign_of_sorted`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L313).

```lean
lemma koszulSign_of_sorted : (φs : List 𝓕)
    → (hs : List.Pairwise le φs) → koszulSign q le φs = 1
```

**`Wick.koszulSign_of_insertionSort`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L325).

```lean
lemma koszulSign_of_insertionSort [Std.Total le] [IsTrans 𝓕 le] (φs : List 𝓕) :
    koszulSign q le (List.insertionSort le φs) = 1
```

**`Wick.koszulSign_of_append_eq_insertionSort_left`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L330).

```lean
lemma koszulSign_of_append_eq_insertionSort_left [Std.Total le] [IsTrans 𝓕 le] :
    (φs φs' : List 𝓕) → koszulSign q le (φs ++ φs') =
    koszulSign q le (List.insertionSort le φs ++ φs') * koszulSign q le φs
```

**`Wick.koszulSign_of_append_eq_insertionSort`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L371).

```lean
lemma koszulSign_of_append_eq_insertionSort [Std.Total le] [IsTrans 𝓕 le] : (φs'' φs φs' : List 𝓕) →
    koszulSign q le (φs'' ++ φs ++ φs') =
    koszulSign q le (φs'' ++ List.insertionSort le φs ++ φs') * koszulSign q le φs
```

## koszulSign with permutations

**`Wick.koszulSign_perm_eq_append`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L392).

```lean
lemma koszulSign_perm_eq_append [IsTrans 𝓕 le] (φ : 𝓕) (φs φs' φs2 : List 𝓕)
    (hp : φs.Perm φs') : (h : ∀ φ' ∈ φs, le φ φ' ∧ le φ' φ) →
    koszulSign q le (φs ++ φs2) = koszulSign q le (φs' ++ φs2)
```

**`Wick.koszulSign_perm_eq`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean#L420).

```lean
lemma koszulSign_perm_eq [IsTrans 𝓕 le] (φ : 𝓕) : (φs1 φs φs' φs2 : List 𝓕) →
    (h : ∀ φ' ∈ φs, le φ φ' ∧ le φ' φ) → (hp : φs.Perm φs') →
    koszulSign q le (φs1 ++ φs ++ φs2) = koszulSign q le (φs1 ++ φs' ++ φs2)
```

## Depends on

- [Koszul sign insert](koszul-koszulsigninsert.md)

## Proof depends on

- [List lemmas (InsertionSort)](../../../mathematics/formathlib/list-insertionsort.md)

## Sources

- [Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/Koszul/KoszulSign.lean)

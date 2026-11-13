---
declaration: module
origin: cited
lean: Physlib.List.insertIdx_map, Physlib.List.eraseIdx_sorted, Physlib.List.mem_eraseIdx_nodup, Physlib.List.insertIdx_eq_take_drop, Physlib.List.insertIdx_length_fin, Physlib.List.insertIdx_getElem_fin, Physlib.List.insertIdx_eraseIdx_fin, Physlib.List.insertIdx_length_fst_append
statement: formalized
proof: formalized
---

# List lemmas

The module `Physlib.Mathematics.ForMathlib.List.InsertIdx`, [Physlib/Mathematics/ForMathlib/List/InsertIdx.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean): 14 declarations, 0 with a docstring.

**`Physlib.List.insertIdx_map`**, a lemma, [line 23](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean#L23).

```lean
lemma insertIdx_map {I J : Type} (f : I → J) : (i : ℕ) → (r : List I) → (r0 : I) →
    (List.insertIdx r i r0).map f = List.insertIdx (r.map f) i (f r0)
```

**`Physlib.List.eraseIdx_sorted`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean#L32).

```lean
lemma eraseIdx_sorted {I : Type} (le : I → I → Prop) :
    (r : List I) → (n : ℕ) →
    List.Pairwise le r → List.Pairwise le (r.eraseIdx n)
```

**`Physlib.List.mem_eraseIdx_nodup`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean#L48).

```lean
lemma mem_eraseIdx_nodup {I : Type} (i : I) :
    (l : List I) → (n : ℕ) → (hn : n < l.length) → (h : List.Nodup l) →
    i ∈ l.eraseIdx n ↔ i ∈ l ∧ i ≠ l[n]
  | [], _, _, _ => by simp
  | a1 :: as, 0, _, h => by
    simp only [List.eraseIdx_zero, List.tail_cons, List.mem_cons, List.getElem_cons_zero, ne_eq]
    by_cases hi : i = a1
    · subst hi
      simp only [List.nodup_cons] at h
      simp [h]
    · simp [hi]
  | a1 :: as, n+1, hn, h => by
    simp only [List.eraseIdx_cons_succ, List.mem_cons, List.getElem_cons_succ, ne_eq]
    simp only [List.nodup_cons] at h
    rw [mem_eraseIdx_nodup i as n (Nat.succ_lt_succ_iff.mp hn) h.2]
    simp_all only [ne_eq]
    obtain ⟨left, right⟩
```

**`Physlib.List.insertIdx_eq_take_drop`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean#L78).

```lean
lemma insertIdx_eq_take_drop {I : Type} (i : I) : (r : List I) → (n : Fin r.length.succ) →
    List.insertIdx r n i = List.take n r ++ i :: r.drop n
```

**`Physlib.List.insertIdx_length_fin`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean#L89).

```lean
lemma insertIdx_length_fin {I : Type} (i : I) :
    (r : List I) → (n : Fin r.length.succ) →
    (List.insertIdx r n i).length = r.length.succ
```

**`Physlib.List.insertIdx_getElem_fin`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean#L99).

```lean
lemma insertIdx_getElem_fin {I : Type} (i : I) :
    (r : List I) → (k : Fin r.length.succ) → (m : Fin r.length) →
    (List.insertIdx r k i)[(k.succAbove m).val] = r[m.val]
```

**`Physlib.List.insertIdx_eraseIdx_fin`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean#L117).

```lean
lemma insertIdx_eraseIdx_fin {I : Type} :
    (r : List I) → (k : Fin r.length) →
    (List.eraseIdx r k).insertIdx k r[k] = r
```

**`Physlib.List.insertIdx_length_fst_append`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean#L127).

```lean
lemma insertIdx_length_fst_append {I : Type} (φ : I) : (φs φs' : List I) →
    List.insertIdx (φs ++ φs') φs.length φ = (φs ++ φ :: φs')
```

**`Physlib.List.get_eq_insertIdx_succAbove`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean#L135).

```lean
lemma get_eq_insertIdx_succAbove {I : Type} (i : I) (r : List I) (k : Fin r.length.succ) :
    r.get = (List.insertIdx r k i).get ∘
    (finCongr (insertIdx_length_fin i r k).symm) ∘ k.succAbove
```

**`Physlib.List.take_insert_same`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean#L141).

```lean
lemma take_insert_same {I : Type} (i : I) :
    (n : ℕ) → (r : List I) →
    List.take n (List.insertIdx r n i) = List.take n r
```

**`Physlib.List.take_eraseIdx_same`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean#L150).

```lean
lemma take_eraseIdx_same {I : Type} :
    (n : ℕ) → (r : List I) →
    List.take n (List.eraseIdx r n) = List.take n r
```

**`Physlib.List.drop_eraseIdx_succ`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean#L159).

```lean
lemma drop_eraseIdx_succ {I : Type} :
    (n : ℕ) → (r : List I) → (hn : n < r.length) →
    r[n] :: List.drop n (List.eraseIdx r n) = List.drop n r
```

**`Physlib.List.take_insert_gt`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean#L171).

```lean
lemma take_insert_gt {I : Type} (i : I) :
    (n m : ℕ) → (h : n < m) → (r : List I) →
    List.take n (List.insertIdx r m i) = List.take n r
```

**`Physlib.List.take_insert_let`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean#L181).

```lean
lemma take_insert_let {I : Type} (i : I) :
    (n m : ℕ) → (h : m ≤ n) → (r : List I) → (hm : m ≤ r.length) →
    (List.take (n + 1) (List.insertIdx r m i)).Perm (i :: List.take n r)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/List/InsertIdx.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertIdx.lean)

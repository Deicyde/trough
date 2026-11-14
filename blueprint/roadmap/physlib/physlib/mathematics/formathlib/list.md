---
declaration: module
origin: cited
lean: Physlib.List.takeWhile_eraseIdx, Physlib.List.dropWile_eraseIdx, Physlib.List.insertionSort_length, Physlib.List.orderedInsertPos, Physlib.List.orderedInsertPos_lt_length, Physlib.List.orderedInsert_get_orderedInsertPos, Physlib.List.orderedInsert_eraseIdx_orderedInsertPos, Physlib.List.orderedInsertPos_cons
statement: formalized
proof: formalized
---

# List lemmas (List)

The module `Physlib.Mathematics.ForMathlib.List`, [Physlib/Mathematics/ForMathlib/List.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean): 58 declarations, 8 with a docstring.

**`Physlib.List.takeWhile_eraseIdx`**, a lemma, [line 23](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L23).

```lean
lemma takeWhile_eraseIdx {I : Type} (P : I → Prop) [DecidablePred P] :
    (l : List I) → (i : ℕ) → (hi : ∀ (i j : Fin l.length), i < j → P (l.get j) → P (l.get i)) →
    List.takeWhile P (List.eraseIdx l i) = (List.takeWhile P l).eraseIdx i
```

**`Physlib.List.dropWile_eraseIdx`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L51).

```lean
lemma dropWile_eraseIdx {I : Type} (P : I → Prop) [DecidablePred P] :
    (l : List I) → (i : ℕ) → (hi : ∀ (i j : Fin l.length), i < j → P (l.get j) → P (l.get i)) →
    List.dropWhile P (List.eraseIdx l i) =
      if (List.takeWhile P l).length ≤ i then
        (List.dropWhile P l).eraseIdx (i - (List.takeWhile P l).length)
      else (List.dropWhile P l)
```

**`Physlib.List.insertionSort_length`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L89).

```lean
lemma insertionSort_length {I : Type} (le1 : I → I → Prop) [DecidableRel le1] (l : List I) :
    (List.insertionSort le1 l).length = l.length
```

**`Physlib.List.orderedInsertPos`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L95).

> The position `r0` ends up in `r` on adding it via `List.orderedInsert _ r0 r`.

```lean
def orderedInsertPos {I : Type} (le1 : I → I → Prop) [DecidableRel le1] (r : List I) (r0 : I) :
    Fin (List.orderedInsert le1 r0 r).length
```

**`Physlib.List.orderedInsertPos_lt_length`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L103).

```lean
lemma orderedInsertPos_lt_length {I : Type} (le1 : I → I → Prop) [DecidableRel le1] (r : List I)
    (r0 : I) : orderedInsertPos le1 r r0 < (r0 :: r).length
```

**`Physlib.List.orderedInsert_get_orderedInsertPos`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L109).

```lean
lemma orderedInsert_get_orderedInsertPos {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r : List I) (r0 : I) :
    (List.orderedInsert le1 r0 r)[(orderedInsertPos le1 r r0).val] = r0
```

**`Physlib.List.orderedInsert_eraseIdx_orderedInsertPos`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L115).

```lean
lemma orderedInsert_eraseIdx_orderedInsertPos {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r : List I) (r0 : I) :
    (List.orderedInsert le1 r0 r).eraseIdx ↑(orderedInsertPos le1 r r0) = r
```

**`Physlib.List.orderedInsertPos_cons`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L123).

```lean
lemma orderedInsertPos_cons {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r : List I) (r0 r1 : I) :
    (orderedInsertPos le1 (r1 ::r) r0).val =
    if le1 r0 r1 then ⟨0, by simp⟩ else (Fin.succ (orderedInsertPos le1 r r0))
```

**`Physlib.List.orderedInsertPos_sigma`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L131).

```lean
lemma orderedInsertPos_sigma {I : Type} {f : I → Type}
    (le1 : I → I → Prop) [DecidableRel le1] (l : List (Σ i, f i))
    (k : I) (a : f k) :
    (orderedInsertPos (fun (i j : Σ i, f i) => le1 i.1 j.1) l ⟨k, a⟩).1 =
    (orderedInsertPos le1 (List.map (fun (i : Σ i, f i) => i.1) l) k).1
```

**`Physlib.List.orderedInsert_get_lt`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L146).

```lean
lemma orderedInsert_get_lt {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r : List I) (r0 : I) (i : ℕ)
    (hi : i < orderedInsertPos le1 r r0) :
    (List.orderedInsert le1 r0 r)[i] = r.get ⟨i, by
      simp only [orderedInsertPos] at hi
      have h1 : (List.takeWhile (fun b => decide ¬le1 r0 b) r).length ≤ r.length :=
        List.Sublist.length_le (List.takeWhile_sublist fun b => decide ¬le1 r0 b)
      omega⟩
```

**`Physlib.List.orderedInsertPos_take_orderedInsert`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L161).

```lean
lemma orderedInsertPos_take_orderedInsert {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r : List I) (r0 : I) :
    (List.take (orderedInsertPos le1 r r0) (List.orderedInsert le1 r0 r)) =
    List.takeWhile (fun b => decide ¬le1 r0 b) r
```

**`Physlib.List.orderedInsertPos_take_eq_orderedInsert`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L167).

```lean
lemma orderedInsertPos_take_eq_orderedInsert {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r : List I) (r0 : I) :
    List.take (orderedInsertPos le1 r r0) r =
    List.take (orderedInsertPos le1 r r0) (List.orderedInsert le1 r0 r)
```

**`Physlib.List.orderedInsertPos_drop_eq_orderedInsert`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L181).

```lean
lemma orderedInsertPos_drop_eq_orderedInsert {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r : List I) (r0 : I) :
    List.drop (orderedInsertPos le1 r r0) r =
    List.drop (orderedInsertPos le1 r r0).succ (List.orderedInsert le1 r0 r)
```

**`Physlib.List.orderedInsertPos_take`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L195).

```lean
lemma orderedInsertPos_take {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r : List I) (r0 : I) :
    List.take (orderedInsertPos le1 r r0) r = List.takeWhile (fun b => decide ¬le1 r0 b) r
```

**`Physlib.List.orderedInsertPos_drop`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L200).

```lean
lemma orderedInsertPos_drop {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r : List I) (r0 : I) :
    List.drop (orderedInsertPos le1 r r0) r = List.dropWhile (fun b => decide ¬le1 r0 b) r
```

**`Physlib.List.orderedInsertPos_succ_take_orderedInsert`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L206).

```lean
lemma orderedInsertPos_succ_take_orderedInsert {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r : List I) (r0 : I) :
    (List.take (orderedInsertPos le1 r r0).succ (List.orderedInsert le1 r0 r)) =
    List.takeWhile (fun b => decide ¬le1 r0 b) r ++ [r0]
```

**`Physlib.List.lt_orderedInsertPos_rel`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L212).

```lean
lemma lt_orderedInsertPos_rel {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r0 : I) (r : List I) (n : Fin r.length)
    (hn : n.val < (orderedInsertPos le1 r r0).val) : ¬ le1 r0 (r.get n)
```

**`Physlib.List.lt_orderedInsertPos_rel_fin`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L222).

```lean
lemma lt_orderedInsertPos_rel_fin {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r0 : I) (r : List I) (n : Fin (List.orderedInsert le1 r0 r).length)
    (hn : n < (orderedInsertPos le1 r r0)) : ¬ le1 r0 ((List.orderedInsert le1 r0 r).get n)
```

**`Physlib.List.gt_orderedInsertPos_rel`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L233).

```lean
lemma gt_orderedInsertPos_rel {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    [Std.Total le1] [IsTrans I le1] (r0 : I) (r : List I) (hs : List.Pairwise le1 r)
    (n : Fin r.length)
    (hn : ¬ n.val < (orderedInsertPos le1 r r0).val) : le1 r0 (r.get n)
```

**`Physlib.List.orderedInsert_eraseIdx_lt_orderedInsertPos`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L250).

```lean
lemma orderedInsert_eraseIdx_lt_orderedInsertPos {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r : List I) (r0 : I) (i : ℕ)
    (hi : i < orderedInsertPos le1 r r0)
    (hr : ∀ (i j : Fin r.length), i < j → ¬le1 r0 (r.get j) → ¬le1 r0 (r.get i)) :
    (List.orderedInsert le1 r0 r).eraseIdx i = List.orderedInsert le1 r0 (r.eraseIdx i)
```

**`Physlib.List.orderedInsert_eraseIdx_orderedInsertPos_le`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L268).

```lean
lemma orderedInsert_eraseIdx_orderedInsertPos_le {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r : List I) (r0 : I) (i : ℕ)
    (hi : orderedInsertPos le1 r r0 ≤ i)
    (hr : ∀ (i j : Fin r.length), i < j → ¬le1 r0 (r.get j) → ¬le1 r0 (r.get i)) :
    (List.orderedInsert le1 r0 r).eraseIdx (Nat.succ i) =
    List.orderedInsert le1 r0 (r.eraseIdx i)
```

**`Physlib.List.orderedInsertEquiv`**, a def, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L300).

> The equivalence between `Fin (r0 :: r).length` and `Fin (List.orderedInsert le1 r0 r).length`
> according to where the elements map, i.e. `0` is taken to `orderedInsertPos le1 r r0`.

```lean
def orderedInsertEquiv {I : Type} (le1 : I → I → Prop) [DecidableRel le1] (r : List I) (r0 : I) :
    Fin (r.length + 1) ≃ Fin (List.orderedInsert le1 r0 r).length
```

**`Physlib.List.orderedInsertEquiv_zero`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L310).

```lean
lemma orderedInsertEquiv_zero {I : Type} (le1 : I → I → Prop) [DecidableRel le1] (r : List I)
    (r0 : I) : orderedInsertEquiv le1 r r0 0 = orderedInsertPos le1 r r0
```

**`Physlib.List.orderedInsertEquiv_succ`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L314).

```lean
lemma orderedInsertEquiv_succ {I : Type} (le1 : I → I → Prop) [DecidableRel le1] (r : List I)
    (r0 : I) (n : ℕ) (hn : Nat.succ n < (r0 :: r).length) :
    orderedInsertEquiv le1 r r0 ⟨Nat.succ n, hn⟩ =
    Fin.cast (List.orderedInsert_length le1 r r0).symm
    ((Fin.succAbove ⟨(orderedInsertPos le1 r r0), orderedInsertPos_lt_length le1 r r0⟩)
    ⟨n, Nat.succ_lt_succ_iff.mp hn⟩)
```

**`Physlib.List.orderedInsertEquiv_fin_succ`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L333).

```lean
lemma orderedInsertEquiv_fin_succ {I : Type} (le1 : I → I → Prop) [DecidableRel le1] (r : List I)
    (r0 : I) (n : Fin r.length) :
    orderedInsertEquiv le1 r r0 n.succ = Fin.cast (List.orderedInsert_length le1 r r0).symm
    ((Fin.succAbove ⟨(orderedInsertPos le1 r r0), orderedInsertPos_lt_length le1 r r0⟩)
      ⟨n, n.isLt⟩)
```

**`Physlib.List.orderedInsertEquiv_monotone_fin_succ`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L350).

```lean
lemma orderedInsertEquiv_monotone_fin_succ {I : Type}
    (le1 : I → I → Prop) [DecidableRel le1] (r : List I)
    (r0 : I) (n m : Fin r.length)
    (hx : orderedInsertEquiv le1 r r0 n.succ < orderedInsertEquiv le1 r r0 m.succ) :
    n < m
```

**`Physlib.List.orderedInsertEquiv_congr`**, a lemma, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L359).

```lean
lemma orderedInsertEquiv_congr {α : Type} {r : α → α → Prop} [DecidableRel r] (a : α)
    (l l' : List α) (h : l = l') :
    orderedInsertEquiv r l a = (Fin.castOrderIso (by simp [h])).toEquiv.trans
    ((orderedInsertEquiv r l' a).trans (Fin.castOrderIso (by simp [h])).toEquiv)
```

**`Physlib.List.get_eq_orderedInsertEquiv`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L366).

```lean
lemma get_eq_orderedInsertEquiv {I : Type} (le1 : I → I → Prop) [DecidableRel le1] (r : List I)
    (r0 : I) :
    (r0 :: r).get = (List.orderedInsert le1 r0 r).get ∘ (orderedInsertEquiv le1 r r0)
```

**`Physlib.List.orderedInsertEquiv_get`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L402).

```lean
lemma orderedInsertEquiv_get {I : Type} (le1 : I → I → Prop) [DecidableRel le1] (r : List I)
    (r0 : I) :
    (r0 :: r).get ∘ (orderedInsertEquiv le1 r r0).symm = (List.orderedInsert le1 r0 r).get
```

**`Physlib.List.orderedInsert_eraseIdx_orderedInsertEquiv_zero`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L408).

```lean
lemma orderedInsert_eraseIdx_orderedInsertEquiv_zero
    {I : Type} (le1 : I → I → Prop) [DecidableRel le1] (r : List I) (r0 : I) :
    (List.orderedInsert le1 r0 r).eraseIdx (orderedInsertEquiv le1 r r0 ⟨0, by simp⟩) = r
```

**`Physlib.List.orderedInsert_eraseIdx_orderedInsertEquiv_succ`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L413).

```lean
lemma orderedInsert_eraseIdx_orderedInsertEquiv_succ
    {I : Type} (le1 : I → I → Prop) [DecidableRel le1] (r : List I) (r0 : I) (n : ℕ)
    (hn : Nat.succ n < (r0 :: r).length)
    (hr : ∀ (i j : Fin r.length), i < j → ¬le1 r0 (r.get j) → ¬le1 r0 (r.get i)) :
    (List.orderedInsert le1 r0 r).eraseIdx (orderedInsertEquiv le1 r r0 ⟨Nat.succ n, hn⟩) =
    (List.orderedInsert le1 r0 (r.eraseIdx n))
```

**`Physlib.List.orderedInsert_eraseIdx_orderedInsertEquiv_fin_succ`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L433).

```lean
lemma orderedInsert_eraseIdx_orderedInsertEquiv_fin_succ
    {I : Type} (le1 : I → I → Prop) [DecidableRel le1] (r : List I) (r0 : I) (n : Fin r.length)
    (hr : ∀ (i j : Fin r.length), i < j → ¬le1 r0 (r.get j) → ¬le1 r0 (r.get i)) :
    (List.orderedInsert le1 r0 r).eraseIdx (orderedInsertEquiv le1 r r0 n.succ) =
    (List.orderedInsert le1 r0 (r.eraseIdx n))
```

**`Physlib.List.orderedInsertEquiv_sigma`**, a lemma, [line 440](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L440).

```lean
lemma orderedInsertEquiv_sigma {I : Type} {f : I → Type}
    (le1 : I → I → Prop) [DecidableRel le1] (l : List (Σ i, f i))
    (i : I) (a : f i) :
    (orderedInsertEquiv (fun i j => le1 i.fst j.fst) l ⟨i, a⟩) =
    (Fin.castOrderIso (by simp)).toEquiv.trans
    ((orderedInsertEquiv le1 (List.map (fun i => i.1) l) i).trans
    (Fin.castOrderIso (by simp [List.orderedInsert_length])).toEquiv)
```

**`Physlib.List.orderedInsert_eq_insertIdx_orderedInsertPos`**, a lemma, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L464).

```lean
lemma orderedInsert_eq_insertIdx_orderedInsertPos {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    (r : List I) (r0 : I) :
    List.orderedInsert le1 r0 r = List.insertIdx r (orderedInsertPos le1 r r0).1 r0
```

**`Physlib.List.insertionSortEquiv`**, a def, [line 513](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L513).

> The equivalence between `Fin l.length ≃ Fin (List.insertionSort r l).length` induced by the
> sorting algorithm.

```lean
def insertionSortEquiv {α : Type} (r : α → α → Prop) [DecidableRel r] : (l : List α) →
    Fin l.length ≃ Fin (List.insertionSort r l).length
```

**`Physlib.List.insertionSortEquiv_get`**, a lemma, [line 519](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L519).

```lean
lemma insertionSortEquiv_get {α : Type} {r : α → α → Prop} [DecidableRel r] : (l : List α) →
    l.get ∘ (insertionSortEquiv r l).symm = (List.insertionSort r l).get
```

**`Physlib.List.insertionSortEquiv_congr`**, a lemma, [line 538](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L538).

```lean
lemma insertionSortEquiv_congr {α : Type} {r : α → α → Prop} [DecidableRel r] (l l' : List α)
    (h : l = l') : insertionSortEquiv r l = (Fin.castOrderIso (by simp [h])).toEquiv.trans
      ((insertionSortEquiv r l').trans (Fin.castOrderIso (by simp [h])).toEquiv)
```

**`Physlib.List.insertionSortEquiv_congr_apply`**, a lemma, [line 544](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L544).

```lean
lemma insertionSortEquiv_congr_apply {α : Type} {r : α → α → Prop} [DecidableRel r] (l l' : List α)
    (h : l = l') (i : Fin l.length) :
    insertionSortEquiv r l i =
    Fin.cast (by simp [h])
    ((insertionSortEquiv r l') (Fin.cast (by simp [h]) i))
```

**`Physlib.List.insertionSort_get_comp_insertionSortEquiv`**, a lemma, [line 552](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L552).

```lean
lemma insertionSort_get_comp_insertionSortEquiv {α : Type} {r : α → α → Prop} [DecidableRel r]
    (l : List α) : (List.insertionSort r l).get ∘ (insertionSortEquiv r l) = l.get
```

**`Physlib.List.insertionSort_eq_ofFn`**, a lemma, [line 557](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L557).

```lean
lemma insertionSort_eq_ofFn {α : Type} {r : α → α → Prop} [DecidableRel r] (l : List α) :
    List.insertionSort r l = List.ofFn (l.get ∘ (insertionSortEquiv r l).symm)
```

**`Physlib.List.insertionSortEquiv_order`**, a lemma, [line 561](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L561).

```lean
lemma insertionSortEquiv_order {α : Type} {r : α → α → Prop} [DecidableRel r] :
    (l : List α) → (i : Fin l.length) → (j : Fin l.length) → (hij : i < j)
    → (hij' : insertionSortEquiv r l j < insertionSortEquiv r l i) →
    ¬ r l[i] l[j]
```

**`Physlib.List.optionErase`**, a def, [line 583](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L583).

> Optional erase of an element in a list. For `none` returns the list, for `some i` returns
> the list with the `i`'th element erased.

```lean
def optionErase {I : Type} (l : List I) (i : Option (Fin l.length)) : List I
```

**`Physlib.List.eraseIdx_length'`**, a lemma, [line 588](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L588).

```lean
lemma eraseIdx_length' {I : Type} (l : List I) (i : Fin l.length) :
    (List.eraseIdx l i).length = l.length - 1
```

**`Physlib.List.eraseIdx_length`**, a lemma, [line 592](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L592).

```lean
lemma eraseIdx_length {I : Type} (l : List I) (i : Fin l.length) :
    (List.eraseIdx l i).length + 1 = l.length
```

**`Physlib.List.eraseIdx_length_succ`**, a lemma, [line 596](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L596).

```lean
lemma eraseIdx_length_succ {I : Type} (l : List I) (i : Fin l.length) :
    (List.eraseIdx l i).length.succ = l.length
```

**`Physlib.List.eraseIdx_cons_length`**, a lemma, [line 600](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L600).

```lean
lemma eraseIdx_cons_length {I : Type} (a : I) (l : List I) (i : Fin (a :: l).length) :
    (List.eraseIdx (a :: l) i).length= l.length
```

**`Physlib.List.eraseIdx_get`**, a lemma, [line 604](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L604).

```lean
lemma eraseIdx_get {I : Type} (l : List I) (i : Fin l.length) :
    (List.eraseIdx l i).get = l.get ∘ (Fin.cast (eraseIdx_length l i)) ∘
    (Fin.cast (eraseIdx_length l i).symm i).succAbove
```

**`Physlib.List.eraseIdx_insertionSort`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L623).

```lean
lemma eraseIdx_insertionSort {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    [Std.Total le1] [IsTrans I le1] :
    (n : ℕ) → (r : List I) → (hn : n < r.length) →
    (List.insertionSort le1 r).eraseIdx ↑((insertionSortEquiv le1 r) ⟨n, hn⟩)
    = List.insertionSort le1 (r.eraseIdx n)
```

**`Physlib.List.eraseIdx_insertionSort_fin`**, a lemma, [line 649](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L649).

```lean
lemma eraseIdx_insertionSort_fin {I : Type} (le1 : I → I → Prop) [DecidableRel le1]
    [Std.Total le1] [IsTrans I le1] (r : List I) (n : Fin r.length) :
    (List.insertionSort le1 r).eraseIdx ↑((Physlib.List.insertionSortEquiv le1 r) n)
    = List.insertionSort le1 (r.eraseIdx n)
```

**`Physlib.List.insertionSortMinPos`**, a def, [line 661](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L661).

> Given a list `i :: l` the left-most minimal position `a` of `i :: l` wrt `r`.
> That is the first position
> of `l` such that for every element `(i :: l)[b]` before that position
> `r ((i :: l)[b]) ((i :: l)[a])` is not true. The use of `i :: l` here
> rather then just `l` is to ensure that such a position exists. .

```lean
def insertionSortMinPos {α : Type} (r : α → α → Prop) [DecidableRel r] (i : α) (l : List α) :
    Fin (i :: l).length
```

**`Physlib.List.insertionSortMin`**, a def, [line 667](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L667).

> The element of `i :: l` at `insertionSortMinPos`.

```lean
def insertionSortMin {α : Type} (r : α → α → Prop) [DecidableRel r] (i : α) (l : List α) :
    α
```

**`Physlib.List.insertionSortMin_eq_insertionSort_head`**, a lemma, [line 670](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L670).

```lean
lemma insertionSortMin_eq_insertionSort_head {α : Type} (r : α → α → Prop) [DecidableRel r]
    (i : α) (l : List α) :
    insertionSortMin r i l = (List.insertionSort r (i :: l)).head (by
    refine List.ne_nil_of_length_pos ?_
    rw [insertionSort_length]
    exact Nat.zero_lt_succ l.length)
```

**`Physlib.List.insertionSortDropMinPos`**, a def, [line 685](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L685).

> The list remaining after dropping the element at the position determined by
> `insertionSortMinPos`.

```lean
def insertionSortDropMinPos {α : Type} (r : α → α → Prop) [DecidableRel r] (i : α) (l : List α) :
    List α
```

**`Physlib.List.insertionSort_eq_insertionSortMin_cons`**, a lemma, [line 688](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L688).

```lean
lemma insertionSort_eq_insertionSortMin_cons {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r] (i : α) (l : List α) :
    List.insertionSort r (i :: l) =
    (insertionSortMin r i l) :: List.insertionSort r (insertionSortDropMinPos r i l)
```

**`Physlib.List.optionEraseZ`**, a def, [line 705](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L705).

> Optional erase of an element in a list, with addition for `none`. For `none` adds `a` to the
> front of the list, for `some i` removes the `i`th element of the list (does not add `a`).
> E.g. `optionEraseZ [0, 1, 2] 4 none = [4, 0, 1, 2]` and
> `optionEraseZ [0, 1, 2] 4 (some 1) = [0, 2]`.

```lean
def optionEraseZ {I : Type} (l : List I) (a : I) (i : Option (Fin l.length)) : List I
```

**`Physlib.List.optionEraseZ_some_length`**, a lemma, [line 711](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L711).

```lean
lemma optionEraseZ_some_length {I : Type} (l : List I) (a : I) (i : (Fin l.length)) :
    (optionEraseZ l a (some i)).length = l.length - 1
```

**`Physlib.List.optionEraseZ_ext`**, a lemma, [line 715](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L715).

```lean
lemma optionEraseZ_ext {I : Type} {l l' : List I} {a a' : I} {i : Option (Fin l.length)}
    {i' : Option (Fin l'.length)} (hl : l = l') (ha : a = a')
    (hi : Option.map (Fin.cast (by rw [hl])) i = i') :
    optionEraseZ l a i = optionEraseZ l' a' i'
```

**`Physlib.List.mem_take_finrange`**, a lemma, [line 725](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean#L725).

```lean
lemma mem_take_finrange : (n m : ℕ) → (a : Fin n) → a ∈ List.take m (List.finRange n) ↔ a.val < m
  | 0, m, a => Fin.elim0 a
  | n+1, 0, a => by
    simp
  | n +1, m + 1, ⟨0, h⟩ => by
    simp [List.finRange_succ]
  | n +1, m + 1, ⟨i + 1, h⟩ => by
    simp only [List.finRange_succ, List.take_succ_cons, List.mem_cons, Fin.ext_iff, Fin.val_zero,
      Nat.add_eq_zero_iff, one_ne_zero, and_false, false_or, add_lt_add_iff_right]
    rw [← List.map_take, @List.mem_map]
    apply Iff.intro
    · intro h
      obtain ⟨a, ha⟩
```

## Depends on

- [Fin lemmas](fin.md)

## Sources

- [Physlib/Mathematics/ForMathlib/List.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List.lean)

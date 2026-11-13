---
declaration: module
origin: cited
lean: Physlib.List.insertionSortMin_lt_length_succ, Physlib.List.insertionSortMinPosFin, Physlib.List.insertionSortMin_lt_mem_insertionSortDropMinPos, Physlib.List.insertionSortMinPos_insertionSortEquiv, Physlib.List.insertionSortEquiv_gt_zero_of_ne_insertionSortMinPos, Physlib.List.insertionSortMin_lt_mem_insertionSortDropMinPos_of_lt, Physlib.List.insertionSort_insertionSort, Physlib.List.orderedInsert_commute
statement: formalized
proof: formalized
---

# List lemmas (InsertionSort)

The module `Physlib.Mathematics.ForMathlib.List.InsertionSort`, [Physlib/Mathematics/ForMathlib/List/InsertionSort.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean): 27 declarations, 1 with a docstring.

**`Physlib.List.insertionSortMin_lt_length_succ`**, a lemma, [line 22](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L22).

```lean
lemma insertionSortMin_lt_length_succ {α : Type} (r : α → α → Prop) [DecidableRel r]
    (i : α) (l : List α) :
    insertionSortMinPos r i l < (insertionSortDropMinPos r i l).length.succ
```

**`Physlib.List.insertionSortMinPosFin`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L29).

> Given a list `i :: l` the left-most minimal position `a` of `i :: l` wrt `r`
> as an element of `Fin (insertionSortDropMinPos r i l).length.succ`.

```lean
def insertionSortMinPosFin {α : Type} (r : α → α → Prop) [DecidableRel r] (i : α) (l : List α) :
    Fin (insertionSortDropMinPos r i l).length.succ
```

**`Physlib.List.insertionSortMin_lt_mem_insertionSortDropMinPos`**, a lemma, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L33).

```lean
lemma insertionSortMin_lt_mem_insertionSortDropMinPos {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r] (a : α) (l : List α)
    (i : Fin (insertionSortDropMinPos r a l).length) :
    r (insertionSortMin r a l) ((insertionSortDropMinPos r a l)[i])
```

**`Physlib.List.insertionSortMinPos_insertionSortEquiv`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L41).

```lean
lemma insertionSortMinPos_insertionSortEquiv {α : Type} (r : α → α → Prop) [DecidableRel r]
    (a : α) (l : List α) :
    insertionSortEquiv r (a ::l) (insertionSortMinPos r a l) =
    ⟨0, by simp [List.orderedInsert_length]⟩
```

**`Physlib.List.insertionSortEquiv_gt_zero_of_ne_insertionSortMinPos`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L48).

```lean
lemma insertionSortEquiv_gt_zero_of_ne_insertionSortMinPos {α : Type} (r : α → α → Prop)
    [DecidableRel r] (a : α) (l : List α) (k : Fin (a :: l).length)
    (hk : k ≠ insertionSortMinPos r a l) :
    ⟨0, by simp [List.orderedInsert_length]⟩ < insertionSortEquiv r (a :: l) k
```

**`Physlib.List.insertionSortMin_lt_mem_insertionSortDropMinPos_of_lt`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L59).

```lean
lemma insertionSortMin_lt_mem_insertionSortDropMinPos_of_lt {α : Type} (r : α → α → Prop)
    [DecidableRel r] (a : α) (l : List α)
    (i : Fin (insertionSortDropMinPos r a l).length)
    (h : (insertionSortMinPosFin r a l).succAbove i < insertionSortMinPosFin r a l) :
    ¬ r ((insertionSortDropMinPos r a l)[i]) (insertionSortMin r a l)
```

**`Physlib.List.insertionSort_insertionSort`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L87).

```lean
lemma insertionSort_insertionSort {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r] (l1 : List α) :
    List.insertionSort r (List.insertionSort r l1) = List.insertionSort r l1
```

**`Physlib.List.orderedInsert_commute`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L93).

```lean
lemma orderedInsert_commute {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r] (a b : α) (hr : ¬ r a b) : (l : List α) →
    List.orderedInsert r a (List.orderedInsert r b l) =
      List.orderedInsert r b (List.orderedInsert r a l)
```

**`Physlib.List.insertionSort_orderedInsert_append`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L113).

```lean
lemma insertionSort_orderedInsert_append {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r] (a : α) : (l1 l2 : List α) →
    List.insertionSort r (List.orderedInsert r a l1 ++ l2) = List.insertionSort r (a :: l1 ++ l2)
```

**`Physlib.List.insertionSort_insertionSort_append`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L127).

```lean
lemma insertionSort_insertionSort_append {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r] : (l1 l2 : List α) →
    List.insertionSort r (List.insertionSort r l1 ++ l2) = List.insertionSort r (l1 ++ l2)
```

**`Physlib.List.insertionSort_append_insertionSort_append`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L137).

```lean
lemma insertionSort_append_insertionSort_append {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r] : (l1 l2 l3 : List α) →
    List.insertionSort r (l1 ++ List.insertionSort r l2 ++ l3) =
      List.insertionSort r (l1 ++ l2 ++ l3)
```

**`Physlib.List.orderedInsert_length`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L148).

```lean
lemma orderedInsert_length {α : Type} (r : α → α → Prop) [DecidableRel r] (a : α) (l : List α) :
    (List.orderedInsert r a l).length = (a :: l).length
```

**`Physlib.List.takeWhile_orderedInsert`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L153).

```lean
lemma takeWhile_orderedInsert {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r]
    (a b : α) (hr : ¬ r a b) : (l : List α) →
    (List.takeWhile (fun c => !decide (r a c)) (List.orderedInsert r b l)).length =
    (List.takeWhile (fun c => !decide (r a c)) l).length + 1
```

**`Physlib.List.takeWhile_orderedInsert'`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L171).

```lean
lemma takeWhile_orderedInsert' {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r]
    (a b : α) (hr : ¬ r a b) : (l : List α) →
    (List.takeWhile (fun c => !decide (r b c)) (List.orderedInsert r a l)).length =
    (List.takeWhile (fun c => !decide (r b c)) l).length
```

**`Physlib.List.insertionSortEquiv_cons_succ`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L189).

```lean
lemma insertionSortEquiv_cons_succ {α : Type} (r : α → α → Prop) [DecidableRel r]
    (a : α) (l : List α) (n : ℕ) (hn : n + 1 < (a :: l).length) :
    insertionSortEquiv r (a :: l) ⟨n + 1, hn⟩ =
    Fin.cast (by simp)
      ((Fin.succAbove ⟨orderedInsertPos r (List.insertionSort r l) a,
          orderedInsertPos_lt_length r (List.insertionSort r l) a⟩)
        (insertionSortEquiv r l ⟨n, by simpa using hn⟩))
```

**`Physlib.List.insertionSortEquiv_commute`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L200).

```lean
lemma insertionSortEquiv_commute {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r] (a b : α) (hr : ¬ r a b) (n : ℕ) : (l : List α) →
    (hn : n + 2 < (a :: b :: l).length) →
    insertionSortEquiv r (a :: b :: l) ⟨n + 2, hn⟩ = (finCongr (by simp))
    (insertionSortEquiv r (b :: a :: l) ⟨n + 2, hn⟩)
```

**`Physlib.List.insertionSortEquiv_orderedInsert_append`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L259).

```lean
lemma insertionSortEquiv_orderedInsert_append {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r] (a a2 : α) : (l1 l2 : List α) →
    (insertionSortEquiv r (List.orderedInsert r a l1 ++ a2 :: l2) ⟨l1.length + 1, by
      simp⟩)
    = (finCongr (by
      simp only [List.cons_append, List.insertionSort_cons, orderedInsert_length, List.length_cons,
        List.length_insertionSort, List.length_append]
      omega))
      ((insertionSortEquiv r (a :: l1 ++ a2 :: l2)) ⟨l1.length + 1, by simp⟩)
```

**`Physlib.List.insertionSortEquiv_insertionSort_append`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L309).

```lean
lemma insertionSortEquiv_insertionSort_append {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r] (a : α) : (l1 l2 : List α) →
    (insertionSortEquiv r (List.insertionSort r l1 ++ a :: l2) ⟨l1.length, by simp⟩)
    = finCongr (by simp) (insertionSortEquiv r (l1 ++ a :: l2) ⟨l1.length, by simp⟩)
```

## Insertion sort with equal fields

**`Physlib.List.orderedInsert_filter_of_pos`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L343).

```lean
lemma orderedInsert_filter_of_pos {α : Type} (r : α → α → Prop) [DecidableRel r]
    [IsTrans α r] (a : α) (p : α → Prop) [DecidablePred p] (h : p a) : (l : List α) →
    (hl : l.Pairwise r) →
    List.filter p (List.orderedInsert r a l) = List.orderedInsert r a (List.filter p l)
```

**`Physlib.List.orderedInsert_filter_of_neg`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L390).

```lean
lemma orderedInsert_filter_of_neg {α : Type} (r : α → α → Prop) [DecidableRel r]
    (a : α) (p : α → Prop) [DecidablePred p] (h : ¬ p a) (l : List α) :
    List.filter p (List.orderedInsert r a l) = (List.filter p l)
```

**`Physlib.List.insertionSort_filter`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L397).

```lean
lemma insertionSort_filter {α : Type} (r : α → α → Prop) [DecidableRel r] [Std.Total r]
    [IsTrans α r] (p : α → Prop) [DecidablePred p] : (l : List α) →
    List.insertionSort r (List.filter p l) =
    List.filter p (List.insertionSort r l)
```

**`Physlib.List.takeWhile_sorted_eq_filter`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L412).

```lean
lemma takeWhile_sorted_eq_filter {α : Type} (r : α → α → Prop) [DecidableRel r]
    [IsTrans α r] (a : α) : (l : List α) → (hl : l.Pairwise r) →
    List.takeWhile (fun c => ¬ r a c) l = List.filter (fun c => ¬ r a c) l
```

**`Physlib.List.dropWhile_sorted_eq_filter`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L427).

```lean
lemma dropWhile_sorted_eq_filter {α : Type} (r : α → α → Prop) [DecidableRel r]
    [IsTrans α r] (a : α) : (l : List α) → (hl : l.Pairwise r) →
    List.dropWhile (fun c => ¬ r a c) l = List.filter (fun c => r a c) l
```

**`Physlib.List.dropWhile_sorted_eq_filter_filter`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L445).

```lean
lemma dropWhile_sorted_eq_filter_filter {α : Type} (r : α → α → Prop) [DecidableRel r]
    [IsTrans α r] (a : α) :(l : List α) → (hl : l.Pairwise r) →
    List.filter (fun c => r a c) l =
    List.filter (fun c => r a c ∧ r c a) l ++ List.filter (fun c => r a c ∧ ¬ r c a) l
```

**`Physlib.List.filter_rel_eq_insertionSort`**, a lemma, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L481).

```lean
lemma filter_rel_eq_insertionSort {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r] (a : α) : (l : List α) →
    List.filter (fun c => r a c ∧ r c a) (l.insertionSort r) =
    List.filter (fun c => r a c ∧ r c a) l
```

**`Physlib.List.insertionSort_of_eq_list`**, a lemma, [line 535](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L535).

```lean
lemma insertionSort_of_eq_list {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r] (a : α) (l1 l l2 : List α)
    (h : ∀ b ∈ l, r a b ∧ r b a) :
    List.insertionSort r (l1 ++ l ++ l2) =
    (List.takeWhile (fun c => ¬ r a c) ((l1 ++ l2).insertionSort r))
    ++ (List.filter (fun c => r a c ∧ r c a) l1)
    ++ l
    ++ (List.filter (fun c => r a c ∧ r c a) l2)
    ++ (List.filter (fun c => r a c ∧ ¬ r c a) ((l1 ++ l2).insertionSort r))
```

**`Physlib.List.insertionSort_of_takeWhile_filter`**, a lemma, [line 585](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean#L585).

```lean
lemma insertionSort_of_takeWhile_filter {α : Type} (r : α → α → Prop) [DecidableRel r]
    [Std.Total r] [IsTrans α r] (a : α) (l1 l2 : List α) :
    List.insertionSort r (l1 ++ l2) =
    (List.takeWhile (fun c => ¬ r a c) ((l1 ++ l2).insertionSort r))
    ++ (List.filter (fun c => r a c ∧ r c a) l1)
    ++ (List.filter (fun c => r a c ∧ r c a) l2)
    ++ (List.filter (fun c => r a c ∧ ¬ r c a) ((l1 ++ l2).insertionSort r))
```

## Depends on

- [List lemmas (List)](list.md)

## Sources

- [Physlib/Mathematics/ForMathlib/List/InsertionSort.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/List/InsertionSort.lean)

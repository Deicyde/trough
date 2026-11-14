---
catalog: module
lean: Cslib.ωSequence.eta, Cslib.ωSequence.cons_head_tail, Cslib.ωSequence.ext, Cslib.ωSequence.get_fun, Cslib.ωSequence.get_zero_cons, Cslib.ωSequence.head_cons, Cslib.ωSequence.tail_cons, Cslib.ωSequence.get_drop, Cslib.ωSequence.tail_eq_drop, Cslib.ωSequence.drop_drop, Cslib.ωSequence.get_tail, Cslib.ωSequence.tail_drop', Cslib.ωSequence.drop_tail', Cslib.ωSequence.tail_drop, Cslib.ωSequence.get_succ, Cslib.ωSequence.get_succ_cons, Cslib.ωSequence.get_cons_append_zero, Cslib.ωSequence.append_get_zero_of_ne_nil, Cslib.ωSequence.append_eq_cons, Cslib.ωSequence.drop_zero, Cslib.ωSequence.drop_succ, Cslib.ωSequence.head_drop, Cslib.ωSequence.cons_injective2, Cslib.ωSequence.cons_injective_left, Cslib.ωSequence.cons_injective_right, Cslib.ωSequence.drop_map, Cslib.ωSequence.get_map, Cslib.ωSequence.tail_map, Cslib.ωSequence.head_map, Cslib.ωSequence.map_eq, Cslib.ωSequence.map_cons, Cslib.ωSequence.map_id, Cslib.ωSequence.map_map, Cslib.ωSequence.map_tail, Cslib.ωSequence.drop_zip, Cslib.ωSequence.get_zip, Cslib.ωSequence.head_zip, Cslib.ωSequence.tail_zip, Cslib.ωSequence.zip_eq, Cslib.ωSequence.const_eq, Cslib.ωSequence.tail_const, Cslib.ωSequence.map_const, Cslib.ωSequence.get_const, Cslib.ωSequence.drop_const, Cslib.ωSequence.head_iterate, Cslib.ωSequence.get_iterate, Cslib.ωSequence.get_succ_iterate', Cslib.ωSequence.tail_iterate, Cslib.ωSequence.iterate_eq, Cslib.ωSequence.get_zero_iterate, Cslib.ωSequence.get_succ_iterate, Cslib.ωSequence.iterate_id, Cslib.ωSequence.map_iterate, Cslib.ωSequence.nil_append_ωSequence, Cslib.ωSequence.cons_append_ωSequence, Cslib.ωSequence.singleton_append_ωSequence, Cslib.ωSequence.append_append_ωSequence, Cslib.ωSequence.get_append_left, Cslib.ωSequence.get_append_right, Cslib.ωSequence.get_append_right', Cslib.ωSequence.get_append_length, Cslib.ωSequence.append_right_injective, Cslib.ωSequence.append_right_inj, Cslib.ωSequence.append_left_injective, Cslib.ωSequence.append_left_right_injective, Cslib.ωSequence.map_append_ωSequence, Cslib.ωSequence.drop_append_ωSequence, Cslib.ωSequence.append_ωSequence_head_tail, Cslib.ωSequence.take_zero, Cslib.ωSequence.take_succ, Cslib.ωSequence.take_succ_cons, Cslib.ωSequence.take_succ', Cslib.ωSequence.take_one, Cslib.ωSequence.length_take, Cslib.ωSequence.take_take, Cslib.ωSequence.concat_take_get, Cslib.ωSequence.getElem?_take, Cslib.ωSequence.getElem?_take_succ, Cslib.ωSequence.dropLast_take, Cslib.ωSequence.append_take_drop, Cslib.ωSequence.append_take, Cslib.ωSequence.take_get, Cslib.ωSequence.take_append_of_le_length, Cslib.ωSequence.take_add, Cslib.ωSequence.take_prefix_take_left, Cslib.ωSequence.take_prefix, Cslib.ωSequence.map_take, Cslib.ωSequence.take_drop, Cslib.ωSequence.drop_append_of_le_length, Cslib.ωSequence.drop_append_of_ge_length, Cslib.ωSequence.take_theorem, Cslib.ωSequence.extract_eq_drop_take, Cslib.ωSequence.extract_eq_ofFn, Cslib.ωSequence.extract_eq_extract, Cslib.ωSequence.extract_eq_take, Cslib.ωSequence.append_extract_drop, Cslib.ωSequence.extract_append_right_right, Cslib.ωSequence.extract_append_zero_right, Cslib.ωSequence.extract_drop, Cslib.ωSequence.length_extract, Cslib.ωSequence.extract_eq_nil, Cslib.ωSequence.extract_eq_nil_iff, Cslib.ωSequence.get_extract, Cslib.ωSequence.append_extract_extract, Cslib.ωSequence.extract_succ_right, Cslib.ωSequence.extract_lu_extract_lu, Cslib.ωSequence.extract_0u_extract_lu, Cslib.ωSequence.extract_0u_extract_l, Cslib.ωSequence.take_extract, Cslib.ωSequence.drop_extract
statement: formalized
proof: formalized
---

# ω-sequences a.k.a. infinite sequences

`Cslib.Foundations.Data.OmegaSequence.Init`, in [Cslib/Foundations/Data/OmegaSequence/Init.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean), by Ching-Tsun Chou, Fabrizio Montesi.

> Most code below is adapted from Mathlib.Data.Stream.Init.

`Cslib.ωSequence.eta` (theorem, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L39))

```lean
protected theorem eta (s : ωSequence α) : head s ::ω tail s = s
```

`Cslib.ωSequence.cons_head_tail` (alias, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L44))

> Alias for `ωSequence.eta` to match `List` API.

```lean
alias cons_head_tail
```

`Cslib.ωSequence.ext` (theorem, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L47))

```lean
protected theorem ext {s₁ s₂ : ωSequence α} : (∀ n, s₁ n = s₂ n) → s₁ = s₂
```

`Cslib.ωSequence.get_fun` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L51))

```lean
theorem get_fun (f : ℕ → α) (n : ℕ) : ωSequence.mk f n = f n
```

`Cslib.ωSequence.get_zero_cons` (theorem, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L55))

```lean
theorem get_zero_cons (a : α) (s : ωSequence α) : (a ::ω s) 0 = a
```

`Cslib.ωSequence.head_cons` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L59))

```lean
theorem head_cons (a : α) (s : ωSequence α) : head (a ::ω s) = a
```

`Cslib.ωSequence.tail_cons` (theorem, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L63))

```lean
theorem tail_cons (a : α) (s : ωSequence α) : tail (a ::ω s) = s
```

`Cslib.ωSequence.get_drop` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L67))

```lean
theorem get_drop (n m : ℕ) (s : ωSequence α) : (drop m s) n = s (m + n)
```

`Cslib.ωSequence.tail_eq_drop` (theorem, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L71))

```lean
theorem tail_eq_drop (s : ωSequence α) : tail s = drop 1 s
```

`Cslib.ωSequence.drop_drop` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L75))

```lean
theorem drop_drop (n m : ℕ) (s : ωSequence α) : drop n (drop m s) = drop (m + n) s
```

`Cslib.ωSequence.get_tail` (theorem, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L79))

```lean
theorem get_tail {n : ℕ} {s : ωSequence α} : s.tail n = s (n + 1)
```

`Cslib.ωSequence.tail_drop'` (theorem, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L82))

```lean
theorem tail_drop' {i : ℕ} {s : ωSequence α} : tail (drop i s) = s.drop (i + 1)
```

`Cslib.ωSequence.drop_tail'` (theorem, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L86))

```lean
theorem drop_tail' {i : ℕ} {s : ωSequence α} : drop i (tail s) = s.drop (i + 1)
```

`Cslib.ωSequence.tail_drop` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L88))

```lean
theorem tail_drop (n : ℕ) (s : ωSequence α) : tail (drop n s) = drop n (tail s)
```

`Cslib.ωSequence.get_succ` (theorem, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L90))

```lean
theorem get_succ (n : ℕ) (s : ωSequence α) : s (succ n) = (tail s) n
```

`Cslib.ωSequence.get_succ_cons` (theorem, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L94))

```lean
theorem get_succ_cons (n : ℕ) (s : ωSequence α) (x : α) : (x ::ω s) n.succ = s n
```

`Cslib.ωSequence.get_cons_append_zero` (lemma, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L98))

```lean
lemma get_cons_append_zero {a : α} {x : List α} {s : ωSequence α} :
    (a :: x ++ω s) 0 = a
```

`Cslib.ωSequence.append_get_zero_of_ne_nil` (lemma, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L101))

```lean
lemma append_get_zero_of_ne_nil {x : List α} {s : ωSequence α} (h : x ≠ []) :
    (x ++ω s) 0 = x.head h
```

`Cslib.ωSequence.append_eq_cons` (lemma, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L107))

```lean
lemma append_eq_cons {a : α} {as : ωSequence α} : [a] ++ω as = a ::ω as
```

`Cslib.ωSequence.drop_zero` (theorem, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L109))

```lean
theorem drop_zero {s : ωSequence α} : s.drop 0 = s
```

`Cslib.ωSequence.drop_succ` (theorem, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L111))

```lean
theorem drop_succ (n : ℕ) (s : ωSequence α) : drop (succ n) s = drop n (tail s)
```

`Cslib.ωSequence.head_drop` (theorem, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L114))

```lean
theorem head_drop (a : ωSequence α) (n : ℕ) : (a.drop n).head = a n
```

`Cslib.ωSequence.cons_injective2` (theorem, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L116))

```lean
theorem cons_injective2 : Function.Injective2 (cons : α → ωSequence α → ωSequence α)
```

`Cslib.ωSequence.cons_injective_left` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L121))

```lean
theorem cons_injective_left (s : ωSequence α) : Function.Injective fun x => cons x s
```

`Cslib.ωSequence.cons_injective_right` (theorem, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L124))

```lean
theorem cons_injective_right (x : α) : Function.Injective (cons x)
```

`Cslib.ωSequence.drop_map` (theorem, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L131))

```lean
theorem drop_map (n : ℕ) (s : ωSequence α) : drop n (map f s) = map f (drop n s)
```

`Cslib.ωSequence.get_map` (theorem, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L135))

```lean
theorem get_map (n : ℕ) (s : ωSequence α) : (map f s) n = f (s n)
```

`Cslib.ωSequence.tail_map` (theorem, [line 138](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L138))

```lean
theorem tail_map (s : ωSequence α) : tail (map f s) = map f (tail s)
```

`Cslib.ωSequence.head_map` (theorem, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L141))

```lean
theorem head_map (s : ωSequence α) : head (map f s) = f (head s)
```

`Cslib.ωSequence.map_eq` (theorem, [line 144](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L144))

```lean
theorem map_eq (s : ωSequence α) : map f s = f (head s) ::ω map f (tail s)
```

`Cslib.ωSequence.map_cons` (theorem, [line 147](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L147))

```lean
theorem map_cons (a : α) (s : ωSequence α) : map f (a ::ω s) = f a ::ω map f s
```

`Cslib.ωSequence.map_id` (theorem, [line 151](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L151))

```lean
theorem map_id (s : ωSequence α) : map id s = s
```

`Cslib.ωSequence.map_map` (theorem, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L155))

```lean
theorem map_map (g : β → δ) (f : α → β) (s : ωSequence α) : map g (map f s) = map (g ∘ f) s
```

`Cslib.ωSequence.map_tail` (theorem, [line 159](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L159))

```lean
theorem map_tail (s : ωSequence α) : map f (tail s) = tail (map f s)
```

`Cslib.ωSequence.drop_zip` (theorem, [line 168](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L168))

```lean
theorem drop_zip (n : ℕ) (s₁ : ωSequence α) (s₂ : ωSequence β) :
    drop n (zip f s₁ s₂) = zip f (drop n s₁) (drop n s₂)
```

`Cslib.ωSequence.get_zip` (theorem, [line 173](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L173))

```lean
theorem get_zip (n : ℕ) (s₁ : ωSequence α) (s₂ : ωSequence β) :
    (zip f s₁ s₂) n = f (s₁ n) (s₂ n)
```

`Cslib.ωSequence.head_zip` (theorem, [line 177](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L177))

```lean
theorem head_zip (s₁ : ωSequence α) (s₂ : ωSequence β) :
    head (zip f s₁ s₂) = f (head s₁) (head s₂)
```

`Cslib.ωSequence.tail_zip` (theorem, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L181))

```lean
theorem tail_zip (s₁ : ωSequence α) (s₂ : ωSequence β) :
    tail (zip f s₁ s₂) = zip f (tail s₁) (tail s₂)
```

`Cslib.ωSequence.zip_eq` (theorem, [line 185](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L185))

```lean
theorem zip_eq (s₁ : ωSequence α) (s₂ : ωSequence β) :
    zip f s₁ s₂ = f (head s₁) (head s₂) ::ω zip f (tail s₁) (tail s₂)
```

`Cslib.ωSequence.const_eq` (theorem, [line 191](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L191))

```lean
theorem const_eq (a : α) : const a = a ::ω const a
```

`Cslib.ωSequence.tail_const` (theorem, [line 196](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L196))

```lean
theorem tail_const (a : α) : tail (const a) = const a
```

`Cslib.ωSequence.map_const` (theorem, [line 201](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L201))

```lean
theorem map_const (f : α → β) (a : α) : map f (const a) = const (f a)
```

`Cslib.ωSequence.get_const` (theorem, [line 205](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L205))

```lean
theorem get_const (n : ℕ) (a : α) : (const a) n = a
```

`Cslib.ωSequence.drop_const` (theorem, [line 209](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L209))

```lean
theorem drop_const (n : ℕ) (a : α) : drop n (const a) = const a
```

`Cslib.ωSequence.head_iterate` (theorem, [line 213](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L213))

```lean
theorem head_iterate (f : α → α) (a : α) : head (iterate f a) = a
```

`Cslib.ωSequence.get_iterate` (theorem, [line 216](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L216))

```lean
theorem get_iterate (f : α → α) (a : α) (n : ℕ) :
    iterate f a n = f^[n] a
```

`Cslib.ωSequence.get_succ_iterate'` (theorem, [line 220](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L220))

```lean
theorem get_succ_iterate' (n : ℕ) (f : α → α) (a : α) :
    iterate f a (succ n) = f (iterate f a n)
```

`Cslib.ωSequence.tail_iterate` (theorem, [line 225](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L225))

```lean
theorem tail_iterate (f : α → α) (a : α) : tail (iterate f a) = iterate f (f a)
```

`Cslib.ωSequence.iterate_eq` (theorem, [line 232](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L232))

```lean
theorem iterate_eq (f : α → α) (a : α) : iterate f a = a ::ω iterate f (f a)
```

`Cslib.ωSequence.get_zero_iterate` (theorem, [line 237](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L237))

```lean
theorem get_zero_iterate (f : α → α) (a : α) : (iterate f a) 0 = a
```

`Cslib.ωSequence.get_succ_iterate` (theorem, [line 240](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L240))

```lean
theorem get_succ_iterate (n : ℕ) (f : α → α) (a : α) :
    iterate f a (succ n) = iterate f (f a) n
```

`Cslib.ωSequence.iterate_id` (theorem, [line 245](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L245))

```lean
theorem iterate_id (a : α) : iterate id a = const a
```

`Cslib.ωSequence.map_iterate` (theorem, [line 248](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L248))

```lean
theorem map_iterate (f : α → α) (a : α) : iterate f (f a) = map f (iterate f a)
```

`Cslib.ωSequence.nil_append_ωSequence` (theorem, [line 252](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L252))

```lean
theorem nil_append_ωSequence (s : ωSequence α) : appendωSequence [] s = s
```

`Cslib.ωSequence.cons_append_ωSequence` (theorem, [line 255](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L255))

```lean
theorem cons_append_ωSequence (a : α) (l : List α) (s : ωSequence α) :
    appendωSequence (a :: l) s = a ::ω appendωSequence l s
```

`Cslib.ωSequence.singleton_append_ωSequence` (theorem, [line 259](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L259))

```lean
theorem singleton_append_ωSequence (a : α) (s : ωSequence α) :
  [a] ++ω s = a ::ω s
```

`Cslib.ωSequence.append_append_ωSequence` (theorem, [line 263](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L263))

```lean
theorem append_append_ωSequence : ∀ (l₁ l₂ : List α) (s : ωSequence α),
    l₁ ++ l₂ ++ω s = l₁ ++ω (l₂ ++ω s)
```

`Cslib.ωSequence.get_append_left` (lemma, [line 269](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L269))

```lean
lemma get_append_left (h : n < x.length) : (x ++ω a) n = x[n]
```

`Cslib.ωSequence.get_append_right` (lemma, [line 278](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L278))

```lean
lemma get_append_right : (x ++ω a) (x.length + n) = a n
```

`Cslib.ωSequence.get_append_right'` (theorem, [line 281](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L281))

```lean
theorem get_append_right' {xl : List α} {xs : ωSequence α} {k : ℕ} (h : xl.length ≤ k) :
    (xl ++ω xs) k = xs (k - xl.length)
```

`Cslib.ωSequence.get_append_length` (lemma, [line 287](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L287))

```lean
lemma get_append_length : (x ++ω a) x.length = a 0
```

`Cslib.ωSequence.append_right_injective` (lemma, [line 289](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L289))

```lean
lemma append_right_injective (h : x ++ω a = x ++ω b) : a = b
```

`Cslib.ωSequence.append_right_inj` (lemma, [line 293](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L293))

```lean
lemma append_right_inj : x ++ω a = x ++ω b ↔ a = b
```

`Cslib.ωSequence.append_left_injective` (lemma, [line 296](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L296))

```lean
lemma append_left_injective (h : x ++ω a = y ++ω b) (hl : x.length = y.length) : x = y
```

`Cslib.ωSequence.append_left_right_injective` (theorem, [line 301](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L301))

```lean
theorem append_left_right_injective (l1 l2 : List α) (s1 s2 : ωSequence α)
    (h1 : l1 ++ω s1 = l2 ++ω s2) (h2 : l1.length = l2.length) : l1 = l2 ∧ s1 = s2
```

`Cslib.ωSequence.map_append_ωSequence` (theorem, [line 306](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L306))

```lean
theorem map_append_ωSequence (f : α → β) :
    ∀ (l : List α) (s : ωSequence α), map f (l ++ω s) = List.map f l ++ω map f s
```

`Cslib.ωSequence.drop_append_ωSequence` (theorem, [line 313](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L313))

```lean
theorem drop_append_ωSequence : ∀ (l : List α) (s : ωSequence α), drop l.length (l ++ω s) = s
```

`Cslib.ωSequence.append_ωSequence_head_tail` (theorem, [line 318](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L318))

```lean
theorem append_ωSequence_head_tail (s : ωSequence α) : [head s] ++ω tail s = s
```

`Cslib.ωSequence.take_zero` (theorem, [line 322](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L322))

```lean
theorem take_zero (s : ωSequence α) : take 0 s = []
```

`Cslib.ωSequence.take_succ` (theorem, [line 328](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L328))

```lean
theorem take_succ (n : ℕ) (s : ωSequence α) : take (succ n) s = head s :: take n (tail s)
```

`Cslib.ωSequence.take_succ_cons` (theorem, [line 332](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L332))

```lean
theorem take_succ_cons {a : α} (n : ℕ) (s : ωSequence α) :
    take (n+1) (a ::ω s) = a :: take n s
```

`Cslib.ωSequence.take_succ'` (theorem, [line 335](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L335))

```lean
theorem take_succ' {s : ωSequence α} : ∀ n, s.take (n+1) = s.take n ++ [s n]
```

`Cslib.ωSequence.take_one` (theorem, [line 340](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L340))

```lean
theorem take_one {xs : ωSequence α} :
    xs.take 1 = [xs 0]
```

`Cslib.ωSequence.length_take` (theorem, [line 345](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L345))

```lean
theorem length_take (n : ℕ) (s : ωSequence α) : (take n s).length = n
```

`Cslib.ωSequence.take_take` (theorem, [line 349](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L349))

```lean
theorem take_take {s : ωSequence α} : ∀ {m n}, (s.take n).take m = s.take (min n m)
```

`Cslib.ωSequence.concat_take_get` (theorem, [line 355](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L355))

```lean
theorem concat_take_get {n : ℕ} {s : ωSequence α} : s.take n ++ [s n] = s.take (n + 1)
```

`Cslib.ωSequence.getElem?_take` (theorem, [line 358](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L358))

```lean
theorem getElem?_take {s : ωSequence α} : ∀ {k n}, k < n → (s.take n)[k]? = s k
```

`Cslib.ωSequence.getElem?_take_succ` (theorem, [line 363](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L363))

```lean
theorem getElem?_take_succ (n : ℕ) (s : ωSequence α) :
    (take (succ n) s)[n]? = some (s n)
```

`Cslib.ωSequence.dropLast_take` (theorem, [line 368](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L368))

```lean
theorem dropLast_take {n : ℕ} {xs : ωSequence α} :
    (ωSequence.take n xs).dropLast = ωSequence.take (n-1) xs
```

`Cslib.ωSequence.append_take_drop` (theorem, [line 375](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L375))

```lean
theorem append_take_drop (n : ℕ) (s : ωSequence α) : appendωSequence (take n s) (drop n s) = s
```

`Cslib.ωSequence.append_take` (lemma, [line 380](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L380))

```lean
lemma append_take : x ++ (a.take n) = (x ++ω a).take (x.length + n)
```

`Cslib.ωSequence.take_get` (lemma, [line 384](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L384))

```lean
lemma take_get (h : m < (a.take n).length) : (a.take n)[m] = a m
```

`Cslib.ωSequence.take_append_of_le_length` (theorem, [line 387](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L387))

```lean
theorem take_append_of_le_length (h : n ≤ x.length) :
    (x ++ω a).take n = x.take n
```

`Cslib.ωSequence.take_add` (lemma, [line 392](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L392))

```lean
lemma take_add : a.take (m + n) = a.take m ++ (a.drop m).take n
```

`Cslib.ωSequence.take_prefix_take_left` (lemma, [line 396](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L396))

```lean
lemma take_prefix_take_left (h : m ≤ n) : a.take m <+: a.take n
```

`Cslib.ωSequence.take_prefix` (lemma, [line 401](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L401))

```lean
lemma take_prefix : a.take m <+: a.take n ↔ m ≤ n
```

`Cslib.ωSequence.map_take` (lemma, [line 404](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L404))

```lean
lemma map_take (f : α → β) : (a.take n).map f = (a.map f).take n
```

`Cslib.ωSequence.take_drop` (lemma, [line 407](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L407))

```lean
lemma take_drop : (a.drop m).take n = (a.take (m + n)).drop m
```

`Cslib.ωSequence.drop_append_of_le_length` (lemma, [line 410](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L410))

```lean
lemma drop_append_of_le_length (h : n ≤ x.length) :
    (x ++ω a).drop n = x.drop n ++ω a
```

`Cslib.ωSequence.drop_append_of_ge_length` (theorem, [line 419](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L419))

```lean
theorem drop_append_of_ge_length {xl : List α} {xs : ωSequence α} {n : ℕ} (h : xl.length ≤ n) :
    (xl ++ω xs).drop n = xs.drop (n - xl.length)
```

`Cslib.ωSequence.take_theorem` (theorem, [line 426](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L426))

```lean
theorem take_theorem (s₁ s₂ : ωSequence α) (h : ∀ n : ℕ, take n s₁ = take n s₂) : s₁ = s₂
```

`Cslib.ωSequence.extract_eq_drop_take` (theorem, [line 435](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L435))

```lean
theorem extract_eq_drop_take {xs : ωSequence α} {m n : ℕ} :
    xs.extract m n = take (n - m) (xs.drop m)
```

`Cslib.ωSequence.extract_eq_ofFn` (theorem, [line 439](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L439))

```lean
theorem extract_eq_ofFn {xs : ωSequence α} {m n : ℕ} :
    xs.extract m n = List.ofFn (fun k : Fin (n - m) ↦ xs (m + k))
```

`Cslib.ωSequence.extract_eq_extract` (theorem, [line 444](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L444))

```lean
theorem extract_eq_extract {xs xs' : ωSequence α} {m n m' n' : ℕ}
    (h : xs.extract m n = xs'.extract m' n') :
    n - m = n' - m' ∧ ∀ k < n - m, xs (m + k) = xs' (m' + k)
```

`Cslib.ωSequence.extract_eq_take` (theorem, [line 452](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L452))

```lean
theorem extract_eq_take {xs : ωSequence α} {n : ℕ} :
    xs.extract 0 n = xs.take n
```

`Cslib.ωSequence.append_extract_drop` (theorem, [line 457](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L457))

```lean
theorem append_extract_drop {xs : ωSequence α} {n : ℕ} :
    (xs.extract 0 n) ++ω (xs.drop n) = xs
```

`Cslib.ωSequence.extract_append_right_right` (theorem, [line 461](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L461))

```lean
theorem extract_append_right_right {xl : List α} {xs : ωSequence α} {m n : ℕ} (h : xl.length ≤ m) :
    (xl ++ω xs).extract m n = xs.extract (m - xl.length) (n - xl.length)
```

`Cslib.ωSequence.extract_append_zero_right` (theorem, [line 465](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L465))

```lean
theorem extract_append_zero_right {xl : List α} {xs : ωSequence α} {n : ℕ} (h : xl.length ≤ n) :
    (xl ++ω xs).extract 0 n = xl ++ (xs.extract 0 (n - xl.length))
```

`Cslib.ωSequence.extract_drop` (theorem, [line 470](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L470))

```lean
theorem extract_drop {xs : ωSequence α} {k m n : ℕ} :
    (xs.drop k).extract m n = xs.extract (k + m) (k + n)
```

`Cslib.ωSequence.length_extract` (theorem, [line 475](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L475))

```lean
theorem length_extract {xs : ωSequence α} {m n : ℕ} :
    (xs.extract m n).length = n - m
```

`Cslib.ωSequence.extract_eq_nil` (theorem, [line 480](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L480))

```lean
theorem extract_eq_nil {xs : ωSequence α} {n : ℕ} :
    xs.extract n n = []
```

`Cslib.ωSequence.extract_eq_nil_iff` (theorem, [line 485](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L485))

```lean
theorem extract_eq_nil_iff {xs : ωSequence α} {m n : ℕ} :
    xs.extract m n = [] ↔ n ≤ m
```

`Cslib.ωSequence.get_extract` (theorem, [line 491](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L491))

```lean
theorem get_extract {xs : ωSequence α} {m n k : ℕ} (h : k < n - m) :
    (xs.extract m n)[k]'(by simp [h]) = xs (m + k)
```

`Cslib.ωSequence.append_extract_extract` (theorem, [line 495](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L495))

```lean
theorem append_extract_extract {xs : ωSequence α} {k m n : ℕ} (h_km : k ≤ m) (h_mn : m ≤ n) :
    (xs.extract k m) ++ (xs.extract m n) = xs.extract k n
```

`Cslib.ωSequence.extract_succ_right` (theorem, [line 501](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L501))

```lean
theorem extract_succ_right {xs : ωSequence α} {m n : ℕ} (h_mn : m ≤ n) :
    xs.extract m (n + 1) = xs.extract m n ++ [xs n]
```

`Cslib.ωSequence.extract_lu_extract_lu` (theorem, [line 507](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L507))

```lean
theorem extract_lu_extract_lu {xs : ωSequence α} {m n i j : ℕ} (h : j ≤ n - m) :
    (xs.extract m n).extract i j = xs.extract (m + i) (m + j)
```

`Cslib.ωSequence.extract_0u_extract_lu` (theorem, [line 513](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L513))

```lean
theorem extract_0u_extract_lu {xs : ωSequence α} {n i j : ℕ} (h : j ≤ n) :
    (xs.extract 0 n).extract i j = xs.extract i j
```

`Cslib.ωSequence.extract_0u_extract_l` (theorem, [line 518](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L518))

```lean
theorem extract_0u_extract_l {xs : ωSequence α} {n i : ℕ} :
    (xs.extract 0 n).extract i = xs.extract i n
```

`Cslib.ωSequence.take_extract` (theorem, [line 523](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L523))

```lean
theorem take_extract {xs : ωSequence α} {m n k : ℕ} (h : k ≤ n - m) :
    (xs.extract m n).take k = xs.extract m (m + k)
```

`Cslib.ωSequence.drop_extract` (theorem, [line 528](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean#L528))

```lean
theorem drop_extract {xs : ωSequence α} {m n k : ℕ} (h : k ≤ n - m) :
    (xs.extract m n).drop k = xs.extract (m + k) n
```

## Depends on

- [Definition of `ωSequence` and functions on infinite sequences](defs.md)

## Sources

- [Cslib/Foundations/Data/OmegaSequence/Init.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Init.lean)

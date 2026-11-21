---
catalog: module
lean: List.interleave, List.nil_interleave, List.interleave_nil, List.cons_interleave, List.interleave_perm_append, List.interleave_eq_nil, List.Perm.interleave, List.length_interleave, List.countP_interleave, List.count_interleave, List.interleave_append_append_of_length_eq_length, List.interleave_append_append_of_length_eq_length_add_one, List.interleave_append_left, List.interleave_append_right, List.interleave_flatten_flatten_of_length_eq_length, List.reverse_interleave_of_length_eq_length, List.reverse_interleave_of_length_eq_length_add_one, List.interleave_ofFn_ofFn_even, List.interleave_ofFn_ofFn_odd, List.right_sublist_interleave, List.left_sublist_interleave, List.IsPrefix.interleave
statement: formalized
proof: formalized
---

# Interleaving lists

`Batteries.Data.List.Interleave`, in [Batteries/Data/List/Interleave.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean), by Yaël Dillies.

> This file defines interleaving of lists as an operation.

`List.interleave` (definition, [line 33](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L33))

> Interleave two lists `l₁` and `l₂`, starting with an element of `l₁`.
>
> This operation fully interleave the two lists when the length of `l₁` is either the length of `l₂`
> or one more. If one of the lists runs out early, the remainder of the other list is kept without
> further interleaving, so that `l₁.interleave l₂` is always a permutation of `l₁ ++ l₂`.
> See `interleave_perm_append`.
>
> ```
> #eval interleave [0, 2, 4] [1] -- [0, 1, 2, 4] -- The second list is too short
> #eval interleave [0, 2, 4] [1, 3] -- [0, 1, 2, 3, 4]
> #eval interleave [0, 2] [1, 3] -- [0, 1, 2, 3]
> #eval interleave [0] [1, 3] -- [0, 1, 3] -- The first list is too short
> ```

```lean
def interleave : List α → List α → List α
```

`List.nil_interleave` (theorem, [line 38](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L38))

```lean
theorem nil_interleave (l₂ : List α) : [].interleave l₂ = l₂
```

`List.interleave_nil` (theorem, [line 41](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L41))

```lean
theorem interleave_nil (l₁ : List α) : l₁.interleave [] = l₁
```

`List.cons_interleave` (theorem, [line 44](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L44))

```lean
theorem cons_interleave (a : α) (l₁ : List α) (l₂ : List α) :
    (a :: l₁).interleave l₂ = a :: interleave l₂ l₁
```

`List.interleave_perm_append` (theorem, [line 47](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L47))

```lean
theorem interleave_perm_append : ∀ {l₁ l₂ : List α}, l₁.interleave l₂ ~ l₁ ++ l₂
```

`List.interleave_eq_nil` (theorem, [line 54](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L54))

```lean
theorem interleave_eq_nil : l₁.interleave l₂ = [] ↔ l₁ = [] ∧ l₂ = []
```

`List.Perm.interleave` (theorem, [line 57](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L57))

```lean
protected theorem Perm.interleave (h₁₃ : l₁ ~ l₃) (h₂₄ : l₂ ~ l₄) :
    l₁.interleave l₂ ~ l₃.interleave l₄
```

`List.length_interleave` (theorem, [line 61](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L61))

```lean
theorem length_interleave (l₁ l₂ : List α) :
    (l₁.interleave l₂).length = l₁.length + l₂.length
```

`List.countP_interleave` (theorem, [line 64](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L64))

```lean
theorem countP_interleave (l₁ l₂ : List α) (p : α → Bool) :
    (l₁.interleave l₂).countP p = l₁.countP p + l₂.countP p
```

`List.count_interleave` (theorem, [line 68](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L68))

```lean
theorem count_interleave [BEq α] (l₁ l₂ : List α) (a : α) :
    (l₁.interleave l₂).count a = l₁.count a + l₂.count a
```

`List.interleave_append_append_of_length_eq_length` (theorem, [line 72](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L72))

```lean
theorem interleave_append_append_of_length_eq_length :
    ∀ {l₁ l₂ : List α} (_h₁₂ : l₁.length = l₂.length) (l₃ l₄ : List α),
      (l₁ ++ l₃).interleave (l₂ ++ l₄) = l₁.interleave l₂ ++ l₃.interleave l₄
```

`List.interleave_append_append_of_length_eq_length_add_one` (theorem, [line 78](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L78))

```lean
theorem interleave_append_append_of_length_eq_length_add_one :
    ∀ {l₁ l₂ : List α} (_h₁₂ : l₁.length = l₂.length + 1) (l₃ l₄ : List α),
      (l₁ ++ l₃).interleave (l₂ ++ l₄) = l₁.interleave l₂ ++ l₄.interleave l₃
```

`List.interleave_append_left` (theorem, [line 83](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L83))

```lean
theorem interleave_append_left :
    ∀ {l₁ l₂ : List α} (_h₂₁ : l₂.length ≤ l₁.length) (l₃ : List α),
      (l₁ ++ l₃).interleave l₂ = l₁.interleave l₂ ++ l₃
```

`List.interleave_append_right` (theorem, [line 89](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L89))

```lean
theorem interleave_append_right :
    ∀ {l₁ l₂ : List α} (_h₁₂ : l₁.length ≤ l₂.length + 1) (l₃ : List α),
    l₁.interleave (l₂ ++ l₃) = l₁.interleave l₂ ++ l₃
```

`List.interleave_flatten_flatten_of_length_eq_length` (theorem, [line 96](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L96))

```lean
theorem interleave_flatten_flatten_of_length_eq_length :
    ∀ {L₁ L₂ : List (List α)} (h₁₂ : L₁.length = L₂.length),
      (∀ i (hi : i + 1 < L₁.length), length L₁[i] = length L₂[i]) →
        L₁.flatten.interleave L₂.flatten = (zipWith interleave L₁ L₂).flatten
```

`List.reverse_interleave_of_length_eq_length` (theorem, [line 107](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L107))

```lean
theorem reverse_interleave_of_length_eq_length :
    ∀ {l₁ l₂ : List α}, l₁.length = l₂.length →
      (l₁.interleave l₂).reverse = l₂.reverse.interleave l₁.reverse
```

`List.reverse_interleave_of_length_eq_length_add_one` (theorem, [line 113](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L113))

```lean
theorem reverse_interleave_of_length_eq_length_add_one :
    ∀ {l₁ l₂ : List α}, l₁.length = l₂.length + 1 →
      (l₁.interleave l₂).reverse = l₁.reverse.interleave l₂.reverse
```

`List.interleave_ofFn_ofFn_even` (theorem, [line 119](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L119))

```lean
theorem interleave_ofFn_ofFn_even :
    ∀ {n : Nat} {f g : Fin n → α},
      interleave (ofFn f) (ofFn g) =
        ofFn (n := 2 * n) (fun i => if i.val % 2 = 0 then f ⟨i / 2, by lia⟩ else g ⟨i / 2, by lia⟩)
```

`List.interleave_ofFn_ofFn_odd` (theorem, [line 126](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L126))

```lean
theorem interleave_ofFn_ofFn_odd :
    ∀ {n : Nat} {f : Fin (n + 1) → α} {g : Fin n → α},
      interleave (ofFn f) (ofFn g) =
        ofFn (n := 2 * n + 1)
          (fun i => if hi : i.val % 2 = 0 then f ⟨i / 2, by lia⟩ else g ⟨i / 2, by lia⟩)
```

`List.right_sublist_interleave` (theorem, [line 134](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L134))

```lean
theorem right_sublist_interleave : ∀ {l₁ l₂ : List α}, l₂ <+ l₁.interleave l₂
```

`List.left_sublist_interleave` (theorem, [line 141](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L141))

```lean
theorem left_sublist_interleave : l₁ <+ l₁.interleave l₂
```

`List.IsPrefix.interleave` (theorem, [line 143](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean#L143))

```lean
protected theorem IsPrefix.interleave  :
    l₁.length = l₂.length ∨ l₁.length = l₂.length + 1 →
    l₁ <+: l₃ → l₂ <+: l₄ → l₁.interleave l₂ <+: l₃.interleave l₄
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/List/Interleave.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Interleave.lean)
- [Declaration ledger](../../../../../../sources/batteries/Batteries.Data.List.Interleave.json)

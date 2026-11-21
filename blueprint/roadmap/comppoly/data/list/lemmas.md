---
catalog: module
lean: List.append_getLast_dropLast, List.foldl_congr_of_mem, List.foldl_split_outer, List.foldl_split_inner, List.foldr_split_outer, List.foldr_split_inner, List.mapM_single, List.getLastI_append_single, List.leftpad_eq_self, List.rightpad_length, List.rightpad_prefix, List.rightpad_suffix, List.rightpad_eq_self, List.rightpad_eq_rightpad_max, List.rightpad_eq_rightpad_append_replicate_of_ge, List.rightpad_eq_if_rightpad_eq_of_ge, List.rightpad_twice_eq_rightpad_max, List.rightpad_getD_eq_getD, List.rightpad_getElem_eq_getD, List.matchSize, List.matchSize_comm, List.matchSize_eq_iff_forall_eq, List.dropLastWhile, List.zipWith_const, List.Nodup.pairwise_ne_map
statement: formalized
proof: formalized
---

# Auxiliary lemmas for `List`

`CompPoly.Data.List.Lemmas`, in [CompPoly/Data/List/Lemmas.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean), by Quang Dao, Chung Thai Nguyen, Gregor Mitscha-Baude.

`List.append_getLast_dropLast` (theorem, [line 23](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L23))

```lean
theorem append_getLast_dropLast {α : Type u} (l : List α) (h : l ≠ []) :
    l.dropLast ++ [l.getLast h] = l
```

`List.foldl_congr_of_mem` (theorem, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L37))

```lean
theorem foldl_congr_of_mem {α : Type u} {β : Type v} {f g : α → β → α}
    (xs : List β) (acc : α) (h : ∀ acc' x, x ∈ xs → f acc' x = g acc' x) :
    xs.foldl f acc = xs.foldl g acc
```

`List.foldl_split_outer` (theorem, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L50))

```lean
theorem foldl_split_outer {α : Type u} {β : Type v} (f : α → β → α) (init : α)
    (l : List β) (h : l ≠ []): foldl (f:=f) (init:=init) (l)
    = f (foldl (f:=f) (init:=init) (l.dropLast)) (l.getLast (by omega))
```

`List.foldl_split_inner` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L57))

```lean
theorem foldl_split_inner {α : Type u} {β : Type v} (f : α → β → α) (init : α)
    (l : List β) (h : l ≠ []): foldl (f:=f) (init:=init) (l)
    = foldl (f:=f) (init:=f (init) (l.head (by omega))) (l.tail)
```

`List.foldr_split_outer` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L65))

```lean
theorem foldr_split_outer {α : Type u} {β : Type v} (f : α → β → β) (init : β)
    (l : List α) (h : l ≠ []): foldr (f:=f) (init:=init) (l)
    = f (l.head (by omega)) (foldr (f:=f) (init:=init) (l.tail))
```

`List.foldr_split_inner` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L73))

```lean
theorem foldr_split_inner {α : Type u} {β : Type v} (f : α → β → β) (init : β)
    (l : List α) (h : l ≠ []): foldr (f:=f) (init:=init) (l)
    = foldr (f:=f) (init:=f (l.getLast (by omega)) (init)) (l.dropLast)
```

`List.mapM_single` (theorem, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L83))

```lean
theorem mapM_single (f : α → m β) (a : α) : List.mapM f [a] = return [← f a]
```

`List.getLastI_append_single` (theorem, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L88))

```lean
theorem getLastI_append_single [Inhabited α] (x : α) : (l ++ [x]).getLastI = x
```

`List.leftpad_eq_self` (theorem, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L94))

```lean
theorem leftpad_eq_self (l : List α) (n : Nat) (h : l.length ≥ n) :
    leftpad n unit l = l
```

`List.rightpad_length` (theorem, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L97))

```lean
theorem rightpad_length (n : Nat) (unit : α) (l : List α) :
    (rightpad n unit l).length = max n l.length
```

`List.rightpad_prefix` (theorem, [line 101](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L101))

```lean
theorem rightpad_prefix (n : Nat) (unit : α) (l : List α) :
    l <+: rightpad n unit l
```

`List.rightpad_suffix` (theorem, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L106))

```lean
theorem rightpad_suffix (n : Nat) (unit : α) (l : List α) :
    replicate (n - l.length) unit <:+ rightpad n unit l
```

`List.rightpad_eq_self` (theorem, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L111))

```lean
theorem rightpad_eq_self (l : List α) (n : Nat) (h : n ≤ l.length) :
    rightpad n unit l = l
```

`List.rightpad_eq_rightpad_max` (theorem, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L114))

```lean
theorem rightpad_eq_rightpad_max (l : List α) (n : Nat) :
    rightpad n unit l = rightpad (max n l.length) unit l
```

`List.rightpad_eq_rightpad_append_replicate_of_ge` (theorem, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L117))

```lean
theorem rightpad_eq_rightpad_append_replicate_of_ge
    (l : List α) (m n : Nat) (h : n ≤ m) :
  rightpad m unit l = rightpad n unit l ++ replicate (m - max n l.length) unit
```

`List.rightpad_eq_if_rightpad_eq_of_ge` (theorem, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L122))

```lean
theorem rightpad_eq_if_rightpad_eq_of_ge (l l' : List α) (m n n' : Nat) (h : n ≤ m) (h' : n' ≤ m) :
    rightpad n unit l = rightpad n' unit l' →
  rightpad m unit l = rightpad m unit l'
```

`List.rightpad_twice_eq_rightpad_max` (theorem, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L139))

```lean
theorem rightpad_twice_eq_rightpad_max (m n : Nat) (unit : α) (l : List α) :
    rightpad n unit (rightpad m unit l) = rightpad (max m n) unit l
```

`List.rightpad_getD_eq_getD` (theorem, [line 159](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L159))

```lean
theorem rightpad_getD_eq_getD (l : List α) (n : Nat) (unit : α) (i : Nat) :
    (rightpad n unit l).getD i unit = l.getD i unit
```

`List.rightpad_getElem_eq_getD` (theorem, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L173))

```lean
theorem rightpad_getElem_eq_getD {a b : List α} {unit : α} {i : Nat}
    (h : i < (a.rightpad b.length unit).length) :
  (a.rightpad b.length unit)[i] = a.getD i unit
```

`List.matchSize` (definition, [line 180](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L180))

> Given two lists of potentially different lengths, right-pads the shorter list with `unit`
> elements until they are the same length.

```lean
def matchSize (l₁ : List α) (l₂ : List α) (unit : α) : List α × List α
```

`List.matchSize_comm` (theorem, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L183))

```lean
theorem matchSize_comm (l₁ : List α) (l₂ : List α) (unit : α) :
    matchSize l₁ l₂ unit = (matchSize l₂ l₁ unit).swap
```

`List.matchSize_eq_iff_forall_eq` (theorem, [line 189](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L189))

> `List.matchSize` returns two equal lists iff the two lists agree at every index `i : Nat`
> (extended by `unit` if necessary).

```lean
theorem matchSize_eq_iff_forall_eq (l₁ l₂ : List α) (unit : α) :
    (fun (x, y) => x = y) (matchSize l₁ l₂ unit) ↔ ∀ i : Nat, l₁.getD i unit = l₂.getD i unit
```

`List.dropLastWhile` (definition, [line 207](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L207))

> `List.dropWhile` but starting from the last element. Performed by `dropWhile` on the reversed
> list, followed by a reversal.

```lean
def dropLastWhile (p : α → Bool) (l : List α) : List α
```

`List.zipWith_const` (lemma, [line 210](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L210))

```lean
lemma zipWith_const {α β : Type _} {f : α → β → β} {l₁ : List α} {l₂ : List β}
    (h₁ : l₁.length = l₂.length) (h₂ : ∀ a b, f a b = b) : l₁.zipWith f l₂ = l₂
```

`List.Nodup.pairwise_ne_map` (theorem, [line 218](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean#L218))

> An injective `f` separates the elements of a duplicate-free list pairwise.
>
> This is `List.Nodup.map` transported along `List.pairwise_map`, stated in the unmapped form that
> `Std.ExtTreeMap.getElem_ofList_of_mem` and friends ask for.

```lean
theorem Nodup.pairwise_ne_map {α : Type u} {β : Type v} {l : List α} {f : α → β}
    (hf : Function.Injective f) (hl : l.Nodup) : l.Pairwise fun a b => f a ≠ f b
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Data/List/Lemmas.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Data/List/Lemmas.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Data.List.Lemmas.json)

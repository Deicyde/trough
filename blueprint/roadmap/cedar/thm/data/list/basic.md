---
catalog: module
lean: List.Equiv, List.Equiv.refl, List.Equiv.symm, List.Equiv.trans, List.equiv_nil, List.cons_equiv_cons, List.cons_equiv_implies_equiv, List.dup_head_equiv, List.dup_head_equiv', List.swap_cons_cons_equiv, List.filter_equiv, List.map_equiv, List.filterMap_equiv, List.append_swap_equiv, List.append_left_equiv, List.append_right_equiv, List.SortedBy, List.Sorted, List.tail_sortedBy, List.sortedBy_implies_head_lt_tail, List.sortedBy_equiv_implies_head_eq, List.sortedBy_equiv_implies_tail_subset, List.sortedBy_equiv_implies_tail_equiv, List.sortedBy_equiv_implies_eq, List.sortedBy_cons, List.mem_of_sortedBy_unique, List.mem_of_sortedBy_implies_find?, List.map_eq_implies_sortedBy, List.filter_sortedBy, List.filterMap_sortedBy, List.filterMap_key_id_sortedBy_key, List.find?_filterMap_key_id, List.mapM_key_id_sortedBy_key, List.isSortedBy_correct, List.isSorted_correct, List.Forallᵥ, List.forallᵥ_def
statement: formalized
proof: formalized
---

# List properties

`Cedar.Thm.Data.List.Basic`, in [Cedar/Thm/Data/List/Basic.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean).

> This file contains useful custom definitions and lemmas about Lists.

> ### Equiv

`List.Equiv` (definition, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L40))

```lean
public def Equiv {α} (a b : List α) : Prop
```

`List.Equiv.refl` (theorem, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L45))

```lean
public theorem Equiv.refl {a : List α} :
  a ≡ a
```

`List.Equiv.symm` (theorem, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L49))

```lean
public theorem Equiv.symm {a b : List α} :
  a ≡ b → b ≡ a
```

`List.Equiv.trans` (theorem, [line 53](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L53))

```lean
public theorem Equiv.trans {a b c : List α} :
  a ≡ b → b ≡ c → a ≡ c
```

`List.equiv_nil` (theorem, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L63))

```lean
public theorem equiv_nil (xs : List α) :
  xs ≡ [] ↔ xs = []
```

`List.cons_equiv_cons` (theorem, [line 73](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L73))

```lean
public theorem cons_equiv_cons (x : α) (xs ys : List α) :
  xs ≡ ys → x :: xs ≡ x :: ys
```

`List.cons_equiv_implies_equiv` (theorem, [line 84](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L84))

```lean
public theorem cons_equiv_implies_equiv (x : α) (xs ys : List α) :
  x :: xs ≡ x :: ys → x ∉ xs → x ∉ ys → xs ≡ ys
```

`List.dup_head_equiv` (theorem, [line 99](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L99))

```lean
public theorem dup_head_equiv (x : α) (xs : List α) :
  x :: x :: xs ≡ x :: xs
```

`List.dup_head_equiv'` (theorem, [line 103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L103))

```lean
public theorem dup_head_equiv' {x : α} {xs : List α} :
  x ∈ xs → x :: xs ≡ xs
```

`List.swap_cons_cons_equiv` (theorem, [line 107](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L107))

```lean
public theorem swap_cons_cons_equiv (x₁ x₂ : α) (xs : List α) :
  x₁ :: x₂ :: xs ≡ x₂ :: x₁ :: xs
```

`List.filter_equiv` (theorem, [line 115](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L115))

```lean
public theorem filter_equiv (f : α → Bool) (xs ys : List α) :
  xs ≡ ys → xs.filter f ≡ ys.filter f
```

`List.map_equiv` (theorem, [line 126](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L126))

```lean
public theorem map_equiv (f : α → β) (xs ys : List α) :
  xs ≡ ys → xs.map f ≡ ys.map f
```

`List.filterMap_equiv` (theorem, [line 141](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L141))

```lean
public theorem filterMap_equiv (f : α → Option β) (xs ys : List α) :
  xs ≡ ys → xs.filterMap f ≡ ys.filterMap f
```

`List.append_swap_equiv` (theorem, [line 153](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L153))

```lean
public theorem append_swap_equiv (xs ys : List α) :
  xs ++ ys ≡ ys ++ xs
```

`List.append_left_equiv` (theorem, [line 158](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L158))

```lean
public theorem append_left_equiv (xs ys zs : List α) :
  xs ≡ ys → xs ++ zs ≡ ys ++ zs
```

`List.append_right_equiv` (theorem, [line 168](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L168))

```lean
public theorem append_right_equiv (xs ys zs : List α) :
  ys ≡ zs → xs ++ ys ≡ xs ++ zs
```

> ### Sorted

`List.SortedBy` (inductive type, [line 180](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L180))

```lean
public inductive SortedBy [LT β] (f : α → β) : List α → Prop where
  | nil : SortedBy f []
  | cons_nil {x} : SortedBy f (x :: nil)
  | cons_cons {x y ys} :
      f x < f y →
      SortedBy f (y :: ys) →
      SortedBy f (x :: y :: ys)
```

`List.Sorted` (abbreviation, [line 188](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L188))

```lean
public abbrev Sorted [LT α] (xs : List α)
```

`List.tail_sortedBy` (theorem, [line 190](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L190))

```lean
public theorem tail_sortedBy [LT β] {f : α → β} {x : α} {xs : List α} :
  SortedBy f (x :: xs) → SortedBy f xs
```

`List.sortedBy_implies_head_lt_tail` (theorem, [line 197](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L197))

```lean
public theorem sortedBy_implies_head_lt_tail [LT β] [StrictLT β] {f : α → β} {x : α} {xs : List α} :
  SortedBy f (x :: xs) → ∀ y, y ∈ xs → f x < f y
```

`List.sortedBy_equiv_implies_head_eq` (theorem, [line 216](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L216))

```lean
public theorem sortedBy_equiv_implies_head_eq [LT β] [StrictLT β] (f : α → β) {x y : α} {xs ys : List α} :
  SortedBy f (x :: xs) →
  SortedBy f (y :: ys) →
  (x :: xs) ≡ (y :: ys) →
  x = y
```

`List.sortedBy_equiv_implies_tail_subset` (theorem, [line 234](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L234))

```lean
public theorem sortedBy_equiv_implies_tail_subset [LT β] [StrictLT β] (f : α → β) {x : α} {xs ys : List α} :
  SortedBy f (x :: xs) →
  SortedBy f (x :: ys) →
  (x :: xs) ⊆ (x :: ys) →
  xs ⊆ ys
```

`List.sortedBy_equiv_implies_tail_equiv` (theorem, [line 253](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L253))

```lean
public theorem sortedBy_equiv_implies_tail_equiv [LT β] [StrictLT β] (f : α → β) {x : α} {xs ys : List α} :
  SortedBy f (x :: xs) →
  SortedBy f (x :: ys) →
  (x :: xs) ≡ (x :: ys) →
  xs ≡ ys
```

`List.sortedBy_equiv_implies_eq` (theorem, [line 266](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L266))

```lean
public theorem sortedBy_equiv_implies_eq [LT β] [StrictLT β] (f : α → β) {xs ys : List α} :
  SortedBy f xs → SortedBy f ys → xs ≡ ys → xs = ys
```

`List.sortedBy_cons` (theorem, [line 292](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L292))

```lean
public theorem sortedBy_cons [LT β] [StrictLT β] {f : α → β} {x : α} {ys : List α} :
  SortedBy f ys →
  (∀ y, y ∈ ys → f x < f y) →
  SortedBy f (x :: ys)
```

`List.mem_of_sortedBy_unique` (theorem, [line 305](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L305))

```lean
public theorem mem_of_sortedBy_unique {α β} [LT β] [StrictLT β] [DecidableLT β] [DecidableEq β]
  {f : α → β} {x y : α} {xs : List α} :
  xs.SortedBy f → x ∈ xs → y ∈ xs → f x = f y →
  x = y
```

`List.mem_of_sortedBy_implies_find?` (theorem, [line 328](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L328))

```lean
public theorem mem_of_sortedBy_implies_find? {α β} [LT β] [StrictLT β] [DecidableLT β] [DecidableEq β]
  {f : α → β} {x : α} {xs : List α} :
  x ∈ xs → xs.SortedBy f →
  xs.find? (fun y => f y == f x) = x
```

`List.map_eq_implies_sortedBy` (theorem, [line 352](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L352))

```lean
public theorem map_eq_implies_sortedBy [LT β] [StrictLT β] {f : α → β} {g : γ → β} {xs : List α} {ys : List γ} :
  xs.map f = ys.map g →
  (SortedBy f xs ↔ SortedBy g ys)
```

`List.filter_sortedBy` (theorem, [line 395](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L395))

```lean
public theorem filter_sortedBy [LT β] [StrictLT β] [DecidableLT β] {f : α → β} (p : α → Bool) {xs : List α} :
  SortedBy f xs → SortedBy f (xs.filter p)
```

`List.filterMap_sortedBy` (theorem, [line 412](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L412))

```lean
public theorem filterMap_sortedBy [LT β] [StrictLT β] [DecidableLT β] {f : α → β} {g : α → Option γ} {f' : γ → β} {xs : List α} :
  (∀ x y, g x = some y → f x = f' y) →
  SortedBy f xs →
  SortedBy f' (xs.filterMap g)
```

`List.filterMap_key_id_sortedBy_key` (theorem, [line 439](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L439))

```lean
public theorem filterMap_key_id_sortedBy_key {α β : Type} [LT α] [StrictLT α] [DecidableLT α] {ks : List α} {fn : α → Option β}
  (hs : ks.Sorted) :
  (ks.filterMap (λ k => do (some (k, ←fn k)))).SortedBy Prod.fst
```

`List.find?_filterMap_key_id` (theorem, [line 452](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L452))

```lean
public theorem find?_filterMap_key_id {α β : Type} [BEq α] [LawfulBEq α] {ks : List α} {fn : α → Option β} {k: α}
  (h₂ : k ∈ ks) :
  ((ks.filterMap (λ k => do (k, ←fn k))).find? (λ ⟨k', _⟩ => k' == k)).map Prod.snd = fn k
```

`List.mapM_key_id_sortedBy_key` (theorem, [line 474](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L474))

```lean
public theorem mapM_key_id_sortedBy_key {α β : Type} [LT α] {ks : List α} {kvs : List (α × β)} {fn : α → Option β}
  (hm : ks.mapM (λ k => do (some (k, ←fn k))) = some kvs)
  (hs : ks.Sorted) :
  kvs.SortedBy Prod.fst
```

`List.isSortedBy_correct` (theorem, [line 510](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L510))

```lean
public theorem isSortedBy_correct {α β} [LT β] [DecidableLT β] {l : List α} {f : α → β} :
  l.SortedBy f ↔ l.isSortedBy f
```

`List.isSorted_correct` (theorem, [line 535](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L535))

```lean
public theorem isSorted_correct {α} [LT α] [DecidableLT α] {l : List α} :
  l.Sorted ↔ l.isSorted
```

> ### Forallᵥ

`List.Forallᵥ` (definition, [line 563](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L563))

```lean
public def Forallᵥ {α β γ} (p : β → γ → Prop) (kvs₁ : List (α × β)) (kvs₂ : List (α × γ)) : Prop
```

`List.forallᵥ_def` (theorem, [line 566](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean#L566))

```lean
public theorem forallᵥ_def {α β γ} {p : β → γ → Prop} {kvs₁ : List (α × β)} {kvs₂ : List (α × γ)} :
  List.Forallᵥ p kvs₁ kvs₂ = List.Forall₂ (λ kv₁ kv₂ => kv₁.fst = kv₂.fst ∧ p kv₁.snd kv₂.snd) kvs₁ kvs₂
```

## Depends on

- [Cedar/Data/LT](../../../data/lt.md)
- [List](../../../data/list.md)

## Proof depends on

- [Data/Control](../control.md)

## Sources

- [Cedar/Thm/Data/List/Basic.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Basic.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Data.List.Basic.json)

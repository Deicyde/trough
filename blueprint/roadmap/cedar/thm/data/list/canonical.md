---
catalog: module
lean: List.insertCanonical_singleton, List.insertCanonical_not_nil, List.insertCanonical_mem, List.insertCanonical_find?, List.insertCanonical_preserves_find_other_element, List.insertCanonical_sortedBy, List.insertCanonical_subset, List.insertCanonical_equiv, List.insertCanonical_preserves_forallᵥ, List.insertCanonical_map_fst, List.insertCanonical_map_fst_canonicalize, List.canonicalize_nil, List.canonicalize_nil', List.canonicalize_not_nil, List.canonicalize_cons, List.canonicalize_singleton, List.canonicalize_sortedBy, List.sortedBy_implies_canonicalize_eq, List.canonicalize_subseteq, List.in_canonicalize_in_list, List.canonicalize_equiv, List.equiv_implies_canonical_eq, List.canonicalize_idempotent, List.canonicalize_id_filter, List.canonicalize_preserves_forallᵥ, List.canonicalize_of_map_fst, List.list_find?_in_tail, List.list_find?_at_head, List.mergeCanonical_nil_left, List.mergeCanonical_nil_right, List.mem_mergeCanonical, List.mergeCanonical_self, List.mergeCanonical_comm, List.mergeCanonical_assoc, List.mergeCanonical_sortedBy
statement: formalized
proof: formalized
---

# Properties of list canonicalization

`Cedar.Thm.Data.List.Canonical`, in [Cedar/Thm/Data/List/Canonical.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean).

> This file contains lemmas about list canonicalization.

> ### insertCanonical

`List.insertCanonical_singleton` (theorem, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L37))

```lean
public theorem insertCanonical_singleton [LT β] [DecidableLT β] (f : α → β)  (x : α) :
  insertCanonical f x [] = [x]
```

`List.insertCanonical_not_nil` (theorem, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L41))

```lean
public theorem insertCanonical_not_nil [DecidableEq β] [LT β] [DecidableLT β] (f : α → β) (x : α) (xs : List α) :
  insertCanonical f x xs ≠ []
```

`List.insertCanonical_mem` (theorem, [line 53](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L53))

```lean
public theorem insertCanonical_mem [LT β] [Cedar.Data.StrictLT β] [DecidableLT β]
  {f : α → β} {xs : List α} (x : α) :
  x ∈ List.insertCanonical f x xs
```

`List.insertCanonical_find?` (theorem, [line 65](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L65))

```lean
public theorem insertCanonical_find?
  [LT β] [Cedar.Data.StrictLT β] [DecidableLT β] [BEq β] [LawfulBEq β]
  {f : α → β} {xs : List α} (x : α) :
  (List.insertCanonical f x xs).find? (λ e => f e == f x) = x
```

`List.insertCanonical_preserves_find_other_element` (theorem, [line 117](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L117))

```lean
public theorem insertCanonical_preserves_find_other_element
  [LT α] [DecidableLT α] [BEq α] [StrictLT α]
  (k : α)
  (x : (α × β)) (xs : List (α × β))  :
  (x.fst == k) = false →
  (List.insertCanonical Prod.fst x xs).find? (λ x => x.fst == k) =
  xs.find? (λ x => x.fst == k)
```

`List.insertCanonical_sortedBy` (theorem, [line 149](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L149))

```lean
public theorem insertCanonical_sortedBy [LT β] [StrictLT β] [DecidableLT β] {f : α → β} {xs : List α} (x : α) :
  SortedBy f xs →
  SortedBy f (insertCanonical f x xs)
```

`List.insertCanonical_subset` (theorem, [line 205](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L205))

```lean
public theorem insertCanonical_subset [LT β] [DecidableLT β] (f : α → β) (x : α) (xs : List α) :
  insertCanonical f x xs ⊆ x :: xs
```

`List.insertCanonical_equiv` (theorem, [line 220](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L220))

```lean
public theorem insertCanonical_equiv [LT α] [StrictLT α] [DecidableLT α] (x : α) (xs : List α) :
  x :: xs ≡ insertCanonical id x xs
```

`List.insertCanonical_preserves_forallᵥ` (theorem, [line 276](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L276))

```lean
public theorem insertCanonical_preserves_forallᵥ {α β γ} [LT α] [StrictLT α] [DecidableLT α] {p : β → γ → Prop}
  {kv₁ : α × β} {kv₂ : α × γ} {kvs₁ : List (α × β)} {kvs₂ : List (α × γ)}
  (h₁ : kv₁.fst = kv₂.fst ∧ p kv₁.snd kv₂.snd)
  (h₂ : Forallᵥ p kvs₁ kvs₂) :
  Forallᵥ p (insertCanonical Prod.fst kv₁ kvs₁) (insertCanonical Prod.fst kv₂ kvs₂)
```

`List.insertCanonical_map_fst` (theorem, [line 306](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L306))

```lean
public theorem insertCanonical_map_fst {α β γ} [LT α] [StrictLT α] [DecidableLT α] (xs : List (α × β)) (f : β → γ) (x : α × β) :
  insertCanonical Prod.fst (Prod.map id f x) (map (Prod.map id f) xs) =
  map (Prod.map id f) (insertCanonical Prod.fst x xs)
```

`List.insertCanonical_map_fst_canonicalize` (theorem, [line 322](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L322))

```lean
public theorem insertCanonical_map_fst_canonicalize {α β γ} [LT α] [StrictLT α] [DecidableLT α] (xs : List (α × β)) (f : β → γ) (x : α × β) :
  insertCanonical Prod.fst (Prod.map id f x) (canonicalize Prod.fst (map (Prod.map id f) xs)) =
  map (Prod.map id f) (insertCanonical Prod.fst x (canonicalize Prod.fst xs))
```

> ## canonicalize

`List.canonicalize_nil` (theorem, [line 372](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L372))

```lean
public theorem canonicalize_nil [LT β] [DecidableLT β] (f : α → β) :
  canonicalize f [] = []
```

`List.canonicalize_nil'` (theorem, [line 376](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L376))

```lean
public theorem canonicalize_nil' [DecidableEq β] [LT β] [DecidableLT β] (f : α → β) (xs : List α) :
  xs = [] ↔ (canonicalize f xs) = []
```

`List.canonicalize_not_nil` (theorem, [line 393](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L393))

```lean
public theorem canonicalize_not_nil [DecidableEq β] [LT β] [DecidableLT β] (f : α → β) (xs : List α) :
  xs ≠ [] ↔ (canonicalize f xs) ≠ []
```

`List.canonicalize_cons` (theorem, [line 409](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L409))

```lean
public theorem canonicalize_cons [LT β] [DecidableLT β] (f : α → β) (xs : List α) (a : α) :
  canonicalize f xs = canonicalize f ys → canonicalize f (a :: xs) = canonicalize f (a :: ys)
```

`List.canonicalize_singleton` (theorem, [line 416](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L416))

```lean
public theorem canonicalize_singleton [LT β] [DecidableLT β] (f : α → β) (x : α) :
  canonicalize f [x] = [x]
```

`List.canonicalize_sortedBy` (theorem, [line 421](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L421))

```lean
public theorem canonicalize_sortedBy [LT β] [StrictLT β] [DecidableLT β] (f : α → β) (xs : List α) :
  SortedBy f (canonicalize f xs)
```

`List.sortedBy_implies_canonicalize_eq` (theorem, [line 431](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L431))

```lean
public theorem sortedBy_implies_canonicalize_eq [LT β] [StrictLT β] [DecidableLT β] {f : α → β} {xs : List α} :
  SortedBy f xs → (canonicalize f xs) = xs
```

`List.canonicalize_subseteq` (theorem, [line 443](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L443))

```lean
public theorem canonicalize_subseteq [LT β] [StrictLT β] [DecidableLT β] (f : α → β) (xs : List α) :
  xs.canonicalize f ⊆ xs
```

`List.in_canonicalize_in_list` (theorem, [line 455](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L455))

> Corollary of `canonicalize_subseteq`

```lean
public theorem in_canonicalize_in_list [LT β] [StrictLT β] [DecidableLT β] {f : α → β} {x : α} {xs : List α} :
  x ∈ xs.canonicalize f → x ∈ xs
```

`List.canonicalize_equiv` (theorem, [line 468](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L468))

```lean
public theorem canonicalize_equiv [LT α] [StrictLT α] [DecidableLT α] (xs : List α) :
  xs ≡ canonicalize id xs
```

`List.equiv_implies_canonical_eq` (theorem, [line 486](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L486))

```lean
public theorem equiv_implies_canonical_eq [LT α] [StrictLT α] [DecidableLT α] (xs ys : List α) :
  xs ≡ ys → (canonicalize id xs) = (canonicalize id ys)
```

`List.canonicalize_idempotent` (theorem, [line 518](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L518))

```lean
public theorem canonicalize_idempotent {α β} [LT β] [StrictLT β] [DecidableLT β] (f : α → β) (xs : List α) :
  canonicalize f (canonicalize f xs) = canonicalize f xs
```

`List.canonicalize_id_filter` (theorem, [line 531](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L531))

```lean
public theorem canonicalize_id_filter {α} [LT α] [StrictLT α] [DecidableLT α] (p : α → Bool) (xs : List α) :
  (canonicalize id xs).filter p = (xs.filter p).canonicalize id
```

`List.canonicalize_preserves_forallᵥ` (theorem, [line 544](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L544))

```lean
public theorem canonicalize_preserves_forallᵥ {α β γ} [LT α] [StrictLT α] [DecidableLT α] (p : β → γ → Prop) (kvs₁ : List (α × β)) (kvs₂ : List (α × γ)) :
  List.Forallᵥ p kvs₁ kvs₂ →
  List.Forallᵥ p (List.canonicalize Prod.fst kvs₁) (List.canonicalize Prod.fst kvs₂)
```

`List.canonicalize_of_map_fst` (theorem, [line 558](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L558))

```lean
public theorem canonicalize_of_map_fst {α β γ} [LT α] [StrictLT α] [DecidableLT α] (xs : List (α × β)) (f : β → γ) :
  List.canonicalize Prod.fst (List.map (Prod.map id f) xs) =
  List.map (Prod.map id f) (List.canonicalize Prod.fst xs)
```

`List.list_find?_in_tail` (theorem, [line 572](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L572))

> If the head of the list is not k, then finding in the tail
> returns the same result as finding the entire list.

```lean
public theorem list_find?_in_tail
  [LT β] [DecidableLT β] [BEq β] [LawfulBEq β] [StrictLT β]
  {f : α → β} {hd : α} {tl : List α} {k : β} :
  (f hd == k) = false →
  (List.canonicalize f (hd :: tl)).find? (λ x => f x == k) =
  (List.canonicalize f tl).find? (λ x => f x == k)
```

`List.list_find?_at_head` (theorem, [line 588](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L588))

> If the head of the list matches k, then finding in the canonicalized list
> returns that head element.

```lean
public theorem list_find?_at_head
  [LT β] [DecidableLT β] [BEq β] [LawfulBEq β] [StrictLT β]
  {f : α → β} {hd : α} {tl : List α} {k : β} :
  (f hd == k) = true →
  (List.canonicalize f (hd :: tl)).find? (λ x => f x == k) = some hd
```

> ### mergeCanonical

`List.mergeCanonical_nil_left` (theorem, [line 601](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L601))

```lean
public theorem mergeCanonical_nil_left [LT α] [DecidableLT α] (ys : List α) :
  mergeCanonical [] ys = ys
```

`List.mergeCanonical_nil_right` (theorem, [line 606](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L606))

```lean
public theorem mergeCanonical_nil_right [LT α] [DecidableLT α] (xs : List α) :
  mergeCanonical xs [] = xs
```

`List.mem_mergeCanonical` (theorem, [line 611](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L611))

> Membership in a merge does not require its inputs to be canonical.

```lean
public theorem mem_mergeCanonical [LT α] [DecidableLT α] [StrictLT α] {xs ys : List α} {a : α} :
  a ∈ mergeCanonical xs ys ↔ a ∈ xs ∨ a ∈ ys
```

`List.mergeCanonical_self` (theorem, [line 634](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L634))

> Merging a list with itself does not require the list to be canonical.

```lean
public theorem mergeCanonical_self [LT α] [DecidableLT α] [StrictLT α] (xs : List α) :
  mergeCanonical xs xs = xs
```

`List.mergeCanonical_comm` (theorem, [line 643](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L643))

> Merging is commutative even if its inputs are not canonical.

```lean
public theorem mergeCanonical_comm [LT α] [DecidableLT α] [StrictLT α] (xs ys : List α) :
  mergeCanonical xs ys = mergeCanonical ys xs
```

`List.mergeCanonical_assoc` (theorem, [line 675](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L675))

> Merging is associative even if its inputs are not canonical.

```lean
public theorem mergeCanonical_assoc [LT α] [DecidableLT α] [StrictLT α] (xs ys zs : List α) :
  mergeCanonical (mergeCanonical xs ys) zs = mergeCanonical xs (mergeCanonical ys zs)
```

`List.mergeCanonical_sortedBy` (theorem, [line 717](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean#L717))

```lean
public theorem mergeCanonical_sortedBy [LT α] [DecidableLT α] [StrictLT α] {xs ys : List α} :
  xs.SortedBy id → ys.SortedBy id → (mergeCanonical xs ys).SortedBy id
```

## Depends on

- [List properties](basic.md)

## Sources

- [Cedar/Thm/Data/List/Canonical.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/List/Canonical.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Data.List.Canonical.json)

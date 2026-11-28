---
catalog: module
lean: List.pairwise_iff_get, List.pwFilter_nil, List.pwFilter_cons_of_pos, List.pwFilter_cons_of_neg, List.pwFilter_map, List.pwFilter_sublist, List.pwFilter_subset, List.pairwise_pwFilter, List.pwFilter_eq_self, List.pwFilter_idem, List.forall_mem_pwFilter
statement: formalized
proof: formalized
---

# Pairwise relations on a list

`Batteries.Data.List.Pairwise`, in [Batteries/Data/List/Pairwise.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/List/Pairwise.lean), by Mario Carneiro, James Gallicchio.

> This file provides basic results about `List.Pairwise` and `List.pwFilter` (definitions are in
> `Batteries.Data.List.Basic`).
> `Pairwise r [a 0, ..., a (n - 1)]` means `∀ i j, i < j → r (a i) (a j)`. For example,
> `Pairwise (≠) l` means that all elements of `l` are distinct, and `Pairwise (<) l` means that `l`
> is strictly increasing.
> `pwFilter r l` is the list obtained by iteratively adding each element of `l` that doesn't break
> the pairwiseness of the list we have so far. It thus yields `l'` a maximal sublist of `l` such that
> `Pairwise r l'`.
>
> ## Tags
>
> sorted, nodup

> ### Pairwise

`List.pairwise_iff_get` (theorem, [line 36](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/List/Pairwise.lean#L36))

```lean
theorem pairwise_iff_get : Pairwise R l ↔ ∀ (i j) (_hij : i < j), R (get l i) (get l j)
```

> ### Pairwise filtering

`List.pwFilter_nil` (theorem, [line 46](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/List/Pairwise.lean#L46))

```lean
theorem pwFilter_nil [DecidableRel R] : pwFilter R [] = []
```

`List.pwFilter_cons_of_pos` (theorem, [line 48](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/List/Pairwise.lean#L48))

```lean
theorem pwFilter_cons_of_pos [DecidableRel (α := α) R] {a : α} {l : List α}
    (h : ∀ b ∈ pwFilter R l, R a b) : pwFilter R (a :: l) = a :: pwFilter R l
```

`List.pwFilter_cons_of_neg` (theorem, [line 51](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/List/Pairwise.lean#L51))

```lean
theorem pwFilter_cons_of_neg [DecidableRel (α := α) R] {a : α} {l : List α}
    (h : ¬∀ b ∈ pwFilter R l, R a b) : pwFilter R (a :: l) = pwFilter R l
```

`List.pwFilter_map` (theorem, [line 54](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/List/Pairwise.lean#L54))

```lean
theorem pwFilter_map [DecidableRel (α := α) R] (f : β → α) :
    ∀ l : List β, pwFilter R (map f l) = map f (pwFilter (fun x y => R (f x) (f y)) l)
```

`List.pwFilter_sublist` (theorem, [line 68](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/List/Pairwise.lean#L68))

```lean
theorem pwFilter_sublist [DecidableRel (α := α) R] : ∀ l : List α, pwFilter R l <+ l
```

`List.pwFilter_subset` (theorem, [line 76](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/List/Pairwise.lean#L76))

```lean
theorem pwFilter_subset [DecidableRel (α := α) R] (l : List α) : pwFilter R l ⊆ l
```

`List.pairwise_pwFilter` (theorem, [line 79](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/List/Pairwise.lean#L79))

```lean
theorem pairwise_pwFilter [DecidableRel (α := α) R] : ∀ l : List α, Pairwise R (pwFilter R l)
```

`List.pwFilter_eq_self` (theorem, [line 87](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/List/Pairwise.lean#L87))

```lean
theorem pwFilter_eq_self [DecidableRel (α := α) R] {l : List α} :
    pwFilter R l = l ↔ Pairwise R l
```

`List.pwFilter_idem` (theorem, [line 98](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/List/Pairwise.lean#L98))

```lean
theorem pwFilter_idem [DecidableRel (α := α) R] :
    pwFilter R (pwFilter R l) = pwFilter R l
```

`List.forall_mem_pwFilter` (theorem, [line 101](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/List/Pairwise.lean#L101))

```lean
theorem forall_mem_pwFilter [DecidableRel (α := α) R]
    (neg_trans : ∀ {x y z}, R x z → R x y ∨ R y z) (a : α) (l : List α) :
    (∀ b ∈ pwFilter R l, R a b) ↔ ∀ b ∈ l, R a b
```

## Depends on

- [List/Basic](basic.md)

## Sources

- [Batteries/Data/List/Pairwise.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/List/Pairwise.lean)
- [Declaration ledger](../../../../../../sources/batteries/Batteries.Data.List.Pairwise.json)

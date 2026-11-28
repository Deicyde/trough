---
catalog: module
lean: Array.Pairwise, Array.pairwise_iff_getElem, Array.pairwise_empty, Array.pairwise_singleton, Array.pairwise_pair, Array.pairwise_append, Array.pairwise_push, Array.pairwise_extract
statement: formalized
proof: formalized
---

# Pairwise

`Batteries.Data.Array.Pairwise`, in [Batteries/Data/Array/Pairwise.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Pairwise.lean), by François G. Dorais.

`Array.Pairwise` (definition, [line 21](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Pairwise.lean#L21))

> `Pairwise R as` means that all the elements of the array `as` are `R`-related to all elements with
> larger indices.
>
> `Pairwise R #[1, 2, 3] ↔ R 1 2 ∧ R 1 3 ∧ R 2 3`
>
> For example `as.Pairwise (· ≠ ·)` asserts that `as` has no duplicates, `as.Pairwise (· < ·)` asserts
> that `as` is strictly sorted and `as.Pairwise (· ≤ ·)` asserts that `as` is weakly sorted.

```lean
def Pairwise (R : α → α → Prop) (as : Array α) : Prop
```

`Array.pairwise_iff_getElem` (theorem, [line 23](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Pairwise.lean#L23))

```lean
theorem pairwise_iff_getElem {as : Array α} : as.Pairwise R ↔
    ∀ (i j : Nat) (_ : i < as.size) (_ : j < as.size), i < j → R as[i] as[j]
```

`Array.pairwise_empty` (theorem, [line 36](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Pairwise.lean#L36))

```lean
theorem pairwise_empty : #[].Pairwise R
```

`Array.pairwise_singleton` (theorem, [line 40](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Pairwise.lean#L40))

```lean
theorem pairwise_singleton (R : α → α → Prop) (a) : #[a].Pairwise R
```

`Array.pairwise_pair` (theorem, [line 44](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Pairwise.lean#L44))

```lean
theorem pairwise_pair : #[a, b].Pairwise R ↔ R a b
```

`Array.pairwise_append` (theorem, [line 48](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Pairwise.lean#L48))

```lean
theorem pairwise_append {as bs : Array α} :
    (as ++ bs).Pairwise R ↔ as.Pairwise R ∧ bs.Pairwise R ∧ (∀ x ∈ as, ∀ y ∈ bs, R x y)
```

`Array.pairwise_push` (theorem, [line 53](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Pairwise.lean#L53))

```lean
theorem pairwise_push {as : Array α} :
    (as.push a).Pairwise R ↔ as.Pairwise R ∧ (∀ x ∈ as, R x a)
```

`Array.pairwise_extract` (theorem, [line 59](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Pairwise.lean#L59))

```lean
theorem pairwise_extract {as : Array α} (h : as.Pairwise R) (start stop) :
    (as.extract start stop).Pairwise R
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/Array/Pairwise.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Array/Pairwise.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Array.Pairwise.json)

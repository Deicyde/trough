---
catalog: module
lean: List.length_partialSums, List.partialSums_ne_nil, List.partialSums_nil, List.partialSums_cons, List.partialSums_append, List.getElem_partialSums, List.getElem?_partialSums, List.take_partialSums, List.length_partialProds, List.partialProds_nil, List.partialProds_cons, List.partialProds_append, List.getElem_partialProds, List.getElem?_partialProds, List.take_partialProds, List.length_flatten_mem_partialSums_map_length, List.getElem_flatten_aux₁, List.getElem_flatten_aux₂, List.getElem_flatten
statement: formalized
proof: formalized
---

# List scan

`Batteries.Data.List.Scan`, in [Batteries/Data/List/Scan.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean), by Parikshit Khanna, Jeremy Avigad, Leonardo de Moura, Floris van Doorn, Mario Carneiro.

> Prove basic results about `List.scanl`, `List.scanr`, `List.scanlM` and `List.scanrM`.

> ### partialSums/partialProd

`List.length_partialSums` (theorem, [line 25](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L25))

```lean
theorem length_partialSums [Add α] [Zero α] {l : List α} :
    l.partialSums.length = l.length + 1
```

`List.partialSums_ne_nil` (theorem, [line 30](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L30))

```lean
theorem partialSums_ne_nil [Add α] [Zero α] {l : List α} :
    l.partialSums ≠ []
```

`List.partialSums_nil` (theorem, [line 34](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L34))

```lean
theorem partialSums_nil [Add α] [Zero α] : ([] : List α).partialSums = [0]
```

`List.partialSums_cons` (theorem, [line 37](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L37))

```lean
theorem partialSums_cons [Add α] [Zero α] [Std.Associative (α := α) (· + ·)]
    [Std.LawfulIdentity (α := α) (· + ·) 0] {l : List α} :
    (a :: l).partialSums = 0 :: l.partialSums.map (a + ·)
```

`List.partialSums_append` (theorem, [line 49](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L49))

```lean
theorem partialSums_append [Add α] [Zero α] [Std.Associative (α := α) (· + ·)]
    [Std.LawfulIdentity (α := α) (· + ·) 0] {l₁ l₂ : List α} :
    (l₁ ++ l₂).partialSums = l₁.partialSums ++ l₂.partialSums.tail.map (l₁.sum + · )
```

`List.getElem_partialSums` (theorem, [line 60](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L60))

```lean
theorem getElem_partialSums [Add α] [Zero α] [Std.Associative (α := α) (· + ·)]
    [Std.LawfulIdentity (α := α) (· + ·) 0] {l : List α} (h : i < l.partialSums.length) :
    l.partialSums[i] = (l.take i).sum
```

`List.getElem?_partialSums` (theorem, [line 66](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L66))

```lean
theorem getElem?_partialSums [Add α] [Zero α] [Std.Associative (α := α) (· + ·)]
    [Std.LawfulIdentity (α := α) (· + ·) 0] {l : List α} :
    l.partialSums[i]? = if i ≤ l.length then some (l.take i).sum else none
```

`List.take_partialSums` (theorem, [line 72](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L72))

```lean
theorem take_partialSums [Add α] [Zero α] {l : List α} :
    l.partialSums.take (i+1) = (l.take i).partialSums
```

`List.length_partialProds` (theorem, [line 77](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L77))

```lean
theorem length_partialProds [Mul α] [One α] {l : List α} :
    l.partialProds.length = l.length + 1
```

`List.partialProds_nil` (theorem, [line 82](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L82))

```lean
theorem partialProds_nil [Mul α] [One α]
  : ([] : List α).partialProds = [1]
```

`List.partialProds_cons` (theorem, [line 86](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L86))

```lean
theorem partialProds_cons [Mul α] [One α] [Std.Associative (α := α) (· * ·)]
    [Std.LawfulIdentity (α := α) (· * ·) 1] {l : List α} :
    (a :: l).partialProds = 1 :: l.partialProds.map (a * ·)
```

`List.partialProds_append` (theorem, [line 98](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L98))

```lean
theorem partialProds_append [Mul α] [One α] [Std.Associative (α := α) (· * ·)]
    [Std.LawfulIdentity (α := α) (· * ·) 1] {l₁ l₂ : List α} :
    (l₁ ++ l₂).partialProds = l₁.partialProds ++ l₂.partialProds.tail.map (l₁.prod * · )
```

`List.getElem_partialProds` (theorem, [line 109](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L109))

```lean
theorem getElem_partialProds [Mul α] [One α] [Std.Associative (α := α) (· * ·)]
    [Std.LawfulIdentity (α := α) (· * ·) 1] {l : List α} (h : i < l.partialProds.length) :
    l.partialProds[i] = (l.take i).prod
```

`List.getElem?_partialProds` (theorem, [line 115](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L115))

```lean
theorem getElem?_partialProds [Mul α] [One α] [Std.Associative (α := α) (· * ·)]
    [Std.LawfulIdentity (α := α) (· * ·) 1] {l : List α} :
    l.partialProds[i]? = if i ≤ l.length then some (l.take i).prod else none
```

`List.take_partialProds` (theorem, [line 121](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L121))

```lean
theorem take_partialProds [Mul α] [One α] {l : List α} :
    l.partialProds.take (i+1) = (l.take i).partialProds
```

> ### flatten

`List.length_flatten_mem_partialSums_map_length` (theorem, [line 127](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L127))

```lean
theorem length_flatten_mem_partialSums_map_length (L : List (List α)) :
    L.flatten.length ∈ (L.map length).partialSums
```

`List.getElem_flatten_aux₁` (theorem, [line 136](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L136))

```lean
theorem getElem_flatten_aux₁ (L : List (List α)) (i : Nat) (h : i < L.flatten.length) :
    (L.map length).partialSums.findIdx (· > i) - 1 < L.length
```

`List.getElem_flatten_aux₂` (theorem, [line 149](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L149))

```lean
theorem getElem_flatten_aux₂ (L : List (List α)) (i : Nat) (h : i < L.flatten.length) :
    let j := (L.map length).partialSums.findIdx (· > i) - 1
    have hj : j < L.length := getElem_flatten_aux₁ L i h
    let k := i - (L.take j).flatten.length
    k < L[j].length
```

`List.getElem_flatten` (theorem, [line 183](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean#L183))

> Indexing into a flattened list: `L.flatten[i]` equals `L[j][k]` where
> `j` is the sublist index and `k` is the offset within that sublist.
>
> The indices are computed as:
> - `j` is one less than where the cumulative sum first exceeds `i`
> - `k` is `i` minus the total length of the first `j` sublists
>
> This theorem states that these indices are in range and the equality holds.

```lean
theorem getElem_flatten (L : List (List α)) (i : Nat) (h : i < L.flatten.length) :
    L.flatten[i] =
      let j := (L.map length).partialSums.findIdx (· > i) - 1
      have hj : j < L.length := getElem_flatten_aux₁ L i h
      let k := i - (L.take j).flatten.length
      have hk : k < L[j].length := getElem_flatten_aux₂ L i h
      L[j][k]
```

## Depends on

- [List/Basic](../part-01/basic.md)

## Proof depends on

- [The `theorem_wanted`, `def_wanted`, and `instance_wanted` commands](../../../../util/proofwanted.md)

## Sources

- [Batteries/Data/List/Scan.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/Scan.lean)
- [Declaration ledger](../../../../../../sources/batteries/Batteries.Data.List.Scan.json)

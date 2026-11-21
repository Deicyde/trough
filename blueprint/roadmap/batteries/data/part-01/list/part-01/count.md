---
catalog: module
lean: List.count_singleton', List.count_concat, List.idxToSigmaCount, List.fst_idxToSigmaCount, List.snd_idxToSigmaCount, List.coe_snd_idxToSigmaCount, List.sigmaCountToIdx, List.coe_sigmaCountToIdx, List.sigmaCountToIdx_idxToSigmaCount, List.leftInverse_sigmaCountToIdx_idxToSigmaCount, List.rightInverse_idxToSigmaCount_sigmaCountToIdx, List.injective_idxToSigmaCount, List.surjective_sigmaCountToIdx, List.idxToSigmaCount_sigmaCountToIdx, List.leftInverse_idxToSigmaCount_sigmaCountToIdx, List.rightInverse_sigmaCountToIdx_idxToSigmaCount, List.injective_sigmaCountToIdx, List.surjective_idxToSigmaCount
statement: formalized
proof: formalized
---

# Counting in lists

`Batteries.Data.List.Count`, in [Batteries/Data/List/Count.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean), by Parikshit Khanna, Jeremy Avigad, Leonardo de Moura, Floris van Doorn, Mario Carneiro.

> This file proves basic properties of `List.countP` and `List.count`, which count the number of
> elements of a list satisfying a predicate and equal to a given element respectively. Their
> definitions can be found in `Batteries.Data.List.Basic`.

> ### count

`List.count_singleton'` (theorem, [line 29](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L29))

```lean
theorem count_singleton' [DecidableEq α] (a b : α) : count a [b] = if b = a then 1 else 0
```

`List.count_concat` (theorem, [line 32](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L32))

```lean
theorem count_concat [BEq α] [LawfulBEq α] (a : α) (l : List α) :
    count a (concat l a) = count a l + 1
```

> ### idxToSigmaCount, sigmaCountToIdx

`List.idxToSigmaCount` (definition, [line 50](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L50))

> `idxToSigmaCount` is essentially a `Fin`-to-`Fin` wrapper for `countBefore` that also
> includes the corresponding element.
>
> For example:
> ```
> idxToSigmaCount [5, 1, 3, 2, 4, 0, 1, 4] 5 = ⟨0, 0⟩
> ```

```lean
def idxToSigmaCount [BEq α] [ReflBEq α] (xs : List α) (i : Fin xs.length) :
    (x : α) × Fin (xs.count x)
```

`List.fst_idxToSigmaCount` (theorem, [line 54](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L54))

```lean
theorem fst_idxToSigmaCount [BEq α] [ReflBEq α] {xs: List α} {i : Fin xs.length} :
    (xs.idxToSigmaCount i).1 = xs[i.1]
```

`List.snd_idxToSigmaCount` (theorem, [line 58](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L58))

```lean
theorem snd_idxToSigmaCount [BEq α] [ReflBEq α] {xs: List α} {i : Fin xs.length} :
    (xs.idxToSigmaCount i).2 = ⟨xs.countBefore xs[i.1] i, by grind⟩
```

`List.coe_snd_idxToSigmaCount` (theorem, [line 62](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L62))

```lean
theorem coe_snd_idxToSigmaCount [BEq α] [ReflBEq α] {xs: List α} {i : Fin xs.length} :
    ((xs.idxToSigmaCount i).2 : Nat) = xs.countBefore xs[i.1] i
```

`List.sigmaCountToIdx` (definition, [line 72](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L72))

> `sigmaCountToIdx` is a `_ × Fin`-to-`Fin` wrapper for `countBefore`.
>
> For example:
> ```
> sigmaCountToIdx [5, 1, 3, 2, 4, 0, 1, 4] ⟨0, 0⟩ = 5
> ```

```lean
def sigmaCountToIdx [BEq α] (xs : List α) (xc : (x : α) × Fin (xs.count x)) :
    Fin xs.length
```

`List.coe_sigmaCountToIdx` (theorem, [line 76](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L76))

```lean
theorem coe_sigmaCountToIdx [BEq α] {xs: List α} {xc : (x : α) × Fin (xs.count x)} :
    (xs.sigmaCountToIdx xc : Nat) = xs.idxOfNth xc.1 xc.2
```

`List.sigmaCountToIdx_idxToSigmaCount` (theorem, [line 80](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L80))

```lean
theorem sigmaCountToIdx_idxToSigmaCount [BEq α] [ReflBEq α] {xs : List α}
    {i : Fin xs.length} : xs.sigmaCountToIdx (xs.idxToSigmaCount i) = i
```

`List.leftInverse_sigmaCountToIdx_idxToSigmaCount` (theorem, [line 83](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L83))

```lean
theorem leftInverse_sigmaCountToIdx_idxToSigmaCount [BEq α] [ReflBEq α] {xs : List α} :
  xs.sigmaCountToIdx.LeftInverse xs.idxToSigmaCount
```

`List.rightInverse_idxToSigmaCount_sigmaCountToIdx` (theorem, [line 86](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L86))

```lean
theorem rightInverse_idxToSigmaCount_sigmaCountToIdx [BEq α] [ReflBEq α] {xs : List α} :
  xs.idxToSigmaCount.RightInverse xs.sigmaCountToIdx
```

`List.injective_idxToSigmaCount` (theorem, [line 89](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L89))

```lean
theorem injective_idxToSigmaCount [BEq α] [ReflBEq α] {xs : List α} :
    xs.idxToSigmaCount.Injective
```

`List.surjective_sigmaCountToIdx` (theorem, [line 92](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L92))

```lean
theorem surjective_sigmaCountToIdx [BEq α] [ReflBEq α] {xs : List α} :
    xs.sigmaCountToIdx.Surjective
```

`List.idxToSigmaCount_sigmaCountToIdx` (theorem, [line 96](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L96))

```lean
theorem idxToSigmaCount_sigmaCountToIdx [BEq α] [LawfulBEq α] {xs : List α}
    {xc : (x : α) × Fin (xs.count x)} : xs.idxToSigmaCount (xs.sigmaCountToIdx xc) = xc
```

`List.leftInverse_idxToSigmaCount_sigmaCountToIdx` (theorem, [line 100](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L100))

```lean
theorem leftInverse_idxToSigmaCount_sigmaCountToIdx [BEq α] [LawfulBEq α] {xs : List α} :
  xs.idxToSigmaCount.LeftInverse xs.sigmaCountToIdx
```

`List.rightInverse_sigmaCountToIdx_idxToSigmaCount` (theorem, [line 103](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L103))

```lean
theorem rightInverse_sigmaCountToIdx_idxToSigmaCount [BEq α] [LawfulBEq α] {xs : List α} :
  xs.sigmaCountToIdx.RightInverse xs.idxToSigmaCount
```

`List.injective_sigmaCountToIdx` (theorem, [line 106](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L106))

```lean
theorem injective_sigmaCountToIdx [BEq α] [LawfulBEq α] {xs : List α} :
    xs.sigmaCountToIdx.Injective
```

`List.surjective_idxToSigmaCount` (theorem, [line 109](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean#L109))

```lean
theorem surjective_idxToSigmaCount [BEq α] [LawfulBEq α] {xs : List α} :
    xs.idxToSigmaCount.Surjective
```

## Depends on

- [List/Basic](basic.md)

## Proof depends on

- [List/Lemmas](lemmas.md)

## Sources

- [Batteries/Data/List/Count.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Count.lean)
- [Declaration ledger](../../../../../../sources/batteries/Batteries.Data.List.Count.json)

---
catalog: module
lean: Vector.allDiff, Vector.uset, Vector.scanlM, Vector.scanrM, Vector.scanl, Vector.scanr
statement: formalized
proof: formalized
---

# Vectors

`Batteries.Data.Vector.Basic`, in [Batteries/Data/Vector/Basic.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Vector/Basic.lean), by Shreyas Srinivas, François G. Dorais, Chad Sharp.

> `Vector α n` is a thin wrapper around `Array α` for arrays of fixed size `n`.

`Vector.allDiff` (definition, [line 23](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Vector/Basic.lean#L23))

> Returns `true` when all elements of the vector are pairwise distinct using `==` for comparison.

```lean
def allDiff [BEq α] (as : Vector α n) : Bool
```

`Vector.uset` (definition, [line 30](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Vector/Basic.lean#L30))

> Set an element of a vector using a `USize` index and a proof that the index is within bounds.

```lean
def uset (xs : Vector α n) (i : USize) (v : α) (h : i.toNat < n) : Vector α n
```

`Vector.scanlM` (definition, [line 75](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Vector/Basic.lean#L75))

> Fold an effectful function `f` over the array from the left, returning the list of partial results.

```lean
def scanlM [Monad m] (f : β → α → m β) (init : β) (as : Vector α n)
    : m (Vector β (n + 1))
```

`Vector.scanrM` (definition, [line 120](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Vector/Basic.lean#L120))

> Fold an effectful function `f` over the array from the right, returning the list of partial results.

```lean
def scanrM [Monad m] (f : α → β → m β) (init : β) (as : Vector α n) :
    m (Vector β (n + 1))
```

`Vector.scanl` (definition, [line 137](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Vector/Basic.lean#L137))

> Fold a function `f` over the list from the left, returning the vector of partial results.

```lean
def scanl (f : β → α → β) (init : β) (as : Vector α n) : Vector β (n + 1)
```

`Vector.scanr` (definition, [line 144](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Vector/Basic.lean#L144))

> Fold a function `f` over the list from the right, returning the vector of partial results.

```lean
def scanr (f : α → β → β) (init : β) (as : Vector α n) : Vector β (n + 1)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Proof depends on

- [UInt](../uint.md)

## Sources

- [Batteries/Data/Vector/Basic.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/Vector/Basic.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Vector.Basic.json)

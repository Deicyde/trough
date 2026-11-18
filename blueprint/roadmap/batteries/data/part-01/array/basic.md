---
catalog: module
lean: Array.equalSet, Array.rangeMinWith, Array.minWith, Array.rangeMinD, Array.minD, Array.rangeMin?, Array.rangeMinI, Array.minI, Array.rangeMaxWith, Array.maxWith, Array.rangeMaxD, Array.maxD, Array.rangeMax?, Array.rangeMaxI, Array.maxI, Array.setN, Array.scanlM, Array.scanrM, Array.scanl, Array.scanr, Subarray.scanlM, Subarray.scanrM, Subarray.scanl, Subarray.scanr, Subarray.isEmpty, Subarray.contains, Subarray.popHead?
statement: formalized
proof: formalized
---

# Array/Basic

`Batteries.Data.Array.Basic`, in [Batteries/Data/Array/Basic.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean), by Arthur Paulino, Floris van Doorn, Jannis Limperg.

> ## Definitions on Arrays
>
> This file contains various definitions on `Array`. It does not contain
> proofs about these definitions, those are contained in other files in `Batteries.Data.Array`.

`Array.equalSet` (definition, [line 27](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L27))

> Check whether `xs` and `ys` are equal as sets, i.e. they contain the same
> elements when disregarding order and duplicates. `O(n*m)`! If your element type
> has an `Ord` instance, it is asymptotically more efficient to sort the two
> arrays, remove duplicates and then compare them elementwise.

```lean
def equalSet [BEq α] (xs ys : Array α) : Bool
```

`Array.rangeMinWith` (definition, [line 36](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L36))

> Returns the first minimal element among `d` and elements of the array.
> If `start` and `stop` are given, only the subarray `xs[start...stop]` is
> considered (in addition to `d`).

```lean
protected def rangeMinWith [ord : Ord α]
    (xs : Array α) (d : α) (start := 0) (stop := xs.size) : α
```

`Array.minWith` (definition, [line 42](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L42))

```lean
protected def minWith
```

`Array.rangeMinD` (definition, [line 50](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L50))

> Find the first minimal element of an array. If the array is empty, `d` is
> returned. If `start` and `stop` are given, only the subarray `xs[start...stop]` is
> considered.

```lean
protected def rangeMinD [ord : Ord α]
    (xs : Array α) (d : α) (start := 0) (stop := xs.size) : α
```

`Array.minD` (definition, [line 58](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L58))

```lean
protected def minD
```

`Array.rangeMin?` (definition, [line 66](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L66))

> Find the first minimal element of an array. If the array is empty, `none` is
> returned. If `start` and `stop` are given, only the subarray `xs[start...stop]` is
> considered.

```lean
protected def rangeMin? [ord : Ord α]
    (xs : Array α) (start := 0) (stop := xs.size) : Option α
```

`Array.rangeMinI` (definition, [line 79](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L79))

> Find the first minimal element of an array. If the array is empty, `default` is
> returned. If `start` and `stop` are given, only the subarray `xs[start...stop]` is
> considered.

```lean
protected def rangeMinI [ord : Ord α] [Inhabited α]
    (xs : Array α) (start := 0) (stop := xs.size) : α
```

`Array.minI` (definition, [line 84](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L84))

```lean
protected def minI
```

`Array.rangeMaxWith` (definition, [line 92](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L92))

> Returns the first maximal element among `d` and elements of the array.
> If `start` and `stop` are given, only the subarray `xs[start...stop]` is
> considered (in addition to `d`).

```lean
protected def rangeMaxWith [ord : Ord α]
    (xs : Array α) (d : α) (start := 0) (stop := xs.size) : α
```

`Array.maxWith` (definition, [line 97](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L97))

```lean
protected def maxWith
```

`Array.rangeMaxD` (definition, [line 105](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L105))

> Find the first maximal element of an array. If the array is empty, `d` is
> returned. If `start` and `stop` are given, only the subarray `xs[start...stop]` is
> considered.

```lean
protected def rangeMaxD [ord : Ord α]
    (xs : Array α) (d : α) (start := 0) (stop := xs.size) : α
```

`Array.maxD` (definition, [line 110](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L110))

```lean
protected def maxD
```

`Array.rangeMax?` (definition, [line 118](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L118))

> Find the first maximal element of an array. If the array is empty, `none` is
> returned. If `start` and `stop` are given, only the subarray `xs[start...stop]` is
> considered.

```lean
protected def rangeMax? [ord : Ord α]
    (xs : Array α) (start := 0) (stop := xs.size) : Option α
```

`Array.rangeMaxI` (definition, [line 128](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L128))

> Find the first maximal element of an array. If the array is empty, `default` is
> returned. If `start` and `stop` are given, only the subarray `xs[start...stop]` is
> considered.

```lean
protected def rangeMaxI [ord : Ord α] [Inhabited α]
    (xs : Array α) (start := 0) (stop := xs.size) : α
```

`Array.maxI` (definition, [line 133](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L133))

```lean
protected def maxI
```

`Array.setN` (alias, [line 136](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L136))

```lean
alias setN
```

`Array.scanlM` (definition, [line 205](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L205))

> Folds a monadic function over an array from the left, accumulating the partial results starting with
> `init`. The accumulated value is combined with the each element of the list in order, using `f`.
>
> The optional parameters `start` and `stop` control the region of the array to be folded. Folding
> proceeds from `start` (inclusive) to `stop` (exclusive), so no folding occurs unless `start < stop`.
> By default, the entire array is folded.
>
> Examples:
> ```lean example
> example [Monad m] (f : α → β → m α) :
>     Array.scanlM f x₀ #[a, b, c] = (do
>       let x₁ ← f x₀ a
>       let x₂ ← f x₁ b
>       let x₃ ← f x₂ c
>       pure #[x₀, x₁, x₂, x₃])
>     := by simp [scanlM, scanlM.loop]
> ```
>
> ```lean example
> example [Monad m] (f : α → β → m α) :
>     Array.scanlM f x₀ #[a, b, c] (start := 1) (stop := 3) = (do
>       let x₁ ← f x₀ b
>       let x₂ ← f x₁ c
>       pure #[x₀, x₁, x₂])
>     := by simp [scanlM, scanlM.loop]
> ```

```lean
def scanlM [Monad m] (f : β → α → m β) (init : β) (as : Array α) (start := 0)
    (stop := as.size) : m (Array β)
```

`Array.scanrM` (definition, [line 331](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L331))

> Folds a monadic function over an array from the right, accumulating the partial results starting
> with `init`. The accumulated value is combined with the each element of the list in order using `f`.
>
> The optional parameters `start` and `stop` control the region of the array to be folded. Folding
> proceeds from `start` (exclusive) to `stop` (inclusive), so no folding occurs unless `start > stop`.
> By default, the entire array is folded.
>
> Examples:
> ```lean example
> example [Monad m] (f : α → β → m β) :
>     Array.scanrM f x₀ #[a, b, c] = (do
>       let x₁ ← f c x₀
>       let x₂ ← f b x₁
>       let x₃ ← f a x₂
>       pure #[x₃, x₂, x₁, x₀])
>     := by simp [scanrM, scanrM.loop]
> ```
>
> ```lean example
> example [Monad m] (f : α → β → m β) :
>     Array.scanrM f x₀ #[a, b, c] (start := 3) (stop := 1) = (do
>       let x₁ ← f c x₀
>       let x₂ ← f b x₁
>       pure #[x₂, x₁, x₀])
>     := by simp [scanrM, scanrM.loop]
> ```

```lean
def scanrM [Monad m]
    (f : α → β → m β) (init : β) (as : Array α) (start := as.size) (stop := 0) : m (Array β)
```

`Array.scanl` (definition, [line 356](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L356))

> Fold a function `f` over the array from the left, returning the array of partial results.
> ```
> scanl (· + ·) 0 #[1, 2, 3] = #[0, 1, 3, 6]
> ```

```lean
def scanl (f : β → α → β) (init : β) (as : Array α) (start := 0) (stop := as.size) : Array β
```

`Array.scanr` (definition, [line 366](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L366))

> Fold a function `f` over the array from the right, returning the array of partial results.
> ```
> scanr (· + ·) 0 #[1, 2, 3] = #[6, 5, 3, 0]
> ```

```lean
def scanr (f : α → β → β) (init : β) (as : Array α) (start := as.size) (stop := 0) : Array β
```

`Subarray.scanlM` (definition, [line 377](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L377))

> Fold a monadic function `f` over the subarray from the left, returning the list of partial results.

```lean
def scanlM [Monad m] (f : β → α → m β) (init : β) (as : Subarray α) : m (Array β)
```

`Subarray.scanrM` (definition, [line 384](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L384))

> Fold a monadic function `f` over the subarray from the right, returning the list of partial results.

```lean
def scanrM [Monad m] (f : α → β → m β) (init : β) (as : Subarray α) : m (Array β)
```

`Subarray.scanl` (definition, [line 391](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L391))

> Fold a function `f` over the subarray from the left, returning the list of partial results.

```lean
def scanl (f : β → α → β) (init : β) (as : Subarray α) : Array β
```

`Subarray.scanr` (definition, [line 398](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L398))

> Fold a function `f` over the subarray from the right, returning the list of partial results.

```lean
def scanr (f : α → β → β) (init : β) (as : Subarray α) : Array β
```

`Subarray.isEmpty` (definition, [line 405](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L405))

> Check whether a subarray is empty.

```lean
def isEmpty (as : Subarray α) : Bool
```

`Subarray.contains` (definition, [line 412](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L412))

> Check whether a subarray contains a given element.

```lean
def contains [BEq α] (as : Subarray α) (a : α) : Bool
```

`Subarray.popHead?` (definition, [line 419](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean#L419))

> Remove the first element of a subarray. Returns the element and the remaining
> subarray, or `none` if the subarray is empty.

```lean
def popHead? (as : Subarray α) : Option (α × Subarray α)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Proof depends on

- [UInt](../../part-02/uint.md)

## Sources

- [Batteries/Data/Array/Basic.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Basic.lean)

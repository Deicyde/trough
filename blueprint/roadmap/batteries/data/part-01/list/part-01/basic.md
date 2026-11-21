---
catalog: module
lean: List.max!, List.min!, List.bagInter, List.diff, List.next?, List.after, List.replaceF, List.replaceFTR, List.replaceF_eq_replaceFTR, List.union, List.inter, List.splitAtD, List.modifyLast, List.headD_eq_head?, List.takeD, List.takeD_zero, List.takeD_succ, List.takeD_nil, List.takeDTR, List.takeDTR_go_eq, List.takeD_eq_takeDTR, List.scanAuxM, List.foldlIdx, List.foldrIdx, List.foldrIdxTR, List.foldrIdx_eq_foldrIdxTR, List.findIdxs, List.findIdxsValues, List.findIdxNth, List.idxsOf, List.idxOfNth, List.countPBefore, List.countBefore, List.lookmap, List.inits, List.initsTR, List.inits_eq_initsTR, List.tails, List.tailsTR, List.tails_eq_tailsTR, List.sublists', List.sublists, List.sublistsFast, List.sublists_eq_sublistsFast, List.Forall₂, List.forall₂_cons, List.all₂, List.all₂_eq_true, List.transpose, List.sections, List.sectionsTR, List.sections_eq_nil_of_isEmpty, List.sections_eq_sectionsTR, List.extractP, List.revzip, List.product, List.productTR, List.product_eq_productTR, List.sigma, List.sigmaTR, List.sigma_eq_sigmaTR, List.ofFnNthVal, List.Disjoint, List.takeWhile₂, List.takeWhile₂TR, List.takeWhile₂_eq_takeWhile₂TR, List.pwFilter, List.IsChain, List.isChain_cons_cons, List.eraseDup, List.rotate, List.rotate', List.mapDiagM, List.forDiagM, List.getRest, List.dropSlice, List.dropSliceTR, List.dropSlice_zero₂, List.dropSlice_eq_dropSliceTR, List.zipWithLeft', List.zipWithLeft'TR, List.zipWithLeft'_eq_zipWithLeft'TR, List.zipWithRight', List.zipLeft', List.zipRight', List.zipWithLeft, List.zipWithLeftTR, List.zipWithLeft_eq_zipWithLeftTR, List.zipWithRight, List.zipLeft, List.zipRight, List.allSome, List.takeList, List.takeListTR, List.takeList_eq_takeListTR, List.toChunksAux, List.toChunks, List.zipWith₃, List.zipWith₄, List.zipWith₅, List.mapWithPrefixSuffixAux, List.mapWithPrefixSuffix, List.mapWithComplement, List.traverse, List.Subperm, List.isSubperm, List.insertP, List.dropPrefix?, List.dropSuffix?, List.dropInfix?, List.partialSums, List.partialProds, List.swapAt, List.swapAtTR, List.swapAt_eq_swapAtTR, List.swap, List.swapTR, List.swap_eq_swapTR
statement: formalized
proof: formalized
---

# List/Basic

`Batteries.Data.List.Basic`, in [Batteries/Data/List/Basic.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean), by Leonardo de Moura.

> ## New definitions

`List.max!` (definition, [line 17](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L17))

> Get the maximum element of a list.
> If the given list is empty, returns `(default : α)` and produces a panic error message.

```lean
def max! {α} [Inhabited α] [Max α] (xs : List α) : α
```

`List.min!` (definition, [line 24](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L24))

> Get the minimum element of a list.
> If the given list is empty, returns `(default : α)` and produces a panic error message.

```lean
def min! {α} [Inhabited α] [Min α] (xs : List α) : α
```

`List.bagInter` (definition, [line 34](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L34))

> Computes the "bag intersection" of `l₁` and `l₂`, that is,
> the collection of elements of `l₁` which are also in `l₂`. As each element
> is identified, it is removed from `l₂`, so elements are counted with multiplicity.

```lean
protected def bagInter {α} [BEq α] : List α → List α → List α
```

`List.diff` (definition, [line 40](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L40))

> Computes the difference of `l₁` and `l₂`, by removing each element in `l₂` from `l₁`.

```lean
protected def diff {α} [BEq α] : List α → List α → List α
```

`List.next?` (definition, [line 47](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L47))

> Get the head and tail of a list, if it is nonempty.

```lean
def next? : List α → Option (α × List α)
```

`List.after` (definition, [line 59](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L59))

> `after p xs` is the suffix of `xs` after the first element that satisfies
> `p`, not including that element.
> ```lean
> after      (· == 1) [0, 1, 2, 3] = [2, 3]
> drop_while (· != 1) [0, 1, 2, 3] = [1, 2, 3]
> ```

```lean
def after (p : α → Bool) : List α → List α
```

`List.replaceF` (definition, [line 64](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L64))

> Replaces the first element of the list for which `f` returns `some` with the returned value.

```lean
def replaceF (f : α → Option α) : List α → List α
```

`List.replaceFTR` (definition, [line 71](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L71))

> Tail-recursive version of `replaceF`.

```lean
def replaceFTR (f : α → Option α) (l : List α) : List α
```

`List.replaceF_eq_replaceFTR` (theorem, [line 79](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L79))

```lean
theorem replaceF_eq_replaceFTR : @replaceF = @replaceFTR
```

`List.union` (definition, [line 93](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L93))

> Constructs the union of two lists, by inserting the elements of `l₁` in reverse order to `l₂`.
> As a result, `l₂` will always be a suffix, but only the last occurrence of each element in `l₁`
> will be retained (but order will otherwise be preserved).

```lean
protected def union [BEq α] (l₁ l₂ : List α) : List α
```

`List.inter` (definition, [line 101](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L101))

> Constructs the intersection of two lists, by filtering the elements of `l₁` that are in `l₂`.
> Unlike `bagInter` this does not preserve multiplicity: `[1, 1].inter [1]` is `[1, 1]`.

```lean
protected def inter [BEq α] (l₁ l₂ : List α) : List α
```

`List.splitAtD` (definition, [line 113](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L113))

> Split a list at an index. Ensures the left list always has the specified length
> by right padding with the provided default element.
> ```
> splitAtD 2 [a, b, c] x = ([a, b], [c])
> splitAtD 4 [a, b, c] x = ([a, b, c, x], [])
> ```

```lean
def splitAtD (n : Nat) (l : List α) (dflt : α) : List α × List α
```

`List.modifyLast` (definition, [line 122](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L122))

> Apply `f` to the last element of `l`, if it exists.

```lean
def modifyLast (f : α → α) (l : List α) : List α
```

`List.headD_eq_head?` (theorem, [line 129](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L129))

```lean
theorem headD_eq_head? (l) (a : α) : headD l a = (head? l).getD a
```

`List.takeD` (definition, [line 135](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L135))

> Take `n` elements from a list `l`. If `l` has less than `n` elements, append `n - length l`
> elements `x`.

```lean
def takeD : Nat → List α → α → List α
```

`List.takeD_zero` (theorem, [line 139](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L139))

```lean
theorem takeD_zero (l) (a : α) : takeD 0 l a = []
```

`List.takeD_succ` (theorem, [line 140](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L140))

```lean
theorem takeD_succ (l) (a : α) :
    takeD (n+1) l a = l.head?.getD a :: takeD n l.tail a
```

`List.takeD_nil` (theorem, [line 143](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L143))

```lean
theorem takeD_nil (n) (a : α) : takeD n [] a = replicate n a
```

`List.takeDTR` (definition, [line 147](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L147))

> Tail-recursive version of `takeD`.

```lean
def takeDTR (n : Nat) (l : List α) (dflt : α) : List α
```

`List.takeDTR_go_eq` (theorem, [line 154](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L154))

```lean
theorem takeDTR_go_eq : ∀ n l, takeDTR.go dflt n l acc = acc.toList ++ takeD n l dflt
```

`List.takeD_eq_takeDTR` (theorem, [line 159](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L159))

```lean
theorem takeD_eq_takeDTR : @takeD = @takeDTR
```

`List.scanAuxM` (definition, [line 165](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L165))

> Tail-recursive helper function for `scanlM` and `scanrM`

```lean
def scanAuxM [Monad m] (f : β → α → m β) (init : β) (l : List α) : m (List β)
```

`List.foldlIdx` (definition, [line 179](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L179))

> Fold a list from left to right as with `foldl`, but the combining function
> also receives each element's index added to an optional parameter `start`
> (i.e. the numbers that `f` takes as its first argument will be greater than or equal to `start` and
> less than `start + l.length`).

```lean
def foldlIdx (f : Nat → α → β → α) (init : α) :
    List β → (start : Nat := 0) → α
```

`List.foldrIdx` (definition, [line 190](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L190))

> Fold a list from right to left as with `foldr`, but the combining function
> also receives each element's index added to an optional parameter `start`
> (i.e. the numbers that `f` takes as its first argument will be greater than or equal to `start` and
> less than `start + l.length`).

```lean
def foldrIdx {α : Type u} {β : Type v} (f : Nat → α → β → β) (init : β) :
    (l : List α) → (start : Nat := 0) → β
```

`List.foldrIdxTR` (definition, [line 196](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L196))

> A tail-recursive version of `foldrIdx`.

```lean
def foldrIdxTR (f : Nat → α → β → β) (init : β) (l : List α) (start : Nat := 0) : β
```

`List.foldrIdx_eq_foldrIdxTR` (theorem, [line 199](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L199))

```lean
theorem foldrIdx_eq_foldrIdxTR : @foldrIdx = @foldrIdxTR
```

`List.findIdxs` (definition, [line 208](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L208))

> `findIdxs p l s` is the list of indexes of elements of `l` that satisfy `p`, added to an
> optional parameter `s` (so that the members of `findIdxs p l s` will be greater than or
> equal to `s` and less than `l.length + s`).

```lean
def findIdxs (p : α → Bool) (l : List α) (start : Nat := 0) : List Nat
```

`List.findIdxsValues` (definition, [line 217](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L217))

> Returns the elements of `l` that satisfy `p` together with their indexes in
> `l` added to an optional parameter `start`. The returned list is ordered by index.
> We have `l.findIdxsValues p s = (l.findIdxs p s).zip (l.filter p)`.

```lean
def findIdxsValues (p : α → Bool) (l : List α) (start : Nat := 0) : List (Nat × α)
```

`List.findIdxNth` (definition, [line 226](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L226))

> `findIdxNth p xs n` returns the index of the `n`th element for which `p` returns `true`.
> For example:
> ```
> findIdxNth (· < 3) [5, 1, 3, 2, 4, 0, 1, 4] 2 = 5
> ```

```lean
def findIdxNth (p : α → Bool) (xs : List α) (n : Nat) : Nat
```

`List.idxsOf` (definition, [line 241](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L241))

> `idxsOf a l s` is the list of all indexes of `a` in `l`,  added to an
> optional parameter `s`. For example:
> ```
> idxsOf b [a, b, a, a] = [1]
> idxsOf a [a, b, a, a] 5 = [5, 7, 8]
> ```

```lean
def idxsOf [BEq α] (a : α) (xs : List α) (start : Nat := 0) : List Nat
```

`List.idxOfNth` (definition, [line 251](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L251))

> `idxOfNth a xs n` returns the index of the `n`th instance of `a` in `xs`, counting from `0`.
>
> For example:
> ```
> idxOfNth 1 [5, 1, 3, 2, 4, 0, 1, 4] 1 = 6
> ```

```lean
def idxOfNth [BEq α] (a : α) (xs : List α) (n : Nat) : Nat
```

`List.countPBefore` (definition, [line 262](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L262))

> `countPBefore p xs i hip` counts the number of `x` in `xs` before the `i`th index for
> which `p x = true`.
>
> For example:
> ```
> countPBefore (· < 3) [5, 1, 3, 2, 4, 0, 1, 4] 5 = 2
> ```

```lean
def countPBefore (p : α → Bool) (xs : List α) (i : Nat) : Nat
```

`List.countBefore` (definition, [line 277](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L277))

> `countBefore a xs n` counts the number of `x` in `xs` before the
> `i`th index for which `x == a` is true.
>
> For example:
> ```
> countBefore 1 [5, 1, 3, 2, 4, 0, 1, 4] 6 = 1
> ```

```lean
def countBefore [BEq α] (a : α) : List α → Nat → Nat
```

`List.lookmap` (definition, [line 285](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L285))

> `lookmap` is a combination of `lookup` and `filterMap`.
> `lookmap f l` will apply `f : α → Option α` to each element of the list,
> replacing `a → b` at the first value `a` in the list such that `f a = some b`.

```lean
def lookmap (f : α → Option α) (l : List α) : List α
```

`List.inits` (definition, [line 299](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L299))

> `inits l` is the list of initial segments of `l`.
> ```
> inits [1, 2, 3] = [[], [1], [1, 2], [1, 2, 3]]
> ```

```lean
def inits : List α → List (List α)
```

`List.initsTR` (definition, [line 304](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L304))

> Tail-recursive version of `inits`.

```lean
def initsTR (l : List α) : List (List α)
```

`List.inits_eq_initsTR` (theorem, [line 307](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L307))

```lean
theorem inits_eq_initsTR : @inits = @initsTR
```

`List.tails` (definition, [line 316](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L316))

> `tails l` is the list of terminal segments of `l`.
> ```
> tails [1, 2, 3] = [[1, 2, 3], [2, 3], [3], []]
> ```

```lean
def tails : List α → List (List α)
```

`List.tailsTR` (definition, [line 321](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L321))

> Tail-recursive version of `tails`.

```lean
def tailsTR (l : List α) : List (List α)
```

`List.tails_eq_tailsTR` (theorem, [line 328](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L328))

```lean
theorem tails_eq_tailsTR : @tails = @tailsTR
```

`List.sublists'` (definition, [line 343](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L343))

> `sublists' l` is the list of all (non-contiguous) sublists of `l`.
> It differs from `sublists` only in the order of appearance of the sublists;
> `sublists'` uses the first element of the list as the MSB,
> `sublists` uses the first element of the list as the LSB.
> ```
> sublists' [1, 2, 3] = [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
> ```

```lean
def sublists' (l : List α) : List (List α)
```

`List.sublists` (definition, [line 354](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L354))

> `sublists l` is the list of all (non-contiguous) sublists of `l`; cf. `sublists'`
> for a different ordering.
> ```
> sublists [1, 2, 3] = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
> ```

```lean
def sublists (l : List α) : List (List α)
```

`List.sublistsFast` (definition, [line 358](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L358))

> A version of `List.sublists` that has faster runtime performance but worse kernel performance

```lean
def sublistsFast (l : List α) : List (List α)
```

`List.sublists_eq_sublistsFast` (theorem, [line 363](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L363))

```lean
theorem sublists_eq_sublistsFast : @sublists = @sublistsFast
```

`List.Forall₂` (inductive type, [line 377](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L377))

> `Forall₂ R l₁ l₂` means that `l₁` and `l₂` have the same length,
> and whenever `a` is the nth element of `l₁`, and `b` is the nth element of `l₂`,
> then `R a b` is satisfied.

```lean
inductive Forall₂ (R : α → β → Prop) : List α → List β → Prop
  /-- Two nil lists are `Forall₂`-related -/
  | nil : Forall₂ R [] []
  /-- Two cons lists are related by `Forall₂ R`
  if the heads are related by `R` and the tails are related by `Forall₂ R` -/
  | cons {a b l₁ l₂} : R a b → Forall₂ R l₁ l₂ → Forall₂ R (a :: l₁) (b :: l₂)
```

`List.forall₂_cons` (theorem, [line 386](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L386))

```lean
theorem forall₂_cons {R : α → β → Prop} {a b l₁ l₂} :
    Forall₂ R (a :: l₁) (b :: l₂) ↔ R a b ∧ Forall₂ R l₁ l₂
```

`List.all₂` (definition, [line 394](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L394))

> Check for all elements `a`, `b`, where `a` and `b` are the nth element of the first and second
> List respectively, that `r a b = true`.

```lean
def all₂ (r : α → β → Bool) : List α → List β → Bool
```

`List.all₂_eq_true` (theorem, [line 402](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L402))

```lean
theorem all₂_eq_true {r : α → β → Bool} :
    ∀ l₁ l₂, all₂ r l₁ l₂ ↔ Forall₂ (r · ·) l₁ l₂
```

`List.transpose` (definition, [line 423](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L423))

> Transpose of a list of lists, treated as a matrix.
> ```
> transpose [[1, 2], [3, 4], [5, 6]] = [[1, 3, 5], [2, 4, 6]]
> ```

```lean
def transpose (l : List (List α)) : List (List α)
```

`List.sections` (definition, [line 450](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L450))

> List of all sections through a list of lists. A section
> of `[L₁, L₂, ..., Lₙ]` is a list whose first element comes from
> `L₁`, whose second element comes from `L₂`, and so on.

```lean
def sections : List (List α) → List (List α)
```

`List.sectionsTR` (definition, [line 455](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L455))

> Optimized version of `sections`.

```lean
def sectionsTR (L : List (List α)) : List (List α)
```

`List.sections_eq_nil_of_isEmpty` (theorem, [line 465](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L465))

```lean
theorem sections_eq_nil_of_isEmpty : ∀ {L}, L.any isEmpty → @sections α L = []
```

`List.sections_eq_sectionsTR` (theorem, [line 472](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L472))

```lean
theorem sections_eq_sectionsTR : @sections = @sectionsTR
```

`List.extractP` (definition, [line 483](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L483))

> `extractP p l` returns a pair of an element `a` of `l` satisfying the predicate
> `p`, and `l`, with `a` removed. If there is no such element `a` it returns `(none, l)`.

```lean
def extractP (p : α → Bool) (l : List α) : Option α × List α
```

`List.revzip` (definition, [line 498](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L498))

> `revzip l` returns a list of pairs of the elements of `l` paired
> with the elements of `l` in reverse order.
> ```
> revzip [1, 2, 3, 4, 5] = [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)]
> ```

```lean
def revzip (l : List α) : List (α × α)
```

`List.product` (definition, [line 507](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L507))

> `product l₁ l₂` is the list of pairs `(a, b)` where `a ∈ l₁` and `b ∈ l₂`.
> ```
> product [1, 2] [5, 6] = [(1, 5), (1, 6), (2, 5), (2, 6)]
> ```

```lean
def product (l₁ : List α) (l₂ : List β) : List (α × β)
```

`List.productTR` (definition, [line 510](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L510))

> Optimized version of `product`.

```lean
def productTR (l₁ : List α) (l₂ : List β) : List (α × β)
```

`List.product_eq_productTR` (theorem, [line 513](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L513))

```lean
theorem product_eq_productTR : @product = @productTR
```

`List.sigma` (definition, [line 523](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L523))

> `sigma l₁ l₂` is the list of dependent pairs `(a, b)` where `a ∈ l₁` and `b ∈ l₂ a`.
> ```
> sigma [1, 2] (λ_, [(5 : Nat), 6]) = [(1, 5), (1, 6), (2, 5), (2, 6)]
> ```

```lean
protected def sigma {σ : α → Type _} (l₁ : List α) (l₂ : ∀ a, List (σ a)) : List (Σ a, σ a)
```

`List.sigmaTR` (definition, [line 527](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L527))

> Optimized version of `sigma`.

```lean
def sigmaTR {σ : α → Type _} (l₁ : List α) (l₂ : ∀ a, List (σ a)) : List (Σ a, σ a)
```

`List.sigma_eq_sigmaTR` (theorem, [line 530](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L530))

```lean
theorem sigma_eq_sigmaTR : @List.sigma = @sigmaTR
```

`List.ofFnNthVal` (definition, [line 536](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L536))

> `ofFnNthVal f i` returns `some (f i)` if `i < n` and `none` otherwise.

```lean
def ofFnNthVal {n} (f : Fin n → α) (i : Nat) : Option α
```

`List.Disjoint` (definition, [line 540](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L540))

> `Disjoint l₁ l₂` means that `l₁` and `l₂` have no elements in common.

```lean
def Disjoint (l₁ l₂ : List α) : Prop
```

`List.takeWhile₂` (definition, [line 549](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L549))

> Returns the longest initial prefix of two lists such that they are pairwise related by `R`.
> ```
> takeWhile₂ (· < ·) [1, 2, 4, 5] [5, 4, 3, 6] = ([1, 2], [5, 4])
> ```

```lean
def takeWhile₂ (R : α → β → Bool) : List α → List β → List α × List β
```

`List.takeWhile₂TR` (definition, [line 557](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L557))

> Tail-recursive version of `takeWhile₂`.

```lean
def takeWhile₂TR (R : α → β → Bool) (as : List α) (bs : List β) : List α × List β
```

`List.takeWhile₂_eq_takeWhile₂TR` (theorem, [line 568](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L568))

```lean
theorem takeWhile₂_eq_takeWhile₂TR : @takeWhile₂ = @takeWhile₂TR
```

`List.pwFilter` (definition, [line 584](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L584))

> `pwFilter R l` is a maximal sublist of `l` which is `Pairwise R`.
> `pwFilter (·≠·)` is the erase duplicates function (cf. `eraseDups`), and `pwFilter (·<·)` finds
> a maximal increasing subsequence in `l`. For example,
> ```
> pwFilter (·<·) [0, 1, 5, 2, 6, 3, 4] = [0, 1, 2, 3, 4]
> ```

```lean
def pwFilter (R : α → α → Prop) [DecidableRel R] (l : List α) : List α
```

`List.IsChain` (inductive type, [line 593](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L593))

> `IsChain R l` means that `R` holds between adjacent elements of `l`. Example:
> ```
> IsChain R [a, b, c, d] ↔ R a b ∧ R b c ∧ R c d
> ```

```lean
inductive IsChain (R : α → α → Prop) : List α → Prop where
  /-- A list of length 0 is a chain. -/
  | nil : IsChain R []
  /-- A list of length 1 is a chain. -/
  | singleton (a : α) : IsChain R [a]
  /-- If `a` relates to `b` and `b::l` is a chain, then `a :: b :: l` is also a chain. -/
  | cons_cons (hr : R a b) (h : IsChain R (b :: l)) : IsChain R (a :: b :: l)
```

`List.isChain_cons_cons` (theorem, [line 604](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L604))

```lean
theorem isChain_cons_cons : IsChain R (a :: b :: l) ↔ R a b ∧ IsChain R (b :: l)
```

`List.eraseDup` (abbreviation, [line 617](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L617))

> **Deprecated:** Use `reverse ∘ eraseDups ∘ reverse` or just `eraseDups` instead.

```lean
abbrev eraseDup [BEq α] : List α → List α
```

`List.rotate` (definition, [line 625](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L625))

> `rotate l n` rotates the elements of `l` to the left by `n`
> ```
> rotate [0, 1, 2, 3, 4, 5] 2 = [2, 3, 4, 5, 0, 1]
> ```

```lean
def rotate (l : List α) (n : Nat) : List α
```

`List.rotate'` (definition, [line 630](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L630))

> `rotate'` is the same as `rotate`, but slower. Used for proofs about `rotate`

```lean
def rotate' : List α → Nat → List α
```

`List.mapDiagM` (definition, [line 644](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L644))

> `mapDiagM f l` calls `f` on all elements in the upper triangular part of `l × l`.
> That is, for each `e ∈ l`, it will run `f e e` and then `f e e'`
> for each `e'` that appears after `e` in `l`.
> ```
> mapDiagM f [1, 2, 3] =
>   return [← f 1 1, ← f 1 2, ← f 1 3, ← f 2 2, ← f 2 3, ← f 3 3]
> ```

```lean
def mapDiagM [Monad m] (f : α → α → m β) (l : List α) : m (List β)
```

`List.forDiagM` (definition, [line 661](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L661))

> `forDiagM f l` calls `f` on all elements in the upper triangular part of `l × l`.
> That is, for each `e ∈ l`, it will run `f e e` and then `f e e'`
> for each `e'` that appears after `e` in `l`.
> ```
> forDiagM f [1, 2, 3] = do f 1 1; f 1 2; f 1 3; f 2 2; f 2 3; f 3 3
> ```

```lean
def forDiagM [Monad m] (f : α → α → m PUnit) : List α → m PUnit
```

`List.getRest` (definition, [line 667](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L667))

> `getRest l l₁` returns `some l₂` if `l = l₁ ++ l₂`.
> If `l₁` is not a prefix of `l`, returns `none`

```lean
def getRest [DecidableEq α] : List α → List α → Option (List α)
```

`List.dropSlice` (definition, [line 673](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L673))

> `List.dropSlice n m xs` removes a slice of length `m` at index `n` in list `xs`.

```lean
def dropSlice : Nat → Nat → List α → List α
```

`List.dropSliceTR` (definition, [line 679](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L679))

> Optimized version of `dropSlice`.

```lean
def dropSliceTR (n m : Nat) (l : List α) : List α
```

`List.dropSlice_zero₂` (theorem, [line 691](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L691))

```lean
theorem dropSlice_zero₂ : ∀ n l, @dropSlice α n 0 l = l
```

`List.dropSlice_eq_dropSliceTR` (theorem, [line 695](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L695))

```lean
theorem dropSlice_eq_dropSliceTR : @dropSlice = @dropSliceTR
```

`List.zipWithLeft'` (definition, [line 716](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L716))

> Left-biased version of `List.zipWith`. `zipWithLeft' f as bs` applies `f` to each
> pair of elements `aᵢ ∈ as` and `bᵢ ∈ bs`. If `bs` is shorter than `as`, `f` is
> applied to `none` for the remaining `aᵢ`. Returns the results of the `f`
> applications and the remaining `bs`.
> ```
> zipWithLeft' prod.mk [1, 2] ['a'] = ([(1, some 'a'), (2, none)], [])
> zipWithLeft' prod.mk [1] ['a', 'b'] = ([(1, some 'a')], ['b'])
> ```

```lean
def zipWithLeft' (f : α → Option β → γ) : List α → List β → List γ × List β
```

`List.zipWithLeft'TR` (definition, [line 722](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L722))

> Tail-recursive version of `zipWithLeft'`.

```lean
def zipWithLeft'TR (f : α → Option β → γ)
    (as : List α) (bs : List β) : List γ × List β
```

`List.zipWithLeft'_eq_zipWithLeft'TR` (theorem, [line 730](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L730))

```lean
theorem zipWithLeft'_eq_zipWithLeft'TR : @zipWithLeft' = @zipWithLeft'TR
```

`List.zipWithRight'` (definition, [line 750](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L750))

> Right-biased version of `List.zipWith`. `zipWithRight' f as bs` applies `f` to each
> pair of elements `aᵢ ∈ as` and `bᵢ ∈ bs`. If `as` is shorter than `bs`, `f` is
> applied to `none` for the remaining `bᵢ`. Returns the results of the `f`
> applications and the remaining `as`.
> ```
> zipWithRight' prod.mk [1] ['a', 'b'] = ([(some 1, 'a'), (none, 'b')], [])
> zipWithRight' prod.mk [1, 2] ['a'] = ([(some 1, 'a')], [2])
> ```

```lean
def zipWithRight' (f : Option α → β → γ) (as : List α) (bs : List β) : List γ × List α
```

`List.zipLeft'` (definition, [line 764](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L764))

> Left-biased version of `List.zip`. `zipLeft' as bs` returns the list of
> pairs `(aᵢ, bᵢ)` for `aᵢ ∈ as` and `bᵢ ∈ bs`. If `bs` is shorter than `as`, the
> remaining `aᵢ` are paired with `none`. Also returns the remaining `bs`.
> ```
> zipLeft' [1, 2] ['a'] = ([(1, some 'a'), (2, none)], [])
> zipLeft' [1] ['a', 'b'] = ([(1, some 'a')], ['b'])
> zipLeft' = zipWithLeft' prod.mk
> ```

```lean
def zipLeft' : List α → List β → List (α × Option β) × List β
```

`List.zipRight'` (definition, [line 777](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L777))

> Right-biased version of `List.zip`. `zipRight' as bs` returns the list of
> pairs `(aᵢ, bᵢ)` for `aᵢ ∈ as` and `bᵢ ∈ bs`. If `as` is shorter than `bs`, the
> remaining `bᵢ` are paired with `none`. Also returns the remaining `as`.
> ```
> zipRight' [1] ['a', 'b'] = ([(some 1, 'a'), (none, 'b')], [])
> zipRight' [1, 2] ['a'] = ([(some 1, 'a')], [2])
> zipRight' = zipWithRight' prod.mk
> ```

```lean
def zipRight' : List α → List β → List (Option α × β) × List α
```

`List.zipWithLeft` (definition, [line 789](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L789))

> Left-biased version of `List.zipWith`. `zipWithLeft f as bs` applies `f` to each pair
> `aᵢ ∈ as` and `bᵢ ‌∈ bs`. If `bs` is shorter than `as`, `f` is applied to `none`
> for the remaining `aᵢ`.
> ```
> zipWithLeft prod.mk [1, 2] ['a'] = [(1, some 'a'), (2, none)]
> zipWithLeft prod.mk [1] ['a', 'b'] = [(1, some 'a')]
> zipWithLeft f as bs = (zipWithLeft' f as bs).fst
> ```

```lean
def zipWithLeft (f : α → Option β → γ) : List α → List β → List γ
```

`List.zipWithLeftTR` (definition, [line 795](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L795))

> Tail-recursive version of `zipWithLeft`.

```lean
def zipWithLeftTR (f : α → Option β → γ)
    (as : List α) (bs : List β) : List γ
```

`List.zipWithLeft_eq_zipWithLeftTR` (theorem, [line 803](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L803))

```lean
theorem zipWithLeft_eq_zipWithLeftTR : @zipWithLeft = @zipWithLeftTR
```

`List.zipWithRight` (definition, [line 821](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L821))

> Right-biased version of `List.zipWith`. `zipWithRight f as bs` applies `f` to each
> pair `aᵢ ∈ as` and `bᵢ ‌∈ bs`. If `as` is shorter than `bs`, `f` is applied to
> `none` for the remaining `bᵢ`.
> ```
> zipWithRight prod.mk [1, 2] ['a'] = [(some 1, 'a')]
> zipWithRight prod.mk [1] ['a', 'b'] = [(some 1, 'a'), (none, 'b')]
> zipWithRight f as bs = (zipWithRight' f as bs).fst
> ```

```lean
def zipWithRight (f : Option α → β → γ) (as : List α) (bs : List β) : List γ
```

`List.zipLeft` (definition, [line 834](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L834))

> Left-biased version of `List.zip`. `zipLeft as bs` returns the list of pairs
> `(aᵢ, bᵢ)` for `aᵢ ∈ as` and `bᵢ ∈ bs`. If `bs` is shorter than `as`, the
> remaining `aᵢ` are paired with `none`.
> ```
> zipLeft [1, 2] ['a'] = [(1, some 'a'), (2, none)]
> zipLeft [1] ['a', 'b'] = [(1, some 'a')]
> zipLeft = zipWithLeft prod.mk
> ```

```lean
def zipLeft : List α → List β → List (α × Option β)
```

`List.zipRight` (definition, [line 846](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L846))

> Right-biased version of `List.zip`. `zipRight as bs` returns the list of pairs
> `(aᵢ, bᵢ)` for `aᵢ ∈ as` and `bᵢ ∈ bs`. If `as` is shorter than `bs`, the
> remaining `bᵢ` are paired with `none`.
> ```
> zipRight [1, 2] ['a'] = [(some 1, 'a')]
> zipRight [1] ['a', 'b'] = [(some 1, 'a'), (none, 'b')]
> zipRight = zipWithRight prod.mk
> ```

```lean
def zipRight : List α → List β → List (Option α × β)
```

`List.allSome` (definition, [line 856](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L856))

> If all elements of `xs` are `some xᵢ`, `allSome xs` returns the `xᵢ`. Otherwise
> it returns `none`.
> ```
> allSome [some 1, some 2] = some [1, 2]
> allSome [some 1, none  ] = none
> ```

```lean
def allSome (l : List (Option α)) : Option (List α)
```

`List.takeList` (definition, [line 869](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L869))

> `takeList as ns` extracts successive sublists from `as`. For `ns = n₁ ... nₘ`,
> it first takes the `n₁` initial elements from `as`, then the next `n₂` ones,
> etc. It returns the sublists of `as` -- one for each `nᵢ` -- and the remaining
> elements of `as`. If `as` does not have at least as many elements as the sum of
> the `nᵢ`, the corresponding sublists will have less than `nᵢ` elements.
> ```
> takeList ['a', 'b', 'c', 'd', 'e'] [2, 1, 1] = ([['a', 'b'], ['c'], ['d']], ['e'])
> takeList ['a', 'b'] [3, 1] = ([['a', 'b'], []], [])
> ```

```lean
def takeList {α} : List α → List Nat → List (List α) × List α
```

`List.takeListTR` (definition, [line 877](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L877))

> Tail-recursive version of `takeList`.

```lean
def takeListTR
    (xs : List α) (ns : List Nat) : List (List α) × List α
```

`List.takeList_eq_takeListTR` (theorem, [line 886](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L886))

```lean
theorem takeList_eq_takeListTR : @takeList = @takeListTR
```

`List.toChunksAux` (definition, [line 898](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L898))

> Auxliary definition used to define `toChunks`.
> `toChunksAux n xs i` returns `(xs.take i, (xs.drop i).toChunks (n+1))`,
> that is, the first `i` elements of `xs`, and the remaining elements chunked into
> sublists of length `n+1`.

```lean
def toChunksAux {α} (n : Nat) : List α → Nat → List α × List (List α)
```

`List.toChunks` (definition, [line 917](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L917))

> `xs.toChunks n` splits the list into sublists of size at most `n`,
> such that `(xs.toChunks n).join = xs`.
> ```
> [1, 2, 3, 4, 5, 6, 7, 8].toChunks 10 = [[1, 2, 3, 4, 5, 6, 7, 8]]
> [1, 2, 3, 4, 5, 6, 7, 8].toChunks 3 = [[1, 2, 3], [4, 5, 6], [7, 8]]
> [1, 2, 3, 4, 5, 6, 7, 8].toChunks 2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
> [1, 2, 3, 4, 5, 6, 7, 8].toChunks 0 = [[1, 2, 3, 4, 5, 6, 7, 8]]
> ```

```lean
def toChunks {α} : Nat → List α → List (List α)
```

> We add some n-ary versions of `List.zipWith` for functions with more than two arguments.
> These can also be written in terms of `List.zip` or `List.zipWith`.
> For example, `zipWith₃ f xs ys zs` could also be written as
> `zipWith id (zipWith f xs ys) zs`
> or as
> `(zip xs <| zip ys zs).map fun ⟨x, y, z⟩ => f x y z`.

`List.zipWith₃` (definition, [line 945](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L945))

> Ternary version of `List.zipWith`.

```lean
def zipWith₃ (f : α → β → γ → δ) : List α → List β → List γ → List δ
```

`List.zipWith₄` (definition, [line 950](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L950))

> Quaternary version of `List.zipWith`.

```lean
def zipWith₄ (f : α → β → γ → δ → ε) : List α → List β → List γ → List δ → List ε
```

`List.zipWith₅` (definition, [line 955](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L955))

> Quinary version of `List.zipWith`.

```lean
def zipWith₅ (f : α → β → γ → δ → ε → ζ) : List α → List β → List γ → List δ → List ε → List ζ
```

`List.mapWithPrefixSuffixAux` (definition, [line 961](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L961))

> An auxiliary function for `List.mapWithPrefixSuffix`.

```lean
def mapWithPrefixSuffixAux {α β} (f : List α → α → List α → β) : List α → List α → List β
```

`List.mapWithPrefixSuffix` (definition, [line 972](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L972))

> `List.mapWithPrefixSuffix f l` maps `f` across a list `l`.
> For each `a ∈ l` with `l = pref ++ [a] ++ suff`, `a` is mapped to `f pref a suff`.
> Example: if `f : list Nat → Nat → list Nat → β`,
> `List.mapWithPrefixSuffix f [1, 2, 3]` will produce the list
> `[f [] 1 [2, 3], f [1] 2 [3], f [1, 2] 3 []]`.

```lean
def mapWithPrefixSuffix {α β} (f : List α → α → List α → β) (l : List α) : List β
```

`List.mapWithComplement` (definition, [line 983](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L983))

> `List.mapWithComplement f l` is a variant of `List.mapWithPrefixSuffix`
> that maps `f` across a list `l`.
> For each `a ∈ l` with `l = pref ++ [a] ++ suff`, `a` is mapped to `f a (pref ++ suff)`,
> i.e., the list input to `f` is `l` with `a` removed.
> Example: if `f : Nat → list Nat → β`, `List.mapWithComplement f [1, 2, 3]` will produce the list
> `[f 1 [2, 3], f 2 [1, 3], f 3 [1, 2]]`.

```lean
def mapWithComplement {α β} (f : α → List α → β) : List α → List β
```

`List.traverse` (definition, [line 990](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L990))

> Map each element of a `List` to an action, evaluate these actions in order,
> and collect the results.

```lean
protected def traverse [Applicative F] (f : α → F β) : List α → F (List β)
```

`List.Subperm` (definition, [line 999](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L999))

> `Subperm l₁ l₂`, denoted `l₁ <+~ l₂`, means that `l₁` is a sublist of
> a permutation of `l₂`. This is an analogue of `l₁ ⊆ l₂` which respects
> multiplicities of elements, and is used for the `≤` relation on multisets.

```lean
def Subperm (l₁ l₂ : List α) : Prop
```

`List.isSubperm` (definition, [line 1007](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L1007))

> `O(|l₁| * (|l₁| + |l₂|))`. Computes whether `l₁` is a sublist of a permutation of `l₂`.
> See `isSubperm_iff` for a characterization in terms of `List.Subperm`.

```lean
def isSubperm [BEq α] (l₁ l₂ : List α) : Bool
```

`List.insertP` (definition, [line 1013](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L1013))

> `O(|l|)`. Inserts `a` in `l` right before the first element such that `p` is true, or at the end of
> the list if `p` always false on `l`.

```lean
def insertP (p : α → Bool) (a : α) (l : List α) : List α
```

`List.dropPrefix?` (definition, [line 1024](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L1024))

> `dropPrefix? l p` returns
> `some r` if `l = p' ++ r` for some `p'` which is paiwise `==` to `p`,
> and `none` otherwise.

```lean
def dropPrefix? [BEq α] : List α → List α → Option (List α)
```

`List.dropSuffix?` (definition, [line 1032](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L1032))

> `dropSuffix? l s` returns
> `some r` if `l = r ++ s'` for some `s'` which is paiwise `==` to `s`,
> and `none` otherwise.

```lean
def dropSuffix? [BEq α] (l s : List α) : Option (List α)
```

`List.dropInfix?` (definition, [line 1043](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L1043))

> `dropInfix? l i` returns
> `some (p, s)` if `l = p ++ i' ++ s` for some `i'` which is paiwise `==` to `i`,
> and `none` otherwise.
>
> Note that this is an inefficient implementation, and if computation time is a concern you should be
> using the Knuth-Morris-Pratt algorithm as implemented in `Batteries.Data.List.Matcher`.

```lean
def dropInfix? [BEq α] (l i : List α) : Option (List α × List α)
```

`List.partialSums` (definition, [line 1061](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L1061))

> Computes the partial sums of the elements of a list.
>
> Examples:
>
> `[a, b, c].partialSums = [0, 0 + a, (0 + a) + b, ((0 + a) + b) + c]`
> `[1, 2, 3].partialSums = [0, 1, 3, 6]`

```lean
def partialSums [Add α] [Zero α] (l : List α) : List α
```

`List.partialProds` (definition, [line 1072](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L1072))

> Computes the partial products of the elements of a list.
>
> Examples:
>
> `[a, b, c].partialProds = [1, 1 * a, (1 * a) * b, ((1 * a) * b) * c]`
> `[2, 3, 5].partialProds = [1, 2, 6, 30]`

```lean
def partialProds [Mul α] [One α] (l : List α) : List α
```

`List.swapAt` (definition, [line 1077](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L1077))

> `swapAt xs i v` sets position `i` of `xs` to `v` and returns the displaced
> element, or `v` itself (with `xs` unchanged) if `i` is out of bounds.

```lean
def swapAt (xs : List α) (i : Nat) (v : α) : α × List α
```

`List.swapAtTR` (definition, [line 1080](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L1080))

> Tail-recursive version of `swapAt`.

```lean
def swapAtTR (l : List α) (i : Nat) (v : α) : α × List α
```

`List.swapAt_eq_swapAtTR` (theorem, [line 1087](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L1087))

```lean
theorem swapAt_eq_swapAtTR : @swapAt = @swapAtTR
```

`List.swap` (definition, [line 1097](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L1097))

> `l.swap i j` exchanges the elements at positions `i` and `j` of `l`.
> If either index is out of bounds, `l` is returned unchanged.

```lean
def swap : List α → Nat → Nat → List α
```

`List.swapTR` (definition, [line 1103](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L1103))

> Tail-recursive version of `swap`.

```lean
def swapTR (l : List α) (i j : Nat) : List α
```

`List.swap_eq_swapTR` (theorem, [line 1111](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean#L1111))

```lean
theorem swap_eq_swapTR : @swap = @swapTR
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/List/Basic.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/List/Basic.lean)
- [Declaration ledger](../../../../../../sources/batteries/Batteries.Data.List.Basic.json)

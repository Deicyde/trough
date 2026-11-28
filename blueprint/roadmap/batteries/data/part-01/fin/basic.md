---
catalog: module
lean: Fin.clamp, Fin.dfoldrM, Fin.dfoldr, Fin.dfoldlM, Fin.dfoldl, Fin.sum, Fin.prod, Fin.countP, Fin.findSome?, Fin.findSomeRev?, Fin.find?, Fin.findRev?, Fin.divNat, Fin.modNat, Fin.mkDivMod
statement: formalized
proof: formalized
---

# Fin/Basic

`Batteries.Data.Fin.Basic`, in [Batteries/Data/Fin/Basic.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean), by Robert Y. Lewis, Keeley Hoek, Mario Carneiro, François G. Dorais, Quang Dao.

`Fin.clamp` (definition, [line 15](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L15))

> `min n m` as an element of `Fin (m + 1)`

```lean
def clamp (n m : Nat) : Fin (m + 1)
```

`Fin.dfoldrM` (definition, [line 27](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L27))

> Heterogeneous monadic fold over `Fin n` from right to left:
> ```
> Fin.foldrM n f xₙ = do
>   let xₙ₋₁ : α (n-1) ← f (n-1) xₙ
>   let xₙ₋₂ : α (n-2) ← f (n-2) xₙ₋₁
>   ...
>   let x₀ : α 0 ← f 0 x₁
>   pure x₀
> ```
> This is the dependent version of `Fin.foldrM`.

```lean
def dfoldrM [Monad m] (n : Nat) (α : Fin (n + 1) → Type _)
    (f : ∀ (i : Fin n), α i.succ → m (α i.castSucc)) (init : α (last n)) : m (α 0)
```

`Fin.dfoldr` (definition, [line 50](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L50))

> Heterogeneous fold over `Fin n` from the right: `foldr 3 f x = f 0 (f 1 (f 2 x))`, where
> `f 2 : α 3 → α 2`, `f 1 : α 2 → α 1`, etc.
>
> This is the dependent version of `Fin.foldr`.

```lean
def dfoldr (n : Nat) (α : Fin (n + 1) → Type _)
    (f : ∀ (i : Fin n), α i.succ → α i.castSucc) (init : α (last n)) : α 0
```

`Fin.dfoldlM` (definition, [line 64](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L64))

> Heterogeneous monadic fold over `Fin n` from left to right:
> ```
> Fin.foldlM n f x₀ = do
>   let x₁ : α 1 ← f 0 x₀
>   let x₂ : α 2 ← f 1 x₁
>   ...
>   let xₙ : α n ← f (n-1) xₙ₋₁
>   pure xₙ
> ```
> This is the dependent version of `Fin.foldlM`.

```lean
def dfoldlM [Monad m] (n : Nat) (α : Fin (n + 1) → Type _)
    (f : ∀ (i : Fin n), α i.castSucc → m (α i.succ)) (init : α 0) : m (α (last n))
```

`Fin.dfoldl` (definition, [line 87](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L87))

> Heterogeneous fold over `Fin n` from the left: `foldl 3 f x = f 0 (f 1 (f 2 x))`, where
> `f 0 : α 0 → α 1`, `f 1 : α 1 → α 2`, etc.
>
> This is the dependent version of `Fin.foldl`.

```lean
def dfoldl (n : Nat) (α : Fin (n + 1) → Type _)
    (f : ∀ (i : Fin n), α i.castSucc → α i.succ) (init : α 0) : α (last n)
```

`Fin.sum` (definition, [line 92](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L92))

> Sum of a tuple indexed by `Fin n`.

```lean
protected def sum [Zero α] [Add α] (x : Fin n → α) : α
```

`Fin.prod` (definition, [line 96](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L96))

> Product of a tuple indexed by `Fin n`.

```lean
protected def prod [One α] [Mul α] (x : Fin n → α) : α
```

`Fin.countP` (definition, [line 100](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L100))

> Count the number of true values of a decidable predicate on `Fin n`.

```lean
protected def countP (p : Fin n → Bool) : Nat
```

`Fin.findSome?` (definition, [line 107](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L107))

> `findSome? f` returns `f i` for the first `i` for which `f i` is `some _`, or `none` if no such
> element is found. The function `f` is not evaluated on further inputs after the first `i` is found.

```lean
def findSome? (f : Fin n → Option α) : Option α
```

`Fin.findSomeRev?` (definition, [line 114](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L114))

> `findSomeRev? f` returns `f i` for the last `i` for which `f i` is `some _`, or `none` if no such
> element is found. The function `f` is not evaluated on further inputs after the first `i` is found.

```lean
def findSomeRev? (f : Fin n → Option α) : Option α
```

`Fin.find?` (abbreviation, [line 122](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L122))

> `find? p` returns the first `i` for which `p i = true`, or `none` if no such element is found.
> The function `p` is not evaluated on further inputs after the first `i` is found.

```lean
abbrev find? (p : Fin n → Bool) : Option (Fin n)
```

`Fin.findRev?` (abbreviation, [line 129](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L129))

> `find? p` returns the first `i` for which `p i = true`, or `none` if no such element is found.
> The function `p` is not evaluated on further inputs after the first `i` is found.

```lean
abbrev findRev? (p : Fin n → Bool) : Option (Fin n)
```

`Fin.divNat` (definition, [line 133](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L133))

> Compute `i / n`, where `n` is a `Nat` and inferred the type of `i`.

```lean
def divNat (i : Fin (m * n)) : Fin m
```

`Fin.modNat` (definition, [line 137](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L137))

> Compute `i % n`, where `n` is a `Nat` and inferred the type of `i`.

```lean
def modNat (i : Fin (m * n)) : Fin n
```

`Fin.mkDivMod` (definition, [line 144](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean#L144))

> Compute the element of `Fin (m * n)` with quotient `i : Fin m` and remainder `j : Fin n`
> when divided by `n`.

```lean
def mkDivMod (i : Fin m) (j : Fin n) : Fin (m * n)
```

## Depends on

- [Nat/Basic](../nat/basic.md)

## Proof depends on

- [Basic lemmas about natural numbers](../nat/lemmas.md)

## Sources

- [Batteries/Data/Fin/Basic.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Basic.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Fin.Basic.json)

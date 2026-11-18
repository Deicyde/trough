---
catalog: module
lean: Array.scanlM.loop_toList, Array.scanlM_eq_scanlM_toList, Array.toList_scanlM, Array.scanrM.loop_toList, Array.scanrM_eq_scanrM_toList, Array.toList_scanrM, Array.scanlM_extract, Array.scanrM_extract, Array.scanlM_empty, Array.scanrM_empty, Array.scanlM_reverse, Array.scanlM_pure, Array.scanrM_pure, Array.idRun_scanlM, Array.idRun_scanrM, Array.scanlM_map, Array.scanrM_map, Array.scanl_eq_scanlM, Array.scanl_eq_scanl_toList, Array.toList_scanl, Array.size_scanl, Array.scanl_empty, Array.scanl_singleton, Array.scanl_ne_empty, Array.scanl_eq_singleton_iff, Array.getElem_scanl, Array.getElem?_scanl, Array.take_scanl, Array.getElem?_scanl_zero, Array.getElem_scanl_zero, Array.getElem?_succ_scanl, Array.getElem_succ_scanl, Array.scanl_push, Array.scanl_map, Array.back_scanl, Array.back?_scanl, Array.back_scanl?, Array.scanr_eq_scanrM, Array.scanr_eq_scanr_toList, Array.toList_scanr, Array.size_scanr, Array.scanr_empty, Array.scanr_ne_empty, Array.scanr_push, Array.back_scanr, Array.back?_scanr, Array.getElem_scanr, Array.getElem?_scanr, Array.getElem_scanr_zero, Array.getElem?_scanr_zero, Array.scanr_map, Array.scanl_reverse, Array.scanr_reverse, Array.scanl_extract, Array.scanr_extract, List.toArray_scanlM, List.toArray_scanrM, List.toArray_scanl, List.toArray_scanr, Subarray.scanlM_eq_scanlM_extract, Subarray.scanrM_eq_scanrM_extract, Subarray.scanl_eq_scanl_extract, Subarray.scanr_eq_scanr_extract
statement: formalized
proof: formalized
---

# Array

`Batteries.Data.Array.Scan`, in [Batteries/Data/Array/Scan.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean), by Chad Sharp.

> Prove basic results about `Array.scanl`, `Array.scanr`, `Array.scanlM` and `Array.scanrM`.

`Array.scanlM.loop_toList` (theorem, [line 23](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L23))

```lean
theorem scanlM.loop_toList [Monad m] [LawfulMonad m]
    {f : β → α → m β} {stop : Nat} (h : stop ≤ as.size) :
    Array.toList <$> scanlM.loop f init as start stop h acc =
      return acc.toList
               ++ (← as.toList.drop start
                  |>.take (stop - start)
                  |>.scanlM f init)
```

`Array.scanlM_eq_scanlM_toList` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L39))

```lean
theorem scanlM_eq_scanlM_toList [Monad m] [LawfulMonad m] {f : β → α → m β} {as : Array α} :
    as.scanlM f init = List.toArray <$> as.toList.scanlM f init
```

`Array.toList_scanlM` (theorem, [line 45](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L45))

```lean
theorem toList_scanlM [Monad m] [LawfulMonad m] {f : β → α → m β} {as : Array α} :
    toList <$> as.scanlM f init = as.toList.scanlM f init
```

`Array.scanrM.loop_toList` (theorem, [line 49](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L49))

```lean
theorem scanrM.loop_toList [Monad m] [LawfulMonad m] {f : α → β → m β}
    {start : Nat} {h : start ≤ as.size} :
    Array.toList <$> scanrM.loop f init as start stop h acc =
      return (← as.toList.drop stop
                  |>.take (start - stop)
                  |>.scanrM f init)
                ++ acc.toList.reverse
```

`Array.scanrM_eq_scanrM_toList` (theorem, [line 75](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L75))

```lean
theorem scanrM_eq_scanrM_toList [Monad m] [LawfulMonad m] {f : α → β → m β} {as : Array α} :
    as.scanrM f init = List.toArray <$> as.toList.scanrM f init
```

`Array.toList_scanrM` (theorem, [line 81](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L81))

```lean
theorem toList_scanrM [Monad m] [LawfulMonad m] {f : α → β → m β} {as : Array α} :
    toList <$> as.scanrM f init = as.toList.scanrM f init
```

`Array.scanlM_extract` (theorem, [line 85](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L85))

```lean
theorem scanlM_extract [Monad m] [LawfulMonad m] {f : β → α → m β} {as : Array α} :
    (as.extract start stop).scanlM f init = as.scanlM f init start stop
```

`Array.scanrM_extract` (theorem, [line 93](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L93))

```lean
theorem scanrM_extract [Monad m] [LawfulMonad m] {f : α → β → m β} {as : Array α} :
    (as.extract stop start).scanrM f init = as.scanrM f init start stop
```

`Array.scanlM_empty` (theorem, [line 102](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L102))

```lean
theorem scanlM_empty [Monad m] {f : β → α → m β} {start stop : Nat} :
    #[].scanlM f init start stop = pure #[init]
```

`Array.scanrM_empty` (theorem, [line 107](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L107))

```lean
theorem scanrM_empty [Monad m] {f : α → β → m β} {start stop : Nat} :
    #[].scanrM f init start stop = pure #[init]
```

`Array.scanlM_reverse` (theorem, [line 111](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L111))

```lean
theorem scanlM_reverse [Monad m] [LawfulMonad m] {f : β → α → m β} {as : Array α} :
    as.reverse.scanlM f init = Array.reverse <$> (as.scanrM (flip f) init)
```

`Array.scanlM_pure` (theorem, [line 117](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L117))

```lean
theorem scanlM_pure [Monad m] [LawfulMonad m] {f : β → α → β} {as : Array α} :
    as.scanlM (m := m) (pure <| f · ·) init = pure (as.scanl f init)
```

`Array.scanrM_pure` (theorem, [line 123](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L123))

```lean
theorem scanrM_pure [Monad m] [LawfulMonad m] {f : α → β → β} {as : Array α} :
    as.scanrM (m := m) (pure <| f · ·) init = pure (as.scanr f init)
```

`Array.idRun_scanlM` (theorem, [line 129](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L129))

```lean
theorem idRun_scanlM {f : β → α → Id β} {as : Array α} :
    (as.scanlM f init).run = as.scanl (f · · |>.run) init
```

`Array.idRun_scanrM` (theorem, [line 134](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L134))

```lean
theorem idRun_scanrM {f : α → β → Id β} {as : Array α} :
    (as.scanrM f init).run = as.scanr (f · · |>.run) init
```

`Array.scanlM_map` (theorem, [line 139](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L139))

```lean
theorem scanlM_map [Monad m] [LawfulMonad m] {f : α₁ → α₂ } {g: β → α₂ → m β} {as : Array α₁} :
    (as.map f).scanlM g init = as.scanlM (g · <| f ·) init
```

`Array.scanrM_map` (theorem, [line 144](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L144))

```lean
theorem scanrM_map [Monad m] [LawfulMonad m] {f : α₁ → α₂ } {g: α₂ → β → m β} {as : Array α₁} :
    (as.map f).scanrM g init = as.scanrM (fun a b => g (f a) b) init
```

`Array.scanl_eq_scanlM` (theorem, [line 150](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L150))

> ### Array.scanl

```lean
theorem scanl_eq_scanlM {f : β → α → β} {as: Array α} :
    as.scanl f init = (as.scanlM (m := Id) (pure <| f · ·) init).run
```

`Array.scanl_eq_scanl_toList` (theorem, [line 154](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L154))

```lean
theorem scanl_eq_scanl_toList {f: β → α → β} {as : Array α} :
    as.scanl f init = (as.toList.scanl f init).toArray
```

`Array.toList_scanl` (theorem, [line 160](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L160))

```lean
theorem toList_scanl {f : β → α → β} {as: Array α} :
    (as.scanl f init).toList = as.toList.scanl f init
```

`Array.size_scanl` (theorem, [line 165](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L165))

```lean
theorem size_scanl {f : β → α → β} (init : β) (as : Array α) :
    size (scanl f init as) = as.size + 1
```

`Array.scanl_empty` (theorem, [line 172](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L172))

```lean
theorem scanl_empty {f : β → α → β} (init : β) :
    scanl f init #[] = #[init]
```

`Array.scanl_singleton` (theorem, [line 178](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L178))

```lean
theorem scanl_singleton {f : β → α → β} :
    scanl f init #[a] = #[init, f init a]
```

`Array.scanl_ne_empty` (theorem, [line 184](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L184))

```lean
theorem scanl_ne_empty {f : β → α → β} : scanl f init as ≠ #[]
```

`Array.scanl_eq_singleton_iff` (theorem, [line 187](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L187))

```lean
theorem scanl_eq_singleton_iff {f : β → α → β} (c : β) :
    scanl f init as = #[c] ↔ c = init ∧ as = #[]
```

`Array.getElem_scanl` (theorem, [line 192](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L192))

```lean
theorem getElem_scanl {f : β → α → β} {as: Array α} (h : i < (as.scanl f init).size) :
    (as.scanl f init)[i]'h = foldl f init (as.take i)
```

`Array.getElem?_scanl` (theorem, [line 198](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L198))

```lean
theorem getElem?_scanl {f : β → α → β} :
    (scanl f a l)[i]? = if i ≤ l.size then some (foldl f a (l.take i)) else none
```

`Array.take_scanl` (theorem, [line 203](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L203))

```lean
theorem take_scanl {f : β → α → β} (init : β) (as : Array α) :
    (scanl f init as).take (i + 1) = scanl f init (as.take i)
```

`Array.getElem?_scanl_zero` (theorem, [line 207](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L207))

```lean
theorem getElem?_scanl_zero {f : β → α → β} : (scanl f init as)[0]? = some init
```

`Array.getElem_scanl_zero` (theorem, [line 209](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L209))

```lean
theorem getElem_scanl_zero {f : β → α → β} : (scanl f init as)[0] = init
```

`Array.getElem?_succ_scanl` (theorem, [line 211](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L211))

```lean
theorem getElem?_succ_scanl {f : β → α → β} :
    (scanl f init as)[i + 1]? = (scanl f init as)[i]?.bind fun x => as[i]?.map fun y => f x y
```

`Array.getElem_succ_scanl` (theorem, [line 215](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L215))

```lean
theorem getElem_succ_scanl {f : β → α → β} (h : i + 1 < (scanl f b as).size) :
    (as.scanl f b)[i + 1] = f (as.scanl f b)[i] (as[i]'(by grind))
```

`Array.scanl_push` (theorem, [line 221](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L221))

```lean
theorem scanl_push {f : β → α → β} {init: β} {a : α} {as : Array α} :
    (as.push a).scanl f init = (as.scanl f init).push (f (as.foldl f init) a)
```

`Array.scanl_map` (theorem, [line 227](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L227))

```lean
theorem scanl_map {f : γ → β → γ} {g : α → β} (init : γ) (as : Array α) :
    scanl f init (as.map g) = scanl (f · <| g ·) init as
```

`Array.back_scanl` (theorem, [line 232](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L232))

```lean
theorem back_scanl {f : β → α → β} {as : Array α} :
    (as.scanl f init).back = as.foldl f init
```

`Array.back?_scanl` (theorem, [line 236](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L236))

```lean
theorem back?_scanl {f : β → α → β} {as : Array α} :
    (as.scanl f init).back? = some (as.foldl f init)
```

`Array.back_scanl?` (alias, [line 241](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L241))

```lean
alias back_scanl?
```

> ### Array.scanr

`Array.scanr_eq_scanrM` (theorem, [line 245](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L245))

```lean
theorem scanr_eq_scanrM {f : α → β → β} {as : Array α} :
    as.scanr f init = (as.scanrM (m := Id) (pure <| f · ·) init).run
```

`Array.scanr_eq_scanr_toList` (theorem, [line 249](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L249))

```lean
theorem scanr_eq_scanr_toList {f : α → β → β} {as : Array α} :
    as.scanr f init = (as.toList.scanr f init).toArray
```

`Array.toList_scanr` (theorem, [line 255](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L255))

```lean
theorem toList_scanr {f : α → β → β} {as : Array α} :
    (as.scanr f init).toList = as.toList.scanr f init
```

`Array.size_scanr` (theorem, [line 260](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L260))

```lean
theorem size_scanr {f : α → β → β} (init : β) (as : Array α) :
    size (as.scanr f init) = as.size + 1
```

`Array.scanr_empty` (theorem, [line 267](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L267))

```lean
theorem scanr_empty {f : α → β → β} {init: β} :
    #[].scanr f init = #[init]
```

`Array.scanr_ne_empty` (theorem, [line 273](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L273))

```lean
theorem scanr_ne_empty {f : α → β → β} {as : Array α} :
    as.scanr f init ≠ #[]
```

`Array.scanr_push` (theorem, [line 278](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L278))

```lean
theorem scanr_push {f : α → β → β} {as : Array α} :
    (as.push a).scanr f init = (as.scanr f (f a init)).push init
```

`Array.back_scanr` (theorem, [line 284](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L284))

```lean
theorem back_scanr {f : α → β → β} {as : Array α} : (as.scanr f init).back = init
```

`Array.back?_scanr` (theorem, [line 287](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L287))

```lean
theorem back?_scanr {f : α → β → β} {as : Array α} :
    (as.scanr f init).back? = some init
```

`Array.getElem_scanr` (theorem, [line 292](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L292))

```lean
theorem getElem_scanr {f : α → β → β} (h : i < (scanr f b l).size) :
    (scanr f b l)[i] = foldr f b (l.drop i)
```

`Array.getElem?_scanr` (theorem, [line 298](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L298))

```lean
theorem getElem?_scanr {f : α → β → β} :
    (scanr f b as)[i]? = if i < as.size + 1 then some (foldr f b (as.drop i)) else none
```

`Array.getElem_scanr_zero` (theorem, [line 302](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L302))

```lean
theorem getElem_scanr_zero {f : α → β → β} :
    (scanr f init as)[0] = as.foldr f init
```

`Array.getElem?_scanr_zero` (theorem, [line 306](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L306))

```lean
theorem getElem?_scanr_zero {f : α → β → β} :
    (scanr f init as)[0]? = some (as.foldr f init )
```

`Array.scanr_map` (theorem, [line 311](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L311))

```lean
theorem scanr_map {f : β → γ → γ} {g : α → β} (init : γ) (as : Array α) :
    scanr f init (as.map g) = scanr (fun x acc => f (g x) acc) init as
```

`Array.scanl_reverse` (theorem, [line 316](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L316))

```lean
theorem scanl_reverse {f : β → α → β} {as : Array α} :
    scanl f init as.reverse = reverse (scanr (flip f) init as)
```

`Array.scanr_reverse` (theorem, [line 323](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L323))

```lean
theorem scanr_reverse {f : α → β → β} {as : Array α} :
    scanr f init as.reverse = reverse (scanl (flip f) init as)
```

`Array.scanl_extract` (theorem, [line 329](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L329))

```lean
theorem scanl_extract {f : β → α → β} {as : Array α} :
    (as.extract start stop).scanl f init = as.scanl f init start stop
```

`Array.scanr_extract` (theorem, [line 334](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L334))

```lean
theorem scanr_extract {f : α → β → β} {as : Array α} :
    (as.extract stop start).scanr f init = as.scanr f init start stop
```

`List.toArray_scanlM` (theorem, [line 343](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L343))

```lean
theorem toArray_scanlM [Monad m] [LawfulMonad m] {f : β → α → m β} {as : List α} :
    toArray <$> as.scanlM f init = as.toArray.scanlM f init
```

`List.toArray_scanrM` (theorem, [line 348](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L348))

```lean
theorem toArray_scanrM [Monad m] [LawfulMonad m] {f : α → β → m β} {as : List α} :
    toArray <$> as.scanrM f init = as.toArray.scanrM f init
```

`List.toArray_scanl` (theorem, [line 353](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L353))

```lean
theorem toArray_scanl {f : β → α → β} {as : List α} :
    (as.scanl f init).toArray = as.toArray.scanl f init
```

`List.toArray_scanr` (theorem, [line 357](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L357))

```lean
theorem toArray_scanr {f : α → β → β} {as : List α} :
    (as.scanr f init).toArray = as.toArray.scanr f init
```

`Subarray.scanlM_eq_scanlM_extract` (theorem, [line 366](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L366))

```lean
theorem scanlM_eq_scanlM_extract [Monad m] [LawfulMonad m] {f : β → α → m β} {as : Subarray α} :
    as.scanlM f init = (as.array.extract as.start as.stop).scanlM f init
```

`Subarray.scanrM_eq_scanrM_extract` (theorem, [line 371](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L371))

```lean
theorem scanrM_eq_scanrM_extract [Monad m] [LawfulMonad m] {f : α → β → m β} {as : Subarray α} :
    as.scanrM f init = (as.array.extract as.start as.stop).scanrM f init
```

`Subarray.scanl_eq_scanl_extract` (theorem, [line 376](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L376))

```lean
theorem scanl_eq_scanl_extract {f : β → α → β} {as : Subarray α} :
    as.scanl f init = (as.array.extract as.start as.stop).scanl f init
```

`Subarray.scanr_eq_scanr_extract` (theorem, [line 381](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean#L381))

```lean
theorem scanr_eq_scanr_extract {f : α → β → β} {as : Subarray α} :
    as.scanr f init = (as.array.extract as.start as.stop).scanr f init
```

## Depends on

- [Array/Basic](basic.md)

## Proof depends on

- [Array/Lemmas](lemmas.md)

## Sources

- [Batteries/Data/Array/Scan.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Array/Scan.lean)

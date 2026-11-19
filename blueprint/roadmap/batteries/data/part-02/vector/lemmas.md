---
catalog: module
lean: Vector.toArray_injective, Vector.get_mk, Vector.getD_mk, Vector.uget_mk, Vector.tail_eq_of_zero, Vector.tail_eq_of_ne_zero, Vector.toList_tail, Vector.getElem_tail, Vector.get_eq_getElem, Vector.swap_same, Vector.last_cons_pop_perm, Vector.swap_last_pop_perm, Vector.get_push_last, Vector.get_push_castSucc, Vector.get_map, Vector.get_reverse, Vector.get_replicate, Vector.get_range, Vector.get_ofFn, Vector.get_cast, Vector.get_tail, Vector.finIdxOf?_empty, Vector.finIdxOf?_eq_none_iff, Vector.finIdxOf?_eq_some_iff, Vector.isSome_finIdxOf?, Vector.isNone_finIdxOf?, Vector.toArray_scanlM, Vector.toArray_scanrM, Vector.toList_scanlM, Vector.toList_scanrM, Vector.scanlM_empty, Vector.scanrM_empty, Vector.scanlM_reverse, Vector.scanlM_pure, Vector.scanrM_pure, Vector.idRun_scanlM, Vector.idRun_scanrM, Vector.scanlM_map, Vector.scanrM_map, Vector.scanl_eq_scanlM, Vector.scanr_eq_scanrM, Vector.toArray_scanl, Vector.toArray_scanr, Vector.toList_scanl, Vector.toList_scanr, Vector.scanl_empty, Vector.scanr_empty, Vector.scanl_singleton, Vector.getElem_scanl, Vector.getElem_scanr, Vector.getElem?_scanl, Vector.getElem?_scanr, Vector.getElem_scanl_zero, Vector.getElem_scanr_zero, Vector.getElem?_scanl_zero, Vector.getElem?_scanr_zero, Vector.getElem?_succ_scanl, Vector.getElem_succ_scanl, Vector.scanl_push, Vector.scanr_push, Vector.scanl_map, Vector.scanr_map, Vector.scanl_reverse, Vector.scanr_reverse, Vector.back_scanl, Vector.back_scanr, Vector.back?_scanl, Vector.back?_scanr
statement: formalized
proof: formalized
---

# Vector/Lemmas

`Batteries.Data.Vector.Lemmas`, in [Batteries/Data/Vector/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean), by Shreyas Srinivas, François G. Dorais, Eric Wieser, Chad Sharp.

`Vector.toArray_injective` (theorem, [line 17](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L17))

```lean
theorem toArray_injective : ∀ {v w : Vector α n}, v.toArray = w.toArray → v = w
```

> ### mk lemmas

`Vector.get_mk` (theorem, [line 22](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L22))

```lean
theorem get_mk (a : Array α) (h : a.size = n) (i) :
    (Vector.mk a h).get i = a[i]
```

`Vector.getD_mk` (theorem, [line 25](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L25))

```lean
theorem getD_mk (a : Array α) (h : a.size = n) (i x) :
    (Vector.mk a h).getD i x = a.getD i x
```

`Vector.uget_mk` (theorem, [line 28](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L28))

```lean
theorem uget_mk (a : Array α) (h : a.size = n) (i) (hi : i.toNat < n) :
    (Vector.mk a h).uget i hi = a.uget i (by simp [h, hi])
```

> ### tail lemmas

`Vector.tail_eq_of_zero` (theorem, [line 33](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L33))

```lean
theorem tail_eq_of_zero {v : Vector α 0} : v.tail = #v[]
```

`Vector.tail_eq_of_ne_zero` (theorem, [line 35](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L35))

```lean
theorem tail_eq_of_ne_zero [NeZero n] {v : Vector α n} :
    v.tail = v.eraseIdx 0 n.pos_of_neZero
```

`Vector.toList_tail` (theorem, [line 44](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L44))

```lean
theorem toList_tail {v : Vector α n} :
    v.tail.toList = v.toList.tail
```

> ### getElem lemmas

`Vector.getElem_tail` (theorem, [line 59](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L59))

```lean
theorem getElem_tail {v : Vector α n} {i : Nat} (hi : i < n - 1) :
    v.tail[i] = v[i + 1]
```

> ### get lemmas

`Vector.get_eq_getElem` (theorem, [line 68](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L68))

```lean
theorem get_eq_getElem (v : Vector α n) (i : Fin n) : v.get i = v[(i : Nat)]
```

`Vector.swap_same` (theorem, [line 71](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L71))

```lean
theorem swap_same {v : Vector α n} {i : Nat} (hi : i < n) : v.swap i i hi hi = v
```

`Vector.last_cons_pop_perm` (theorem, [line 75](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L75))

```lean
theorem last_cons_pop_perm {v : Vector α (n+1)} : (v[n] :: v.pop.toList).Perm v.toList
```

`Vector.swap_last_pop_perm` (theorem, [line 80](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L80))

```lean
theorem swap_last_pop_perm {v : Vector α (n+1)} {i : Fin (n+1)} (hi : i.val < n) :
    (v[i] :: (v.swap i n (by omega) (by omega) |>.pop).toList).Perm v.toList
```

`Vector.get_push_last` (theorem, [line 87](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L87))

```lean
theorem get_push_last (v : Vector α n) (a : α) :
    (v.push a).get (Fin.last n) = a
```

`Vector.get_push_castSucc` (theorem, [line 91](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L91))

```lean
theorem get_push_castSucc (v : Vector α n) (a : α) (i : Fin n) :
    (v.push a).get (Fin.castSucc i) = v.get i
```

`Vector.get_map` (theorem, [line 95](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L95))

```lean
theorem get_map (v : Vector α n) (f : α → β) (i : Fin n) :
    (v.map f).get i = f (v.get i)
```

`Vector.get_reverse` (theorem, [line 99](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L99))

```lean
theorem get_reverse (v : Vector α n) (i : Fin n) :
    v.reverse.get i = v.get (i.rev)
```

`Vector.get_replicate` (theorem, [line 103](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L103))

```lean
theorem get_replicate (n : Nat) (a : α) (i : Fin n) : (replicate n a).get i = a
```

`Vector.get_range` (theorem, [line 106](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L106))

```lean
theorem get_range (n : Nat) (i : Fin n) : (range n).get i = i
```

`Vector.get_ofFn` (theorem, [line 109](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L109))

```lean
theorem get_ofFn (f : Fin n → α) (i : Fin n) : (ofFn f).get i = f i
```

`Vector.get_cast` (theorem, [line 112](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L112))

```lean
theorem get_cast (v : Vector α m) (h : m = n) (i : Fin n) :
    (v.cast h).get i = v.get (i.cast h.symm)
```

`Vector.get_tail` (theorem, [line 117](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L117))

```lean
theorem get_tail (v : Vector α (n + 1)) (i : Fin n) :
    v.tail.get i = v.get i.succ
```

> ### finIdxOf? lemmas

`Vector.finIdxOf?_empty` (theorem, [line 123](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L123))

```lean
theorem finIdxOf?_empty [BEq α] (v : Vector α 0) : v.finIdxOf? a = none
```

`Vector.finIdxOf?_eq_none_iff` (theorem, [line 127](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L127))

```lean
theorem finIdxOf?_eq_none_iff [BEq α] [LawfulBEq α] {v : Vector α n} {a : α} :
    v.finIdxOf? a = none ↔ a ∉ v
```

`Vector.finIdxOf?_eq_some_iff` (theorem, [line 133](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L133))

```lean
theorem finIdxOf?_eq_some_iff [BEq α] [LawfulBEq α] {v : Vector α n} {a : α} {i : Fin n} :
    v.finIdxOf? a = some i ↔ v.get i = a ∧ ∀ j < i, ¬v.get j = a
```

`Vector.isSome_finIdxOf?` (theorem, [line 139](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L139))

```lean
theorem isSome_finIdxOf? [BEq α] [PartialEquivBEq α] {v : Vector α n} {a : α} :
    (v.finIdxOf? a).isSome = v.contains a
```

`Vector.isNone_finIdxOf?` (theorem, [line 145](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L145))

```lean
theorem isNone_finIdxOf? [BEq α] [PartialEquivBEq α] {v : Vector α n} {a : α} :
    (v.finIdxOf? a).isNone = !v.contains a
```

`Vector.toArray_scanlM` (theorem, [line 168](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L168))

```lean
theorem toArray_scanlM [Monad m] [LawfulMonad m] {f : β → α → m β} {as : Vector α n} :
    Vector.toArray <$> as.scanlM f init = as.toArray.scanlM f init
```

`Vector.toArray_scanrM` (theorem, [line 189](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L189))

```lean
theorem toArray_scanrM [Monad m] [LawfulMonad m] {f : α → β → m β} {as : Vector α n} :
    Vector.toArray <$> as.scanrM f init = as.toArray.scanrM f init
```

> ### scanlM/scanrM lemmas

`Vector.toList_scanlM` (theorem, [line 196](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L196))

```lean
theorem toList_scanlM [Monad m] [LawfulMonad m] {f : β → α → m β} {as : Vector α n} :
    Vector.toList <$> as.scanlM f init = as.toList.scanlM f init
```

`Vector.toList_scanrM` (theorem, [line 203](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L203))

```lean
theorem toList_scanrM [Monad m] [LawfulMonad m] {f : α → β → m β} {as : Vector α n} :
    Vector.toList <$> as.scanrM f init = as.toList.scanrM f init
```

`Vector.scanlM_empty` (theorem, [line 210](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L210))

```lean
theorem scanlM_empty [Monad m] [LawfulMonad m] {f : β → α → m β} :
    (#v[] : Vector α 0).scanlM f init = pure #v[init]
```

`Vector.scanrM_empty` (theorem, [line 216](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L216))

```lean
theorem scanrM_empty [Monad m] [LawfulMonad m] {f : α → β → m β} :
    (#v[] : Vector α 0).scanrM f init = pure #v[init]
```

`Vector.scanlM_reverse` (theorem, [line 221](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L221))

```lean
theorem scanlM_reverse [Monad m] [LawfulMonad m] {f : β → α → m β} {as : Vector α n} :
    as.reverse.scanlM f init = Vector.reverse <$> (as.scanrM (flip f) init)
```

`Vector.scanlM_pure` (theorem, [line 228](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L228))

```lean
theorem scanlM_pure [Monad m] [LawfulMonad m] {f : β → α → β} {as : Vector α n} :
    as.scanlM (m := m) (pure <| f · ·) init = pure (as.scanl f init)
```

`Vector.scanrM_pure` (theorem, [line 235](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L235))

```lean
theorem scanrM_pure [Monad m] [LawfulMonad m] {f : α → β → β} {as : Vector α n} :
    as.scanrM (m := m) (pure <| f · ·) init = pure (as.scanr f init)
```

`Vector.idRun_scanlM` (theorem, [line 241](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L241))

```lean
theorem idRun_scanlM {f : β → α → Id β} {as : Vector α n} :
    (as.scanlM f init).run = as.scanl (f · · |>.run) init
```

`Vector.idRun_scanrM` (theorem, [line 245](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L245))

```lean
theorem idRun_scanrM {f : α → β → Id β} {as : Vector α n} :
    (as.scanrM f init).run = as.scanr (f · · |>.run) init
```

`Vector.scanlM_map` (theorem, [line 250](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L250))

```lean
theorem scanlM_map [Monad m] [LawfulMonad m] {f : α₁ → α₂} {g : β → α₂ → m β} {as : Vector α₁ n} :
    (as.map f).scanlM g init = as.scanlM (g · <| f ·) init
```

`Vector.scanrM_map` (theorem, [line 256](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L256))

```lean
theorem scanrM_map [Monad m] [LawfulMonad m] {f : α₁ → α₂} {g : α₂ → β → m β} {as : Vector α₁ n} :
    (as.map f).scanrM g init = as.scanrM (fun a b => g (f a) b) init
```

> ### scanl/scanr lemmas

`Vector.scanl_eq_scanlM` (theorem, [line 263](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L263))

```lean
theorem scanl_eq_scanlM {f : β → α → β} {as : Vector α n} :
    as.scanl f init = (as.scanlM (m := Id) (pure <| f · ·) init).run
```

`Vector.scanr_eq_scanrM` (theorem, [line 267](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L267))

```lean
theorem scanr_eq_scanrM {f : α → β → β} {as : Vector α n} :
    as.scanr f init = (as.scanrM (m := Id) (pure <| f · ·) init).run
```

`Vector.toArray_scanl` (theorem, [line 271](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L271))

```lean
theorem toArray_scanl {f : β → α → β} {as : Vector α n} :
    (as.scanl f init).toArray = as.toArray.scanl f init
```

`Vector.toArray_scanr` (theorem, [line 278](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L278))

```lean
theorem toArray_scanr {f : α → β → β} {as : Vector α n} :
    (as.scanr f init).toArray = as.toArray.scanr f init
```

`Vector.toList_scanl` (theorem, [line 286](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L286))

```lean
theorem toList_scanl {f : β → α → β} {as : Vector α n} :
    (as.scanl f init).toList = as.toList.scanl f init
```

`Vector.toList_scanr` (theorem, [line 291](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L291))

```lean
theorem toList_scanr {f : α → β → β} {as : Vector α n} :
    (as.scanr f init).toList = as.toList.scanr f init
```

`Vector.scanl_empty` (theorem, [line 296](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L296))

```lean
theorem scanl_empty {f : β → α → β} :
    #v[].scanl f init = #v[init]
```

`Vector.scanr_empty` (theorem, [line 302](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L302))

```lean
theorem scanr_empty {f : α → β → β} :
    #v[].scanr f init = #v[init]
```

`Vector.scanl_singleton` (theorem, [line 308](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L308))

```lean
theorem scanl_singleton {f : β → α → β} {a : α} :
    #v[a].scanl f init = #v[init, f init a]
```

`Vector.getElem_scanl` (theorem, [line 314](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L314))

```lean
theorem getElem_scanl {f : β → α → β} {as : Vector α n} (h : i < n + 1) :
    (as.scanl f init)[i] = (as.take i).foldl f init
```

`Vector.getElem_scanr` (theorem, [line 322](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L322))

```lean
theorem getElem_scanr {f : α → β → β} {as : Vector α n} (h : i < n + 1) :
    (as.scanr f init)[i] = (as.drop i).foldr f init
```

`Vector.getElem?_scanl` (theorem, [line 330](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L330))

```lean
theorem getElem?_scanl {f : β → α → β} {as : Vector α n} :
    (as.scanl f init)[i]? = if i ≤ n then some ((as.take i).foldl f init) else none
```

`Vector.getElem?_scanr` (theorem, [line 338](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L338))

```lean
theorem getElem?_scanr {f : α → β → β} {as : Vector α n} :
    (as.scanr f init)[i]? = if i < n + 1 then some ((as.drop i).foldr f init)
      else none
```

`Vector.getElem_scanl_zero` (theorem, [line 346](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L346))

```lean
theorem getElem_scanl_zero {f : β → α → β} {as : Vector α n} :
    (as.scanl f init)[0] = init
```

`Vector.getElem_scanr_zero` (theorem, [line 349](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L349))

```lean
theorem getElem_scanr_zero {f : α → β → β} {as : Vector α n} :
    (as.scanr f init)[0] = as.foldr f init
```

`Vector.getElem?_scanl_zero` (theorem, [line 352](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L352))

```lean
theorem getElem?_scanl_zero {f : β → α → β} {as : Vector α n} :
    (as.scanl f init)[0]? = some init
```

`Vector.getElem?_scanr_zero` (theorem, [line 355](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L355))

```lean
theorem getElem?_scanr_zero {f : α → β → β} {as : Vector α n} :
    (as.scanr f init)[0]? = some (as.foldr f init)
```

`Vector.getElem?_succ_scanl` (theorem, [line 358](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L358))

```lean
theorem getElem?_succ_scanl {f : β → α → β} {as : Vector α n} :
    (as.scanl f init)[i + 1]? = (as.scanl f init)[i]?.bind fun x => as[i]?.map fun y => f x y
```

`Vector.getElem_succ_scanl` (theorem, [line 362](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L362))

```lean
theorem getElem_succ_scanl {f : β → α → β} {as : Vector α n} (h : i + 1 < n + 1) :
    (as.scanl f init)[i + 1] = f (as.scanl f init)[i] as[i]
```

`Vector.scanl_push` (theorem, [line 373](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L373))

```lean
theorem scanl_push {f : β → α → β} {as : Vector α n} {a : α} :
    (as.push a).scanl f init = (as.scanl f init).push (f (as.foldl f init) a)
```

`Vector.scanr_push` (theorem, [line 379](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L379))

```lean
theorem scanr_push {f : α → β → β} {as : Vector α n} {a : α} :
    (as.push a).scanr f init = (as.scanr f (f a init)).push init
```

`Vector.scanl_map` (theorem, [line 385](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L385))

```lean
theorem scanl_map {f : γ → β → γ} {g : α → β} {as : Vector α n} :
    (as.map g).scanl f init = as.scanl (f · <| g ·) init
```

`Vector.scanr_map` (theorem, [line 391](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L391))

```lean
theorem scanr_map {f : β → γ → γ} {g : α → β} {as : Vector α n} :
    (as.map g).scanr f init = as.scanr (fun x acc => f (g x) acc) init
```

`Vector.scanl_reverse` (theorem, [line 397](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L397))

```lean
theorem scanl_reverse {f : β → α → β} {as : Vector α n} :
    (as.reverse).scanl f init = (as.scanr (flip f) init).reverse
```

`Vector.scanr_reverse` (theorem, [line 403](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L403))

```lean
theorem scanr_reverse {f : α → β → β} {as : Vector α n} :
    (as.reverse).scanr f init = (as.scanl (flip f) init).reverse
```

`Vector.back_scanl` (theorem, [line 414](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L414))

```lean
theorem back_scanl {f : β → α → β} {as : Vector α n} :
    (as.scanl f init).back = as.foldl f init
```

`Vector.back_scanr` (theorem, [line 428](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L428))

```lean
theorem back_scanr {f : α → β → β} {as : Vector α n} :
    (as.scanr f init).back = init
```

`Vector.back?_scanl` (theorem, [line 432](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L432))

```lean
theorem back?_scanl {f : β → α → β} {as : Vector α n} :
    (as.scanl f init).back? = some (as.foldl f init)
```

`Vector.back?_scanr` (theorem, [line 438](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean#L438))

```lean
theorem back?_scanr {f : α → β → β} {as : Vector α n} :
    (as.scanr f init).back? = some init
```

## Depends on

- [Array/Basic](../../part-01/array/basic.md)
- [Vectors](basic.md)

## Proof depends on

- [Array](../../part-01/array/scan.md)

## Sources

- [Batteries/Data/Vector/Lemmas.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Vector/Lemmas.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Vector.Lemmas.json)

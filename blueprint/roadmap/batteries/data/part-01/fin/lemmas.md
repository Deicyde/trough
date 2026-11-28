---
catalog: module
lean: Fin.foldl_assoc, Fin.foldr_assoc, Fin.coe_clamp, Fin.sum_zero, Fin.sum_succ, Fin.sum_eq_sum_map_finRange, Fin.prod_zero, Fin.prod_succ, Fin.prod_eq_prod_map_finRange, Fin.countP_zero, Fin.countP_one, Fin.countP_succ, Fin.countP_eq_countP_map_finRange, Fin.countP_le, Fin.findSome?_zero, Fin.findSome?_one, Fin.findSome?_succ, Fin.findSome?_succ_of_some, Fin.findSome?_succ_of_isSome, Fin.findSome?_succ_of_none, Fin.findSome?_succ_of_isNone, Fin.findSome?_eq_some_iff, Fin.findSome?_eq_none_iff, Fin.isNone_findSome?_iff, Fin.isSome_findSome?_iff, Fin.exists_minimal_of_findSome?_eq_some, Fin.exists_eq_some_of_findSome?_eq_some, Fin.eq_none_of_findSome?_eq_none, Fin.exists_isSome_of_isSome_findSome?, Fin.isNone_of_isNone_findSome?, Fin.isSome_findSome?_of_isSome, Fin.map_findSome?, Fin.findSome?_guard, Fin.bind_findSome?_guard_isSome, Fin.findSome?_eq_findSome?_finRange, Fin.findSome?_rev, Fin.findSomeRev?_rev, Fin.findSomeRev?_zero, Fin.findSomeRev?_one, Fin.findSomeRev?_succ, Fin.findSomeRev?_eq_some_iff, Fin.findSomeRev?_eq_none_iff, Fin.isNone_findSomeRev?_iff, Fin.isSome_findSomeRev?_iff, Fin.exists_minimal_of_findSomeRev?_eq_some, Fin.exists_eq_some_of_findSomeRev?_eq_some, Fin.eq_none_of_findSomeRev?_eq_none, Fin.exists_isSome_of_isSome_findSomeRev?, Fin.isNone_of_isNone_findSomeRev?, Fin.isSome_findSomeRev?_of_isSome, Fin.map_findSomeRev?, Fin.findSomeRev?_guard, Fin.bind_findSomeRev?_guard_isSome, Fin.find?_zero, Fin.find?_one, Fin.find?_succ, Fin.find?_eq_some_iff, Fin.isSome_find?_iff, Fin.find?_eq_none_iff, Fin.isNone_find?_iff, Fin.eq_true_of_find?_eq_some, Fin.eq_false_of_find?_eq_some_of_lt, Fin.eq_false_of_find?_eq_none, Fin.exists_eq_true_of_isSome_find?, Fin.eq_false_of_isNone_find?, Fin.isSome_find?_of_eq_true, Fin.get_find?_eq_true, Fin.get_find?_minimal, Fin.bind_find?_isSome, Fin.find?_eq_find?_finRange, Fin.exists_eq_true_iff_exists_minimal_eq_true, Fin.exists_iff_exists_minimal, Fin.find?_rev, Fin.map_rev_findRev?, Fin.findRev?_zero, Fin.findRev?_succ, Fin.findRev?_one, Fin.findRev?_eq_some_iff, Fin.findRev?_eq_none_iff, Fin.isSome_findRev?_iff, Fin.isNone_findRev?_iff, Fin.eq_true_of_findRev?_eq_some, Fin.eq_false_of_findRev?_eq_some_of_lt, Fin.eq_false_of_findRev?_eq_none, Fin.exists_eq_true_of_isSome_findRev?, Fin.eq_false_of_isNone_findRev?, Fin.isSome_findRev?_of_eq_true, Fin.get_findRev?_eq_true, Fin.get_findRev?_maximal, Fin.exists_eq_true_iff_exists_maximal_eq_true, Fin.exists_iff_exists_maximal, Fin.bind_findRev?_isSome, Fin.findRev?_rev, Fin.map_rev_find?, Fin.find?_le_findRev?, Fin.find?_eq_findRev?_iff, Fin.coe_divNat, Fin.coe_modNat, Fin.coe_mkDivMod, Fin.ext_divNat_modNat, Fin.ext_divNat_modNat_iff, Fin.lt_divNat_modNat_iff, Fin.le_divNat_modNat_iff, Fin.divNat_mkDivMod, Fin.modNat_mkDivMod, Fin.mkDivMod_divNat_modNat, Fin.divNat_mkDivMod_modNat, Fin.mkDivMod_inj, Fin.mkDivMod_lt_mkDivMod_iff, Fin.mkDivMod_le_mkDivMod_iff
statement: formalized
proof: formalized
---

# Fin/Lemmas

`Batteries.Data.Fin.Lemmas`, in [Batteries/Data/Fin/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean), by Mario Carneiro.

> ### rev

> ### foldl/foldr

`Fin.foldl_assoc` (theorem, [line 25](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L25))

```lean
theorem foldl_assoc {op : α → α → α} [ha : Std.Associative op] {f : Fin n → α} {a₁ a₂} :
    foldl n (fun x i => op x (f i)) (op a₁ a₂) = op a₁ (foldl n (fun x i => op x (f i)) a₂)
```

`Fin.foldr_assoc` (theorem, [line 31](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L31))

```lean
theorem foldr_assoc {op : α → α → α} [ha : Std.Associative op] {f : Fin n → α} {a₁ a₂} :
    foldr n (fun i x => op (f i) x) (op a₁ a₂) = op (foldr n (fun i x => op (f i) x) a₁) a₂
```

> ### clamp

`Fin.coe_clamp` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L39))

```lean
theorem coe_clamp (n m : Nat) : (clamp n m : Nat) = min n m
```

> ### sum

`Fin.sum_zero` (theorem, [line 44](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L44))

```lean
theorem sum_zero [Zero α] [Add α] (x : Fin 0 → α) :
    Fin.sum x = 0
```

`Fin.sum_succ` (theorem, [line 48](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L48))

```lean
theorem sum_succ [Zero α] [Add α] (x : Fin (n + 1) → α) :
    Fin.sum x = x 0 + Fin.sum (x ·.succ)
```

`Fin.sum_eq_sum_map_finRange` (theorem, [line 53](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L53))

```lean
theorem sum_eq_sum_map_finRange [Zero α] [Add α] (x : Fin n → α) :
    Fin.sum x = (List.finRange n |>.map x).sum
```

> ### prod

`Fin.prod_zero` (theorem, [line 60](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L60))

```lean
theorem prod_zero [One α] [Mul α] (x : Fin 0 → α) :
    Fin.prod x = 1
```

`Fin.prod_succ` (theorem, [line 64](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L64))

```lean
theorem prod_succ [One α] [Mul α] (x : Fin (n + 1) → α) :
    Fin.prod x = x 0 * Fin.prod (x ·.succ)
```

`Fin.prod_eq_prod_map_finRange` (theorem, [line 69](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L69))

```lean
theorem prod_eq_prod_map_finRange [One α] [Mul α] (x : Fin n → α) :
    Fin.prod x = (List.finRange n |>.map x).prod
```

> ### countP

`Fin.countP_zero` (theorem, [line 75](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L75))

```lean
theorem countP_zero (p : Fin 0 → Bool) : Fin.countP p = 0
```

`Fin.countP_one` (theorem, [line 78](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L78))

```lean
theorem countP_one (p : Fin 1 → Bool) : Fin.countP p = (p 0).toNat
```

`Fin.countP_succ` (theorem, [line 81](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L81))

```lean
theorem countP_succ (p : Fin (n + 1) → Bool) :
    Fin.countP p = (p 0).toNat + Fin.countP (p ·.succ)
```

`Fin.countP_eq_countP_map_finRange` (theorem, [line 86](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L86))

```lean
theorem countP_eq_countP_map_finRange (x : Fin n → Bool) :
    Fin.countP x = (List.finRange n).countP x
```

`Fin.countP_le` (theorem, [line 94](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L94))

```lean
theorem countP_le (p : Fin n → Bool) : Fin.countP p ≤ n
```

> ### findSome?

`Fin.findSome?_zero` (theorem, [line 104](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L104))

```lean
theorem findSome?_zero {f : Fin 0 → Option α} : findSome? f = none
```

`Fin.findSome?_one` (theorem, [line 106](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L106))

```lean
theorem findSome?_one {f : Fin 1 → Option α} : findSome? f = f 0
```

`Fin.findSome?_succ` (theorem, [line 109](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L109))

```lean
theorem findSome?_succ {f : Fin (n+1) → Option α} :
    findSome? f = (f 0).or (findSome? (f ·.succ))
```

`Fin.findSome?_succ_of_some` (theorem, [line 114](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L114))

```lean
theorem findSome?_succ_of_some {f : Fin (n+1) → Option α} (h : f 0 = some x) :
    findSome? f = some x
```

`Fin.findSome?_succ_of_isSome` (theorem, [line 117](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L117))

```lean
theorem findSome?_succ_of_isSome {f : Fin (n+1) → Option α} (h : (f 0).isSome) :
    findSome? f = f 0
```

`Fin.findSome?_succ_of_none` (theorem, [line 120](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L120))

```lean
theorem findSome?_succ_of_none {f : Fin (n+1) → Option α} (h : f 0 = none) :
    findSome? f = findSome? (f ·.succ)
```

`Fin.findSome?_succ_of_isNone` (theorem, [line 123](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L123))

```lean
theorem findSome?_succ_of_isNone {f : Fin (n+1) → Option α} (h : (f 0).isNone) :
    findSome? f = findSome? (f ·.succ)
```

`Fin.findSome?_eq_some_iff` (theorem, [line 127](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L127))

```lean
theorem findSome?_eq_some_iff {f : Fin n → Option α} :
    findSome? f = some a ↔ ∃ i, f i = some a ∧ ∀ j < i, f j = none
```

`Fin.findSome?_eq_none_iff` (theorem, [line 137](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L137))

```lean
theorem findSome?_eq_none_iff {f : Fin n → Option α} :
    findSome? f = none ↔ ∀ i, f i = none
```

`Fin.isNone_findSome?_iff` (theorem, [line 143](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L143))

```lean
theorem isNone_findSome?_iff {f : Fin n → Option α} :
    (findSome? f).isNone ↔ ∀ i, (f i).isNone
```

`Fin.isSome_findSome?_iff` (theorem, [line 146](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L146))

```lean
theorem isSome_findSome?_iff {f : Fin n → Option α} :
    (findSome? f).isSome ↔ ∃ i, (f i).isSome
```

`Fin.exists_minimal_of_findSome?_eq_some` (theorem, [line 150](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L150))

```lean
theorem exists_minimal_of_findSome?_eq_some {f : Fin n → Option α}
    (h : findSome? f = some x) : ∃ i, f i = some x ∧ ∀ j < i, f j = none
```

`Fin.exists_eq_some_of_findSome?_eq_some` (theorem, [line 154](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L154))

```lean
theorem exists_eq_some_of_findSome?_eq_some {f : Fin n → Option α}
    (h : findSome? f = some x) : ∃ i, f i = some x
```

`Fin.eq_none_of_findSome?_eq_none` (theorem, [line 157](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L157))

```lean
theorem eq_none_of_findSome?_eq_none {f : Fin n → Option α} (h : findSome? f = none) (i) :
    f i = none
```

`Fin.exists_isSome_of_isSome_findSome?` (theorem, [line 160](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L160))

```lean
theorem exists_isSome_of_isSome_findSome? {f : Fin n → Option α} (h : (findSome? f).isSome) :
    ∃ i, (f i).isSome
```

`Fin.isNone_of_isNone_findSome?` (theorem, [line 163](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L163))

```lean
theorem isNone_of_isNone_findSome? {f : Fin n → Option α} (h : (findSome? f).isNone) :
    (f i).isNone
```

`Fin.isSome_findSome?_of_isSome` (theorem, [line 166](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L166))

```lean
theorem isSome_findSome?_of_isSome {f : Fin n → Option α} (h : (f i).isSome) :
    (findSome? f).isSome
```

`Fin.map_findSome?` (theorem, [line 169](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L169))

```lean
theorem map_findSome? (f : Fin n → Option α) (g : α → β) :
    (findSome? f).map g = findSome? (Option.map g <| f ·)
```

`Fin.findSome?_guard` (theorem, [line 175](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L175))

```lean
theorem findSome?_guard {p : Fin n → Bool} : findSome? (Option.guard p) = find? p
```

`Fin.bind_findSome?_guard_isSome` (theorem, [line 177](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L177))

```lean
theorem bind_findSome?_guard_isSome {f : Fin n → Option α} :
    (findSome? (Option.guard fun i => (f i).isSome)).bind f = findSome? f
```

`Fin.findSome?_eq_findSome?_finRange` (theorem, [line 186](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L186))

```lean
theorem findSome?_eq_findSome?_finRange (f : Fin n → Option α) :
    findSome? f = (List.finRange n).findSome? f
```

> ### findSomeRev?

`Fin.findSome?_rev` (theorem, [line 197](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L197))

```lean
theorem findSome?_rev {f : Fin n → Option α} : findSome? (f ·.rev) = findSomeRev? f
```

`Fin.findSomeRev?_rev` (theorem, [line 200](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L200))

```lean
theorem findSomeRev?_rev {f : Fin n → Option α} :
    findSomeRev? (f ·.rev) = findSome? f
```

`Fin.findSomeRev?_zero` (theorem, [line 203](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L203))

```lean
theorem findSomeRev?_zero {f : Fin 0 → Option α} : findSomeRev? f = none
```

`Fin.findSomeRev?_one` (theorem, [line 206](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L206))

```lean
theorem findSomeRev?_one {f : Fin 1 → Option α} : findSomeRev? f = f 0
```

`Fin.findSomeRev?_succ` (theorem, [line 209](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L209))

```lean
theorem findSomeRev?_succ {f : Fin (n+1) → Option α} :
    findSomeRev? f = (f (last n)).or (findSomeRev? fun i => f i.castSucc)
```

`Fin.findSomeRev?_eq_some_iff` (theorem, [line 215](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L215))

```lean
theorem findSomeRev?_eq_some_iff {f : Fin n → Option α} :
    findSomeRev? f = some a ↔ ∃ i, f i = some a ∧ ∀ j, i < j → f j = none
```

`Fin.findSomeRev?_eq_none_iff` (theorem, [line 220](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L220))

```lean
theorem findSomeRev?_eq_none_iff {f : Fin n → Option α} :
    findSomeRev? f = none ↔ ∀ i, f i = none
```

`Fin.isNone_findSomeRev?_iff` (theorem, [line 224](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L224))

```lean
theorem isNone_findSomeRev?_iff {f : Fin n → Option α} :
    (findSomeRev? f).isNone ↔ ∀ i, (f i).isNone
```

`Fin.isSome_findSomeRev?_iff` (theorem, [line 227](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L227))

```lean
theorem isSome_findSomeRev?_iff {f : Fin n → Option α} :
    (findSomeRev? f).isSome ↔ ∃ i, (f i).isSome
```

`Fin.exists_minimal_of_findSomeRev?_eq_some` (theorem, [line 231](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L231))

```lean
theorem exists_minimal_of_findSomeRev?_eq_some {f : Fin n → Option α}
    (h : findSomeRev? f = some x) : ∃ i, f i = some x ∧ ∀ j, i < j → f j = none
```

`Fin.exists_eq_some_of_findSomeRev?_eq_some` (theorem, [line 235](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L235))

```lean
theorem exists_eq_some_of_findSomeRev?_eq_some {f : Fin n → Option α}
    (h : findSomeRev? f = some x) : ∃ i, f i = some x
```

`Fin.eq_none_of_findSomeRev?_eq_none` (theorem, [line 238](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L238))

```lean
theorem eq_none_of_findSomeRev?_eq_none {f : Fin n → Option α} (h : findSomeRev? f = none) (i) :
    f i = none
```

`Fin.exists_isSome_of_isSome_findSomeRev?` (theorem, [line 241](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L241))

```lean
theorem exists_isSome_of_isSome_findSomeRev? {f : Fin n → Option α} (h : (findSomeRev? f).isSome) :
    ∃ i, (f i).isSome
```

`Fin.isNone_of_isNone_findSomeRev?` (theorem, [line 244](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L244))

```lean
theorem isNone_of_isNone_findSomeRev? {f : Fin n → Option α} (h : (findSomeRev? f).isNone) :
    (f i).isNone
```

`Fin.isSome_findSomeRev?_of_isSome` (theorem, [line 247](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L247))

```lean
theorem isSome_findSomeRev?_of_isSome {f : Fin n → Option α} (h : (f i).isSome) :
    (findSomeRev? f).isSome
```

`Fin.map_findSomeRev?` (theorem, [line 250](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L250))

```lean
theorem map_findSomeRev? (f : Fin n → Option α) (g : α → β) :
    (findSomeRev? f).map g = findSomeRev? (Option.map g <| f ·)
```

`Fin.findSomeRev?_guard` (theorem, [line 257](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L257))

```lean
theorem findSomeRev?_guard {p : Fin n → Bool} : findSomeRev? (Option.guard p) = findRev? p
```

`Fin.bind_findSomeRev?_guard_isSome` (theorem, [line 259](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L259))

```lean
theorem bind_findSomeRev?_guard_isSome {f : Fin n → Option α} :
    (findSomeRev? (Option.guard fun i => (f i).isSome)).bind f = findSomeRev? f
```

> ### find?

`Fin.find?_zero` (theorem, [line 269](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L269))

```lean
theorem find?_zero {p : Fin 0 → Bool} : find? p = none
```

`Fin.find?_one` (theorem, [line 271](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L271))

```lean
theorem find?_one {p : Fin 1 → Bool} : find? p = if p 0 then some 0 else none
```

`Fin.find?_succ` (theorem, [line 274](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L274))

```lean
theorem find?_succ {p : Fin (n+1) → Bool} :
    find? p = if p 0 then some 0 else (find? (p ·.succ)).map Fin.succ
```

`Fin.find?_eq_some_iff` (theorem, [line 280](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L280))

```lean
theorem find?_eq_some_iff {p : Fin n → Bool} :
    find? p = some i ↔ p i ∧ ∀ j, j < i → p j = false
```

`Fin.isSome_find?_iff` (theorem, [line 283](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L283))

```lean
theorem isSome_find?_iff {p : Fin n → Bool} :
    (find? p).isSome ↔ ∃ i, p i
```

`Fin.find?_eq_none_iff` (theorem, [line 287](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L287))

```lean
theorem find?_eq_none_iff {p : Fin n → Bool} : find? p = none ↔ ∀ i, p i = false
```

`Fin.isNone_find?_iff` (theorem, [line 289](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L289))

```lean
theorem isNone_find?_iff {p : Fin n → Bool} : (find? p).isNone ↔ ∀ i, p i = false
```

`Fin.eq_true_of_find?_eq_some` (theorem, [line 291](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L291))

```lean
theorem eq_true_of_find?_eq_some {p : Fin n → Bool} (h : find? p = some i) : p i
```

`Fin.eq_false_of_find?_eq_some_of_lt` (theorem, [line 294](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L294))

```lean
theorem eq_false_of_find?_eq_some_of_lt {p : Fin n → Bool} (h : find? p = some i) :
    ∀ j < i, p j = false
```

`Fin.eq_false_of_find?_eq_none` (theorem, [line 297](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L297))

```lean
theorem eq_false_of_find?_eq_none {p : Fin n → Bool} (h : find? p = none) (i) :
    p i = false
```

`Fin.exists_eq_true_of_isSome_find?` (theorem, [line 300](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L300))

```lean
theorem exists_eq_true_of_isSome_find? {p : Fin n → Bool} (h : (find? p).isSome) :
    ∃ i, p i
```

`Fin.eq_false_of_isNone_find?` (theorem, [line 303](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L303))

```lean
theorem eq_false_of_isNone_find? {p : Fin n → Bool} (h : (find? p).isNone) : p i = false
```

`Fin.isSome_find?_of_eq_true` (theorem, [line 306](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L306))

```lean
theorem isSome_find?_of_eq_true {p : Fin n → Bool} (h : p i) :
    (find? p).isSome
```

`Fin.get_find?_eq_true` (theorem, [line 309](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L309))

```lean
theorem get_find?_eq_true {p : Fin n → Bool} (h : (find? p).isSome) : p ((find? p).get h)
```

`Fin.get_find?_minimal` (theorem, [line 312](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L312))

```lean
theorem get_find?_minimal {p : Fin n → Bool} (h : (find? p).isSome) :
    ∀ j, j < (find? p).get h → p j = false
```

`Fin.bind_find?_isSome` (theorem, [line 316](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L316))

```lean
theorem bind_find?_isSome {f : Fin n → Option α} :
    (find? (fun i => (f i).isSome)).bind f = findSome? f
```

`Fin.find?_eq_find?_finRange` (theorem, [line 319](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L319))

```lean
theorem find?_eq_find?_finRange {p : Fin n → Bool} : find? p = (List.finRange n).find? p
```

`Fin.exists_eq_true_iff_exists_minimal_eq_true` (theorem, [line 322](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L322))

```lean
theorem exists_eq_true_iff_exists_minimal_eq_true (p : Fin n → Bool):
    (∃ i, p i) ↔ ∃ i, p i ∧ ∀ j < i, p j = false
```

`Fin.exists_iff_exists_minimal` (theorem, [line 325](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L325))

```lean
theorem exists_iff_exists_minimal (p : Fin n → Prop) [DecidablePred p] :
    (∃ i, p i) ↔ ∃ i, p i ∧ ∀ j < i, ¬ p j
```

`Fin.find?_rev` (theorem, [line 328](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L328))

```lean
theorem find?_rev {p : Fin n → Bool} : find? (p ·.rev) = (findRev? p).map rev
```

`Fin.map_rev_findRev?` (theorem, [line 331](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L331))

```lean
theorem map_rev_findRev? {p : Fin n → Bool} : (findRev? (p ·.rev)).map rev = find? p
```

> ### findRev?

`Fin.findRev?_zero` (theorem, [line 336](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L336))

```lean
theorem findRev?_zero {p : Fin 0 → Bool} : findRev? p = none
```

`Fin.findRev?_succ` (theorem, [line 338](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L338))

```lean
theorem findRev?_succ {p : Fin (n+1) → Bool} :
    findRev? p = if p (last n) then some (last n)
    else (findRev? fun i => p i.castSucc).map Fin.castSucc
```

`Fin.findRev?_one` (theorem, [line 344](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L344))

```lean
theorem findRev?_one {p : Fin 1 → Bool} : findRev? p = if p 0 then some 0 else none
```

`Fin.findRev?_eq_some_iff` (theorem, [line 348](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L348))

```lean
theorem findRev?_eq_some_iff {p : Fin n → Bool} :
    findRev? p = some i ↔ p i ∧ ∀ j, i < j → p j = false
```

`Fin.findRev?_eq_none_iff` (theorem, [line 352](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L352))

```lean
theorem findRev?_eq_none_iff {p : Fin n → Bool} : findRev? p = none ↔ ∀ i, p i = false
```

`Fin.isSome_findRev?_iff` (theorem, [line 354](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L354))

```lean
theorem isSome_findRev?_iff {p : Fin n → Bool} :
    (findRev? p).isSome ↔ ∃ i, p i
```

`Fin.isNone_findRev?_iff` (theorem, [line 357](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L357))

```lean
theorem isNone_findRev?_iff {p : Fin n → Bool} : (findRev? p).isNone ↔ ∀ i, p i = false
```

`Fin.eq_true_of_findRev?_eq_some` (theorem, [line 359](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L359))

```lean
theorem eq_true_of_findRev?_eq_some {p : Fin n → Bool} (h : findRev? p = some i) : p i
```

`Fin.eq_false_of_findRev?_eq_some_of_lt` (theorem, [line 362](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L362))

```lean
theorem eq_false_of_findRev?_eq_some_of_lt {p : Fin n → Bool} (h : findRev? p = some i) :
    ∀ j, i < j → p j = false
```

`Fin.eq_false_of_findRev?_eq_none` (theorem, [line 365](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L365))

```lean
theorem eq_false_of_findRev?_eq_none {p : Fin n → Bool} (h : findRev? p = none) (i) :
    p i = false
```

`Fin.exists_eq_true_of_isSome_findRev?` (theorem, [line 368](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L368))

```lean
theorem exists_eq_true_of_isSome_findRev? {p : Fin n → Bool} (h : (findRev? p).isSome) :
    ∃ i, p i
```

`Fin.eq_false_of_isNone_findRev?` (theorem, [line 371](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L371))

```lean
theorem eq_false_of_isNone_findRev? {p : Fin n → Bool} (h : (findRev? p).isNone) : p i = false
```

`Fin.isSome_findRev?_of_eq_true` (theorem, [line 374](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L374))

```lean
theorem isSome_findRev?_of_eq_true {p : Fin n → Bool} (h : p i) :
    (findRev? p).isSome
```

`Fin.get_findRev?_eq_true` (theorem, [line 377](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L377))

```lean
theorem get_findRev?_eq_true {p : Fin n → Bool} (h : (findRev? p).isSome) :
    p ((findRev? p).get h)
```

`Fin.get_findRev?_maximal` (theorem, [line 380](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L380))

```lean
theorem get_findRev?_maximal {p : Fin n → Bool} (h : (findRev? p).isSome) :
    ∀ j, (findRev? p).get h < j → p j = false
```

`Fin.exists_eq_true_iff_exists_maximal_eq_true` (theorem, [line 384](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L384))

```lean
theorem exists_eq_true_iff_exists_maximal_eq_true (p : Fin n → Bool):
    (∃ i, p i) ↔ ∃ i, p i ∧ ∀ j , i < j → p j = false
```

`Fin.exists_iff_exists_maximal` (theorem, [line 387](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L387))

```lean
theorem exists_iff_exists_maximal (p : Fin n → Prop) [DecidablePred p] :
    (∃ i, p i) ↔ ∃ i, p i ∧ ∀ j, i < j → ¬ p j
```

`Fin.bind_findRev?_isSome` (theorem, [line 390](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L390))

```lean
theorem bind_findRev?_isSome {f : Fin n → Option α} :
    (findRev? (fun i => (f i).isSome)).bind f = findSomeRev? f
```

`Fin.findRev?_rev` (theorem, [line 393](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L393))

```lean
theorem findRev?_rev {p : Fin n → Bool} : findRev? (p ·.rev) = (find? p).map rev
```

`Fin.map_rev_find?` (theorem, [line 396](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L396))

```lean
theorem map_rev_find? {p : Fin n → Bool} : (find? (p ·.rev)).map rev = findRev? p
```

`Fin.find?_le_findRev?` (theorem, [line 399](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L399))

```lean
theorem find?_le_findRev? {p : Fin n → Bool} : find? p ≤ findRev? p
```

`Fin.find?_eq_findRev?_iff` (theorem, [line 402](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L402))

```lean
theorem find?_eq_findRev?_iff {p : Fin n → Bool} : find? p = findRev? p ↔
    ∀ i j, p i = true → p j = true → i = j
```

> ### divNat / modNat / mkDivMod

`Fin.coe_divNat` (theorem, [line 408](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L408))

```lean
theorem coe_divNat (i : Fin (m * n)) : (i.divNat : Nat) = i / n
```

`Fin.coe_modNat` (theorem, [line 410](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L410))

```lean
theorem coe_modNat (i : Fin (m * n)) : (i.modNat : Nat) = i % n
```

`Fin.coe_mkDivMod` (theorem, [line 412](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L412))

```lean
theorem coe_mkDivMod (i : Fin m) (j : Fin n) :
    (mkDivMod i j : Nat) = i.val.mkDivMod j
```

`Fin.ext_divNat_modNat` (theorem, [line 415](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L415))

```lean
theorem ext_divNat_modNat {a b : Fin (m * n)} (h0 : a.divNat = b.divNat)
    (h1 : a.modNat = b.modNat) : a = b
```

`Fin.ext_divNat_modNat_iff` (theorem, [line 419](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L419))

```lean
theorem ext_divNat_modNat_iff {a b : Fin (m * n)} :
    a = b ↔ a.divNat = b.divNat ∧ a.modNat = b.modNat
```

`Fin.lt_divNat_modNat_iff` (theorem, [line 423](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L423))

```lean
theorem lt_divNat_modNat_iff {a b : Fin (m * n)} :
    a < b ↔ a.divNat < b.divNat ∨ a.divNat = b.divNat ∧ a.modNat < b.modNat
```

`Fin.le_divNat_modNat_iff` (theorem, [line 427](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L427))

```lean
theorem le_divNat_modNat_iff {a b : Fin (m * n)} :
    a ≤ b ↔ a.divNat < b.divNat ∨ a.divNat = b.divNat ∧ a.modNat ≤ b.modNat
```

`Fin.divNat_mkDivMod` (theorem, [line 431](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L431))

```lean
theorem divNat_mkDivMod (i : Fin m) (j : Fin n) : (mkDivMod i j).divNat = i
```

`Fin.modNat_mkDivMod` (theorem, [line 434](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L434))

```lean
theorem modNat_mkDivMod (i : Fin m) (j : Fin n) : (mkDivMod i j).modNat = j
```

`Fin.mkDivMod_divNat_modNat` (theorem, [line 437](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L437))

```lean
theorem mkDivMod_divNat_modNat (k : Fin (m * n)) :
    k.divNat.mkDivMod k.modNat = k
```

`Fin.divNat_mkDivMod_modNat` (alias, [line 441](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L441))

```lean
alias divNat_mkDivMod_modNat
```

`Fin.mkDivMod_inj` (theorem, [line 443](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L443))

```lean
theorem mkDivMod_inj {i₁ i₂ : Fin m} {j₁ j₂ : Fin n} :
    mkDivMod i₁ j₁ = mkDivMod i₂ j₂ ↔ i₁ = i₂ ∧ j₁ = j₂
```

`Fin.mkDivMod_lt_mkDivMod_iff` (theorem, [line 447](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L447))

```lean
theorem mkDivMod_lt_mkDivMod_iff {i₁ i₂ : Fin m} {j₁ j₂ : Fin n} :
    mkDivMod i₁ j₁ < mkDivMod i₂ j₂ ↔ i₁ < i₂ ∨ i₁ = i₂ ∧ j₁ < j₂
```

`Fin.mkDivMod_le_mkDivMod_iff` (theorem, [line 451](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean#L451))

```lean
theorem mkDivMod_le_mkDivMod_iff {i₁ i₂ : Fin m} {j₁ j₂ : Fin n} :
    mkDivMod i₁ j₁ ≤ mkDivMod i₂ j₂ ↔ i₁ < i₂ ∨ i₁ = i₂ ∧ j₁ ≤ j₂
```

## Depends on

- [Fin/Basic](basic.md)

## Sources

- [Batteries/Data/Fin/Lemmas.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Data/Fin/Lemmas.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.Fin.Lemmas.json)

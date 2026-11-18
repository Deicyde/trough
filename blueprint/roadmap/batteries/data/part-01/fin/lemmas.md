---
catalog: module
lean: Fin.foldl_assoc, Fin.foldr_assoc, Fin.coe_clamp, Fin.sum_zero, Fin.sum_succ, Fin.sum_eq_sum_map_finRange, Fin.prod_zero, Fin.prod_succ, Fin.prod_eq_prod_map_finRange, Fin.countP_zero, Fin.countP_one, Fin.countP_succ, Fin.countP_eq_countP_map_finRange, Fin.countP_le, Fin.findSome?_zero, Fin.findSome?_one, Fin.findSome?_succ, Fin.findSome?_succ_of_some, Fin.findSome?_succ_of_isSome, Fin.findSome?_succ_of_none, Fin.findSome?_succ_of_isNone, Fin.findSome?_eq_some_iff, Fin.findSome?_eq_none_iff, Fin.isNone_findSome?_iff, Fin.isSome_findSome?_iff, Fin.exists_minimal_of_findSome?_eq_some, Fin.exists_eq_some_of_findSome?_eq_some, Fin.eq_none_of_findSome?_eq_none, Fin.exists_isSome_of_isSome_findSome?, Fin.isNone_of_isNone_findSome?, Fin.isSome_findSome?_of_isSome, Fin.map_findSome?, Fin.findSome?_guard, Fin.bind_findSome?_guard_isSome, Fin.findSome?_eq_findSome?_finRange, Fin.findSome?_rev, Fin.findSomeRev?_rev, Fin.findSomeRev?_zero, Fin.findSomeRev?_one, Fin.findSomeRev?_succ, Fin.findSomeRev?_eq_some_iff, Fin.findSomeRev?_eq_none_iff, Fin.isNone_findSomeRev?_iff, Fin.isSome_findSomeRev?_iff, Fin.exists_minimal_of_findSomeRev?_eq_some, Fin.exists_eq_some_of_findSomeRev?_eq_some, Fin.eq_none_of_findSomeRev?_eq_none, Fin.exists_isSome_of_isSome_findSomeRev?, Fin.isNone_of_isNone_findSomeRev?, Fin.isSome_findSomeRev?_of_isSome, Fin.map_findSomeRev?, Fin.findSomeRev?_guard, Fin.bind_findSomeRev?_guard_isSome, Fin.find?_zero, Fin.find?_one, Fin.find?_succ, Fin.find?_eq_some_iff, Fin.isSome_find?_iff, Fin.find?_eq_none_iff, Fin.isNone_find?_iff, Fin.eq_true_of_find?_eq_some, Fin.eq_false_of_find?_eq_some_of_lt, Fin.eq_false_of_find?_eq_none, Fin.exists_eq_true_of_isSome_find?, Fin.eq_false_of_isNone_find?, Fin.isSome_find?_of_eq_true, Fin.get_find?_eq_true, Fin.get_find?_minimal, Fin.bind_find?_isSome, Fin.find?_eq_find?_finRange, Fin.exists_eq_true_iff_exists_minimal_eq_true, Fin.exists_iff_exists_minimal, Fin.find?_rev, Fin.map_rev_findRev?, Fin.findRev?_zero, Fin.findRev?_succ, Fin.findRev?_one, Fin.findRev?_eq_some_iff, Fin.findRev?_eq_none_iff, Fin.isSome_findRev?_iff, Fin.isNone_findRev?_iff, Fin.eq_true_of_findRev?_eq_some, Fin.eq_false_of_findRev?_eq_some_of_lt, Fin.eq_false_of_findRev?_eq_none, Fin.exists_eq_true_of_isSome_findRev?, Fin.eq_false_of_isNone_findRev?, Fin.isSome_findRev?_of_eq_true, Fin.get_findRev?_eq_true, Fin.get_findRev?_maximal, Fin.exists_eq_true_iff_exists_maximal_eq_true, Fin.exists_iff_exists_maximal, Fin.bind_findRev?_isSome, Fin.findRev?_rev, Fin.map_rev_find?, Fin.find?_le_findRev?, Fin.find?_eq_findRev?_iff, Fin.coe_divNat, Fin.coe_modNat, Fin.coe_mkDivMod, Fin.divNat_mkDivMod, Fin.modNat_mkDivMod, Fin.divNat_mkDivMod_modNat
statement: formalized
proof: formalized
---

# Fin/Lemmas

`Batteries.Data.Fin.Lemmas`, in [Batteries/Data/Fin/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean), by Mario Carneiro.

> ### rev

> ### foldl/foldr

`Fin.foldl_assoc` (theorem, [line 23](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L23))

```lean
theorem foldl_assoc {op : α → α → α} [ha : Std.Associative op] {f : Fin n → α} {a₁ a₂} :
    foldl n (fun x i => op x (f i)) (op a₁ a₂) = op a₁ (foldl n (fun x i => op x (f i)) a₂)
```

`Fin.foldr_assoc` (theorem, [line 29](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L29))

```lean
theorem foldr_assoc {op : α → α → α} [ha : Std.Associative op] {f : Fin n → α} {a₁ a₂} :
    foldr n (fun i x => op (f i) x) (op a₁ a₂) = op (foldr n (fun i x => op (f i) x) a₁) a₂
```

> ### clamp

`Fin.coe_clamp` (theorem, [line 37](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L37))

```lean
theorem coe_clamp (n m : Nat) : (clamp n m : Nat) = min n m
```

> ### sum

`Fin.sum_zero` (theorem, [line 42](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L42))

```lean
theorem sum_zero [Zero α] [Add α] (x : Fin 0 → α) :
    Fin.sum x = 0
```

`Fin.sum_succ` (theorem, [line 46](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L46))

```lean
theorem sum_succ [Zero α] [Add α] (x : Fin (n + 1) → α) :
    Fin.sum x = x 0 + Fin.sum (x ·.succ)
```

`Fin.sum_eq_sum_map_finRange` (theorem, [line 51](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L51))

```lean
theorem sum_eq_sum_map_finRange [Zero α] [Add α] (x : Fin n → α) :
    Fin.sum x = (List.finRange n |>.map x).sum
```

> ### prod

`Fin.prod_zero` (theorem, [line 58](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L58))

```lean
theorem prod_zero [One α] [Mul α] (x : Fin 0 → α) :
    Fin.prod x = 1
```

`Fin.prod_succ` (theorem, [line 62](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L62))

```lean
theorem prod_succ [One α] [Mul α] (x : Fin (n + 1) → α) :
    Fin.prod x = x 0 * Fin.prod (x ·.succ)
```

`Fin.prod_eq_prod_map_finRange` (theorem, [line 67](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L67))

```lean
theorem prod_eq_prod_map_finRange [One α] [Mul α] (x : Fin n → α) :
    Fin.prod x = (List.finRange n |>.map x).prod
```

> ### countP

`Fin.countP_zero` (theorem, [line 73](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L73))

```lean
theorem countP_zero (p : Fin 0 → Bool) : Fin.countP p = 0
```

`Fin.countP_one` (theorem, [line 76](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L76))

```lean
theorem countP_one (p : Fin 1 → Bool) : Fin.countP p = (p 0).toNat
```

`Fin.countP_succ` (theorem, [line 79](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L79))

```lean
theorem countP_succ (p : Fin (n + 1) → Bool) :
    Fin.countP p = (p 0).toNat + Fin.countP (p ·.succ)
```

`Fin.countP_eq_countP_map_finRange` (theorem, [line 84](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L84))

```lean
theorem countP_eq_countP_map_finRange (x : Fin n → Bool) :
    Fin.countP x = (List.finRange n).countP x
```

`Fin.countP_le` (theorem, [line 92](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L92))

```lean
theorem countP_le (p : Fin n → Bool) : Fin.countP p ≤ n
```

> ### findSome?

`Fin.findSome?_zero` (theorem, [line 102](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L102))

```lean
theorem findSome?_zero {f : Fin 0 → Option α} : findSome? f = none
```

`Fin.findSome?_one` (theorem, [line 104](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L104))

```lean
theorem findSome?_one {f : Fin 1 → Option α} : findSome? f = f 0
```

`Fin.findSome?_succ` (theorem, [line 107](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L107))

```lean
theorem findSome?_succ {f : Fin (n+1) → Option α} :
    findSome? f = (f 0).or (findSome? (f ·.succ))
```

`Fin.findSome?_succ_of_some` (theorem, [line 112](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L112))

```lean
theorem findSome?_succ_of_some {f : Fin (n+1) → Option α} (h : f 0 = some x) :
    findSome? f = some x
```

`Fin.findSome?_succ_of_isSome` (theorem, [line 115](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L115))

```lean
theorem findSome?_succ_of_isSome {f : Fin (n+1) → Option α} (h : (f 0).isSome) :
    findSome? f = f 0
```

`Fin.findSome?_succ_of_none` (theorem, [line 118](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L118))

```lean
theorem findSome?_succ_of_none {f : Fin (n+1) → Option α} (h : f 0 = none) :
    findSome? f = findSome? (f ·.succ)
```

`Fin.findSome?_succ_of_isNone` (theorem, [line 121](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L121))

```lean
theorem findSome?_succ_of_isNone {f : Fin (n+1) → Option α} (h : (f 0).isNone) :
    findSome? f = findSome? (f ·.succ)
```

`Fin.findSome?_eq_some_iff` (theorem, [line 125](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L125))

```lean
theorem findSome?_eq_some_iff {f : Fin n → Option α} :
    findSome? f = some a ↔ ∃ i, f i = some a ∧ ∀ j < i, f j = none
```

`Fin.findSome?_eq_none_iff` (theorem, [line 135](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L135))

```lean
theorem findSome?_eq_none_iff {f : Fin n → Option α} :
    findSome? f = none ↔ ∀ i, f i = none
```

`Fin.isNone_findSome?_iff` (theorem, [line 141](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L141))

```lean
theorem isNone_findSome?_iff {f : Fin n → Option α} :
    (findSome? f).isNone ↔ ∀ i, (f i).isNone
```

`Fin.isSome_findSome?_iff` (theorem, [line 144](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L144))

```lean
theorem isSome_findSome?_iff {f : Fin n → Option α} :
    (findSome? f).isSome ↔ ∃ i, (f i).isSome
```

`Fin.exists_minimal_of_findSome?_eq_some` (theorem, [line 148](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L148))

```lean
theorem exists_minimal_of_findSome?_eq_some {f : Fin n → Option α}
    (h : findSome? f = some x) : ∃ i, f i = some x ∧ ∀ j < i, f j = none
```

`Fin.exists_eq_some_of_findSome?_eq_some` (theorem, [line 152](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L152))

```lean
theorem exists_eq_some_of_findSome?_eq_some {f : Fin n → Option α}
    (h : findSome? f = some x) : ∃ i, f i = some x
```

`Fin.eq_none_of_findSome?_eq_none` (theorem, [line 155](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L155))

```lean
theorem eq_none_of_findSome?_eq_none {f : Fin n → Option α} (h : findSome? f = none) (i) :
    f i = none
```

`Fin.exists_isSome_of_isSome_findSome?` (theorem, [line 158](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L158))

```lean
theorem exists_isSome_of_isSome_findSome? {f : Fin n → Option α} (h : (findSome? f).isSome) :
    ∃ i, (f i).isSome
```

`Fin.isNone_of_isNone_findSome?` (theorem, [line 161](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L161))

```lean
theorem isNone_of_isNone_findSome? {f : Fin n → Option α} (h : (findSome? f).isNone) :
    (f i).isNone
```

`Fin.isSome_findSome?_of_isSome` (theorem, [line 164](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L164))

```lean
theorem isSome_findSome?_of_isSome {f : Fin n → Option α} (h : (f i).isSome) :
    (findSome? f).isSome
```

`Fin.map_findSome?` (theorem, [line 167](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L167))

```lean
theorem map_findSome? (f : Fin n → Option α) (g : α → β) :
    (findSome? f).map g = findSome? (Option.map g <| f ·)
```

`Fin.findSome?_guard` (theorem, [line 173](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L173))

```lean
theorem findSome?_guard {p : Fin n → Bool} : findSome? (Option.guard p) = find? p
```

`Fin.bind_findSome?_guard_isSome` (theorem, [line 175](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L175))

```lean
theorem bind_findSome?_guard_isSome {f : Fin n → Option α} :
    (findSome? (Option.guard fun i => (f i).isSome)).bind f = findSome? f
```

`Fin.findSome?_eq_findSome?_finRange` (theorem, [line 184](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L184))

```lean
theorem findSome?_eq_findSome?_finRange (f : Fin n → Option α) :
    findSome? f = (List.finRange n).findSome? f
```

> ### findSomeRev?

`Fin.findSome?_rev` (theorem, [line 195](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L195))

```lean
theorem findSome?_rev {f : Fin n → Option α} : findSome? (f ·.rev) = findSomeRev? f
```

`Fin.findSomeRev?_rev` (theorem, [line 198](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L198))

```lean
theorem findSomeRev?_rev {f : Fin n → Option α} :
    findSomeRev? (f ·.rev) = findSome? f
```

`Fin.findSomeRev?_zero` (theorem, [line 201](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L201))

```lean
theorem findSomeRev?_zero {f : Fin 0 → Option α} : findSomeRev? f = none
```

`Fin.findSomeRev?_one` (theorem, [line 204](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L204))

```lean
theorem findSomeRev?_one {f : Fin 1 → Option α} : findSomeRev? f = f 0
```

`Fin.findSomeRev?_succ` (theorem, [line 207](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L207))

```lean
theorem findSomeRev?_succ {f : Fin (n+1) → Option α} :
    findSomeRev? f = (f (last n)).or (findSomeRev? fun i => f i.castSucc)
```

`Fin.findSomeRev?_eq_some_iff` (theorem, [line 213](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L213))

```lean
theorem findSomeRev?_eq_some_iff {f : Fin n → Option α} :
    findSomeRev? f = some a ↔ ∃ i, f i = some a ∧ ∀ j, i < j → f j = none
```

`Fin.findSomeRev?_eq_none_iff` (theorem, [line 218](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L218))

```lean
theorem findSomeRev?_eq_none_iff {f : Fin n → Option α} :
    findSomeRev? f = none ↔ ∀ i, f i = none
```

`Fin.isNone_findSomeRev?_iff` (theorem, [line 222](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L222))

```lean
theorem isNone_findSomeRev?_iff {f : Fin n → Option α} :
    (findSomeRev? f).isNone ↔ ∀ i, (f i).isNone
```

`Fin.isSome_findSomeRev?_iff` (theorem, [line 225](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L225))

```lean
theorem isSome_findSomeRev?_iff {f : Fin n → Option α} :
    (findSomeRev? f).isSome ↔ ∃ i, (f i).isSome
```

`Fin.exists_minimal_of_findSomeRev?_eq_some` (theorem, [line 229](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L229))

```lean
theorem exists_minimal_of_findSomeRev?_eq_some {f : Fin n → Option α}
    (h : findSomeRev? f = some x) : ∃ i, f i = some x ∧ ∀ j, i < j → f j = none
```

`Fin.exists_eq_some_of_findSomeRev?_eq_some` (theorem, [line 233](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L233))

```lean
theorem exists_eq_some_of_findSomeRev?_eq_some {f : Fin n → Option α}
    (h : findSomeRev? f = some x) : ∃ i, f i = some x
```

`Fin.eq_none_of_findSomeRev?_eq_none` (theorem, [line 236](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L236))

```lean
theorem eq_none_of_findSomeRev?_eq_none {f : Fin n → Option α} (h : findSomeRev? f = none) (i) :
    f i = none
```

`Fin.exists_isSome_of_isSome_findSomeRev?` (theorem, [line 239](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L239))

```lean
theorem exists_isSome_of_isSome_findSomeRev? {f : Fin n → Option α} (h : (findSomeRev? f).isSome) :
    ∃ i, (f i).isSome
```

`Fin.isNone_of_isNone_findSomeRev?` (theorem, [line 242](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L242))

```lean
theorem isNone_of_isNone_findSomeRev? {f : Fin n → Option α} (h : (findSomeRev? f).isNone) :
    (f i).isNone
```

`Fin.isSome_findSomeRev?_of_isSome` (theorem, [line 245](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L245))

```lean
theorem isSome_findSomeRev?_of_isSome {f : Fin n → Option α} (h : (f i).isSome) :
    (findSomeRev? f).isSome
```

`Fin.map_findSomeRev?` (theorem, [line 248](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L248))

```lean
theorem map_findSomeRev? (f : Fin n → Option α) (g : α → β) :
    (findSomeRev? f).map g = findSomeRev? (Option.map g <| f ·)
```

`Fin.findSomeRev?_guard` (theorem, [line 255](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L255))

```lean
theorem findSomeRev?_guard {p : Fin n → Bool} : findSomeRev? (Option.guard p) = findRev? p
```

`Fin.bind_findSomeRev?_guard_isSome` (theorem, [line 257](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L257))

```lean
theorem bind_findSomeRev?_guard_isSome {f : Fin n → Option α} :
    (findSomeRev? (Option.guard fun i => (f i).isSome)).bind f = findSomeRev? f
```

> ### find?

`Fin.find?_zero` (theorem, [line 267](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L267))

```lean
theorem find?_zero {p : Fin 0 → Bool} : find? p = none
```

`Fin.find?_one` (theorem, [line 269](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L269))

```lean
theorem find?_one {p : Fin 1 → Bool} : find? p = if p 0 then some 0 else none
```

`Fin.find?_succ` (theorem, [line 272](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L272))

```lean
theorem find?_succ {p : Fin (n+1) → Bool} :
    find? p = if p 0 then some 0 else (find? (p ·.succ)).map Fin.succ
```

`Fin.find?_eq_some_iff` (theorem, [line 278](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L278))

```lean
theorem find?_eq_some_iff {p : Fin n → Bool} :
    find? p = some i ↔ p i ∧ ∀ j, j < i → p j = false
```

`Fin.isSome_find?_iff` (theorem, [line 281](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L281))

```lean
theorem isSome_find?_iff {p : Fin n → Bool} :
    (find? p).isSome ↔ ∃ i, p i
```

`Fin.find?_eq_none_iff` (theorem, [line 285](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L285))

```lean
theorem find?_eq_none_iff {p : Fin n → Bool} : find? p = none ↔ ∀ i, p i = false
```

`Fin.isNone_find?_iff` (theorem, [line 287](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L287))

```lean
theorem isNone_find?_iff {p : Fin n → Bool} : (find? p).isNone ↔ ∀ i, p i = false
```

`Fin.eq_true_of_find?_eq_some` (theorem, [line 289](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L289))

```lean
theorem eq_true_of_find?_eq_some {p : Fin n → Bool} (h : find? p = some i) : p i
```

`Fin.eq_false_of_find?_eq_some_of_lt` (theorem, [line 292](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L292))

```lean
theorem eq_false_of_find?_eq_some_of_lt {p : Fin n → Bool} (h : find? p = some i) :
    ∀ j < i, p j = false
```

`Fin.eq_false_of_find?_eq_none` (theorem, [line 295](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L295))

```lean
theorem eq_false_of_find?_eq_none {p : Fin n → Bool} (h : find? p = none) (i) :
    p i = false
```

`Fin.exists_eq_true_of_isSome_find?` (theorem, [line 298](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L298))

```lean
theorem exists_eq_true_of_isSome_find? {p : Fin n → Bool} (h : (find? p).isSome) :
    ∃ i, p i
```

`Fin.eq_false_of_isNone_find?` (theorem, [line 301](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L301))

```lean
theorem eq_false_of_isNone_find? {p : Fin n → Bool} (h : (find? p).isNone) : p i = false
```

`Fin.isSome_find?_of_eq_true` (theorem, [line 304](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L304))

```lean
theorem isSome_find?_of_eq_true {p : Fin n → Bool} (h : p i) :
    (find? p).isSome
```

`Fin.get_find?_eq_true` (theorem, [line 307](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L307))

```lean
theorem get_find?_eq_true {p : Fin n → Bool} (h : (find? p).isSome) : p ((find? p).get h)
```

`Fin.get_find?_minimal` (theorem, [line 310](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L310))

```lean
theorem get_find?_minimal {p : Fin n → Bool} (h : (find? p).isSome) :
    ∀ j, j < (find? p).get h → p j = false
```

`Fin.bind_find?_isSome` (theorem, [line 314](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L314))

```lean
theorem bind_find?_isSome {f : Fin n → Option α} :
    (find? (fun i => (f i).isSome)).bind f = findSome? f
```

`Fin.find?_eq_find?_finRange` (theorem, [line 317](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L317))

```lean
theorem find?_eq_find?_finRange {p : Fin n → Bool} : find? p = (List.finRange n).find? p
```

`Fin.exists_eq_true_iff_exists_minimal_eq_true` (theorem, [line 320](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L320))

```lean
theorem exists_eq_true_iff_exists_minimal_eq_true (p : Fin n → Bool):
    (∃ i, p i) ↔ ∃ i, p i ∧ ∀ j < i, p j = false
```

`Fin.exists_iff_exists_minimal` (theorem, [line 323](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L323))

```lean
theorem exists_iff_exists_minimal (p : Fin n → Prop) [DecidablePred p] :
    (∃ i, p i) ↔ ∃ i, p i ∧ ∀ j < i, ¬ p j
```

`Fin.find?_rev` (theorem, [line 326](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L326))

```lean
theorem find?_rev {p : Fin n → Bool} : find? (p ·.rev) = (findRev? p).map rev
```

`Fin.map_rev_findRev?` (theorem, [line 329](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L329))

```lean
theorem map_rev_findRev? {p : Fin n → Bool} : (findRev? (p ·.rev)).map rev = find? p
```

> ### findRev?

`Fin.findRev?_zero` (theorem, [line 334](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L334))

```lean
theorem findRev?_zero {p : Fin 0 → Bool} : findRev? p = none
```

`Fin.findRev?_succ` (theorem, [line 336](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L336))

```lean
theorem findRev?_succ {p : Fin (n+1) → Bool} :
    findRev? p = if p (last n) then some (last n)
    else (findRev? fun i => p i.castSucc).map Fin.castSucc
```

`Fin.findRev?_one` (theorem, [line 342](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L342))

```lean
theorem findRev?_one {p : Fin 1 → Bool} : findRev? p = if p 0 then some 0 else none
```

`Fin.findRev?_eq_some_iff` (theorem, [line 346](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L346))

```lean
theorem findRev?_eq_some_iff {p : Fin n → Bool} :
    findRev? p = some i ↔ p i ∧ ∀ j, i < j → p j = false
```

`Fin.findRev?_eq_none_iff` (theorem, [line 350](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L350))

```lean
theorem findRev?_eq_none_iff {p : Fin n → Bool} : findRev? p = none ↔ ∀ i, p i = false
```

`Fin.isSome_findRev?_iff` (theorem, [line 352](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L352))

```lean
theorem isSome_findRev?_iff {p : Fin n → Bool} :
    (findRev? p).isSome ↔ ∃ i, p i
```

`Fin.isNone_findRev?_iff` (theorem, [line 355](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L355))

```lean
theorem isNone_findRev?_iff {p : Fin n → Bool} : (findRev? p).isNone ↔ ∀ i, p i = false
```

`Fin.eq_true_of_findRev?_eq_some` (theorem, [line 357](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L357))

```lean
theorem eq_true_of_findRev?_eq_some {p : Fin n → Bool} (h : findRev? p = some i) : p i
```

`Fin.eq_false_of_findRev?_eq_some_of_lt` (theorem, [line 360](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L360))

```lean
theorem eq_false_of_findRev?_eq_some_of_lt {p : Fin n → Bool} (h : findRev? p = some i) :
    ∀ j, i < j → p j = false
```

`Fin.eq_false_of_findRev?_eq_none` (theorem, [line 363](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L363))

```lean
theorem eq_false_of_findRev?_eq_none {p : Fin n → Bool} (h : findRev? p = none) (i) :
    p i = false
```

`Fin.exists_eq_true_of_isSome_findRev?` (theorem, [line 366](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L366))

```lean
theorem exists_eq_true_of_isSome_findRev? {p : Fin n → Bool} (h : (findRev? p).isSome) :
    ∃ i, p i
```

`Fin.eq_false_of_isNone_findRev?` (theorem, [line 369](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L369))

```lean
theorem eq_false_of_isNone_findRev? {p : Fin n → Bool} (h : (findRev? p).isNone) : p i = false
```

`Fin.isSome_findRev?_of_eq_true` (theorem, [line 372](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L372))

```lean
theorem isSome_findRev?_of_eq_true {p : Fin n → Bool} (h : p i) :
    (findRev? p).isSome
```

`Fin.get_findRev?_eq_true` (theorem, [line 375](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L375))

```lean
theorem get_findRev?_eq_true {p : Fin n → Bool} (h : (findRev? p).isSome) :
    p ((findRev? p).get h)
```

`Fin.get_findRev?_maximal` (theorem, [line 378](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L378))

```lean
theorem get_findRev?_maximal {p : Fin n → Bool} (h : (findRev? p).isSome) :
    ∀ j, (findRev? p).get h < j → p j = false
```

`Fin.exists_eq_true_iff_exists_maximal_eq_true` (theorem, [line 382](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L382))

```lean
theorem exists_eq_true_iff_exists_maximal_eq_true (p : Fin n → Bool):
    (∃ i, p i) ↔ ∃ i, p i ∧ ∀ j , i < j → p j = false
```

`Fin.exists_iff_exists_maximal` (theorem, [line 385](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L385))

```lean
theorem exists_iff_exists_maximal (p : Fin n → Prop) [DecidablePred p] :
    (∃ i, p i) ↔ ∃ i, p i ∧ ∀ j, i < j → ¬ p j
```

`Fin.bind_findRev?_isSome` (theorem, [line 388](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L388))

```lean
theorem bind_findRev?_isSome {f : Fin n → Option α} :
    (findRev? (fun i => (f i).isSome)).bind f = findSomeRev? f
```

`Fin.findRev?_rev` (theorem, [line 391](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L391))

```lean
theorem findRev?_rev {p : Fin n → Bool} : findRev? (p ·.rev) = (find? p).map rev
```

`Fin.map_rev_find?` (theorem, [line 394](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L394))

```lean
theorem map_rev_find? {p : Fin n → Bool} : (find? (p ·.rev)).map rev = findRev? p
```

`Fin.find?_le_findRev?` (theorem, [line 397](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L397))

```lean
theorem find?_le_findRev? {p : Fin n → Bool} : find? p ≤ findRev? p
```

`Fin.find?_eq_findRev?_iff` (theorem, [line 400](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L400))

```lean
theorem find?_eq_findRev?_iff {p : Fin n → Bool} : find? p = findRev? p ↔
    ∀ i j, p i = true → p j = true → i = j
```

> ### divNat / modNat / mkDivMod

`Fin.coe_divNat` (theorem, [line 406](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L406))

```lean
theorem coe_divNat (i : Fin (m * n)) : (i.divNat : Nat) = i / n
```

`Fin.coe_modNat` (theorem, [line 408](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L408))

```lean
theorem coe_modNat (i : Fin (m * n)) : (i.modNat : Nat) = i % n
```

`Fin.coe_mkDivMod` (theorem, [line 410](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L410))

```lean
theorem coe_mkDivMod (i : Fin m) (j : Fin n) : (mkDivMod i j : Nat) = n * i + j
```

`Fin.divNat_mkDivMod` (theorem, [line 412](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L412))

```lean
theorem divNat_mkDivMod (i : Fin m) (j : Fin n) : (mkDivMod i j).divNat = i
```

`Fin.modNat_mkDivMod` (theorem, [line 415](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L415))

```lean
theorem modNat_mkDivMod (i : Fin m) (j : Fin n) : (mkDivMod i j).modNat = j
```

`Fin.divNat_mkDivMod_modNat` (theorem, [line 418](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean#L418))

```lean
theorem divNat_mkDivMod_modNat (k : Fin (m * n)) :
    mkDivMod k.divNat k.modNat = k
```

## Depends on

- [Fin/Basic](basic.md)

## Sources

- [Batteries/Data/Fin/Lemmas.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/Fin/Lemmas.lean)

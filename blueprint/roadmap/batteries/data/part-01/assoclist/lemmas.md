---
catalog: module
lean: Batteries.AssocList.empty_eq, Batteries.AssocList.isEmpty_eq, Batteries.AssocList.length_nil, Batteries.AssocList.length_cons, Batteries.AssocList.length_toList, Batteries.AssocList.forM_eq, Batteries.AssocList.toList_mapKey, Batteries.AssocList.length_mapKey, Batteries.AssocList.toList_mapVal, Batteries.AssocList.length_mapVal, Batteries.AssocList.filterMapVal_nil, Batteries.AssocList.filterMapVal_cons, Batteries.AssocList.toList_filterMapVal, Batteries.AssocList.length_filterMapVal_le, Batteries.AssocList.findEntryP?_eq, Batteries.AssocList.findEntry?_eq, Batteries.AssocList.find?_eq_findEntry?, Batteries.AssocList.find?_eq, Batteries.AssocList.find?_mapVal, Batteries.AssocList.any_eq, Batteries.AssocList.all_eq, Batteries.AssocList.contains_eq, Batteries.AssocList.toList_replace, Batteries.AssocList.length_replace, Batteries.AssocList.toList_eraseP, Batteries.AssocList.toList_erase, Batteries.AssocList.toList_modify, Batteries.AssocList.length_modify, Batteries.AssocList.forIn_eq, List.toList_toAssocList, Batteries.AssocList.toList_toAssocList, List.length_toAssocList, Batteries.AssocList.beq_nil₂, Batteries.AssocList.beq_nil_cons, Batteries.AssocList.beq_cons_nil, Batteries.AssocList.beq_cons₂, Batteries.AssocList.beq_eq
statement: formalized
proof: formalized
---

# Lemmas about association lists

`Batteries.Data.AssocList.Lemmas`, in [Batteries/Data/AssocList/Lemmas.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean), by Leonardo de Moura, Mario Carneiro, Yann Herklotz.

> Each operation on `AssocList` is specified by a lemma relating it to the corresponding
> operation on `List (α × β)`, transported along `AssocList.toList`.

`Batteries.AssocList.empty_eq` (theorem, [line 24](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L24))

```lean
theorem empty_eq : (∅ : AssocList α β) = nil
```

`Batteries.AssocList.isEmpty_eq` (theorem, [line 26](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L26))

```lean
theorem isEmpty_eq (l : AssocList α β) : isEmpty l = l.toList.isEmpty
```

`Batteries.AssocList.length_nil` (theorem, [line 29](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L29))

```lean
theorem length_nil : length (nil : AssocList α β) = 0
```

`Batteries.AssocList.length_cons` (theorem, [line 30](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L30))

```lean
theorem length_cons : length (cons a b t) = length t + 1
```

`Batteries.AssocList.length_toList` (theorem, [line 32](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L32))

```lean
theorem length_toList (l : AssocList α β) : l.toList.length = l.length
```

`Batteries.AssocList.forM_eq` (theorem, [line 35](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L35))

```lean
theorem forM_eq [Monad m] (f : α → β → m PUnit) (l) :
    forM f l = l.toList.forM (fun (a, b) => f a b)
```

`Batteries.AssocList.toList_mapKey` (theorem, [line 39](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L39))

```lean
theorem toList_mapKey (f : α → δ) (l : AssocList α β) :
    (mapKey f l).toList = l.toList.map (fun (a, b) => (f a, b))
```

`Batteries.AssocList.length_mapKey` (theorem, [line 43](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L43))

```lean
theorem length_mapKey : (mapKey f l).length = l.length
```

`Batteries.AssocList.toList_mapVal` (theorem, [line 46](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L46))

```lean
theorem toList_mapVal (f : α → β → δ) (l : AssocList α β) :
    (mapVal f l).toList = l.toList.map (fun (a, b) => (a, f a b))
```

`Batteries.AssocList.length_mapVal` (theorem, [line 50](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L50))

```lean
theorem length_mapVal : (mapVal f l).length = l.length
```

`Batteries.AssocList.filterMapVal_nil` (theorem, [line 53](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L53))

```lean
theorem filterMapVal_nil : filterMapVal f nil = nil
```

`Batteries.AssocList.filterMapVal_cons` (theorem, [line 55](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L55))

```lean
theorem filterMapVal_cons (f : α → β → Option γ) (k) (v) (t) :
    filterMapVal f (.cons k v t) =
      match f k v with
      | none => filterMapVal f t
      | some d => .cons k d (filterMapVal f t)
```

`Batteries.AssocList.toList_filterMapVal` (theorem, [line 61](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L61))

```lean
theorem toList_filterMapVal (f : α → β → Option δ) (l : AssocList α β) :
    (filterMapVal f l).toList =
      l.toList.filterMap (fun (a, b) => (f a b).map fun v => (a, v))
```

`Batteries.AssocList.length_filterMapVal_le` (theorem, [line 73](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L73))

```lean
theorem length_filterMapVal_le : (filterMapVal f l).length ≤ l.length
```

`Batteries.AssocList.findEntryP?_eq` (theorem, [line 82](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L82))

```lean
theorem findEntryP?_eq (p : α → β → Bool) (l : AssocList α β) :
    findEntryP? p l = l.toList.find? fun (a, b) => p a b
```

`Batteries.AssocList.findEntry?_eq` (theorem, [line 86](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L86))

```lean
theorem findEntry?_eq [BEq α] (a : α) (l : AssocList α β) :
    findEntry? a l = l.toList.find? (·.1 == a)
```

`Batteries.AssocList.find?_eq_findEntry?` (theorem, [line 89](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L89))

```lean
theorem find?_eq_findEntry? [BEq α] (a : α) (l : AssocList α β) :
    find? a l = (l.findEntry? a).map (·.2)
```

`Batteries.AssocList.find?_eq` (theorem, [line 93](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L93))

```lean
theorem find?_eq [BEq α] (a : α) (l : AssocList α β) :
    find? a l = (l.toList.find? (·.1 == a)).map (·.2)
```

`Batteries.AssocList.find?_mapVal` (theorem, [line 96](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L96))

```lean
theorem find?_mapVal [BEq α] [LawfulBEq α] (f : α → β → γ)
    (a : α) (l : AssocList α β) :
    (l.mapVal f).find? a = (l.find? a).map (f a)
```

`Batteries.AssocList.any_eq` (theorem, [line 103](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L103))

```lean
theorem any_eq (p : α → β → Bool) (l : AssocList α β) :
    any p l = l.toList.any fun (a, b) => p a b
```

`Batteries.AssocList.all_eq` (theorem, [line 106](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L106))

```lean
theorem all_eq (p : α → β → Bool) (l : AssocList α β) :
    all p l = l.toList.all fun (a, b) => p a b
```

`Batteries.AssocList.contains_eq` (theorem, [line 109](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L109))

```lean
theorem contains_eq [BEq α] (a : α) (l : AssocList α β) :
    contains a l = l.toList.any (·.1 == a)
```

`Batteries.AssocList.toList_replace` (theorem, [line 113](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L113))

```lean
theorem toList_replace [BEq α] (a : α) (b : β) (l : AssocList α β) :
    (replace a b l).toList =
    l.toList.replaceF (bif ·.1 == a then some (a, b) else none)
```

`Batteries.AssocList.length_replace` (theorem, [line 118](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L118))

```lean
theorem length_replace [BEq α] {a : α} : (replace a b l).length = l.length
```

`Batteries.AssocList.toList_eraseP` (theorem, [line 124](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L124))

```lean
theorem toList_eraseP (p) (l : AssocList α β) :
    (eraseP p l).toList = l.toList.eraseP fun (a, b) => p a b
```

`Batteries.AssocList.toList_erase` (theorem, [line 128](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L128))

```lean
theorem toList_erase [BEq α] (a : α) (l : AssocList α β) :
    (erase a l).toList = l.toList.eraseP (·.1 == a)
```

`Batteries.AssocList.toList_modify` (theorem, [line 131](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L131))

```lean
theorem toList_modify [BEq α] (a : α) (l : AssocList α β) :
    (modify a f l).toList =
    l.toList.replaceF fun (k, v) => bif k == a then some (a, f k v) else none
```

`Batteries.AssocList.length_modify` (theorem, [line 138](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L138))

```lean
theorem length_modify [BEq α] {a : α} : (modify a f l).length = l.length
```

`Batteries.AssocList.forIn_eq` (theorem, [line 144](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L144))

```lean
theorem forIn_eq [Monad m] (l : AssocList α β) (init : δ)
    (f : (α × β) → δ → m (ForInStep δ)) : forIn l init f = forIn l.toList init f
```

`List.toList_toAssocList` (theorem, [line 150](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L150))

```lean
theorem _root_.List.toList_toAssocList (l : List (α × β)) : l.toAssocList.toList = l
```

`Batteries.AssocList.toList_toAssocList` (theorem, [line 153](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L153))

```lean
theorem toList_toAssocList (l : AssocList α β) : l.toList.toAssocList = l
```

`List.length_toAssocList` (theorem, [line 156](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L156))

```lean
theorem _root_.List.length_toAssocList (l : List (α × β)) :
    l.toAssocList.length = l.length
```

`Batteries.AssocList.beq_nil₂` (theorem, [line 160](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L160))

```lean
theorem beq_nil₂ [BEq α] [BEq β] : ((.nil : AssocList α β) == .nil) = true
```

`Batteries.AssocList.beq_nil_cons` (theorem, [line 161](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L161))

```lean
theorem beq_nil_cons [BEq α] [BEq β] : ((.nil : AssocList α β) == .cons a b t) = false
```

`Batteries.AssocList.beq_cons_nil` (theorem, [line 163](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L163))

```lean
theorem beq_cons_nil [BEq α] [BEq β] : ((.cons a b t : AssocList α β) == .nil) = false
```

`Batteries.AssocList.beq_cons₂` (theorem, [line 165](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L165))

```lean
theorem beq_cons₂ [BEq α] [BEq β] :
    ((.cons a b t : AssocList α β) == .cons a' b' t') = (a == a' && b == b' && t == t')
```

`Batteries.AssocList.beq_eq` (theorem, [line 180](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean#L180))

```lean
protected theorem beq_eq [BEq α] [BEq β] {l m : AssocList α β} :
    (l == m) = (l.toList == m.toList)
```

## Depends on

- [Association lists](basic.md)
- [List/Basic](../list/part-01/basic.md)

## Sources

- [Batteries/Data/AssocList/Lemmas.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/AssocList/Lemmas.lean)

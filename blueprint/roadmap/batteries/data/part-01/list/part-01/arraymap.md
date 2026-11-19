---
catalog: module
lean: List.toArrayMap, List.toArrayMap_toList, List.toArrayMap_eq_toArray_map
statement: formalized
proof: formalized
---

# ArrayMap

`Batteries.Data.List.ArrayMap`, in [Batteries/Data/List/ArrayMap.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/ArrayMap.lean), by Michael Rothgang.

`List.toArrayMap` (definition, [line 20](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/ArrayMap.lean#L20))

> This function is provided as a more efficient runtime alternative to `(l.map f).toArray`.
> (It avoids the intermediate memory allocation of creating an intermediate list first.)
> For verification purposes, we immediately simplify it to that form.

```lean
def toArrayMap (l : List α) (f : α → β) : Array β
```

`List.toArrayMap_toList` (theorem, [line 27](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/ArrayMap.lean#L27))

```lean
theorem toArrayMap_toList (l : List α) (f : α → β ) : (l.toArrayMap f).toList = l.map f
```

`List.toArrayMap_eq_toArray_map` (theorem, [line 40](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/ArrayMap.lean#L40))

```lean
theorem toArrayMap_eq_toArray_map (l : List α) (f : α → β) : l.toArrayMap f = (l.map f).toArray
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/List/ArrayMap.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Data/List/ArrayMap.lean)
- [Declaration ledger](../../../../../../sources/batteries/Batteries.Data.List.ArrayMap.json)

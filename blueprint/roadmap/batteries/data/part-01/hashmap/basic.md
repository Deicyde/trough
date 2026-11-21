---
catalog: module
lean: Std.HashMap.findEntry?, Std.HashMap.ofListWith, Batteries.HashMap, Batteries.mkHashMap, Batteries.HashMap.empty, Batteries.HashMap.size, Batteries.HashMap.isEmpty, Batteries.HashMap.insert, Batteries.HashMap.insert', Batteries.HashMap.erase, Batteries.HashMap.modify, Batteries.HashMap.find?, Batteries.HashMap.findD, Batteries.HashMap.find!, Batteries.HashMap.findEntry?, Batteries.HashMap.contains, Batteries.HashMap.foldM, Batteries.HashMap.fold, Batteries.HashMap.mergeWithM, Batteries.HashMap.mergeWith, Batteries.HashMap.forM, Batteries.HashMap.toList, Batteries.HashMap.toArray, Batteries.HashMap.numBuckets, Batteries.HashMap.ofList, Batteries.HashMap.ofListWith
statement: formalized
proof: formalized
---

# HashMap/Basic

`Batteries.Data.HashMap.Basic`, in [Batteries/Data/HashMap/Basic.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean), by Leonardo de Moura, Mario Carneiro.

`Std.HashMap.findEntry?` (definition, [line 28](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L28))

> Given a key `a`, returns a key-value pair in the map whose key compares equal to `a`.
> Note that the returned key may not be identical to the input, if `==` ignores some part
> of the value.
> ```
> def hashMap := ofList [("one", 1), ("two", 2)]
> hashMap.findEntry? "one" = some ("one", 1)
> hashMap.findEntry? "three" = none
> ```

```lean
def findEntry? [BEq α] [Hashable α] (m : Std.HashMap α β) (k : α) : Option (α × β)
```

`Std.HashMap.ofListWith` (definition, [line 37](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L37))

> Variant of `ofList` which accepts a function that combines values of duplicated keys.
> ```
> ofListWith [("one", 1), ("one", 2)] (fun v₁ v₂ => v₁ + v₂) = {"one" => 3}
> ```

```lean
def ofListWith [BEq α] [Hashable α] (l : List (α × β)) (f : β → β → β) : HashMap α β
```

`Batteries.HashMap` (structure, [line 55](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L55))

> `HashMap α β` is a key-value map which stores elements in an array using a hash function
> to find the values. This allows it to have very good performance for lookups
> (average `O(1)` for a perfectly random hash function), but it is not a persistent data structure,
> meaning that one should take care to use the map linearly when performing updates.
> Copies are `O(n)`.

```lean
structure _root_.Batteries.HashMap (α : Type u) (β : Type v) [BEq α] [Hashable α] where
  /-- The inner `Std.HashMap` powering the `Batteries.HashMap`. -/
  inner : Std.HashMap α β
```

`Batteries.mkHashMap` (definition, [line 62](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L62))

> Make a new hash map with the specified capacity.

```lean
def _root_.Batteries.mkHashMap [BEq α] [Hashable α] (capacity := 0) : HashMap α β
```

`Batteries.HashMap.empty` (definition, [line 76](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L76))

> Make a new empty hash map.
> ```
> (empty : Batteries.HashMap Int Int).toList = []
> ```

```lean
def empty [BEq α] [Hashable α] : HashMap α β
```

`Batteries.HashMap.size` (definition, [line 86](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L86))

> The number of elements in the hash map.
> ```
> (ofList [("one", 1), ("two", 2)]).size = 2
> ```

```lean
def size (self : HashMap α β) : Nat
```

`Batteries.HashMap.isEmpty` (definition, [line 95](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L95))

> Is the map empty?
> ```
> (empty : Batteries.HashMap Int Int).isEmpty = true
> (ofList [("one", 1), ("two", 2)]).isEmpty = false
> ```

```lean
def isEmpty (self : HashMap α β) : Bool
```

`Batteries.HashMap.insert` (definition, [line 106](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L106))

> Inserts key-value pair `a, b` into the map.
> If an element equal to `a` is already in the map, it is replaced by `b`.
> ```
> def hashMap := ofList [("one", 1), ("two", 2)]
> hashMap.insert "three" 3 = {"one" => 1, "two" => 2, "three" => 3}
> hashMap.insert "two" 0 = {"one" => 1, "two" => 0}
> ```

```lean
def insert (self : HashMap α β) (a : α) (b : β) : HashMap α β
```

`Batteries.HashMap.insert'` (definition, [line 118](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L118))

> Similar to `insert`, but also returns a boolean flag indicating whether an existing entry has been
> replaced with `a => b`.
> ```
> def hashMap := ofList [("one", 1), ("two", 2)]
> hashMap.insert' "three" 3 = ({"one" => 1, "two" => 2, "three" => 3}, false)
> hashMap.insert' "two" 0 = ({"one" => 1, "two" => 0}, true)
> ```

```lean
def insert' (m : HashMap α β) (a : α) (b : β) : HashMap α β × Bool
```

`Batteries.HashMap.erase` (definition, [line 130](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L130))

> Removes key `a` from the map. If it does not exist in the map, the map is returned unchanged.
> ```
> def hashMap := ofList [("one", 1), ("two", 2)]
> hashMap.erase "one" = {"two" => 2}
> hashMap.erase "three" = {"one" => 1, "two" => 2}
> ```

```lean
def erase (self : HashMap α β) (a : α) : HashMap α β
```

`Batteries.HashMap.modify` (definition, [line 140](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L140))

> Performs an in-place edit of the value, ensuring that the value is used linearly.
> The function `f` is passed the original key of the entry, along with the value in the map.
> ```
> (ofList [("one", 1), ("two", 2)]).modify "one" (fun _ v => v + 1) = {"one" => 2, "two" => 2}
> (ofList [("one", 1), ("two", 2)]).modify "three" (fun _ v => v + 1) = {"one" => 1, "two" => 2}
> ```

```lean
def modify (self : HashMap α β) (a : α) (f : α → β → β) : HashMap α β
```

`Batteries.HashMap.find?` (definition, [line 151](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L151))

> Looks up an element in the map with key `a`.
> ```
> def hashMap := ofList [("one", 1), ("two", 2)]
> hashMap.find? "one" = some 1
> hashMap.find? "three" = none
> ```

```lean
def find? (self : HashMap α β) (a : α) : Option β
```

`Batteries.HashMap.findD` (definition, [line 161](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L161))

> Looks up an element in the map with key `a`. Returns `b₀` if the element is not found.
> ```
> def hashMap := ofList [("one", 1), ("two", 2)]
> hashMap.findD "one" 0 = 1
> hashMap.findD "three" 0 = 0
> ```

```lean
def findD (self : HashMap α β) (a : α) (b₀ : β) : β
```

`Batteries.HashMap.find!` (definition, [line 171](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L171))

> Looks up an element in the map with key `a`. Panics if the element is not found.
> ```
> def hashMap := ofList [("one", 1), ("two", 2)]
> hashMap.find! "one" = 1
> hashMap.find! "three" => panic!
> ```

```lean
def find! [Inhabited β] (self : HashMap α β) (a : α) : β
```

`Batteries.HashMap.findEntry?` (definition, [line 189](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L189))

> Given a key `a`, returns a key-value pair in the map whose key compares equal to `a`.
> Note that the returned key may not be identical to the input, if `==` ignores some part
> of the value.
> ```
> def hashMap := ofList [("one", 1), ("two", 2)]
> hashMap.findEntry? "one" = some ("one", 1)
> hashMap.findEntry? "three" = none
> ```

```lean
def findEntry? [BEq α] [Hashable α] (m : HashMap α β) (k : α) : Option (α × β)
```

`Batteries.HashMap.contains` (definition, [line 200](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L200))

> Returns true if the element `a` is in the map.
> ```
> def hashMap := ofList [("one", 1), ("two", 2)]
> hashMap.contains "one" = true
> hashMap.contains "three" = false
> ```

```lean
def contains (self : HashMap α β) (a : α) : Bool
```

`Batteries.HashMap.foldM` (definition, [line 213](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L213))

> Folds a monadic function over the elements in the map (in arbitrary order).
> ```
> def sumEven (sum: Nat) (k : String) (v : Nat) : Except String Nat :=
>   if v % 2 == 0 then pure (sum + v) else throw s!"value {v} at key {k} is not even"
>
> foldM sumEven 0 (ofList [("one", 1), ("three", 3)]) =
>   Except.error "value 3 at key three is not even"
> foldM sumEven 0 (ofList [("two", 2), ("four", 4)]) = Except.ok 6
> ```

```lean
def foldM [Monad m] (f : δ → α → β → m δ) (init : δ) (self : HashMap α β) : m δ
```

`Batteries.HashMap.fold` (definition, [line 222](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L222))

> Folds a function over the elements in the map (in arbitrary order).
> ```
> fold (fun sum _ v => sum + v) 0 (ofList [("one", 1), ("two", 2)]) = 3
> ```

```lean
def fold (f : δ → α → β → δ) (init : δ) (self : HashMap α β) : δ
```

`Batteries.HashMap.mergeWithM` (definition, [line 239](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L239))

> Combines two hashmaps using a monadic function `f` to combine two values at a key.
> ```
> def map1 := ofList [("one", 1), ("two", 2)]
> def map2 := ofList [("two", 2), ("three", 3)]
> def map3 := ofList [("two", 3), ("three", 3)]
> def mergeIfNoConflict? (_ : String) (v₁ v₂ : Nat) : Option Nat :=
>   if v₁ != v₂ then none else some v₁
>
>
> mergeWithM mergeIfNoConflict? map1 map2 = some {"one" => 1, "two" => 2, "three" => 3}
> mergeWithM mergeIfNoConflict? map1 map3 = none
> ```

```lean
def mergeWithM [Monad m] (f : α → β → β → m β)
    (self other : HashMap α β) : m (HashMap α β)
```

`Batteries.HashMap.mergeWith` (definition, [line 251](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L251))

> Combines two hashmaps using function `f` to combine two values at a key.
> ```
> mergeWith (fun _ v₁ v₂ => v₁ + v₂ )
>   (ofList [("one", 1), ("two", 2)]) (ofList [("two", 2), ("three", 3)]) =
>     {"one" => 1, "two" => 4, "three" => 3}
> ```

```lean
def mergeWith (f : α → β → β → β) (self other : HashMap α β) : HashMap α β
```

`Batteries.HashMap.forM` (definition, [line 264](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L264))

> Runs a monadic function over the elements in the map (in arbitrary order).
> ```
> def checkEven (k : String) (v : Nat) : Except String Unit :=
>   if v % 2 == 0 then pure () else throw s!"value {v} at key {k} is not even"
>
> forM checkEven (ofList [("one", 1), ("three", 3)]) = Except.error "value 3 at key three is not even"
> forM checkEven (ofList [("two", 2), ("four", 4)]) = Except.ok ()
> ```

```lean
def forM [Monad m] (f : α → β → m PUnit) (self : HashMap α β) : m PUnit
```

`Batteries.HashMap.toList` (definition, [line 274](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L274))

> Converts the map into a list of key-value pairs.
> ```
> open List
> (ofList [("one", 1), ("two", 2)]).toList ~ [("one", 1), ("two", 2)]
> ```

```lean
def toList (self : HashMap α β) : List (α × β)
```

`Batteries.HashMap.toArray` (definition, [line 283](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L283))

> Converts the map into an array of key-value pairs.
> ```
> open List
> (ofList [("one", 1), ("two", 2)]).toArray.data ~ #[("one", 1), ("two", 2)].data
> ```

```lean
def toArray (self : HashMap α β) : Array (α × β)
```

`Batteries.HashMap.numBuckets` (definition, [line 286](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L286))

> The number of buckets in the hash map.

```lean
def numBuckets (self : HashMap α β) : Nat
```

`Batteries.HashMap.ofList` (definition, [line 295](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L295))

> Builds a `HashMap` from a list of key-value pairs.
> Values of duplicated keys are replaced by their respective last occurrences.
> ```
> ofList [("one", 1), ("one", 2)] = {"one" => 2}
> ```

```lean
def ofList [BEq α] [Hashable α] (l : List (α × β)) : HashMap α β
```

`Batteries.HashMap.ofListWith` (definition, [line 304](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean#L304))

> Variant of `ofList` which accepts a function that combines values of duplicated keys.
> ```
> ofListWith [("one", 1), ("one", 2)] (fun v₁ v₂ => v₁ + v₂) = {"one" => 3}
> ```

```lean
def ofListWith [BEq α] [Hashable α] (l : List (α × β)) (f : β → β → β) : HashMap α β
```

## Depends on

- [HashMap](../../../lean/hashmap.md)

## Sources

- [Batteries/Data/HashMap/Basic.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/HashMap/Basic.lean)
- [Declaration ledger](../../../../../sources/batteries/Batteries.Data.HashMap.Basic.json)

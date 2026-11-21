---
catalog: module
lean: ByteSlice.isEmpty, ByteSlice.stop_eq_start_add_size, ByteSlice.pop, ByteSlice.popFront, ByteSlice.foldlM, ByteSlice.foldl, ByteSlice.forIn
statement: formalized
proof: formalized
---

# ByteSlice

`Batteries.Data.ByteSlice`, in [Batteries/Data/ByteSlice.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/ByteSlice.lean), by Mario Carneiro, François G. Dorais.

`ByteSlice.isEmpty` (abbreviation, [line 15](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/ByteSlice.lean#L15))

> Test whether a byte slice is empty.

```lean
public protected abbrev isEmpty (s : ByteSlice)
```

`ByteSlice.stop_eq_start_add_size` (theorem, [line 17](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/ByteSlice.lean#L17))

```lean
public theorem stop_eq_start_add_size (s : ByteSlice) : s.stop = s.start + s.size
```

`ByteSlice.pop` (abbreviation, [line 21](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/ByteSlice.lean#L21))

> Returns the subslice obtained by removing the last element.

```lean
public abbrev pop (s : ByteSlice) : ByteSlice
```

`ByteSlice.popFront` (abbreviation, [line 25](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/ByteSlice.lean#L25))

> Returns the subslice obtained by removing the first element.

```lean
public abbrev popFront (s : ByteSlice) : ByteSlice
```

`ByteSlice.foldlM` (definition, [line 30](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/ByteSlice.lean#L30))

> Folds a monadic function over a `ByteSubarray` from left to right.

```lean
public def foldlM [Monad m] (s : ByteSlice) (f : β → UInt8 → m β) (init : β) : m β
```

`ByteSlice.foldl` (definition, [line 35](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/ByteSlice.lean#L35))

> Folds a function over a `ByteSubarray` from left to right.

```lean
public def foldl (s : ByteSlice) (f : β → UInt8 → β) (init : β) : β
```

`ByteSlice.forIn` (definition, [line 40](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/ByteSlice.lean#L40))

> Implementation of `forIn` for a `ByteSlice`.

```lean
public protected def forIn [Monad m] (s : ByteSlice) (init : β) (f : UInt8 → β → m (ForInStep β)) :
    m β
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Data/ByteSlice.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Data/ByteSlice.lean)
- [Declaration ledger](../../../../sources/batteries/Batteries.Data.ByteSlice.json)

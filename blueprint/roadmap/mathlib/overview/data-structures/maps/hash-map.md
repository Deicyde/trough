---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: Std.HashMap
---

# Hash map

Hash maps.

This is a simple separate-chaining hash table. The data of the hash map consists of a cached size
and an array of buckets, where each bucket is a linked list of key-value pairs. The number of buckets
is always a power of two. The hash map doubles its size upon inserting an element such that the
number of elements is more than 75% of the number of buckets.

The hash table is backed by an `Array`. Users should make sure that the hash map is used linearly to
avoid expensive copies.

The hash map uses `==` (provided by the `BEq` typeclass) to compare keys and `hash` (provided by
the `Hashable` typeclass) to hash them. To ensure that the operations behave as expected, `==`
should be an equivalence relation and `a == b` should imply `hash a = hash b` (see also the
`EquivBEq` and `LawfulHashable` typeclasses). Both of these conditions are automatic if the BEq
instance is lawful, i.e., if `a == b` implies `a = b`.

These hash maps contain a bundled well-formedness invariant, which means that they cannot
be used in nested inductive types. For these use cases, `Std.Data.HashMap.Raw` and
`Std.Data.HashMap.Raw.WF` unbundle the invariant from the hash map. When in doubt, prefer
`HashMap` over `HashMap.Raw`.

Dependent hash maps, in which keys may occur in their values' types, are available as
`Std.Data.DHashMap`.

```lean
Std.HashMap.{u, v} (α : Type u) (β : Type v) [BEq α] [Hashable α] : Type (max u v)
```

## Depends on

- [Array](../list-like-structures/array.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)

## Sources

- [Mathlib documentation: `Std.HashMap`](https://leanprover-community.github.io/mathlib4_docs/Std/Data/HashMap/Basic.html#Std.HashMap)
- [Mathlib overview: Data structures › Maps](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L588)

---
catalog: module
lean: Aesop.UnionFind, Aesop.UnionFind.size, Aesop.UnionFind.add, Aesop.UnionFind.addArray, Aesop.UnionFind.ofArray, Aesop.UnionFind.find?, Aesop.UnionFind.merge, Aesop.UnionFind.sets, Aesop.cluster
statement: formalized
proof: formalized
---

# UnionFind

`Aesop.Util.UnionFind`, in [Aesop/Util/UnionFind.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnionFind.lean), by Jannis Limperg.

`Aesop.UnionFind` (structure, [line 14](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnionFind.lean#L14))

```lean
structure UnionFind (α) [BEq α] [Hashable α] where
  parents : Array USize
  sizes : Array USize
  toRep : Std.HashMap α USize
  -- Invariant: `toRep` contains exactly the indices of `parents` as values
  deriving Inhabited
```

`Aesop.UnionFind.size` (definition, [line 28](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnionFind.lean#L28))

```lean
def size (u : UnionFind α) : Nat
```

`Aesop.UnionFind.add` (definition, [line 31](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnionFind.lean#L31))

```lean
def add (x : α) (u : UnionFind α) : UnionFind α
```

`Aesop.UnionFind.addArray` (definition, [line 39](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnionFind.lean#L39))

```lean
def addArray (xs : Array α) (u : UnionFind α) : UnionFind α
```

`Aesop.UnionFind.ofArray` (definition, [line 42](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnionFind.lean#L42))

```lean
def ofArray (xs : Array α) : UnionFind α
```

`Aesop.UnionFind.find?` (definition, [line 57](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnionFind.lean#L57))

```lean
partial def find? (x : α) (u : UnionFind α) : Option USize × UnionFind α
```

`Aesop.UnionFind.merge` (opaque constant, [line 87](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnionFind.lean#L87))

```lean
opaque merge (x y : α) : UnionFind α → UnionFind α
```

`Aesop.UnionFind.sets` (definition, [line 89](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnionFind.lean#L89))

```lean
def sets {α : Type v} [BEq α] [Hashable α] (u : UnionFind α) : Array (Array α) × UnionFind α
```

`Aesop.cluster` (definition, [line 105](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnionFind.lean#L105))

> Cluster the `as` according to which `bs` are associated to them by `f`. Two
> members `a₁, a₂` of `as` are put in the same cluster iff `f a₁ ∩ f a₂ ≠ ∅`.

```lean
def cluster [BEq α] [Hashable α] [BEq β] [Hashable β] (f : α → Array β)
    (as : Array α) : Array (Array α)
```

## Depends on

Its statements use no other Aesop module's declarations.

## Sources

- [Aesop/Util/UnionFind.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Util/UnionFind.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Util.UnionFind.json)

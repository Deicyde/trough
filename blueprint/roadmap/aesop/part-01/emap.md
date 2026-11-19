---
catalog: module
lean: Aesop.EMap, Aesop.EMap.empty, Aesop.EMap.foldlM, Aesop.EMap.foldl, Aesop.EMap.alterM, Aesop.EMap.alter, Aesop.EMap.insertNew, Aesop.EMap.insertWithM, Aesop.EMap.insertWith, Aesop.EMap.insert, Aesop.EMap.singleton, Aesop.EMap.findWithKey?, Aesop.EMap.find?, Aesop.EMap.mapM, Aesop.EMap.map
statement: formalized
proof: formalized
---

# EMap

`Aesop.EMap`, in [Aesop/EMap.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean), by Jannis Limperg.

`Aesop.EMap` (structure, [line 20](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L20))

> A map whose keys are expressions. Keys are identified up to defeq. We use
> `reducible` transparency and treat metavariables as rigid (i.e.,
> unassignable).

```lean
structure EMap (α) where
  /-- The mappings stored in the map. Defeq expressions are identified, so
  for each equivalence class of defeq expressions we only store one
  representative. Missing values indicate expressions that were removed from the
  map. -/
  rep : PArray (Option (Expr × α))
  /-- An index for `rep`. For each expression `e` at index `i` in `rep`,
  `idx.getMatch` returns a list of indexes containing `i`. This is used as a
  pre-filter during lookups/insertions/modifications to reduce the number of
  defeq comparisons. -/
  idx : DiscrTree Nat
  deriving Inhabited
```

`Aesop.EMap.empty` (definition, [line 35](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L35))

```lean
protected def empty : EMap α
```

`Aesop.EMap.foldlM` (definition, [line 54](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L54))

```lean
def foldlM (init : σ) (f : σ → Expr → α → m σ) (map : EMap α) : m σ
```

`Aesop.EMap.foldl` (definition, [line 59](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L59))

```lean
def foldl (init : σ) (f : σ → Expr → α → σ) (map : EMap α) : σ
```

`Aesop.EMap.alterM` (definition, [line 66](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L66))

```lean
def alterM (e : Expr) (f : α → m (Option α × β)) (map : EMap α) :
    m (EMap α × Option β)
```

`Aesop.EMap.alter` (definition, [line 82](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L82))

```lean
def alter (e : Expr) (f : α → Option α × β) (map : EMap α) :
    MetaM (EMap α × Option β)
```

`Aesop.EMap.insertNew` (definition, [line 87](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L87))

```lean
def insertNew (e : Expr) (a : α) (map : EMap α) : m (EMap α)
```

`Aesop.EMap.insertWithM` (definition, [line 94](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L94))

```lean
def insertWithM (e : Expr) (f : Option α → m α) (map : EMap α) :
    m (EMap α × Option α × α)
```

`Aesop.EMap.insertWith` (definition, [line 106](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L106))

```lean
def insertWith (e : Expr) (f : Option α → α) (map : EMap α) :
    MetaM (EMap α × Option α × α)
```

`Aesop.EMap.insert` (definition, [line 110](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L110))

```lean
def insert (e : Expr) (a : α) (map : EMap α) : MetaM (EMap α)
```

`Aesop.EMap.singleton` (definition, [line 113](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L113))

```lean
def singleton (e : Expr) (a : α) : m (EMap α)
```

`Aesop.EMap.findWithKey?` (definition, [line 116](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L116))

```lean
def findWithKey? (e : Expr) (map : EMap α) : MetaM (Option (Expr × α))
```

`Aesop.EMap.find?` (definition, [line 127](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L127))

```lean
def find? (e : Expr) (map : EMap α) : MetaM (Option α)
```

`Aesop.EMap.mapM` (definition, [line 131](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L131))

```lean
def mapM (f : Expr → α → m β) (map : EMap α) : m (EMap β)
```

`Aesop.EMap.map` (definition, [line 135](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean#L135))

```lean
def map (f : Expr → α → β) (map : EMap α) : EMap β
```

## Depends on

- [Util/Basic](util/basic.md)

## Sources

- [Aesop/EMap.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/EMap.lean)
- [Declaration ledger](../../../sources/aesop/Aesop.EMap.json)

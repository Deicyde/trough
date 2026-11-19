---
catalog: module
lean: Cedar.Spec.Value.sliceEUIDs, Cedar.Spec.EntityData.sliceEUIDs, Cedar.Spec.Request.sliceEUIDs, Cedar.Spec.Entities.sliceAtLevel, Cedar.Spec.Entities.closedAtLevel
statement: formalized
proof: formalized
---

# Spec/Slice

`Cedar.Spec.Slice`, in [Cedar/Spec/Slice.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Slice.lean).

> This file defines entity slicing at a level

`Cedar.Spec.Value.sliceEUIDs` (definition, [line 32](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Slice.lean#L32))

```lean
public def Value.sliceEUIDs : Value → Set EntityUID
```

`Cedar.Spec.EntityData.sliceEUIDs` (definition, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Slice.lean#L37))

```lean
public def EntityData.sliceEUIDs (ed : EntityData) : Set EntityUID
```

`Cedar.Spec.Request.sliceEUIDs` (definition, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Slice.lean#L41))

```lean
public def Request.sliceEUIDs (r : Request) : Set EntityUID
```

`Cedar.Spec.Entities.sliceAtLevel` (definition, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Slice.lean#L46))

```lean
public def Entities.sliceAtLevel (es : Entities) (r : Request) (level : Nat) : Entities
```

`Cedar.Spec.Entities.closedAtLevel` (definition, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Slice.lean#L71))

> Executable check deciding whether `es` is *closed at a level* for request `r`:
> every entity reachable from the request roots within `level` dereferences is
> present in `es`.  It reuses the reachable-entity set computed by the slicing
> algorithm (`Entities.sliceAtLevel.sliceAtLevel`, which collects every entity
> reachable in `level` hops, whether or not it is present) and checks that each is
> actually in the store.
>
> `Cedar.Thm.closedAtLevel_iff` proves this returns `true` exactly when the
> `EntitiesClosedAtLevel` predicate holds, so a Cedar user can run this to obtain
> the issue-#642 guarantee: a level-validated policy set evaluated against a store
> passing this check never errors with `entityDoesNotExist`.

```lean
public def Entities.closedAtLevel (es : Entities) (r : Request) (level : Nat) : Bool
```

## Depends on

- [Entities](entities.md)
- [Request](request.md)

## Sources

- [Cedar/Spec/Slice.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Slice.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Spec.Slice.json)

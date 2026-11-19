---
catalog: module
lean: Cedar.Spec.Tag, Cedar.Spec.EntityData, Cedar.Spec.Entities, Cedar.Spec.Entities.ancestors, Cedar.Spec.Entities.ancestorsOrEmpty, Cedar.Spec.Entities.attrs, Cedar.Spec.Entities.attrsOrEmpty, Cedar.Spec.Entities.tags, Cedar.Spec.Entities.tagsOrEmpty
statement: formalized
proof: formalized
---

# Entities

`Cedar.Spec.Entities`, in [Cedar/Spec/Entities.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Entities.lean).

> This file defines Cedar entities.

`Cedar.Spec.Tag` (abbreviation, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Entities.lean#L31))

```lean
public abbrev Tag
```

`Cedar.Spec.EntityData` (structure, [line 33](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Entities.lean#L33))

```lean
public structure EntityData where
  attrs : Map Attr Value
  ancestors : Set EntityUID
  tags : Map Tag Value
```

`Cedar.Spec.Entities` (abbreviation, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Entities.lean#L38))

```lean
public abbrev Entities
```

`Cedar.Spec.Entities.ancestors` (definition, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Entities.lean#L41))

```lean
public def Entities.ancestors (es : Entities) (uid : EntityUID) : Result (Set EntityUID)
```

`Cedar.Spec.Entities.ancestorsOrEmpty` (definition, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Entities.lean#L46))

```lean
public def Entities.ancestorsOrEmpty (es : Entities) (uid : EntityUID) : Set EntityUID
```

`Cedar.Spec.Entities.attrs` (definition, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Entities.lean#L52))

```lean
public def Entities.attrs (es : Entities) (uid : EntityUID) : Result (Map Attr Value)
```

`Cedar.Spec.Entities.attrsOrEmpty` (definition, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Entities.lean#L57))

```lean
public def Entities.attrsOrEmpty (es : Entities) (uid : EntityUID) : Map Attr Value
```

`Cedar.Spec.Entities.tags` (definition, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Entities.lean#L63))

```lean
public def Entities.tags (es : Entities) (uid : EntityUID) : Result (Map Tag Value)
```

`Cedar.Spec.Entities.tagsOrEmpty` (definition, [line 68](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Entities.lean#L68))

```lean
public def Entities.tagsOrEmpty (es : Entities) (uid : EntityUID) : Map Tag Value
```

## Depends on

- [Value](value.md)

## Sources

- [Cedar/Spec/Entities.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Entities.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Spec.Entities.json)

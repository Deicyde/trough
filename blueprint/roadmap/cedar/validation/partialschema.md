---
catalog: module
lean: Cedar.Validation.PartialEntitySchemaEntry, Cedar.Validation.PartialEntitySchemaEntry.isValidEntityEID, Cedar.Validation.PartialEntitySchemaEntry.tags?, Cedar.Validation.PartialEntitySchemaEntry.attrs?, Cedar.Validation.PartialEntitySchemaEntry.ancestors, Cedar.Validation.PartialEntitySchemaEntry.isStandard, Cedar.Validation.PartialEntitySchemaEntry.isExternal, Cedar.Validation.PartialEntitySchemaEntry.toEntitySchemaEntry?, Cedar.Validation.PartialEntitySchemaEntry.withAncestors, Cedar.Validation.PartialActionSchemaEntry, Cedar.Validation.PartialActionSchemaEntry.ancestors, Cedar.Validation.PartialActionSchemaEntry.isExternal, Cedar.Validation.PartialActionSchemaEntry.toActionSchemaEntry?, Cedar.Validation.PartialActionSchemaEntry.withAncestors, Cedar.Validation.PartialEntitySchema, Cedar.Validation.PartialActionSchema, Cedar.Validation.PartialSchema, Cedar.Validation.Schema.toPartialSchema, Cedar.Validation.PartialSchema.isComplete, Cedar.Validation.PartialSchema.asSchema?
statement: formalized
proof: formalized
---

# Validation/PartialSchema

`Cedar.Validation.PartialSchema`, in [Cedar/Validation/PartialSchema.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean).

`Cedar.Validation.PartialEntitySchemaEntry` (inductive type, [line 28](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L28))

```lean
public inductive PartialEntitySchemaEntry where
  | defined (entry : EntitySchemaEntry)
  | external (parents : Set EntityType)
deriving Repr
```

`Cedar.Validation.PartialEntitySchemaEntry.isValidEntityEID` (definition, [line 33](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L33))

```lean
public def PartialEntitySchemaEntry.isValidEntityEID (entry : PartialEntitySchemaEntry) (eid : String) : Bool
```

`Cedar.Validation.PartialEntitySchemaEntry.tags?` (definition, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L38))

```lean
public def PartialEntitySchemaEntry.tags? : PartialEntitySchemaEntry → Option (Option CedarType)
```

`Cedar.Validation.PartialEntitySchemaEntry.attrs?` (definition, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L42))

```lean
public def PartialEntitySchemaEntry.attrs? : PartialEntitySchemaEntry → Option RecordType
```

`Cedar.Validation.PartialEntitySchemaEntry.ancestors` (definition, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L46))

```lean
public def PartialEntitySchemaEntry.ancestors : PartialEntitySchemaEntry → Set EntityType
```

`Cedar.Validation.PartialEntitySchemaEntry.isStandard` (definition, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L50))

```lean
public def PartialEntitySchemaEntry.isStandard : PartialEntitySchemaEntry → Bool
```

`Cedar.Validation.PartialEntitySchemaEntry.isExternal` (definition, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L54))

```lean
public def PartialEntitySchemaEntry.isExternal : PartialEntitySchemaEntry → Bool
```

`Cedar.Validation.PartialEntitySchemaEntry.toEntitySchemaEntry?` (definition, [line 58](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L58))

```lean
public def PartialEntitySchemaEntry.toEntitySchemaEntry? : PartialEntitySchemaEntry → Option EntitySchemaEntry
```

`Cedar.Validation.PartialEntitySchemaEntry.withAncestors` (definition, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L62))

```lean
public def PartialEntitySchemaEntry.withAncestors (ancestors : Set EntityType) : PartialEntitySchemaEntry → PartialEntitySchemaEntry
```

`Cedar.Validation.PartialActionSchemaEntry` (inductive type, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L70))

```lean
public inductive PartialActionSchemaEntry where
  | defined (entry : ActionSchemaEntry)
  | external (parents : Set EntityUID)
deriving Repr
```

`Cedar.Validation.PartialActionSchemaEntry.ancestors` (definition, [line 75](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L75))

```lean
public def PartialActionSchemaEntry.ancestors : PartialActionSchemaEntry → Set EntityUID
```

`Cedar.Validation.PartialActionSchemaEntry.isExternal` (definition, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L79))

```lean
public def PartialActionSchemaEntry.isExternal : PartialActionSchemaEntry → Bool
```

`Cedar.Validation.PartialActionSchemaEntry.toActionSchemaEntry?` (definition, [line 83](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L83))

```lean
public def PartialActionSchemaEntry.toActionSchemaEntry? : PartialActionSchemaEntry → Option ActionSchemaEntry
```

`Cedar.Validation.PartialActionSchemaEntry.withAncestors` (definition, [line 87](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L87))

```lean
public def PartialActionSchemaEntry.withAncestors (ancestors : Set EntityUID) : PartialActionSchemaEntry → PartialActionSchemaEntry
```

`Cedar.Validation.PartialEntitySchema` (abbreviation, [line 95](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L95))

```lean
public abbrev PartialEntitySchema
```

`Cedar.Validation.PartialActionSchema` (abbreviation, [line 97](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L97))

```lean
public abbrev PartialActionSchema
```

`Cedar.Validation.PartialSchema` (structure, [line 99](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L99))

```lean
public structure PartialSchema where
  ets  : PartialEntitySchema
  acts : PartialActionSchema
deriving Repr
```

`Cedar.Validation.Schema.toPartialSchema` (definition, [line 107](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L107))

```lean
public def Schema.toPartialSchema (s : Schema) : PartialSchema
```

`Cedar.Validation.PartialSchema.isComplete` (definition, [line 115](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L115))

```lean
public def PartialSchema.isComplete (ps : PartialSchema) : Bool
```

`Cedar.Validation.PartialSchema.asSchema?` (definition, [line 118](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean#L118))

```lean
public def PartialSchema.asSchema? (ps : PartialSchema) : Option Schema
```

## Depends on

- [Validation/Types](types.md)

## Sources

- [Cedar/Validation/PartialSchema.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialSchema.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Validation.PartialSchema.json)

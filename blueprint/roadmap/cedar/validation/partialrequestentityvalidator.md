---
catalog: module
lean: Cedar.Validation.PartialEntitySchemaEntry.validationView, Cedar.Validation.PartialActionSchemaEntry.validationView, Cedar.Validation.PartialSchema.validationView, Cedar.Validation.PartialSchema.validateRequest, Cedar.Validation.PartialSchema.validateEntities
statement: formalized
proof: formalized
---

# PartialRequestEntityValidator

`Cedar.Validation.PartialRequestEntityValidator`, in [Cedar/Validation/PartialRequestEntityValidator.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialRequestEntityValidator.lean).

> This file validates requests and entity stores against partial schemas.

`Cedar.Validation.PartialEntitySchemaEntry.validationView` (definition, [line 33](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialRequestEntityValidator.lean#L33))

```lean
public def PartialEntitySchemaEntry.validationView : PartialEntitySchemaEntry → EntitySchemaEntry
```

`Cedar.Validation.PartialActionSchemaEntry.validationView` (definition, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialRequestEntityValidator.lean#L41))

```lean
public def PartialActionSchemaEntry.validationView : PartialActionSchemaEntry → ActionSchemaEntry
```

`Cedar.Validation.PartialSchema.validationView` (definition, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialRequestEntityValidator.lean#L50))

```lean
public def PartialSchema.validationView (ps : PartialSchema) : Schema
```

`Cedar.Validation.PartialSchema.validateRequest` (definition, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialRequestEntityValidator.lean#L57))

```lean
public def PartialSchema.validateRequest
    (ps : PartialSchema)
    (request : Request) : RequestValidationResult
```

`Cedar.Validation.PartialSchema.validateEntities` (definition, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialRequestEntityValidator.lean#L67))

> Validate, treating external schema as empty schema declarations.
> Does validate actions with external type.
> Does NOT validate entities with external type.

```lean
public def PartialSchema.validateEntities
    (ps : PartialSchema)
    (entities : Entities) : EntityValidationResult
```

## Depends on

- [Validation/PartialSchema](partialschema.md)
- [RequestEntityValidator](requestentityvalidator.md)

## Sources

- [Cedar/Validation/PartialRequestEntityValidator.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/PartialRequestEntityValidator.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Validation.PartialRequestEntityValidator.json)

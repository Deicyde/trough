---
catalog: module
lean: Cedar.Validation.RequestValidationError, Cedar.Validation.RequestValidationResult, Cedar.Validation.EntityValidationError, Cedar.Validation.EntityValidationResult, Cedar.Validation.instanceOfBoolType, Cedar.Validation.instanceOfEntityType, Cedar.Validation.instanceOfExtType, Cedar.Validation.requiredAttributePresent, Cedar.Validation.instanceOfType, Cedar.Validation.instanceOfRequestType, Cedar.Validation.instanceOfSchema, Cedar.Validation.requestMatchesEnvironment, Cedar.Validation.validateRequest, Cedar.Validation.entitiesMatchEnvironment, Cedar.Validation.actionSchemaEntryToEntityData, Cedar.Validation.validateEntities, Cedar.Validation.entityValidationErrorToJson, Cedar.Validation.requestValidationErrorToJson
statement: formalized
proof: formalized
---

# RequestEntityValidator

`Cedar.Validation.RequestEntityValidator`, in [Cedar/Validation/RequestEntityValidator.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean).

> This file includes boolean definitions for the propositions declared in `Cedar/Thm/Validation/Typechecker/Types.lean`.

`Cedar.Validation.RequestValidationError` (inductive type, [line 33](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L33))

```lean
public inductive RequestValidationError where
```

`Cedar.Validation.RequestValidationResult` (abbreviation, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L36))

```lean
public abbrev RequestValidationResult
```

`Cedar.Validation.EntityValidationError` (inductive type, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L38))

```lean
public inductive EntityValidationError where
```

`Cedar.Validation.EntityValidationResult` (abbreviation, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L41))

```lean
public abbrev EntityValidationResult
```

`Cedar.Validation.instanceOfBoolType` (definition, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L43))

```lean
public def instanceOfBoolType (b : Bool) (bty : BoolType) : Bool
```

`Cedar.Validation.instanceOfEntityType` (definition, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L50))

```lean
public def instanceOfEntityType (e : EntityUID) (ety : EntityType) (schema : Schema) : Bool
```

`Cedar.Validation.instanceOfExtType` (definition, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L54))

```lean
public def instanceOfExtType (ext : Ext) (extty: ExtType) : Bool
```

`Cedar.Validation.requiredAttributePresent` (definition, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L62))

```lean
public def requiredAttributePresent (r : Map Attr Value) (rty : Map Attr (Qualified CedarType)) (k : Attr)
```

`Cedar.Validation.instanceOfType` (definition, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L67))

```lean
public def instanceOfType (v : Value) (ty : CedarType) (schema : Schema) : Bool
```

`Cedar.Validation.instanceOfRequestType` (definition, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L93))

```lean
public def instanceOfRequestType (request : Request) (env : TypeEnv) : Bool
```

`Cedar.Validation.instanceOfSchema` (definition, [line 111](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L111))

> For every entity in the store,
> 1. The entity's type is defined in the type store (either `ets` or `as` for action entities).
> 2. The entity's attributes match the attribute types indicated in the type store.
> 3. The entity's ancestors' types are consistent with the ancestor information
>    in the type store.
> 4. The entity's tags' types are consistent with the tags information in the type store.
>
> For every action in the entity store, the action's ancestors are consistent
> with the ancestor information in the action store.

```lean
public def instanceOfSchema (entities : Entities) (env : TypeEnv) : EntityValidationResult
```

`Cedar.Validation.requestMatchesEnvironment` (definition, [line 149](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L149))

```lean
public def requestMatchesEnvironment (env : TypeEnv) (request : Request) : Bool
```

`Cedar.Validation.validateRequest` (definition, [line 151](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L151))

```lean
public def validateRequest (schema : Schema) (request : Request) : RequestValidationResult
```

`Cedar.Validation.entitiesMatchEnvironment` (definition, [line 156](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L156))

```lean
public def entitiesMatchEnvironment (env : TypeEnv) (entities : Entities) : EntityValidationResult
```

`Cedar.Validation.actionSchemaEntryToEntityData` (definition, [line 159](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L159))

```lean
public def actionSchemaEntryToEntityData (ase : ActionSchemaEntry) : EntityData
```

`Cedar.Validation.validateEntities` (definition, [line 165](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L165))

```lean
public def validateEntities (schema : Schema) (entities : Entities) : EntityValidationResult
```

`Cedar.Validation.entityValidationErrorToJson` (definition, [line 170](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L170))

```lean
public def entityValidationErrorToJson : EntityValidationError → Lean.Json
```

`Cedar.Validation.requestValidationErrorToJson` (definition, [line 176](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean#L176))

```lean
public def requestValidationErrorToJson : RequestValidationError → Lean.Json
```

## Depends on

- [Entities](../spec/entities.md)
- [Request](../spec/request.md)
- [Cedar/Validation/Validator](validator.md)

## Sources

- [Cedar/Validation/RequestEntityValidator.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/RequestEntityValidator.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Validation.RequestEntityValidator.json)

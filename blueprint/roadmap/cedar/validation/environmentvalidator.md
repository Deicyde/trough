---
catalog: module
lean: Cedar.Validation.EnvironmentValidationError, Cedar.Validation.EnvironmentValidationResult, Cedar.Validation.EntityType.validateWellFormed, Cedar.Validation.QualifiedType.validateWellFormed, Cedar.Validation.validateAttrsWellFormed, Cedar.Validation.CedarType.validateWellFormed, Cedar.Validation.CedarType.validateLifted, Cedar.Validation.StandardSchemaEntry.validateWellFormed, Cedar.Validation.EntitySchemaEntry.validateWellFormed, Cedar.Validation.EntitySchema.validateWellFormed, Cedar.Validation.ActionSchemaEntry.validateWellFormed, Cedar.Validation.ActionSchema.validateAcyclicActionHierarchy, Cedar.Validation.ActionSchema.validateTransitiveActionHierarchy, Cedar.Validation.ActionSchema.validateWellFormed, Cedar.Validation.RequestType.validateWellFormed, Cedar.Validation.TypeEnv.validateWellFormed, Cedar.Validation.Schema.validateWellFormed
statement: formalized
proof: formalized
---

# EnvironmentValidator

`Cedar.Validation.EnvironmentValidator`, in [Cedar/Validation/EnvironmentValidator.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean).

> This file contains the executable version of `TypeEnv.WellFormed`
> and related definitions.

`Cedar.Validation.EnvironmentValidationError` (inductive type, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L35))

```lean
public inductive EnvironmentValidationError where
```

`Cedar.Validation.EnvironmentValidationResult` (abbreviation, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L43))

```lean
public abbrev EnvironmentValidationResult
```

`Cedar.Validation.EntityType.validateWellFormed` (definition, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L45))

```lean
public def EntityType.validateWellFormed (env : TypeEnv) (ety : EntityType) : EnvironmentValidationResult
```

`Cedar.Validation.QualifiedType.validateWellFormed` (definition, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L52))

```lean
public def QualifiedType.validateWellFormed (env : TypeEnv) (qty : QualifiedType) : EnvironmentValidationResult
```

`Cedar.Validation.validateAttrsWellFormed` (definition, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L59))

```lean
public def validateAttrsWellFormed (env : TypeEnv) (rty : List (Attr × QualifiedType)) : EnvironmentValidationResult
```

`Cedar.Validation.CedarType.validateWellFormed` (definition, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L67))

```lean
public def CedarType.validateWellFormed (env : TypeEnv) (ty : CedarType) : EnvironmentValidationResult
```

`Cedar.Validation.CedarType.validateLifted` (definition, [line 88](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L88))

```lean
public def CedarType.validateLifted (ty : CedarType) : EnvironmentValidationResult
```

`Cedar.Validation.StandardSchemaEntry.validateWellFormed` (definition, [line 113](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L113))

```lean
public def StandardSchemaEntry.validateWellFormed (env : TypeEnv) (entry : StandardSchemaEntry) : EnvironmentValidationResult
```

`Cedar.Validation.EntitySchemaEntry.validateWellFormed` (definition, [line 132](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L132))

```lean
public def EntitySchemaEntry.validateWellFormed (env : TypeEnv) (entry : EntitySchemaEntry) : EnvironmentValidationResult
```

`Cedar.Validation.EntitySchema.validateWellFormed` (definition, [line 141](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L141))

```lean
public def EntitySchema.validateWellFormed (env : TypeEnv) (ets : EntitySchema) : EnvironmentValidationResult
```

`Cedar.Validation.ActionSchemaEntry.validateWellFormed` (definition, [line 148](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L148))

```lean
public def ActionSchemaEntry.validateWellFormed (env : TypeEnv) (entry : ActionSchemaEntry) : EnvironmentValidationResult
```

`Cedar.Validation.ActionSchema.validateAcyclicActionHierarchy` (definition, [line 167](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L167))

```lean
public def ActionSchema.validateAcyclicActionHierarchy (acts : ActionSchema) : EnvironmentValidationResult
```

`Cedar.Validation.ActionSchema.validateTransitiveActionHierarchy` (definition, [line 173](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L173))

```lean
public def ActionSchema.validateTransitiveActionHierarchy (acts : ActionSchema) : EnvironmentValidationResult
```

`Cedar.Validation.ActionSchema.validateWellFormed` (definition, [line 182](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L182))

```lean
public def ActionSchema.validateWellFormed (env : TypeEnv) (acts : ActionSchema) : EnvironmentValidationResult
```

`Cedar.Validation.RequestType.validateWellFormed` (definition, [line 195](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L195))

```lean
public def RequestType.validateWellFormed (env : TypeEnv) (reqty : RequestType) : EnvironmentValidationResult
```

`Cedar.Validation.TypeEnv.validateWellFormed` (definition, [line 209](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L209))

```lean
public def TypeEnv.validateWellFormed (env : TypeEnv) : EnvironmentValidationResult
```

`Cedar.Validation.Schema.validateWellFormed` (definition, [line 216](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean#L216))

```lean
public def Schema.validateWellFormed (schema : Schema) : EnvironmentValidationResult
```

## Depends on

- [Cedar/Validation/Validator](validator.md)

## Sources

- [Cedar/Validation/EnvironmentValidator.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/EnvironmentValidator.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Validation.EnvironmentValidator.json)

---
catalog: module
lean: Cedar.SymCC.CompiledSchema, Cedar.SymCC.CompiledSchema.compile, Cedar.SymCC.CompiledSchema.symEnv, Cedar.SymCC.CompiledSchema.typeEnv
statement: formalized
proof: formalized
---

# CompiledSchema

`Cedar.SymCCOpt.CompiledSchema`, in [Cedar/SymCCOpt/CompiledSchema.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledSchema.lean).

`Cedar.SymCC.CompiledSchema` (structure, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledSchema.lean#L34))

> Represents a schema compiled into a symbolic representation of its entity types,
> stored together with the original schema. Building `SymEntities` is expensive
> but only depends on the schema (and not specific request type), so this
> structure avoids repeating that work on multiple solver queriers using the same
> schema.

```lean
public structure CompiledSchema where
  schema : Schema
  entities : SymEntities
deriving Repr, Inhabited
```

`Cedar.SymCC.CompiledSchema.compile` (definition, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledSchema.lean#L39))

```lean
public def CompiledSchema.compile (schema : Schema) : CompiledSchema
```

`Cedar.SymCC.CompiledSchema.symEnv` (definition, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledSchema.lean#L42))

```lean
public def CompiledSchema.symEnv (schema : CompiledSchema) (reqty : RequestType) : SymEnv
```

`Cedar.SymCC.CompiledSchema.typeEnv` (definition, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledSchema.lean#L45))

```lean
public def CompiledSchema.typeEnv (schema : CompiledSchema) (reqty : RequestType) : TypeEnv
```

## Depends on

- [Env](../symcc/part-01/env.md)

## Sources

- [Cedar/SymCCOpt/CompiledSchema.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/CompiledSchema.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.SymCCOpt.CompiledSchema.json)

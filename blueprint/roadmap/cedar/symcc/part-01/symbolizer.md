---
catalog: module
lean: Cedar.Spec.Prim.symbolize, Cedar.Spec.Value.symbolize?, Cedar.Spec.Request.symbolize?, Cedar.Spec.defaultEidOf, Cedar.Spec.defaultLitWithDefaultEid, Cedar.Spec.Entities.symbolizeAttrs?, Cedar.Spec.Entities.symbolizeTags?, Cedar.Spec.Entities.symbolizeAncs?, Cedar.Spec.Entities.symbolize?, Cedar.Spec.Env.symbolize?
statement: formalized
proof: formalized
---

# Cedar/SymCC/Symbolizer

`Cedar.SymCC.Symbolizer`, in [Cedar/SymCC/Symbolizer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Symbolizer.lean).

> This file contains functions to encode a concrete `Env`
> into a `SymEnv`, which can also be thought of as an "inverse"
> of concretization.

`Cedar.Spec.Prim.symbolize` (definition, [line 32](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Symbolizer.lean#L32))

```lean
def Prim.symbolize : Prim → Term
```

`Cedar.Spec.Value.symbolize?` (definition, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Symbolizer.lean#L39))

> Encodes a `Value` as a `Term` assuming it is of a certain type

```lean
def Value.symbolize? (v : Value) (ty : CedarType) : Option Term
```

`Cedar.Spec.Request.symbolize?` (definition, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Symbolizer.lean#L79))

> The variable ids here should match the variables in `SymRequest.ofRequestType`.

```lean
def Request.symbolize? (req : Request) (Γ : TypeEnv) (var : TermVar) : Option Term
```

`Cedar.Spec.defaultEidOf` (definition, [line 91](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Symbolizer.lean#L91))

```lean
def defaultEidOf (Γ : TypeEnv) (ety : EntityType) : String
```

`Cedar.Spec.defaultLitWithDefaultEid` (definition, [line 95](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Symbolizer.lean#L95))

```lean
def defaultLitWithDefaultEid (Γ : TypeEnv) (ty : TermType) : Term
```

`Cedar.Spec.Entities.symbolizeAttrs?` (definition, [line 101](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Symbolizer.lean#L101))

> Generates an interpretation of the attribute map.

```lean
def Entities.symbolizeAttrs?
  (entities : Entities) (Γ : TypeEnv)
  (ety : EntityType) (entry : EntitySchemaEntry)
  (uuf : UUF) : Option UDF
```

`Cedar.Spec.Entities.symbolizeTags?` (definition, [line 131](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Symbolizer.lean#L131))

> Generates interpretations for the tag key and value maps.

```lean
def Entities.symbolizeTags?
  (entities : Entities) (Γ : TypeEnv)
  (ety : EntityType) (entry : EntitySchemaEntry)
  (uuf : UUF) : Option UDF
```

`Cedar.Spec.Entities.symbolizeAncs?` (definition, [line 185](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Symbolizer.lean#L185))

> Generates an interpretation for the ancestor map.

```lean
def Entities.symbolizeAncs?
  (entities : Entities) (Γ : TypeEnv)
  (ety : EntityType) (entry : EntitySchemaEntry)
  (uuf : UUF) : Option UDF
```

`Cedar.Spec.Entities.symbolize?` (definition, [line 221](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Symbolizer.lean#L221))

> Symbolizes a concrete `Entities` into (part of) an `Interpretation` of `SymEnv.ofEnv Γ`.
> The `UUF` ids here should match those in `SymEntityData.ofStandardEntityType`.

```lean
def Entities.symbolize? (entities : Entities) (Γ : TypeEnv) (uuf : UUF) : Option UDF
```

`Cedar.Spec.Env.symbolize?` (definition, [line 231](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Symbolizer.lean#L231))

> Converts an `Env` (assumed to be a well-typed instance of `TypeEnv`) into
> an `Interpretation` of `SymEnv.ofEnv Γ`.

```lean
def Env.symbolize? (env : Env) (Γ : TypeEnv) : Interpretation
```

## Depends on

- [Concretizing symbolic environments](concretizer.md)
- [Cedar/SymCC/Decoder](decoder.md)

## Proof depends on

- [Map properties](../../thm/data/map.md)

## Sources

- [Cedar/SymCC/Symbolizer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Symbolizer.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Symbolizer.json)

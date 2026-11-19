---
catalog: module
lean: Cedar.SymCC.SymRequest, Cedar.SymCC.SymRequest.isLiteral, Cedar.SymCC.SymEntityData, Cedar.SymCC.SymTags.isLiteral, Cedar.SymCC.SymEntityData.isLiteral, Cedar.SymCC.SymEntities, Cedar.SymCC.SymEntities.attrs, Cedar.SymCC.SymEntities.ancestors, Cedar.SymCC.SymEntities.ancestorsOfType, Cedar.SymCC.SymEntities.isValidEntityType, Cedar.SymCC.SymEntities.isValidEntityUID, Cedar.SymCC.SymEntities.tags, Cedar.SymCC.SymEntities.isLiteral, Cedar.SymCC.SymEnv, Cedar.SymCC.SymEnv.isLiteral, Cedar.SymCC.UUF.attrsId, Cedar.SymCC.UUF.ancsId, Cedar.SymCC.UUF.tagKeysId, Cedar.SymCC.UUF.tagValsId, Cedar.SymCC.SymEntityData.ofStandardEntityType, Cedar.SymCC.SymEntityData.emptyAttrs, Cedar.SymCC.SymEntityData.ofEnumEntityType, Cedar.SymCC.SymEntityData.ofEntityType, Cedar.SymCC.SymEntityData.ofActionType, Cedar.SymCC.SymEntities.ofSchema, Cedar.SymCC.SymRequest.ofRequestType, Cedar.SymCC.SymEnv.ofEnv
statement: formalized
proof: formalized
---

# Env

`Cedar.SymCC.Env`, in [Cedar/SymCC/Env.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean).

> This file defines the ADTs that represent the symbolic environment.
> The environment consists of a symbolic request, entity store, and action store.
> A symbolic environment is _literal_ when it consists of literal terms and
> interpreted functions (UDFs).

`Cedar.SymCC.SymRequest` (structure, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L35))

```lean
public structure SymRequest where
  principal : Term
  action : Term
  resource : Term
  context : Term
```

`Cedar.SymCC.SymRequest.isLiteral` (definition, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L41))

```lean
public def SymRequest.isLiteral (req : SymRequest) : Bool
```

`Cedar.SymCC.SymEntityData` (structure, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L61))

> Represents the entity data for _all entities_ of a _single type_

```lean
public structure SymEntityData where
  attrs : UnaryFunction
  /--
  Let `t₁` be the entity type which this `SymEntityData` represents the data for.
  Let `t₂` be an entity type in this map's keys.
  The `UnaryFunction` here maps entities of type `t₁` to
  the set of entities of type `t₂` which are ancestors of that entity.
  (Of course, the `UnaryFunction` is on SMT-level values, so the domain is
  essentially `t₁`-typed `Term`s, and the output is essentially a
  `Set<t₂>`-typed `Term`.)
  -/
  ancestors : Map EntityType UnaryFunction
  /-- Specifies the EIDs of enum members for this entity type, if applicable -/
  members : Option (Set String)
  /-- `none` means this entity type has no tags -/
  tags : Option SymTags
```

`Cedar.SymCC.SymTags.isLiteral` (definition, [line 78](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L78))

```lean
public def SymTags.isLiteral (τs : SymTags) : Bool
```

`Cedar.SymCC.SymEntityData.isLiteral` (definition, [line 82](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L82))

```lean
public def SymEntityData.isLiteral (δ : SymEntityData) : Bool
```

`Cedar.SymCC.SymEntities` (abbreviation, [line 89](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L89))

```lean
public abbrev SymEntities
```

`Cedar.SymCC.SymEntities.attrs` (definition, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L93))

```lean
public def SymEntities.attrs (εs : SymEntities) (ety : EntityType) : Option UnaryFunction
```

`Cedar.SymCC.SymEntities.ancestors` (definition, [line 96](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L96))

```lean
public def SymEntities.ancestors (εs : SymEntities) (ety : EntityType) : Option (Map EntityType UnaryFunction)
```

`Cedar.SymCC.SymEntities.ancestorsOfType` (definition, [line 99](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L99))

```lean
public def SymEntities.ancestorsOfType (εs : SymEntities) (ety ancTy : EntityType) : Option UnaryFunction
```

`Cedar.SymCC.SymEntities.isValidEntityType` (definition, [line 102](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L102))

```lean
public def SymEntities.isValidEntityType (εs : SymEntities) (ety : EntityType) : Bool
```

`Cedar.SymCC.SymEntities.isValidEntityUID` (definition, [line 105](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L105))

```lean
public def SymEntities.isValidEntityUID (εs : SymEntities) (uid : EntityUID) : Bool
```

`Cedar.SymCC.SymEntities.tags` (definition, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L110))

```lean
public def SymEntities.tags (εs : SymEntities) (ety : EntityType) : Option (Option SymTags)
```

`Cedar.SymCC.SymEntities.isLiteral` (definition, [line 113](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L113))

```lean
public def SymEntities.isLiteral (es : SymEntities) : Bool
```

`Cedar.SymCC.SymEnv` (structure, [line 116](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L116))

```lean
public structure SymEnv where
  request  : SymRequest
  entities : SymEntities
```

`Cedar.SymCC.SymEnv.isLiteral` (definition, [line 120](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L120))

```lean
public def SymEnv.isLiteral (env : SymEnv) : Bool
```

`Cedar.SymCC.UUF.attrsId` (definition, [line 127](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L127))

```lean
public def UUF.attrsId (ety : EntityType) : String
```

`Cedar.SymCC.UUF.ancsId` (definition, [line 130](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L130))

```lean
public def UUF.ancsId (ety : EntityType) (ancTy : EntityType) : String
```

`Cedar.SymCC.UUF.tagKeysId` (definition, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L133))

```lean
public def UUF.tagKeysId (ety : EntityType) : String
```

`Cedar.SymCC.UUF.tagValsId` (definition, [line 136](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L136))

```lean
public def UUF.tagValsId (ety : EntityType) : String
```

`Cedar.SymCC.SymEntityData.ofStandardEntityType` (definition, [line 141](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L141))

```lean
public def SymEntityData.ofStandardEntityType (ety : EntityType) (sch : StandardSchemaEntry) : SymEntityData
```

`Cedar.SymCC.SymEntityData.emptyAttrs` (definition, [line 176](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L176))

```lean
public def SymEntityData.emptyAttrs (ety : EntityType) : UnaryFunction
```

`Cedar.SymCC.SymEntityData.ofEnumEntityType` (definition, [line 186](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L186))

```lean
public def SymEntityData.ofEnumEntityType (ety : EntityType) (eids : Set String) : SymEntityData
```

`Cedar.SymCC.SymEntityData.ofEntityType` (definition, [line 196](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L196))

```lean
public def SymEntityData.ofEntityType (ety : EntityType) : EntitySchemaEntry → SymEntityData
```

`Cedar.SymCC.SymEntityData.ofActionType` (definition, [line 202](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L202))

```lean
public def SymEntityData.ofActionType (actTy : EntityType) (actTys : List EntityType) (sch : ActionSchema) : SymEntityData
```

`Cedar.SymCC.SymEntities.ofSchema` (definition, [line 236](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L236))

> Creates symbolic entities for the given schema. This function assumes that the
> schemas are well-formed in the following sense:
> * All entity types that appear in the attributes or ancestors fields of `ets` are
>   declared either in `ets` or `acts`.
> * All entity types that appear in the ancestors fields of `acts` are declared in `acts`.
> An entity type is declared in `ets` if it's a key in the underlying map; it's
> declared in `acts` if it's the type of a key in the underlying map. This
> function also assumes `ets` and `ats` declare disjoint sets of types.
> This function assumes that no entity types have tags, and that action types
> have no attributes.

```lean
public def SymEntities.ofSchema (ets : EntitySchema) (acts : ActionSchema) : SymEntities
```

`Cedar.SymCC.SymRequest.ofRequestType` (definition, [line 245](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L245))

> Creates a symbolic request for the given request type.

```lean
public def SymRequest.ofRequestType (reqTy : RequestType) : SymRequest
```

`Cedar.SymCC.SymEnv.ofEnv` (definition, [line 257](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean#L257))

> Returns a symbolic environment that conforms to the given
> type environment.

```lean
public def SymEnv.ofEnv (tyEnv : TypeEnv) : SymEnv
```

## Depends on

- [Tags](tags.md)

## Sources

- [Cedar/SymCC/Env.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Env.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Env.json)

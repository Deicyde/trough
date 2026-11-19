---
catalog: module
lean: Cedar.Validation.BoolType, Cedar.Validation.BoolType.not, Cedar.Validation.BoolType.lift, Cedar.Validation.ExtType, Cedar.Validation.Qualified, Cedar.Validation.Qualified.getType, Cedar.Validation.Qualified.isRequired, Cedar.Validation.Qualified.map, Cedar.Validation.Qualified.transpose, Cedar.Validation.CedarType, Cedar.Validation.QualifiedType, Cedar.Validation.RecordType, Cedar.Validation.QualifiedType.liftBoolTypes, Cedar.Validation.RecordType.liftBoolTypes, Cedar.Validation.CedarType.liftBoolTypes, Cedar.Validation.StandardSchemaEntry, Cedar.Validation.EntitySchemaEntry, Cedar.Validation.EntitySchemaEntry.isValidEntityEID, Cedar.Validation.EntitySchemaEntry.tags?, Cedar.Validation.EntitySchemaEntry.attrs, Cedar.Validation.EntitySchemaEntry.ancestors, Cedar.Validation.EntitySchemaEntry.isStandard, Cedar.Validation.EntitySchemaEntry.withAncestors, Cedar.Validation.EntitySchema, Cedar.Validation.EntitySchema.entityTypeMembers?, Cedar.Validation.EntitySchema.isValidEntityUID, Cedar.Validation.EntitySchema.contains, Cedar.Validation.EntitySchema.attrs?, Cedar.Validation.EntitySchema.tags?, Cedar.Validation.ActionSchemaEntry, Cedar.Validation.ActionSchema, Cedar.Validation.ActionSchema.actionType?, Cedar.Validation.ActionSchema.contains, Cedar.Validation.ActionSchema.descendentOf, Cedar.Validation.Schema, Cedar.Validation.RequestType, Cedar.Validation.TypeEnv, Cedar.Validation.TypeEnv.schema, Cedar.Validation.ActionSchema.maybeDescendentOf, Cedar.Validation.TypeEnv.descendentOf, Cedar.Validation.decCedarType, Cedar.Validation.decEntitySchemaEntry
statement: formalized
proof: formalized
---

# Validation/Types

`Cedar.Validation.Types`, in [Cedar/Validation/Types.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean).

`Cedar.Validation.BoolType` (inductive type, [line 29](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L29))

```lean
public inductive BoolType where
  | anyBool
  | tt
  | ff
deriving Repr
```

`Cedar.Validation.BoolType.not` (definition, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L36))

```lean
public def BoolType.not : BoolType → BoolType
```

`Cedar.Validation.BoolType.lift` (definition, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L41))

```lean
public def BoolType.lift : BoolType → BoolType
```

`Cedar.Validation.ExtType` (inductive type, [line 44](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L44))

```lean
public inductive ExtType where
  | ipAddr
  | decimal
  | datetime
  | duration
deriving Repr
```

`Cedar.Validation.Qualified` (inductive type, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L51))

```lean
public inductive Qualified (α : Type u) where
  | optional (a : α)
  | required (a : α)
deriving Repr
```

`Cedar.Validation.Qualified.getType` (definition, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L62))

```lean
public def getType {α} : Qualified α → α
```

`Cedar.Validation.Qualified.isRequired` (definition, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L67))

```lean
public def isRequired {α} : Qualified α → Bool
```

`Cedar.Validation.Qualified.map` (definition, [line 72](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L72))

```lean
public def map {α β} (f : α → β) : Qualified α → Qualified β
```

`Cedar.Validation.Qualified.transpose` (definition, [line 76](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L76))

```lean
public def transpose {α ε} : Qualified (Except ε α) → Except ε (Qualified α)
```

`Cedar.Validation.CedarType` (inductive type, [line 84](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L84))

```lean
public inductive CedarType where
  | bool (bty : BoolType)
  | int
  | string
  | entity (ety : EntityType)
  | set (ty : CedarType)
  | record (rty : Map Attr (Qualified CedarType))
  | ext (xty : ExtType)
deriving Repr
```

`Cedar.Validation.QualifiedType` (abbreviation, [line 97](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L97))

```lean
public abbrev QualifiedType
```

`Cedar.Validation.RecordType` (abbreviation, [line 99](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L99))

```lean
public abbrev RecordType
```

`Cedar.Validation.QualifiedType.liftBoolTypes` (definition, [line 102](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L102))

```lean
public def QualifiedType.liftBoolTypes : QualifiedType → QualifiedType
```

`Cedar.Validation.RecordType.liftBoolTypes` (definition, [line 106](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L106))

```lean
public def RecordType.liftBoolTypes : RecordType → RecordType
```

`Cedar.Validation.CedarType.liftBoolTypes` (definition, [line 109](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L109))

```lean
public def CedarType.liftBoolTypes : CedarType → CedarType
```

`Cedar.Validation.StandardSchemaEntry` (structure, [line 116](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L116))

```lean
public structure StandardSchemaEntry where
  ancestors : Cedar.Data.Set EntityType
  attrs : RecordType
  tags : Option CedarType
```

`Cedar.Validation.EntitySchemaEntry` (inductive type, [line 121](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L121))

```lean
public inductive EntitySchemaEntry where
  | standard (ty: StandardSchemaEntry)
  | enum (eids: Set String)
```

`Cedar.Validation.EntitySchemaEntry.isValidEntityEID` (definition, [line 125](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L125))

```lean
public def EntitySchemaEntry.isValidEntityEID (entry: EntitySchemaEntry) (eid: String): Bool
```

`Cedar.Validation.EntitySchemaEntry.tags?` (definition, [line 130](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L130))

```lean
public def EntitySchemaEntry.tags? : EntitySchemaEntry → Option CedarType
```

`Cedar.Validation.EntitySchemaEntry.attrs` (definition, [line 134](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L134))

```lean
public def EntitySchemaEntry.attrs : EntitySchemaEntry → RecordType
```

`Cedar.Validation.EntitySchemaEntry.ancestors` (definition, [line 138](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L138))

```lean
public def EntitySchemaEntry.ancestors : EntitySchemaEntry → Set EntityType
```

`Cedar.Validation.EntitySchemaEntry.isStandard` (definition, [line 142](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L142))

```lean
public def EntitySchemaEntry.isStandard : EntitySchemaEntry → Bool
```

`Cedar.Validation.EntitySchemaEntry.withAncestors` (definition, [line 146](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L146))

```lean
public def EntitySchemaEntry.withAncestors (ancestors : Set EntityType) : EntitySchemaEntry → EntitySchemaEntry
```

`Cedar.Validation.EntitySchema` (abbreviation, [line 150](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L150))

```lean
public abbrev EntitySchema
```

`Cedar.Validation.EntitySchema.entityTypeMembers?` (definition, [line 152](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L152))

```lean
public def EntitySchema.entityTypeMembers? (ets: EntitySchema) (et: EntityType) : Option (Set String)
```

`Cedar.Validation.EntitySchema.isValidEntityUID` (definition, [line 157](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L157))

```lean
public def EntitySchema.isValidEntityUID (ets : EntitySchema) (uid : EntityUID) : Bool
```

`Cedar.Validation.EntitySchema.contains` (definition, [line 162](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L162))

```lean
public def EntitySchema.contains (ets : EntitySchema) (ety : EntityType) : Bool
```

`Cedar.Validation.EntitySchema.attrs?` (definition, [line 165](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L165))

```lean
public def EntitySchema.attrs? (ets : EntitySchema) (ety : EntityType) : Option RecordType
```

`Cedar.Validation.EntitySchema.tags?` (definition, [line 168](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L168))

```lean
public def EntitySchema.tags? (ets : EntitySchema) (ety : EntityType) : Option (Option CedarType)
```

`Cedar.Validation.ActionSchemaEntry` (structure, [line 171](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L171))

```lean
public structure ActionSchemaEntry where
  appliesToPrincipal : Set EntityType
  appliesToResource : Set EntityType
  ancestors : Set EntityUID
  context : RecordType
deriving Repr, Inhabited
```

`Cedar.Validation.ActionSchema` (abbreviation, [line 178](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L178))

```lean
public abbrev ActionSchema
```

`Cedar.Validation.ActionSchema.actionType?` (definition, [line 180](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L180))

```lean
public def ActionSchema.actionType? (acts: ActionSchema) (ety : EntityType) : Bool
```

`Cedar.Validation.ActionSchema.contains` (definition, [line 183](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L183))

```lean
public def ActionSchema.contains (as : ActionSchema) (uid : EntityUID) : Bool
```

`Cedar.Validation.ActionSchema.descendentOf` (definition, [line 186](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L186))

```lean
public def ActionSchema.descendentOf (as : ActionSchema)  (uid₁ uid₂ : EntityUID) : Bool
```

`Cedar.Validation.Schema` (structure, [line 193](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L193))

```lean
public structure Schema where
  ets : EntitySchema
  acts : ActionSchema
deriving Inhabited
```

`Cedar.Validation.RequestType` (structure, [line 198](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L198))

```lean
public structure RequestType where
  principal : EntityType
  action : EntityUID
  resource : EntityType
  context : RecordType
deriving Inhabited
```

`Cedar.Validation.TypeEnv` (structure, [line 205](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L205))

```lean
public structure TypeEnv where
  ets : EntitySchema
  acts : ActionSchema
  reqty : RequestType
deriving Inhabited
```

`Cedar.Validation.TypeEnv.schema` (definition, [line 211](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L211))

```lean
public def TypeEnv.schema (env : TypeEnv) : Schema
```

`Cedar.Validation.ActionSchema.maybeDescendentOf` (definition, [line 213](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L213))

```lean
public def ActionSchema.maybeDescendentOf (as : ActionSchema) (ety₁ ety₂ : EntityType) : Bool
```

`Cedar.Validation.TypeEnv.descendentOf` (definition, [line 216](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L216))

```lean
public def TypeEnv.descendentOf (env : TypeEnv) (ety₁ ety₂ : EntityType) : Bool
```

`Cedar.Validation.decCedarType` (definition, [line 236](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L236))

```lean
public def decCedarType (a b : CedarType) : Decidable (a = b)
```

`Cedar.Validation.decEntitySchemaEntry` (definition, [line 307](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean#L307))

```lean
public def decEntitySchemaEntry (e₁ e₂: EntitySchemaEntry) : Decidable (e₁ = e₂)
```

## Depends on

- [Value](../spec/value.md)

## Sources

- [Cedar/Validation/Types.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Types.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Validation.Types.json)

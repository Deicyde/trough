---
catalog: module
lean: Cedar.Spec.Prim.WellTyped, Cedar.Spec.Var.WellTyped, Cedar.Spec.UnaryOp.WellTyped, Cedar.Spec.BinaryOp.WellTyped, Cedar.Spec.ExtFun.WellTyped, Cedar.Thm.ExtHasAttrChainValid, Cedar.Thm.TypedExpr.WellTyped
statement: formalized
proof: formalized
---

# Expr/Definition

`Cedar.Thm.WellTyped.Expr.Definition`, in [Cedar/Thm/WellTyped/Expr/Definition.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Definition.lean).

> This file contains well-typedness definitions of `TypedExpr`

`Cedar.Spec.Prim.WellTyped` (inductive type, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Definition.lean#L31))

```lean
public inductive Prim.WellTyped (env : TypeEnv) : Prim → CedarType → Prop
  | bool (b : Bool) :
    WellTyped env (.bool b) (.bool .anyBool)
  | int (i : Int64) :
    WellTyped env (.int i) .int
  | string (s : String) :
    WellTyped env (.string s) .string
  | entityUID (uid : EntityUID)
    (h₁ : env.ets.isValidEntityUID uid ∨ env.acts.contains uid) :
    WellTyped env (.entityUID uid) (.entity uid.ty)
```

`Cedar.Spec.Var.WellTyped` (inductive type, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Definition.lean#L42))

```lean
public inductive Var.WellTyped (env : TypeEnv) : Var → CedarType → Prop
  | principal :
    WellTyped env .principal (.entity env.reqty.principal)
  | resource :
    WellTyped env .resource (.entity env.reqty.resource)
  | action :
    WellTyped env .action (.entity env.reqty.action.ty)
  | context:
    WellTyped env .context (CedarType.liftBoolTypes (.record env.reqty.context))
```

`Cedar.Spec.UnaryOp.WellTyped` (inductive type, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Definition.lean#L52))

```lean
public inductive UnaryOp.WellTyped : UnaryOp → TypedExpr → CedarType → Prop
  | not {x₁ : TypedExpr}
    (h₁ : x₁.typeOf = .bool .anyBool) :
    WellTyped .not x₁ (.bool .anyBool)
  | neg {x₁ : TypedExpr}
    (h₁ : x₁.typeOf = .int) :
    WellTyped .neg x₁ .int
  | isEmpty {x₁ : TypedExpr} {eltTy : CedarType}
    (h₁ : x₁.typeOf = .set eltTy) :
    WellTyped .isEmpty x₁ (.bool .anyBool)
  | like {x₁ : TypedExpr} {p : Pattern}
    (h₁ : x₁.typeOf = .string) :
    WellTyped (.like p) x₁ (.bool .anyBool)
  | is {ety₁ ety₂ : EntityType}
    (h₁ : x₁.typeOf = .entity ety₂) :
    WellTyped (.is ety₁) x₁ (.bool .anyBool)
```

`Cedar.Spec.BinaryOp.WellTyped` (inductive type, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Definition.lean#L69))

```lean
public inductive BinaryOp.WellTyped (env : TypeEnv) : BinaryOp → TypedExpr → TypedExpr → CedarType → Prop
  | eq_lit {p₁ p₂ : Prim} {ty₁ ty₂ : CedarType} :
    -- do we need hypothesis like `InstanceOfType (.prim p₁) ty₁`?
    WellTyped env .eq (.lit p₁ ty₁) (.lit p₂ ty₂) (.bool .anyBool)
  | eq_entity {ety₁ ety₂ : EntityType} {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .entity ety₁)
    (h₂ : x₂.typeOf = .entity ety₂) :
    WellTyped env .eq x₁ x₂ (.bool .anyBool)
  | eq {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = x₂.typeOf) :
    WellTyped env .eq x₁ x₂ (.bool .anyBool)
  | memₑ {x₁ x₂ : TypedExpr} {ety₁ ety₂ : EntityType}
    (h₁ : x₁.typeOf = .entity ety₁)
    (h₂ : x₂.typeOf = .entity ety₂) :
    WellTyped env .mem x₁ x₂ (.bool .anyBool)
  | memₛ {x₁ x₂ : TypedExpr} {ety₁ ety₂ : EntityType}
    (h₁ : x₁.typeOf = .entity ety₁)
    (h₂ : x₂.typeOf = .set (.entity ety₂)) :
    WellTyped env .mem x₁ x₂ (.bool .anyBool)
  | less_int {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .int)
    (h₂ : x₂.typeOf = .int) :
    WellTyped env .less x₁ x₂ (.bool .anyBool)
  | less_datetime {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .datetime)
    (h₂ : x₂.typeOf = .ext .datetime) :
    WellTyped env .less x₁ x₂ (.bool .anyBool)
  | less_duration {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .duration)
    (h₂ : x₂.typeOf = .ext .duration) :
    WellTyped env .less x₁ x₂ (.bool .anyBool)
  | lessEq_int {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .int)
    (h₂ : x₂.typeOf = .int) :
    WellTyped env .lessEq x₁ x₂ (.bool .anyBool)
  | lessEq_datetime {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .datetime)
    (h₂ : x₂.typeOf = .ext .datetime) :
    WellTyped env .lessEq x₁ x₂ (.bool .anyBool)
  | lessEq_duration {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .duration)
    (h₂ : x₂.typeOf = .ext .duration) :
    WellTyped env .lessEq x₁ x₂ (.bool .anyBool)
  | add {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .int)
    (h₂ : x₂.typeOf = .int) :
    WellTyped env .add x₁ x₂ .int
  | sub {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .int)
    (h₂ : x₂.typeOf = .int) :
    WellTyped env .sub x₁ x₂ .int
  | mul {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .int)
    (h₂ : x₂.typeOf = .int) :
    WellTyped env .mul x₁ x₂ .int
  | contains {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .set x₂.typeOf) :
    WellTyped env .contains x₁ x₂ (.bool .anyBool)
  | containsAll {x₁ x₂ : TypedExpr} {ty : CedarType}
    (h₁ : x₁.typeOf = .set ty)
    (h₂ : x₂.typeOf = .set ty) :
    WellTyped env .containsAll x₁ x₂ (.bool .anyBool)
  | containsAny {x₁ x₂ : TypedExpr} {ty : CedarType}
    (h₁ : x₁.typeOf = .set ty)
    (h₂ : x₂.typeOf = .set ty) :
    WellTyped env .containsAny x₁ x₂ (.bool .anyBool)
  | hasTag {x₁ x₂ : TypedExpr} {ety : EntityType}
    (h₁ : x₁.typeOf = .entity ety)
    (h₂ : x₂.typeOf = .string) :
    WellTyped env .hasTag x₁ x₂ (.bool .anyBool)
  | getTag {x₁ x₂ : TypedExpr} {ety : EntityType} {ty : CedarType}
    (h₁ : x₁.typeOf = .entity ety)
    (h₂ : x₂.typeOf = .string)
    (h₃ : env.ets.tags? ety = .some (.some ty)) :
    WellTyped env .getTag x₁ x₂ ty.liftBoolTypes
```

`Cedar.Spec.ExtFun.WellTyped` (inductive type, [line 145](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Definition.lean#L145))

```lean
public inductive ExtFun.WellTyped : ExtFun → List TypedExpr → CedarType → Prop
  | decimal {s₁ : String} {d₁ : Decimal}
    (h₁ : d₁ = Decimal.decimal s₁) :
    WellTyped .decimal [.lit (.string s₁) .string] (.ext .decimal)
  | lessThan {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .decimal)
    (h₂ : x₂.typeOf = .ext .decimal) :
    WellTyped .lessThan [x₁, x₂] (.bool .anyBool)
  | lessThanOrEqual {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .decimal)
    (h₂ : x₂.typeOf = .ext .decimal) :
    WellTyped .lessThanOrEqual [x₁, x₂] (.bool .anyBool)
  | greaterThan {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .decimal)
    (h₂ : x₂.typeOf = .ext .decimal) :
    WellTyped .greaterThan [x₁, x₂] (.bool .anyBool)
  | greaterThanOrEqual {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .decimal)
    (h₂ : x₂.typeOf = .ext .decimal) :
    WellTyped .greaterThanOrEqual [x₁, x₂] (.bool .anyBool)
  | ip {s₁ : String} {ip₁ : IPAddr}
    (h₁ : ip₁ =  IPAddr.ip s₁) :
    WellTyped .ip [.lit (.string s₁) .string] (.ext .ipAddr)
  | isIpv4 {x₁ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .ipAddr) :
    WellTyped .isIpv4 [x₁] (.bool .anyBool)
  | isIpv6 {x₁ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .ipAddr) :
    WellTyped .isIpv6 [x₁] (.bool .anyBool)
  | isLoopback {x₁ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .ipAddr) :
    WellTyped .isLoopback [x₁] (.bool .anyBool)
  | isMulticast {x₁ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .ipAddr) :
    WellTyped .isMulticast [x₁] (.bool .anyBool)
  | isInRange {x₁ : TypedExpr} {xs : List TypedExpr}
    (h₁ : x₁.typeOf = .ext .ipAddr)
    (h₂ : xs.length > 0)
    (h₃ : ∀ x ∈ xs, x.typeOf = .ext .ipAddr):
    WellTyped .isInRange (x₁ :: xs) (.bool .anyBool)
  | datetime {s₁ : String} {d₁ : Datetime}
    (h₁ : d₁ =  Datetime.parse s₁) :
    WellTyped .datetime [.lit (.string s₁) .string] (.ext .datetime)
  | duration {s₁ : String} {d₁ : Duration}
    (h₁ : d₁ =  Datetime.Duration.parse s₁) :
    WellTyped .duration [.lit (.string s₁) .string] (.ext .duration)
  | offset {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .datetime)
    (h₂ : x₂.typeOf = .ext .duration):
    WellTyped .offset [x₁, x₂] (.ext .datetime)
  | durationSince {x₁ x₂ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .datetime)
    (h₂ : x₂.typeOf = .ext .datetime):
    WellTyped .durationSince [x₁, x₂] (.ext .duration)
  | toDate {x₁ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .datetime) :
    WellTyped .toDate [x₁] (.ext .datetime)
  | toTime {x₁ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .datetime) :
    WellTyped .toTime [x₁] (.ext .duration)
  | toMilliseconds {x₁ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .duration) :
    WellTyped .toMilliseconds [x₁] .int
  | toSeconds {x₁ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .duration) :
    WellTyped .toSeconds [x₁] .int
  | toMinutes {x₁ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .duration) :
    WellTyped .toMinutes [x₁] .int
  | toHours {x₁ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .duration) :
    WellTyped .toHours [x₁] .int
  | toDays {x₁ : TypedExpr}
    (h₁ : x₁.typeOf = .ext .duration) :
    WellTyped .toDays [x₁] .int
```

`Cedar.Thm.ExtHasAttrChainValid` (inductive type, [line 239](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Definition.lean#L239))

> Chain validity for extended `has` attribute checks.
> Starting from a Cedar type, each intermediate attribute access in the chain
> must either:
> - yield an entity or record type (so that `attrsOf` succeeds on the next value),
> - not be present in the schema (absent attribute is valid).
> The LAST attribute in the chain doesn't need this constraint (we just check existence).
> In other words, a valid chain doesn't have intermediate accesses to attributes that are
> neither entitiy nor records.

```lean
public inductive ExtHasAttrChainValid (ets : EntitySchema) : CedarType → List Attr → Prop where
  /-- A single-attribute chain is always valid (just a `has` check, no deeper traversal) -/
  | last {ty : CedarType} {attr : Attr} :
    ExtHasAttrChainValid ets ty [attr]
  /-- Intermediate attribute has entity type in the schema -/
  | cons_entity {ety nextEty : EntityType} {attr : Attr} {rest : List Attr}
    {rty : RecordType} {qty : QualifiedType}
    (h₁ : ets.attrs? ety = .some rty)
    (h₂ : rty.find? attr = .some qty)
    (h₃ : qty.getType = .entity nextEty)
    (h₄ : ExtHasAttrChainValid ets (.entity nextEty) rest) :
    ExtHasAttrChainValid ets (.entity ety) (attr :: rest)
  /-- Intermediate attribute has record type in the schema -/
  | cons_record_from_entity {ety : EntityType} {attr : Attr} {rest : List Attr}
    {rty : RecordType} {qty : QualifiedType} {recRty : RecordType}
    (h₁ : ets.attrs? ety = .some rty)
    (h₂ : rty.find? attr = .some qty)
    (h₃ : qty.getType = .record recRty)
    (h₄ : ExtHasAttrChainValid ets (.record recRty) rest) :
    ExtHasAttrChainValid ets (.entity ety) (attr :: rest)
  /-- Attribute not found in schema for entity — chain is vacuously valid
      (at runtime, `find?` will return `.none` → `.ok false`) -/
  | cons_not_in_schema_entity {ety : EntityType} {attr : Attr} {rest : List Attr}
    (h₁ : ets.attrs? ety = .none ∨ ∀ rty, ets.attrs? ety = .some rty → rty.find? attr = .none) :
    ExtHasAttrChainValid ets (.entity ety) (attr :: rest)
  /-- Record type: intermediate attribute has entity type -/
  | cons_entity_from_record {recRty : RecordType} {attr : Attr} {rest : List Attr}
    {qty : QualifiedType} {nextEty : EntityType}
    (h₁ : recRty.find? attr = .some qty)
    (h₂ : qty.getType = .entity nextEty)
    (h₃ : ExtHasAttrChainValid ets (.entity nextEty) rest) :
    ExtHasAttrChainValid ets (.record recRty) (attr :: rest)
  /-- Record type: intermediate attribute has record type -/
  | cons_record_from_record {recRty : RecordType} {attr : Attr} {rest : List Attr}
    {qty : QualifiedType} {nextRecRty : RecordType}
    (h₁ : recRty.find? attr = .some qty)
    (h₂ : qty.getType = .record nextRecRty)
    (h₃ : ExtHasAttrChainValid ets (.record nextRecRty) rest) :
    ExtHasAttrChainValid ets (.record recRty) (attr :: rest)
  /-- Record type: attribute not in record type — vacuously valid -/
  | cons_not_in_record {recRty : RecordType} {attr : Attr} {rest : List Attr}
    (h₁ : recRty.find? attr = .none) :
    ExtHasAttrChainValid ets (.record recRty) (attr :: rest)
```

`Cedar.Thm.TypedExpr.WellTyped` (inductive type, [line 284](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Definition.lean#L284))

```lean
public inductive TypedExpr.WellTyped (env : TypeEnv) : TypedExpr → Prop
```

## Depends on

- [TypedExpr](../../../validation/typedexpr.md)

## Sources

- [Cedar/Thm/WellTyped/Expr/Definition.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Definition.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.WellTyped.Expr.Definition.json)

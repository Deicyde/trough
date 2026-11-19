---
catalog: module
lean: Cedar.Spec.UnaryResidualWellTyped, Cedar.Spec.BinaryResidualWellTyped, Cedar.Spec.ExtResidualWellTyped, Cedar.Thm.Residual.WellTyped, Cedar.Thm.well_typed_bool, Cedar.Thm.well_typed_int, Cedar.Thm.well_typed_string, Cedar.Thm.well_typed_entity
statement: formalized
proof: formalized
---

# Residual/Definition

`Cedar.Thm.WellTyped.Residual.Definition`, in [Cedar/Thm/WellTyped/Residual/Definition.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Definition.lean).

> This file contains well-typedness definitions of `TypedExpr`

`Cedar.Spec.UnaryResidualWellTyped` (inductive type, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Definition.lean#L31))

```lean
inductive UnaryResidualWellTyped : UnaryOp → Residual → CedarType → Prop
  | not {x₁ : Residual}
    (h₁ : x₁.typeOf = .bool .anyBool) :
    UnaryResidualWellTyped .not x₁ (.bool .anyBool)
  | neg {x₁ : Residual}
    (h₁ : x₁.typeOf = .int) :
    UnaryResidualWellTyped .neg x₁ .int
  | isEmpty {x₁ : Residual} {eltTy : CedarType}
    (h₁ : x₁.typeOf = .set eltTy) :
    UnaryResidualWellTyped .isEmpty x₁ (.bool .anyBool)
  | like {x₁ : Residual} {p : Pattern}
    (h₁ : x₁.typeOf = .string) :
    UnaryResidualWellTyped (.like p) x₁ (.bool .anyBool)
  | is {ety₁ ety₂ : EntityType}
    (h₁ : x₁.typeOf = .entity ety₂) :
    UnaryResidualWellTyped (.is ety₁) x₁ (.bool .anyBool)
```

`Cedar.Spec.BinaryResidualWellTyped` (inductive type, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Definition.lean#L48))

```lean
inductive BinaryResidualWellTyped (env : TypeEnv) : BinaryOp → Residual → Residual → CedarType → Prop
  | eq_val {p₁ p₂ : Value} {ty₁ ty₂ : CedarType} :
    BinaryResidualWellTyped env .eq (.val p₁ ty₁) (.val p₂ ty₂) (.bool .anyBool)
  | eq_entity {ety₁ ety₂ : EntityType} {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .entity ety₁)
    (h₂ : x₂.typeOf = .entity ety₂) :
    BinaryResidualWellTyped env .eq x₁ x₂ (.bool .anyBool)
  | eq {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = x₂.typeOf) :
    BinaryResidualWellTyped env .eq x₁ x₂ (.bool .anyBool)
  | memₑ {x₁ x₂ : Residual} {ety₁ ety₂ : EntityType}
    (h₁ : x₁.typeOf = .entity ety₁)
    (h₂ : x₂.typeOf = .entity ety₂) :
    BinaryResidualWellTyped env .mem x₁ x₂ (.bool .anyBool)
  | memₛ {x₁ x₂ : Residual} {ety₁ ety₂ : EntityType}
    (h₁ : x₁.typeOf = .entity ety₁)
    (h₂ : x₂.typeOf = .set (.entity ety₂)) :
    BinaryResidualWellTyped env .mem x₁ x₂ (.bool .anyBool)
  | less_int {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .int)
    (h₂ : x₂.typeOf = .int) :
    BinaryResidualWellTyped env .less x₁ x₂ (.bool .anyBool)
  | less_datetime {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .ext .datetime)
    (h₂ : x₂.typeOf = .ext .datetime) :
    BinaryResidualWellTyped env .less x₁ x₂ (.bool .anyBool)
  | less_duration {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .ext .duration)
    (h₂ : x₂.typeOf = .ext .duration) :
    BinaryResidualWellTyped env .less x₁ x₂ (.bool .anyBool)
  | lessEq_int {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .int)
    (h₂ : x₂.typeOf = .int) :
    BinaryResidualWellTyped env .lessEq x₁ x₂ (.bool .anyBool)
  | lessEq_datetime {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .ext .datetime)
    (h₂ : x₂.typeOf = .ext .datetime) :
    BinaryResidualWellTyped env .lessEq x₁ x₂ (.bool .anyBool)
  | lessEq_duration {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .ext .duration)
    (h₂ : x₂.typeOf = .ext .duration) :
    BinaryResidualWellTyped env .lessEq x₁ x₂ (.bool .anyBool)
  | add {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .int)
    (h₂ : x₂.typeOf = .int) :
    BinaryResidualWellTyped env .add x₁ x₂ .int
  | sub {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .int)
    (h₂ : x₂.typeOf = .int) :
    BinaryResidualWellTyped env .sub x₁ x₂ .int
  | mul {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .int)
    (h₂ : x₂.typeOf = .int) :
    BinaryResidualWellTyped env .mul x₁ x₂ .int
  | contains {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .set x₂.typeOf) :
    BinaryResidualWellTyped env .contains x₁ x₂ (.bool .anyBool)
  | containsAll {x₁ x₂ : Residual} {ty : CedarType}
    (h₁ : x₁.typeOf = .set ty)
    (h₂ : x₂.typeOf = .set ty) :
    BinaryResidualWellTyped env .containsAll x₁ x₂ (.bool .anyBool)
  | containsAny {x₁ x₂ : Residual} {ty : CedarType}
    (h₁ : x₁.typeOf = .set ty)
    (h₂ : x₂.typeOf = .set ty) :
    BinaryResidualWellTyped env .containsAny x₁ x₂ (.bool .anyBool)
  | hasTag {x₁ x₂ : Residual} {ety : EntityType}
    (h₁ : x₁.typeOf = .entity ety)
    (h₂ : x₂.typeOf = .string) :
    BinaryResidualWellTyped env .hasTag x₁ x₂ (.bool .anyBool)
  | getTag {x₁ x₂ : Residual} {ety : EntityType} {ty : CedarType}
    (h₁ : x₁.typeOf = .entity ety)
    (h₂ : x₂.typeOf = .string)
    (h₃ : env.ets.tags? ety = .some (.some ty)) :
    BinaryResidualWellTyped env .getTag x₁ x₂ ty.liftBoolTypes
```

`Cedar.Spec.ExtResidualWellTyped` (inductive type, [line 124](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Definition.lean#L124))

```lean
inductive ExtResidualWellTyped : ExtFun → List Residual → CedarType → Prop
  | decimal {s₁ : String} {d₁ : Decimal}
    (h₁ : d₁ = Decimal.decimal s₁) :
    ExtResidualWellTyped .decimal [.val (.prim (.string s₁)) .string] (.ext .decimal)
  | lessThan {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .ext .decimal)
    (h₂ : x₂.typeOf = .ext .decimal) :
    ExtResidualWellTyped .lessThan [x₁, x₂] (.bool .anyBool)
  | lessThanOrEqual {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .ext .decimal)
    (h₂ : x₂.typeOf = .ext .decimal) :
    ExtResidualWellTyped .lessThanOrEqual [x₁, x₂] (.bool .anyBool)
  | greaterThan {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .ext .decimal)
    (h₂ : x₂.typeOf = .ext .decimal) :
    ExtResidualWellTyped .greaterThan [x₁, x₂] (.bool .anyBool)
  | greaterThanOrEqual {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .ext .decimal)
    (h₂ : x₂.typeOf = .ext .decimal) :
    ExtResidualWellTyped .greaterThanOrEqual [x₁, x₂] (.bool .anyBool)
  | ip {s₁ : String} {ip₁ : IPAddr}
    (h₁ : ip₁ =  IPAddr.ip s₁) :
    ExtResidualWellTyped .ip [.val (.prim (.string s₁)) .string] (.ext .ipAddr)
  | isIpv4 {x₁ : Residual}
    (h₁ : x₁.typeOf = .ext .ipAddr) :
    ExtResidualWellTyped .isIpv4 [x₁] (.bool .anyBool)
  | isIpv6 {x₁ : Residual}
    (h₁ : x₁.typeOf = .ext .ipAddr) :
    ExtResidualWellTyped .isIpv6 [x₁] (.bool .anyBool)
  | isLoopback {x₁ : Residual}
    (h₁ : x₁.typeOf = .ext .ipAddr) :
    ExtResidualWellTyped .isLoopback [x₁] (.bool .anyBool)
  | isMulticast {x₁ : Residual}
    (h₁ : x₁.typeOf = .ext .ipAddr) :
    ExtResidualWellTyped .isMulticast [x₁] (.bool .anyBool)
  | isInRange {x₁ : Residual} {xs : List Residual}
    (h₁ : x₁.typeOf = .ext .ipAddr)
    (h₂ : xs.length > 0)
    (h₃ : ∀ x ∈ xs, x.typeOf = .ext .ipAddr):
    ExtResidualWellTyped .isInRange (x₁ :: xs) (.bool .anyBool)
  | datetime {s₁ : String} {d₁ : Datetime}
    (h₁ : d₁ =  Datetime.parse s₁) :
    ExtResidualWellTyped .datetime [.val (.prim (.string s₁)) .string] (.ext .datetime)
  | duration {s₁ : String} {d₁ : Duration}
    (h₁ : d₁ =  Datetime.Duration.parse s₁) :
    ExtResidualWellTyped .duration [.val (.prim (.string s₁)) .string] (.ext .duration)
  | offset {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .ext .datetime)
    (h₂ : x₂.typeOf = .ext .duration):
    ExtResidualWellTyped .offset [x₁, x₂] (.ext .datetime)
  | durationSince {x₁ x₂ : Residual}
    (h₁ : x₁.typeOf = .ext .datetime)
    (h₂ : x₂.typeOf = .ext .datetime):
    ExtResidualWellTyped .durationSince [x₁, x₂] (.ext .duration)
  | toDate {x₁ : Residual}
    (h₁ : x₁.typeOf = .ext .datetime) :
    ExtResidualWellTyped .toDate [x₁] (.ext .datetime)
  | toTime {x₁ : Residual}
    (h₁ : x₁.typeOf = .ext .datetime) :
    ExtResidualWellTyped .toTime [x₁] (.ext .duration)
  | toMilliseconds {x₁ : Residual}
    (h₁ : x₁.typeOf = .ext .duration) :
    ExtResidualWellTyped .toMilliseconds [x₁] .int
  | toSeconds {x₁ : Residual}
    (h₁ : x₁.typeOf = .ext .duration) :
    ExtResidualWellTyped .toSeconds [x₁] .int
  | toMinutes {x₁ : Residual}
    (h₁ : x₁.typeOf = .ext .duration) :
    ExtResidualWellTyped .toMinutes [x₁] .int
  | toHours {x₁ : Residual}
    (h₁ : x₁.typeOf = .ext .duration) :
    ExtResidualWellTyped .toHours [x₁] .int
  | toDays {x₁ : Residual}
    (h₁ : x₁.typeOf = .ext .duration) :
    ExtResidualWellTyped .toDays [x₁] .int
```

`Cedar.Thm.Residual.WellTyped` (inductive type, [line 212](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Definition.lean#L212))

> Well-typedness definition for Residual expressions

```lean
inductive Residual.WellTyped (env : TypeEnv) : Residual → Prop
```

`Cedar.Thm.well_typed_bool` (theorem, [line 292](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Definition.lean#L292))

```lean
theorem well_typed_bool {env : TypeEnv} {b : Bool}:
 Residual.WellTyped env (.val (.prim (.bool b)) (CedarType.bool BoolType.anyBool))
```

`Cedar.Thm.well_typed_int` (theorem, [line 296](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Definition.lean#L296))

```lean
theorem well_typed_int {env : TypeEnv} {i : Int64}:
 Residual.WellTyped env (.val (.prim (.int i)) CedarType.int)
```

`Cedar.Thm.well_typed_string` (theorem, [line 300](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Definition.lean#L300))

```lean
theorem well_typed_string {env : TypeEnv} {s : String}:
 Residual.WellTyped env (.val (.prim (.string s)) CedarType.string)
```

`Cedar.Thm.well_typed_entity` (theorem, [line 304](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Definition.lean#L304))

```lean
theorem well_typed_entity {env : TypeEnv} {e : EntityUID} {ety : EntityType} :
  InstanceOfEntityType e ety env → Residual.WellTyped env (.val (.prim (.entityUID e)) (.entity ety))
```

## Depends on

- [TPE/Residual](../../../tpe/residual.md)
- [Typechecker/Types](../../validation-2/typechecker-2/types.md)
- [Expr/Definition](../expr-2/definition.md)

## Sources

- [Cedar/Thm/WellTyped/Residual/Definition.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Residual/Definition.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.WellTyped.Residual.Definition.json)

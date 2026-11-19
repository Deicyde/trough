---
catalog: module
lean: Cedar.Thm.InstanceOfBoolType, Cedar.Thm.InstanceOfEntityType, Cedar.Thm.InstanceOfExtType, Cedar.Thm.InstanceOfType, Cedar.Thm.InstanceOfRequestType, Cedar.Thm.InstanceOfEntityTags, Cedar.Thm.IsValidEntityEID, Cedar.Thm.InstanceOfEntitySchemaEntry, Cedar.Thm.InstanceOfActionSchemaEntry, Cedar.Thm.InstanceOfSchemaEntry, Cedar.Thm.Entities.HasAllActions, Cedar.Thm.InstanceOfSchema, Cedar.Thm.InstanceOfWellFormedEnvironment, Cedar.Thm.false_is_instance_of_ff, Cedar.Thm.true_is_instance_of_tt, Cedar.Thm.bool_is_instance_of_anyBool, Cedar.Thm.duration_is_instance_of_duration, Cedar.Thm.datetime_is_instance_of_datetime, Cedar.Thm.decimal_is_instance_of_decimal, Cedar.Thm.ipaddr_is_instance_of_ipaddr, Cedar.Thm.instance_of_bool_is_bool, Cedar.Thm.instance_of_ff_is_false, Cedar.Thm.instance_of_tt_is_true, Cedar.Thm.instance_of_anyBool_is_bool, Cedar.Thm.instance_of_int_is_int, Cedar.Thm.instance_of_string_is_string, Cedar.Thm.instance_of_entity_type_is_entity, Cedar.Thm.instance_of_decimal_type_is_decimal, Cedar.Thm.instance_of_ipAddr_type_is_ipAddr, Cedar.Thm.instance_of_datetime_type_is_datetime, Cedar.Thm.instance_of_duration_type_is_duration, Cedar.Thm.instance_of_set_type_is_set, Cedar.Thm.instance_of_record_type_is_record, Cedar.Thm.instance_of_attribute_type, Cedar.Thm.absent_attribute_is_absent, Cedar.Thm.required_attribute_is_present, Cedar.Thm.well_typed_entity_attributes, Cedar.Thm.instance_of_type_bool_is_bool, Cedar.Thm.bool_type_is_inhabited, Cedar.Thm.entity_type_is_inhabited, Cedar.Thm.ext_type_is_inhabited, Cedar.Thm.instance_of_record_nil, Cedar.Thm.instance_of_record_cons, Cedar.Thm.sizeOf_attribute_lt_sizeOf_qualified, Cedar.Thm.type_is_inhabited_bool, Cedar.Thm.type_is_inhabited_int, Cedar.Thm.type_is_inhabited_string, Cedar.Thm.type_is_inhabited_entity, Cedar.Thm.type_is_inhabited_set, Cedar.Thm.type_is_inhabited_ext, Cedar.Thm.type_is_inhabited_record, Cedar.Thm.type_is_inhabited, Cedar.Thm.instance_of_lubBool_left, Cedar.Thm.instance_of_lubBool, Cedar.Thm.sizeOf_attr_type_lt_sizeOf_record_type, Cedar.Thm.instance_of_lub_left, Cedar.Thm.instance_of_lub, Cedar.Thm.type_of_lit_inversion, Cedar.Thm.InstanceOfWellFormedEnvironment.wf_env, Cedar.Thm.InstanceOfWellFormedEnvironment.instance_of_schema_entry, Cedar.Thm.InstanceOfWellFormedEnvironment.instance_of_schema, Cedar.Thm.InstanceOfWellFormedEnvironment.wf_action_data
statement: formalized
proof: formalized
---

# Typechecker/Types

`Cedar.Thm.Validation.Typechecker.Types`, in [Cedar/Thm/Validation/Typechecker/Types.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean).

> This file contains useful definitions and lemmas about Cedar types.

`Cedar.Thm.InstanceOfBoolType` (definition, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L43))

```lean
def InstanceOfBoolType : Bool → BoolType → Prop
```

`Cedar.Thm.InstanceOfEntityType` (definition, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L49))

```lean
def InstanceOfEntityType (e : EntityUID) (ety: EntityType) (env : TypeEnv) : Prop
```

`Cedar.Thm.InstanceOfExtType` (definition, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L52))

```lean
def InstanceOfExtType : Ext → ExtType → Prop
```

`Cedar.Thm.InstanceOfType` (inductive type, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L59))

```lean
inductive InstanceOfType (env : TypeEnv) : Value → CedarType → Prop where
  | instance_of_bool (b : Bool) (bty : BoolType)
      (h₁ : InstanceOfBoolType b bty) :
      InstanceOfType env (.prim (.bool b)) (.bool bty)
  | instance_of_int :
      InstanceOfType env (.prim (.int _)) .int
  | instance_of_string :
      InstanceOfType env (.prim (.string _)) .string
  | instance_of_entity (e : EntityUID) (ety: EntityType)
      (h₁ : InstanceOfEntityType e ety env) :
      InstanceOfType env (.prim (.entityUID e)) (.entity ety)
  | instance_of_set (s : Set Value) (ty : CedarType)
      (h₁ : ∀ v, v ∈ s → InstanceOfType env v ty) :
      InstanceOfType env (.set s) (.set ty)
  | instance_of_record (r : Map Attr Value) (rty : RecordType)
      -- if an attribute is present in the record, then it is present in the type
      (h₁ : ∀ (k : Attr), r.contains k → rty.contains k)
      -- if an attribute is present, then it has the expected type
      (h₂ : ∀ (k : Attr) (v : Value) (qty : QualifiedType),
        r.find? k = some v → rty.find? k = some qty → InstanceOfType env v qty.getType)
      -- required attributes are present
      (h₃ : ∀ (k : Attr) (qty : QualifiedType), rty.find? k = some qty → qty.isRequired → r.contains k) :
      InstanceOfType env (.record r) (.record rty)
  | instance_of_ext (x : Ext) (xty : ExtType)
      (h₁ : InstanceOfExtType x xty) :
      InstanceOfType env (.ext x) (.ext xty)
```

`Cedar.Thm.InstanceOfRequestType` (definition, [line 86](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L86))

```lean
def InstanceOfRequestType (request : Request) (env : TypeEnv) : Prop
```

`Cedar.Thm.InstanceOfEntityTags` (definition, [line 92](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L92))

```lean
def InstanceOfEntityTags (data : EntityData) (entry : EntitySchemaEntry) (env : TypeEnv) : Prop
```

`Cedar.Thm.IsValidEntityEID` (definition, [line 97](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L97))

```lean
def IsValidEntityEID (entry: EntitySchemaEntry) (eid: String) : Prop
```

`Cedar.Thm.InstanceOfEntitySchemaEntry` (definition, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L110))

> For every entity `(uid, data)` in the store,
> 1. The entity's type is defined in the type store.
> 2. The entity's attributes match the attribute types indicated in the type store.
> 3. The entity's ancestors' types are consistent with the ancestor information
>    in the type store.
> 4. The entity's tags' types are consistent with the tags information in the type store.

```lean
def InstanceOfEntitySchemaEntry (uid : EntityUID) (data : EntityData) (env : TypeEnv) : Prop
```

`Cedar.Thm.InstanceOfActionSchemaEntry` (definition, [line 121](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L121))

> Similar to `WellFormedEntityData`, but a special case for action entities
> since they are stored disjoint from `ets`

```lean
def InstanceOfActionSchemaEntry (uid : EntityUID) (data : EntityData) (env : TypeEnv) : Prop
```

`Cedar.Thm.InstanceOfSchemaEntry` (definition, [line 129](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L129))

```lean
def InstanceOfSchemaEntry (uid : EntityUID) (data : EntityData) (env : TypeEnv) : Prop
```

`Cedar.Thm.Entities.HasAllActions` (definition, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L133))

```lean
def Entities.HasAllActions (entities : Entities) (env : TypeEnv) : Prop
```

`Cedar.Thm.InstanceOfSchema` (definition, [line 140](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L140))

> Each entry in the store is valid

```lean
def InstanceOfSchema (entities : Entities) (env : TypeEnv) : Prop
```

`Cedar.Thm.InstanceOfWellFormedEnvironment` (definition, [line 146](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L146))

```lean
def InstanceOfWellFormedEnvironment (request : Request) (entities : Entities) (env : TypeEnv) : Prop
```

`Cedar.Thm.false_is_instance_of_ff` (theorem, [line 153](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L153))

```lean
theorem false_is_instance_of_ff {env : TypeEnv} :
  InstanceOfType env (Value.prim (Prim.bool false)) (CedarType.bool BoolType.ff)
```

`Cedar.Thm.true_is_instance_of_tt` (theorem, [line 159](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L159))

```lean
theorem true_is_instance_of_tt {env : TypeEnv} :
  InstanceOfType env (Value.prim (Prim.bool true)) (CedarType.bool BoolType.tt)
```

`Cedar.Thm.bool_is_instance_of_anyBool` (theorem, [line 165](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L165))

```lean
theorem bool_is_instance_of_anyBool {env : TypeEnv} (b : Bool) :
  InstanceOfType env (Value.prim (Prim.bool b)) (CedarType.bool BoolType.anyBool)
```

`Cedar.Thm.duration_is_instance_of_duration` (theorem, [line 171](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L171))

```lean
theorem duration_is_instance_of_duration {env : TypeEnv} {d : Duration}:
  InstanceOfType env (Value.ext (Ext.duration d)) (CedarType.ext .duration)
```

`Cedar.Thm.datetime_is_instance_of_datetime` (theorem, [line 177](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L177))

```lean
theorem datetime_is_instance_of_datetime {env : TypeEnv} {d : Ext.Datetime}:
  InstanceOfType env (Value.ext (Ext.datetime d)) (CedarType.ext .datetime)
```

`Cedar.Thm.decimal_is_instance_of_decimal` (theorem, [line 183](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L183))

```lean
theorem decimal_is_instance_of_decimal {env : TypeEnv} {d : Ext.Decimal}:
  InstanceOfType env (Value.ext (Ext.decimal d)) (CedarType.ext .decimal)
```

`Cedar.Thm.ipaddr_is_instance_of_ipaddr` (theorem, [line 189](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L189))

```lean
theorem ipaddr_is_instance_of_ipaddr {env : TypeEnv} {ip : IPAddr}:
  InstanceOfType env (Value.ext (Ext.ipaddr ip)) (CedarType.ext .ipAddr)
```

`Cedar.Thm.instance_of_bool_is_bool` (theorem, [line 195](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L195))

```lean
theorem instance_of_bool_is_bool {env : TypeEnv} {v₁ : Value} {bty : BoolType} :
  InstanceOfType env v₁ (CedarType.bool bty) →
  ∃ b, v₁ = .prim (.bool b)
```

`Cedar.Thm.instance_of_ff_is_false` (theorem, [line 203](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L203))

```lean
theorem instance_of_ff_is_false {env : TypeEnv} {v₁ : Value} :
  InstanceOfType env v₁ (CedarType.bool BoolType.ff) →
  v₁ = .prim (.bool false)
```

`Cedar.Thm.instance_of_tt_is_true` (theorem, [line 214](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L214))

```lean
theorem instance_of_tt_is_true {env : TypeEnv} {v₁ : Value} :
  InstanceOfType env v₁ (CedarType.bool BoolType.tt) →
  v₁ = .prim (.bool true)
```

`Cedar.Thm.instance_of_anyBool_is_bool` (theorem, [line 225](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L225))

```lean
theorem instance_of_anyBool_is_bool {env : TypeEnv} {v₁ : Value} :
  InstanceOfType env v₁ (CedarType.bool BoolType.anyBool) →
  ∃ b, v₁ = .prim (.bool b)
```

`Cedar.Thm.instance_of_int_is_int` (theorem, [line 230](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L230))

```lean
theorem instance_of_int_is_int {env : TypeEnv} {v₁ : Value} :
  InstanceOfType env v₁ CedarType.int →
  ∃ i, v₁ = .prim (.int i)
```

`Cedar.Thm.instance_of_string_is_string` (theorem, [line 239](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L239))

```lean
theorem instance_of_string_is_string {env : TypeEnv} {v₁ : Value} :
  InstanceOfType env v₁ CedarType.string →
  ∃ s, v₁ = .prim (.string s)
```

`Cedar.Thm.instance_of_entity_type_is_entity` (theorem, [line 248](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L248))

```lean
theorem instance_of_entity_type_is_entity {env : TypeEnv} {ety : EntityType} :
  InstanceOfType env v₁ (.entity ety) →
  ∃ euid, euid.ty = ety ∧ v₁ = .prim (.entityUID euid)
```

`Cedar.Thm.instance_of_decimal_type_is_decimal` (theorem, [line 259](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L259))

```lean
theorem instance_of_decimal_type_is_decimal {env : TypeEnv} {v₁ : Value} :
  InstanceOfType env v₁ (CedarType.ext ExtType.decimal) →
  ∃ d, v₁ = .ext (.decimal d)
```

`Cedar.Thm.instance_of_ipAddr_type_is_ipAddr` (theorem, [line 271](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L271))

```lean
theorem instance_of_ipAddr_type_is_ipAddr {env : TypeEnv} {v₁ : Value} :
  InstanceOfType env v₁ (CedarType.ext ExtType.ipAddr) →
  ∃ d, v₁ = .ext (.ipaddr d)
```

`Cedar.Thm.instance_of_datetime_type_is_datetime` (theorem, [line 283](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L283))

```lean
theorem instance_of_datetime_type_is_datetime {env : TypeEnv} {v₁ : Value} :
  InstanceOfType env v₁ (CedarType.ext ExtType.datetime) →
  ∃ d, v₁ = .ext (.datetime d)
```

`Cedar.Thm.instance_of_duration_type_is_duration` (theorem, [line 295](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L295))

```lean
theorem instance_of_duration_type_is_duration {env : TypeEnv} {v₁ : Value} :
  InstanceOfType env v₁ (CedarType.ext ExtType.duration) →
  ∃ d, v₁ = .ext (.duration d)
```

`Cedar.Thm.instance_of_set_type_is_set` (theorem, [line 307](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L307))

```lean
theorem instance_of_set_type_is_set {env : TypeEnv} {v : Value} {ty : CedarType} :
  InstanceOfType env v (.set ty) →
  ∃ s, v = .set s ∧ (∀ ev ∈ s, InstanceOfType env ev ty)
```

`Cedar.Thm.instance_of_record_type_is_record` (theorem, [line 316](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L316))

```lean
theorem instance_of_record_type_is_record {env : TypeEnv} {v : Value} {rty : RecordType} :
  InstanceOfType env v (.record rty) →
  ∃ r, v = .record r
```

`Cedar.Thm.instance_of_attribute_type` (theorem, [line 325](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L325))

```lean
theorem instance_of_attribute_type {env : TypeEnv} {r : Map Attr Value} {v : Value} {rty : RecordType} {a : Attr} {aty : CedarType} {qaty : QualifiedType}
  (h₁ : InstanceOfType env (.record r) (.record rty))
  (h₂ : rty.find? a = .some qaty)
  (h₃ : qaty.getType = aty)
  (h₄ : r.find? a = .some v) :
  InstanceOfType env v aty
```

`Cedar.Thm.absent_attribute_is_absent` (theorem, [line 337](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L337))

```lean
theorem absent_attribute_is_absent {env : TypeEnv} {r : Map Attr Value} {rty : RecordType} {a : Attr}
  (h₁ : InstanceOfType env (.record r) (.record rty))
  (h₂ : rty.find? a = .none) :
  r.find? a = .none
```

`Cedar.Thm.required_attribute_is_present` (theorem, [line 349](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L349))

```lean
theorem required_attribute_is_present {env : TypeEnv} {r : Map Attr Value} {rty : RecordType} {a : Attr} {aty : CedarType}
  (h₁ : InstanceOfType env (.record r) (.record rty))
  (h₂ : rty.find? a = .some (Qualified.required aty)) :
  ∃ v, r.find? a = .some v
```

`Cedar.Thm.well_typed_entity_attributes` (theorem, [line 360](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L360))

```lean
theorem well_typed_entity_attributes
  {env : TypeEnv} {request : Request} {entities : Entities}
  {uid: EntityUID} {d: EntityData} {rty : RecordType}
  (h₁ : InstanceOfWellFormedEnvironment request entities env)
  (h₂ : Map.find? entities uid = some d)
  (h₃ : EntitySchema.attrs? env.ets uid.ty = some rty) :
  InstanceOfType env d.attrs (.record rty)
```

`Cedar.Thm.instance_of_type_bool_is_bool` (theorem, [line 387](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L387))

```lean
theorem instance_of_type_bool_is_bool {env : TypeEnv} (v : Value) (ty : CedarType) :
  InstanceOfType env v ty →
  ty ⊑ .bool .anyBool →
  ∃ b, v = .prim (.bool b)
```

`Cedar.Thm.bool_type_is_inhabited` (theorem, [line 398](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L398))

```lean
theorem bool_type_is_inhabited (bty : BoolType) :
  ∃ b, InstanceOfBoolType b bty
```

`Cedar.Thm.entity_type_is_inhabited` (theorem, [line 407](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L407))

```lean
theorem entity_type_is_inhabited {env : TypeEnv} {ety : EntityType}
  (hwf_env : env.WellFormed)
  (hwf : EntityType.WellFormed env ety) :
  ∃ euid, InstanceOfEntityType euid ety env
```

`Cedar.Thm.ext_type_is_inhabited` (theorem, [line 450](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L450))

```lean
theorem ext_type_is_inhabited (xty : ExtType) :
  ∃ x, InstanceOfExtType x xty
```

`Cedar.Thm.instance_of_record_nil` (theorem, [line 460](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L460))

```lean
theorem instance_of_record_nil {env : TypeEnv} :
  InstanceOfType env (Value.record (Map.mk [])) (CedarType.record (Map.mk []))
```

`Cedar.Thm.instance_of_record_cons` (theorem, [line 466](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L466))

```lean
theorem instance_of_record_cons {env : TypeEnv} {hd : Attr × Qualified CedarType} {tl : List (Attr × Qualified CedarType)} {rhd : Value} {rtl : List (Attr × Value)}
  (h₁ : InstanceOfType env rhd (Qualified.getType hd.snd))
  (h₂ : InstanceOfType env (Value.record (Map.mk rtl)) (CedarType.record (Map.mk tl))) :
  InstanceOfType env (Value.record (Map.mk ((hd.fst, rhd) :: rtl))) (CedarType.record (Map.mk (hd :: tl)))
```

`Cedar.Thm.sizeOf_attribute_lt_sizeOf_qualified` (theorem, [line 500](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L500))

```lean
theorem sizeOf_attribute_lt_sizeOf_qualified (aqty : Attr × Qualified CedarType) :
  sizeOf (Qualified.getType aqty.snd) < sizeOf aqty
```

`Cedar.Thm.type_is_inhabited_bool` (theorem, [line 514](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L514))

```lean
theorem type_is_inhabited_bool {env : TypeEnv} {bty : BoolType} :
  ∃ v, InstanceOfType env v (.bool bty)
```

`Cedar.Thm.type_is_inhabited_int` (theorem, [line 521](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L521))

```lean
theorem type_is_inhabited_int {env : TypeEnv} :
  ∃ v, InstanceOfType env v CedarType.int
```

`Cedar.Thm.type_is_inhabited_string` (theorem, [line 527](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L527))

```lean
theorem type_is_inhabited_string {env : TypeEnv} :
  ∃ v, InstanceOfType env v CedarType.string
```

`Cedar.Thm.type_is_inhabited_entity` (theorem, [line 533](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L533))

```lean
theorem type_is_inhabited_entity {env : TypeEnv} {ety : EntityType} :
  env.WellFormed → CedarType.WellFormed env (.entity ety) →
  ∃ v, InstanceOfType env v (.entity ety)
```

`Cedar.Thm.type_is_inhabited_set` (theorem, [line 543](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L543))

```lean
theorem type_is_inhabited_set {env : TypeEnv} {ty : CedarType} :
  ∃ v, InstanceOfType env v (.set ty)
```

`Cedar.Thm.type_is_inhabited_ext` (theorem, [line 550](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L550))

```lean
theorem type_is_inhabited_ext {env : TypeEnv} {xty : ExtType} :
  ∃ v, InstanceOfType env v (.ext xty)
```

`Cedar.Thm.type_is_inhabited_record` (theorem, [line 557](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L557))

```lean
theorem type_is_inhabited_record {env : TypeEnv} {rty : List (Attr × Qualified CedarType) }
  (hwf : (CedarType.record (Map.mk rty)).WellFormed env)
  (ih_ty : ∀ aty ∈ rty, aty.snd.getType.WellFormed env → ∃ v, InstanceOfType env v aty.snd.getType) :
  ∃ v, InstanceOfType env v (.record (Map.mk rty))
```

`Cedar.Thm.type_is_inhabited` (theorem, [line 576](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L576))

```lean
theorem type_is_inhabited {env : TypeEnv} {ty : CedarType}
  (hwf_env : env.WellFormed)
  (hwf : ty.WellFormed env) :
  ∃ v, InstanceOfType env v ty
```

`Cedar.Thm.instance_of_lubBool_left` (theorem, [line 605](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L605))

```lean
theorem instance_of_lubBool_left {env : TypeEnv} {v : Value} {bty₁ bty₂ : BoolType} :
  InstanceOfType env v (CedarType.bool bty₁) →
  InstanceOfType env v (CedarType.bool (lubBool bty₁ bty₂))
```

`Cedar.Thm.instance_of_lubBool` (theorem, [line 616](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L616))

```lean
theorem instance_of_lubBool {env : TypeEnv} {v : Value} {bty₁ bty₂ : BoolType} :
  (InstanceOfType env v (CedarType.bool bty₁) ∨ InstanceOfType env v (CedarType.bool bty₂)) →
  InstanceOfType env v (CedarType.bool (lubBool bty₁ bty₂))
```

`Cedar.Thm.sizeOf_attr_type_lt_sizeOf_record_type` (theorem, [line 625](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L625))

```lean
theorem sizeOf_attr_type_lt_sizeOf_record_type {a : Attr} {qty : QualifiedType } {rty : List (Attr × Qualified CedarType) }
  (h₁ : CedarType.record (Map.mk rty) = ty)
  (h₂ : Map.find? (Map.mk rty) a = .some qty) :
  sizeOf qty.getType < sizeOf ty
```

`Cedar.Thm.instance_of_lub_left` (theorem, [line 653](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L653))

```lean
theorem instance_of_lub_left {env : TypeEnv} {v : Value} {ty ty₁ ty₂ : CedarType}
  (h₁ : (ty₁ ⊔ ty₂) = .some ty)
  (h₂ : InstanceOfType env v ty₁) :
  InstanceOfType env v ty
```

`Cedar.Thm.instance_of_lub` (theorem, [line 708](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L708))

```lean
theorem instance_of_lub {env : TypeEnv} {v : Value} {ty ty₁ ty₂ : CedarType}
  (h₁ : (ty₁ ⊔ ty₂) = .some ty)
  (h₂ : InstanceOfType env v ty₁ ∨ InstanceOfType env v ty₂) :
  InstanceOfType env v ty
```

`Cedar.Thm.type_of_lit_inversion` (theorem, [line 722](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L722))

> …

```lean
theorem type_of_lit_inversion {p : Prim} {c₁ c₂ : Capabilities} {tx : TypedExpr} {env : TypeEnv}
  (h₁ : (typeOf (.lit p) c₁ env) = .ok (tx, c₂)) :
  ∃ ty, tx = .lit p ty
```

`Cedar.Thm.InstanceOfWellFormedEnvironment.wf_env` (theorem, [line 734](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L734))

> Obtains the fact of well-formed environment from `InstanceOfWellFormedEnvironment`.

```lean
theorem InstanceOfWellFormedEnvironment.wf_env
  {env : TypeEnv} {request : Request} {entities : Entities}
  (h : InstanceOfWellFormedEnvironment request entities env):
  env.WellFormed
```

`Cedar.Thm.InstanceOfWellFormedEnvironment.instance_of_schema_entry` (theorem, [line 742](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L742))

```lean
theorem InstanceOfWellFormedEnvironment.instance_of_schema_entry
  {env : TypeEnv} {request : Request} {entities : Entities}
  {uid : EntityUID} {data : EntityData}
  (h : InstanceOfWellFormedEnvironment request entities env)
  (hentry : entities.find? uid = some data) :
  InstanceOfSchemaEntry uid data env
```

`Cedar.Thm.InstanceOfWellFormedEnvironment.instance_of_schema` (theorem, [line 752](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L752))

```lean
theorem InstanceOfWellFormedEnvironment.instance_of_schema
  {env : TypeEnv} {request : Request} {entities : Entities}
  (h : InstanceOfWellFormedEnvironment request entities env) :
  InstanceOfSchema entities env
```

`Cedar.Thm.InstanceOfWellFormedEnvironment.wf_action_data` (theorem, [line 760](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean#L760))

```lean
theorem InstanceOfWellFormedEnvironment.wf_action_data
  {env : TypeEnv} {request : Request} {entities : Entities}
  {uid : EntityUID} {entry : ActionSchemaEntry}
  (h : InstanceOfWellFormedEnvironment request entities env)
  (hacts : Map.find? env.acts uid = some entry) :
  ∃ data,
    Map.find? entities uid = some data ∧
    data.ancestors = entry.ancestors
```

## Depends on

- [Entities](../../../spec/entities.md)
- [Request](../../../spec/request.md)
- [Typechecker/WF](wf.md)
- [Cedar/Validation/Typechecker](../../../validation/typechecker.md)

## Proof depends on

- [LUB](lub.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/Types.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Types.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.Types.json)

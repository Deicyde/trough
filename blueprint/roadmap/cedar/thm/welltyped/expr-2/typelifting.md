---
catalog: module
lean: Cedar.Thm.type_of_after_lifted_is_lifted, Cedar.Thm.type_lifting_preserves_expr, Cedar.Thm.type_lifting_preserves_evaluation_results, Cedar.Thm.Lifted, Cedar.Thm.lifted_record_is_lifted, Cedar.Thm.lifted_type_is_lifted, Cedar.Thm.lifted_type_is_super_type, Cedar.Thm.lifted_record_type_is_top, Cedar.Thm.lifted_type_is_top, Cedar.Thm.lifted_type_lub, Cedar.Thm.type_lifting_preserves_instance_of_type, Cedar.Thm.lift_bool_types_record_eq_map_on_values, Cedar.Thm.lift_bool_types_record_eq, Cedar.Thm.wf_type_iff_wf_liftBoolTypes
statement: formalized
proof: formalized
---

# TypeLifting

`Cedar.Thm.WellTyped.Expr.TypeLifting`, in [Cedar/Thm/WellTyped/Expr/TypeLifting.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean).

> This file contains theorems related to `TypedExpr.liftBoolTypes`

`Cedar.Thm.type_of_after_lifted_is_lifted` (theorem, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean#L38))

```lean
theorem type_of_after_lifted_is_lifted (x : TypedExpr) :
  x.liftBoolTypes.typeOf = x.typeOf.liftBoolTypes
```

`Cedar.Thm.type_lifting_preserves_expr` (theorem, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean#L43))

```lean
theorem type_lifting_preserves_expr (x : TypedExpr) :
  x.toExpr = x.liftBoolTypes.toExpr
```

`Cedar.Thm.type_lifting_preserves_evaluation_results` (theorem, [line 88](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean#L88))

```lean
theorem type_lifting_preserves_evaluation_results {x : TypedExpr} {request : Request} {entities : Entities} :
  evaluate x.toExpr request entities = evaluate x.liftBoolTypes.toExpr request entities
```

`Cedar.Thm.Lifted` (inductive type, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean#L93))

```lean
inductive Lifted : CedarType → CedarType → Prop
  | bool {bty : BoolType} :
    Lifted (.bool bty) (.bool .anyBool)
  | int :
    Lifted .int .int
  | string :
    Lifted .string .string
  | entity {ety : EntityType} :
    Lifted (.entity ety) (.entity ety)
  | ext {extTy : ExtType} :
    Lifted (.ext extTy) (.ext extTy)
  | set {ty₁ ty₂ : CedarType}
    (h : Lifted ty₁ ty₂) :
    Lifted (.set ty₁) (.set ty₂)
  | record_nil :
    Lifted (.record (.mk [])) (.record (.mk []))
  | record_fst_optional {ty₁ ty₂ : CedarType} {k : Attr} {m₁ m₂ : List (Attr × QualifiedType)}
    (h₁ : Lifted ty₁ ty₂)
    (h₂ : Lifted (.record (.mk m₁)) (.record (.mk m₂))) :
    Lifted (.record (.mk ((k, .optional ty₁) :: m₁))) (.record (.mk ((k, .optional ty₂) :: m₂)))
  | record_fst_required {ty₁ ty₂ : CedarType} {k : Attr} {m₁ m₂ : List (Attr × QualifiedType)}
    (h₁ : Lifted ty₁ ty₂)
    (h₂ : Lifted (.record (.mk m₁)) (.record (.mk m₂))) :
    Lifted (.record (.mk ((k, .required ty₁) :: m₁))) (.record (.mk ((k, .required ty₂) :: m₂)))
```

`Cedar.Thm.lifted_record_is_lifted` (theorem, [line 120](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean#L120))

```lean
theorem lifted_record_is_lifted (m : List (Attr × QualifiedType)) :
  Lifted (.record (.mk m)) (.record (.mk (m.map (λ (k, v) => (k, QualifiedType.liftBoolTypes v)))))
```

`Cedar.Thm.lifted_type_is_lifted` (theorem, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean#L133))

```lean
theorem lifted_type_is_lifted (ty : CedarType) :
  Lifted ty ty.liftBoolTypes
```

`Cedar.Thm.lifted_type_is_super_type` (theorem, [line 174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean#L174))

```lean
theorem lifted_type_is_super_type {ty₁ ty₂ : CedarType} :
  Lifted ty₁ ty₂ → ty₁ ⊑ ty₂
```

`Cedar.Thm.lifted_record_type_is_top` (theorem, [line 245](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean#L245))

```lean
theorem lifted_record_type_is_top {r₁ r₂ : List (Attr × Qualified CedarType)} :
  IsLubOfRecordTypes r₂ r₁ r₂ →
  r₁.map (λ (k, v) => (k, QualifiedType.liftBoolTypes v)) =
  r₂.map (λ (k, v) => (k, QualifiedType.liftBoolTypes v))
```

`Cedar.Thm.lifted_type_is_top` (theorem, [line 279](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean#L279))

```lean
theorem lifted_type_is_top {ty₁ ty₂ : CedarType} :
  ty₁ ⊑ ty₂ →
  ty₁.liftBoolTypes = ty₂.liftBoolTypes
```

`Cedar.Thm.lifted_type_lub` (theorem, [line 319](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean#L319))

```lean
theorem lifted_type_lub {ty₁ ty₂ ty : CedarType} :
  (ty₁ ⊔ ty₂) = .some ty →
  ty₁.liftBoolTypes = ty₂.liftBoolTypes
```

`Cedar.Thm.type_lifting_preserves_instance_of_type` (theorem, [line 331](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean#L331))

```lean
theorem type_lifting_preserves_instance_of_type {env : TypeEnv} {v : Value} {ty : CedarType} :
  InstanceOfType env v ty →
  InstanceOfType env v ty.liftBoolTypes
```

`Cedar.Thm.lift_bool_types_record_eq_map_on_values` (theorem, [line 345](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean#L345))

```lean
theorem lift_bool_types_record_eq_map_on_values {rty : Data.Map Attr QualifiedType} :
  RecordType.liftBoolTypes rty = rty.mapOnValues QualifiedType.liftBoolTypes
```

`Cedar.Thm.lift_bool_types_record_eq` (theorem, [line 350](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean#L350))

```lean
theorem lift_bool_types_record_eq {rty : Data.Map Attr QualifiedType} :
  CedarType.liftBoolTypes (.record rty) = .record (RecordType.liftBoolTypes rty)
```

`Cedar.Thm.wf_type_iff_wf_liftBoolTypes` (theorem, [line 355](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean#L355))

```lean
theorem wf_type_iff_wf_liftBoolTypes {env : TypeEnv} :
  ∀ {ty : CedarType},
  CedarType.WellFormed env ty ↔ CedarType.WellFormed env ty.liftBoolTypes
```

## Depends on

- [Spec/Evaluator](../../../spec/evaluator.md)
- [LUB](../../validation-2/typechecker-2/lub.md)
- [Typechecker/Types](../../validation-2/typechecker-2/types.md)

## Sources

- [Cedar/Thm/WellTyped/Expr/TypeLifting.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/TypeLifting.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.WellTyped.Expr.TypeLifting.json)

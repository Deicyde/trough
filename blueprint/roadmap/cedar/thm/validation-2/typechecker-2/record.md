---
catalog: module
lean: Cedar.Thm.AttrValueHasAttrType, Cedar.Thm.AttrExprHasAttrType, Cedar.Thm.type_of_record_inversion_forall, Cedar.Thm.type_of_record_inversion, Cedar.Thm.mk_vals_instance_of_mk_types₁, Cedar.Thm.mk_vals_instance_of_mk_types₂, Cedar.Thm.mk_vals_instance_of_mk_types₃, Cedar.Thm.mk_vals_instance_of_mk_types, Cedar.Thm.find_mk_xs_find_mk_txs, Cedar.Thm.find_make_xs_find_make_txs, Cedar.Thm.head_of_vals_instance_of_head_of_types, Cedar.Thm.vals_instance_of_types, Cedar.Thm.type_of_record_is_sound_ok, Cedar.Thm.type_of_record_is_sound_err, Cedar.Thm.type_of_record_is_sound, Cedar.Thm.type_of_ok_list
statement: formalized
proof: formalized
---

# Typechecker/Record

`Cedar.Thm.Validation.Typechecker.Record`, in [Cedar/Thm/Validation/Typechecker/Record.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean).

> This file proves that typechecking of `.record` expressions is sound.

`Cedar.Thm.AttrValueHasAttrType` (definition, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L37))

```lean
def AttrValueHasAttrType {env : TypeEnv} (av : Attr × Value) (aqty : Attr × QualifiedType) : Prop
```

`Cedar.Thm.AttrExprHasAttrType` (definition, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L40))

```lean
def AttrExprHasAttrType (c : Capabilities) (env : TypeEnv) (ax : Attr × Expr) (atx : Attr × TypedExpr) : Prop
```

`Cedar.Thm.type_of_record_inversion_forall` (theorem, [line 44](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L44))

```lean
theorem type_of_record_inversion_forall {axs : List (Attr × Expr)} {c : Capabilities} {env : TypeEnv} {rtx : List (Attr × TypedExpr)}
  (h₁ : axs.mapM (λ x => (typeOf x.snd c env).map (λ (ty, _) => (x.fst, ty))) = Except.ok rtx) :
  List.Forall₂ (AttrExprHasAttrType c env) axs rtx
```

`Cedar.Thm.type_of_record_inversion` (theorem, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L79))

```lean
theorem type_of_record_inversion {axs : List (Attr × Expr)} {c c' : Capabilities} {env : TypeEnv} {tx : TypedExpr}
  (h₁ : typeOf (Expr.record axs) c env = Except.ok (tx, c')) :
  c' = ∅ ∧
  ∃ (atxs : List (Attr × TypedExpr)),
    tx = .record atxs (.record (Map.make (atxs.map λ (a, tx) => (a, .required tx.typeOf)))) ∧
    List.Forall₂ (AttrExprHasAttrType c env) axs atxs
```

`Cedar.Thm.mk_vals_instance_of_mk_types₁` (theorem, [line 95](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L95))

```lean
theorem mk_vals_instance_of_mk_types₁ {env : TypeEnv} {a : Attr} {avs : List (Attr × Value)} {rty : List (Attr × QualifiedType)}
  (h₁ : List.Forall₂ (AttrValueHasAttrType (env := env)) avs rty)
  (h₂ : Map.contains (Map.mk avs) a = true) :
  Map.contains (Map.mk rty) a = true
```

`Cedar.Thm.mk_vals_instance_of_mk_types₂` (theorem, [line 113](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L113))

```lean
theorem mk_vals_instance_of_mk_types₂ {env : TypeEnv} {a : Attr} {v : Value} {qty : QualifiedType} {avs : List (Attr × Value)} {rtx : List (Attr × QualifiedType)}
  (h₁ : List.Forall₂ (AttrValueHasAttrType (env := env)) avs rtx)
  (h₂ : Map.find? (Map.mk avs) a = some v)
  (h₃ : (Map.mk rtx).find? a = some qty) :
  InstanceOfType env v (Qualified.getType qty)
```

`Cedar.Thm.mk_vals_instance_of_mk_types₃` (theorem, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L133))

```lean
theorem mk_vals_instance_of_mk_types₃ {env : TypeEnv} {a : Attr} {qty : QualifiedType} {avs : List (Attr × Value)} {rtx : List (Attr × QualifiedType)}
  (h₁ : List.Forall₂ (AttrValueHasAttrType (env := env)) avs rtx)
  (h₂ : (Map.mk rtx).find? a = some qty) :
  Map.contains (Map.mk avs) a = true
```

`Cedar.Thm.mk_vals_instance_of_mk_types` (theorem, [line 151](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L151))

```lean
theorem mk_vals_instance_of_mk_types {env : TypeEnv} {avs : List (Attr × Value)} {rty : List (Attr × QualifiedType)}
  (h₁ : List.Forall₂ (AttrValueHasAttrType (env := env)) avs rty) :
  InstanceOfType env (Value.record (Map.mk avs)) (CedarType.record (Map.mk rty))
```

`Cedar.Thm.find_mk_xs_find_mk_txs` (theorem, [line 166](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L166))

```lean
theorem find_mk_xs_find_mk_txs {axs : List (Attr × Expr)} {atxs : List (Attr × TypedExpr)}
  (h₁ : List.Forall₂ (AttrExprHasAttrType c env) axs atxs)
  (h₂ : (Map.mk axs).find? a = some x) :
  ∃ tx c', (Map.mk atxs).find? a = some tx ∧ typeOf x c env = .ok (tx, c')
```

`Cedar.Thm.find_make_xs_find_make_txs` (theorem, [line 188](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L188))

```lean
theorem find_make_xs_find_make_txs {axs : List (Attr × Expr)} {atxs : List (Attr × TypedExpr)}
  (h₁ : List.Forall₂ (AttrExprHasAttrType c env) axs atxs)
  (h₂ : (Map.make axs).find? a = some x) :
  ∃ tx c', (Map.make atxs).find? a = some tx ∧ typeOf x c env = .ok (tx, c')
```

`Cedar.Thm.head_of_vals_instance_of_head_of_types` (theorem, [line 203](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L203))

```lean
theorem head_of_vals_instance_of_head_of_types {xhd : Attr × Expr} {c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities} {rhd : Attr × TypedExpr} {vhd : Attr × Value}
  (h₁ : TypeOfIsSound xhd.snd)
  (h₂ : CapabilitiesInvariant c₁ request entities)
  (h₃ : InstanceOfWellFormedEnvironment request entities env)
  (h₄ : AttrExprHasAttrType c₁ env xhd rhd)
  (h₅ : bindAttr xhd.fst (evaluate xhd.snd request entities) = Except.ok vhd) :
  AttrValueHasAttrType (env := env) vhd (rhd.fst, .required rhd.snd.typeOf)
```

`Cedar.Thm.vals_instance_of_types` (theorem, [line 220](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L220))

```lean
theorem vals_instance_of_types {axs : List (Attr × Expr)} {c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities} {rtx : List (Attr × TypedExpr)} {avs : List (Attr × Value)}
  (ih : ∀ (axᵢ : Attr × Expr), axᵢ ∈ axs → TypeOfIsSound axᵢ.snd)
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : List.Forall₂ (AttrExprHasAttrType c₁ env) axs rtx)
  (h₄ : (axs.mapM fun x => bindAttr x.fst (evaluate x.snd request entities)) = Except.ok avs) :
  List.Forall₂ (AttrValueHasAttrType (env := env)) avs (rtx.map λ (a, tx) => (a, .required tx.typeOf))
```

`Cedar.Thm.type_of_record_is_sound_ok` (theorem, [line 249](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L249))

```lean
theorem type_of_record_is_sound_ok {axs : List (Attr × Expr)} {c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities} {rtx : List (Attr × TypedExpr)} {avs : List (Attr × Value)}
  (ih : ∀ (axᵢ : Attr × Expr), axᵢ ∈ axs → TypeOfIsSound axᵢ.snd)
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : List.Forall₂ (AttrExprHasAttrType c₁ env) axs rtx)
  (h₄ : (axs.mapM fun x => bindAttr x.fst (evaluate x.snd request entities)) = Except.ok avs) :
  InstanceOfType env (Value.record (Map.make avs)) (CedarType.record (Map.make (rtx.map λ (a, tx) => (a, .required tx.typeOf))))
```

`Cedar.Thm.type_of_record_is_sound_err` (theorem, [line 265](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L265))

```lean
theorem type_of_record_is_sound_err {axs : List (Attr × Expr)} {c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities} {rtx : List (Attr × TypedExpr)} {err : Error}
  (ih : ∀ (axᵢ : Attr × Expr), axᵢ ∈ axs → TypeOfIsSound axᵢ.snd)
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : List.Forall₂ (AttrExprHasAttrType c₁ env) axs rtx)
  (h₄ : (axs.mapM fun x => bindAttr x.fst (evaluate x.snd request entities)) = Except.error err) :
  err = Error.entityDoesNotExist ∨ err = Error.extensionError ∨ err = Error.arithBoundsError
```

`Cedar.Thm.type_of_record_is_sound` (theorem, [line 302](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L302))

```lean
theorem type_of_record_is_sound {axs : List (Attr × Expr)} {c₁ c₂ : Capabilities} {env : TypeEnv} {tx : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.record axs) c₁ env = Except.ok (tx, c₂))
  (ih : ∀ (axᵢ : Attr × Expr), axᵢ ∈ axs → TypeOfIsSound axᵢ.snd) :
  GuardedCapabilitiesInvariant (Expr.record axs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.record axs) request entities v ∧ InstanceOfType env v tx.typeOf
```

`Cedar.Thm.type_of_ok_list` (theorem, [line 327](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean#L327))

```lean
theorem type_of_ok_list {c₁ env xs ys request entities} :
  List.Forall₂ (fun x y => justType (typeOf x c₁ env) = Except.ok y) xs ys →
  (∀ (x₁ : Expr),
    x₁ ∈ xs →
      ∀ {c₂ : Capabilities} {ty : TypedExpr},
        typeOf x₁ c₁ env = Except.ok (ty, c₂) → evaluate x₁ request entities = evaluate ty.toExpr request entities) →
  List.Forall₂ (fun x y => evaluate x request entities = evaluate y.toExpr request entities) xs ys
```

## Depends on

- [Typechecker/Basic](basic.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/Record.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Record.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.Record.json)

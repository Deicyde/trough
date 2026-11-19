---
catalog: module
lean: Cedar.Thm.typechecked_is_well_typed_after_lifting_lit, Cedar.Thm.typechecked_is_well_typed_after_lifting_var, Cedar.Thm.typechecked_is_well_typed_after_lifting_ite, Cedar.Thm.typechecked_is_well_typed_after_lifting_and, Cedar.Thm.typechecked_is_well_typed_after_lifting_or, Cedar.Thm.typechecked_is_well_typed_after_lifting_unary_app, Cedar.Thm.typechecked_is_well_typed_after_lifting_binary_app, Cedar.Thm.typechecked_is_well_typed_after_lifting_has_attr, Cedar.Thm.typeOfExtHasAttr_tyNext_type_entity_or_record, Cedar.Thm.typechecked_is_well_typed_after_lifting_ext_has_attr, Cedar.Thm.typechecked_is_well_typed_after_lifting_get_attr_in_record, Cedar.Thm.typechecked_is_well_typed_after_lifting_get_attr, Cedar.Thm.typechecked_is_well_typed_after_lifting_call_arg, Cedar.Thm.typechecked_is_well_typed_after_lifting_call, Cedar.Thm.foldM_lub_some, Cedar.Thm.typechecked_is_well_typed_after_lifting_set, Cedar.Thm.record_lifting_make, Cedar.Thm.typechecked_is_well_typed_after_lifting_record, Cedar.Thm.typechecked_is_well_typed_after_lifting
statement: formalized
proof: formalized
---

# Expr/Typechecking

`Cedar.Thm.WellTyped.Expr.Typechecking`, in [Cedar/Thm/WellTyped/Expr/Typechecking.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean).

> This file contains expression-kind-specific lemmas of the theorem `typechecked_is_well_typed_after_lifting`

`Cedar.Thm.typechecked_is_well_typed_after_lifting_lit` (theorem, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L38))

```lean
theorem typechecked_is_well_typed_after_lifting_lit
{p : Prim}
{c₁ c₂ : Capabilities}
{env : TypeEnv}
{ty : TypedExpr} :
  typeOf (Expr.lit p) c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting_var` (theorem, [line 66](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L66))

```lean
theorem typechecked_is_well_typed_after_lifting_var
{v : Var}
{c₁ c₂ : Capabilities}
{env : TypeEnv}
{ty : TypedExpr} :
  typeOf (Expr.var v) c₁ env = Except.ok (ty, c₂) →
  TypedExpr.WellTyped env ty.liftBoolTypes
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting_ite` (theorem, [line 87](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L87))

```lean
theorem typechecked_is_well_typed_after_lifting_ite
{cond thenExpr elseExpr : Expr}
{c₁ c₂ : Capabilities}
{env : TypeEnv}
{ty : TypedExpr}
(hᵢ₁ : ∀ {c₂ : Capabilities} {ty : TypedExpr},
    typeOf cond c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes)
(hᵢ₂ : ∀ (c₁_1 : Capabilities) {c₂ : Capabilities} {ty : TypedExpr},
    typeOf thenExpr (c₁ ∪ c₁_1) env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes)
(hᵢ₃ : ∀ {c₂ : Capabilities} {ty : TypedExpr},
    typeOf elseExpr c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes)
:
  typeOf (cond.ite thenExpr elseExpr) c₁ env = Except.ok (ty, c₂) →
  TypedExpr.WellTyped env ty.liftBoolTypes
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting_and` (theorem, [line 176](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L176))

```lean
theorem typechecked_is_well_typed_after_lifting_and
{x₁ x₂ : Expr}
{c₁ c₂ : Capabilities}
{env : TypeEnv}
{ty : TypedExpr}
(hᵢ₁ : ∀ {c₂ : Capabilities} {ty : TypedExpr},
    typeOf x₁ c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes)
(hᵢ₂ : ∀ (c : Capabilities) {c₂ : Capabilities} {ty : TypedExpr},
    typeOf x₂ (c₁ ∪ c) env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes) :
  typeOf (x₁.and x₂) c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting_or` (theorem, [line 225](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L225))

```lean
theorem typechecked_is_well_typed_after_lifting_or
{x₁ x₂ : Expr}
{c₁ c₂ : Capabilities}
{env : TypeEnv}
{ty : TypedExpr}
(hᵢ₁ : ∀ {c₂ : Capabilities} {ty : TypedExpr},
    typeOf x₁ c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes)
(hᵢ₂ : ∀ {c₂ : Capabilities} {ty : TypedExpr},
    typeOf x₂ c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes) :
  typeOf (x₁.or x₂) c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting_unary_app` (theorem, [line 291](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L291))

```lean
theorem typechecked_is_well_typed_after_lifting_unary_app
{x₁: Expr}
{c₁ c₂ : Capabilities}
{env : TypeEnv}
{ty : TypedExpr}
{op₁ : UnaryOp}
(hᵢ₁ : ∀ {c₂ : Capabilities} {ty : TypedExpr},
    typeOf x₁ c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes) :
  typeOf (Expr.unaryApp op₁ x₁) c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting_binary_app` (theorem, [line 331](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L331))

```lean
theorem typechecked_is_well_typed_after_lifting_binary_app
{x₁ x₂ : Expr}
{c₁ c₂ : Capabilities}
{env : TypeEnv}
{ty : TypedExpr}
{op₂ : BinaryOp}
(hᵢ₁ : ∀ {c₂ : Capabilities} {ty : TypedExpr},
    typeOf x₁ c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes)
(hᵢ₂ : ∀ {c₂ : Capabilities} {ty : TypedExpr},
    typeOf x₂ c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes) :
  typeOf (Expr.binaryApp op₂ x₁ x₂) c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting_has_attr` (theorem, [line 653](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L653))

```lean
theorem typechecked_is_well_typed_after_lifting_has_attr
{x₁ : Expr}
{c₁ c₂ : Capabilities}
{env : TypeEnv}
{ty : TypedExpr}
{attr : Attr}
(hᵢ₁ : ∀ {c₂ : Capabilities} {ty : TypedExpr},
    typeOf x₁ c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes) :
  typeOf (x₁.hasAttr attr) c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes
```

`Cedar.Thm.typeOfExtHasAttr_tyNext_type_entity_or_record` (theorem, [line 817](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L817))

```lean
theorem typeOfExtHasAttr_tyNext_type_entity_or_record
  {tyNext : TypedExpr} {x₁ : Expr} {b : Attr} {rest : List Attr}
  {c : Capabilities} {env : TypeEnv} {res : BoolType × Capabilities}
  (hrec : typeOfExtHasAttr tyNext x₁ (b :: rest) c env = .ok res) :
  (∃ ety, tyNext.typeOf = .entity ety) ∨ (∃ rty, tyNext.typeOf = .record rty)
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting_ext_has_attr` (theorem, [line 993](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L993))

```lean
theorem typechecked_is_well_typed_after_lifting_ext_has_attr
{x₁ : Expr}
{c₁ c₂ : Capabilities}
{env : TypeEnv}
{ty : TypedExpr}
{attr : Attr}
{attrs : List Attr}
(hᵢ₁ : ∀ {c₂ : Capabilities} {ty : TypedExpr},
    typeOf x₁ c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes) :
  typeOf (x₁.extHasAttr attr attrs) c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting_get_attr_in_record` (theorem, [line 1045](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L1045))

```lean
theorem typechecked_is_well_typed_after_lifting_get_attr_in_record
{x₁ : Expr}
{c₁ c₂ : Capabilities}
{attr : Attr}
{tc : TypedExpr × Capabilities}
{rty : Data.Map Attr (Qualified CedarType)}
{a : CedarType}
(h₃ : getAttrInRecord tc.fst.typeOf rty x₁ attr c₁ = Except.ok (a, c₂)) :
  Option.map Qualified.getType ((RecordType.liftBoolTypes rty).find? attr) = some a.liftBoolTypes
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting_get_attr` (theorem, [line 1083](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L1083))

```lean
theorem typechecked_is_well_typed_after_lifting_get_attr
{x₁ : Expr}
{c₁ c₂ : Capabilities}
{env : TypeEnv}
{ty : TypedExpr}
{attr : Attr}
(hᵢ₁ : ∀ {c₂ : Capabilities} {ty : TypedExpr},
    typeOf x₁ c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes) :
  typeOf (x₁.getAttr attr) c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting_call_arg` (theorem, [line 1126](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L1126))

```lean
theorem typechecked_is_well_typed_after_lifting_call_arg
{c₁: Capabilities}
{env : TypeEnv}
{xs : List Expr}
{tys : List TypedExpr}
(hᵢ : List.Forall₂ (fun x y => justType (typeOf x c₁ env) = Except.ok y) xs tys)
(hᵢ₁ : ∀ (x₁ : Expr),
  x₁ ∈ xs →
    ∀ {c₂ : Capabilities} {ty : TypedExpr},
        typeOf x₁ c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes) :
  ∀ (x : TypedExpr), (x ∈ tys.map₁ fun x => x.val.liftBoolTypes) → TypedExpr.WellTyped env x
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting_call` (theorem, [line 1150](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L1150))

```lean
theorem typechecked_is_well_typed_after_lifting_call
{c₁ c₂ : Capabilities}
{env : TypeEnv}
{ty : TypedExpr}
{xfn : ExtFun}
{xs : List Expr}
(hᵢ₁ : ∀ (x₁ : Expr),
  x₁ ∈ xs →
    ∀ {c₂ : Capabilities} {ty : TypedExpr},
        typeOf x₁ c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes) :
  typeOf (Expr.call xfn xs) c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes
```

`Cedar.Thm.foldM_lub_some` (theorem, [line 1439](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L1439))

```lean
theorem foldM_lub_some {x y: CedarType} {xs : List CedarType} :
  List.foldlM lub? x xs = some y →
  ∀ t ∈ xs, t ⊑ y
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting_set` (theorem, [line 1460](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L1460))

```lean
theorem typechecked_is_well_typed_after_lifting_set
{c₁ c₂ : Capabilities}
{env : TypeEnv}
{ty : TypedExpr}
{xs : List Expr}
(hᵢ₁ : ∀ (x₁ : Expr),
  x₁ ∈ xs →
    ∀ {c₂ : Capabilities} {ty : TypedExpr},
        typeOf x₁ c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes) :
  typeOf (Expr.set xs) c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes
```

`Cedar.Thm.record_lifting_make` (theorem, [line 1519](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L1519))

```lean
theorem record_lifting_make {tys : List (Attr × TypedExpr)} :
  RecordType.liftBoolTypes
    (Data.Map.make (List.map (fun x => (x.fst, Qualified.required x.snd.typeOf)) tys)) =
  Data.Map.make
    (List.map (fun x => (x.fst, Qualified.required x.snd.typeOf))
      (List.map (fun x => (x.fst, x.snd.liftBoolTypes)) tys))
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting_record` (theorem, [line 1532](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L1532))

```lean
theorem typechecked_is_well_typed_after_lifting_record
{c₁ c₂ : Capabilities}
{env : TypeEnv}
{ty : TypedExpr}
{axs : List (Attr × Expr)}
(hᵢ₁ : ∀ (a₁ : Attr) (x₁ : Expr),
  sizeOf (a₁, x₁).snd < 1 + sizeOf axs →
    ∀ {c₂ : Capabilities} {ty : TypedExpr},
        typeOf x₁ c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes) :
  typeOf (Expr.record axs) c₁ env = Except.ok (ty, c₂) → TypedExpr.WellTyped env ty.liftBoolTypes
```

`Cedar.Thm.typechecked_is_well_typed_after_lifting` (theorem, [line 1571](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean#L1571))

> The type checker produces typed expressions that are well-typed after type
> lifting. …

```lean
theorem typechecked_is_well_typed_after_lifting
{e : Expr}
{c₁ c₂ : Capabilities}
{env : TypeEnv}
{ty : TypedExpr} :
  typeOf e c₁ env = .ok (ty, c₂) →
  TypedExpr.WellTyped env ty.liftBoolTypes
```

## Depends on

- [Expr/Definition](definition.md)
- [Cedar/Validation/Typechecker](../../../validation/typechecker.md)

## Proof depends on

- [TypeLifting](typelifting.md)

## Sources

- [Cedar/Thm/WellTyped/Expr/Typechecking.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/Typechecking.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.WellTyped.Expr.Typechecking.json)

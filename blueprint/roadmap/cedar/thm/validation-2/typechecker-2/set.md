---
catalog: module
lean: Cedar.Thm.type_of_set_tail, Cedar.Thm.type_of_set_inversion, Cedar.Thm.list_is_sound_implies_tail_is_sound, Cedar.Thm.list_is_typed_implies_tail_is_typed, Cedar.Thm.type_of_set_is_sound_err, Cedar.Thm.type_of_set_is_sound_ok, Cedar.Thm.type_of_set_is_sound, Cedar.Thm.type_of_ok_attr_list
statement: formalized
proof: formalized
---

# Typechecker/Set

`Cedar.Thm.Validation.Typechecker.Set`, in [Cedar/Thm/Validation/Typechecker/Set.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Set.lean).

> This file proves that typechecking of `.set` expressions is sound.

`Cedar.Thm.type_of_set_tail` (theorem, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Set.lean#L39))

```lean
theorem type_of_set_tail
  {x xhd : Expr } {xtl : List Expr} {c : Capabilities}
  {env : TypeEnv} {ty : CedarType} {hd : TypedExpr } {tl : List TypedExpr}
  (h₁ : (List.mapM₁ (xhd :: xtl) fun x => justType (typeOf x.val c env)) = Except.ok (hd :: tl))
  (h₂ : List.foldlM lub? hd.typeOf (tl.map TypedExpr.typeOf) = some ty)
  (h₃ : List.Mem x xtl) :
  ∃ ty', (typeOf (Expr.set xtl) c env) = Except.ok (.set tl (.set ty'), []) ∧
  (ty' ⊔ ty) = some ty
```

`Cedar.Thm.type_of_set_inversion` (theorem, [line 82](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Set.lean#L82))

```lean
theorem type_of_set_inversion {xs : List Expr} {c c' : Capabilities} {env : TypeEnv} {tx : TypedExpr}
  (h₁ : typeOf (Expr.set xs) c env = Except.ok (tx, c')) :
  c' = ∅ ∧
  ∃ txs ty,
    tx = (.set txs (.set ty)) ∧
    ∀ xᵢ ∈ xs,
      ∃ txᵢ cᵢ,
        txᵢ ∈ txs ∧
        typeOf xᵢ c env = Except.ok (txᵢ, cᵢ) ∧
        (txᵢ.typeOf ⊔ ty) = .some ty
```

`Cedar.Thm.list_is_sound_implies_tail_is_sound` (theorem, [line 140](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Set.lean#L140))

```lean
theorem list_is_sound_implies_tail_is_sound {hd : Expr} {tl : List Expr}
  (h₁ : ∀ (xᵢ : Expr), xᵢ ∈ hd :: tl → TypeOfIsSound xᵢ) :
  ∀ (xᵢ : Expr), xᵢ ∈ tl → TypeOfIsSound xᵢ
```

`Cedar.Thm.list_is_typed_implies_tail_is_typed` (theorem, [line 148](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Set.lean#L148))

```lean
theorem list_is_typed_implies_tail_is_typed {hd : Expr} {tl : List Expr} {c₁ : Capabilities} {env : TypeEnv} {ty : CedarType}
  (h₁ : ∀ (xᵢ : Expr), xᵢ ∈ hd :: tl → ∃ txᵢ cᵢ, (typeOf xᵢ c₁ env) = Except.ok (txᵢ, cᵢ) ∧ (txᵢ.typeOf ⊔ ty) = some ty) :
  ∀ (xᵢ : Expr), xᵢ ∈ tl → ∃ txᵢ cᵢ, typeOf xᵢ c₁ env = Except.ok (txᵢ, cᵢ) ∧ (txᵢ.typeOf ⊔ ty) = some ty
```

`Cedar.Thm.type_of_set_is_sound_err` (theorem, [line 156](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Set.lean#L156))

```lean
theorem type_of_set_is_sound_err {xs : List Expr} {c₁ : Capabilities} {env : TypeEnv} {ty : CedarType} {request : Request} {entities : Entities} {err : Error}
  (ih : ∀ (xᵢ : Expr), xᵢ ∈ xs → TypeOfIsSound xᵢ)
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₄ : ∀ (xᵢ : Expr), xᵢ ∈ xs → ∃ txᵢ cᵢ, (typeOf xᵢ c₁ env) = Except.ok (txᵢ, cᵢ) ∧ (txᵢ.typeOf ⊔ ty) = some ty)
  (h₅ : (xs.mapM fun x => evaluate x request entities) = Except.error err) :
  err = Error.entityDoesNotExist ∨
  err = Error.extensionError ∨
  err = Error.arithBoundsError
```

`Cedar.Thm.type_of_set_is_sound_ok` (theorem, [line 193](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Set.lean#L193))

```lean
theorem type_of_set_is_sound_ok { xs : List Expr } { c₁ : Capabilities } { env : TypeEnv } { request : Request } { entities : Entities } { ty : CedarType } { v : Value } { vs : List Value }
  (ih : ∀ (xᵢ : Expr), xᵢ ∈ xs → TypeOfIsSound xᵢ)
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : ∀ (xᵢ : Expr), xᵢ ∈ xs → ∃ txᵢ cᵢ, (typeOf xᵢ c₁ env) = Except.ok (txᵢ, cᵢ) ∧ (txᵢ.typeOf ⊔ ty) = some ty)
  (h₄ : (xs.mapM fun x => evaluate x request entities) = Except.ok vs)
  (h₅ : v ∈ vs):
  InstanceOfType env v ty
```

`Cedar.Thm.type_of_set_is_sound` (theorem, [line 239](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Set.lean#L239))

```lean
theorem type_of_set_is_sound {xs : List Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {sty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.set xs) c₁ env = Except.ok (sty, c₂))
  (ih : ∀ (xᵢ : Expr), xᵢ ∈ xs → TypeOfIsSound xᵢ) :
  GuardedCapabilitiesInvariant (Expr.set xs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.set xs) request entities v ∧ InstanceOfType env v sty.typeOf
```

`Cedar.Thm.type_of_ok_attr_list` (theorem, [line 267](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Set.lean#L267))

```lean
theorem type_of_ok_attr_list {c₁ env atys request entities} {axs : List (Attr × Expr)} :
  List.Forall₂ (fun x y => Except.map (fun x_1 => (x.fst, x_1.fst)) (typeOf x.snd c₁ env) = Except.ok y) axs atys →
  (∀ (a₁ : Attr) (x₁ : Expr),
    sizeOf (a₁, x₁).snd < 1 + sizeOf axs →
      ∀ {c₂ : Capabilities} {ty : TypedExpr},
        typeOf x₁ c₁ env = Except.ok (ty, c₂) → evaluate x₁ request entities = evaluate ty.toExpr request entities) →
 List.Forall₂ (fun x y => bindAttr x.fst (evaluate x.snd request entities) = bindAttr y.fst (evaluate y.snd.toExpr request entities)) axs atys
```

## Depends on

- [Typechecker/Basic](basic.md)

## Proof depends on

- [Thm/Data/LT](../../data/lt.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/Set.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Set.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.Set.json)

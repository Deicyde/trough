---
catalog: module
lean: Cedar.Thm.type_of_unary_inversion, Cedar.Thm.type_of_not_inversion, Cedar.Thm.type_of_not_is_sound, Cedar.Thm.type_of_neg_inversion, Cedar.Thm.type_of_neg_is_sound, Cedar.Thm.type_of_isEmpty_inversion, Cedar.Thm.type_of_isEmpty_is_sound, Cedar.Thm.type_of_like_inversion, Cedar.Thm.type_of_like_is_sound, Cedar.Thm.type_of_is_inversion, Cedar.Thm.type_of_is_is_sound, Cedar.Thm.type_of_unaryApp_is_sound
statement: formalized
proof: formalized
---

# Typechecker/UnaryApp

`Cedar.Thm.Validation.Typechecker.UnaryApp`, in [Cedar/Thm/Validation/Typechecker/UnaryApp.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/UnaryApp.lean).

> This file proves that typechecking of `.unaryApp` expressions is sound.

`Cedar.Thm.type_of_unary_inversion` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/UnaryApp.lean#L35))

```lean
theorem type_of_unary_inversion {op : UnaryOp} {x₁ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {tx : TypedExpr}
  (h₁ : typeOf (Expr.unaryApp op x₁) c₁ env = Except.ok (tx, c₂)) :
  c₂ = ∅ ∧
  ∃ tx₁ ty c₁',
    tx = .unaryApp op tx₁ ty ∧
    typeOf x₁ c₁ env = Except.ok (tx₁, c₁') ∧
    match op with
    | .not => ∃ bty, ty = .bool bty.not ∧ tx₁.typeOf = .bool bty
    | .neg => tx₁.typeOf = .int ∧ ty = .int
    | .isEmpty => ty = .bool .anyBool ∧ ∃ ty₀, tx₁.typeOf = .set ty₀
    | .like _ => ty = .bool .anyBool ∧ tx₁.typeOf = .string
    | .is ety₀  => ∃ ety₁, ty = .bool (if ety₀ = ety₁ then .tt else .ff) ∧ tx₁.typeOf = .entity ety₁
```

`Cedar.Thm.type_of_not_inversion` (theorem, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/UnaryApp.lean#L62))

```lean
theorem type_of_not_inversion {x₁ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.unaryApp .not x₁) c₁ env = Except.ok (ty, c₂)) :
  c₂ = ∅ ∧
  ∃ bty c₁',
    ty.typeOf = .bool bty.not ∧
    (typeOf x₁ c₁ env).typeOf = Except.ok (.bool bty, c₁')
```

`Cedar.Thm.type_of_not_is_sound` (theorem, [line 85](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/UnaryApp.lean#L85))

```lean
theorem type_of_not_is_sound {x₁ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.unaryApp .not x₁) c₁ env = Except.ok (ty, c₂))
  (ih : TypeOfIsSound x₁) :
  GuardedCapabilitiesInvariant (Expr.unaryApp .not x₁) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.unaryApp .not x₁) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_neg_inversion` (theorem, [line 124](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/UnaryApp.lean#L124))

```lean
theorem type_of_neg_inversion {x₁ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.unaryApp .neg x₁) c₁ env = Except.ok (ty, c₂)) :
  c₂ = ∅ ∧
  ty.typeOf = .int ∧
  ∃ c₁', (typeOf x₁ c₁ env).typeOf = Except.ok (.int, c₁')
```

`Cedar.Thm.type_of_neg_is_sound` (theorem, [line 141](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/UnaryApp.lean#L141))

```lean
theorem type_of_neg_is_sound {x₁ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.unaryApp .neg x₁) c₁ env = Except.ok (ty, c₂))
  (ih : TypeOfIsSound x₁) :
  GuardedCapabilitiesInvariant (Expr.unaryApp .neg x₁) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.unaryApp .neg x₁) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_isEmpty_inversion` (theorem, [line 173](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/UnaryApp.lean#L173))

```lean
theorem type_of_isEmpty_inversion {x₁ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.unaryApp .isEmpty x₁) c₁ env = Except.ok (ty, c₂)) :
  c₂ = ∅ ∧
  ty.typeOf = .bool .anyBool ∧
  ∃ c₁' ty₀, (typeOf x₁ c₁ env).typeOf = Except.ok (.set ty₀, c₁')
```

`Cedar.Thm.type_of_isEmpty_is_sound` (theorem, [line 190](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/UnaryApp.lean#L190))

```lean
theorem type_of_isEmpty_is_sound {x₁ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.unaryApp .isEmpty x₁) c₁ env = Except.ok (ty, c₂))
  (ih : TypeOfIsSound x₁) :
  GuardedCapabilitiesInvariant (Expr.unaryApp .isEmpty x₁) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.unaryApp .isEmpty x₁) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_like_inversion` (theorem, [line 216](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/UnaryApp.lean#L216))

```lean
theorem type_of_like_inversion {x₁ : Expr} {p : Pattern} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.unaryApp (.like p) x₁) c₁ env = Except.ok (ty, c₂)) :
  c₂ = ∅ ∧
  ty.typeOf = .bool .anyBool ∧
  ∃ c₁', (typeOf x₁ c₁ env).typeOf = Except.ok (.string, c₁')
```

`Cedar.Thm.type_of_like_is_sound` (theorem, [line 233](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/UnaryApp.lean#L233))

```lean
theorem type_of_like_is_sound {x₁ : Expr} {p : Pattern} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.unaryApp (.like p) x₁) c₁ env = Except.ok (ty, c₂))
  (ih : TypeOfIsSound x₁) :
  GuardedCapabilitiesInvariant (Expr.unaryApp (.like p) x₁) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.unaryApp (.like p) x₁) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_is_inversion` (theorem, [line 259](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/UnaryApp.lean#L259))

```lean
theorem type_of_is_inversion {x₁ : Expr} {ety : EntityType} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.unaryApp (.is ety) x₁) c₁ env = Except.ok (ty, c₂)) :
  c₂ = ∅ ∧
  ∃ ety' c₁',
    ty.typeOf = (.bool (if ety = ety' then .tt else .ff)) ∧
    (typeOf x₁ c₁ env).typeOf = Except.ok (.entity ety', c₁')
```

`Cedar.Thm.type_of_is_is_sound` (theorem, [line 282](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/UnaryApp.lean#L282))

```lean
theorem type_of_is_is_sound {x₁ : Expr} {ety : EntityType} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.unaryApp (.is ety) x₁) c₁ env = Except.ok (ty, c₂))
  (ih : TypeOfIsSound x₁) :
  GuardedCapabilitiesInvariant (Expr.unaryApp (.is ety) x₁) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.unaryApp (.is ety) x₁) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_unaryApp_is_sound` (theorem, [line 311](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/UnaryApp.lean#L311))

```lean
theorem type_of_unaryApp_is_sound {op₁ : UnaryOp} {x₁ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.unaryApp op₁ x₁) c₁ env = Except.ok (ty, c₂))
  (ih : TypeOfIsSound x₁) :
  GuardedCapabilitiesInvariant (Expr.unaryApp op₁ x₁) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.unaryApp op₁ x₁) request entities v ∧ InstanceOfType env v ty.typeOf
```

## Depends on

- [Typechecker/Basic](basic.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/UnaryApp.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/UnaryApp.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.UnaryApp.json)

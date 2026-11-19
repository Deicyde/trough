---
catalog: module
lean: Cedar.Thm.type_of_contains_inversion, Cedar.Thm.type_of_contains_is_sound
statement: formalized
proof: formalized
---

# Contains

`Cedar.Thm.Validation.Typechecker.BinaryApp.Contains`, in [Cedar/Thm/Validation/Typechecker/BinaryApp/Contains.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Contains.lean).

> This file proves that typechecking of `.binaryApp .contains` expressions is sound.

`Cedar.Thm.type_of_contains_inversion` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Contains.lean#L35))

```lean
theorem type_of_contains_inversion {x₁ x₂ : Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.binaryApp .contains x₁ x₂) c env = Except.ok (ty, c')) :
  c' = ∅ ∧
  ty.typeOf = .bool .anyBool ∧
  ∃ ty₁ ty₂,
    (ty₁ ⊔ ty₂).isSome ∧
    (∃ c₁, (typeOf x₁ c env).typeOf = Except.ok (.set ty₁, c₁)) ∧
    (∃ c₂, (typeOf x₂ c env).typeOf = Except.ok (ty₂, c₂))
```

`Cedar.Thm.type_of_contains_is_sound` (theorem, [line 60](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Contains.lean#L60))

```lean
theorem type_of_contains_is_sound {x₁ x₂ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.binaryApp .contains x₁ x₂) c₁ env = Except.ok (ty, c₂))
  (ih₁ : TypeOfIsSound x₁)
  (ih₂ : TypeOfIsSound x₂) :
  GuardedCapabilitiesInvariant (Expr.binaryApp .contains x₁ x₂) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.binaryApp .contains x₁ x₂) request entities v ∧ InstanceOfType env v ty.typeOf
```

## Depends on

- [Typechecker/Basic](../basic.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/BinaryApp/Contains.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Contains.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.BinaryApp.Contains.json)

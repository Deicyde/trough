---
catalog: module
lean: Cedar.Thm.type_of_getTag_inversion, Cedar.Thm.type_of_getTag_is_sound
statement: formalized
proof: formalized
---

# GetTag

`Cedar.Thm.Validation.Typechecker.BinaryApp.GetTag`, in [Cedar/Thm/Validation/Typechecker/BinaryApp/GetTag.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/GetTag.lean).

> This file proves that typechecking of `.binaryApp .getTag` expressions is sound.

`Cedar.Thm.type_of_getTag_inversion` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/GetTag.lean#L35))

```lean
theorem type_of_getTag_inversion {x₁ x₂ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {tx : TypedExpr}
  (h₁ : typeOf (Expr.binaryApp .getTag x₁ x₂) c₁ env = .ok (tx, c₂)) :
  c₂ = [] ∧
  ∃ ety ty tx₁ tx₂ c₁' c₂',
    typeOf x₁ c₁ env = .ok (tx₁, c₁') ∧
    tx₁.typeOf = .entity ety ∧
    typeOf x₂ c₁ env = .ok (tx₂, c₂') ∧
    tx₂.typeOf = .string ∧
    env.ets.tags? ety = some (some ty) ∧
    tx = .binaryApp .getTag tx₁ tx₂ ty ∧
    (x₁, .tag x₂) ∈ c₁
```

`Cedar.Thm.type_of_getTag_is_sound` (theorem, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/GetTag.lean#L70))

```lean
theorem type_of_getTag_is_sound {x₁ x₂ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {tx : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.binaryApp .getTag x₁ x₂) c₁ env = Except.ok (tx, c₂))
  (ih₁ : TypeOfIsSound x₁)
  (ih₂ : TypeOfIsSound x₂) :
  GuardedCapabilitiesInvariant (Expr.binaryApp .getTag x₁ x₂) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.binaryApp .getTag x₁ x₂) request entities v ∧ InstanceOfType env v tx.typeOf
```

## Depends on

- [Typechecker/Basic](../basic.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/BinaryApp/GetTag.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/GetTag.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.BinaryApp.GetTag.json)

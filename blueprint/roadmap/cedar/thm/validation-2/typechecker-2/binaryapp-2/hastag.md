---
catalog: module
lean: Cedar.Thm.type_of_hasTag_inversion, Cedar.Thm.type_of_hasTag_is_sound
statement: formalized
proof: formalized
---

# HasTag

`Cedar.Thm.Validation.Typechecker.BinaryApp.HasTag`, in [Cedar/Thm/Validation/Typechecker/BinaryApp/HasTag.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/HasTag.lean).

> This file proves that typechecking of `.binaryApp .hasTag` expressions is sound.

`Cedar.Thm.type_of_hasTag_inversion` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/HasTag.lean#L35))

```lean
theorem type_of_hasTag_inversion {x₁ x₂ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.binaryApp .hasTag x₁ x₂) c₁ env = .ok (ty, c₂)) :
  ∃ ety c₁' c₂',
    (typeOf x₁ c₁ env).typeOf = .ok (.entity ety, c₁') ∧
    (typeOf x₂ c₁ env).typeOf = .ok (.string, c₂') ∧
    typeOfHasTag ety x₁ x₂ c₁ env = .ok (ty.typeOf, c₂)
```

`Cedar.Thm.type_of_hasTag_is_sound` (theorem, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/HasTag.lean#L133))

```lean
theorem type_of_hasTag_is_sound {x₁ x₂ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.binaryApp .hasTag x₁ x₂) c₁ env = Except.ok (ty, c₂))
  (ih₁ : TypeOfIsSound x₁)
  (ih₂ : TypeOfIsSound x₂) :
  GuardedCapabilitiesInvariant (Expr.binaryApp .hasTag x₁ x₂) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.binaryApp .hasTag x₁ x₂) request entities v ∧ InstanceOfType env v ty.typeOf
```

## Depends on

- [Typechecker/Basic](../basic.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/BinaryApp/HasTag.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/HasTag.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.BinaryApp.HasTag.json)

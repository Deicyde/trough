---
catalog: module
lean: Cedar.Thm.type_of_and_inversion, Cedar.Thm.type_of_and_is_sound
statement: formalized
proof: formalized
---

# Typechecker/And

`Cedar.Thm.Validation.Typechecker.And`, in [Cedar/Thm/Validation/Typechecker/And.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/And.lean).

> This file proves that typechecking of `.and` expressions is sound.

`Cedar.Thm.type_of_and_inversion` (theorem, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/And.lean#L36))

```lean
theorem type_of_and_inversion {x₁ x₂ : Expr} {c c' : Capabilities} {env : TypeEnv} {tx : TypedExpr}
  (h₁ : typeOf (Expr.and x₁ x₂) c env = Except.ok (tx, c')) :
  ∃ tx₁ bty₁ c₁,
    typeOf x₁ c env = .ok (tx₁, c₁) ∧
    tx₁.typeOf = .bool bty₁ ∧
    if bty₁ = BoolType.ff
    then tx = tx₁ ∧ c' = ∅
    else ∃ bty tx₂ bty₂ c₂,
      tx = (.and tx₁ tx₂ (.bool bty)) ∧
      typeOf x₂ (c ∪ c₁) env = .ok (tx₂, c₂) ∧
      tx₂.typeOf = .bool bty₂ ∧
      if bty₂ = BoolType.ff
      then bty = BoolType.ff ∧ c' = ∅
      else bty = lubBool bty₁ bty₂ ∧ c' = c₁ ∪ c₂
```

`Cedar.Thm.type_of_and_is_sound` (theorem, [line 89](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/And.lean#L89))

```lean
theorem type_of_and_is_sound {x₁ x₂ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {tx : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.and x₁ x₂) c₁ env = Except.ok (tx, c₂))
  (ih₁ : TypeOfIsSound x₁)
  (ih₂ : TypeOfIsSound x₂) :
  GuardedCapabilitiesInvariant (Expr.and x₁ x₂) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.and x₁ x₂) request entities v ∧ InstanceOfType env v tx.typeOf
```

## Depends on

- [Typechecker/Basic](basic.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/And.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/And.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.And.json)

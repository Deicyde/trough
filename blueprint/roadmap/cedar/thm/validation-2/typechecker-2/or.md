---
catalog: module
lean: Cedar.Thm.type_of_or_inversion, Cedar.Thm.type_of_or_is_sound
statement: formalized
proof: formalized
---

# Typechecker/Or

`Cedar.Thm.Validation.Typechecker.Or`, in [Cedar/Thm/Validation/Typechecker/Or.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Or.lean).

> This file proves that typechecking of `.or` expressions is sound.

`Cedar.Thm.type_of_or_inversion` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Or.lean#L35))

```lean
theorem type_of_or_inversion {x₁ x₂ : Expr} {c c' : Capabilities} {env : TypeEnv} {tx : TypedExpr}
  (h₁ : typeOf (Expr.or x₁ x₂) c env = Except.ok (tx, c')) :
  ∃ tx₁ bty₁ c₁,
    typeOf x₁ c env = .ok (tx₁, c₁) ∧
    tx₁.typeOf = .bool bty₁ ∧
    if bty₁ = BoolType.tt
    then tx = tx₁ ∧ c' = ∅
    else ∃ bty tx₂ bty₂ c₂,
      tx = (.or tx₁ tx₂ (.bool bty)) ∧
      typeOf x₂ c env = .ok (tx₂, c₂) ∧
      tx₂.typeOf = .bool bty₂ ∧
      if bty₁ = BoolType.ff
      then bty = bty₂ ∧ c' = c₂
      else if bty₂ = BoolType.tt
      then bty = BoolType.tt ∧ c' = ∅
      else if bty₂ = BoolType.ff
      then bty = BoolType.anyBool ∧ c' = c₁
      else bty = BoolType.anyBool ∧ c' = c₁ ∩ c₂
```

`Cedar.Thm.type_of_or_is_sound` (theorem, [line 105](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Or.lean#L105))

```lean
theorem type_of_or_is_sound {x₁ x₂ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.or x₁ x₂) c₁ env = Except.ok (ty, c₂))
  (ih₁ : TypeOfIsSound x₁)
  (ih₂ : TypeOfIsSound x₂) :
  GuardedCapabilitiesInvariant (Expr.or x₁ x₂) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.or x₁ x₂) request entities v ∧ InstanceOfType env v ty.typeOf
```

## Depends on

- [Typechecker/Basic](basic.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/Or.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/Or.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.Or.json)

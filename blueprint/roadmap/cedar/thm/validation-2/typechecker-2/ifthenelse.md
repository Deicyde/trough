---
catalog: module
lean: Cedar.Thm.type_of_ite_inversion, Cedar.Thm.type_of_ite_is_sound
statement: formalized
proof: formalized
---

# Typechecker/IfThenElse

`Cedar.Thm.Validation.Typechecker.IfThenElse`, in [Cedar/Thm/Validation/Typechecker/IfThenElse.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/IfThenElse.lean).

> This file proves that typechecking of `.ite` expressions is sound.

`Cedar.Thm.type_of_ite_inversion` (theorem, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/IfThenElse.lean#L34))

```lean
theorem type_of_ite_inversion {x₁ x₂ x₃ : Expr} {c c' : Capabilities} {env : TypeEnv} {tx : TypedExpr}
  (h₁ : typeOf (Expr.ite x₁ x₂ x₃) c env = Except.ok (tx, c')) :
  ∃ tx₁ bty₁ c₁ tx₂ c₂ tx₃ c₃,
    tx = TypedExpr.ite tx₁ tx₂ tx₃ tx.typeOf ∧
    typeOf x₁ c env = .ok (tx₁, c₁) ∧
    tx₁.typeOf = .bool bty₁ ∧
    match bty₁ with
    | .ff      =>
      typeOf x₃ c env = .ok (tx₃, c₃) ∧
      tx.typeOf = tx₃.typeOf ∧ c' = c₃
    | .tt      =>
      typeOf x₂ (c ∪ c₁) env = .ok (tx₂, c₂) ∧
      tx.typeOf = tx₂.typeOf ∧ c' = c₁ ∪ c₂
    | .anyBool =>
      typeOf x₂ (c ∪ c₁) env = .ok (tx₂, c₂) ∧
      typeOf x₃ c env = .ok (tx₃, c₃) ∧
      (tx₂.typeOf ⊔ tx₃.typeOf) = (.some tx.typeOf) ∧ c' = (c₁ ∪ c₂) ∩ c₃
```

`Cedar.Thm.type_of_ite_is_sound` (theorem, [line 91](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/IfThenElse.lean#L91))

```lean
theorem type_of_ite_is_sound {x₁ x₂ x₃ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.ite x₁ x₂ x₃) c₁ env = Except.ok (ty, c₂))
  (ih₁ : TypeOfIsSound x₁)
  (ih₂ : TypeOfIsSound x₂)
  (ih₃ : TypeOfIsSound x₃) :
  GuardedCapabilitiesInvariant (Expr.ite x₁ x₂ x₃) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.ite x₁ x₂ x₃) request entities v ∧ InstanceOfType env v ty.typeOf
```

## Depends on

- [Typechecker/Basic](basic.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/IfThenElse.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/IfThenElse.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.IfThenElse.json)

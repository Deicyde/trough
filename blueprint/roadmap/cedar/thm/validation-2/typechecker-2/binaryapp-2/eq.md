---
catalog: module
lean: Cedar.Thm.type_of_eq_inversion, Cedar.Thm.no_entity_type_lub_implies_not_eq, Cedar.Thm.type_of_eq_is_sound
statement: formalized
proof: formalized
---

# Eq

`Cedar.Thm.Validation.Typechecker.BinaryApp.Eq`, in [Cedar/Thm/Validation/Typechecker/BinaryApp/Eq.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Eq.lean).

> This file proves that typechecking of `.binaryApp .eq` expressions is sound.

`Cedar.Thm.type_of_eq_inversion` (theorem, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Eq.lean#L36))

```lean
theorem type_of_eq_inversion {x₁ x₂ : Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : typeOf (Expr.binaryApp .eq x₁ x₂) c env = Except.ok (ty, c')) :
  c' = ∅ ∧
  match x₁, x₂ with
  | .lit p₁, .lit p₂ =>
    if p₁ = p₂ then ty.typeOf = (.bool .tt) else ty.typeOf = (.bool .ff)
  | _, _ =>
    ∃ ty₁ c₁ ty₂ c₂,
      typeOf x₁ c env = Except.ok (ty₁, c₁) ∧
      typeOf x₂ c env = Except.ok (ty₂, c₂) ∧
      match ty₁.typeOf ⊔ ty₂.typeOf with
      | .some _ => ty.typeOf = (.bool .anyBool)
      | .none   =>
        ty.typeOf = (.bool .ff) ∧
        ∃ ety₁ ety₂, ty₁.typeOf = .entity ety₁ ∧ ty₂.typeOf = .entity ety₂
```

`Cedar.Thm.no_entity_type_lub_implies_not_eq` (theorem, [line 100](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Eq.lean#L100))

```lean
theorem no_entity_type_lub_implies_not_eq {env : TypeEnv} {v₁ v₂ : Value} {ety₁ ety₂ : EntityType}
  (h₁ : InstanceOfType env v₁ (CedarType.entity ety₁))
  (h₂ : InstanceOfType env v₂ (CedarType.entity ety₂))
  (h₃ : (CedarType.entity ety₁ ⊔ CedarType.entity ety₂) = none) :
  ¬ v₁ = v₂
```

`Cedar.Thm.type_of_eq_is_sound` (theorem, [line 115](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Eq.lean#L115))

```lean
theorem type_of_eq_is_sound {x₁ x₂ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.binaryApp .eq x₁ x₂) c₁ env = Except.ok (ty, c₂))
  (ih₁ : TypeOfIsSound x₁)
  (ih₂ : TypeOfIsSound x₂) :
  GuardedCapabilitiesInvariant (Expr.binaryApp .eq x₁ x₂) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.binaryApp .eq x₁ x₂) request entities v ∧ InstanceOfType env v ty.typeOf
```

## Depends on

- [Typechecker/Basic](../basic.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/BinaryApp/Eq.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Eq.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.BinaryApp.Eq.json)

---
catalog: module
lean: Cedar.Thm.type_of_int_cmp_inversion, Cedar.Thm.type_of_int_cmp_is_sound
statement: formalized
proof: formalized
---

# Cmp

`Cedar.Thm.Validation.Typechecker.BinaryApp.Cmp`, in [Cedar/Thm/Validation/Typechecker/BinaryApp/Cmp.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Cmp.lean).

> This file proves that typechecking of `.binaryApp .less` and `binaryApp .lessEq` expressions is sound.

`Cedar.Thm.type_of_int_cmp_inversion` (theorem, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Cmp.lean#L36))

```lean
theorem type_of_int_cmp_inversion {op₂ : BinaryOp} {x₁ x₂ : Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : op₂ = .less ∨ op₂ = .lessEq)
  (h₂ : typeOf (Expr.binaryApp op₂ x₁ x₂) c env = Except.ok (ty, c')) :
  c' = ∅ ∧
  ty.typeOf = .bool .anyBool ∧
  (((∃ c₁, (typeOf x₁ c env).typeOf = Except.ok (.int, c₁)) ∧
   (∃ c₂, (typeOf x₂ c env).typeOf = Except.ok (.int, c₂))) ∨
  ((∃ c₁, (typeOf x₁ c env).typeOf = Except.ok (.ext .datetime, c₁)) ∧
   (∃ c₂, (typeOf x₂ c env).typeOf = Except.ok (.ext .datetime, c₂))) ∨
  ((∃ c₁, (typeOf x₁ c env).typeOf = Except.ok (.ext .duration, c₁)) ∧
   (∃ c₂, (typeOf x₂ c env).typeOf = Except.ok (.ext .duration, c₂))))
```

`Cedar.Thm.type_of_int_cmp_is_sound` (theorem, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Cmp.lean#L79))

```lean
theorem type_of_int_cmp_is_sound {op₂ : BinaryOp} {x₁ x₂ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₀ : op₂ = .less ∨ op₂ = .lessEq)
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.binaryApp op₂ x₁ x₂) c₁ env = Except.ok (ty, c₂))
  (ih₁ : TypeOfIsSound x₁)
  (ih₂ : TypeOfIsSound x₂) :
  GuardedCapabilitiesInvariant (Expr.binaryApp op₂ x₁ x₂) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.binaryApp op₂ x₁ x₂) request entities v ∧ InstanceOfType env v ty.typeOf
```

## Depends on

- [Typechecker/Basic](../basic.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/BinaryApp/Cmp.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Cmp.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.BinaryApp.Cmp.json)

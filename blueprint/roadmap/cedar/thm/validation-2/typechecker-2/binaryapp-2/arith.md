---
catalog: module
lean: Cedar.Thm.type_of_int_arith_inversion, Cedar.Thm.type_of_int_arith_is_sound
statement: formalized
proof: formalized
---

# Arith

`Cedar.Thm.Validation.Typechecker.BinaryApp.Arith`, in [Cedar/Thm/Validation/Typechecker/BinaryApp/Arith.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Arith.lean).

> This file proves that typechecking of `.binaryApp .add`, `binaryApp .sub`, and `binaryApp .mul` expressions is sound.

`Cedar.Thm.type_of_int_arith_inversion` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Arith.lean#L35))

```lean
theorem type_of_int_arith_inversion {op₂ : BinaryOp} {x₁ x₂ : Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : op₂ = .add ∨ op₂ = .sub ∨ op₂ = .mul)
  (h₂ : typeOf (Expr.binaryApp op₂ x₁ x₂) c env = Except.ok (ty, c')) :
  c' = ∅ ∧
  ty.typeOf = .int ∧
  (∃ c₁, (typeOf x₁ c env).typeOf = Except.ok (.int, c₁)) ∧
  (∃ c₂, (typeOf x₂ c env).typeOf = Except.ok (.int, c₂))
```

`Cedar.Thm.type_of_int_arith_is_sound` (theorem, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Arith.lean#L61))

```lean
theorem type_of_int_arith_is_sound {op₂ : BinaryOp} {x₁ x₂ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₀ : op₂ = .add ∨ op₂ = .sub ∨ op₂ = .mul)
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

- [Cedar/Thm/Validation/Typechecker/BinaryApp/Arith.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/Arith.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.BinaryApp.Arith.json)

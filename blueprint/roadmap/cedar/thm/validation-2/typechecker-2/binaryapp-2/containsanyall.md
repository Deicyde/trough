---
catalog: module
lean: Cedar.Thm.type_of_containsA_inversion, Cedar.Thm.type_of_containsA_is_sound
statement: formalized
proof: formalized
---

# ContainsAnyAll

`Cedar.Thm.Validation.Typechecker.BinaryApp.ContainsAnyAll`, in [Cedar/Thm/Validation/Typechecker/BinaryApp/ContainsAnyAll.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/ContainsAnyAll.lean).

> This file proves that typechecking of `.binaryApp .containsAny` and `.binaryApp .containsAll` expressions is sound.

`Cedar.Thm.type_of_containsA_inversion` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/ContainsAnyAll.lean#L35))

```lean
theorem type_of_containsA_inversion {op₂ : BinaryOp} {x₁ x₂ : Expr} {c c' : Capabilities} {env : TypeEnv} {ty : TypedExpr}
  (h₁ : op₂ = .containsAll ∨ op₂ = .containsAny)
  (h₂ : typeOf (Expr.binaryApp op₂ x₁ x₂) c env = Except.ok (ty, c')) :
  c' = ∅ ∧
  ty.typeOf = .bool .anyBool ∧
  ∃ ty₁ ty₂,
    (ty₁ ⊔ ty₂).isSome ∧
    (∃ c₁, (typeOf x₁ c env).typeOf = Except.ok (.set ty₁, c₁)) ∧
    (∃ c₂, (typeOf x₂ c env).typeOf = Except.ok (.set ty₂, c₂))
```

`Cedar.Thm.type_of_containsA_is_sound` (theorem, [line 65](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/ContainsAnyAll.lean#L65))

```lean
theorem type_of_containsA_is_sound {op₂ : BinaryOp} {x₁ x₂ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₀ : op₂ = .containsAll ∨ op₂ = .containsAny)
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

- [Cedar/Thm/Validation/Typechecker/BinaryApp/ContainsAnyAll.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp/ContainsAnyAll.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.BinaryApp.ContainsAnyAll.json)

---
catalog: module
lean: Cedar.Thm.type_of_binaryApp_inversion, Cedar.Thm.type_of_binaryApp_is_sound
statement: formalized
proof: formalized
---

# Typechecker/BinaryApp

`Cedar.Thm.Validation.Typechecker.BinaryApp`, in [Cedar/Thm/Validation/Typechecker/BinaryApp.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp.lean).

> This file proves that typechecking of `.binaryApp` expressions is sound.

`Cedar.Thm.type_of_binaryApp_inversion` (theorem, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp.lean#L43))

```lean
theorem type_of_binaryApp_inversion {op₂ : BinaryOp} {x₁ x₂ : Expr} {c c' : Capabilities} {env : TypeEnv} {tx : TypedExpr}
  (htx : typeOf (Expr.binaryApp op₂ x₁ x₂) c env = Except.ok (tx, c')) :
  ∃ tx₁ c₁ tx₂ c₂,
    typeOf x₁ c env = Except.ok (tx₁, c₁) ∧
    typeOf x₂ c env = Except.ok (tx₂, c₂) ∧
    ∃ ty, tx = .binaryApp op₂ tx₁ tx₂ ty
```

`Cedar.Thm.type_of_binaryApp_is_sound` (theorem, [line 65](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp.lean#L65))

```lean
theorem type_of_binaryApp_is_sound {op₂ : BinaryOp} {x₁ x₂ : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.binaryApp op₂ x₁ x₂) c₁ env = Except.ok (ty, c₂))
  (ih₁ : TypeOfIsSound x₁)
  (ih₂ : TypeOfIsSound x₂) :
  GuardedCapabilitiesInvariant (Expr.binaryApp op₂ x₁ x₂) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.binaryApp op₂ x₁ x₂) request entities v ∧ InstanceOfType env v ty.typeOf
```

## Depends on

- [Typechecker/Basic](basic.md)

## Proof depends on

- [Arith](binaryapp-2/arith.md)
- [Cmp](binaryapp-2/cmp.md)
- [Contains](binaryapp-2/contains.md)
- [ContainsAnyAll](binaryapp-2/containsanyall.md)
- [Eq](binaryapp-2/eq.md)
- [GetTag](binaryapp-2/gettag.md)
- [HasTag](binaryapp-2/hastag.md)
- [Mem](binaryapp-2/mem.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/BinaryApp.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/BinaryApp.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.BinaryApp.json)

---
catalog: module
lean: Cedar.Thm.type_of_lit_is_sound, Cedar.Thm.type_of_var_is_sound
statement: formalized
proof: formalized
---

# Typechecker/LitVar

`Cedar.Thm.Validation.Typechecker.LitVar`, in [Cedar/Thm/Validation/Typechecker/LitVar.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LitVar.lean).

> This file proves that typechecking of `.lit` and `.var` expressions is sound.

`Cedar.Thm.type_of_lit_is_sound` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LitVar.lean#L35))

```lean
theorem type_of_lit_is_sound {l : Prim} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₃ : (typeOf (Expr.lit l) c₁ env) = Except.ok (ty, c₂)) :
  GuardedCapabilitiesInvariant (Expr.lit l) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.lit l) request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_var_is_sound` (theorem, [line 64](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LitVar.lean#L64))

```lean
theorem type_of_var_is_sound {var : Var} {c₁ c₂ : Capabilities} {env : TypeEnv} {e' : TypedExpr} {request : Request} {entities : Entities}
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.var var) c₁ env = Except.ok (e', c₂)) :
  GuardedCapabilitiesInvariant (Expr.var var) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.var var) request entities v ∧ InstanceOfType env v e'.typeOf
```

## Depends on

- [Typechecker/Basic](basic.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/LitVar.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/LitVar.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.LitVar.json)

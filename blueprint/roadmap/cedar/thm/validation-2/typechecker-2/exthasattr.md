---
catalog: module
lean: Cedar.Thm.type_of_extHasAttr_is_sound
statement: formalized
proof: formalized
---

# Typechecker/ExtHasAttr

`Cedar.Thm.Validation.Typechecker.ExtHasAttr`, in [Cedar/Thm/Validation/Typechecker/ExtHasAttr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/ExtHasAttr.lean).

> This file proves that typechecking of `.extHasAttr` expressions is sound.

`Cedar.Thm.type_of_extHasAttr_is_sound` (theorem, [line 1102](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/ExtHasAttr.lean#L1102))

```lean
theorem type_of_extHasAttr_is_sound {x₁ : Expr} {a : Attr} {attrs : List Attr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities}
  (h₁ : CapabilitiesInvariant c₁ request entities)
  (h₂ : InstanceOfWellFormedEnvironment request entities env)
  (h₃ : typeOf (Expr.extHasAttr x₁ a attrs) c₁ env = Except.ok (ty, c₂))
  (ih : TypeOfIsSound x₁) :
  GuardedCapabilitiesInvariant (Expr.extHasAttr x₁ a attrs) c₂ request entities ∧
  ∃ v, EvaluatesTo (Expr.extHasAttr x₁ a attrs) request entities v ∧ InstanceOfType env v ty.typeOf
```

## Depends on

- [Typechecker/Basic](basic.md)

## Proof depends on

- [Typechecker/GetAttr](getattr.md)
- [Typechecker/HasAttr](hasattr.md)

## Sources

- [Cedar/Thm/Validation/Typechecker/ExtHasAttr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker/ExtHasAttr.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.ExtHasAttr.json)

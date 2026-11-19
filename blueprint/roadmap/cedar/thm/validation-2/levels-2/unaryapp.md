---
catalog: module
lean: Cedar.Thm.level_based_slicing_is_sound_unary_app
statement: formalized
proof: formalized
---

# Levels/UnaryApp

`Cedar.Thm.Validation.Levels.UnaryApp`, in [Cedar/Thm/Validation/Levels/UnaryApp.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/UnaryApp.lean).

> This file proves that level checking for `.unaryApp` expressions is sound.

`Cedar.Thm.level_based_slicing_is_sound_unary_app` (theorem, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/UnaryApp.lean#L39))

```lean
theorem level_based_slicing_is_sound_unary_app {op : UnaryOp} {e : Expr} {n : Nat} {c₀ c₁: Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf (.unaryApp op e) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ihe : TypedAtLevelIsSound e)
  : evaluate (.unaryApp op e) request entities = evaluate (.unaryApp op e) request (entities.sliceAtLevel request n)
```

## Depends on

- [Levels/Basic](basic.md)

## Proof depends on

- [Authorization/Evaluator](../../authorization-2/evaluator.md)
- [Typechecker/UnaryApp](../typechecker-2/unaryapp.md)

## Sources

- [Cedar/Thm/Validation/Levels/UnaryApp.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/UnaryApp.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Levels.UnaryApp.json)

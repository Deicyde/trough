---
catalog: module
lean: Cedar.Thm.level_based_slicing_is_sound_or
statement: formalized
proof: formalized
---

# Levels/Or

`Cedar.Thm.Validation.Levels.Or`, in [Cedar/Thm/Validation/Levels/Or.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/Or.lean).

> This file proves that level checking for `.or` expressions is sound.

`Cedar.Thm.level_based_slicing_is_sound_or` (theorem, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/Or.lean#L41))

```lean
theorem level_based_slicing_is_sound_or {e₁ e₂ : Expr} {n : Nat} {c₀ c₁: Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf (.or e₁ e₂) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ih₁ : TypedAtLevelIsSound e₁)
  (ih₂ : TypedAtLevelIsSound e₂)
  : evaluate (.or e₁ e₂) request entities = evaluate (.or e₁ e₂) request (entities.sliceAtLevel request n)
```

## Depends on

- [Levels/Basic](basic.md)

## Proof depends on

- [Thm/Validation/Typechecker](../typechecker.md)

## Sources

- [Cedar/Thm/Validation/Levels/Or.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/Or.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Levels.Or.json)

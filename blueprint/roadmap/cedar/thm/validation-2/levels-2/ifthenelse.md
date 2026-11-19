---
catalog: module
lean: Cedar.Thm.level_based_slicing_is_sound_if
statement: formalized
proof: formalized
---

# Levels/IfThenElse

`Cedar.Thm.Validation.Levels.IfThenElse`, in [Cedar/Thm/Validation/Levels/IfThenElse.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/IfThenElse.lean).

> This file proves that level checking for `.ite` expressions is sound.

`Cedar.Thm.level_based_slicing_is_sound_if` (theorem, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/IfThenElse.lean#L40))

```lean
theorem level_based_slicing_is_sound_if {x₁ x₂ x₃ : Expr} {n : Nat} {c₀ c₁: Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (htx : typeOf (.ite x₁ x₂ x₃) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ih₁ : TypedAtLevelIsSound x₁)
  (ih₂ : TypedAtLevelIsSound x₂)
  (ih₃ : TypedAtLevelIsSound x₃)
  : evaluate (.ite x₁ x₂ x₃) request entities = evaluate (.ite x₁ x₂ x₃) request (entities.sliceAtLevel request n)
```

## Depends on

- [Levels/Basic](basic.md)

## Proof depends on

- [Thm/Validation/Typechecker](../typechecker.md)

## Sources

- [Cedar/Thm/Validation/Levels/IfThenElse.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/IfThenElse.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Levels.IfThenElse.json)

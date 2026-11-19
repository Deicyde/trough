---
catalog: module
lean: Cedar.Thm.not_dereferencing_apply₂_invariant_entities, Cedar.Thm.level_based_slicing_is_sound_inₑ, Cedar.Thm.level_based_slicing_is_sound_binary_app
statement: formalized
proof: formalized
---

# Levels/BinaryApp

`Cedar.Thm.Validation.Levels.BinaryApp`, in [Cedar/Thm/Validation/Levels/BinaryApp.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/BinaryApp.lean).

> This file proves that level checking for `.binaryApp` expressions is sound.

`Cedar.Thm.not_dereferencing_apply₂_invariant_entities` (theorem, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/BinaryApp.lean#L40))

```lean
theorem not_dereferencing_apply₂_invariant_entities {op : BinaryOp} {entities entities' : Entities} {v₁ v₂ : Value}
  (hop : ¬ DereferencingBinaryOp op)
  : apply₂ op v₁ v₂ entities = apply₂ op v₁ v₂ entities'
```

`Cedar.Thm.level_based_slicing_is_sound_inₑ` (theorem, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/BinaryApp.lean#L54))

```lean
theorem level_based_slicing_is_sound_inₑ {e₁ : Expr} {euid₁ euid₂ : EntityUID} {n : Nat} {c₀ c₁ : Capabilities} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf e₁ c₀ env = Except.ok (tx₁, c₁))
  (hl : tx₁.EntityAccessAtLevel env n (n + 1) [])
  (he : evaluate e₁ request entities = .ok (Value.prim (Prim.entityUID euid₁)))
  : inₑ euid₁ euid₂ entities = inₑ euid₁ euid₂ (entities.sliceAtLevel request (n + 1))
```

`Cedar.Thm.level_based_slicing_is_sound_binary_app` (theorem, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/BinaryApp.lean#L67))

```lean
theorem level_based_slicing_is_sound_binary_app {op : BinaryOp} {e₁ e₂ : Expr} {n : Nat} {c₀ c₁: Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf (.binaryApp op e₁ e₂) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ihe₁ : TypedAtLevelIsSound e₁)
  (ihe₂ : TypedAtLevelIsSound e₂)
  : evaluate (.binaryApp op e₁ e₂) request entities = evaluate (.binaryApp op e₁ e₂) request (entities.sliceAtLevel request n)
```

## Depends on

- [Levels/Basic](basic.md)

## Proof depends on

- [Validation/Slice](../slice.md)

## Sources

- [Cedar/Thm/Validation/Levels/BinaryApp.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/BinaryApp.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Levels.BinaryApp.json)

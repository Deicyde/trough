---
catalog: module
lean: Cedar.Thm.level_based_slicing_is_sound_get_attr_entity, Cedar.Thm.level_based_slicing_is_sound_get_attr_record, Cedar.Thm.level_based_slicing_is_sound_get_attr
statement: formalized
proof: formalized
---

# Levels/GetAttr

`Cedar.Thm.Validation.Levels.GetAttr`, in [Cedar/Thm/Validation/Levels/GetAttr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/GetAttr.lean).

> This file proves that level checking for `.getAttr` expressions is sound.

`Cedar.Thm.level_based_slicing_is_sound_get_attr_entity` (theorem, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/GetAttr.lean#L42))

```lean
theorem level_based_slicing_is_sound_get_attr_entity {e : Expr} {tx₁: TypedExpr} {ty : CedarType} {a : Attr} {n : Nat} {c₀ c₁: Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hl : (tx₁.getAttr a ty).AtLevel env n)
  (ht : typeOf e c₀ env = Except.ok (tx₁, c₁))
  (hety : tx₁.typeOf = CedarType.entity ety)
  (ihe : TypedAtLevelIsSound e)
  : evaluate (.getAttr e a) request entities = evaluate (.getAttr e a) request (entities.sliceAtLevel request n)
```

`Cedar.Thm.level_based_slicing_is_sound_get_attr_record` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/GetAttr.lean#L69))

```lean
theorem level_based_slicing_is_sound_get_attr_record {e : Expr} {tx : TypedExpr} {ty : CedarType} {a : Attr} {n : Nat} {c₀: Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hl : (tx.getAttr a ty).AtLevel env n)
  (htx : typeOf e c₀ env = Except.ok (tx, c₁'))
  (hrty : tx.typeOf = CedarType.record rty)
  (ihe : TypedAtLevelIsSound e)
  : evaluate (.getAttr e a) request entities = evaluate (.getAttr e a) request (entities.sliceAtLevel request n)
```

`Cedar.Thm.level_based_slicing_is_sound_get_attr` (theorem, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/GetAttr.lean#L94))

```lean
theorem level_based_slicing_is_sound_get_attr {e : Expr} {tx : TypedExpr} {a : Attr} {n : Nat} {c₀ c₁: Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf (e.getAttr a) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ihe : TypedAtLevelIsSound e)
  : evaluate (.getAttr e a) request entities = evaluate (.getAttr e a) request (entities.sliceAtLevel request n)
```

## Depends on

- [Levels/Basic](basic.md)

## Proof depends on

- [Validation/Slice](../slice.md)

## Sources

- [Cedar/Thm/Validation/Levels/GetAttr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/GetAttr.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Levels.GetAttr.json)

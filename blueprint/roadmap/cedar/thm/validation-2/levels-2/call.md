---
catalog: module
lean: Cedar.Thm.level_based_slicing_is_sound_call
statement: formalized
proof: formalized
---

# Levels/Call

`Cedar.Thm.Validation.Levels.Call`, in [Cedar/Thm/Validation/Levels/Call.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/Call.lean).

`Cedar.Thm.level_based_slicing_is_sound_call` (theorem, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/Call.lean#L34))

```lean
theorem level_based_slicing_is_sound_call {xs : List Expr} {n : Nat} {c₀ c₁: Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf (.call xfn xs) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ih : ∀ x ∈ xs, TypedAtLevelIsSound x) :
  evaluate (.call xfn xs) request entities = evaluate (.call xfn xs) request (entities.sliceAtLevel request n)
```

## Depends on

- [Levels/Basic](basic.md)

## Proof depends on

- [Authorization/Evaluator](../../authorization-2/evaluator.md)
- [Typechecker/Call](../typechecker-2/call.md)

## Sources

- [Cedar/Thm/Validation/Levels/Call.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/Call.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Levels.Call.json)

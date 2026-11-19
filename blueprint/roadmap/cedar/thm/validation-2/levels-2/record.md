---
catalog: module
lean: Cedar.Thm.level_based_slicing_is_sound_record_attrs, Cedar.Thm.level_based_slicing_is_sound_record
statement: formalized
proof: formalized
---

# Levels/Record

`Cedar.Thm.Validation.Levels.Record`, in [Cedar/Thm/Validation/Levels/Record.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/Record.lean).

> This file proves that level checking for `.record` expressions is sound.

`Cedar.Thm.level_based_slicing_is_sound_record_attrs` (theorem, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/Record.lean#L40))

```lean
theorem level_based_slicing_is_sound_record_attrs {rxs : List (Attr × Expr)} {n : Nat} {c : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : List.Forall₂ (AttrExprHasAttrType c env) rxs atxs)
  (hl : ∀ atx ∈ atxs, atx.snd.AtLevel env n)
  (ih : ∀ x ∈ rxs, TypedAtLevelIsSound x.snd)
  :
  (rxs.mapM₂ λ x => do
    let v ← (evaluate x.1.snd request entities)
    Except.ok (x.1.fst, v)) =
  (rxs.mapM₂ λ x => do
    let v ← (evaluate x.1.snd request (entities.sliceAtLevel request n))
    Except.ok (x.1.fst, v))
```

`Cedar.Thm.level_based_slicing_is_sound_record` (theorem, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/Record.lean#L71))

```lean
theorem level_based_slicing_is_sound_record {rxs : List (Attr × Expr)} {n : Nat} {c₀ c₁: Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf (.record rxs) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ih : ∀ x ∈ rxs, TypedAtLevelIsSound x.snd) :
  evaluate (.record rxs) request entities = evaluate (.record rxs) request (entities.sliceAtLevel request n)
```

## Depends on

- [Levels/Basic](basic.md)
- [Typechecker/Record](../typechecker-2/record.md)

## Proof depends on

- [Authorization/Evaluator](../../authorization-2/evaluator.md)

## Sources

- [Cedar/Thm/Validation/Levels/Record.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/Record.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Levels.Record.json)

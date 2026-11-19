---
catalog: module
lean: Cedar.Thm.Value.sliceEUIDs_wf, Cedar.Thm.EntityData.sliceEUIDs_wf, Cedar.Thm.Request.sliceEUIDs_wf, Cedar.Thm.slice_at_level_inner_well_formed, Cedar.Thm.slice_at_level_request_well_formed, Cedar.Thm.checked_eval_entity_in_slice, Cedar.Thm.not_entities_then_not_slice, Cedar.Thm.checked_eval_entity_find_entities_eq_find_slice
statement: formalized
proof: formalized
---

# Validation/Slice

`Cedar.Thm.Validation.Slice`, in [Cedar/Thm/Validation/Slice.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice.lean).

`Cedar.Thm.Value.sliceEUIDs_wf` (theorem, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice.lean#L39))

```lean
theorem Value.sliceEUIDs_wf (v : Value) :
  v.sliceEUIDs.WellFormed
```

`Cedar.Thm.EntityData.sliceEUIDs_wf` (theorem, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice.lean#L56))

```lean
theorem EntityData.sliceEUIDs_wf (ed : EntityData) :
  ed.sliceEUIDs.WellFormed
```

`Cedar.Thm.Request.sliceEUIDs_wf` (theorem, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice.lean#L62))

```lean
theorem Request.sliceEUIDs_wf (r : Request) :
  r.sliceEUIDs.WellFormed
```

`Cedar.Thm.slice_at_level_inner_well_formed` (theorem, [line 66](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice.lean#L66))

```lean
theorem slice_at_level_inner_well_formed {entities : Entities} {work : Set EntityUID} {n : Nat} :
  work.WellFormed →
  (Entities.sliceAtLevel.sliceAtLevel entities work n).WellFormed
```

`Cedar.Thm.slice_at_level_request_well_formed` (theorem, [line 77](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice.lean#L77))

```lean
theorem slice_at_level_request_well_formed {entities : Entities} {request : Request} {n : Nat} :
  (Entities.sliceAtLevel.sliceAtLevel entities request.sliceEUIDs n).WellFormed
```

`Cedar.Thm.checked_eval_entity_in_slice` (theorem, [line 81](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice.lean#L81))

```lean
theorem checked_eval_entity_in_slice  {n : Nat} {c c' : Capabilities} {tx : TypedExpr} {env : TypeEnv} {entities : Entities} {ed : EntityData}
  (hc : CapabilitiesInvariant c request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf e c env = .ok (tx, c'))
  (hl : tx.EntityAccessAtLevel env n nmax [])
  (he : evaluate e request entities = .ok (Value.prim (Prim.entityUID euid)))
  (hf : entities.find? euid = some ed) :
  (Entities.sliceAtLevel entities request (n + 1)).find? euid = some ed
```

`Cedar.Thm.not_entities_then_not_slice` (theorem, [line 104](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice.lean#L104))

```lean
theorem not_entities_then_not_slice {n: Nat} {request : Request} {uid : EntityUID} {entities : Entities}
  (hse : entities.find? uid = none) :
  (Entities.sliceAtLevel entities request n).find? uid = none
```

`Cedar.Thm.checked_eval_entity_find_entities_eq_find_slice` (theorem, [line 115](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice.lean#L115))

> If an expression checks at level `n` and then evaluates to an entity, then the
> data for that entity in the slice will be the same as in the original entities.

```lean
theorem checked_eval_entity_find_entities_eq_find_slice  {n nmax : Nat} {c c' : Capabilities} {tx : TypedExpr} {env : TypeEnv} {entities : Entities}
  (hc : CapabilitiesInvariant c request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf e c env = .ok (tx, c'))
  (hl : tx.EntityAccessAtLevel env n nmax [])
  (he : evaluate e request entities = .ok (Value.prim (Prim.entityUID euid))) :
  (Entities.sliceAtLevel entities request (n + 1)).find? euid = entities.find? euid
```

## Depends on

- [Spec/Slice](../../spec/slice.md)
- [CheckLevel](levels-2/checklevel.md)
- [Typechecker/Basic](typechecker-2/basic.md)

## Proof depends on

- [Reachable](slice-2/reachable.md)

## Sources

- [Cedar/Thm/Validation/Slice.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Validation.Slice.json)

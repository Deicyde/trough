---
catalog: module
lean: Cedar.Thm.typed_record_contains_typed_attrs, Cedar.Thm.record_entity_access_implies_attr_entity_access, Cedar.Thm.checked_eval_entity_reachable_record
statement: formalized
proof: formalized
---

# Reachable/Record

`Cedar.Thm.Validation.Slice.Reachable.Record`, in [Cedar/Thm/Validation/Slice/Reachable/Record.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Record.lean).

`Cedar.Thm.typed_record_contains_typed_attrs` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Record.lean#L35))

```lean
theorem typed_record_contains_typed_attrs {rxs : List (Attr × Expr)} {a : Attr} {x : Expr} {c c' : Capabilities} {env : TypeEnv}
  (ht : typeOf (Expr.record rxs) c env = Except.ok (tx, c'))
  (hx : (Map.make rxs).find? a = some x) :
  ∃ rtxs ty atx,
    tx = .record rtxs ty ∧
    (Map.make rtxs).find? a = some atx ∧
    ∃ c', typeOf x c env = .ok (atx, c')
```

`Cedar.Thm.record_entity_access_implies_attr_entity_access` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Record.lean#L47))

```lean
theorem record_entity_access_implies_attr_entity_access {atx : TypedExpr} {rtxs : List (Attr × TypedExpr)} {ty : CedarType} {n nmax : Nat} {a : Attr} {path : List Attr}
  (hl : (TypedExpr.record rtxs ty).EntityAccessAtLevel env n nmax (a :: path))
  (hatx : (Map.make rtxs).find? a = some atx) :
  atx.EntityAccessAtLevel env n nmax path
```

`Cedar.Thm.checked_eval_entity_reachable_record` (theorem, [line 58](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Record.lean#L58))

```lean
theorem checked_eval_entity_reachable_record {rxs : List (Attr × Expr)} {n : Nat} {c c' : Capabilities} {tx : TypedExpr} {env : TypeEnv} {entities : Entities} {path : List Attr}
  (hc : CapabilitiesInvariant c request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf (.record rxs) c env = .ok (tx, c'))
  (hl : tx.EntityAccessAtLevel env n nmax path)
  (he : evaluate (.record rxs) request entities = .ok v)
  (ha : Value.EuidViaPath v path euid)
  (ih : ∀ a x, (Map.make rxs).find? a = some x → CheckedEvalEntityReachable x) :
  ReachableIn entities request.sliceEUIDs euid (n + 1)
```

## Depends on

- [Reachable/Basic](basic.md)

## Proof depends on

- [Authorization/Evaluator](../../../authorization-2/evaluator.md)
- [Typechecker/Record](../../typechecker-2/record.md)

## Sources

- [Cedar/Thm/Validation/Slice/Reachable/Record.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Record.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.Validation.Slice.Reachable.Record.json)

---
catalog: module
lean: Cedar.Thm.var_entity_reachable
statement: formalized
proof: formalized
---

# Reachable/Var

`Cedar.Thm.Validation.Slice.Reachable.Var`, in [Cedar/Thm/Validation/Slice/Reachable/Var.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Var.lean).

`Cedar.Thm.var_entity_reachable` (theorem, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Var.lean#L37))

```lean
theorem var_entity_reachable {var : Var} {v : Value} {n : Nat} {request : Request} {entities : Entities} {euid : EntityUID} {path : List Attr}
  (he : evaluate (.var var) request entities = .ok v)
  (ha : Value.EuidViaPath v path euid) :
  ReachableIn entities request.sliceEUIDs euid (n + 1)
```

## Depends on

- [Reachable/Basic](basic.md)

## Proof depends on

- [Authorization/Evaluator](../../../authorization-2/evaluator.md)

## Sources

- [Cedar/Thm/Validation/Slice/Reachable/Var.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Var.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.Validation.Slice.Reachable.Var.json)

---
catalog: module
lean: Cedar.Thm.reachable_attr_step, Cedar.Thm.checked_eval_entity_reachable_get_attr
statement: formalized
proof: formalized
---

# Reachable/GetAttr

`Cedar.Thm.Validation.Slice.Reachable.GetAttr`, in [Cedar/Thm/Validation/Slice/Reachable/GetAttr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/GetAttr.lean).

`Cedar.Thm.reachable_attr_step` (theorem, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/GetAttr.lean#L37))

```lean
theorem reachable_attr_step {n : Nat} {euid euid' : EntityUID} {start : Set EntityUID} {entities : Entities} {ed : EntityData} {path : List Attr}
  (hr : ReachableIn entities start euid n)
  (he₁: entities.find? euid = some ed)
  (he₂ : Value.EuidViaPath (.record ed.attrs) path euid' ) :
  ReachableIn entities start euid' (n + 1)
```

`Cedar.Thm.checked_eval_entity_reachable_get_attr` (theorem, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/GetAttr.lean#L61))

```lean
theorem checked_eval_entity_reachable_get_attr {e : Expr} {n : Nat} {c c' : Capabilities} {tx : TypedExpr} {env : TypeEnv} {entities : Entities} {path : List Attr}
  (hc : CapabilitiesInvariant c request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf (e.getAttr a) c env = .ok (tx, c'))
  (hl : tx.EntityAccessAtLevel env n nmax path)
  (he : evaluate (e.getAttr a) request entities = .ok v)
  (ha : Value.EuidViaPath v path euid)
  (ih : CheckedEvalEntityReachable e) :
  ReachableIn entities request.sliceEUIDs euid (n + 1)
```

## Depends on

- [Reachable/Basic](basic.md)

## Proof depends on

- [Thm/Validation/Typechecker](../../typechecker.md)

## Sources

- [Cedar/Thm/Validation/Slice/Reachable/GetAttr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/GetAttr.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.Validation.Slice.Reachable.GetAttr.json)

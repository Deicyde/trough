---
catalog: module
lean: Cedar.Thm.checked_eval_entity_reachable_ite
statement: formalized
proof: formalized
---

# Reachable/IfThenElse

`Cedar.Thm.Validation.Slice.Reachable.IfThenElse`, in [Cedar/Thm/Validation/Slice/Reachable/IfThenElse.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/IfThenElse.lean).

`Cedar.Thm.checked_eval_entity_reachable_ite` (theorem, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/IfThenElse.lean#L37))

```lean
theorem checked_eval_entity_reachable_ite {e₁ e₂ e₃: Expr} {n : Nat} {c c' : Capabilities} {tx : TypedExpr} {env : TypeEnv} {entities : Entities} {path : List Attr}
  (hc : CapabilitiesInvariant c request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf (.ite e₁ e₂ e₃) c env = .ok (tx, c'))
  (hl : tx.EntityAccessAtLevel env n nmax path)
  (he : evaluate (.ite e₁ e₂ e₃) request entities = .ok v)
  (ha : Value.EuidViaPath v path euid)
  (ih₂ : CheckedEvalEntityReachable e₂)
  (ih₃ : CheckedEvalEntityReachable e₃) :
  ReachableIn entities request.sliceEUIDs euid (n + 1)
```

## Depends on

- [Reachable/Basic](basic.md)

## Proof depends on

- [Thm/Validation/Typechecker](../../typechecker.md)

## Sources

- [Cedar/Thm/Validation/Slice/Reachable/IfThenElse.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/IfThenElse.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.Validation.Slice.Reachable.IfThenElse.json)

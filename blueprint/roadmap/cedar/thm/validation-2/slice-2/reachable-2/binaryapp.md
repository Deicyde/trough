---
catalog: module
lean: Cedar.Thm.reachable_tag_step, Cedar.Thm.checked_eval_entity_reachable_get_tag, Cedar.Thm.binary_op_not_euid_via_path, Cedar.Thm.checked_eval_entity_reachable_binary
statement: formalized
proof: formalized
---

# Reachable/BinaryApp

`Cedar.Thm.Validation.Slice.Reachable.BinaryApp`, in [Cedar/Thm/Validation/Slice/Reachable/BinaryApp.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/BinaryApp.lean).

`Cedar.Thm.reachable_tag_step` (theorem, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/BinaryApp.lean#L38))

```lean
theorem reachable_tag_step {n : Nat} {euid euid' : EntityUID} {start : Set EntityUID} {entities : Entities} {ed : EntityData} {tag : Tag} {path : List Attr}
  (hr : ReachableIn entities start euid n)
  (he₁ : entities.find? euid = some ed)
  (he₂ : ed.tags.find? tag = some tv)
  (he₃ : Value.EuidViaPath tv path euid') :
  ReachableIn entities start euid' (n + 1)
```

`Cedar.Thm.checked_eval_entity_reachable_get_tag` (theorem, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/BinaryApp.lean#L61))

```lean
theorem checked_eval_entity_reachable_get_tag {e₁ e₂: Expr} {n : Nat} {c c' : Capabilities} {tx : TypedExpr} {env : TypeEnv} {entities : Entities} {path : List Attr}
  (hc : CapabilitiesInvariant c request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf (.binaryApp .getTag e₁ e₂) c env = .ok (tx, c'))
  (hl : tx.EntityAccessAtLevel env n nmax path)
  (he : evaluate (.binaryApp .getTag e₁ e₂) request entities = .ok v)
  (ha : Value.EuidViaPath v path euid)
  (ih₁ : CheckedEvalEntityReachable e₁) :
  ReachableIn entities request.sliceEUIDs euid (n + 1)
```

`Cedar.Thm.binary_op_not_euid_via_path` (theorem, [line 95](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/BinaryApp.lean#L95))

```lean
theorem binary_op_not_euid_via_path {op : BinaryOp} {e₁ e₂: Expr} {entities : Entities} {path : List Attr}
  (hop : op ≠ .getTag)
  (he : evaluate (.binaryApp op e₁ e₂) request entities = .ok v) :
  ¬Value.EuidViaPath v path euid
```

`Cedar.Thm.checked_eval_entity_reachable_binary` (theorem, [line 117](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/BinaryApp.lean#L117))

```lean
theorem checked_eval_entity_reachable_binary {op : BinaryOp} {e₁ e₂: Expr} {n : Nat} {c c' : Capabilities} {tx : TypedExpr} {env : TypeEnv} {entities : Entities} {path : List Attr}
  (hc : CapabilitiesInvariant c request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf (.binaryApp op e₁ e₂) c env = .ok (tx, c'))
  (hl : tx.EntityAccessAtLevel env n nmax path)
  (he : evaluate (.binaryApp op e₁ e₂) request entities = .ok v)
  (ha : Value.EuidViaPath v path euid)
  (ih₁ : CheckedEvalEntityReachable e₁) :
  ReachableIn entities request.sliceEUIDs euid (n + 1)
```

## Depends on

- [Reachable/Basic](basic.md)

## Proof depends on

- [Authorization/Evaluator](../../../authorization-2/evaluator.md)
- [Eq](../../typechecker-2/binaryapp-2/eq.md)
- [GetTag](../../typechecker-2/binaryapp-2/gettag.md)

## Sources

- [Cedar/Thm/Validation/Slice/Reachable/BinaryApp.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/BinaryApp.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.Validation.Slice.Reachable.BinaryApp.json)

---
catalog: module
lean: Cedar.Thm.checked_eval_entity_lit_is_action, Cedar.Thm.and_not_euid_via_path, Cedar.Thm.or_not_euid_via_path, Cedar.Thm.unary_not_euid_via_path, Cedar.Thm.has_attr_not_euid_via_path, Cedar.Thm.set_not_euid_via_path, Cedar.Thm.call_not_euid_via_path, Cedar.Thm.checked_eval_entity_reachable, Cedar.Thm.in_work_then_in_slice, Cedar.Thm.slice_contains_reachable, Cedar.Thm.reachable_of_mem_slice, Cedar.Thm.reachable_then_mem_slice
statement: formalized
proof: formalized
---

# Reachable

`Cedar.Thm.Validation.Slice.Reachable`, in [Cedar/Thm/Validation/Slice/Reachable.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable.lean).

`Cedar.Thm.checked_eval_entity_lit_is_action` (theorem, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable.lean#L45))

```lean
theorem checked_eval_entity_lit_is_action {p : Prim} {n nmax : Nat} {c c' : Capabilities} {tx : TypedExpr} {env : TypeEnv} {entities : Entities} {path : List Attr}
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf (.lit p) c env = .ok (tx, c'))
  (he : evaluate (.lit p) request entities = .ok v)
  (hel : tx.EntityAccessAtLevel env n nmax path)
  (ha : Value.EuidViaPath v path euid) :
  request.action = euid
```

`Cedar.Thm.and_not_euid_via_path` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable.lean#L69))

```lean
theorem and_not_euid_via_path {e₁ e₂: Expr} {entities : Entities} {path : List Attr}
  (he : evaluate (.and e₁ e₂) request entities = .ok v) :
  ¬ Value.EuidViaPath v path euid
```

`Cedar.Thm.or_not_euid_via_path` (theorem, [line 83](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable.lean#L83))

```lean
theorem or_not_euid_via_path {e₁ e₂: Expr} {entities : Entities} {path : List Attr}
  (he : evaluate (.or e₁ e₂) request entities = .ok v) :
  ¬ Value.EuidViaPath v path euid
```

`Cedar.Thm.unary_not_euid_via_path` (theorem, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable.lean#L98))

```lean
theorem unary_not_euid_via_path {op : UnaryOp} {e₁ : Expr} {entities : Entities} {path : List Attr}
  (he : evaluate (.unaryApp op e₁) request entities = .ok v) :
  ¬ Value.EuidViaPath v path euid
```

`Cedar.Thm.has_attr_not_euid_via_path` (theorem, [line 113](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable.lean#L113))

```lean
theorem has_attr_not_euid_via_path {e₁ : Expr} {a : Attr} {entities : Entities} {path : List Attr}
  (he : evaluate (.hasAttr e₁ a) request entities = .ok v) :
  ¬ Value.EuidViaPath v path euid
```

`Cedar.Thm.set_not_euid_via_path` (theorem, [line 126](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable.lean#L126))

```lean
theorem set_not_euid_via_path {xs : List Expr} {entities : Entities} {path : List Attr}
  (he : evaluate (.set xs) request entities = .ok v) :
  ¬ Value.EuidViaPath v path euid
```

`Cedar.Thm.call_not_euid_via_path` (theorem, [line 136](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable.lean#L136))

```lean
theorem call_not_euid_via_path {xfn : ExtFun} {xs : List Expr} {entities : Entities} {path : List Attr}
  (he : evaluate (.call xfn xs) request entities = .ok v) :
  ¬ Value.EuidViaPath v path euid
```

`Cedar.Thm.checked_eval_entity_reachable` (theorem, [line 157](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable.lean#L157))

> If an expression checks at level `n` and then evaluates an entity (or a record
> containing an entity), then that entity must reachable in `n + 1` steps.

```lean
theorem checked_eval_entity_reachable {e : Expr} {n nmax: Nat} {c c' : Capabilities} {tx : TypedExpr} {env : TypeEnv} {request : Request} {entities : Entities} {v : Value} {path : List Attr} {euid : EntityUID}
  (hc : CapabilitiesInvariant c request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf e c env = .ok (tx, c'))
  (hl : tx.EntityAccessAtLevel env n nmax path)
  (he : evaluate e request entities = .ok v)
  (ha : Value.EuidViaPath v path euid) :
  ReachableIn entities request.sliceEUIDs euid (n + 1)
```

`Cedar.Thm.in_work_then_in_slice` (theorem, [line 259](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable.lean#L259))

```lean
theorem in_work_then_in_slice {entities : Entities} {work : Set EntityUID} {euid : EntityUID} {n : Nat}
  (hw : euid ∈ work)
  : euid ∈ Entities.sliceAtLevel.sliceAtLevel entities work (n + 1)
```

`Cedar.Thm.slice_contains_reachable` (theorem, [line 274](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable.lean#L274))

> If an entity is reachable in `n` steps, then it must be included in slice at
> `n`. This lemma talks about the inner slicing function, so it's possible that
> the entity isn't in the original entities if it's in `work`.

```lean
theorem slice_contains_reachable {n: Nat} {work : Set EntityUID} {euid : EntityUID} {entities : Entities}
  (hw : ReachableIn entities work euid (n + 1)) :
  euid ∈ Entities.sliceAtLevel.sliceAtLevel entities work (n + 1)
```

`Cedar.Thm.reachable_of_mem_slice` (theorem, [line 301](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable.lean#L301))

> Converse of `slice_contains_reachable`: every entity in the level-`n` slice (the
> reachable set computed by `Entities.sliceAtLevel`) is reachable in `n` steps.
> Together with `reachable_then_mem_slice` this gives `euid ∈ slice ↔ ReachableIn`,
> the bridge that makes `Entities.closedAtLevel` decide `EntitiesClosedAtLevel`.

```lean
theorem reachable_of_mem_slice {n : Nat} {work : Set EntityUID} {euid : EntityUID} {entities : Entities}
  (h : euid ∈ Entities.sliceAtLevel.sliceAtLevel entities work n) :
  ReachableIn entities work euid n
```

`Cedar.Thm.reachable_then_mem_slice` (theorem, [line 325](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable.lean#L325))

> `ReachableIn` at any level implies membership in the level-`n` slice.  Wraps
> `slice_contains_reachable` (the `n + 1` case); `n = 0` is vacuous since
> `ReachableIn _ _ _ 0` is uninhabited.

```lean
theorem reachable_then_mem_slice {n : Nat} {work : Set EntityUID} {euid : EntityUID} {entities : Entities}
  (hr : ReachableIn entities work euid n) :
  euid ∈ Entities.sliceAtLevel.sliceAtLevel entities work n
```

## Depends on

- [Reachable/Basic](reachable-2/basic.md)

## Proof depends on

- [Reachable/BinaryApp](reachable-2/binaryapp.md)
- [Reachable/GetAttr](reachable-2/getattr.md)
- [Reachable/IfThenElse](reachable-2/ifthenelse.md)
- [Reachable/Record](reachable-2/record.md)
- [Reachable/Var](reachable-2/var.md)
- [Thm/Validation/Validator](../validator.md)

## Sources

- [Cedar/Thm/Validation/Slice/Reachable.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Slice.Reachable.json)

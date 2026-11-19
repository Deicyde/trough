---
catalog: module
lean: Cedar.Thm.wellTypedPolicies_empty, Cedar.Thm.wellTypedPolicies_allowAll, Cedar.Thm.isAuthorized_empty, Cedar.Thm.isAuthorized_allowAll, Cedar.Thm.footprint_allowAll
statement: formalized
proof: formalized
---

# AllowDeny

`Cedar.Thm.SymCC.Opt.AllowDeny`, in [Cedar/Thm/SymCC/Opt/AllowDeny.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/AllowDeny.lean).

> Proofs about various functions applied to `allowAll` and `denyAll` policies, and empty policy sets.

`Cedar.Thm.wellTypedPolicies_empty` (theorem, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/AllowDeny.lean#L31))

> `wellTypedPolicies` on the empty policy set

```lean
theorem wellTypedPolicies_empty (Γ : Validation.TypeEnv) :
  wellTypedPolicies [] Γ = .ok []
```

`Cedar.Thm.wellTypedPolicies_allowAll` (theorem, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/AllowDeny.lean#L39))

> `wellTypedPolicies` on `Policy.allowAll`

```lean
theorem wellTypedPolicies_allowAll (Γ : Validation.TypeEnv) :
  wellTypedPolicies [Policy.allowAll] Γ = .ok [verifyAlwaysAllows.allowAll]
```

`Cedar.Thm.isAuthorized_empty` (theorem, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/AllowDeny.lean#L50))

> `SymCC.isAuthorized` on the empty policy set

```lean
theorem isAuthorized_empty (εnv : SymEnv) :
  SymCC.isAuthorized [] εnv = .ok (.bool false)
```

`Cedar.Thm.isAuthorized_allowAll` (theorem, [line 77](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/AllowDeny.lean#L77))

> `SymCC.isAuthorized` on `verifyAlwaysAllows.allowAll`

```lean
theorem isAuthorized_allowAll (εnv : SymEnv) :
  SymCC.isAuthorized [verifyAlwaysAllows.allowAll] εnv = .ok (.bool true)
```

`Cedar.Thm.footprint_allowAll` (theorem, [line 86](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/AllowDeny.lean#L86))

> `SymCC.footprint` on `verifyAlwaysAllows.allowAll.toExpr`

```lean
theorem footprint_allowAll (εnv : SymEnv) :
  SymCC.footprint verifyAlwaysAllows.allowAll.toExpr εnv = Data.Set.empty
```

## Depends on

- [SymCC](../../../symcc-2.md)

## Proof depends on

- [Basic properties of partial evaluation of terms](../term/pe.md)

## Sources

- [Cedar/Thm/SymCC/Opt/AllowDeny.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/AllowDeny.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Opt.AllowDeny.json)

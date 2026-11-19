---
catalog: module
lean: Cedar.Thm.well_typed_implies_wf_type, Cedar.Thm.typechecked_has_well_formed_type
statement: formalized
proof: formalized
---

# Expr/WF

`Cedar.Thm.WellTyped.Expr.WF`, in [Cedar/Thm/WellTyped/Expr/WF.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/WF.lean).

> This file contains the theorems that `TypedExpr.WellTyped` implies `CedarType.WellFormed`.

`Cedar.Thm.well_typed_implies_wf_type` (theorem, [line 40](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/WF.lean#L40))

> `TypedExpr.WellTyped` implies well-formedness of the type (`CedarType.WellFormed`).

```lean
theorem well_typed_implies_wf_type
  {env : TypeEnv} {tx : TypedExpr}
  (hwf_env : env.WellFormed)
  (hwt : TypedExpr.WellTyped env tx) :
  CedarType.WellFormed env tx.typeOf
```

`Cedar.Thm.typechecked_has_well_formed_type` (theorem, [line 172](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/WF.lean#L172))

> The result of `typeOf` has a well-formed type.

```lean
theorem typechecked_has_well_formed_type
  {e : Expr}
  {c₁ c₂ : Capabilities}
  {env : TypeEnv}
  {tx : TypedExpr}
  (hwf : env.WellFormed)
  (hty : typeOf e c₁ env = .ok (tx, c₂)) :
  tx.typeOf.WellFormed env
```

## Depends on

- [Typechecker/WF](../../validation-2/typechecker-2/wf.md)
- [Expr/Definition](definition.md)
- [Cedar/Validation/Typechecker](../../../validation/typechecker.md)

## Proof depends on

- [Expr/Typechecking](typechecking.md)

## Sources

- [Cedar/Thm/WellTyped/Expr/WF.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr/WF.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.WellTyped.Expr.WF.json)

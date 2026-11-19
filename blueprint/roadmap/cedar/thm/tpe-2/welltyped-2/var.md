---
catalog: module
lean: Cedar.Thm.partial_eval_well_typed_var
statement: formalized
proof: formalized
---

# WellTyped/Var

`Cedar.Thm.TPE.WellTyped.Var`, in [Cedar/Thm/TPE/WellTyped/Var.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Var.lean).

`Cedar.Thm.partial_eval_well_typed_var` (theorem, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Var.lean#L34))

```lean
theorem partial_eval_well_typed_var {env : TypeEnv} {v : Var} {ty : CedarType} {req : Request} {preq : PartialRequest} {es : Entities} {pes : PartialEntities} :
  PEWellTyped env (Residual.var v ty) (TPE.evaluate env (Residual.var v ty) preq pes) req preq es pes
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [WellTyped/Basic](basic.md)

## Proof depends on

- [PreservesTypeOf](../preservestypeof.md)
- [TypeLifting](../../welltyped/expr-2/typelifting.md)

## Sources

- [Cedar/Thm/TPE/WellTyped/Var.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Var.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.WellTyped.Var.json)

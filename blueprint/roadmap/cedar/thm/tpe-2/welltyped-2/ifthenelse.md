---
catalog: module
lean: Cedar.Thm.partial_eval_well_typed_ite
statement: formalized
proof: formalized
---

# WellTyped/IfThenElse

`Cedar.Thm.TPE.WellTyped.IfThenElse`, in [Cedar/Thm/TPE/WellTyped/IfThenElse.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/IfThenElse.lean).

`Cedar.Thm.partial_eval_well_typed_ite` (theorem, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/IfThenElse.lean#L34))

```lean
theorem partial_eval_well_typed_ite {env : TypeEnv} {c t e : Residual} {ty : CedarType} {req : Request} {preq : PartialRequest} {es : Entities} {pes : PartialEntities} :
  Residual.WellTyped env (TPE.evaluate env c preq pes) →
  Residual.WellTyped env (TPE.evaluate env t preq pes) →
  Residual.WellTyped env (TPE.evaluate env e preq pes) →
  PEWellTyped env (Residual.ite c t e ty) (TPE.evaluate env (Residual.ite c t e ty) preq pes) req preq es pes
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [WellTyped/Basic](basic.md)

## Proof depends on

- [PreservesTypeOf](../preservestypeof.md)

## Sources

- [Cedar/Thm/TPE/WellTyped/IfThenElse.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/IfThenElse.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.WellTyped.IfThenElse.json)

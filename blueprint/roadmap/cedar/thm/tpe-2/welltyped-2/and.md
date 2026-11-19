---
catalog: module
lean: Cedar.Thm.partial_eval_well_typed_and
statement: formalized
proof: formalized
---

# WellTyped/And

`Cedar.Thm.TPE.WellTyped.And`, in [Cedar/Thm/TPE/WellTyped/And.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/And.lean).

`Cedar.Thm.partial_eval_well_typed_and` (theorem, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/And.lean#L34))

```lean
theorem partial_eval_well_typed_and {env : TypeEnv} {a b : Residual} {ty : CedarType} {req : Request} {preq : PartialRequest} {es : Entities} {pes : PartialEntities} :
  Residual.WellTyped env (TPE.evaluate env a preq pes) →
  Residual.WellTyped env (TPE.evaluate env b preq pes) →
  PEWellTyped env (Residual.and a b ty) (TPE.evaluate env (Residual.and a b ty) preq pes) req preq es pes
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [WellTyped/Basic](basic.md)

## Proof depends on

- [PreservesTypeOf](../preservestypeof.md)

## Sources

- [Cedar/Thm/TPE/WellTyped/And.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/And.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.WellTyped.And.json)

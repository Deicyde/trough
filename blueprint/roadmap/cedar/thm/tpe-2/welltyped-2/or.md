---
catalog: module
lean: Cedar.Thm.partial_eval_well_typed_or
statement: formalized
proof: formalized
---

# WellTyped/Or

`Cedar.Thm.TPE.WellTyped.Or`, in [Cedar/Thm/TPE/WellTyped/Or.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Or.lean).

`Cedar.Thm.partial_eval_well_typed_or` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Or.lean#L35))

```lean
theorem partial_eval_well_typed_or {env : TypeEnv} {a b : Residual} {ty : CedarType} {req : Request} {preq : PartialRequest} {es : Entities} {pes : PartialEntities} :
  Residual.WellTyped env (TPE.evaluate env a preq pes) →
  Residual.WellTyped env (TPE.evaluate env b preq pes) →
  PEWellTyped env (Residual.or a b ty) (TPE.evaluate env (Residual.or a b ty) preq pes) req preq es pes
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [WellTyped/Basic](basic.md)

## Proof depends on

- [PreservesTypeOf](../preservestypeof.md)

## Sources

- [Cedar/Thm/TPE/WellTyped/Or.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Or.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.WellTyped.Or.json)

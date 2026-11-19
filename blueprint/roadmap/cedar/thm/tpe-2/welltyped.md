---
catalog: module
lean: Cedar.Thm.partial_eval_preserves_well_typed
statement: formalized
proof: formalized
---

# TPE/WellTyped

`Cedar.Thm.TPE.WellTyped`, in [Cedar/Thm/TPE/WellTyped.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped.lean).

> This file contains theorems about partial evaluation preserving well-typedness of residuals.

`Cedar.Thm.partial_eval_preserves_well_typed` (theorem, [line 60](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped.lean#L60))

> Theorem: Partial evaluation preserves well-typedness of residuals.
>
> If a residual is well-typed in some type environment, then partially evaluating it
> with a partial request and partial entities produces another well-typed residual
> in the same type environment.
>
> This is a fundamental property ensuring that the partial evaluation process
> maintains type safety throughout the computation.

```lean
theorem partial_eval_preserves_well_typed
  {env : TypeEnv}
  {res : Residual}
  {req : Request}
  {preq : PartialRequest}
  {es : Entities}
  {pes : PartialEntities} :
  InstanceOfWellFormedEnvironment req es env →
  RequestAndEntitiesRefine req es preq pes →
  Residual.WellTyped env res →
  Residual.WellTyped env (TPE.evaluate env res preq pes)
```

## Depends on

- [TPE/Evaluator](../../tpe/evaluator.md)
- [Thm/TPE/Input](input.md)
- [Residual/Definition](../welltyped/residual-2/definition.md)

## Proof depends on

- [WellTyped/And](welltyped-2/and.md)
- [WellTyped/Binary](welltyped-2/binary.md)
- [WellTyped/Call](welltyped-2/call.md)
- [WellTyped/ExtHasAttr](welltyped-2/exthasattr.md)
- [WellTyped/GetAttr](welltyped-2/getattr.md)
- [WellTyped/IfThenElse](welltyped-2/ifthenelse.md)
- [WellTyped/Or](welltyped-2/or.md)
- [WellTyped/Record](welltyped-2/record.md)
- [WellTyped/Set](welltyped-2/set.md)
- [WellTyped/Unary](welltyped-2/unary.md)
- [WellTyped/Var](welltyped-2/var.md)

## Sources

- [Cedar/Thm/TPE/WellTyped.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.TPE.WellTyped.json)

---
catalog: module
lean: Cedar.Thm.batched_evaluate_loop_eq_evaluate
statement: formalized
proof: formalized
---

# Evaluate

`Cedar.Thm.BatchedEvaluator.Evaluate`, in [Cedar/Thm/BatchedEvaluator/Evaluate.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Evaluate.lean).

> Soundness of batched expression evaluation: batched evaluation of a single
> well-typed residual produces the same result as direct evaluation with the
> complete entity store.

`Cedar.Thm.batched_evaluate_loop_eq_evaluate` (theorem, [line 23](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Evaluate.lean#L23))

```lean
theorem batched_evaluate_loop_eq_evaluate
  {x : Residual}
  {req : Request}
  (es : Entities)
  {current_store : PartialEntities}
  {env : TypeEnv} :
  EntityLoader.WellBehaved es loader →
  Residual.WellTyped env x →
  RequestAndEntitiesRefine req es req.asPartialRequest current_store →
  InstanceOfWellFormedEnvironment req es env →
  (Residual.evaluate (batchedEvaluateLoop env x req loader current_store iters) req es).toOption = (Residual.evaluate x req es).toOption
```

## Depends on

- [Common](common.md)
- [Residual/Definition](../welltyped/residual-2/definition.md)

## Proof depends on

- [TPE/Soundness](../tpe-2/soundness.md)

## Sources

- [Cedar/Thm/BatchedEvaluator/Evaluate.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Evaluate.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.BatchedEvaluator.Evaluate.json)

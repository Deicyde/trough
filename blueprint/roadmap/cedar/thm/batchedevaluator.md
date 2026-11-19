---
catalog: module
lean: Cedar.Thm.batched_evaluate_eq_evaluate, Cedar.Thm.batched_authorize_ok_equiv, Cedar.Thm.batched_authorize_decision_eq_authorize
statement: formalized
proof: formalized
---

# Thm/BatchedEvaluator

`Cedar.Thm.BatchedEvaluator`, in [Cedar/Thm/BatchedEvaluator.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator.lean).

> This file defines the main theorems for batched authorization and evaluation.

`Cedar.Thm.batched_evaluate_eq_evaluate` (theorem, [line 22](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator.lean#L22))

> The main correctness theorem for batched evaluation:
> Batched evaluation with an entity loader produces the same result
> as normal evaluation with the complete entity store.

```lean
theorem batched_evaluate_eq_evaluate
  {x : TypedExpr}
  {req : Request}
  {es : Entities}
  {env : TypeEnv} :
  EntityLoader.WellBehaved es loader →
  TypedExpr.WellTyped env x →
  InstanceOfWellFormedEnvironment req es env →
  (Residual.evaluate (batchedEvaluate env x req loader iters) req es).toOption = (evaluate x.toExpr req es).toOption
```

`Cedar.Thm.batched_authorize_ok_equiv` (theorem, [line 58](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator.lean#L58))

> A successful batched authorization returns `isAuthorizedFromResiduals` of a list equivalent to the
> policies, so any property of it transfers to the batched path without a second induction.

```lean
theorem batched_authorize_ok_equiv
  {schema : Schema} {policies : List Policy} {req : Request}
  {es : Entities} {response : TPE.Response} :
  EntityLoader.WellBehaved es loader →
  schema.validateWellFormed = .ok () →
  validateEntities schema es = .ok () →
  batchedAuthorize schema policies req loader iters = .ok response →
  ∃ rps, response = isAuthorizedFromResiduals rps ∧
    ResidualPoliciesEquiv policies rps req es
```

`Cedar.Thm.batched_authorize_decision_eq_authorize` (theorem, [line 122](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator.lean#L122))

> The main correctness theorem for batched authorization:
> If the batched authorizer reaches a definitive decision, that decision
> agrees with the concrete authorizer.

```lean
theorem batched_authorize_decision_eq_authorize
  {schema : Schema} {policies : List Policy} {req : Request}
  {es : Entities} {response : TPE.Response} {d : Decision} :
  EntityLoader.WellBehaved es loader →
  schema.validateWellFormed = .ok () →
  validateEntities schema es = .ok () →
  batchedAuthorize schema policies req loader iters = .ok response →
  response.decision = some d →
  (Spec.isAuthorized req es policies).decision = d
```

## Depends on

- [Common](batchedevaluator-2/common.md)
- [Thm/TPE/Authorizer](tpe-2/authorizer.md)
- [Expr/Definition](welltyped/expr-2/definition.md)

## Proof depends on

- [Authorize](batchedevaluator-2/authorize.md)
- [Evaluate](batchedevaluator-2/evaluate.md)

## Sources

- [Cedar/Thm/BatchedEvaluator.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Thm.BatchedEvaluator.json)

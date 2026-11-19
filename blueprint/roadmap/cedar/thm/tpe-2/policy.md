---
catalog: module
lean: Cedar.Thm.partial_evaluate_policy_is_sound
statement: formalized
proof: formalized
---

# TPE/Policy

`Cedar.Thm.TPE.Policy`, in [Cedar/Thm/TPE/Policy.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Policy.lean).

`Cedar.Thm.partial_evaluate_policy_is_sound` (theorem, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Policy.lean#L46))

> Policy evaluation soundness for TPE: Evaluating a result residual is equivalent to
> evaluating the input policy, given valid and consistent requests and entities.
> The equivalence is w.r.t authorization results. That is, the evaluation results
> are strictly equal when they are `.ok` or both errors (captured by
> `Except.toOption`). We do not care if the error types match because they do not
> impact authorization results. As a matter of fact, they do not match because all
> errors encountered during TPE are represented by an `error` residual, whose
> interpretation always produces an `extensionError`.

```lean
theorem partial_evaluate_policy_is_sound
  {schema : Schema}
  {residual : Residual}
  {policy : Policy}
  {req : Request}
  {es : Entities}
  {preq : PartialRequest}
  {pes : PartialEntities}
  {env : TypeEnv} :
  evaluatePolicy schema policy preq pes = .ok residual →
  schema.environment? preq.principal.ty preq.resource.ty preq.action = .some env →
  InstanceOfWellFormedEnvironment req es env →
  RequestAndEntitiesRefine req es preq pes →
  (Spec.evaluate policy.toExpr req es).toOption = (Residual.evaluate residual req es).toOption
```

## Depends on

- [TPE/Evaluator](../../tpe/evaluator.md)
- [Thm/TPE/Input](input.md)
- [Typechecker/Types](../validation-2/typechecker-2/types.md)

## Proof depends on

- [Conversion](conversion.md)
- [TPE/Soundness](soundness.md)
- [SubstituteAction](../validation-2/substituteaction.md)
- [Thm/Validation/Typechecker](../validation-2/typechecker.md)

## Sources

- [Cedar/Thm/TPE/Policy.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Policy.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.TPE.Policy.json)

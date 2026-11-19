---
catalog: module
lean: Cedar.Thm.evaluatePolicy_ok_implies_env_some, Cedar.Thm.evaluatePolicy_ok_implies_requestMatchesEnvironment, Cedar.Thm.evaluatePolicy_ok_implies_well_formed_env, Cedar.Thm.ResidualPoliciesEquivAndWellTyped, Cedar.Thm.equiv_well_typed_implies_equiv, Cedar.Thm.residuals_equiv_preserved, Cedar.Thm.batched_authorize_loop_equiv, Cedar.Thm.batched_authorize_loop_decision_agrees, Cedar.Thm.evaluatePolicies_equiv_and_well_typed
statement: formalized
proof: formalized
---

# Authorize

`Cedar.Thm.BatchedEvaluator.Authorize`, in [Cedar/Thm/BatchedEvaluator/Authorize.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Authorize.lean).

> Soundness of batched authorization: if the batched authorizer reaches a
> definitive decision, that decision agrees with the concrete authorizer.

`Cedar.Thm.evaluatePolicy_ok_implies_env_some` (theorem, [line 23](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Authorize.lean#L23))

```lean
theorem evaluatePolicy_ok_implies_env_some {schema : Schema} {p : Policy}
  {preq : PartialRequest} {pes : PartialEntities} {r : Residual} :
  evaluatePolicy schema p preq pes = .ok r →
  ∃ env, schema.environment? preq.principal.ty preq.resource.ty preq.action = .some env
```

`Cedar.Thm.evaluatePolicy_ok_implies_requestMatchesEnvironment` (theorem, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Authorize.lean#L38))

```lean
theorem evaluatePolicy_ok_implies_requestMatchesEnvironment
  {schema : Schema} {p : Policy} {req : Request} {r : Residual} {pes : PartialEntities} :
  evaluatePolicy schema p req.asPartialRequest pes = .ok r →
  ∀ env, schema.environment? req.asPartialRequest.principal.ty req.asPartialRequest.resource.ty req.asPartialRequest.action = .some env →
  requestMatchesEnvironment env req
```

`Cedar.Thm.evaluatePolicy_ok_implies_well_formed_env` (theorem, [line 55](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Authorize.lean#L55))

> If `evaluatePolicy` succeeds on a concrete request, and the schema and entities
> pass validation, then `InstanceOfWellFormedEnvironment` holds for the
> environment determined by the schema and request.

```lean
theorem evaluatePolicy_ok_implies_well_formed_env
  {schema : Schema} {p : Policy} {req : Request} {es : Entities} {r : Residual}
  {pes : PartialEntities} :
  evaluatePolicy schema p req.asPartialRequest pes = .ok r →
  schema.validateWellFormed = .ok () →
  validateEntities schema es = .ok () →
  ∃ env,
    schema.environment? req.asPartialRequest.principal.ty req.asPartialRequest.resource.ty req.asPartialRequest.action = .some env ∧
    InstanceOfWellFormedEnvironment req es env
```

`Cedar.Thm.ResidualPoliciesEquivAndWellTyped` (definition, [line 73](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Authorize.lean#L73))

```lean
def ResidualPoliciesEquivAndWellTyped
  (env : TypeEnv)
  (policies : List Policy)
  (residuals : List ResidualPolicy)
  (req : Request)
  (es : Entities) : Prop
```

`Cedar.Thm.equiv_well_typed_implies_equiv` (theorem, [line 86](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Authorize.lean#L86))

```lean
theorem equiv_well_typed_implies_equiv
  (h : ResidualPoliciesEquivAndWellTyped env policies residuals req es) :
  ResidualPoliciesEquiv policies residuals req es
```

`Cedar.Thm.residuals_equiv_preserved` (theorem, [line 91](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Authorize.lean#L91))

```lean
theorem residuals_equiv_preserved
  {env : TypeEnv} {policies : List Policy} {residuals : List ResidualPolicy}
  {req : Request} {es : Entities} {pes : PartialEntities}
  (h_sound : ResidualPoliciesEquivAndWellTyped env policies residuals req es)
  (h_wf : InstanceOfWellFormedEnvironment req es env)
  (h_ref : RequestAndEntitiesRefine req es req.asPartialRequest pes) :
  ResidualPoliciesEquivAndWellTyped env policies
    (residuals.map λ rp => ⟨rp.id, rp.effect, Cedar.TPE.evaluate env rp.residual req.asPartialRequest pes⟩)
    req es
```

`Cedar.Thm.batched_authorize_loop_equiv` (theorem, [line 110](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Authorize.lean#L110))

> The loop's response is `isAuthorizedFromResiduals` of a list still equivalent to the policies.

```lean
theorem batched_authorize_loop_equiv
  {policies : List Policy} {residuals : List ResidualPolicy} {req : Request}
  (es : Entities) {current_store : PartialEntities} {env : TypeEnv} :
  EntityLoader.WellBehaved es loader →
  ResidualPoliciesEquivAndWellTyped env policies residuals req es →
  RequestAndEntitiesRefine req es req.asPartialRequest current_store →
  InstanceOfWellFormedEnvironment req es env →
  ∃ rps, batchedAuthorizeLoop env residuals req loader current_store iters
      = isAuthorizedFromResiduals rps ∧
    ResidualPoliciesEquivAndWellTyped env policies rps req es
```

`Cedar.Thm.batched_authorize_loop_decision_agrees` (theorem, [line 143](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Authorize.lean#L143))

> The loop's decision agrees with concrete authorization.

```lean
theorem batched_authorize_loop_decision_agrees
  {policies : List Policy} {residuals : List ResidualPolicy} {req : Request}
  (es : Entities) {current_store : PartialEntities} {env : TypeEnv} {d : Decision} :
  EntityLoader.WellBehaved es loader →
  ResidualPoliciesEquivAndWellTyped env policies residuals req es →
  RequestAndEntitiesRefine req es req.asPartialRequest current_store →
  InstanceOfWellFormedEnvironment req es env →
  (batchedAuthorizeLoop env residuals req loader current_store iters).decision = some d →
  (Spec.isAuthorized req es policies).decision = d
```

`Cedar.Thm.evaluatePolicies_equiv_and_well_typed` (theorem, [line 158](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Authorize.lean#L158))

```lean
theorem evaluatePolicies_equiv_and_well_typed
  {schema : Schema} {policies : List Policy} {rps : List ResidualPolicy}
  {req : Request} {es : Entities} {preq : PartialRequest}
  {pes : PartialEntities} {env : TypeEnv} :
  List.Forall₂ (λ p rp => ResidualPolicy.mk p.id p.effect <$> evaluatePolicy schema p preq pes = .ok rp) policies rps →
  schema.environment? preq.principal.ty preq.resource.ty preq.action = .some env →
  InstanceOfWellFormedEnvironment req es env →
  RequestAndEntitiesRefine req es preq pes →
  ResidualPoliciesEquivAndWellTyped env policies rps req es
```

## Depends on

- [Common](common.md)
- [Thm/TPE/Authorizer](../tpe-2/authorizer.md)
- [Residual/Definition](../welltyped/residual-2/definition.md)

## Sources

- [Cedar/Thm/BatchedEvaluator/Authorize.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/BatchedEvaluator/Authorize.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.BatchedEvaluator.Authorize.json)

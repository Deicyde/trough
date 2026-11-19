---
catalog: module
lean: Cedar.Thm.ResidualPoliciesEquiv, Cedar.Thm.isValidAndConsistent_env, Cedar.Thm.evaluatePolicies_residuals_equiv, Cedar.Thm.reauthorize_satisfied_policies_equiv, Cedar.Thm.reauthorize_error_policies_equiv, Cedar.Thm.no_satisfied_effect_if_empty_satisfied_and_residual_policies, Cedar.Thm.satisfied_effect_if_non_empty_satisfied_policies, Cedar.Thm.residuals_decision_agrees, Cedar.Thm.partial_authorize_error_policies_is_sound, Cedar.Thm.partial_authorize_satisfied_policies_is_sound, Cedar.Thm.partial_authorize_satisfied_forbids_is_sound, Cedar.Thm.partial_authorize_satisfied_permits_is_sound
statement: formalized
proof: formalized
---

# Thm/TPE/Authorizer

`Cedar.Thm.TPE.Authorizer`, in [Cedar/Thm/TPE/Authorizer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Authorizer.lean).

`Cedar.Thm.ResidualPoliciesEquiv` (definition, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Authorizer.lean#L38))

```lean
def ResidualPoliciesEquiv
  (policies : List Policy)
  (residuals : List ResidualPolicy)
  (req : Request)
  (es : Entities) : Prop
```

`Cedar.Thm.isValidAndConsistent_env` (theorem, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Authorizer.lean#L49))

```lean
theorem isValidAndConsistent_env
  {schema : Schema} {req : Request} {es : Entities}
  {preq : PartialRequest} {pes : PartialEntities} :
  isValidAndConsistent schema req es preq pes = .ok () →
  ∃ env,
    schema.environment? preq.principal.ty preq.resource.ty preq.action = .some env ∧
    InstanceOfWellFormedEnvironment req es env
```

`Cedar.Thm.evaluatePolicies_residuals_equiv` (theorem, [line 82](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Authorizer.lean#L82))

```lean
theorem evaluatePolicies_residuals_equiv
  {schema : Schema}
  {policies : List Policy}
  {rps : List ResidualPolicy}
  {req : Request}
  {es : Entities}
  {preq : PartialRequest}
  {pes : PartialEntities}
  (hv : isValidAndConsistent schema req es preq pes = Except.ok ())
  (h : isAuthorized.evaluatePolicies schema policies preq pes = Except.ok rps) :
  ResidualPoliciesEquiv policies rps req es
```

`Cedar.Thm.reauthorize_satisfied_policies_equiv` (theorem, [line 104](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Authorizer.lean#L104))

```lean
theorem reauthorize_satisfied_policies_equiv
  {policies : List Policy}
  {req : Request}
  {es : Entities}
  {residuals : List ResidualPolicy}
  (h_auth : ResidualPoliciesEquiv policies residuals req es) :
  ∀ effect,
    TPE.Response.reauthorize.satisfiedPolicies effect residuals req es = Spec.satisfiedPolicies effect policies req es
```

`Cedar.Thm.reauthorize_error_policies_equiv` (theorem, [line 136](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Authorizer.lean#L136))

```lean
theorem reauthorize_error_policies_equiv
  {policies : List Policy}
  {req : Request}
  {es : Entities}
  {residuals : List ResidualPolicy}
  (h_auth : ResidualPoliciesEquiv policies residuals req es) :
  TPE.Response.reauthorize.errorPolicies residuals req es = Spec.errorPolicies policies req es
```

`Cedar.Thm.no_satisfied_effect_if_empty_satisfied_and_residual_policies` (theorem, [line 174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Authorizer.lean#L174))

```lean
theorem no_satisfied_effect_if_empty_satisfied_and_residual_policies
  {policies : List Policy}
  {rps : List ResidualPolicy}
  {req : Request}
  {es : Entities}
  {effect : Effect}
  (h₃ : ResidualPoliciesEquiv policies rps req es)
  (h_satisfied_empty : (isAuthorizedFromResiduals.satisfiedPolicies effect rps).isEmpty)
  (h_residual_empty : (isAuthorizedFromResiduals.residualPolicies effect rps).isEmpty) :
  ¬HasSatisfiedEffect effect req es policies
```

`Cedar.Thm.satisfied_effect_if_non_empty_satisfied_policies` (theorem, [line 211](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Authorizer.lean#L211))

```lean
theorem satisfied_effect_if_non_empty_satisfied_policies
  {policies : List Policy}
  {rps : List ResidualPolicy}
  {req : Request}
  {es : Entities}
  {effect : Effect}
  (h₃ : ResidualPoliciesEquiv policies rps req es)
  (h_non_empty : ¬(isAuthorizedFromResiduals.satisfiedPolicies effect rps).isEmpty) :
  HasSatisfiedEffect effect req es policies
```

`Cedar.Thm.residuals_decision_agrees` (theorem, [line 238](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Authorizer.lean#L238))

```lean
theorem residuals_decision_agrees
  {policies : List Policy}
  {rps : List ResidualPolicy}
  {req : Request}
  {es : Entities}
  {d : Decision}
  (h₃ : ResidualPoliciesEquiv policies rps req es)
  (h_dec : (isAuthorizedFromResiduals rps).decision = some d) :
  (Spec.isAuthorized req es policies).decision = d
```

`Cedar.Thm.partial_authorize_error_policies_is_sound` (theorem, [line 267](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Authorizer.lean#L267))

```lean
theorem partial_authorize_error_policies_is_sound
  {policies : List Policy}
  {rps : List ResidualPolicy}
  {req : Request}
  {es : Entities}
  (effect : Effect)
  (h₁ : ResidualPoliciesEquiv policies rps req es) :
  isAuthorizedFromResiduals.errorPolicies effect rps ⊆ (Spec.isAuthorized req es policies).erroringPolicies
```

`Cedar.Thm.partial_authorize_satisfied_policies_is_sound` (theorem, [line 293](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Authorizer.lean#L293))

```lean
theorem partial_authorize_satisfied_policies_is_sound
  {policies : List Policy}
  {rps : List ResidualPolicy}
  {req : Request}
  {es : Entities}
  (effect : Effect)
  (h₁ : ResidualPoliciesEquiv policies rps req es) :
  isAuthorizedFromResiduals.satisfiedPolicies effect rps ⊆ Spec.satisfiedPolicies effect policies req es
```

`Cedar.Thm.partial_authorize_satisfied_forbids_is_sound` (theorem, [line 321](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Authorizer.lean#L321))

```lean
theorem partial_authorize_satisfied_forbids_is_sound
  {schema : Schema}
  {policies : List Policy}
  {req : Request}
  {es : Entities}
  {preq : PartialRequest}
  {pes : PartialEntities} :
  TPE.isAuthorized schema policies preq pes = Except.ok response →
  isValidAndConsistent schema req es preq pes = Except.ok () →
  response.satisfiedForbids ⊆ Spec.satisfiedPolicies .forbid policies req es
```

`Cedar.Thm.partial_authorize_satisfied_permits_is_sound` (theorem, [line 340](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Authorizer.lean#L340))

```lean
theorem partial_authorize_satisfied_permits_is_sound
  {schema : Schema}
  {policies : List Policy}
  {req : Request}
  {es : Entities}
  {preq : PartialRequest}
  {pes : PartialEntities} :
  TPE.isAuthorized schema policies preq pes = Except.ok response →
  isValidAndConsistent schema req es preq pes = Except.ok () →
  response.satisfiedPermits ⊆ Spec.satisfiedPolicies .permit policies req es
```

## Depends on

- [Cedar/TPE/Authorizer](../../tpe/authorizer.md)
- [Authorization](../authorization.md)
- [Typechecker/Types](../validation-2/typechecker-2/types.md)

## Proof depends on

- [TPE/Policy](policy.md)
- [RequestEntityValidation](../validation-2/requestentityvalidation.md)

## Sources

- [Cedar/Thm/TPE/Authorizer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Authorizer.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.TPE.Authorizer.json)

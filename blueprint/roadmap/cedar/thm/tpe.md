---
catalog: module
lean: Cedar.Thm.reauthorize_is_sound, Cedar.Thm.partial_authorize_decision_is_sound, Cedar.Thm.partial_re_authorize_decision_eq, Cedar.Thm.partial_authorize_erroring_policies_is_sound, Cedar.Thm.partial_authorize_allow_determining_policies_is_sound, Cedar.Thm.partial_authorize_satisfied_permits_not_determining_if_deny, Cedar.Thm.partial_authorize_satisfied_forbid_is_determining, Cedar.Thm.partial_authorize_no_satisfied_forbids_if_allow
statement: formalized
proof: formalized
---

# TPE

`Cedar.Thm.TPE`, in [Cedar/Thm/TPE.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE.lean).

> This file defines the main theorem of TPE soundness for authorization.
>
> Significant lemmas proving soundness of policy and expression evaluation are in
> `Cedar.Thm.TPE.Policy` and `Cedar.Thm.TPE.Soundness`.

`Cedar.Thm.reauthorize_is_sound` (theorem, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE.lean#L51))

> Main re-authorization soundness theorem: The result of reauthorizing a
> partial authorization response with concrete request and entities is equivalent
> to directly authorizing with the concrete request and entities.

```lean
theorem reauthorize_is_sound
  {schema : Schema}
  {policies : List Policy}
  {req : Request}
  {es : Entities}
  {preq : PartialRequest}
  {pes : PartialEntities}
  {response : TPE.Response} :
  isValidAndConsistent schema req es preq pes = Except.ok () →
  TPE.isAuthorized schema policies preq pes = Except.ok response →
  response.reauthorize req es = Spec.isAuthorized req es policies
```

`Cedar.Thm.partial_authorize_decision_is_sound` (theorem, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE.lean#L79))

> Main partial authorization soundness theorem: If partial authorization
> returns a decision, then concrete authorization will reach the same.

```lean
theorem partial_authorize_decision_is_sound
  {schema : Schema}
  {policies : List Policy}
  {req : Request}
  {es : Entities}
  {preq : PartialRequest}
  {pes : PartialEntities}
  {response : TPE.Response}
  {decision : Decision} :
  TPE.isAuthorized schema policies preq pes = Except.ok response →
  isValidAndConsistent schema req es preq pes = Except.ok () →
  response.decision = some decision →
  (Spec.isAuthorized req es policies).decision = decision
```

`Cedar.Thm.partial_re_authorize_decision_eq` (theorem, [line 102](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE.lean#L102))

> Trivial composition of the first two soundness theorems directly relating
> the decision of partial authorization and subsequent re-authorization.

```lean
theorem partial_re_authorize_decision_eq
  {schema : Schema}
  {policies : List Policy}
  {req : Request}
  {es : Entities}
  {preq : PartialRequest}
  {pes : PartialEntities}
  {response : TPE.Response}
  {decision : Decision} :
  TPE.isAuthorized schema policies preq pes = Except.ok response →
  isValidAndConsistent schema req es preq pes = Except.ok () →
  response.decision = some decision →
  (response.reauthorize req es).decision = decision
```

`Cedar.Thm.partial_authorize_erroring_policies_is_sound` (theorem, [line 123](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE.lean#L123))

> All policies reported as erroring after partial authorization will appear in
> the set of erroring policies after concrete authorization.

```lean
theorem partial_authorize_erroring_policies_is_sound
  {schema : Schema}
  {policies : List Policy}
  {req : Request}
  {es : Entities}
  {preq : PartialRequest}
  {pes : PartialEntities}
  {response : TPE.Response} :
  TPE.isAuthorized schema policies preq pes = Except.ok response →
  isValidAndConsistent schema req es preq pes = Except.ok () →
  (response.errorForbids ∪ response.errorPermits) ⊆ (Spec.isAuthorized req es policies).erroringPolicies
```

`Cedar.Thm.partial_authorize_allow_determining_policies_is_sound` (theorem, [line 148](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE.lean#L148))

> If the result of concrete authorization is `allow`, then all `permit`
> policies satisfied after partial authorization are determining policies.

```lean
theorem partial_authorize_allow_determining_policies_is_sound
  {schema : Schema}
  {policies : List Policy}
  {req : Request}
  {es : Entities}
  {preq : PartialRequest}
  {pes : PartialEntities}
  {response : TPE.Response} :
  TPE.isAuthorized schema policies preq pes = Except.ok response →
  isValidAndConsistent schema req es preq pes = Except.ok () →
  (Spec.isAuthorized req es policies).decision = .allow →
  response.satisfiedPermits ⊆ (Spec.isAuthorized req es policies).determiningPolicies
```

`Cedar.Thm.partial_authorize_satisfied_permits_not_determining_if_deny` (theorem, [line 178](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE.lean#L178))

> If the result of concrete authorization is `deny`, then any permit policies
> satisfied after partial authorization cannot be determining policies.

```lean
theorem partial_authorize_satisfied_permits_not_determining_if_deny
  {schema : Schema}
  {policies : List Policy}
  {req : Request}
  {es : Entities}
  {preq : PartialRequest}
  {pes : PartialEntities}
  {response : TPE.Response} :
  TPE.isAuthorized schema policies preq pes = Except.ok response →
  isValidAndConsistent schema req es preq pes = Except.ok () →
  (Spec.isAuthorized req es policies).decision = .deny →
  PolicyIdsUnique policies →
  (response.satisfiedPermits ∩ (Spec.isAuthorized req es policies).determiningPolicies).isEmpty
```

`Cedar.Thm.partial_authorize_satisfied_forbid_is_determining` (theorem, [line 215](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE.lean#L215))

> Like `partial_authorize_allow_determining_policies_is_sound` for `forbid`
> policies, but we can prove a stronger theorem because of `forbid_trumps_permit`.
> Any forbid policy satisfied after partial evaluation will always be determining.

```lean
theorem partial_authorize_satisfied_forbid_is_determining
  {schema : Schema}
  {policies : List Policy}
  {req : Request}
  {es : Entities}
  {preq : PartialRequest}
  {pes : PartialEntities}
  {response : TPE.Response} :
  TPE.isAuthorized schema policies preq pes = Except.ok response →
  isValidAndConsistent schema req es preq pes = Except.ok () →
  response.satisfiedForbids ⊆ (Spec.isAuthorized req es policies).determiningPolicies
```

`Cedar.Thm.partial_authorize_no_satisfied_forbids_if_allow` (theorem, [line 265](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE.lean#L265))

> Like `partial_authorize_satisfied_permits_not_determining_if_deny` for
> `forbid` policies, but we can prove a stronger theorem because any satisfied
> forbid causes the decision to be `deny`.  If the result of concrete
> authorization is `allow`, then there can be no satisfied forbid policies after
> partial authorization.

```lean
theorem partial_authorize_no_satisfied_forbids_if_allow
  {schema : Schema}
  {policies : List Policy}
  {req : Request}
  {es : Entities}
  {preq : PartialRequest}
  {pes : PartialEntities}
  {response : TPE.Response} :
  TPE.isAuthorized schema policies preq pes = Except.ok response →
  isValidAndConsistent schema req es preq pes = Except.ok () →
  (Spec.isAuthorized req es policies).decision = .allow →
  response.satisfiedForbids.isEmpty
```

## Depends on

- [Cedar/TPE/Authorizer](../tpe/authorizer.md)
- [Authorization](authorization.md)

## Proof depends on

- [Thm/TPE/Authorizer](tpe-2/authorizer.md)

## Sources

- [Cedar/Thm/TPE.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Thm.TPE.json)

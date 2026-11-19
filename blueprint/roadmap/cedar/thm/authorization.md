---
catalog: module
lean: Cedar.Thm.PolicyIdsUnique, Cedar.Thm.HasSatisfiedEffect, Cedar.Thm.satisfied_iff_satisfiedPolicies_non_empty, Cedar.Thm.IsExplicitlyForbidden, Cedar.Thm.explicitly_forbidden_iff_satisfying_forbid, Cedar.Thm.IsExplicitlyPermitted, Cedar.Thm.explicitly_permitted_iff_satisfying_permit, Cedar.Thm.forbid_trumps_permit, Cedar.Thm.allowed_only_if_explicitly_permitted, Cedar.Thm.default_deny, Cedar.Thm.allowed_iff_explicitly_permitted_and_not_denied, Cedar.Thm.denied_iff_explicitly_denied_or_not_permitted, Cedar.Thm.order_and_dup_independent, Cedar.Thm.unchanged_allow_when_add_permit, Cedar.Thm.unchanged_deny_when_add_forbid, Cedar.Thm.determiningPolicies_of, Cedar.Thm.unchanged_determining_when_add_policy_and_decision_unchanged, Cedar.Thm.unchanged_erroring_when_add_policy, Cedar.Thm.determining_erroring_disjoint_when_unique_ids
statement: formalized
proof: formalized
---

# Authorization

`Cedar.Thm.Authorization`, in [Cedar/Thm/Authorization.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean).

> This file contains basic theorems about Cedar's authorizer.

`Cedar.Thm.PolicyIdsUnique` (definition, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L34))

```lean
def PolicyIdsUnique (policies : Policies)
```

`Cedar.Thm.HasSatisfiedEffect` (definition, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L37))

```lean
def HasSatisfiedEffect (effect : Effect) (request : Request) (entities : Entities) (policies : Policies) : Prop
```

`Cedar.Thm.satisfied_iff_satisfiedPolicies_non_empty` (theorem, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L43))

```lean
theorem satisfied_iff_satisfiedPolicies_non_empty {effect : Effect} {request : Request} {entities : Entities} {policies : Policies} :
  HasSatisfiedEffect effect request entities policies ↔ (satisfiedPolicies effect policies request entities).isEmpty = false
```

`Cedar.Thm.IsExplicitlyForbidden` (definition, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L50))

> A request is explicitly forbidden when there is at least one satisfied forbid policy.

```lean
def IsExplicitlyForbidden
```

`Cedar.Thm.explicitly_forbidden_iff_satisfying_forbid` (theorem, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L52))

```lean
theorem explicitly_forbidden_iff_satisfying_forbid :
  IsExplicitlyForbidden req entities policies ↔ (satisfiedPolicies .forbid policies req entities).isEmpty = false
```

`Cedar.Thm.IsExplicitlyPermitted` (definition, [line 60](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L60))

> A request is explicitly permitted when there is at least one satisfied permit policy.
> Note that there may still be satisfied forbid policies leading to a deny decisions.

```lean
def IsExplicitlyPermitted
```

`Cedar.Thm.explicitly_permitted_iff_satisfying_permit` (theorem, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L62))

```lean
theorem explicitly_permitted_iff_satisfying_permit :
  IsExplicitlyPermitted req entities policies ↔ (satisfiedPolicies .permit policies req entities).isEmpty = false
```

`Cedar.Thm.forbid_trumps_permit` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L69))

> Forbid trumps permit: if a `forbid` policy is satisfied, the request is denied.

```lean
theorem forbid_trumps_permit
  (request : Request) (entities : Entities) (policies : Policies) :
  (IsExplicitlyForbidden request entities policies) →
  (isAuthorized request entities policies).decision = .deny
```

`Cedar.Thm.allowed_only_if_explicitly_permitted` (theorem, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L80))

> A request is allowed only if it is explicitly permitted.

```lean
theorem allowed_only_if_explicitly_permitted (request : Request) (entities : Entities) (policies : Policies) :
  (isAuthorized request entities policies).decision = .allow →
  IsExplicitlyPermitted request entities policies
```

`Cedar.Thm.default_deny` (theorem, [line 97](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L97))

> Default deny: if not explicitly permitted, the request is denied.
> This is contrapositive of allowed_only_if_explicitly_permitted.

```lean
theorem default_deny (request : Request) (entities : Entities) (policies : Policies) :
  ¬ IsExplicitlyPermitted request entities policies →
  (isAuthorized request entities policies).decision = .deny
```

`Cedar.Thm.allowed_iff_explicitly_permitted_and_not_denied` (theorem, [line 114](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L114))

> A request is allowed if and only if it is explicitly permitted and is not
> explicitly forbidden.

```lean
theorem allowed_iff_explicitly_permitted_and_not_denied (request : Request) (entities : Entities) (policies : Policies) :
  (IsExplicitlyPermitted request entities policies ∧ ¬ IsExplicitlyForbidden request entities policies) ↔
  (isAuthorized request entities policies).decision = .allow
```

`Cedar.Thm.denied_iff_explicitly_denied_or_not_permitted` (theorem, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L133))

> A request is denied if and only if it is explicitly denied or it is not explicitly permitted.

```lean
theorem denied_iff_explicitly_denied_or_not_permitted (request: Request) (entities : Entities) (policies: Policies) :
  (IsExplicitlyForbidden request entities policies ∨ ¬ IsExplicitlyPermitted request entities policies) ↔
    (isAuthorized request entities policies).decision = .deny
```

`Cedar.Thm.order_and_dup_independent` (theorem, [line 158](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L158))

> Order and duplicate independence: isAuthorized produces the same result
> regardless of policy order or duplicates.

```lean
theorem order_and_dup_independent (request : Request) (entities : Entities) (policies₁ policies₂ : Policies) :
  policies₁ ≡ policies₂ →
  isAuthorized request entities policies₁ = isAuthorized request entities policies₂
```

`Cedar.Thm.unchanged_allow_when_add_permit` (theorem, [line 171](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L171))

> Adding a permit policy won't change an Allow decision.

```lean
theorem unchanged_allow_when_add_permit (request: Request) (entities: Entities) (policies: Policies) (policy₂: Policy) :
  policy₂.effect = .permit →
  (isAuthorized request entities policies).decision = .allow →
  (isAuthorized request entities (policy₂ :: policies)).decision = .allow
```

`Cedar.Thm.unchanged_deny_when_add_forbid` (theorem, [line 184](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L184))

> Adding a forbid policy won't change a Deny decision.

```lean
theorem unchanged_deny_when_add_forbid (request : Request) (entities: Entities) (policies: Policies) (policy₂: Policy) :
  policy₂.effect = .forbid →
  (isAuthorized request entities policies).decision = .deny →
  (isAuthorized request entities (policy₂ :: policies)).decision = .deny
```

`Cedar.Thm.determiningPolicies_of` (theorem, [line 200](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L200))

> The determining policies of a allow/deny decision are exactly the satisfied policies of permit/forbid resp.

```lean
theorem determiningPolicies_of (request: Request) (entities: Entities) (policies: Policies) :
  let auth := isAuthorized request entities policies
  auth.determiningPolicies = satisfiedPolicies (if auth.decision = .allow then .permit else .forbid) policies request entities
```

`Cedar.Thm.unchanged_determining_when_add_policy_and_decision_unchanged` (theorem, [line 215](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L215))

> If P is a determining policy, then adding a new policy resulting in the same decision won't change that.

```lean
theorem unchanged_determining_when_add_policy_and_decision_unchanged (request: Request) (entities: Entities) (policies: Policies) (policy₀ : Policy) :
  let auth  := (isAuthorized request entities policies)
  let auth' := (isAuthorized request entities (policy₀ :: policies))
  auth.decision = auth'.decision → auth.determiningPolicies ⊆ auth'.determiningPolicies
```

`Cedar.Thm.unchanged_erroring_when_add_policy` (theorem, [line 237](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L237))

> If P is an erroring policy, then adding another policy won’t change that (even if the decision changes).

```lean
theorem unchanged_erroring_when_add_policy (request: Request) (entities: Entities) (policies : Policies) (policy₀ : Policy) :
  (isAuthorized request entities policies).erroringPolicies ⊆ (isAuthorized request entities (policy₀ :: policies)).erroringPolicies
```

`Cedar.Thm.determining_erroring_disjoint_when_unique_ids` (theorem, [line 254](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean#L254))

> Determining policies and erroring policies of an isAuthorized response are disjoint when input policy IDs are unique.

```lean
theorem determining_erroring_disjoint_when_unique_ids (request : Request) (entities : Entities) (policies : Policies) :
  PolicyIdsUnique policies →
    ((isAuthorized request entities policies).determiningPolicies ∩ (isAuthorized request entities policies).erroringPolicies).isEmpty
```

## Depends on

- [Spec/Authorizer](../spec/authorizer.md)
- [List properties](data/list/basic.md)

## Proof depends on

- [Authorization/Authorizer](authorization-2/authorizer.md)

## Sources

- [Cedar/Thm/Authorization.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Thm.Authorization.json)

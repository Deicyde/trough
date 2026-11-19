---
catalog: module
lean: Cedar.Thm.determiningPolicies_wf, Cedar.Thm.if_hasError_then_exists_error, Cedar.Thm.satisfiedPolicies_order_and_dup_independent, Cedar.Thm.errorPolicies_order_and_dup_independent, Cedar.Thm.satisfied_policies_congr_evaluate, Cedar.Thm.error_policies_congr_evaluate, Cedar.Thm.isAuthorized_eq_of_satisfied_and_error_policies_eq, Cedar.Thm.is_authorized_congr_evaluate, Cedar.Thm.alternateErrorPolicies, Cedar.Thm.alternate_errorPolicies_equiv_errorPolicies, Cedar.Thm.exists_hasError_of_mem_erroringPolicies, Cedar.Thm.principal_eval_ok_means_principal_in_uid, Cedar.Thm.resource_eval_ok_means_resource_in_uid, Cedar.Thm.satisfied_implies_principal_scope, Cedar.Thm.satisfied_implies_resource_scope, Cedar.Thm.mapM_evaluate_uids_produces_uids, Cedar.Thm.asEntityUID_of_uid, Cedar.Thm.mapM_asEntityUID_of_uid, Cedar.Thm.Except.isOk_iff_exists, Cedar.Thm.if_mapM_doesn't_fail_on_list_then_doesn't_fail_on_set, Cedar.Thm.mapM_asEntityUID_on_set_uids_produces_ok, Cedar.Thm.mapOrErr_value_asEntityUID_on_uids_produces_set, Cedar.Thm.action_in_set_of_euids_produces_boolean, Cedar.Thm.principal_scope_produces_boolean, Cedar.Thm.action_scope_produces_boolean, Cedar.Thm.resource_scope_produces_boolean, Cedar.Thm.produces_boolean_means_not_non_boolean, Cedar.Thm.principal_scope_does_not_throw, Cedar.Thm.action_scope_does_not_throw, Cedar.Thm.resource_scope_does_not_throw, Cedar.Thm.principal_scope_false_then_policy_false, Cedar.Thm.action_scope_false_then_policy_false, Cedar.Thm.resource_scope_false_then_policy_false, Cedar.Thm.error_implies_scope_satisfied, Cedar.Thm.error_implies_principal_scope_in, Cedar.Thm.error_implies_resource_scope_in
statement: formalized
proof: formalized
---

# Authorization/Authorizer

`Cedar.Thm.Authorization.Authorizer`, in [Cedar/Thm/Authorization/Authorizer.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean).

> This file contains useful lemmas about the `Authorizer` functions.

`Cedar.Thm.determiningPolicies_wf` (theorem, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L38))

```lean
theorem determiningPolicies_wf {policies : Policies} {request : Request} {entities : Entities} :
  (isAuthorized request entities policies).determiningPolicies.WellFormed
```

`Cedar.Thm.if_hasError_then_exists_error` (theorem, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L52))

```lean
theorem if_hasError_then_exists_error {policy : Policy} {request : Request} {entities : Entities} :
  hasError policy request entities →
  ∃ err, evaluate policy.toExpr request entities = .error err
```

`Cedar.Thm.satisfiedPolicies_order_and_dup_independent` (theorem, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L62))

```lean
theorem satisfiedPolicies_order_and_dup_independent {policies₁ policies₂ : Policies} (effect : Effect) (request : Request) (entities : Entities) :
  policies₁ ≡ policies₂ →
  satisfiedPolicies effect policies₁ request entities = satisfiedPolicies effect policies₂ request entities
```

`Cedar.Thm.errorPolicies_order_and_dup_independent` (theorem, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L71))

```lean
theorem errorPolicies_order_and_dup_independent {policies₁ policies₂ : Policies} (request : Request) (entities : Entities) :
  policies₁ ≡ policies₂ →
  errorPolicies policies₁ request entities = errorPolicies policies₂ request entities
```

`Cedar.Thm.satisfied_policies_congr_evaluate` (theorem, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L80))

```lean
theorem satisfied_policies_congr_evaluate {ps : Policies} {r₁ r₂ : Request} {es₁ es₂ : Entities} (effect : Effect)
  (heq : ∀ p ∈ ps, evaluate p.toExpr r₁ es₁ = evaluate p.toExpr r₂ es₂) :
  satisfiedPolicies effect ps r₁ es₁ = satisfiedPolicies effect ps r₂ es₂
```

`Cedar.Thm.error_policies_congr_evaluate` (theorem, [line 91](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L91))

```lean
theorem error_policies_congr_evaluate {ps : Policies} {r₁ r₂ : Request} {es₁ es₂ : Entities}
  (heq : ∀ p ∈ ps, evaluate p.toExpr r₁ es₁ = evaluate p.toExpr r₂ es₂) :
  errorPolicies ps r₁ es₁ = errorPolicies ps r₂ es₂
```

`Cedar.Thm.isAuthorized_eq_of_satisfied_and_error_policies_eq` (theorem, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L108))

> `isAuthorized` depends only on the sets of forbid-satisfied, permit-satisfied,
> and erroring policies.

```lean
theorem isAuthorized_eq_of_satisfied_and_error_policies_eq
  {r₁ r₂ : Request} {es₁ es₂ : Entities} {ps₁ ps₂ : Policies}
  (hf : satisfiedPolicies .forbid ps₁ r₁ es₁ = satisfiedPolicies .forbid ps₂ r₂ es₂)
  (hp : satisfiedPolicies .permit ps₁ r₁ es₁ = satisfiedPolicies .permit ps₂ r₂ es₂)
  (he : errorPolicies ps₁ r₁ es₁ = errorPolicies ps₂ r₂ es₂) :
  isAuthorized r₁ es₁ ps₁ = isAuthorized r₂ es₂ ps₂
```

`Cedar.Thm.is_authorized_congr_evaluate` (theorem, [line 117](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L117))

```lean
theorem is_authorized_congr_evaluate {ps : Policies} {r₁ r₂ : Request} {es₁ es₂ : Entities}
  (heq : ∀ p ∈ ps, evaluate p.toExpr r₁ es₁ = evaluate p.toExpr r₂ es₂) :
  isAuthorized r₁ es₁ ps = isAuthorized r₂ es₂ ps
```

`Cedar.Thm.alternateErrorPolicies` (definition, [line 131](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L131))

> an alternate, proved-equivalent, definition of errorPolicies that's easier to prove things about

```lean
def alternateErrorPolicies (policies : Policies) (request : Request) (entities : Entities) : Set PolicyID
```

`Cedar.Thm.alternate_errorPolicies_equiv_errorPolicies` (theorem, [line 134](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L134))

```lean
theorem alternate_errorPolicies_equiv_errorPolicies (policies : Policies) (request : Request) (entities : Entities) :
  errorPolicies policies request entities = alternateErrorPolicies policies request entities
```

`Cedar.Thm.exists_hasError_of_mem_erroringPolicies` (theorem, [line 156](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L156))

```lean
theorem exists_hasError_of_mem_erroringPolicies {ps : Policies} {request : Request} {entities : Entities} {pid : PolicyID}
  (h : pid ∈ (isAuthorized request entities ps).erroringPolicies) :
  ∃ p ∈ ps, p.id = pid ∧ hasError p request entities = true
```

`Cedar.Thm.principal_eval_ok_means_principal_in_uid` (theorem, [line 166](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L166))

```lean
theorem principal_eval_ok_means_principal_in_uid {policy : Policy} {request : Request} {entities : Entities} {uid: EntityUID} :
  evaluate policy.principalScope.toExpr request entities = .ok true →
  policy.principalScope.scope.bound = .some uid →
  inₑ request.principal uid entities = true
```

`Cedar.Thm.resource_eval_ok_means_resource_in_uid` (theorem, [line 189](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L189))

```lean
theorem resource_eval_ok_means_resource_in_uid {policy : Policy} {request : Request} {entities : Entities} {uid : EntityUID} :
  evaluate policy.resourceScope.toExpr request entities = .ok true →
  policy.resourceScope.scope.bound = .some uid →
  inₑ request.resource uid entities = true
```

`Cedar.Thm.satisfied_implies_principal_scope` (theorem, [line 212](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L212))

```lean
theorem satisfied_implies_principal_scope {policy : Policy} {request : Request} {entities : Entities} {uid : EntityUID} :
  satisfied policy request entities = true →
  policy.principalScope.scope.bound = .some uid →
  inₑ request.principal uid entities = true
```

`Cedar.Thm.satisfied_implies_resource_scope` (theorem, [line 222](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L222))

```lean
theorem satisfied_implies_resource_scope {policy : Policy} {request : Request} {entities : Entities} {uid : EntityUID} :
  satisfied policy request entities = true →
  policy.resourceScope.scope.bound = .some uid →
  inₑ request.resource uid entities = true
```

`Cedar.Thm.mapM_evaluate_uids_produces_uids` (theorem, [line 235](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L235))

```lean
theorem mapM_evaluate_uids_produces_uids (list : List EntityUID) (request : Request) (entities : Entities) :
  List.mapM (evaluate · request entities) (list.map fun uid => Expr.lit (.entityUID uid)) =
  .ok (list.map (Value.prim ∘ Prim.entityUID))
```

`Cedar.Thm.asEntityUID_of_uid` (theorem, [line 243](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L243))

```lean
theorem asEntityUID_of_uid (uid : EntityUID) :
  Value.asEntityUID (.prim (.entityUID uid)) = .ok uid
```

`Cedar.Thm.mapM_asEntityUID_of_uid` (theorem, [line 250](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L250))

```lean
theorem mapM_asEntityUID_of_uid (uids : List EntityUID) :
  List.mapM Value.asEntityUID (uids.map (Value.prim ∘ Prim.entityUID)) = .ok uids
```

`Cedar.Thm.Except.isOk_iff_exists` (theorem, [line 264](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L264))

> Batteries has `Option.isSome_iff_exists`, but not this analogue for `Except`

```lean
theorem Except.isOk_iff_exists {x : Except ε α} :
  Except.isOk x ↔ ∃ a, x = .ok a
```

`Cedar.Thm.if_mapM_doesn't_fail_on_list_then_doesn't_fail_on_set` (theorem, [line 269](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L269))

```lean
theorem if_mapM_doesn't_fail_on_list_then_doesn't_fail_on_set [LT α] [DecidableLT α] [StrictLT α] {f : α → Except ε β} {xs : List α} :
  Except.isOk (xs.mapM f) →
  Except.isOk ((Set.elts (Set.make xs)).mapM f)
```

`Cedar.Thm.mapM_asEntityUID_on_set_uids_produces_ok` (theorem, [line 290](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L290))

```lean
theorem mapM_asEntityUID_on_set_uids_produces_ok (uids : List EntityUID) :
  Except.isOk (List.mapM
    Value.asEntityUID
    (Set.elts (Set.make (uids.map (Value.prim ∘ Prim.entityUID)))))
```

`Cedar.Thm.mapOrErr_value_asEntityUID_on_uids_produces_set` (theorem, [line 300](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L300))

```lean
theorem mapOrErr_value_asEntityUID_on_uids_produces_set (list : List EntityUID) (err : Error) :
  Set.mapOrErr Value.asEntityUID (Set.make (list.map (Value.prim ∘ Prim.entityUID))) err =
  .ok (Set.make list)
```

`Cedar.Thm.action_in_set_of_euids_produces_boolean` (theorem, [line 327](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L327))

```lean
theorem action_in_set_of_euids_produces_boolean (list : List EntityUID) (request : Request) (entities : Entities) :
  producesBool
    (Expr.binaryApp
      BinaryOp.mem
      (Expr.var .action)
      (Expr.set (list.map fun uid => Expr.lit (.entityUID uid))))
    request
    entities
```

`Cedar.Thm.principal_scope_produces_boolean` (theorem, [line 352](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L352))

> Lemma: evaluating the principalScope of any policy produces a boolean (and does not error)

```lean
theorem principal_scope_produces_boolean (policy : Policy) (request : Request) (entities : Entities) :
  producesBool policy.principalScope.toExpr request entities
```

`Cedar.Thm.action_scope_produces_boolean` (theorem, [line 370](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L370))

> Lemma: evaluating the actionScope of any policy produces a boolean (and does not error)

```lean
theorem action_scope_produces_boolean (policy : Policy) (request : Request) (entities : Entities) :
  producesBool policy.actionScope.toExpr request entities
```

`Cedar.Thm.resource_scope_produces_boolean` (theorem, [line 400](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L400))

> Lemma: evaluating the resourceScope of any policy produces a boolean (and does not error)

```lean
theorem resource_scope_produces_boolean (policy : Policy) (request : Request) (entities : Entities) :
  producesBool policy.resourceScope.toExpr request entities
```

`Cedar.Thm.produces_boolean_means_not_non_boolean` (theorem, [line 418](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L418))

> Lemma: if something produces a boolean, it does not produce a non-boolean

```lean
theorem produces_boolean_means_not_non_boolean {e : Expr} {request : Request} {entities : Entities} :
  producesBool e request entities → ¬ producesNonBool e request entities
```

`Cedar.Thm.principal_scope_does_not_throw` (theorem, [line 430](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L430))

```lean
theorem principal_scope_does_not_throw (policy : Policy) (request : Request) (entities : Entities) (err : Error) :
  ¬ (evaluate policy.principalScope.toExpr request entities = .error err)
```

`Cedar.Thm.action_scope_does_not_throw` (theorem, [line 437](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L437))

```lean
theorem action_scope_does_not_throw (policy : Policy) (request : Request) (entities : Entities) (err : Error) :
  ¬ (evaluate policy.actionScope.toExpr request entities = .error err)
```

`Cedar.Thm.resource_scope_does_not_throw` (theorem, [line 444](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L444))

```lean
theorem resource_scope_does_not_throw (policy : Policy) (request : Request) (entities : Entities) (err : Error) :
  ¬ (evaluate policy.resourceScope.toExpr request entities = .error err)
```

`Cedar.Thm.principal_scope_false_then_policy_false` (theorem, [line 451](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L451))

```lean
theorem principal_scope_false_then_policy_false {p : Policy}
  (hp: evaluate p.principalScope.toExpr req entities = .ok false) :
  evaluate p.toExpr req entities = .ok false
```

`Cedar.Thm.action_scope_false_then_policy_false` (theorem, [line 458](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L458))

```lean
theorem action_scope_false_then_policy_false {p : Policy}
  (ha: evaluate p.actionScope.toExpr req entities = .ok false) :
  evaluate p.toExpr req entities = .ok false
```

`Cedar.Thm.resource_scope_false_then_policy_false` (theorem, [line 467](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L467))

```lean
theorem resource_scope_false_then_policy_false {p : Policy}
  (hr : evaluate p.resourceScope.toExpr req entities = .ok false) :
  evaluate p.toExpr req entities = .ok false
```

`Cedar.Thm.error_implies_scope_satisfied` (theorem, [line 482](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L482))

> For a policy to throw an error, we must have at least gotten past the scope,
> so the scope constraints must have been satisfied.

```lean
theorem error_implies_scope_satisfied {policy : Policy} {request : Request} {entities : Entities} {err : Error} :
  evaluate policy.toExpr request entities = .error err →
  evaluate policy.principalScope.toExpr request entities = .ok true ∧
  evaluate policy.actionScope.toExpr request entities = .ok true ∧
  evaluate policy.resourceScope.toExpr request entities = .ok true
```

`Cedar.Thm.error_implies_principal_scope_in` (theorem, [line 551](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L551))

> For a policy to throw an error, we must have at least gotten past the scope,
> so the scope constraints must have been satisfied.

```lean
theorem error_implies_principal_scope_in {policy : Policy} {request : Request} {entities : Entities} {uid : EntityUID} {err : Error} :
  evaluate policy.toExpr request entities = .error err →
  policy.principalScope.scope.bound = .some uid →
  inₑ request.principal uid entities = true
```

`Cedar.Thm.error_implies_resource_scope_in` (theorem, [line 564](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean#L564))

> For a policy to throw an error, we must have at least gotten past the scope,
> so the scope constraints must have been satisfied.

```lean
theorem error_implies_resource_scope_in {policy : Policy} {request : Request} {entities : Entities} {uid : EntityUID} {err : Error} :
  evaluate policy.toExpr request entities = .error err →
  policy.resourceScope.scope.bound = .some uid →
  inₑ request.resource uid entities = true
```

## Depends on

- [Spec/Authorizer](../../spec/authorizer.md)
- [Authorization/Evaluator](evaluator.md)
- [Set properties](../data/set.md)

## Proof depends on

- [Thm/Data/LT](../data/lt.md)

## Sources

- [Cedar/Thm/Authorization/Authorizer.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Authorization/Authorizer.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Authorization.Authorizer.json)

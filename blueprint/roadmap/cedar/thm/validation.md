---
catalog: module
lean: Cedar.Thm.validation_is_sound, Cedar.Thm.validate_with_level_is_sound, Cedar.Thm.validate_with_level_no_dne, Cedar.Thm.error_of_mem_erroringPolicies, Cedar.Thm.validate_with_level_no_dne_response, Cedar.Thm.validation_is_sound_response
statement: formalized
proof: formalized
---

# Validation

`Cedar.Thm.Validation`, in [Cedar/Thm/Validation.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation.lean).

> This file contains the top-level correctness properties for the Cedar validator.
> We show that if validation succeeds for a set of policies, then for any request
> consistent with the schema, evaluating a policy in this set either produces a
> boolean value, or throws one of the errors in the set of valid errors.
> -

`Cedar.Thm.validation_is_sound` (theorem, [line 55](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation.lean#L55))

> If a set of policies is well-typed (valid) with respect to the schema according to the validator,
> and the input request and entities are consistent with the schema, then evaluating a policy in this set
> either produces a boolean value, or throws an error of type `entityDoesNotExist`, `extensionError`, or
> `arithBoundsError`. These errors cannot be protected against at validation time, as they depend on runtime
> information.

```lean
theorem validation_is_sound (policies : Policies) (schema : Schema) (request : Request) (entities : Entities) :
  schema.validateWellFormed = .ok () →
  validate policies schema = .ok () →
  validateRequest schema request = .ok () →
  validateEntities schema entities = .ok () →
  AllEvaluateToBool policies request entities
```

`Cedar.Thm.validate_with_level_is_sound` (theorem, [line 91](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation.lean#L91))

> If a set of policies is well-typed and validates at a level `n`, then any
> authorization request made using a slice of entities obtained by slicing at
> level `n` will return the same response as authorizing using the original
> entities.

```lean
theorem validate_with_level_is_sound {ps : Policies} {schema : Schema} {n : Nat} {request : Request} {entities : Entities}
  (hwf : schema.validateWellFormed = .ok ())
  (hr : validateRequest schema request = .ok ())
  (he : validateEntities schema entities = .ok ())
  (htl : validateWithLevel ps schema n = .ok ()) :
  isAuthorized request entities ps = isAuthorized request (entities.sliceAtLevel request n) ps
```

`Cedar.Thm.validate_with_level_no_dne` (theorem, [line 111](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation.lean#L111))

> End-to-end statement of issue #642 for a validated policy set, phrased over the
> *executable* closure check `Entities.closedAtLevel`: if `ps` validates at level
> `n` and the store passes `entities.closedAtLevel request n`, then no policy
> evaluates to `entityDoesNotExist`.  These are exactly the evaluations
> `isAuthorized` performs, so this is the per-policy guarantee `isAuthorized`
> inherits: the authorizer surfaces evaluation results only through the
> kind-agnostic `errorPolicies` / `satisfiedPolicies` and never raises
> `entityDoesNotExist` of its own.  Mirrors `validate_with_level_is_sound`, with the
> runtime closure obligation discharged by running `Entities.closedAtLevel`
> (`closedAtLevel_iff` bridges it to the `EntitiesClosedAtLevel` predicate).

```lean
theorem validate_with_level_no_dne {ps : Policies} {schema : Schema} {n : Nat} {request : Request} {entities : Entities}
  (hwf : schema.validateWellFormed = .ok ())
  (hr : validateRequest schema request = .ok ())
  (he : validateEntities schema entities = .ok ())
  (hcl : entities.closedAtLevel request n)
  (htl : validateWithLevel ps schema n = .ok ()) :
  ∀ p ∈ ps, evaluate p.toExpr request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.error_of_mem_erroringPolicies` (theorem, [line 129](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation.lean#L129))

> Bridge from `Response.erroringPolicies` membership back to the evaluator: if a
> policy id appears in the erroring set produced by `isAuthorized`, then some
> policy in `ps` with that id genuinely errored on evaluation.  Because policy ids
> need not be unique, this recovers *a* policy with the id, not necessarily a
> specific one.

```lean
theorem error_of_mem_erroringPolicies {ps : Policies} {request : Request} {entities : Entities} {pid : PolicyID}
  (h : pid ∈ (isAuthorized request entities ps).erroringPolicies) :
  ∃ p ∈ ps, p.id = pid ∧ ∃ e, evaluate p.toExpr request entities = .error e
```

`Cedar.Thm.validate_with_level_no_dne_response` (theorem, [line 144](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation.lean#L144))

> `Response`-level form of `validate_with_level_no_dne` (issue #642): for a policy
> set that validates at level `n` over a store closed at that level, no policy in
> the authorizer's `erroringPolicies` errored with `entityDoesNotExist`.  The
> `erroringPolicies` membership premise is not needed for soundness — *no* policy
> evaluates to `entityDoesNotExist` at all (`validate_with_level_no_dne`) — but it
> phrases the guarantee at the `isAuthorized` `Response` level.

```lean
theorem validate_with_level_no_dne_response {ps : Policies} {schema : Schema} {n : Nat} {request : Request} {entities : Entities}
  (hwf : schema.validateWellFormed = .ok ())
  (hr : validateRequest schema request = .ok ())
  (he : validateEntities schema entities = .ok ())
  (hcl : entities.closedAtLevel request n)
  (htl : validateWithLevel ps schema n = .ok ()) :
  ∀ p ∈ ps, p.id ∈ (isAuthorized request entities ps).erroringPolicies →
    evaluate p.toExpr request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.validation_is_sound_response` (theorem, [line 165](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation.lean#L165))

> `Response`-level form of `validation_is_sound`: for a validated policy set with
> unique policy ids, every policy in the authorizer's `erroringPolicies` errored
> with one of the three errors validation cannot rule out (`entityDoesNotExist`,
> `extensionError`, `arithBoundsError`).  Uniqueness of ids (`PolicyIdsUnique`, as
> in `determining_erroring_disjoint_when_unique_ids`) is required: an id in
> `erroringPolicies` only witnesses that *some* policy with that id errored, so
> without uniqueness it need not be the policy `p` quantified over.

```lean
theorem validation_is_sound_response (policies : Policies) (schema : Schema) (request : Request) (entities : Entities)
  (huniq : PolicyIdsUnique policies)
  (hwf : schema.validateWellFormed = .ok ())
  (hv : validate policies schema = .ok ())
  (hr : validateRequest schema request = .ok ())
  (he : validateEntities schema entities = .ok ()) :
  ∀ p ∈ policies, p.id ∈ (isAuthorized request entities policies).erroringPolicies →
    evaluate p.toExpr request entities = .error .entityDoesNotExist ∨
    evaluate p.toExpr request entities = .error .extensionError ∨
    evaluate p.toExpr request entities = .error .arithBoundsError
```

## Depends on

- [Spec/Slice](../spec/slice.md)
- [Authorization](authorization.md)
- [Thm/Validation/Validator](validation-2/validator.md)
- [EnvironmentValidator](../validation/environmentvalidator.md)
- [RequestEntityValidator](../validation/requestentityvalidator.md)

## Proof depends on

- [Thm/Validation/Levels](validation-2/levels.md)
- [RequestEntityValidation](validation-2/requestentityvalidation.md)

## Sources

- [Cedar/Thm/Validation.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Thm.Validation.json)

---
catalog: module
lean: Cedar.Thm.level_based_slicing_is_sound_expr, Cedar.Thm.typecheck_policy_with_level_is_sound, Cedar.Thm.typecheck_policy_with_level_no_dne_on_slice, Cedar.Thm.typecheck_policy_at_level_with_environments_is_sound, Cedar.Thm.validate_with_level_is_sound_wf, Cedar.Thm.typecheck_policy_at_level_with_environments_no_dne, Cedar.Thm.validate_with_level_no_dne_wf
statement: formalized
proof: formalized
---

# Thm/Validation/Levels

`Cedar.Thm.Validation.Levels`, in [Cedar/Thm/Validation/Levels.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels.lean).

`Cedar.Thm.level_based_slicing_is_sound_expr` (theorem, [line 53](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels.lean#L53))

```lean
theorem level_based_slicing_is_sound_expr {e : Expr} {n : Nat} {tx : TypedExpr} {c c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf e c env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n) :
  evaluate e request entities = evaluate e request (entities.sliceAtLevel request n)
```

`Cedar.Thm.typecheck_policy_with_level_is_sound` (theorem, [line 122](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels.lean#L122))

```lean
theorem typecheck_policy_with_level_is_sound {p : Policy} {tx : TypedExpr} {n : Nat} {env : TypeEnv} {request : Request} {entities : Entities}
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (htl : typecheckPolicyWithLevel p n env = .ok tx) :
  evaluate p.toExpr request entities = evaluate p.toExpr request (entities.sliceAtLevel request n)
```

`Cedar.Thm.typecheck_policy_with_level_no_dne_on_slice` (theorem, [line 147](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels.lean#L147))

> The sliced variant of `typecheck_policy_with_level_no_dne` (issue #642): evaluating
> a level-checked policy against the level-`n` *slice* of a closed store also never
> produces `entityDoesNotExist`.  Follows trivially by transporting the full-store
> result across the semantic-equivalence soundness theorem.

```lean
theorem typecheck_policy_with_level_no_dne_on_slice {p : Policy} {tx : TypedExpr} {n : Nat} {env : TypeEnv} {request : Request} {entities : Entities}
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (htl : typecheckPolicyWithLevel p n env = .ok tx) :
  evaluate p.toExpr request (entities.sliceAtLevel request n) ≠ .error .entityDoesNotExist
```

`Cedar.Thm.typecheck_policy_at_level_with_environments_is_sound` (theorem, [line 156](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels.lean#L156))

```lean
theorem typecheck_policy_at_level_with_environments_is_sound {p : Policy} {schema : Schema} {n : Nat} {request : Request} {entities : Entities}
  (he : ∃ env ∈ schema.environments, InstanceOfWellFormedEnvironment request entities env)
  (htl : typecheckPolicyWithEnvironments (typecheckPolicyWithLevel · n) p schema = .ok ()) :
  evaluate p.toExpr request entities = evaluate p.toExpr request (entities.sliceAtLevel request n)
```

`Cedar.Thm.validate_with_level_is_sound_wf` (theorem, [line 174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels.lean#L174))

```lean
theorem validate_with_level_is_sound_wf {ps : Policies} {schema : Schema} {n : Nat} {request : Request} {entities : Entities}
  (hwf : InstanceOfWellFormedSchema schema request entities)
  (htl : validateWithLevel ps schema n = .ok ()) :
  isAuthorized request entities ps = isAuthorized request (entities.sliceAtLevel request n) ps
```

`Cedar.Thm.typecheck_policy_at_level_with_environments_no_dne` (theorem, [line 191](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels.lean#L191))

> The `_no_dne` analogue of `typecheck_policy_at_level_with_environments_is_sound`:
> a policy that level-checks against every environment of the schema (and so, in
> particular, the one the request inhabits), evaluated against a store closed at
> that level, never produces `entityDoesNotExist`.

```lean
theorem typecheck_policy_at_level_with_environments_no_dne {p : Policy} {schema : Schema} {n : Nat} {request : Request} {entities : Entities}
  (he : ∃ env ∈ schema.environments, InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (htl : typecheckPolicyWithEnvironments (typecheckPolicyWithLevel · n) p schema = .ok ()) :
  evaluate p.toExpr request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.validate_with_level_no_dne_wf` (theorem, [line 219](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels.lean#L219))

> Validator-level statement of issue #642: if every policy in `ps` validates at
> level `n` and `entities` is closed at level `n` for the request, then no policy
> evaluates to an `entityDoesNotExist` error.  This is exactly the family of
> evaluations `isAuthorized` performs, so it is the closure guarantee `isAuthorized`
> inherits (the authorizer surfaces evaluation results only through the
> kind-agnostic `errorPolicies` / `satisfiedPolicies`, and never introduces a
> `entityDoesNotExist` of its own).  Mirrors `validate_with_level_is_sound_wf`.

```lean
theorem validate_with_level_no_dne_wf {ps : Policies} {schema : Schema} {n : Nat} {request : Request} {entities : Entities}
  (hwf : InstanceOfWellFormedSchema schema request entities)
  (hcl : EntitiesClosedAtLevel entities request n)
  (htl : validateWithLevel ps schema n = .ok ()) :
  ∀ p ∈ ps, evaluate p.toExpr request entities ≠ .error .entityDoesNotExist
```

## Depends on

- [Spec/Authorizer](../../spec/authorizer.md)
- [Level checking rules out `entityDoesNotExist` errors (issue #642)](levels-2/noentitieserror.md)
- [Thm/Validation/Validator](validator.md)

## Proof depends on

- [Authorization/Authorizer](../authorization-2/authorizer.md)
- [Levels/And](levels-2/and.md)
- [Levels/BinaryApp](levels-2/binaryapp.md)
- [Levels/Call](levels-2/call.md)
- [Levels/ExtHasAttr](levels-2/exthasattr.md)
- [Levels/GetAttr](levels-2/getattr.md)
- [Levels/HasAttr](levels-2/hasattr.md)
- [Levels/IfThenElse](levels-2/ifthenelse.md)
- [Levels/Or](levels-2/or.md)
- [Levels/Record](levels-2/record.md)
- [Levels/Set](levels-2/set.md)
- [Levels/UnaryApp](levels-2/unaryapp.md)

## Sources

- [Cedar/Thm/Validation/Levels.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Validation.Levels.json)

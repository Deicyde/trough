---
catalog: module
lean: Cedar.Thm.wellTypedPolicy_ok_implies_exists_typed_exprs, Cedar.Thm.wellTypedPolicy_ok_implies_well_typed_expr, Cedar.Thm.substitute_action_preserves_valid_refs, Cedar.Thm.wellTypedPolicy_preserves_valid_refs, Cedar.Thm.wellTypedPolicy_preserves_StronglyWellFormedForPolicy, Cedar.Thm.wellTypedPolicies_preserves_StronglyWellFormedForPolicies, Cedar.Thm.wellTypedPolicy_preserves_evaluation, Cedar.Thm.wellTypedPolicies_preserves_policy_id_and_effect, Cedar.Thm.wellTypedPolicies_preserves_satisfiedWithEffect, Cedar.Thm.wellTypedPolicies_preserves_satisfiedPolicies, Cedar.Thm.wellTypedPolicies_preserves_errored, Cedar.Thm.wellTypedPolicies_preserves_errorPolicies, Cedar.Thm.wellTypedPolicies_preserves_isAuthorized
statement: formalized
proof: formalized
---

# SymCC/WellTyped

`Cedar.Thm.SymCC.WellTyped`, in [Cedar/Thm/SymCC/WellTyped.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean).

> This file contains some results about `wellTypedPolicies` and `wellTypedPolicy`
> preserving the validity or results of some definitions (`StronglyWellFormedFor*`,
> `evaluate`, `isAuthorized`, etc.).

`Cedar.Thm.wellTypedPolicy_ok_implies_exists_typed_exprs` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean#L35))

> Reduces `wellTypedPolicy` being `ok` to the existence of `TypedExpr`s.

```lean
theorem wellTypedPolicy_ok_implies_exists_typed_exprs
  {Γ : TypeEnv} {p p' : Policy}
  (hwt : wellTypedPolicy p Γ = .ok p') :
  ∃ tx tx' : TypedExpr, ∃ c,
    TypedExpr.WellTyped Γ tx.liftBoolTypes ∧
    TypedExpr.WellTyped Γ tx' ∧
    typeOf (substituteAction Γ.reqty.action p.toExpr) ∅ Γ = Except.ok (tx, c) ∧
    p'.toExpr = tx'.toExpr ∧
    tx' =
      (TypedExpr.and (TypedExpr.lit (Prim.bool true) (.bool .anyBool))
      (TypedExpr.and (TypedExpr.lit (Prim.bool true) (.bool .anyBool))
      (TypedExpr.and (TypedExpr.lit (Prim.bool true) (.bool .anyBool))
        tx.liftBoolTypes
      (.bool .anyBool))
      (.bool .anyBool))
      (.bool .anyBool)) ∧
    tx.liftBoolTypes.typeOf = .bool .anyBool
```

`Cedar.Thm.wellTypedPolicy_ok_implies_well_typed_expr` (theorem, [line 123](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean#L123))

> If a policy `p` is well-typed via `wellTypedPolicy`, then there
> is a well-typed `TypedExpr` corresponding to `p`'s condition.

```lean
theorem wellTypedPolicy_ok_implies_well_typed_expr
  {Γ : TypeEnv} {p p' : Policy}
  (hwt : wellTypedPolicy p Γ = .ok p') :
  ∃ tx : TypedExpr,
    TypedExpr.WellTyped Γ tx ∧
    tx.toExpr = p'.toExpr
```

`Cedar.Thm.substitute_action_preserves_valid_refs` (theorem, [line 137](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean#L137))

> `wellTypedPolicy` preserves `Entities.ValidRefsFor`.

```lean
theorem substitute_action_preserves_valid_refs
  {Γ : TypeEnv} {request : Request} {entities : Entities} {expr : Expr}
  (hinst : InstanceOfWellFormedEnvironment request entities Γ) :
  entities.ValidRefsFor expr ↔ entities.ValidRefsFor (substituteAction request.action expr)
```

`Cedar.Thm.wellTypedPolicy_preserves_valid_refs` (theorem, [line 283](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean#L283))

> `wellTypedPolicy` preserves `Entities.ValidRefsFor`.

```lean
theorem wellTypedPolicy_preserves_valid_refs
  {Γ : TypeEnv} {request : Request} {entities : Entities} {p p' : Policy}
  (hinst : InstanceOfWellFormedEnvironment request entities Γ)
  (hwt : wellTypedPolicy p Γ = .ok p')
  (hswf : entities.ValidRefsFor p.toExpr) :
  entities.ValidRefsFor p'.toExpr
```

`Cedar.Thm.wellTypedPolicy_preserves_StronglyWellFormedForPolicy` (theorem, [line 309](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean#L309))

```lean
theorem wellTypedPolicy_preserves_StronglyWellFormedForPolicy
  {Γ : TypeEnv} {env : Env} {p p' : Policy}
  (hinst : InstanceOfWellFormedEnvironment env.request env.entities Γ)
  (hwt : wellTypedPolicy p Γ = .ok p')
  (hswf : env.StronglyWellFormedForPolicy p) :
  env.StronglyWellFormedForPolicy p'
```

`Cedar.Thm.wellTypedPolicies_preserves_StronglyWellFormedForPolicies` (theorem, [line 320](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean#L320))

```lean
theorem wellTypedPolicies_preserves_StronglyWellFormedForPolicies
  {Γ : TypeEnv} {env : Env} {ps ps' : Policies}
  (hinst : InstanceOfWellFormedEnvironment env.request env.entities Γ)
  (hwt : wellTypedPolicies ps Γ = .ok ps')
  (hswf : env.StronglyWellFormedForPolicies ps) :
  env.StronglyWellFormedForPolicies ps'
```

`Cedar.Thm.wellTypedPolicy_preserves_evaluation` (theorem, [line 342](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean#L342))

> `wellTypedPolicy` preserves the result of `evaluate`.

```lean
theorem wellTypedPolicy_preserves_evaluation
  {Γ : TypeEnv} {request : Request} {entities : Entities}
  {p p' : Policy}
  (hinst : InstanceOfWellFormedEnvironment request entities Γ)
  (hwt : wellTypedPolicy p Γ = .ok p') :
  evaluate p.toExpr request entities
  = evaluate p'.toExpr request entities
```

`Cedar.Thm.wellTypedPolicies_preserves_policy_id_and_effect` (theorem, [line 394](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean#L394))

```lean
theorem wellTypedPolicies_preserves_policy_id_and_effect
  {Γ : TypeEnv} {p p' : Policy}
  (hwt : wellTypedPolicy p Γ = .ok p') :
  p.id = p'.id ∧ p.effect = p'.effect
```

`Cedar.Thm.wellTypedPolicies_preserves_satisfiedWithEffect` (theorem, [line 405](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean#L405))

```lean
theorem wellTypedPolicies_preserves_satisfiedWithEffect
  {Γ : TypeEnv} {entities : Entities} {request : Request}
  {p p' : Policy}
  (effect : Effect)
  (hinst : InstanceOfWellFormedEnvironment request entities Γ)
  (hwt : wellTypedPolicy p Γ = .ok p') :
  satisfiedWithEffect effect p request entities
  = satisfiedWithEffect effect p' request entities
```

`Cedar.Thm.wellTypedPolicies_preserves_satisfiedPolicies` (theorem, [line 420](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean#L420))

```lean
theorem wellTypedPolicies_preserves_satisfiedPolicies
  {Γ : TypeEnv} {entities : Entities} {request : Request}
  {ps ps' : Policies}
  (effect : Effect)
  (hinst : InstanceOfWellFormedEnvironment request entities Γ)
  (hwt : wellTypedPolicies ps Γ = .ok ps') :
  satisfiedPolicies effect ps request entities
  = satisfiedPolicies effect ps' request entities
```

`Cedar.Thm.wellTypedPolicies_preserves_errored` (theorem, [line 444](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean#L444))

```lean
theorem wellTypedPolicies_preserves_errored
  {Γ : TypeEnv} {entities : Entities} {request : Request}
  {p p' : Policy}
  (hinst : InstanceOfWellFormedEnvironment request entities Γ)
  (hwt : wellTypedPolicy p Γ = .ok p') :
  errored p request entities
  = errored p' request entities
```

`Cedar.Thm.wellTypedPolicies_preserves_errorPolicies` (theorem, [line 457](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean#L457))

```lean
theorem wellTypedPolicies_preserves_errorPolicies
  {Γ : TypeEnv} {entities : Entities} {request : Request}
  {ps ps' : Policies}
  (hinst : InstanceOfWellFormedEnvironment request entities Γ)
  (hwt : wellTypedPolicies ps Γ = .ok ps') :
  errorPolicies ps request entities
  = errorPolicies ps' request entities
```

`Cedar.Thm.wellTypedPolicies_preserves_isAuthorized` (theorem, [line 479](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean#L479))

> `wellTypedPolicies` preserves the result of `isAuthorized`.

```lean
theorem wellTypedPolicies_preserves_isAuthorized
  {Γ : TypeEnv} {entities : Entities} {request : Request}
  {ps ps' : Policies}
  (hinst : InstanceOfWellFormedEnvironment request entities Γ)
  (hwt : wellTypedPolicies ps Γ = .ok ps') :
  isAuthorized request entities ps
  = isAuthorized request entities ps'
```

## Depends on

- [Spec/Authorizer](../../spec/authorizer.md)
- [SymCC](../../symcc-2.md)
- [Strongly well-formed ancestor relations](data/hierarchy.md)
- [Typechecker/Types](../validation-2/typechecker-2/types.md)
- [Expr/Definition](../welltyped/expr-2/definition.md)

## Proof depends on

- [ValidRefs](validrefs.md)
- [SubstituteAction](../validation-2/substituteaction.md)
- [Thm/Validation/Typechecker](../validation-2/typechecker.md)

## Sources

- [Cedar/Thm/SymCC/WellTyped.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/WellTyped.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.SymCC.WellTyped.json)

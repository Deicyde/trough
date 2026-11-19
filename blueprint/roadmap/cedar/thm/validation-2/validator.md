---
catalog: module
lean: Cedar.Thm.EvaluatesToBool, Cedar.Thm.AllEvaluateToBool, Cedar.Thm.InstanceOfWellFormedSchema, Cedar.Thm.action_matches_env, Cedar.Thm.typecheck_policy_produces_wt, Cedar.Thm.typecheck_policy_is_sound, Cedar.Thm.typecheck_policy_with_environments_is_sound
statement: formalized
proof: formalized
---

# Thm/Validation/Validator

`Cedar.Thm.Validation.Validator`, in [Cedar/Thm/Validation/Validator.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Validator.lean).

`Cedar.Thm.EvaluatesToBool` (definition, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Validator.lean#L38))

> For a single expression, evaluates to a boolean value (or appropriate error)

```lean
def EvaluatesToBool (expr : Expr) (request : Request) (entities : Entities) : Prop
```

`Cedar.Thm.AllEvaluateToBool` (definition, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Validator.lean#L42))

> Every policy as an expression evaluates to a boolean value or appropriate error

```lean
def AllEvaluateToBool (policies : Policies) (request : Request) (entities : Entities) : Prop
```

`Cedar.Thm.InstanceOfWellFormedSchema` (definition, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Validator.lean#L45))

```lean
def InstanceOfWellFormedSchema (schema : Schema) (request : Request) (entities : Entities) : Prop
```

`Cedar.Thm.action_matches_env` (theorem, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Validator.lean#L49))

```lean
theorem action_matches_env {env : TypeEnv} {request : Request} {entities : Entities} :
  InstanceOfWellFormedEnvironment request entities env →
  request.action = env.reqty.action
```

`Cedar.Thm.typecheck_policy_produces_wt` (theorem, [line 58](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Validator.lean#L58))

```lean
theorem typecheck_policy_produces_wt {policy : Policy} {Γ : TypeEnv} {tx : TypedExpr} :
  typecheckPolicy policy Γ = .ok tx →
  TypedExpr.WellTyped Γ tx.liftBoolTypes
```

`Cedar.Thm.typecheck_policy_is_sound` (theorem, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Validator.lean#L71))

```lean
theorem typecheck_policy_is_sound {policy : Policy} {env : TypeEnv} {tx : TypedExpr} {request : Request} {entities : Entities} :
  InstanceOfWellFormedEnvironment request entities env →
  typecheckPolicy policy env = .ok tx →
  ∃ b : Bool, EvaluatesTo policy.toExpr request entities b
```

`Cedar.Thm.typecheck_policy_with_environments_is_sound` (theorem, [line 90](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Validator.lean#L90))

```lean
theorem typecheck_policy_with_environments_is_sound (policy : Policy) (schema : Schema) (request : Request) (entities : Entities) :
  (∃ env ∈ schema.environments, InstanceOfWellFormedEnvironment request entities env) →
  typecheckPolicyWithEnvironments typecheckPolicy policy schema = .ok () →
  ∃ b : Bool, EvaluatesTo policy.toExpr request entities b
```

## Depends on

- [Typechecker/Basic](typechecker-2/basic.md)
- [Expr/Definition](../welltyped/expr-2/definition.md)
- [Cedar/Validation/Validator](../../validation/validator.md)

## Proof depends on

- [SubstituteAction](substituteaction.md)
- [Thm/Validation/Typechecker](typechecker.md)

## Sources

- [Cedar/Thm/Validation/Validator.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Validator.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Validation.Validator.json)

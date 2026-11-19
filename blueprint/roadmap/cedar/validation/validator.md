---
catalog: module
lean: Cedar.Validation.Schema.environments, Cedar.Validation.Schema.environmentsForAction?, Cedar.Validation.Schema.environment?, Cedar.Validation.ValidationError, Cedar.Validation.ValidationResult, Cedar.Validation.checkEntities, Cedar.Validation.mapOnVars, Cedar.Validation.substituteAction, Cedar.Validation.typecheckPolicy, Cedar.Validation.typecheckPolicyWithLevel, Cedar.Validation.allFalse, Cedar.Validation.typecheckPolicyWithEnvironments, Cedar.Validation.validate, Cedar.Validation.validateWithLevel, Cedar.Validation.validationErrorToJson
statement: formalized
proof: formalized
---

# Cedar/Validation/Validator

`Cedar.Validation.Validator`, in [Cedar/Validation/Validator.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean).

> This file defines the Cedar validator.

`Cedar.Validation.Schema.environments` (definition, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L46))

> Return every schema-defined environment.

```lean
public def Schema.environments (schema : Schema) : List TypeEnv
```

`Cedar.Validation.Schema.environmentsForAction?` (definition, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L63))

> Return all the schema-defined environments for a particular `action`, or
> `none` if this action is not declared in the schema.
>
> Note that `some ∅` means something different than `none` -- `some ∅` means
> that the `action` was declared in the schema, but there are no valid
> environments for it

```lean
public def Schema.environmentsForAction? (schema : Schema) (action : EntityUID) : Option (List TypeEnv)
```

`Cedar.Validation.Schema.environment?` (definition, [line 81](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L81))

> Return the environment for the particular (p,a,r) tuple, or `none` if this
> is not a valid tuple in this schema

```lean
public def Schema.environment? (schema : Schema) (principal resource : EntityType) (action : EntityUID) : Option TypeEnv
```

`Cedar.Validation.ValidationError` (inductive type, [line 96](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L96))

```lean
public inductive ValidationError where
  | typeError (pid : PolicyID) (error : TypeError)
  | levelError (pid : PolicyID)
  | impossiblePolicy (pid : PolicyID)
deriving Repr, BEq
```

`Cedar.Validation.ValidationResult` (abbreviation, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L108))

```lean
public abbrev ValidationResult
```

> Check that all referenced entity types, actions, and enum entities are declared
> in the schema.  The Lean model of typechecking _also_ does this check, but Rust
> does it only as a separate pass.  This means the Rust validator will report
> undefined entity types that the Lean typechecker ignores due to short-circuiting.
> We include this validation pass so that the validators behave exactly the same,
> but we don't need to prove anything about it for soundness.

`Cedar.Validation.checkEntities` (definition, [line 118](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L118))

```lean
public def checkEntities (schema : Schema) : Expr → Except TypeError Unit
```

`Cedar.Validation.mapOnVars` (definition, [line 150](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L150))

```lean
public def mapOnVars (f : Var → Expr) : Expr → Expr
```

`Cedar.Validation.substituteAction` (definition, [line 193](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L193))

```lean
public def substituteAction (uid : EntityUID) (expr : Expr) : Expr
```

`Cedar.Validation.typecheckPolicy` (definition, [line 201](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L201))

> Check that a policy is Boolean-typed.

```lean
public def typecheckPolicy (policy : Policy) (env : TypeEnv) : Except ValidationError TypedExpr
```

`Cedar.Validation.typecheckPolicyWithLevel` (definition, [line 210](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L210))

```lean
public def typecheckPolicyWithLevel (policy : Policy) (level : Nat) (env : TypeEnv) : Except ValidationError TypedExpr
```

`Cedar.Validation.allFalse` (definition, [line 217](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L217))

```lean
public def allFalse (txs : List TypedExpr) : Bool
```

`Cedar.Validation.typecheckPolicyWithEnvironments` (definition, [line 221](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L221))

> Check a policy under multiple environments.

```lean
public def typecheckPolicyWithEnvironments (tc : Policy → TypeEnv → Except ValidationError TypedExpr) (policy : Policy) (schema : Schema) : ValidationResult
```

`Cedar.Validation.validate` (definition, [line 230](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L230))

> Analyze a set of policies to check that all are boolean-typed, and that
> none are guaranteed to be false under all possible environments.

```lean
public def validate (policies : Policies) (schema : Schema) : ValidationResult
```

`Cedar.Validation.validateWithLevel` (definition, [line 237](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L237))

> Analyze a set of policies to check that all are boolean-typed, and that
> none are guaranteed to be false under all possible environments.

```lean
public def validateWithLevel (policies : Policies) (schema : Schema) (level : Nat) : ValidationResult
```

`Cedar.Validation.validationErrorToJson` (definition, [line 248](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean#L248))

```lean
public def validationErrorToJson : ValidationError → Lean.Json
```

## Depends on

- [Cedar/Validation/Levels](levels.md)

## Sources

- [Cedar/Validation/Validator.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Validator.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Validation.Validator.json)

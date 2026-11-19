---
catalog: module
lean: Cedar.Thm.typecheck, Cedar.Thm.typecheck_is_sound
statement: formalized
proof: formalized
---

# Thm/Typechecking

`Cedar.Thm.Typechecking`, in [Cedar/Thm/Typechecking.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Typechecking.lean).

> This file defines the top-level soundness property for the type checker.
> -

`Cedar.Thm.typecheck` (definition, [line 32](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Typechecking.lean#L32))

```lean
def typecheck (policy : Policy) (env : TypeEnv) : Except TypeError CedarType
```

`Cedar.Thm.typecheck_is_sound` (theorem, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Typechecking.lean#L47))

> If typechecking succeeds, then for any request consistent with the schema,
> either (1) evaluation produces a boolean or (2) it returns an error of type
> `entityDoesNotExist`, `extensionError`, or `arithBoundsError`. Both options are
> encoded in the `EvaluatesTo` predicate. The type checker cannot protect against
> these errors because it has no knowledge of the entities/context that will be
> provided at authorization time, and it does not reason about the semantics of
> arithmetic operators.

```lean
theorem typecheck_is_sound (policy : Policy) (env : TypeEnv) (t : CedarType) (request : Request) (entities : Entities) :
  InstanceOfWellFormedEnvironment request entities env →
  typecheck policy env = .ok t →
  (∃ (b : Bool), EvaluatesTo policy.toExpr request entities b)
```

## Depends on

- [Spec/Policy](../spec/policy.md)
- [Typechecker/Basic](validation-2/typechecker-2/basic.md)

## Proof depends on

- [Thm/Validation/Typechecker](validation-2/typechecker.md)

## Sources

- [Cedar/Thm/Typechecking.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Typechecking.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Thm.Typechecking.json)

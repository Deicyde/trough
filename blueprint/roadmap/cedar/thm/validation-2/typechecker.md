---
catalog: module
lean: Cedar.Thm.type_of_is_sound, Cedar.Thm.type_of_preserves_evaluation_results
statement: formalized
proof: formalized
---

# Thm/Validation/Typechecker

`Cedar.Thm.Validation.Typechecker`, in [Cedar/Thm/Validation/Typechecker.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker.lean).

> This file contains useful definitions and lemmas about the `Typechecker` functions.

`Cedar.Thm.type_of_is_sound` (theorem, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker.lean#L56))

> If an expression is well-typed according to the typechecker, and the input
> environment and capabilities satisfy some invariants, then either (1) evaluation
> produces a value of the returned type or (2) it returns an error of type
> `entityDoesNotExist`, `extensionError`, or `arithBoundsError`. Both options are
> encoded in the `EvaluatesTo` predicate.

```lean
theorem type_of_is_sound {e : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities} :
  CapabilitiesInvariant c₁ request entities →
  InstanceOfWellFormedEnvironment request entities env →
  typeOf e c₁ env = .ok (ty, c₂) →
  GuardedCapabilitiesInvariant e c₂ request entities ∧
  ∃ (v : Value), EvaluatesTo e request entities v ∧ InstanceOfType env v ty.typeOf
```

`Cedar.Thm.type_of_preserves_evaluation_results` (theorem, [line 118](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker.lean#L118))

> The type checker, if succeeds, should produce a typed expression that
> evaluates to the same result as the input expression.

```lean
theorem type_of_preserves_evaluation_results {e : Expr} {c₁ c₂ : Capabilities} {env : TypeEnv} {ty : TypedExpr} {request : Request} {entities : Entities} :
  CapabilitiesInvariant c₁ request entities →
  InstanceOfWellFormedEnvironment request entities env →
  typeOf e c₁ env = .ok (ty, c₂) →
  evaluate e request entities = evaluate ty.toExpr request entities
```

## Depends on

- [Typechecker/Basic](typechecker-2/basic.md)

## Proof depends on

- [Typechecker/And](typechecker-2/and.md)
- [Typechecker/BinaryApp](typechecker-2/binaryapp.md)
- [Typechecker/Call](typechecker-2/call.md)
- [Typechecker/ExtHasAttr](typechecker-2/exthasattr.md)
- [Typechecker/IfThenElse](typechecker-2/ifthenelse.md)
- [Typechecker/LitVar](typechecker-2/litvar.md)
- [Typechecker/Or](typechecker-2/or.md)
- [Typechecker/Record](typechecker-2/record.md)
- [Typechecker/Set](typechecker-2/set.md)
- [Typechecker/UnaryApp](typechecker-2/unaryapp.md)

## Sources

- [Cedar/Thm/Validation/Typechecker.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Typechecker.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Validation.Typechecker.json)

---
catalog: module
lean: Cedar.Thm.well_typed_is_sound
statement: formalized
proof: formalized
---

# WellTyped/Expr

`Cedar.Thm.WellTyped.Expr`, in [Cedar/Thm/WellTyped/Expr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr.lean).

> This file contains well-typedness theorems of `TypedExpr`

`Cedar.Thm.well_typed_is_sound` (theorem, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr.lean#L42))

> Successful evaluation of a well-typed expression should produce a value
> of corresponding type.

```lean
theorem well_typed_is_sound {ty : TypedExpr} {v : Value} {env : TypeEnv} {request : Request} {entities : Entities} :
  InstanceOfWellFormedEnvironment request entities env →
  TypedExpr.WellTyped env ty →
  evaluate ty.toExpr request entities = .ok v →
  InstanceOfType env v ty.typeOf
```

## Depends on

- [Spec/Evaluator](../../spec/evaluator.md)
- [Typechecker/Types](../validation-2/typechecker-2/types.md)
- [Expr/Definition](expr-2/definition.md)

## Proof depends on

- [Conversion](../tpe-2/conversion.md)
- [WellTyped/Residual](residual.md)

## Sources

- [Cedar/Thm/WellTyped/Expr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/WellTyped/Expr.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.WellTyped.Expr.json)

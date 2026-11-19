---
catalog: module
lean: Cedar.Thm.try_decide_residual₁_is_bool, Cedar.Thm.partial_eval_well_typed_unaryApp
statement: formalized
proof: formalized
---

# WellTyped/Unary

`Cedar.Thm.TPE.WellTyped.Unary`, in [Cedar/Thm/TPE/WellTyped/Unary.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Unary.lean).

`Cedar.Thm.try_decide_residual₁_is_bool` (theorem, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Unary.lean#L36))

> The reductions only ever decide a boolean.

```lean
theorem try_decide_residual₁_is_bool
  {op₁ : UnaryOp} {r : Residual} {v : Value}
  (hdec : TPE.tryDecideResidual₁ op₁ r = .some v) :
  ∃ b : Bool, v = .prim (.bool b)
```

`Cedar.Thm.partial_eval_well_typed_unaryApp` (theorem, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Unary.lean#L49))

> Helper theorem: Partial evaluation preserves well-typedness for unary application residuals.

```lean
theorem partial_eval_well_typed_unaryApp {env : TypeEnv} {op : UnaryOp} {expr : Residual} {ty : CedarType} {req : Request} {preq : PartialRequest} {es : Entities} {pes : PartialEntities} :
  Residual.WellTyped env (TPE.evaluate env expr preq pes) →
  PEWellTyped env (Residual.unaryApp op expr ty) (TPE.evaluate env (Residual.unaryApp op expr ty) preq pes) req preq es pes
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [WellTyped/Basic](basic.md)

## Proof depends on

- [Authorization/Authorizer](../../authorization-2/authorizer.md)
- [PreservesTypeOf](../preservestypeof.md)

## Sources

- [Cedar/Thm/TPE/WellTyped/Unary.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Unary.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.WellTyped.Unary.json)

---
catalog: module
lean: Cedar.Thm.ext_well_typed_after_map, Cedar.Thm.partial_eval_well_typed_call
statement: formalized
proof: formalized
---

# WellTyped/Call

`Cedar.Thm.TPE.WellTyped.Call`, in [Cedar/Thm/TPE/WellTyped/Call.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Call.lean).

`Cedar.Thm.ext_well_typed_after_map` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Call.lean#L35))

```lean
theorem ext_well_typed_after_map {xfn args ty env f} :
  ExtResidualWellTyped xfn args ty →
  (∀ arg, arg ∈ args → Residual.WellTyped env arg → Residual.WellTyped env (f arg)) →
  (∀ arg, arg ∈ args → (f arg).typeOf = arg.typeOf) →
  (∀ x, x.asValue.isSome → f x = x) →
  ExtResidualWellTyped xfn (args.map f) ty
```

`Cedar.Thm.partial_eval_well_typed_call` (theorem, [line 101](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Call.lean#L101))

```lean
theorem partial_eval_well_typed_call {env : TypeEnv} {xfn : ExtFun} {args : List Residual} {ty : CedarType} {req : Request} {preq : PartialRequest} {es : Entities} {pes : PartialEntities} :
  (∀ r ∈ args, Residual.WellTyped env (TPE.evaluate env r preq pes)) →
  PEWellTyped env (Residual.call xfn args ty) (TPE.evaluate env (Residual.call xfn args ty) preq pes) req preq es pes
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [WellTyped/Basic](basic.md)

## Proof depends on

- [PreservesTypeOf](../preservestypeof.md)
- [Typechecker/Call](../../validation-2/typechecker-2/call.md)

## Sources

- [Cedar/Thm/TPE/WellTyped/Call.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Call.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.WellTyped.Call.json)

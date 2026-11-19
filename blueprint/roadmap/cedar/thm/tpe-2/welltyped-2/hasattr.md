---
catalog: module
lean: Cedar.Thm.try_decide_has_residual_is_bool, Cedar.Thm.partial_eval_well_typed_hasAttr
statement: formalized
proof: formalized
---

# WellTyped/HasAttr

`Cedar.Thm.TPE.WellTyped.HasAttr`, in [Cedar/Thm/TPE/WellTyped/HasAttr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/HasAttr.lean).

`Cedar.Thm.try_decide_has_residual_is_bool` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/HasAttr.lean#L35))

> The reductions only ever decide a boolean.

```lean
theorem try_decide_has_residual_is_bool
  {env : TypeEnv} {r : Residual} {a : Attr} {v : Value}
  (hdec : TPE.tryDecideHasResidual env r a = .some v) :
  ∃ b : Bool, v = .prim (.bool b)
```

`Cedar.Thm.partial_eval_well_typed_hasAttr` (theorem, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/HasAttr.lean#L45))

```lean
theorem partial_eval_well_typed_hasAttr {env : TypeEnv} {expr : Residual} {attr : Attr} {ty : CedarType} {req : Request} {preq : PartialRequest} {es : Entities} {pes : PartialEntities} :
  Residual.WellTyped env (TPE.evaluate env expr preq pes) →
  PEWellTyped env (Residual.hasAttr expr attr ty) (TPE.evaluate env (Residual.hasAttr expr attr ty) preq pes) req preq es pes
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [WellTyped/Basic](basic.md)

## Proof depends on

- [PreservesTypeOf](../preservestypeof.md)

## Sources

- [Cedar/Thm/TPE/WellTyped/HasAttr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/HasAttr.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.WellTyped.HasAttr.json)

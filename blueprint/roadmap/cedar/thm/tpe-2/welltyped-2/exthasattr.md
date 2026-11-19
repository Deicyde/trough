---
catalog: module
lean: Cedar.Thm.partial_eval_well_typed_extHasAttr
statement: formalized
proof: formalized
---

# WellTyped/ExtHasAttr

`Cedar.Thm.TPE.WellTyped.ExtHasAttr`, in [Cedar/Thm/TPE/WellTyped/ExtHasAttr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/ExtHasAttr.lean).

`Cedar.Thm.partial_eval_well_typed_extHasAttr` (theorem, [line 188](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/ExtHasAttr.lean#L188))

```lean
theorem partial_eval_well_typed_extHasAttr {env : TypeEnv} {expr : Residual} {attr : Attr} {attrs : List Attr} {ty : CedarType} {req : Request} {preq : PartialRequest} {es : Entities} {pes : PartialEntities} :
  Residual.WellTyped env (TPE.evaluate env expr preq pes) →
  PEWellTyped env (Residual.extHasAttr expr attr attrs ty) (TPE.evaluate env (Residual.extHasAttr expr attr attrs ty) preq pes) req preq es pes
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [WellTyped/Basic](basic.md)

## Proof depends on

- [WellTyped/HasAttr](hasattr.md)

## Sources

- [Cedar/Thm/TPE/WellTyped/ExtHasAttr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/ExtHasAttr.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.WellTyped.ExtHasAttr.json)

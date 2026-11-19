---
catalog: module
lean: Cedar.Thm.partial_eval_well_typed_record
statement: formalized
proof: formalized
---

# WellTyped/Record

`Cedar.Thm.TPE.WellTyped.Record`, in [Cedar/Thm/TPE/WellTyped/Record.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Record.lean).

`Cedar.Thm.partial_eval_well_typed_record` (theorem, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Record.lean#L34))

```lean
theorem partial_eval_well_typed_record {env : TypeEnv} {ls : List (Attr × Residual)} {ty : CedarType} {req : Request} {preq : PartialRequest} {es : Entities} {pes : PartialEntities} :
  (∀ k v, (k, v) ∈ ls → Residual.WellTyped env (TPE.evaluate env v preq pes)) →
  PEWellTyped env (Residual.record ls ty) (TPE.evaluate env (Residual.record ls ty) preq pes) req preq es pes
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [WellTyped/Basic](basic.md)

## Proof depends on

- [PreservesTypeOf](../preservestypeof.md)

## Sources

- [Cedar/Thm/TPE/WellTyped/Record.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Record.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.WellTyped.Record.json)

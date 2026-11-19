---
catalog: module
lean: Cedar.Thm.partial_eval_well_typed_set
statement: formalized
proof: formalized
---

# WellTyped/Set

`Cedar.Thm.TPE.WellTyped.Set`, in [Cedar/Thm/TPE/WellTyped/Set.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Set.lean).

`Cedar.Thm.partial_eval_well_typed_set` (theorem, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Set.lean#L37))

> Helper theorem: Partial evaluation preserves well-typedness for set residuals.

```lean
theorem partial_eval_well_typed_set {env : TypeEnv} {ls : List Residual} {ty : CedarType} {req : Request} {preq : PartialRequest} {es : Entities} {pes : PartialEntities} :
  (∀ r ∈ ls, Residual.WellTyped env (TPE.evaluate env r preq pes)) →
  PEWellTyped env (Residual.set ls ty) (TPE.evaluate env (Residual.set ls ty) preq pes) req preq es pes
```

## Depends on

- [TPE/Evaluator](../../../tpe/evaluator.md)
- [WellTyped/Basic](basic.md)

## Proof depends on

- [Thm/Data/LT](../../data/lt.md)
- [PreservesTypeOf](../preservestypeof.md)

## Sources

- [Cedar/Thm/TPE/WellTyped/Set.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/WellTyped/Set.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.WellTyped.Set.json)

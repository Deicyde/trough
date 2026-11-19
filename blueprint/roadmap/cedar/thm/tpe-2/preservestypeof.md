---
catalog: module
lean: Cedar.Thm.PEPreservesTypeOf, Cedar.Thm.partial_eval_preserves_typeof
statement: formalized
proof: formalized
---

# PreservesTypeOf

`Cedar.Thm.TPE.PreservesTypeOf`, in [Cedar/Thm/TPE/PreservesTypeOf.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/PreservesTypeOf.lean).

`Cedar.Thm.PEPreservesTypeOf` (abbreviation, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/PreservesTypeOf.lean#L31))

```lean
abbrev PEPreservesTypeOf (res : Residual) : Prop
```

`Cedar.Thm.partial_eval_preserves_typeof` (theorem, [line 333](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/PreservesTypeOf.lean#L333))

> Theorem: TPE.evaluate env preserves the typeOf property.
>
> If a residual has a certain type, then partially evaluating it produces
> a residual with the same type.

```lean
theorem partial_eval_preserves_typeof :
  ∀ res, PEPreservesTypeOf res
```

## Depends on

- [TPE/Evaluator](../../tpe/evaluator.md)
- [Residual/Definition](../welltyped/residual-2/definition.md)

## Sources

- [Cedar/Thm/TPE/PreservesTypeOf.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/PreservesTypeOf.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.TPE.PreservesTypeOf.json)

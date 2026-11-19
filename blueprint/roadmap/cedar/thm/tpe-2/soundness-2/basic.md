---
catalog: module
lean: Cedar.Thm.asValue_some, Cedar.Thm.isError_true, Cedar.Thm.asValue_evaluate_val, Cedar.Thm.isError_evaluate_err
statement: formalized
proof: formalized
---

# Soundness/Basic

`Cedar.Thm.TPE.Soundness.Basic`, in [Cedar/Thm/TPE/Soundness/Basic.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Basic.lean).

> This file contains basic utility theorems used in the TPE soundness proof.

`Cedar.Thm.asValue_some` (theorem, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Basic.lean#L39))

```lean
theorem asValue_some {r : Residual} {v : Value} :
  r.asValue = .some v ↔ (∃ ty, r = .val v ty)
```

`Cedar.Thm.isError_true` (theorem, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Basic.lean#L49))

```lean
theorem isError_true {r : Residual} :
  r.isError ↔ (∃ ty, r = .error ty)
```

`Cedar.Thm.asValue_evaluate_val` (theorem, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Basic.lean#L59))

```lean
theorem asValue_evaluate_val {r : Residual} {v : Value} :
  r.asValue = .some v → ∀ req es, r.evaluate req es = Except.ok v
```

`Cedar.Thm.isError_evaluate_err` (theorem, [line 66](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Basic.lean#L66))

```lean
theorem isError_evaluate_err {r : Spec.Residual} :
  r.isError → ∀ req es, ∃ e, r.evaluate req es = .error e
```

## Depends on

- [TPE/Residual](../../../tpe/residual.md)

## Proof depends on

- [WellTyped/Binary](../welltyped-2/binary.md)
- [Residual/Soundness](../../welltyped/residual-2/soundness.md)

## Sources

- [Cedar/Thm/TPE/Soundness/Basic.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/Soundness/Basic.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.TPE.Soundness.Basic.json)

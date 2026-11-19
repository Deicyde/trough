---
catalog: module
lean: Cedar.Thm.value_type_bool_implies_bool, Cedar.Thm.verifyNeverErrors_wbeq, Cedar.Thm.verifyAlwaysMatches_wbeq, Cedar.Thm.verifyNeverMatches_wbeq
statement: formalized
proof: formalized
---

# VerifyEvaluateQueries

`Cedar.Thm.SymCC.Verifier.VerifyEvaluateQueries`, in [Cedar/Thm/SymCC/Verifier/VerifyEvaluateQueries.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluateQueries.lean).

> This file proves that `verifyEvaluate` queries are well-behaved.
> -

`Cedar.Thm.value_type_bool_implies_bool` (theorem, [line 27](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluateQueries.lean#L27))

```lean
theorem value_type_bool_implies_bool {v : Value} {t : Term} :
  v ∼ t → t.typeOf = .bool → ∃ b, v = .prim (.bool b)
```

`Cedar.Thm.verifyNeverErrors_wbeq` (theorem, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluateQueries.lean#L43))

```lean
theorem verifyNeverErrors_wbeq :
  WellBehavedEvaluateQuery isSome Except.isOk
```

`Cedar.Thm.verifyAlwaysMatches_wbeq` (theorem, [line 68](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluateQueries.lean#L68))

```lean
theorem verifyAlwaysMatches_wbeq :
  WellBehavedEvaluateQuery (eq · (⊙true)) (· == .ok true)
```

`Cedar.Thm.verifyNeverMatches_wbeq` (theorem, [line 114](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluateQueries.lean#L114))

```lean
theorem verifyNeverMatches_wbeq :
  WellBehavedEvaluateQuery (λ t => not (eq t (⊙true))) (· != .ok true)
```

## Depends on

- [VerifyEvaluate](verifyevaluate.md)

## Sources

- [Cedar/Thm/SymCC/Verifier/VerifyEvaluateQueries.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Verifier/VerifyEvaluateQueries.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Verifier.VerifyEvaluateQueries.json)

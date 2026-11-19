---
catalog: module
lean: Cedar.Thm.ofRecordType_as_map
statement: formalized
proof: formalized
---

# ofType

`Cedar.Thm.SymCC.Term.ofType`, in [Cedar/Thm/SymCC/Term/ofType.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/ofType.lean).

`Cedar.Thm.ofRecordType_as_map` (theorem, [line 25](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/ofType.lean#L25))

> Rephrases `ofRecordType` with map

```lean
theorem ofRecordType_as_map (rty : List (Attr × QualifiedType)) :
  TermType.ofRecordType rty
  = rty.map λ (a, qty) => (a, TermType.ofQualifiedType qty)
```

## Depends on

- [TermType](../../../symcc/part-02/termtype.md)

## Sources

- [Cedar/Thm/SymCC/Term/ofType.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Term/ofType.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Term.ofType.json)

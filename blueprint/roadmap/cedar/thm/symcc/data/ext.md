---
catalog: module
lean: Cedar.Thm.toDate_eq_smod
statement: formalized
proof: formalized
---

# Extension function rewriting lemmas

`Cedar.Thm.SymCC.Data.Ext`, in [Cedar/Thm/SymCC/Data/Ext.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Ext.lean).

> This file contains lemmas that rewrite Cedar extension function definitions
> into equivalent forms that are easier to reason about in SymCC proofs.

`Cedar.Thm.toDate_eq_smod` (theorem, [line 66](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Ext.lean#L66))

> Equivalent formulation of `toDate` using `Int64.smod`, useful for symbolic compilation.

```lean
public theorem toDate_eq_smod (datetime : Spec.Ext.Datetime) :
  toDate datetime =
  let millisPerDayI64 := Int64.ofIntChecked MILLISECONDS_PER_DAY (by decide)
  datetime? (datetime.val - Int64.smod datetime.val millisPerDayI64)
```

## Depends on

- [Datetime](../../../spec/ext-2/datetime.md)

## Sources

- [Cedar/Thm/SymCC/Data/Ext.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Data/Ext.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Data.Ext.json)

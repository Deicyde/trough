---
catalog: module
lean: Cedar.Thm.Datetime.parse_eq_some_iff_isDatetimeValue, Cedar.Thm.Datetime.bind_parse_toString?
statement: formalized
proof: formalized
---

# Derived datetime parser corollaries

`Cedar.Thm.Ext.Datetime.Corollaries`, in [Cedar/Thm/Ext/Datetime/Corollaries.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Corollaries.lean).

`Cedar.Thm.Datetime.parse_eq_some_iff_isDatetimeValue` (theorem, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Corollaries.lean#L30))

> Exact parser characterization derived from soundness and completeness: parsing succeeds with
> `d` precisely when the declarative grammar relation assigns the input the value
> `d.val.toInt`.

```lean
public theorem parse_eq_some_iff_isDatetimeValue (str : String) (d : Datetime) :
    Datetime.parse str = some d ↔ IsDatetimeValue str d.val.toInt
```

`Cedar.Thm.Datetime.bind_parse_toString?` (theorem, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Corollaries.lean#L35))

> Total `Option` formulation of the partial serialization roundtrip.

```lean
public theorem bind_parse_toString? (d : Datetime) :
    (toString? d).bind Datetime.parse = (toString? d).map (fun _ => d)
```

## Depends on

- [Datetime grammar: definitions](grammar.md)

## Proof depends on

- [Datetime parser correctness](../datetime.md)

## Sources

- [Cedar/Thm/Ext/Datetime/Corollaries.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Corollaries.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Ext.Datetime.Corollaries.json)

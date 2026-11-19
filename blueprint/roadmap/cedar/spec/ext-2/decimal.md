---
catalog: module
lean: Cedar.Spec.Ext.DECIMAL_DIGITS, Cedar.Spec.Ext.Decimal, Cedar.Spec.Ext.Decimal.decimal?, Cedar.Spec.Ext.Decimal.parse, Cedar.Spec.Ext.Decimal.decimal
statement: formalized
proof: formalized
---

# Spec/Ext/Decimal

`Cedar.Spec.Ext.Decimal`, in [Cedar/Spec/Ext/Decimal.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Decimal.lean).

> This file defines Cedar decimal values and functions.

`Cedar.Spec.Ext.DECIMAL_DIGITS` (abbreviation, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Decimal.lean#L36))

> A decimal number consists of an integer part and a fractional part.
> The former is the integer number before the decimal point.
> The latter is the decimal number minus its integer part.
> For instance, 10.234 is a decimal number. Its integer part is 10 and its fractional part is 0.234
> We restrict the number of the digits after the decimal point to 4.

```lean
public abbrev DECIMAL_DIGITS : Nat
```

`Cedar.Spec.Ext.Decimal` (abbreviation, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Decimal.lean#L38))

```lean
public abbrev Decimal
```

`Cedar.Spec.Ext.Decimal.decimal?` (definition, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Decimal.lean#L45))

> Create a `Decimal` from an `Int` representing its internal encoding. Most callers should use higher-level constructors, e.g., `Decimal.parse`

```lean
public def decimal? (i : Int) : Option Decimal
```

`Cedar.Spec.Ext.Decimal.parse` (definition, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Decimal.lean#L48))

```lean
public def parse (str : String) : Option Decimal
```

`Cedar.Spec.Ext.Decimal.decimal` (abbreviation, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Decimal.lean#L79))

```lean
public abbrev decimal
```

## Depends on

- [Int64](../../data/int64.md)
- [Ext/Util](util.md)

## Sources

- [Cedar/Spec/Ext/Decimal.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Decimal.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Spec.Ext.Decimal.json)

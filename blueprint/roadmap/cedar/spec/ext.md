---
catalog: module
lean: Cedar.Spec.IPAddr, Cedar.Spec.Duration, Cedar.Spec.Ext, Cedar.Spec.Ext.lt, Cedar.Spec.Ext.decLt
statement: formalized
proof: formalized
---

# Ext

`Cedar.Spec.Ext`, in [Cedar/Spec/Ext.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext.lean).

> This file defines Cedar extension values.

`Cedar.Spec.IPAddr` (abbreviation, [line 29](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext.lean#L29))

```lean
public abbrev IPAddr
```

`Cedar.Spec.Duration` (abbreviation, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext.lean#L30))

```lean
public abbrev Duration
```

`Cedar.Spec.Ext` (inductive type, [line 32](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext.lean#L32))

```lean
public inductive Ext where
  | decimal (d : Ext.Decimal)
  | ipaddr (ip : IPAddr)
  | datetime (dt : Ext.Datetime)
  | duration (dur: Duration)
```

`Cedar.Spec.Ext.lt` (definition, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext.lean#L39))

> Ordering on extension types: .decimal < .ipaddr < .datetime < .duration

```lean
public def Ext.lt : Ext → Ext → Bool
```

`Cedar.Spec.Ext.decLt` (instance, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext.lean#L57))

```lean
public instance Ext.decLt (x y : Ext) : Decidable (x < y)
```

## Depends on

- [Datetime](ext-2/datetime.md)
- [Spec/Ext/Decimal](ext-2/decimal.md)
- [IPAddr](ext-2/ipaddr.md)

## Sources

- [Cedar/Spec/Ext.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Spec.Ext.json)

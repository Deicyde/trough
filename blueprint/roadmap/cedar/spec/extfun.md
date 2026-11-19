---
catalog: module
lean: Cedar.Spec.ExtFun, Cedar.Spec.res, Cedar.Spec.call
statement: formalized
proof: formalized
---

# Spec/ExtFun

`Cedar.Spec.ExtFun`, in [Cedar/Spec/ExtFun.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/ExtFun.lean).

> This file defines Cedar extension functions.

`Cedar.Spec.ExtFun` (inductive type, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/ExtFun.lean#L30))

```lean
public inductive ExtFun where
  | decimal             ----- Decimal functions -----
  | lessThan
  | lessThanOrEqual
  | greaterThan
  | greaterThanOrEqual
  | ip                  ----- IpAddr functions -----
  | isIpv4
  | isIpv6
  | isLoopback
  | isMulticast
  | isInRange
  | datetime            ----- Datetime functions -----
  | duration
  | offset
  | durationSince
  | toDate
  | toTime
  | toMilliseconds
  | toSeconds
  | toMinutes
  | toHours
  | toDays
```

`Cedar.Spec.res` (definition, [line 55](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/ExtFun.lean#L55))

```lean
public def res {α} [Coe α Ext] : Option α → Result Value
```

`Cedar.Spec.call` (definition, [line 60](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/ExtFun.lean#L60))

```lean
public def call : ExtFun → List Value → Result Value
```

## Depends on

- [Value](value.md)

## Sources

- [Cedar/Spec/ExtFun.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/ExtFun.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Spec.ExtFun.json)

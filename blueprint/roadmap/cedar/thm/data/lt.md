---
catalog: module
lean: Cedar.Thm.IPNetPrefix.strictLT, Cedar.Thm.CIDR.strictLT, Cedar.Thm.IPNet.strictLT, Cedar.Thm.Datetime.strictLT, Cedar.Thm.Duration.strictLT, Cedar.Thm.Ext.strictLT, Cedar.Thm.Name.strictLT, Cedar.Thm.EntityUID.strictLT, Cedar.Thm.Prim.strictLT, Cedar.Thm.Value.strictLT
statement: formalized
proof: formalized
---

# Thm/Data/LT

`Cedar.Thm.Data.LT`, in [Cedar/Thm/Data/LT.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/LT.lean).

> This file contains proofs that the less-than (`<`) relation on Cedar values is strict.

`Cedar.Thm.IPNetPrefix.strictLT` (instance, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/LT.lean#L39))

```lean
public instance IPNetPrefix.strictLT {w} : StrictLT (Ext.IPAddr.IPNetPrefix w)
```

`Cedar.Thm.CIDR.strictLT` (instance, [line 66](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/LT.lean#L66))

```lean
public instance CIDR.strictLT {w} : StrictLT (Ext.IPAddr.CIDR w)
```

`Cedar.Thm.IPNet.strictLT` (instance, [line 106](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/LT.lean#L106))

```lean
public instance IPNet.strictLT : StrictLT Ext.IPAddr.IPNet
```

`Cedar.Thm.Datetime.strictLT` (instance, [line 131](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/LT.lean#L131))

```lean
public instance Datetime.strictLT : StrictLT Ext.Datetime
```

`Cedar.Thm.Duration.strictLT` (instance, [line 152](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/LT.lean#L152))

```lean
public instance Duration.strictLT : StrictLT Ext.Datetime.Duration
```

`Cedar.Thm.Ext.strictLT` (instance, [line 173](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/LT.lean#L173))

```lean
public instance Ext.strictLT : StrictLT Ext
```

`Cedar.Thm.Name.strictLT` (instance, [line 237](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/LT.lean#L237))

```lean
public instance Name.strictLT : StrictLT Name
```

`Cedar.Thm.EntityUID.strictLT` (instance, [line 314](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/LT.lean#L314))

```lean
public instance EntityUID.strictLT : StrictLT EntityUID
```

`Cedar.Thm.Prim.strictLT` (instance, [line 351](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/LT.lean#L351))

```lean
public instance Prim.strictLT : StrictLT Prim
```

`Cedar.Thm.Value.strictLT` (instance, [line 622](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/LT.lean#L622))

```lean
public instance Value.strictLT : StrictLT Value
```

## Depends on

- [Value](../../spec/value.md)

## Sources

- [Cedar/Thm/Data/LT.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Data/LT.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Data.LT.json)

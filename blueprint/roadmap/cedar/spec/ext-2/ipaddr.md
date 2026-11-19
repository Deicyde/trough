---
catalog: module
lean: Cedar.Spec.Ext.IPAddr.ADDR_SIZE, Cedar.Spec.Ext.IPAddr.V4_WIDTH, Cedar.Spec.Ext.IPAddr.V6_WIDTH, Cedar.Spec.Ext.IPAddr.IPNetAddr, Cedar.Spec.Ext.IPAddr.IPv4Addr, Cedar.Spec.Ext.IPAddr.IPv4Addr.mk, Cedar.Spec.Ext.IPAddr.IPv6Addr, Cedar.Spec.Ext.IPAddr.IPv6Addr.mk, Cedar.Spec.Ext.IPAddr.IPNetPrefix, Cedar.Spec.Ext.IPAddr.IPv4Prefix, Cedar.Spec.Ext.IPAddr.IPv6Prefix, Cedar.Spec.Ext.IPAddr.IPNetPrefix.toNat, Cedar.Spec.Ext.IPAddr.CIDR, Cedar.Spec.Ext.IPAddr.CIDR.subnetWidth, Cedar.Spec.Ext.IPAddr.CIDR.range, Cedar.Spec.Ext.IPAddr.CIDR.inRange, Cedar.Spec.Ext.IPAddr.IPNet, Cedar.Spec.Ext.IPAddr.IPNet.isV4, Cedar.Spec.Ext.IPAddr.IPNet.isV6, Cedar.Spec.Ext.IPAddr.IPNet.inRange, Cedar.Spec.Ext.IPAddr.LOOP_BACK_CIDR_V4, Cedar.Spec.Ext.IPAddr.LOOP_BACK_CIDR_V6, Cedar.Spec.Ext.IPAddr.MULTICAST_CIDR_V4, Cedar.Spec.Ext.IPAddr.MULTICAST_CIDR_V6, Cedar.Spec.Ext.IPAddr.IPNet.isLoopback, Cedar.Spec.Ext.IPAddr.IPNet.isMulticast, Cedar.Spec.Ext.IPAddr.ip, Cedar.Spec.Ext.IPAddr.IPNetPrefix.lt, Cedar.Spec.Ext.IPAddr.IPNetPrefix.decLt, Cedar.Spec.Ext.IPAddr.CIDR.lt, Cedar.Spec.Ext.IPAddr.CIDR.decLt, Cedar.Spec.Ext.IPAddr.IPNet.lt, Cedar.Spec.Ext.IPAddr.IPNet.decLt, Cedar.Spec.Ext.IPAddr.toHex
statement: formalized
proof: formalized
---

# IPAddr

`Cedar.Spec.Ext.IPAddr`, in [Cedar/Spec/Ext/IPAddr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean).

> This file defines Cedar IpAddr values and functions.

`Cedar.Spec.Ext.IPAddr.ADDR_SIZE` (abbreviation, [line 31](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L31))

```lean
public abbrev ADDR_SIZE (w : Nat)
```

`Cedar.Spec.Ext.IPAddr.V4_WIDTH` (abbreviation, [line 33](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L33))

```lean
public abbrev V4_WIDTH
```

`Cedar.Spec.Ext.IPAddr.V6_WIDTH` (abbreviation, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L34))

```lean
public abbrev V6_WIDTH
```

`Cedar.Spec.Ext.IPAddr.IPNetAddr` (abbreviation, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L38))

```lean
public abbrev IPNetAddr (w : Nat)
```

`Cedar.Spec.Ext.IPAddr.IPv4Addr` (abbreviation, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L45))

> IPv4 address: a 32 bit number partitioned into 4 groups. a0 is most signifcant
> and a3 is the least significant. In other words, the number represented is
> a0++a1++a2++a3.
> -

```lean
public abbrev IPv4Addr
```

`Cedar.Spec.Ext.IPAddr.IPv4Addr.mk` (definition, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L47))

```lean
public def IPv4Addr.mk (a₀ a₁ a₂ a₃ : BitVec 8) : IPv4Addr
```

`Cedar.Spec.Ext.IPAddr.IPv6Addr` (abbreviation, [line 55](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L55))

> IPv6 address: a 128 bit number partitioned into 8 groups. a0 is most signifcant
> and a7 is the least significant. In other words, the number represented is
> a0++a1++a2++a3++a4++a5++a6++a7.
> -

```lean
public abbrev IPv6Addr
```

`Cedar.Spec.Ext.IPAddr.IPv6Addr.mk` (definition, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L57))

```lean
public def IPv6Addr.mk (a₀ a₁ a₂ a₃ a₄ a₅ a₆ a₇ : BitVec 16) : IPv6Addr
```

`Cedar.Spec.Ext.IPAddr.IPNetPrefix` (abbreviation, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L62))

```lean
public abbrev IPNetPrefix (n : Nat)
```

`Cedar.Spec.Ext.IPAddr.IPv4Prefix` (abbreviation, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L63))

```lean
public abbrev IPv4Prefix
```

`Cedar.Spec.Ext.IPAddr.IPv6Prefix` (abbreviation, [line 64](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L64))

```lean
public abbrev IPv6Prefix
```

`Cedar.Spec.Ext.IPAddr.IPNetPrefix.toNat` (definition, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L69))

```lean
public def IPNetPrefix.toNat {w} : IPNetPrefix w → Nat
```

`Cedar.Spec.Ext.IPAddr.CIDR` (structure, [line 82](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L82))

```lean
public structure CIDR (w : Nat) where
  addr : IPNetAddr w
  pre  : IPNetPrefix w  -- We use "pre" because "prefix" is a keyword in Lean
```

`Cedar.Spec.Ext.IPAddr.CIDR.subnetWidth` (definition, [line 86](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L86))

```lean
public def CIDR.subnetWidth {w} (cidr : CIDR w) : BitVec (ADDR_SIZE w)
```

`Cedar.Spec.Ext.IPAddr.CIDR.range` (definition, [line 92](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L92))

```lean
public def CIDR.range {w} (cidr : CIDR w) : (IPNetAddr w) × (IPNetAddr w)
```

`Cedar.Spec.Ext.IPAddr.CIDR.inRange` (definition, [line 99](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L99))

```lean
public def CIDR.inRange {w} (cidr₁ cidr₂ : CIDR w) : Bool
```

`Cedar.Spec.Ext.IPAddr.IPNet` (inductive type, [line 104](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L104))

```lean
public inductive IPNet where
  | V4 : CIDR V4_WIDTH → IPNet
  | V6 : CIDR V6_WIDTH → IPNet
```

`Cedar.Spec.Ext.IPAddr.IPNet.isV4` (definition, [line 109](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L109))

```lean
public def IPNet.isV4 : IPNet → Bool
```

`Cedar.Spec.Ext.IPAddr.IPNet.isV6` (definition, [line 114](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L114))

```lean
public def IPNet.isV6 : IPNet → Bool
```

`Cedar.Spec.Ext.IPAddr.IPNet.inRange` (definition, [line 118](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L118))

```lean
public def IPNet.inRange : IPNet → IPNet → Bool
```

`Cedar.Spec.Ext.IPAddr.LOOP_BACK_CIDR_V4` (definition, [line 125](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L125))

```lean
public def LOOP_BACK_CIDR_V4
```

`Cedar.Spec.Ext.IPAddr.LOOP_BACK_CIDR_V6` (definition, [line 126](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L126))

```lean
public def LOOP_BACK_CIDR_V6
```

`Cedar.Spec.Ext.IPAddr.MULTICAST_CIDR_V4` (definition, [line 130](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L130))

```lean
public def MULTICAST_CIDR_V4
```

`Cedar.Spec.Ext.IPAddr.MULTICAST_CIDR_V6` (definition, [line 131](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L131))

```lean
public def MULTICAST_CIDR_V6
```

`Cedar.Spec.Ext.IPAddr.IPNet.isLoopback` (definition, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L133))

```lean
public def IPNet.isLoopback : IPNet → Bool
```

`Cedar.Spec.Ext.IPAddr.IPNet.isMulticast` (definition, [line 137](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L137))

```lean
public def IPNet.isMulticast : IPNet → Bool
```

`Cedar.Spec.Ext.IPAddr.ip` (definition, [line 237](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L237))

```lean
public def ip (str : String) : Option IPNet
```

`Cedar.Spec.Ext.IPAddr.IPNetPrefix.lt` (definition, [line 244](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L244))

```lean
public def IPNetPrefix.lt {w} (p₁ p₂ : IPNetPrefix w) : Bool
```

`Cedar.Spec.Ext.IPAddr.IPNetPrefix.decLt` (instance, [line 250](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L250))

```lean
public instance IPNetPrefix.decLt {w} (d₁ d₂ : IPNetPrefix w) : Decidable (d₁ < d₂)
```

`Cedar.Spec.Ext.IPAddr.CIDR.lt` (definition, [line 253](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L253))

```lean
public def CIDR.lt {w} (cidr₁ cidr₂ : CIDR w) : Bool
```

`Cedar.Spec.Ext.IPAddr.CIDR.decLt` (instance, [line 259](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L259))

```lean
public instance CIDR.decLt {w} (d₁ d₂ : CIDR w) : Decidable (d₁ < d₂)
```

`Cedar.Spec.Ext.IPAddr.IPNet.lt` (definition, [line 262](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L262))

```lean
public def IPNet.lt : IPNet → IPNet → Bool
```

`Cedar.Spec.Ext.IPAddr.IPNet.decLt` (instance, [line 271](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L271))

```lean
public instance IPNet.decLt (d₁ d₂ : IPNet) : Decidable (d₁ < d₂)
```

`Cedar.Spec.Ext.IPAddr.toHex` (definition, [line 275](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean#L275))

```lean
public def toHex (n : Nat) : String
```

## Depends on

Its statements use no other Cedar module's declarations.

## Proof depends on

- [Ext/Util](util.md)

## Sources

- [Cedar/Spec/Ext/IPAddr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/IPAddr.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Spec.Ext.IPAddr.json)

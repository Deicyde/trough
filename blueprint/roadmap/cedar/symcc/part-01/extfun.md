---
catalog: module
lean: Cedar.SymCC.Decimal.lessThan, Cedar.SymCC.Decimal.lessThanOrEqual, Cedar.SymCC.Decimal.greaterThan, Cedar.SymCC.Decimal.greaterThanOrEqual, Cedar.SymCC.IPAddr.isIpv4, Cedar.SymCC.IPAddr.isIpv6, Cedar.SymCC.IPAddr.subnetWidth, Cedar.SymCC.IPAddr.range, Cedar.SymCC.IPAddr.rangeV4, Cedar.SymCC.IPAddr.rangeV6, Cedar.SymCC.IPAddr.inRange, Cedar.SymCC.IPAddr.inRangeV, Cedar.SymCC.IPAddr.isInRange, Cedar.SymCC.IPAddr.inRangeVs, Cedar.SymCC.IPAddr.isInRangeV, Cedar.SymCC.IPAddr.ipTerm, Cedar.SymCC.IPAddr.inRangeLit, Cedar.SymCC.IPAddr.isLoopback, Cedar.SymCC.IPAddr.isMulticast, Cedar.SymCC.Duration.toMilliseconds, Cedar.SymCC.Duration.toSeconds, Cedar.SymCC.Duration.toMinutes, Cedar.SymCC.Duration.toHours, Cedar.SymCC.Duration.toDays, Cedar.SymCC.Datetime.offset, Cedar.SymCC.Datetime.durationSince, Cedar.SymCC.Datetime.toDate, Cedar.SymCC.Datetime.toTime
statement: formalized
proof: formalized
---

# SymCC/ExtFun

`Cedar.SymCC.ExtFun`, in [Cedar/SymCC/ExtFun.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean).

> This file contains the symbolic encoding (factory functions) for extension
> operators.
>
> The extension functions are total. If given well-formed and type-correct
> arguments, an extension function will return a well-formed and type-correct
> output. Otherwise, the output is an arbitrary term.
>
> This design lets us minimize the number of error paths in the overall
> specification of symbolic compilation, which makes for nicer code and proofs, and
> it more closely tracks the specification of the concrete evaluator.
>
> See `Compiler.lean` to see how the symbolic compiler uses this API. See also
> `Factory.lean`.

`Cedar.SymCC.Decimal.lessThan` (definition, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L50))

```lean
public def lessThan (t₁ t₂ : Term) : Term
```

`Cedar.SymCC.Decimal.lessThanOrEqual` (definition, [line 53](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L53))

```lean
public def lessThanOrEqual (t₁ t₂ : Term) : Term
```

`Cedar.SymCC.Decimal.greaterThan` (definition, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L56))

```lean
public def greaterThan (t₁ t₂ : Term) : Term
```

`Cedar.SymCC.Decimal.greaterThanOrEqual` (definition, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L59))

```lean
public def greaterThanOrEqual (t₁ t₂ : Term) : Term
```

`Cedar.SymCC.IPAddr.isIpv4` (definition, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L67))

```lean
public def isIpv4 (t : Term) : Term
```

`Cedar.SymCC.IPAddr.isIpv6` (definition, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L70))

```lean
public def isIpv6 (t : Term) : Term
```

`Cedar.SymCC.IPAddr.subnetWidth` (definition, [line 73](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L73))

```lean
def subnetWidth (w : Nat) (ipPre : Term) : Term
```

`Cedar.SymCC.IPAddr.range` (definition, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L80))

```lean
def range (w : Nat) (ipAddr ipPre : Term) : Term × Term
```

`Cedar.SymCC.IPAddr.rangeV4` (definition, [line 87](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L87))

```lean
def rangeV4 (t : Term) : Term × Term
```

`Cedar.SymCC.IPAddr.rangeV6` (definition, [line 90](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L90))

```lean
def rangeV6 (t : Term) : Term × Term
```

`Cedar.SymCC.IPAddr.inRange` (definition, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L93))

```lean
def inRange (range : Term → Term × Term) (t₁ t₂ : Term) : Term
```

`Cedar.SymCC.IPAddr.inRangeV` (definition, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L98))

```lean
def inRangeV (isIp : Term → Term) (range : Term → Term × Term) (t₁ t₂ : Term) : Term
```

`Cedar.SymCC.IPAddr.isInRange` (definition, [line 102](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L102))

```lean
public def isInRange (t₁ t₂ : Term) : Term
```

`Cedar.SymCC.IPAddr.inRangeVs` (definition, [line 111](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L111))

> Variadic `inRangeV`: `t` is `isIp` and in range of any of `ts` (each of which
> must also be `isIp`). Left-folds the per-range checks with `or`.

```lean
def inRangeVs (isIp : Term → Term) (range : Term → Term × Term) (t : Term) (ts : List Term) : Term
```

`Cedar.SymCC.IPAddr.isInRangeV` (definition, [line 120](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L120))

> Variadic `isInRange`: `t₁` is in range of any of `ts`. A single top-level `or` of the ipv4 and ipv6
> `inRangeVs` checks, each folding over all ranges. With a single range this reduces to the binary
> `isInRange`.

```lean
public def isInRangeV (t₁ : Term) (ts : List Term) : Term
```

`Cedar.SymCC.IPAddr.ipTerm` (definition, [line 125](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L125))

```lean
def ipTerm (ip : IPAddr) : Term
```

`Cedar.SymCC.IPAddr.inRangeLit` (definition, [line 127](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L127))

```lean
def inRangeLit (t : Term) (cidr₄ : Ext.IPAddr.CIDR Ext.IPAddr.V4_WIDTH) (cidr₆ : Ext.IPAddr.CIDR Ext.IPAddr.V6_WIDTH) : Term
```

`Cedar.SymCC.IPAddr.isLoopback` (definition, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L133))

```lean
public def isLoopback (t : Term) : Term
```

`Cedar.SymCC.IPAddr.isMulticast` (definition, [line 136](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L136))

```lean
public def isMulticast (t : Term) : Term
```

`Cedar.SymCC.Duration.toMilliseconds` (definition, [line 143](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L143))

```lean
public def toMilliseconds (t : Term) : Term
```

`Cedar.SymCC.Duration.toSeconds` (definition, [line 145](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L145))

```lean
public def toSeconds (t : Term) : Term
```

`Cedar.SymCC.Duration.toMinutes` (definition, [line 148](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L148))

```lean
public def toMinutes (t : Term) : Term
```

`Cedar.SymCC.Duration.toHours` (definition, [line 151](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L151))

```lean
public def toHours (t : Term) : Term
```

`Cedar.SymCC.Duration.toDays` (definition, [line 154](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L154))

```lean
public def toDays (t : Term) : Term
```

`Cedar.SymCC.Datetime.offset` (definition, [line 161](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L161))

```lean
public def offset (dt dur : Term) : Term
```

`Cedar.SymCC.Datetime.durationSince` (definition, [line 166](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L166))

```lean
public def durationSince (dt₁ dt₂ : Term) : Term
```

`Cedar.SymCC.Datetime.toDate` (definition, [line 171](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L171))

```lean
public def toDate (dt : Term) : Term
```

`Cedar.SymCC.Datetime.toTime` (definition, [line 179](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean#L179))

```lean
public def toTime (dt : Term) : Term
```

## Depends on

- [Factory](factory.md)

## Sources

- [Cedar/SymCC/ExtFun.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/ExtFun.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.ExtFun.json)

---
catalog: module
lean: Cedar.Thm.IPAddr.splitDoubleColonModel, Cedar.Thm.IPAddr.splitOn_doubleColon_eq, Cedar.Thm.IPAddr.isWfV4_iff_exists_value, Cedar.Thm.IPAddr.isWfV6_iff_exists_value
statement: formalized
proof: formalized
---

# IPAddr grammar bridge lemmas

`Cedar.Thm.Ext.IPAddr.Lemmas`, in [Cedar/Thm/Ext/IPAddr/Lemmas.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Lemmas.lean).

> These lemmas connect the parser-independent grammar definitions in
> `Cedar.Thm.Ext.IPAddr.Grammar` (`IsWfIPNet`, `IsIPNetValue`, and the component value functions) to
> the actual `Cedar.Spec.Ext.IPAddr.parse`. They culminate in the per-form parse characterizations
> the aggregator `parse_sound`/`parse_complete` build on.
>
> The parser structure (from `Cedar.Spec.Ext.IPAddr`) is:
> - `parse str = if (parseIPv4Net str).isSome then parseIPv4Net str else parseIPv6Net str`;
> - `parseIPv4Net` splits on `'/'`, parses four `parseNumV4` groups (split on `'.'`) and an optional
>   `parsePrefixNat` prefix;
> - `parseIPv6Net` splits on `'/'`, parses the address via `parseSegsV6` (which handles `::` via
>   `splitOn "::"` and pads to eight hextets) and an optional `parsePrefixNat` prefix.
>
> Each numeric primitive (`parseNumV4`, `parseNumV6`, `parsePrefixNat`) enforces the length /
> leading-zero / range side conditions that the grammar predicates transcribe.

> ## Numeric-token bridges

> ## IPv4 form

> ## IPv6 form

> ## Specialized model of `String.splitOn "::"`

`Cedar.Thm.IPAddr.splitDoubleColonModel` (definition, [line 693](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Lemmas.lean#L693))

> The proof-layer model of `String.splitOn "::"`.

```lean
public def splitDoubleColonModel (str : String) : List String
```

`Cedar.Thm.IPAddr.splitOn_doubleColon_eq` (theorem, [line 914](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Lemmas.lean#L914))

> `String.splitOn "::"` agrees with the proof-layer character-list model on every string.

```lean
public theorem splitOn_doubleColon_eq (s : String) :
    s.splitOn "::" = splitDoubleColonModel s
```

`Cedar.Thm.IPAddr.isWfV4_iff_exists_value` (theorem, [line 1402](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Lemmas.lean#L1402))

> Well-formed IPv4 syntax is exactly syntax to which the grammar assigns some V4 value.

```lean
public theorem isWfV4_iff_exists_value {str : String} :
    IsWfV4 str ↔ ∃ net, IsV4Value str net
```

`Cedar.Thm.IPAddr.isWfV6_iff_exists_value` (theorem, [line 1411](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Lemmas.lean#L1411))

> Well-formed IPv6 syntax is exactly syntax to which the grammar assigns some V6 value.

```lean
public theorem isWfV6_iff_exists_value {str : String} :
    IsWfV6 str ↔ ∃ net, IsV6Value str net
```

> ## Canonical-rendering lemmas

## Depends on

- [IPAddr grammar: definitions](grammar.md)

## Sources

- [Cedar/Thm/Ext/IPAddr/Lemmas.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Lemmas.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Ext.IPAddr.Lemmas.json)

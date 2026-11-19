---
catalog: module
lean: Cedar.Thm.IPAddr.wf_iff_exists_value, Cedar.Thm.IPAddr.parse_sound, Cedar.Thm.IPAddr.parse_complete_v4, Cedar.Thm.IPAddr.parse_complete_v6, Cedar.Thm.IPAddr.parse_complete, Cedar.Thm.IPAddr.parse_eq_some_iff_isIPNetValue, Cedar.Thm.IPAddr.isIPNetValue_unique, Cedar.Thm.IPAddr.parse_eq_none_iff, Cedar.Thm.IPAddr.parse_toString_roundtrip, Cedar.Thm.IPAddr.toString_injective, Cedar.Thm.IPAddr.normalize_eq_iff_parse_eq
statement: formalized
proof: formalized
---

# IPAddr parser correctness

`Cedar.Thm.Ext.IPAddr`, in [Cedar/Thm/Ext/IPAddr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr.lean).

> `parse_sound`, `parse_complete`, and `parse_eq_none_iff` characterize exactly when
> `Cedar.Spec.Ext.IPAddr.ip` (a.k.a. `ip`) succeeds, in terms of the grammar-level `IsWfIPNet`
> predicate and declarative `IsIPNetValue` relation. Its two branches use `v4Value` and `v6Value` to
> give the denotation of the same components that witness the input rendering. The parser-independent
> bridge lemmas they build on live in `Cedar.Thm.Ext.IPAddr.Lemmas`.

> ## Well-formedness and valuation

`Cedar.Thm.IPAddr.wf_iff_exists_value` (theorem, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr.lean#L41))

> Well-formed IP-net syntax is exactly syntax to which the grammar assigns some `IPNet`.

```lean
public theorem wf_iff_exists_value {str : String} :
    IsWfIPNet str ↔ ∃ net, IsIPNetValue str net
```

> ## Soundness

`Cedar.Thm.IPAddr.parse_sound` (theorem, [line 58](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr.lean#L58))

> Soundness of `IPAddr.ip`: if parsing succeeds, the declarative grammar relation assigns the
> input exactly the returned `IPNet`.

```lean
public theorem parse_sound (str : String) (net : IPNet) (h : IPAddr.ip str = some net) :
    IsIPNetValue str net
```

> ## Completeness

`Cedar.Thm.IPAddr.parse_complete_v4` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr.lean#L69))

> Completeness for the V4 form: a well-formed V4 string parses to its `v4Value`.

```lean
public theorem parse_complete_v4 {v : V4Components} {pre : Option String}
    (hsyn : v.syntaxWf) (hcon : v.constraintsWf)
    (hpre : IsWfOptionalPrefix 2 (ADDR_SIZE V4_WIDTH) pre) :
    IPAddr.ip (v.asString ++ (match pre with | none => "" | some p => "/" ++ p))
      = some (v4Value v pre)
```

`Cedar.Thm.IPAddr.parse_complete_v6` (theorem, [line 84](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr.lean#L84))

> Completeness for the V6 form: a well-formed V6 string parses to its `v6Value`.

```lean
public theorem parse_complete_v6 {v : V6Components} {pre : Option String}
    (hsyn : v.syntaxWf)
    (hpre : IsWfOptionalPrefix 3 (ADDR_SIZE V6_WIDTH) pre) :
    IPAddr.ip (v.asString ++ (match pre with | none => "" | some p => "/" ++ p))
      = some (v6Value v pre)
```

`Cedar.Thm.IPAddr.parse_complete` (theorem, [line 115](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr.lean#L115))

> Completeness of `IPAddr.ip`: if the grammar assigns `str` the value `net`, parsing returns that
> exact `IPNet`.

```lean
public theorem parse_complete (str : String) (net : IPNet)
    (h : IsIPNetValue str net) :
    IPAddr.ip str = some net
```

`Cedar.Thm.IPAddr.parse_eq_some_iff_isIPNetValue` (theorem, [line 134](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr.lean#L134))

> Exact parser characterization: parsing succeeds with `net` precisely when the declarative
> grammar relation assigns the input that `IPNet`.

```lean
public theorem parse_eq_some_iff_isIPNetValue (str : String) (net : IPNet) :
    IPAddr.ip str = some net ↔ IsIPNetValue str net
```

`Cedar.Thm.IPAddr.isIPNetValue_unique` (theorem, [line 140](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr.lean#L140))

> The relational value specification is single-valued: an IP-net string denotes at most one
> `IPNet`.

```lean
public theorem isIPNetValue_unique {str : String} {net₁ net₂ : IPNet}
    (h₁ : IsIPNetValue str net₁) (h₂ : IsIPNetValue str net₂) : net₁ = net₂
```

> ## Failure characterization

`Cedar.Thm.IPAddr.parse_eq_none_iff` (theorem, [line 152](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr.lean#L152))

> Failure characterization: `IPAddr.ip` rejects exactly the strings that are not well-formed
> IP-nets. (There is no overflow condition — the grammar's field bounds already exclude
> out-of-range values.)

```lean
public theorem parse_eq_none_iff (str : String) :
    IPAddr.ip str = none ↔ ¬ IsWfIPNet str
```

> ## Roundtrip

`Cedar.Thm.IPAddr.parse_toString_roundtrip` (theorem, [line 170](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr.lean#L170))

> `parse ∘ toString` roundtrip: parsing the canonical representation recovers the original
> IP-net.

```lean
public theorem parse_toString_roundtrip (net : IPNet) :
    IPAddr.ip (toString net) = some net
```

`Cedar.Thm.IPAddr.toString_injective` (theorem, [line 181](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr.lean#L181))

> `toString` is injective: distinct IP-nets produce distinct canonical strings.

```lean
public theorem toString_injective (net net' : IPNet) (h : toString net = toString net') :
    net = net'
```

`Cedar.Thm.IPAddr.normalize_eq_iff_parse_eq` (theorem, [line 190](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr.lean#L190))

> Equal normal form iff equal value: normalization decides IP-net equality.

```lean
public theorem normalize_eq_iff_parse_eq (str str' : String) :
    normalize str = normalize str' ↔ IPAddr.ip str = IPAddr.ip str'
```

## Depends on

- [IPAddr grammar: definitions](ipaddr-2/grammar.md)

## Proof depends on

- [IPAddr grammar bridge lemmas](ipaddr-2/lemmas.md)

## Sources

- [Cedar/Thm/Ext/IPAddr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Ext.IPAddr.json)

---
catalog: module
lean: Cedar.Thm.IPAddr.IsCanonicalNat, Cedar.Thm.IPAddr.V4Components, Cedar.Thm.IPAddr.V4Components.syntaxWf, Cedar.Thm.IPAddr.V4Components.constraintsWf, Cedar.Thm.IPAddr.V4Components.asString, Cedar.Thm.IPAddr.V4Components.toAddr, Cedar.Thm.IPAddr.IsHexGroup, Cedar.Thm.IPAddr.hexValue, Cedar.Thm.IPAddr.V6Components, Cedar.Thm.IPAddr.V6Components.expand, Cedar.Thm.IPAddr.V6Components.syntaxWf, Cedar.Thm.IPAddr.V6Components.asString, Cedar.Thm.IPAddr.V6Components.toAddr, Cedar.Thm.IPAddr.IsWfOptionalPrefix, Cedar.Thm.IPAddr.prefixValue, Cedar.Thm.IPAddr.V4Production, Cedar.Thm.IPAddr.IsWfV4, Cedar.Thm.IPAddr.V6Production, Cedar.Thm.IPAddr.IsWfV6, Cedar.Thm.IPAddr.IsWfIPNet, Cedar.Thm.IPAddr.v4Value, Cedar.Thm.IPAddr.v6Value, Cedar.Thm.IPAddr.IsV4Value, Cedar.Thm.IPAddr.IsV6Value, Cedar.Thm.IPAddr.IsIPNetValue, Cedar.Thm.IPAddr.normalize
statement: formalized
proof: formalized
---

# IPAddr grammar: definitions

`Cedar.Thm.Ext.IPAddr.Grammar`, in [Cedar/Thm/Ext/IPAddr/Grammar.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean).

> This file contains only the grammar-level definitions: the well-formedness predicates, component
> value functions, and relational value specification. `IsWfIPNet` states the syntax,
> `v4Value`/`v6Value` give the denotation of identified components, and `IsIPNetValue str net`
> combines those same witnesses to say that `str` denotes `net`. The lemmas connecting these
> definitions to `IPAddr.parse` live in `Cedar.Thm.Ext.IPAddr.Lemmas`.
>
> The accepted syntax (transcribed from the spec parser) is, informally:
>
> ```
> IPNet    ::= V4Net | V6Net          -- V4 tried first; a string is V6 only if it is not V4
> V4Net    ::= V4Addr ['/' V4Prefix]
> V4Addr   ::= NumV4 '.' NumV4 '.' NumV4 '.' NumV4
> NumV4    ::= Digit{1,3}             -- no leading zeros unless the group is exactly "0"; value ≤ 255
> V4Prefix ::= Digit{1,2}            -- no leading zeros unless exactly "0"; value ≤ 32
>
> V6Net    ::= V6Addr ['/' V6Prefix]
> V6Addr   ::= a `::`-compressed sequence of hextets that expands to exactly 8 groups
> NumV6    ::= HexDigit{1,4}          -- value ≤ 0xffff (automatic from ≤ 4 hex digits)
> V6Prefix ::= Digit{1,3}            -- no leading zeros unless exactly "0"; value ≤ 128
> ```
>
> The `::` compression may appear at most once and denotes a run of zero hextets that pads the total
> to 8 groups.

> ## Shared digit/number-token predicates

`Cedar.Thm.IPAddr.IsCanonicalNat` (definition, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L62))

> A `Digit⁺` string that additionally forbids a leading zero unless it is exactly `"0"` — the
> "no leading zeros" rule the spec parser enforces on every numeric group and prefix
> (`str.startsWith "0" → str = "0"`).

```lean
public def IsCanonicalNat (s : String) : Prop
```

> ## IPv4 grammar
>
> `V4Addr` is four dot-separated groups, each a canonical 1–3 digit number `≤ 255`; the optional
> prefix is a canonical 1–2 digit number `≤ 32`.

`Cedar.Thm.IPAddr.V4Components` (structure, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L71))

> The grammar's `V4Addr ::= NumV4 '.' NumV4 '.' NumV4 '.' NumV4`: four decimal groups.

```lean
public structure V4Components where
  g₀ : String
  g₁ : String
  g₂ : String
  g₃ : String
```

`Cedar.Thm.IPAddr.V4Components.syntaxWf` (definition, [line 78](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L78))

> Each group is a canonical number of at most 3 digits.

```lean
public def V4Components.syntaxWf (v : V4Components) : Prop
```

`Cedar.Thm.IPAddr.V4Components.constraintsWf` (definition, [line 85](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L85))

> Each group's value is at most `255` (`0xff`).

```lean
public def V4Components.constraintsWf (v : V4Components) : Prop
```

`Cedar.Thm.IPAddr.V4Components.asString` (definition, [line 89](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L89))

> Render a `V4Addr` as `g₀ '.' g₁ '.' g₂ '.' g₃`.

```lean
public def V4Components.asString (v : V4Components) : String
```

`Cedar.Thm.IPAddr.V4Components.toAddr` (definition, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L93))

> The `IPv4Addr` value of well-formed V4 groups.

```lean
public def V4Components.toAddr (v : V4Components) : IPv4Addr
```

> ## IPv6 grammar
>
> `V6Addr` is a `::`-compressed sequence of hextets. Rather than model the compression syntactically
> here, a `V6Components` record holds the eight expanded hextets together with the *rendering* (the
> concrete `::`-form string), and well-formedness is phrased existentially over that rendering (as in
> the duration/datetime grammars). Each hextet is a 1–4 character hex-digit string.

`Cedar.Thm.IPAddr.IsHexGroup` (definition, [line 105](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L105))

> A `Digit⁺`-style predicate for hex groups: a non-empty string all of whose characters are hex
> digits, of length at most 4.

```lean
public def IsHexGroup (s : String) : Prop
```

`Cedar.Thm.IPAddr.hexValue` (definition, [line 109](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L109))

> Numeric value of a hex group (`Σ digit · 16ⁱ`), matching the spec parser's `foldl`.

```lean
public def hexValue (s : String) : Nat
```

`Cedar.Thm.IPAddr.V6Components` (inductive type, [line 118](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L118))

> A V6 address, as the spec parser accepts it: either a full list of hextets with no `::`
> compression, or a `::`-compressed form with a left and right list of hextets and an implicit
> run of zero hextets between them. This mirrors `parseSegsV6`'s `splitOn "::"`:
> - `full gs`     ↔ the string has no `::`; `gs` is the `':'`-separated hextet list;
> - `gap l r`     ↔ the string is `l₀:…:lₘ '::' r₀:…:rₙ`; the gap expands to `8 − (|l|+|r|)`
>   zero hextets.

```lean
public inductive V6Components where
  | full (gs : List String)
  | gap  (l r : List String)
```

`Cedar.Thm.IPAddr.V6Components.expand` (definition, [line 124](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L124))

> The eight expanded hextet strings a `V6Components` denotes: the full list itself, or the two
> sides padded with the appropriate number of `"0"` hextets between them.

```lean
public def V6Components.expand : V6Components → List String
```

`Cedar.Thm.IPAddr.V6Components.syntaxWf` (definition, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L133))

> Syntactic well-formedness of a V6 address:
> - every present hextet is a valid 1–4 digit hex group;
> - the `full` form has exactly 8 hextets (no `::` ⇒ `splitToList ':'` must give 8);
> - the `gap` form's two sides total *strictly fewer* than 8 (so the `::` denotes ≥ 1 zero
>   hextet — `parseSegsV6` requires `len < 8`).

```lean
public def V6Components.syntaxWf : V6Components → Prop
```

`Cedar.Thm.IPAddr.V6Components.asString` (definition, [line 139](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L139))

> Render a V6 address to its concrete string: hextets joined by `':'`, with `"::"` at the gap.
> (`intercalate ":"` matches the parser's `splitToList (· = ':')` / `splitOn "::"` inverse.)

```lean
public def V6Components.asString : V6Components → String
```

`Cedar.Thm.IPAddr.V6Components.toAddr` (definition, [line 145](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L145))

> The `IPv6Addr` value: the eight expanded hextets' hex values. Well-formedness guarantees
> `expand` has length 8; on other lengths this defaults the missing groups to `0`.

```lean
public def V6Components.toAddr (v : V6Components) : IPv6Addr
```

> ## Prefix grammar
>
> An optional CIDR suffix `'/' Prefix`, where `Prefix` is a canonical decimal number bounded by the
> address width (`≤ 32` for V4, `≤ 128` for V6). Absence of the suffix denotes the full-width prefix
> (`ADDR_SIZE`).

`Cedar.Thm.IPAddr.IsWfOptionalPrefix` (definition, [line 158](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L158))

> The optional prefix, with its digit-count and value bounds `(digits, size)`
> (`(2, 32)` for V4, `(3, 128)` for V6). `none` is the implicit full-width prefix.

```lean
public def IsWfOptionalPrefix (digits size : Nat) : Option String → Prop
```

`Cedar.Thm.IPAddr.prefixValue` (definition, [line 163](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L163))

> The `IPNetPrefix` value of an optional prefix string: `none` maps to the full-width prefix.

```lean
public def prefixValue (w : Nat) : Option String → IPNetPrefix w
```

> ## Top-level well-formedness
>
> An IP-net string is well-formed when it is either a well-formed V4 rendering or a well-formed V6
> rendering (with V4 taking precedence, mirroring the parser's `if ipv4.isSome then … else …`). Both
> are phrased existentially over the components' `asString` rendering (as in the duration/datetime
> grammars), baking the separators, group count, and `::`-compression rules into the witness.

`Cedar.Thm.IPAddr.V4Production` (definition, [line 175](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L175))

> The IPv4 grammar production witnessed by address components and an optional CIDR prefix.

```lean
public def V4Production (str : String) (v : V4Components) (pre : Option String) : Prop
```

`Cedar.Thm.IPAddr.IsWfV4` (definition, [line 182](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L182))

> A well-formed IPv4-net string has a valid IPv4 grammar production.

```lean
public def IsWfV4 (str : String) : Prop
```

`Cedar.Thm.IPAddr.V6Production` (definition, [line 186](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L186))

> The IPv6 grammar production witnessed by address components and an optional CIDR prefix.

```lean
public def V6Production (str : String) (v : V6Components) (pre : Option String) : Prop
```

`Cedar.Thm.IPAddr.IsWfV6` (definition, [line 192](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L192))

> A well-formed IPv6-net string has a valid IPv6 grammar production.

```lean
public def IsWfV6 (str : String) : Prop
```

`Cedar.Thm.IPAddr.IsWfIPNet` (definition, [line 198](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L198))

> A string is a well-formed IP-net iff it is a well-formed V4 or V6 net. Because the parser tries
> V4 first and only falls through to V6 when V4 fails, and the two grammars are disjoint on their
> accepted strings, this disjunction faithfully characterizes acceptance.

```lean
public def IsWfIPNet (str : String) : Prop
```

> ## Value relation
>
> The component value functions are independent of the parser. The relational definitions below
> tie those values to the same witnesses used by the syntax predicates, so no second string decoder
> is needed.

`Cedar.Thm.IPAddr.v4Value` (definition, [line 208](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L208))

> The `IPNet` value of a well-formed V4 string's components.

```lean
public def v4Value (v : V4Components) (pre : Option String) : IPNet
```

`Cedar.Thm.IPAddr.v6Value` (definition, [line 212](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L212))

> The `IPNet` value of a well-formed V6 string's components.

```lean
public def v6Value (v : V6Components) (pre : Option String) : IPNet
```

`Cedar.Thm.IPAddr.IsV4Value` (definition, [line 216](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L216))

> `net` is the value of a well-formed IPv4-net rendering.

```lean
public def IsV4Value (str : String) (net : IPNet) : Prop
```

`Cedar.Thm.IPAddr.IsV6Value` (definition, [line 222](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L222))

> `net` is the value of a well-formed IPv6-net rendering.

```lean
public def IsV6Value (str : String) (net : IPNet) : Prop
```

`Cedar.Thm.IPAddr.IsIPNetValue` (definition, [line 228](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L228))

> `net` is the value of the IP-net literal `str`, through either the V4 or V6 production.

```lean
public def IsIPNetValue (str : String) (net : IPNet) : Prop
```

`Cedar.Thm.IPAddr.normalize` (definition, [line 233](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean#L233))

> Canonical-form normalizer: parse the string and re-serialize.
> Returns `none` for malformed inputs.

```lean
public def normalize (str : String) : Option String
```

## Depends on

- [IPAddr](../../../spec/ext-2/ipaddr.md)
- [String](../../data/string.md)

## Sources

- [Cedar/Thm/Ext/IPAddr/Grammar.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/IPAddr/Grammar.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Ext.IPAddr.Grammar.json)

---
catalog: module
lean: Cedar.Thm.Decimal.wf_iff_exists_value, Cedar.Thm.Decimal.parse_complete, Cedar.Thm.Decimal.parse_sound, Cedar.Thm.Decimal.parse_eq_some_iff_isDecimalValue, Cedar.Thm.Decimal.parse_toString_roundtrip, Cedar.Thm.Decimal.parse_eq_none_iff, Cedar.Thm.Decimal.toString_injective, Cedar.Thm.Decimal.normalize_eq_iff_parse_eq
statement: formalized
proof: formalized
---

# Thm/Ext/Decimal

`Cedar.Thm.Ext.Decimal`, in [Cedar/Thm/Ext/Decimal.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal.lean).

`Cedar.Thm.Decimal.wf_iff_exists_value` (theorem, [line 32](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal.lean#L32))

> Well-formed decimal syntax is exactly syntax to which the grammar assigns some value.

```lean
public theorem wf_iff_exists_value {s : String} :
    IsWfDecimal s ↔ ∃ v, IsDecimalValue s v
```

`Cedar.Thm.Decimal.parse_complete` (theorem, [line 43](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal.lean#L43))

> Completeness of `Decimal.parse`: if the grammar assigns `s` the value `d.toInt`, then parsing
> accepts the string as `d`. Well-formedness is not a separate hypothesis — `IsDecimalValue`
> already asserts that `s` is a rendering of the grammar's productions.

```lean
public theorem parse_complete (s : String) (d : Decimal)
    (hval : IsDecimalValue s d.toInt) : Decimal.parse s = some d
```

`Cedar.Thm.Decimal.parse_sound` (theorem, [line 51](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal.lean#L51))

> Soundness of `Decimal.parse`: if parsing succeeds, then the input is a well-formed rendering
> whose grammar value is exactly the returned decimal's value. (The value is automatically in
> `Int64` range, since `d : Decimal = Int64`, so no range conjunct is stated.)

```lean
public theorem parse_sound (s : String) (d : Decimal) (h : Decimal.parse s = some d) :
    IsDecimalValue s d.toInt
```

`Cedar.Thm.Decimal.parse_eq_some_iff_isDecimalValue` (theorem, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal.lean#L80))

> Exact parser characterization: parsing succeeds with `d` precisely when the declarative
> grammar relation assigns the input the value `d.toInt`.

```lean
public theorem parse_eq_some_iff_isDecimalValue (s : String) (d : Decimal) :
    Decimal.parse s = some d ↔ IsDecimalValue s d.toInt
```

`Cedar.Thm.Decimal.parse_toString_roundtrip` (theorem, [line 85](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal.lean#L85))

> Parsing the canonical string representation of a decimal returns the same decimal.

```lean
public theorem parse_toString_roundtrip (d : Decimal) :
    Decimal.parse (toString d) = some d
```

`Cedar.Thm.Decimal.parse_eq_none_iff` (theorem, [line 92](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal.lean#L92))

> Failure characterization for `Decimal.parse`: parsing rejects exactly malformed strings and
> well-formed strings whose grammar value overflows the `Int64` range. The value relation is
> total on well-formed syntax, so these cases are exhaustive and mutually exclusive.

```lean
public theorem parse_eq_none_iff (s : String) :
    Decimal.parse s = none ↔ ¬ IsWfDecimal s ∨
    ∃ v, IsDecimalValue s v ∧ (v < Int64.MIN ∨ v > Int64.MAX)
```

`Cedar.Thm.Decimal.toString_injective` (theorem, [line 113](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal.lean#L113))

> `toString` is injective: distinct decimals produce distinct strings.

```lean
public theorem toString_injective (d d' : Decimal) (h : toString d = toString d') : d = d'
```

`Cedar.Thm.Decimal.normalize_eq_iff_parse_eq` (theorem, [line 121](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal.lean#L121))

> Equal normal form iff equal value: normalization decides decimal equality.

```lean
public theorem normalize_eq_iff_parse_eq (s s' : String) :
    normalize s = normalize s' ↔ Decimal.parse s = Decimal.parse s'
```

## Depends on

- [Decimal grammar: definitions](decimal-2/grammar.md)

## Proof depends on

- [Decimal/Lemmas](decimal-2/lemmas.md)

## Sources

- [Cedar/Thm/Ext/Decimal.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Decimal.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Ext.Decimal.json)

---
catalog: module
lean: Cedar.Thm.Datetime.wf_iff_exists_value, Cedar.Thm.Datetime.parse_sound, Cedar.Thm.Datetime.parse_complete, Cedar.Thm.Datetime.parse_eq_none_iff, Cedar.Thm.Datetime.parse_toString_roundtrip, Cedar.Thm.Datetime.toString?_injective, Cedar.Thm.Datetime.normalize_eq_iff_parse_eq
statement: formalized
proof: formalized
---

# Datetime parser correctness

`Cedar.Thm.Ext.Datetime`, in [Cedar/Thm/Ext/Datetime.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime.lean).

> ## Soundness, completeness, and failure characterization

`Cedar.Thm.Datetime.wf_iff_exists_value` (theorem, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime.lean#L36))

> Well-formed datetime syntax is exactly syntax to which the grammar assigns some value.

```lean
public theorem wf_iff_exists_value {str : String} :
    IsWfDatetime str ↔ ∃ v, IsDatetimeValue str v
```

`Cedar.Thm.Datetime.parse_sound` (theorem, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime.lean#L46))

> Soundness of `Datetime.parse`: if parsing succeeds, the grammar assigns the input the returned
> datetime's value.

```lean
public theorem parse_sound (str : String) (d : Datetime)
    (h : Datetime.parse str = some d) :
    IsDatetimeValue str d.val.toInt
```

`Cedar.Thm.Datetime.parse_complete` (theorem, [line 68](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime.lean#L68))

> Completeness of `Datetime.parse`: if the grammar assigns a string the value `d.val.toInt`,
> then parsing accepts the string as `d`.

```lean
public theorem parse_complete (str : String) (d : Datetime)
    (hval : IsDatetimeValue str d.val.toInt) :
    Datetime.parse str = some d
```

> ## Failure characterization

`Cedar.Thm.Datetime.parse_eq_none_iff` (theorem, [line 97](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime.lean#L97))

> Because the grammar bounds years to four digits and zone offsets to `±23:59`, every
> well-formed datetime value fits in `Int64`. Parsing therefore rejects exactly malformed
> strings.

```lean
public theorem parse_eq_none_iff (str : String) :
    Datetime.parse str = none ↔ ¬ IsWfDatetime str
```

> ## Canonical serialization

`Cedar.Thm.Datetime.parse_toString_roundtrip` (theorem, [line 128](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime.lean#L128))

> `parse ∘ toString?` roundtrip: every successfully serialized datetime parses back to the
> original value.

```lean
public theorem parse_toString_roundtrip {d : Datetime} {str : String}
    (h : toString? d = some str) :
    Datetime.parse str = some d
```

`Cedar.Thm.Datetime.toString?_injective` (theorem, [line 136](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime.lean#L136))

> `toString?` is injective on the values it serializes: datetimes with the same (defined)
> canonical string are equal. (Partial-serializer analogue of `Decimal`/`Duration`'s
> `toString_injective`.)

```lean
public theorem toString?_injective {d d' : Datetime} {str : String}
    (h : toString? d = some str) (h' : toString? d' = some str) :
    d = d'
```

> ## Normalization

`Cedar.Thm.Datetime.normalize_eq_iff_parse_eq` (theorem, [line 155](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime.lean#L155))

> Equal normal form iff equal parse — normalization decides datetime equality.
>
> Datetime serialization is *partial* (`toString?`), so `normalize = (parse ·).bind toString?`
> can collapse two distinct parseable-but-unserializable values to the shared `none`. The forward
> direction therefore carries a serializability hypothesis on the parsed values; this is exactly
> what a full *serialization-completeness* result (`parse s = some d → (toString? d).isSome`,
> which needs the `Std.Time` civil-calendar round-trip) would discharge unconditionally, closing
> the gap with `Decimal`/`Duration`'s total-`toString` versions. The backward direction is
> unconditional.

```lean
public theorem normalize_eq_iff_parse_eq (s s' : String)
    (hs : ∀ d, Datetime.parse s = some d → (toString? d).isSome)
    (hs' : ∀ d, Datetime.parse s' = some d → (toString? d).isSome) :
    normalize s = normalize s' ↔ Datetime.parse s = Datetime.parse s'
```

## Depends on

- [Datetime grammar: definitions](datetime-2/grammar.md)

## Proof depends on

- [Datetime/Lemmas](datetime-2/lemmas.md)

## Sources

- [Cedar/Thm/Ext/Datetime.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Ext.Datetime.json)

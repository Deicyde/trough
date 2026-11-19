---
catalog: module
lean: Cedar.Thm.Duration.wf_iff_exists_value, Cedar.Thm.Duration.parse_complete, Cedar.Thm.Duration.parse_sound, Cedar.Thm.Duration.parse_eq_some_iff_isDurationValue, Cedar.Thm.Duration.parse_eq_none_iff, Cedar.Thm.Duration.parse_neg, Cedar.Thm.Duration.offset_durationSince_inverse, Cedar.Thm.Duration.parse_toString_roundtrip, Cedar.Thm.Duration.toString_injective, Cedar.Thm.Duration.normalize_eq_iff_parse_eq
statement: formalized
proof: formalized
---

# Duration

`Cedar.Thm.Ext.Duration`, in [Cedar/Thm/Ext/Duration.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration.lean).

> Duration parser theorem surface.
>
> `parse_sound` and `parse_complete` characterize successful parsing against the declarative
> `IsDurationValue` relation. `parse_eq_none_iff` characterizes exactly when parsing rejects.

`Cedar.Thm.Duration.wf_iff_exists_value` (theorem, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration.lean#L38))

> Well-formed duration syntax is exactly syntax to which the grammar assigns some value.

```lean
public theorem wf_iff_exists_value {str : String} :
    IsWfDuration str ↔ ∃ v, IsDurationValue str v
```

`Cedar.Thm.Duration.parse_complete` (theorem, [line 48](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration.lean#L48))

> Completeness of `Duration.parse`: if the grammar assigns `str` the value `d.val.toInt`, then
> parsing accepts the string as `d`.

```lean
public theorem parse_complete (str : String) (d : Duration)
    (hval : IsDurationValue str d.val.toInt) :
    Duration.parse str = some d
```

`Cedar.Thm.Duration.parse_sound` (theorem, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration.lean#L56))

> Soundness of `Duration.parse`: if parsing succeeds, the declarative grammar relation assigns
> the input exactly the returned duration's value.

```lean
public theorem parse_sound (str : String) (d : Duration)
    (h : Duration.parse str = some d) :
    IsDurationValue str d.val.toInt
```

`Cedar.Thm.Duration.parse_eq_some_iff_isDurationValue` (theorem, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration.lean#L79))

> Exact parser characterization: parsing succeeds with `d` precisely when the declarative
> grammar relation assigns the input the value `d.val.toInt`.

```lean
public theorem parse_eq_some_iff_isDurationValue (str : String) (d : Duration) :
    Duration.parse str = some d ↔ IsDurationValue str d.val.toInt
```

`Cedar.Thm.Duration.parse_eq_none_iff` (theorem, [line 85](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration.lean#L85))

> Failure characterization for `Duration.parse`: parsing rejects exactly malformed strings and
> well-formed strings whose grammar value overflows the `Int64` range.

```lean
public theorem parse_eq_none_iff (str : String) :
    Duration.parse str = none ↔
    ¬ IsWfDuration str ∨
      ∃ v, IsDurationValue str v ∧ (v < Int64.MIN ∨ v > Int64.MAX)
```

`Cedar.Thm.Duration.parse_neg` (theorem, [line 104](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration.lean#L104))

> Parsing a negated duration string negates the underlying value.

```lean
public theorem parse_neg (s : String) (d : Duration)
    (hpos : ¬ s.startsWith "-")
    (h : Duration.parse s = some d) :
    Duration.parse ("-" ++ s) = duration? (-d.val.toInt)
```

`Cedar.Thm.Duration.offset_durationSince_inverse` (theorem, [line 139](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration.lean#L139))

> `offset` and `durationSince` are inverses: adding a duration then computing
> the difference gives back the same duration.

```lean
public theorem offset_durationSince_inverse (dt : Datetime) (dur : Duration) (dt' : Datetime)
    (h : offset dt dur = some dt') :
    durationSince dt' dt = some dur
```

`Cedar.Thm.Duration.parse_toString_roundtrip` (theorem, [line 154](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration.lean#L154))

> `parse ∘ toString` roundtrip: parsing the string representation recovers the original.

```lean
public theorem parse_toString_roundtrip (d : Duration) :
    Duration.parse (Duration.toString d) = some d
```

`Cedar.Thm.Duration.toString_injective` (theorem, [line 192](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration.lean#L192))

> `toString` is injective: distinct durations produce distinct strings.

```lean
public theorem toString_injective (d d' : Duration)
    (h : Duration.toString d = Duration.toString d') :
    d = d'
```

`Cedar.Thm.Duration.normalize_eq_iff_parse_eq` (theorem, [line 202](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration.lean#L202))

> Equal normal form iff equal value: normalization decides duration equality.

```lean
public theorem normalize_eq_iff_parse_eq (s s' : String) :
    normalize s = normalize s' ↔ Duration.parse s = Duration.parse s'
```

## Depends on

- [Duration grammar: definitions](duration-2/grammar.md)

## Proof depends on

- [Duration/Lemmas](duration-2/lemmas.md)

## Sources

- [Cedar/Thm/Ext/Duration.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.Ext.Duration.json)

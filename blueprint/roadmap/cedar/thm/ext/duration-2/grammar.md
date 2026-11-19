---
catalog: module
lean: Cedar.Thm.Duration.durationChunk, Cedar.Thm.Duration.IsWfOptionalQuantity, Cedar.Thm.Duration.Components, Cedar.Thm.Duration.Components.nonempty, Cedar.Thm.Duration.Components.quantitiesWf, Cedar.Thm.Duration.Components.asString, Cedar.Thm.Duration.optionalNatOf, Cedar.Thm.Duration.Components.toMillis, Cedar.Thm.Duration.value, Cedar.Thm.Duration.canonicalComponents, Cedar.Thm.Duration.canonicalBody, Cedar.Thm.Duration.IsWfBody, Cedar.Thm.Duration.DurationProduction, Cedar.Thm.Duration.IsWfDuration, Cedar.Thm.Duration.IsDurationValue, Cedar.Thm.Duration.normalize
statement: formalized
proof: formalized
---

# Duration grammar: definitions

`Cedar.Thm.Ext.Duration.Grammar`, in [Cedar/Thm/Ext/Duration/Grammar.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean).

> This file contains only grammar-level definitions: the well-formedness predicates and the value
> relation. `IsWfDuration` states the syntax, `value` gives the denotation of already identified
> components, and `IsDurationValue str v` combines the same witnesses to say that `str` denotes `v`.
> The executable extraction machinery used to connect these definitions to `Duration.parse` lives
> in `Cedar.Thm.Ext.Duration.Lemmas`.

`Cedar.Thm.Duration.durationChunk` (definition, [line 42](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L42))

> Render an optional duration component as its string representation.
> `none` produces `""`, `some digits` produces `digits ++ suffix`.

```lean
public def durationChunk (digits? : Option String) (suffix : String) : String
```

`Cedar.Thm.Duration.IsWfOptionalQuantity` (definition, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L49))

> Lift the `Digit⁺` quantity-token predicate (`IsDigits`) to optional components:
> `none` is trivially valid.

```lean
public def IsWfOptionalQuantity : Option String → Prop
```

`Cedar.Thm.Duration.Components` (structure, [line 55](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L55))

> The five optional digit-string components of a duration body, one per time unit.
> Each field holds `none` (unit absent) or `some digits` (unit present with that value).

```lean
public structure Components where
  days : Option String
  hours : Option String
  minutes : Option String
  seconds : Option String
  milliseconds : Option String
```

`Cedar.Thm.Duration.Components.nonempty` (definition, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L63))

> At least one component must be present (the body cannot be empty).

```lean
public def Components.nonempty (components : Components) : Prop
```

`Cedar.Thm.Duration.Components.quantitiesWf` (definition, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L71))

> Every present component must be a valid duration quantity (nonempty, parseable digits).

```lean
public def Components.quantitiesWf
    (components : Components) : Prop
```

`Cedar.Thm.Duration.Components.asString` (definition, [line 81](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L81))

> Canonical string representation: concatenate present components in order `d h m s ms`.
> Absent components contribute `""`.

```lean
public def Components.asString (components : Components) : String
```

`Cedar.Thm.Duration.optionalNatOf` (definition, [line 90](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L90))

> Natural-number value of an optional duration quantity. An absent component denotes zero;
> a present well-formed component is read by the shared grammar-level `natOf`.

```lean
public def optionalNatOf : Option String → Nat
```

`Cedar.Thm.Duration.Components.toMillis` (definition, [line 95](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L95))

> Unsigned millisecond value of already identified duration components.

```lean
public def Components.toMillis (components : Components) : Int
```

`Cedar.Thm.Duration.value` (definition, [line 103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L103))

> The grammar's value function, applied to an already identified sign and component record.

```lean
public def value (sign : String) (components : Components) : Int
```

`Cedar.Thm.Duration.canonicalComponents` (definition, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L108))

> Canonical maximized components for a duration value split into days, hours, minutes,
> seconds, and milliseconds. All five fields are present, including zero-valued fields.

```lean
public def canonicalComponents (days hours minutes seconds ms : Nat) :
    Components
```

`Cedar.Thm.Duration.canonicalBody` (definition, [line 118](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L118))

> Canonical maximized duration body: `days d`, `hours h`, `minutes m`, `seconds s`,
> and `milliseconds ms`, printed largest-to-smallest.

```lean
public def canonicalBody (days hours minutes seconds ms : Nat) : String
```

`Cedar.Thm.Duration.IsWfBody` (definition, [line 125](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L125))

> A duration body string is well-formed iff it equals `components.asString` for some
> `Components` that is nonempty and has valid quantities.

```lean
public def IsWfBody (body : String) : Prop
```

`Cedar.Thm.Duration.DurationProduction` (definition, [line 132](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L132))

> The grammar production witnessed by an optional sign and a nonempty component record.

```lean
public def DurationProduction (str sign : String) (components : Components) : Prop
```

`Cedar.Thm.Duration.IsWfDuration` (definition, [line 139](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L139))

> A duration string is well-formed iff it has a valid grammar production.

```lean
public def IsWfDuration (str : String) : Prop
```

`Cedar.Thm.Duration.IsDurationValue` (definition, [line 143](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L143))

> `v` is the value assigned to a valid duration production.

```lean
public def IsDurationValue (str : String) (v : Int) : Prop
```

`Cedar.Thm.Duration.normalize` (definition, [line 150](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean#L150))

> Canonical-form normalizer: parse the string and re-serialize.
> Returns `none` for malformed or out-of-range inputs.

```lean
public def normalize (str : String) : Option String
```

## Depends on

- [Datetime](../../../spec/ext-2/datetime.md)
- [String](../../data/string.md)

## Sources

- [Cedar/Thm/Ext/Duration/Grammar.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Duration/Grammar.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Ext.Duration.Grammar.json)

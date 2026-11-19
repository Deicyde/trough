---
catalog: module
lean: Cedar.Spec.Ext.Datetime, Cedar.Spec.Ext.Datetime.lt, Cedar.Spec.Ext.Datetime.le, Cedar.Spec.Ext.Datetime.decLt, Cedar.Spec.Ext.Datetime.decLe, Cedar.Spec.Ext.Datetime.datetime?, Cedar.Spec.Ext.Datetime.parse, Cedar.Spec.Ext.Datetime.datetime, Cedar.Spec.Ext.Datetime.Duration, Cedar.Spec.Ext.Datetime.Duration.lt, Cedar.Spec.Ext.Datetime.Duration.le, Cedar.Spec.Ext.Datetime.Duration.decLt, Cedar.Spec.Ext.Datetime.Duration.decLe, Cedar.Spec.Ext.Datetime.MILLISECONDS_PER_SECOND, Cedar.Spec.Ext.Datetime.MILLISECONDS_PER_MINUTE, Cedar.Spec.Ext.Datetime.MILLISECONDS_PER_HOUR, Cedar.Spec.Ext.Datetime.MILLISECONDS_PER_DAY, Cedar.Spec.Ext.Datetime.duration?, Cedar.Spec.Ext.Datetime.Duration.parse, Cedar.Spec.Ext.Datetime.duration, Cedar.Spec.Ext.Datetime.offset, Cedar.Spec.Ext.Datetime.durationSince, Cedar.Spec.Ext.Datetime.toDate, Cedar.Spec.Ext.Datetime.toTime, Cedar.Spec.Ext.Datetime.Duration.toMilliseconds, Cedar.Spec.Ext.Datetime.Duration.toSeconds, Cedar.Spec.Ext.Datetime.Duration.toMinutes, Cedar.Spec.Ext.Datetime.Duration.toHours, Cedar.Spec.Ext.Datetime.Duration.toDays, Cedar.Spec.Ext.Datetime.durationComponent, Cedar.Spec.Ext.Datetime.Duration.toString
statement: formalized
proof: formalized
---

# Datetime

`Cedar.Spec.Ext.Datetime`, in [Cedar/Spec/Ext/Datetime.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean).

> This file defines Cedar datetime values and functions.

`Cedar.Spec.Ext.Datetime` (structure, [line 44](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L44))

> A datetime value is measured in milliseconds and constructed from a datetime string.
> A datetime string must be of one of the forms:
>   - `YYYY-MM-DD` (date only)
>   - `YYYY-MM-DDThh:mm:ssZ` (UTC)
>   - `YYYY-MM-DDThh:mm:ss.SSSZ` (UTC with millisecond precision)
>   - `YYYY-MM-DDThh:mm:ss(+|-)hhmm` (With timezone offset in hours and minutes)
>   - `YYYY-MM-DDThh:mm:ss.SSS(+|-)hhmm` (With timezone offset in hours and minutes and millisecond precision)
>
> Regardless of the timezone, offset is always normalized to UTC.
>
> The datetime type does not provide a way to create a datetime from a Unix timestamp.
> One of the readable formats listed above must be used instead.

```lean
public structure Datetime where
  val : Int64
```

`Cedar.Spec.Ext.Datetime.lt` (definition, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L47))

```lean
public def Datetime.lt (d₁ d₂ : Datetime) : Bool
```

`Cedar.Spec.Ext.Datetime.le` (definition, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L50))

```lean
public def Datetime.le (d₁ d₂ : Datetime) : Bool
```

`Cedar.Spec.Ext.Datetime.decLt` (instance, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L59))

```lean
public instance Datetime.decLt (d₁ d₂ : Datetime) : Decidable (d₁ < d₂)
```

`Cedar.Spec.Ext.Datetime.decLe` (instance, [line 62](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L62))

```lean
public instance Datetime.decLe (d₁ d₂ : Datetime) : Decidable (d₁ ≤ d₂)
```

`Cedar.Spec.Ext.Datetime.datetime?` (definition, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L80))

```lean
public def datetime? (i: Int) : Option Datetime
```

`Cedar.Spec.Ext.Datetime.parse` (definition, [line 119](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L119))

```lean
public def parse (str: String) : Option Datetime
```

`Cedar.Spec.Ext.Datetime.datetime` (abbreviation, [line 135](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L135))

```lean
public abbrev datetime
```

`Cedar.Spec.Ext.Datetime.Duration` (structure, [line 153](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L153))

> A duration value is measured in milliseconds and constructed from a duration string.
> A duration string is a concatenated sequence of quantity-unit pairs where the quantity
> is a natural number and unit is one of the following:
>   - `d` (for days)
>   - `h` (for hours)
>   - `m` (for minutes)
>   - `s` (for seconds)
>   - `ms` (for milliseconds)
>
> Duration strings are required to be ordered from largest unit to smallest
> unit, and contain one quantity per unit. Units with zero quantity may be
> omitted.
>
> A duration may be negative. Negative duration strings must begin with `-`.

```lean
public structure Duration where
  val : Int64
```

`Cedar.Spec.Ext.Datetime.Duration.lt` (definition, [line 158](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L158))

```lean
public def Duration.lt (d₁ d₂ : Duration) : Bool
```

`Cedar.Spec.Ext.Datetime.Duration.le` (definition, [line 161](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L161))

```lean
public def Duration.le (d₁ d₂ : Duration) : Bool
```

`Cedar.Spec.Ext.Datetime.Duration.decLt` (instance, [line 170](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L170))

```lean
public instance Duration.decLt (d₁ d₂ : Duration) : Decidable (d₁ < d₂)
```

`Cedar.Spec.Ext.Datetime.Duration.decLe` (instance, [line 173](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L173))

```lean
public instance Duration.decLe (d₁ d₂ : Duration) : Decidable (d₁ ≤ d₂)
```

`Cedar.Spec.Ext.Datetime.MILLISECONDS_PER_SECOND` (definition, [line 180](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L180))

```lean
public def MILLISECONDS_PER_SECOND: Int
```

`Cedar.Spec.Ext.Datetime.MILLISECONDS_PER_MINUTE` (definition, [line 182](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L182))

```lean
public def MILLISECONDS_PER_MINUTE: Int
```

`Cedar.Spec.Ext.Datetime.MILLISECONDS_PER_HOUR` (definition, [line 184](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L184))

```lean
public def MILLISECONDS_PER_HOUR: Int
```

`Cedar.Spec.Ext.Datetime.MILLISECONDS_PER_DAY` (definition, [line 186](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L186))

```lean
public def MILLISECONDS_PER_DAY: Int
```

`Cedar.Spec.Ext.Datetime.duration?` (definition, [line 191](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L191))

> Create a `Duration` from an `Int` representing its internal encoding. Most callers should use higher-level constructors, e.g., `Duration.parse`

```lean
public def duration? (i: Int) : Option Duration
```

`Cedar.Spec.Ext.Datetime.Duration.parse` (definition, [line 249](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L249))

```lean
public def Duration.parse (str : String) : Option Duration
```

`Cedar.Spec.Ext.Datetime.duration` (abbreviation, [line 255](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L255))

```lean
public abbrev duration
```

`Cedar.Spec.Ext.Datetime.offset` (definition, [line 257](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L257))

```lean
public def offset (datetime: Datetime) (duration: Duration) : Option Datetime
```

`Cedar.Spec.Ext.Datetime.durationSince` (definition, [line 260](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L260))

```lean
public def durationSince (datetime other: Datetime) : Option Duration
```

`Cedar.Spec.Ext.Datetime.toDate` (definition, [line 263](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L263))

```lean
public def toDate (datetime: Datetime) : Option Datetime
```

`Cedar.Spec.Ext.Datetime.toTime` (definition, [line 271](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L271))

```lean
public def toTime (datetime: Datetime) : Duration
```

`Cedar.Spec.Ext.Datetime.Duration.toMilliseconds` (definition, [line 280](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L280))

```lean
public def Duration.toMilliseconds (duration: Duration) : Int64
```

`Cedar.Spec.Ext.Datetime.Duration.toSeconds` (definition, [line 283](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L283))

```lean
public def Duration.toSeconds (duration: Duration) : Int64
```

`Cedar.Spec.Ext.Datetime.Duration.toMinutes` (definition, [line 286](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L286))

```lean
public def Duration.toMinutes (duration: Duration) : Int64
```

`Cedar.Spec.Ext.Datetime.Duration.toHours` (definition, [line 289](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L289))

```lean
public def Duration.toHours (duration: Duration) : Int64
```

`Cedar.Spec.Ext.Datetime.Duration.toDays` (definition, [line 292](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L292))

```lean
public def Duration.toDays (duration: Duration) : Int64
```

`Cedar.Spec.Ext.Datetime.durationComponent` (definition, [line 296](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L296))

> Render a duration component as `toString n ++ suffix`.

```lean
public def durationComponent (n : Nat) (suffix : String) : String
```

`Cedar.Spec.Ext.Datetime.Duration.toString` (definition, [line 319](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean#L319))

> Convert a `Duration` to its canonical string representation.
> The format is `[-]<days>d<hours>h<minutes>m<seconds>s<milliseconds>ms`,
> with units maximized and printed largest-to-smallest.
>
> `Cedar.Thm.Duration.parse_toString_roundtrip` proves that parsing
> this representation recovers the original duration.

```lean
public def Duration.toString (d : Duration) : String
```

## Depends on

- [Int64](../../data/int64.md)

## Proof depends on

- [Ext/Util](util.md)

## Sources

- [Cedar/Spec/Ext/Datetime.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Ext/Datetime.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Spec.Ext.Datetime.json)

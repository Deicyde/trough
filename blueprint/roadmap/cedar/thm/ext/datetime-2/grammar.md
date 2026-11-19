---
catalog: module
lean: Cedar.Thm.Datetime.isLeapYear, Cedar.Thm.Datetime.daysInMonth, Cedar.Thm.Datetime.DateComponents, Cedar.Thm.Datetime.DateComponents.syntaxWf, Cedar.Thm.Datetime.DateComponents.constraintsWf, Cedar.Thm.Datetime.DateComponents.asString, Cedar.Thm.Datetime.TimeComponents, Cedar.Thm.Datetime.TimeComponents.syntaxWf, Cedar.Thm.Datetime.TimeComponents.constraintsWf, Cedar.Thm.Datetime.TimeComponents.asString, Cedar.Thm.Datetime.OffsetComponents, Cedar.Thm.Datetime.OffsetComponents.syntaxWf, Cedar.Thm.Datetime.OffsetComponents.constraintsWf, Cedar.Thm.Datetime.OffsetComponents.asString, Cedar.Thm.Datetime.Zone, Cedar.Thm.Datetime.Zone.syntaxWf, Cedar.Thm.Datetime.Zone.constraintsWf, Cedar.Thm.Datetime.Zone.asString, Cedar.Thm.Datetime.TimePart, Cedar.Thm.Datetime.IsWfOptionalMillis, Cedar.Thm.Datetime.TimePart.syntaxWf, Cedar.Thm.Datetime.TimePart.constraintsWf, Cedar.Thm.Datetime.TimePart.asString, Cedar.Thm.Datetime.DatetimeComponents, Cedar.Thm.Datetime.DatetimeComponents.syntaxWf, Cedar.Thm.Datetime.DatetimeComponents.constraintsWf, Cedar.Thm.Datetime.DatetimeComponents.asString, Cedar.Thm.Datetime.DatetimeProduction, Cedar.Thm.Datetime.IsWfDatetime, Cedar.Thm.Datetime.epochDays, Cedar.Thm.Datetime.OffsetComponents.seconds, Cedar.Thm.Datetime.Zone.offsetSeconds, Cedar.Thm.Datetime.DateComponents.toMillis, Cedar.Thm.Datetime.TimePart.toMillis, Cedar.Thm.Datetime.DatetimeComponents.toMillis, Cedar.Thm.Datetime.IsDatetimeValue, Cedar.Thm.Datetime.MILLIS_PER_DAY, Cedar.Thm.Datetime.MIN_UTC_MILLIS, Cedar.Thm.Datetime.MAX_UTC_MILLIS, Cedar.Thm.Datetime.MAX_OFFSET_MILLIS, Cedar.Thm.Datetime.MIN_REPRESENTABLE_MILLIS, Cedar.Thm.Datetime.MAX_REPRESENTABLE_MILLIS, Cedar.Thm.Datetime.fixedWidthNat, Cedar.Thm.Datetime.CanonicalLocalTime, Cedar.Thm.Datetime.canonicalLocalTime?, Cedar.Thm.Datetime.canonicalComponents, Cedar.Thm.Datetime.isFixedDigits, Cedar.Thm.Datetime.DatetimeComponents.syntaxWfB, Cedar.Thm.Datetime.DatetimeComponents.constraintsWfB, Cedar.Thm.Datetime.canonicalComponents?, Cedar.Thm.Datetime.toString?, Cedar.Thm.Datetime.normalize
statement: formalized
proof: formalized
---

# Datetime grammar: definitions

`Cedar.Thm.Ext.Datetime.Grammar`, in [Cedar/Thm/Ext/Datetime/Grammar.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean).

> This file gives a direct, parser-independent transcription of the datetime grammar, its component
> value function, and the declarative relation connecting a string to its epoch-millisecond value.
> Well-formedness takes the same shape as the decimal and duration grammars — the string is the
> rendering of well-formed components — but the datetime grammar describes a date optionally
> followed by a time, a fractional-seconds field, and a zone designator, so the components form a
> nested record rather than a flat sequence of fields.
> The `Digit⁺` predicate `IsDigits` and its fixed-width refinement `IsFixedDigits` (the grammar's
> `Digit{n}`, used for every numeric field here) are shared with the decimal and duration grammars
> and live in `Cedar.Thm.Data.String`, together with the shared `natOf` numeric reader.

> ## Numeric constraints
>
> The grammar's `Constraints` block bounds each numeric field. These are pure arithmetic predicates
> over the field values; `daysInMonth` and `isLeapYear` transcribe the two auxiliary functions the
> day constraint depends on.

`Cedar.Thm.Datetime.isLeapYear` (definition, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L49))

> The grammar's `isLeapYear(y) = (4 | y) ∧ (¬(100 | y) ∨ (400 | y))`, as a decidable `Bool`.

```lean
public def isLeapYear (y : Nat) : Bool
```

`Cedar.Thm.Datetime.daysInMonth` (definition, [line 54](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L54))

> The grammar's `daysInMonth(y, m)`: 30 for April/June/September/November, 28 or 29 for
> February depending on the leap year, and 31 otherwise.

```lean
public def daysInMonth (y m : Nat) : Nat
```

> ## Components
>
> Each nonterminal of the grammar becomes a record of its fixed-width digit fields. A `syntaxWf`
> predicate pins the field widths (`Digit{n}`) and a `constraintsWf` predicate imposes the numeric
> bounds from the grammar's `Constraints` block.

`Cedar.Thm.Datetime.DateComponents` (structure, [line 66](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L66))

> The grammar's `Date ::= YYYY '-' MM '-' DD`.

```lean
public structure DateComponents where
  year : String
  month : String
  day : String
```

`Cedar.Thm.Datetime.DateComponents.syntaxWf` (definition, [line 72](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L72))

> `YYYY` is `Digit{4}`; `MM` and `DD` are `Digit{2}`.

```lean
public def DateComponents.syntaxWf (d : DateComponents) : Prop
```

`Cedar.Thm.Datetime.DateComponents.constraintsWf` (definition, [line 78](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L78))

> The month/day bounds: `01 ≤ MM ≤ 12` and `01 ≤ DD ≤ daysInMonth(YYYY, MM)`.

```lean
public def DateComponents.constraintsWf (d : DateComponents) : Prop
```

`Cedar.Thm.Datetime.DateComponents.asString` (definition, [line 84](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L84))

> Render a date as `YYYY '-' MM '-' DD`.

```lean
public def DateComponents.asString (d : DateComponents) : String
```

`Cedar.Thm.Datetime.TimeComponents` (structure, [line 88](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L88))

> The grammar's `Time ::= hh ':' mm ':' ss`.

```lean
public structure TimeComponents where
  hours : String
  minutes : String
  seconds : String
```

`Cedar.Thm.Datetime.TimeComponents.syntaxWf` (definition, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L94))

> `hh`, `mm`, and `ss` are each `Digit{2}`.

```lean
public def TimeComponents.syntaxWf (t : TimeComponents) : Prop
```

`Cedar.Thm.Datetime.TimeComponents.constraintsWf` (definition, [line 100](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L100))

> The time bounds: `00 ≤ hh ≤ 23`, `00 ≤ mm ≤ 59`, `00 ≤ ss ≤ 59`.

```lean
public def TimeComponents.constraintsWf (t : TimeComponents) : Prop
```

`Cedar.Thm.Datetime.TimeComponents.asString` (definition, [line 106](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L106))

> Render a time as `hh ':' mm ':' ss`.

```lean
public def TimeComponents.asString (t : TimeComponents) : String
```

`Cedar.Thm.Datetime.OffsetComponents` (structure, [line 111](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L111))

> The grammar's `Offset ::= ('+' | '-') hh mm`. `negative` records the sign character;
> `hours` and `mm` reuse the `hh`/`mm` nonterminals of `Time`.

```lean
public structure OffsetComponents where
  negative : Bool
  hours : String
  minutes : String
```

`Cedar.Thm.Datetime.OffsetComponents.syntaxWf` (definition, [line 117](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L117))

> The offset's `hh` and `mm` are each `Digit{2}`, matching the `Time` nonterminals.

```lean
public def OffsetComponents.syntaxWf (o : OffsetComponents) : Prop
```

`Cedar.Thm.Datetime.OffsetComponents.constraintsWf` (definition, [line 123](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L123))

> Because the offset reuses the `hh`/`mm` nonterminals, it inherits their bounds:
> `00 ≤ hh ≤ 23` and `00 ≤ mm ≤ 59`.

```lean
public def OffsetComponents.constraintsWf (o : OffsetComponents) : Prop
```

`Cedar.Thm.Datetime.OffsetComponents.asString` (definition, [line 128](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L128))

> Render an offset as `('+' | '-') hh mm`.

```lean
public def OffsetComponents.asString (o : OffsetComponents) : String
```

`Cedar.Thm.Datetime.Zone` (inductive type, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L133))

> The zone designator that terminates a datetime with a time: either the UTC marker `'Z'`
> (`Date 'T' Time 'Z'` / `Date 'T' Time '.' SSS 'Z'`) or an explicit `Offset`.

```lean
public inductive Zone where
  | utc
  | offset (o : OffsetComponents)
```

`Cedar.Thm.Datetime.Zone.syntaxWf` (definition, [line 138](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L138))

> A UTC marker imposes nothing; an offset must have well-formed digit fields.

```lean
public def Zone.syntaxWf : Zone → Prop
```

`Cedar.Thm.Datetime.Zone.constraintsWf` (definition, [line 143](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L143))

> A UTC marker imposes nothing; an offset must satisfy the `hh`/`mm` bounds.

```lean
public def Zone.constraintsWf : Zone → Prop
```

`Cedar.Thm.Datetime.Zone.asString` (definition, [line 148](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L148))

> Render the zone: `'Z'` for UTC, otherwise the offset's `('+' | '-') hh mm`.

```lean
public def Zone.asString : Zone → String
```

`Cedar.Thm.Datetime.TimePart` (structure, [line 155](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L155))

> The time-bearing tail of a datetime: a `Time`, an optional fractional-seconds field `SSS`
> (`'.' SSS`), and a `Zone`. Absent `SSS` (`none`) corresponds to the forms without a
> `'.' SSS`; `some` corresponds to the `'.' SSS` forms.

```lean
public structure TimePart where
  time : TimeComponents
  millis : Option String
  zone : Zone
```

`Cedar.Thm.Datetime.IsWfOptionalMillis` (definition, [line 162](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L162))

> Lift `IsFixedDigits 3` (the grammar's `SSS ::= Digit{3}`) to the optional field:
> an absent `SSS` is trivially valid.

```lean
public def IsWfOptionalMillis : Option String → Prop
```

`Cedar.Thm.Datetime.TimePart.syntaxWf` (definition, [line 167](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L167))

> The time, the optional `SSS`, and the zone are each well-formed.

```lean
public def TimePart.syntaxWf (tp : TimePart) : Prop
```

`Cedar.Thm.Datetime.TimePart.constraintsWf` (definition, [line 174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L174))

> The time and zone satisfy their numeric bounds. `SSS` is unconstrained (`000`–`999` are all
> valid), so it contributes no numeric constraint.

```lean
public def TimePart.constraintsWf (tp : TimePart) : Prop
```

`Cedar.Thm.Datetime.TimePart.asString` (definition, [line 178](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L178))

> Render the tail: `'T' Time ['.' SSS] Zone`, so `some sss` inserts `'.' sss`.

```lean
public def TimePart.asString (tp : TimePart) : String
```

`Cedar.Thm.Datetime.DatetimeComponents` (structure, [line 186](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L186))

> A datetime is a `Date` optionally followed by a time-bearing tail. `none` is the date-only
> form `Date`; `some tp` covers the four `Date 'T' Time …` forms, with the presence of `SSS`
> and the choice of `Zone` selecting among them.

```lean
public structure DatetimeComponents where
  date : DateComponents
  time : Option TimePart
```

`Cedar.Thm.Datetime.DatetimeComponents.syntaxWf` (definition, [line 191](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L191))

> Every present component has well-formed digit fields.

```lean
public def DatetimeComponents.syntaxWf (c : DatetimeComponents) : Prop
```

`Cedar.Thm.Datetime.DatetimeComponents.constraintsWf` (definition, [line 195](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L195))

> Every present component satisfies its numeric bounds.

```lean
public def DatetimeComponents.constraintsWf (c : DatetimeComponents) : Prop
```

`Cedar.Thm.Datetime.DatetimeComponents.asString` (definition, [line 202](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L202))

> Canonical string representation: the date, followed by the time-bearing tail when present.
> Phrasing well-formedness existentially over `asString` (below) bakes the grammar's structure
> in for free — the separators, the fixed field order, and the choice among the five top-level
> forms all follow from the shape of the witnessing record.

```lean
public def DatetimeComponents.asString (c : DatetimeComponents) : String
```

`Cedar.Thm.Datetime.DatetimeProduction` (definition, [line 207](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L207))

> The datetime grammar production witnessed by a syntactically and numerically valid component
> record and its rendering.

```lean
public def DatetimeProduction (str : String) (components : DatetimeComponents) : Prop
```

`Cedar.Thm.Datetime.IsWfDatetime` (definition, [line 213](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L213))

> A datetime string is well-formed exactly when it has a valid grammar production.

```lean
public def IsWfDatetime (str : String) : Prop
```

> ## Value relation
>
> The component value functions below transcribe the grammar's date/time →
> milliseconds-since-epoch formula. `IsDatetimeValue str v` then reuses the same witnesses as
> `IsWfDatetime` and states that their denotation is `v`. No second string parser is part of the
> trusted grammar specification.

`Cedar.Thm.Datetime.epochDays` (definition, [line 226](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L226))

> Day count of a date since the Unix epoch (1970-01-01), via Howard Hinnant's `days_from_civil`
> algorithm. This transcribes `Std.Time.PlainDate.toEpochDay` over raw `Nat` fields, independently
> of the `Std.Time` date type.

```lean
public def epochDays (year month day : Nat) : Int
```

`Cedar.Thm.Datetime.OffsetComponents.seconds` (definition, [line 238](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L238))

> The offset's signed second count: `± (hh × 3600 + mm × 60)`. Positive offsets (`+hhmm`) are
> east of UTC, so the parser subtracts this to normalize to UTC.

```lean
public def OffsetComponents.seconds (o : OffsetComponents) : Int
```

`Cedar.Thm.Datetime.Zone.offsetSeconds` (definition, [line 244](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L244))

> Signed UTC-normalization seconds contributed by a zone: `0` for the `'Z'` marker, and the
> offset's second count otherwise.

```lean
public def Zone.offsetSeconds : Zone → Int
```

`Cedar.Thm.Datetime.DateComponents.toMillis` (definition, [line 249](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L249))

> Milliseconds-since-epoch value of a well-formed date's midnight UTC.

```lean
public def DateComponents.toMillis (d : DateComponents) : Int
```

`Cedar.Thm.Datetime.TimePart.toMillis` (definition, [line 255](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L255))

> Milliseconds-since-epoch value of a datetime's time-bearing tail relative to its date's
> midnight: the wall-clock time in milliseconds, less the zone offset (converting to UTC),
> plus the optional fractional-seconds field.

```lean
public def TimePart.toMillis (tp : TimePart) : Int
```

`Cedar.Thm.Datetime.DatetimeComponents.toMillis` (definition, [line 263](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L263))

> Milliseconds-since-epoch value of a whole datetime: the date's midnight plus the time-bearing
> tail's contribution (`0` for the date-only form).

```lean
public def DatetimeComponents.toMillis (c : DatetimeComponents) : Int
```

`Cedar.Thm.Datetime.IsDatetimeValue` (definition, [line 272](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L272))

> `v` is the value of the datetime literal `str`: `str` is the rendering of syntactically and
> numerically well-formed datetime components, and `v` is their epoch-millisecond denotation.
>
> The existential supplies the grammar decomposition directly, so this relation does not
> re-parse the string. It is total on well-formed syntax (`wf_iff_exists_value`) and
> single-valued (`isDatetimeValue_unique`).

```lean
public def IsDatetimeValue (str : String) (v : Int) : Prop
```

> ## Canonical serialization
>
> `Datetime` stores an arbitrary `Int64` millisecond value, while the concrete syntax restricts
> years to `0000` through `9999`. Serialization is therefore partial. It always emits the most
> explicit grammar form, `YYYY-MM-DDTHH:mm:ss.SSS±HHMM`, using a zero offset when UTC is in range and
> the smallest minute offset needed at either endpoint. All decimal fields are rendered here rather
> than through `Std.Time`'s formatter.

`Cedar.Thm.Datetime.MILLIS_PER_DAY` (definition, [line 286](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L286))

> …

```lean
public def MILLIS_PER_DAY : Int
```

`Cedar.Thm.Datetime.MIN_UTC_MILLIS` (definition, [line 289](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L289))

> Smallest millisecond value whose UTC civil date has a four-digit nonnegative year.

```lean
public def MIN_UTC_MILLIS : Int
```

`Cedar.Thm.Datetime.MAX_UTC_MILLIS` (definition, [line 292](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L292))

> Largest millisecond value whose UTC civil date has a four-digit nonnegative year.

```lean
public def MAX_UTC_MILLIS : Int
```

`Cedar.Thm.Datetime.MAX_OFFSET_MILLIS` (definition, [line 295](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L295))

> Largest legal timezone-offset magnitude, `23:59`, in milliseconds.

```lean
public def MAX_OFFSET_MILLIS : Int
```

`Cedar.Thm.Datetime.MIN_REPRESENTABLE_MILLIS` (definition, [line 298](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L298))

> Exact lower endpoint representable by the datetime grammar.

```lean
public def MIN_REPRESENTABLE_MILLIS : Int
```

`Cedar.Thm.Datetime.MAX_REPRESENTABLE_MILLIS` (definition, [line 301](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L301))

> Exact upper endpoint representable by the datetime grammar.

```lean
public def MAX_REPRESENTABLE_MILLIS : Int
```

`Cedar.Thm.Datetime.fixedWidthNat` (definition, [line 304](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L304))

> Render a natural number as an ASCII decimal string padded with leading zeroes to `width`.

```lean
public def fixedWidthNat (width n : Nat) : String
```

`Cedar.Thm.Datetime.CanonicalLocalTime` (structure, [line 308](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L308))

> The local millisecond value and explicit offset selected for canonical serialization.

```lean
public structure CanonicalLocalTime where
  localMillis : Int
  offsetNegative : Bool
  offsetMinutes : Nat
```

`Cedar.Thm.Datetime.canonicalLocalTime?` (definition, [line 315](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L315))

> Select UTC whenever possible. Immediately outside the UTC civil range, select the smallest
> minute offset that moves the local civil time back into that range.

```lean
public def canonicalLocalTime? (value : Int) : Option CanonicalLocalTime
```

`Cedar.Thm.Datetime.canonicalComponents` (definition, [line 342](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L342))

> Build canonical grammar components from an in-range local millisecond value and its selected
> explicit offset. `PlainDate.ofEpochDay` supplies numeric calendar fields only; rendering is
> performed by `fixedWidthNat`.

```lean
public def canonicalComponents (localTime : CanonicalLocalTime) : DatetimeComponents
```

`Cedar.Thm.Datetime.isFixedDigits` (definition, [line 374](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L374))

> Executable mirror of `IsFixedDigits`.

```lean
public def isFixedDigits (width : Nat) (s : String) : Bool
```

`Cedar.Thm.Datetime.DatetimeComponents.syntaxWfB` (definition, [line 378](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L378))

> Executable mirror of `DatetimeComponents.syntaxWf`.

```lean
public def DatetimeComponents.syntaxWfB (components : DatetimeComponents) : Bool
```

`Cedar.Thm.Datetime.DatetimeComponents.constraintsWfB` (definition, [line 394](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L394))

> Executable mirror of `DatetimeComponents.constraintsWf`.

```lean
public def DatetimeComponents.constraintsWfB (components : DatetimeComponents) : Bool
```

`Cedar.Thm.Datetime.canonicalComponents?` (definition, [line 415](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L415))

> Produce certified canonical components for a datetime value. The final check is deliberately
> stated in terms of the owned grammar and value function, insulating serialization from
> `Std.Time` formatting behavior.

```lean
public def canonicalComponents? (d : Cedar.Spec.Ext.Datetime) : Option DatetimeComponents
```

`Cedar.Thm.Datetime.toString?` (definition, [line 426](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L426))

> Canonical partial serializer for datetime values. Every successful result has the fixed form
> `YYYY-MM-DDTHH:mm:ss.SSS±HHMM`.

```lean
public def toString? (d : Cedar.Spec.Ext.Datetime) : Option String
```

`Cedar.Thm.Datetime.normalize` (definition, [line 432](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean#L432))

> Canonical-form normalizer: parse the string and re-serialize. Returns `none` for malformed
> inputs (mirror of the decimal and duration normalizers); because serialization is partial the
> re-serialization is a `bind` rather than the total `map` used there.

```lean
public def normalize (str : String) : Option String
```

## Depends on

- [Datetime](../../../spec/ext-2/datetime.md)
- [String](../../data/string.md)

## Sources

- [Cedar/Thm/Ext/Datetime/Grammar.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Grammar.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Ext.Datetime.Grammar.json)

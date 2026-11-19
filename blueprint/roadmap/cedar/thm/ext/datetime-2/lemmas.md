---
catalog: module
lean: Cedar.Thm.Datetime.isDatetimeValue_unique, Cedar.Thm.Datetime.toString?_eq_none_of_not_representable
statement: formalized
proof: formalized
---

# Datetime/Lemmas

`Cedar.Thm.Ext.Datetime.Lemmas`, in [Cedar/Thm/Ext/Datetime/Lemmas.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Lemmas.lean).

> # Datetime grammar roundtrip lemmas
>
> The trusted grammar specification carries component witnesses directly through
> `IsDatetimeValue`. The small structural decoder below is therefore proof-local: it establishes
> that a well-formed rendering determines those witnesses uniquely. The lemmas prove its roundtrip
> nonterminal by nonterminal, using digit-field separator-freeness from `IsDigits`, and culminate in
> `parseComponents_asString`.

`Cedar.Thm.Datetime.isDatetimeValue_unique` (theorem, [line 448](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Lemmas.lean#L448))

> The declarative value relation is single-valued: a datetime string denotes at most one
> epoch-millisecond value.

```lean
public theorem isDatetimeValue_unique {str : String} {v₁ v₂ : Int}
    (h₁ : IsDatetimeValue str v₁) (h₂ : IsDatetimeValue str v₂) : v₁ = v₂
```

> ## Canonical serialization certificates

`Cedar.Thm.Datetime.toString?_eq_none_of_not_representable` (theorem, [line 547](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Lemmas.lean#L547))

> Values outside the exact grammar-representable millisecond interval do not serialize: the
> canonical local-time selection returns `none`, so `toString?` short-circuits.

```lean
public theorem toString?_eq_none_of_not_representable (d : Cedar.Spec.Ext.Datetime)
    (h : d.val.toInt < MIN_REPRESENTABLE_MILLIS ∨ MAX_REPRESENTABLE_MILLIS < d.val.toInt) :
    toString? d = none
```

> ## Foundational `Parsec` symbolic-evaluation lemmas
>
> `Std.Time.GenericFormat.parse` is built on the `Std.Internal.Parsec` combinator library over the
> string iterator `It := Σ s : String, s.Pos`. The alternation-value bridge below
> (`stdTime_alternation_value`) ultimately needs to symbolically evaluate that parser on the
> rendering of well-formed components. These lemmas are the base of that evaluation ladder: they give
> the one-step reduction of the primitive combinators (`any`, monadic `bind`, `satisfy`) on the
> string iterator, and — on top of them — the `exactlyChars` walk lemma (`exactlyChars_digits`),
> which shows a fixed-width run of digit characters is consumed exactly and advances the iterator past
> it. They are parser-agnostic (nothing datetime-specific).
>
> Built on top of these are the evaluation lemmas for `parseNum`/`parseWith`/`parseWithDate`,
> `DateBuilder.build`, and `toTimestamp` that follow further below.

> ### Fraction (millisecond) field: right-padded digit arithmetic
>
> The `.S (.truncated 3)` modifier reads three digits, right-pads to nine `'0'`s (via `rightPadAscii`), and
> converts to a nanosecond count — so `SSS` milliseconds become `SSS × 10⁶` nanoseconds. These helpers
> establish that `String.toNat!` of a digit string with `k` appended zeros multiplies its value by
> `10ᵏ`, then `parseWith_fraction` assembles the modifier reduction.

> ## Assembling the DateOnly parser: `parseWithDate` sequence
>
> These lemmas lift the primitive rungs to arbitrary interior positions (the `_at` suffix, via
> the `String.Pos.Splits` API) and thread the five `parseWithDate` steps of the `yyyy-MM-dd`
> format through a `DateBuilder`, culminating in `parseWithDate_dateOnly`.

> ## Position-general foundations
>
> The existing repo lemmas (`parseWith_year`, `pstring_prefix`, …) are stated with the iterator at
> `startPos` of `sub ++ rest`. To compose the five DateOnly parser steps we need to run each parser at
> an *interior* position of the single fixed string. The `String.Pos.Splits` API makes this clean:
> `exactlyChars_go_digits` is already position-general, so we lift each rung to an "at position `p`"
> form, where `p.Splits pre (field ++ rest)`.

> ### Offset parsing (`.x .hourMinute`)
>
> The timezone-offset modifier `±hhmm` (`DateWithOffset`/`DateWithOffsetAndMillis`) reduces to
> `Std.Time.parseOffset .yes .no false`: a sign character (`<|>` alternation), two bounded 2-digit
> fields (no colon, since `withColon = false`), and no seconds. These helpers give the `pchar`,
> `seqRight` (`*>`), and `orElse` (`<|>`) reductions, then `parseWith_hourMinute_at` assembles them.

> ## `parseWithDate` single-step lemmas (position-general)
>
> Each combines the `parseWithDate` `do`-block reduction with the corresponding `parseWith`/`pstring`
> position-general lemma, producing the advanced builder and threaded position.

> ## `DateBuilder.build` value for the date-only form
>
> With the `parseWithDate` sequence delivering a `DateBuilder` carrying the parsed `y`/`M`/`d`
> fields, the remaining step is `build .any`: it discharges the `year.Valid month day` guard from the
> grammar constraints, constructs a midnight-UTC `DateTime`, and its epoch-millisecond value is
> `epochDays … × 86400000`. The helper lemmas below cover the integer `tdiv`/`tmod` recovery under the
> `Duration` sign invariant, the `Std.Time` ↔ grammar validity bridges (`isLeap`/`days`), and the
> midnight-timestamp arithmetic.

> ## General timestamp value: nonzero time and nonzero offset
>
> The date-only build collapsed the timestamp through a zero-offset midnight zone. The time-bearing
> forms need the general computation: a nonzero wall-clock time and an offset→UTC subtraction. These
> lemmas generalize `midnight_toTimestampAssumingUTC`/`ofPlainDateTime_zero_timestamp`, culminating in
> `zoned_value` — the epoch-millisecond value of a `DateTime` built from a plain date+time against
> a fixed-offset zone.

> ## Date-only slice: `DateOnly.parse` value
>
> Composing `parseWithDate_dateOnly` (the format-part sequence into a filled `DateBuilder`) and
> `build_dateOnly_value` (the builder's epoch-ms value) through the `GenericFormat.parse` wrapper —
> `parser.go`, the trailing `<* eof`, and `.run`/`.toOption` — gives the value of `DateOnly.parse` on
> a well-formed date string. This closes the `c.time = none` case of `stdTime_alternation_value`.

> ## DateUTC slice: `DateUTC.parse` value
>
> The time-bearing analogue of the date-only slice, for the `yyyy-MM-dd'T'HH:mm:ss'Z'` form: the
> filled builder (`y`/`M`/`d`/`H`/`m`/`s`) builds through the general `zoned_value` at a
> zero-offset UTC zone, and `DateUTC.parse` yields `c.toMillis`.

> ## DateUTCWithMillis slice: `DateUTCWithMillis.parse` value
>
> The `.SSS` millisecond analogue of the DateUTC slice (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`): adds the
> fraction field before `Z`, with a nonzero `nano = natOf sss * 10⁶` fed to `zoned_value` as
> `ms = natOf sss`. The `digit_le`/`natOf_le_999` helpers bound a 3-digit `SSS` field.

> ## STEP A: step_fraction

> ## STEP B: parseWithDate_dateUTCWithMillis (14-step sequence)

> ## STEP C: build_dateUTCWithMillis_value

> ## STEP D: dateUTCWithMillis_parse value

> ## DateWithOffset slice: `DateWithOffset.parse` value
>
> The offset-bearing analogue of the DateUTC slice, for the `yyyy-MM-dd'T'HH:mm:ssxx` form: the final
> format part is the `±hhmm` offset (via `step_offset`) instead of the `Z` literal, and the built
> zone has a *nonzero* offset, exercising `zoned_value`'s offset→UTC subtraction.

> ## DateWithOffsetAndMillis slice: `DateWithOffsetAndMillis.parse` value
>
> The last form (`yyyy-MM-dd'T'HH:mm:ss.SSSxx`) — the union of the `.SSS` and offset wrinkles: it
> merges the DateUTCWithMillis and DateWithOffset slices (fraction field + nonzero-offset zone).

> ## DateWithOffsetAndMillis: parseWithDate sequence (14 steps, ending in step_offset)

> ## DateWithOffsetAndMillis: build value (nonzero millis AND nonzero offset)

> ## DateWithOffsetAndMillis: parse value

> ## Bridge to `Std.Time`: `Datetime.parse` ↔ the grammar value relation
>
> The lemmas above (roundtrip + `Parsec` foundations) are the parser-independent half — they relate
> `IsWfDatetime`, `IsDatetimeValue`, the proof-local structural decoder, and the primitive `Parsec`
> combinators, all of which we control. The lemmas below are the missing half: they relate the
> *actual* `Datetime.parse` (which delegates to `Std.Time.GenericFormat.parse`) to those definitions.
> Each is a self-contained obligation about `Std.Time`'s behavior on the five fixed datetime formats;
> discharging them requires symbolically evaluating `Std.Time`'s well-founded-recursion parsers — the
> `Parsec` foundations above are the first rung of that ladder (see the note in the aggregator).
>
> The decomposition mirrors the structure of `Datetime.parse`:
> 1. three Boolean guards (`dateContainsLeapSeconds`, `checkOffsetLen`, `tzOffsetMinsLt60`);
> 2. the five-way format alternation `DateOnly.parse <|> … <|> DateWithOffsetAndMillis.parse`;
> 3. the offset-range check `< MAX_OFFSET_SECONDS` and the final `datetime?` (i.e. `Int64.ofInt?`).

> ### Packaged walk steps
>
> Every `*_full_inv` / `*_go_preserves` walk repeats the same ~20-line block per format item:
> `go_cons_app`, case the `parseWithDate`, thread string-preservation, expose the underlying
> `parseWith`/`pstring`, and `injection` the positions. These two lemmas package one step each
> (modifier / string separator), so a walk step becomes a single
> `obtain ⟨p', v, hstep, hgo⟩ := go_step_modifier … hpres hgo`. The modifier version takes the
> field's string-preservation fact as a hypothesis (each field has its own `*_preserves` lemma).

> ## Phase 1: time-field string preservation helpers

> ## Phase 2: DateUTC full parse inversion

> ## Phase 3: build inversion, parse-ok inversion, and wf assembly

> ## Phase 3: DateWithOffset (the `±hhmm` offset tail)

> ## Except `<|>` reductions

> ## Master "parse produces error" helpers
>
> `GenericFormat.parse F s = (parser F.string F.config .any <* eof).run s`. Two ways the alternation's
> earlier parsers fail on a wrong-form string:
>   (A) the inner `parser` itself errors (a `pstring`/offset step diverges); or
>   (B) the inner `parser` succeeds but *not at end of string* (leftover), so the trailing `<* eof`
>       rejects.

> ## DateOnly fails on a time-bearing string
>
> `c.asString = c.date.asString ++ tp.asString` with `tp.asString = "T" ++ ...` nonempty. The DateOnly
> format's `parser.go` threads the five date steps identically (they only inspect the date prefix),
> `build` succeeds, but the resulting position sits right after the date (before `"T"`), which is not
> `endPos`. So `<* eof` rejects.

> ## Next-part failure primitives

> ## Shared `yyyy-MM-dd'T'HH:mm:ss` prefix threading
>
> All four time-bearing formats share the 11-part prefix `[y,"-",M,"-",d,"T",H,":",m,":",s]`. This
> lemma threads that prefix on `c.date.asString ++ "T" ++ tp.time.asString ++ tail` (any `tail`, any
> format suffix `suf`), leaving `parser.go` positioned after the seconds field with the six-field
> builder, ready to run `suf`.

> ## Tail structure after `time.asString`
>
> `c.asString = c.date.asString ++ "T" ++ tp.time.asString ++ tail`, where
> `tail = (millis-part) ++ tp.zone.asString`. We expose `tail = singleton c₀ ++ rest` and identify the
> leading char `c₀` for each form.

> ## Wrong-form failure via prefix + next-part mismatch
>
> Given a `.string (singleton lc)` as the first suffix part, if the tail (after `ss`) starts with
> `c₀ ≠ lc`, the format `F = prefix ++ [.string (singleton lc), ...]` errors on `c.asString`.

> ## Tail leading-char decompositions
>
> Identify `tail = singleton c₀ ++ rest` for each shape.

> ## Per-parser wrong-form failures

> ## Case 1 scaffolding

> ## Main theorem: 5-way case split

> ## Forward parse-guard lemmas
>
> `Datetime.parse` applies three Boolean guards (`dateContainsLeapSeconds`, `checkOffsetLen`,
> `tzOffsetMinsLt60`) before the format alternation. On a well-formed rendering `c.asString` all three
> pass; these lemmas discharge them for `parse_complete`. The offset-minutes guard reduces to the
> grammar bound `natOf o.minutes ≤ 59`, which requires the `String.Slice`-level fact that
> `toNat?` and `isNat` depend only on the character list.

> ## Leap-seconds guard
>
> `dateContainsLeapSeconds str` reads the two bytes at positions 17 and 18 (the seconds field of a
> `Date 'T' Time …` rendering, whose prefix `yyyy-MM-ddThh:mm:` is exactly 17 ASCII bytes) and rejects
> `"…60…"`. On a well-formed rendering it always returns `false`: date-only strings are too short
> (length 10 < 20), and for time-bearing strings the grammar bounds the seconds field by `59`, so it
> is never `"60"`.

> ## Int64-range bound for the datetime value
>
> The grammar bounds a datetime to 4-digit years and `±23:59` offsets, so `toMillis` always fits in
> `Int64`. We prove this by bounding `epochDays` (the Hinnant forward algorithm) and then the linear
> `toMillis` combination. `omega` treats `Int.tdiv`/`Int.tmod` as opaque, so each `tdiv` site is fed the
> Euclidean identity `Int.mul_tdiv_add_tmod` plus `tmod` sign/magnitude facts.

## Depends on

- [Datetime grammar: definitions](grammar.md)

## Sources

- [Cedar/Thm/Ext/Datetime/Lemmas.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Ext/Datetime/Lemmas.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Ext.Datetime.Lemmas.json)

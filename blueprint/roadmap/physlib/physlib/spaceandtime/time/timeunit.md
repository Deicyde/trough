---
declaration: module
origin: cited
lean: TimeUnit, TimeUnit.seconds, TimeUnit.femtoseconds, TimeUnit.picoseconds, TimeUnit.nanoseconds, TimeUnit.microseconds, TimeUnit.milliseconds, TimeUnit.centiseconds
statement: formalized
proof: formalized
---

# Units on time

The module `Physlib.SpaceAndTime.Time.TimeUnit`, [Physlib/SpaceAndTime/Time/TimeUnit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean): 22 declarations (1 instance with no name), 13 with a docstring.

> A unit of time corresponds to a choice of translationally-invariant
> metric on the time manifold. Such a choice is (non-canonically) equivalent to a
> choice of positive real number. We define the type `TimeUnit` to be equivalent to the
> positive reals.
>
> On `TimeUnit` there is an instance of division giving a real number, corresponding to the
> ratio of the two scales of time unit.
>
> We define `HasTimeDimension` to be a property of a function from `TimeUnit` to a type `M`
> which is a function that scales with the time unit with respect to the rational power `d`.
>
> To define specific time units, we first state the existence of a
> a given time unit, and then construct all other time units from it. We choose to state the
> existence of the time unit of seconds, and construct all other time units from that.

**`TimeUnit`**, a structure, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L36).

> The choices of translationally-invariant metrics on the time manifold.
> Such a choice corresponds to a choice of units for time.

```lean
structure TimeUnit : Type where
  /-- The underlying scale of the unit. -/
  val : ℝ
  property : 0 < val
```

**An instance with no name**, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L41).

```lean
instance : PositiveRealUnitCore TimeUnit
```

## Specific choices of time units

> To define a specific time units.
> We first define the notion of a second to correspond to the length unit with underlying value
> equal to `1`. This is really down to a choice in the isomorphism between the set of metrics
> on the time manifold and the positive reals.
> From this choice of second, we can define other length units by scaling second.

**`TimeUnit.seconds`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L66).

> The definition of a time unit of seconds.

```lean
def seconds : TimeUnit
```

**`TimeUnit.femtoseconds`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L69).

> The time unit of femtoseconds (10⁻¹⁵ of a second).

```lean
noncomputable def femtoseconds : TimeUnit
```

**`TimeUnit.picoseconds`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L72).

> The time unit of picoseconds (10⁻¹² of a second).

```lean
noncomputable def picoseconds : TimeUnit
```

**`TimeUnit.nanoseconds`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L75).

> The time unit of nanoseconds (10⁻⁹ of a second).

```lean
noncomputable def nanoseconds : TimeUnit
```

**`TimeUnit.microseconds`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L78).

> The time unit of microseconds (10⁻⁶ of a second).

```lean
noncomputable def microseconds : TimeUnit
```

**`TimeUnit.milliseconds`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L81).

> The time unit of milliseconds (10⁻³ of a second).

```lean
noncomputable def milliseconds : TimeUnit
```

**`TimeUnit.centiseconds`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L84).

> The time unit of centiseconds (10⁻² of a second).

```lean
noncomputable def centiseconds : TimeUnit
```

**`TimeUnit.deciseconds`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L87).

> The time unit of deciseconds (10⁻¹ of a second).

```lean
noncomputable def deciseconds : TimeUnit
```

**`TimeUnit.minutes`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L90).

> The time unit of minutes.

```lean
noncomputable def minutes : TimeUnit
```

**`TimeUnit.hours`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L93).

> The time unit of hours.

```lean
noncomputable def hours : TimeUnit
```

**`TimeUnit.days`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L96).

> The time unit of 24 hour days.

```lean
noncomputable def days : TimeUnit
```

**`TimeUnit.weeks`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L99).

> The time unit of 7 day weeks.

```lean
noncomputable def weeks : TimeUnit
```

## Relations between time units

**`TimeUnit.minutes_div_seconds`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L107).

```lean
lemma minutes_div_seconds : minutes / seconds = (60 : ℝ≥0)
```

**`TimeUnit.hours_div_seconds`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L110).

```lean
lemma hours_div_seconds : hours / seconds = (3600 : ℝ≥0)
```

**`TimeUnit.days_div_seconds`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L113).

```lean
lemma days_div_seconds : days / seconds = (86400 : ℝ≥0)
```

**`TimeUnit.weeks_div_seconds`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L116).

```lean
lemma weeks_div_seconds : weeks / seconds = (604800 : ℝ≥0)
```

**`TimeUnit.days_div_minutes`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L119).

```lean
lemma days_div_minutes : days / minutes = (1440 : ℝ≥0)
```

**`TimeUnit.weeks_div_minutes`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L125).

```lean
lemma weeks_div_minutes : weeks / minutes = (10080 : ℝ≥0)
```

**`TimeUnit.days_div_hours`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L131).

```lean
lemma days_div_hours : days / hours = (24 : ℝ≥0)
```

**`TimeUnit.weeks_div_hours`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean#L137).

```lean
lemma weeks_div_hours : weeks / hours = (168 : ℝ≥0)
```

## Depends on

- [A. Shared arithmetic for positive-real unit types](../../units/positiverealunit.md)

## Sources

- [Physlib/SpaceAndTime/Time/TimeUnit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeUnit.lean)

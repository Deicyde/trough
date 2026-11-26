---
declaration: module
origin: cited
lean: Time.CaesiumClock.elapsedCycles, Time.CaesiumClock.elapsedCycles_add, Time.CaesiumClock.cyclesPerSecond, Time.CaesiumClock.IsCalibrated, Time.CaesiumClock.isCalibrated_iff_rate, Time.CaesiumClock.unitOfReadings, Time.CaesiumClock.isCalibrated_iff_eq_unitOfReadings, Time.CaesiumClock.elapsed_seconds
statement: formalized
proof: formalized
---

# Measuring elapsed time with a caesium clock

The module `PhyslibAlpha.SpaceAndTime.Time.CaesiumClock`, [PhyslibAlpha/SpaceAndTime/Time/CaesiumClock.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/Time/CaesiumClock.lean): 9 declarations, 9 with a docstring; 1 private, not shown.

> An ideal clock measures a duration by the change in phase of a reference oscillation.

## i. Overview

> The SI second fixes the frequency of the radiation corresponding to the unperturbed ground-state
> hyperfine transition of the caesium-133 atom. One second spans exactly 9 192 631 770 periods.
> We model the accumulated phase in cycles, allowing fractional and signed differences.
>
> For an ideal uniform clock the phase is an affine function of proper time along the clock.
> The coordinate on `Time` has a fixed but arbitrary unit. Identifying an observed phase with
> this ideal radiation is the physical input. Two distinct readings then determine the size of
> the coordinate unit in SI seconds. The observation interval need not itself last one second,
> and its endpoints need no absolute phase or time origin.

## ii. Key results

> - `isCalibrated_iff_rate` relates a calibration observation to the rate in the chosen unit.
> - `isCalibrated_iff_eq_unitOfReadings` recovers the unique time unit from two phase readings.
> - `elapsed_seconds` recovers signed elapsed time in seconds from two phase readings.
> - `one_second_iff` characterizes one-second intervals by the defining cycle count.

## iv. References

> - BIPM, *The International System of Units (SI)*, 9th edition, section 2.3.1
>   [ref: bipm\_si\_brochure\_2019].

## A. Phase readings and calibration

**`Time.CaesiumClock.elapsedCycles`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/Time/CaesiumClock.lean#L58).

> The signed number of cycles between two readings, from unwrapped phase readings in cycles.

```lean
def elapsedCycles {E : Type*} (phase : E → ℝ) (start stop : E) : ℝ
```

**`Time.CaesiumClock.elapsedCycles_add`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/Time/CaesiumClock.lean#L62).

> Cycle counts add when two measurement intervals are joined.

```lean
lemma elapsedCycles_add {E : Type*} (phase : E → ℝ) (a b c : E) :
    elapsedCycles phase a b + elapsedCycles phase b c = elapsedCycles phase a c
```

**`Time.CaesiumClock.cyclesPerSecond`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/Time/CaesiumClock.lean#L68).

> The number of periods stipulated by the SI definition of one second.

```lean
def cyclesPerSecond : ℕ
```

**`Time.CaesiumClock.IsCalibrated`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/Time/CaesiumClock.lean#L72).

> A uniform clock is calibrated in coordinate unit `u` when a single interval of one second
> advances its phase by the defining count. The starting instant need not be specified.

```lean
def IsCalibrated (phase : Time →ᵃ[ℝ] ℝ) (u : TimeUnit) : Prop
```

**`Time.CaesiumClock.isCalibrated_iff_rate`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/Time/CaesiumClock.lean#L82).

> One calibration interval determines the rate in cycles per coordinate unit.

```lean
lemma isCalibrated_iff_rate (phase : Time →ᵃ[ℝ] ℝ) (u : TimeUnit) :
    IsCalibrated phase u ↔ phase.linear 1 = (u / seconds : ℝ) * cyclesPerSecond
```

## B. Recovering the unit and measuring durations

**`Time.CaesiumClock.unitOfReadings`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/Time/CaesiumClock.lean#L104).

> The coordinate time unit inferred from two instants and the observed number of cycles
> between them. Its size in seconds is the cycle count divided by the SI count and by the
> coordinate duration.

```lean
def unitOfReadings (start stop : Time) (count : ℝ) (ht : 0 < stop -ᵥ start) (hc : 0 < count) :
    TimeUnit
```

**`Time.CaesiumClock.isCalibrated_iff_eq_unitOfReadings`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/Time/CaesiumClock.lean#L111).

> For a uniform caesium clock, any two increasing phase readings in forward time determine
> the unique calibrated unit, without a prior calibration or an independent rate measurement.

```lean
lemma isCalibrated_iff_eq_unitOfReadings (phase : Time →ᵃ[ℝ] ℝ) (u : TimeUnit)
    (start stop : Time) (ht : 0 < stop -ᵥ start) (hc : 0 < elapsedCycles phase start stop) :
    IsCalibrated phase u ↔
      u = unitOfReadings start stop (elapsedCycles phase start stop) ht hc
```

**`Time.CaesiumClock.elapsed_seconds`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/Time/CaesiumClock.lean#L130).

> Dividing the signed cycle count by the SI defining count gives the elapsed time in seconds,
> even when the input instants use a different unit.

```lean
lemma elapsed_seconds {phase : Time →ᵃ[ℝ] ℝ} {u : TimeUnit} (h : IsCalibrated phase u)
    (start stop : Time) :
    elapsedCycles phase start stop / cyclesPerSecond = (stop -ᵥ start) * (u / seconds : ℝ)
```

**`Time.CaesiumClock.one_second_iff`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/Time/CaesiumClock.lean#L138).

> A pair of readings differs by the defining cycle count exactly when the second instant
> is one SI second after the first, expressed in the coordinate unit.

```lean
lemma one_second_iff {phase : Time →ᵃ[ℝ] ℝ} {u : TimeUnit} (h : IsCalibrated phase u)
    (start stop : Time) :
    stop -ᵥ start = (seconds / u : ℝ) ↔ elapsedCycles phase start stop = cyclesPerSecond
```

## Depends on

- [Time](../../../physlib/spaceandtime/time/basic.md)
- [Units on time](../../../physlib/spaceandtime/time/timeunit.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/Time/CaesiumClock.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/SpaceAndTime/Time/CaesiumClock.lean)

---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannTransfer.clock, ClassicalMechanics.HohmannTransfer.hasDerivAt_clock, ClassicalMechanics.HohmannTransfer.clock_continuous, ClassicalMechanics.HohmannTransfer.clock_strictMono, ClassicalMechanics.HohmannTransfer.clock_bounds, ClassicalMechanics.HohmannTransfer.clock_surjective, ClassicalMechanics.HohmannTransfer.clockIso, ClassicalMechanics.HohmannTransfer.anomaly
statement: formalized
proof: formalized
---

# Kepler time for the Hohmann ellipse

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Dynamics.KeplerClock`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean): 21 declarations, 3 with a docstring.

> The eccentric anomaly is obtained by inverting Kepler time.

## i. Overview

> The derivative of the clock is strictly positive for eccentricity below one. Monotonicity and
> surjectivity give an inverse on all real times, whose derivative follows from the inverse rule.

## ii. Key results

> - `hasDerivAt_anomaly` gives the main result of this module.

## iv. References

> - [ref: hohmann\_jpl\_orbital\_mechanics] describes the Hohmann ellipse and its apses.

## A. The clock and its inverse

**`ClassicalMechanics.HohmannTransfer.clock`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L42).

> The elapsed Kepler time at a given eccentric anomaly.

```lean
def clock (p : Parameters) (u : ℝ) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.hasDerivAt_clock`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L44).

```lean
lemma hasDerivAt_clock (p : Parameters) (u : ℝ) :
    HasDerivAt (clock p) (D p u / p.n) u
```

**`ClassicalMechanics.HohmannTransfer.clock_continuous`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L47).

```lean
lemma clock_continuous (p : Parameters) : Continuous (clock p)
```

**`ClassicalMechanics.HohmannTransfer.clock_strictMono`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L49).

```lean
lemma clock_strictMono (p : Parameters) : StrictMono (clock p)
```

**`ClassicalMechanics.HohmannTransfer.clock_bounds`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L53).

```lean
lemma clock_bounds (p : Parameters) (u : ℝ) :
    (u-p.e)/p.n ≤ clock p u ∧ clock p u ≤ (u+p.e)/p.n
```

**`ClassicalMechanics.HohmannTransfer.clock_surjective`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L60).

```lean
lemma clock_surjective (p : Parameters) : Function.Surjective (clock p)
```

**`ClassicalMechanics.HohmannTransfer.clockIso`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L73).

> The inverse is the inverse of a proved order isomorphism.

```lean
def clockIso (p : Parameters) : ℝ ≃o ℝ
```

**`ClassicalMechanics.HohmannTransfer.anomaly`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L81).

> The eccentric anomaly at the given physical time.

```lean
def anomaly (p : Parameters) (t : ℝ) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.clock_anomaly`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L83).

```lean
lemma clock_anomaly (p : Parameters) (t : ℝ) : clock p (anomaly p t) = t
```

**`ClassicalMechanics.HohmannTransfer.anomaly_clock`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L85).

```lean
lemma anomaly_clock (p : Parameters) (u : ℝ) : anomaly p (clock p u) = u
```

**`ClassicalMechanics.HohmannTransfer.anomaly_continuous`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L87).

```lean
lemma anomaly_continuous (p : Parameters) : Continuous (anomaly p)
```

**`ClassicalMechanics.HohmannTransfer.anomaly_strictMono`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L89).

```lean
lemma anomaly_strictMono (p : Parameters) : StrictMono (anomaly p)
```

**`ClassicalMechanics.HohmannTransfer.hasDerivAt_anomaly`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L91).

```lean
lemma hasDerivAt_anomaly (p : Parameters) (t : ℝ) :
    HasDerivAt (anomaly p) (p.n / D p (anomaly p t)) t
```

**`ClassicalMechanics.HohmannTransfer.clock_zero`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L99).

```lean
lemma clock_zero (p : Parameters) : clock p 0 = 0
```

**`ClassicalMechanics.HohmannTransfer.clock_pi`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L100).

```lean
lemma clock_pi (p : Parameters) : clock p Real.pi = p.transferTime
```

**`ClassicalMechanics.HohmannTransfer.anomaly_zero`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L102).

```lean
lemma anomaly_zero (p : Parameters) : anomaly p 0 = 0
```

**`ClassicalMechanics.HohmannTransfer.anomaly_transferTime`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L104).

```lean
lemma anomaly_transferTime (p : Parameters) :
    anomaly p p.transferTime = Real.pi
```

**`ClassicalMechanics.HohmannTransfer.kepler_equation`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L107).

```lean
lemma kepler_equation (p : Parameters) (t : ℝ) :
    anomaly p t - p.e * Real.sin (anomaly p t) = p.n*t
```

**`ClassicalMechanics.HohmannTransfer.anomaly_bounds`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L112).

```lean
lemma anomaly_bounds (p : Parameters) {t : ℝ} (ht : t ∈ Set.Icc 0 p.transferTime) :
    anomaly p t ∈ Set.Icc 0 Real.pi
```

**`ClassicalMechanics.HohmannTransfer.clock_add_two_pi`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L117).

```lean
lemma clock_add_two_pi (p : Parameters) (u : ℝ) :
    clock p (u+2*Real.pi) = clock p u + 2*p.transferTime
```

**`ClassicalMechanics.HohmannTransfer.anomaly_add_period`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean#L121).

```lean
lemma anomaly_add_period (p : Parameters) (t : ℝ) :
    anomaly p (t+2*p.transferTime) = anomaly p t + 2*Real.pi
```

## Depends on

- [Geometry of the Hohmann ellipse](hohmann-dynamics-geometry.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/KeplerClock.lean)

---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannOptimality.Bielliptic.Parameters, ClassicalMechanics.HohmannOptimality.Bielliptic.departureSpeed, ClassicalMechanics.HohmannOptimality.Bielliptic.arrivalSpeed, ClassicalMechanics.HohmannOptimality.Bielliptic.firstApoSpeed, ClassicalMechanics.HohmannOptimality.Bielliptic.secondApoSpeed, ClassicalMechanics.HohmannOptimality.Bielliptic.cost, ClassicalMechanics.HohmannOptimality.Bielliptic.hohmannPeri, ClassicalMechanics.HohmannOptimality.Bielliptic.hohmannCost
statement: formalized
proof: formalized
---

# The cost of a finite bielliptic transfer

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Optimality.Bielliptic`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean): 26 declarations, 14 with a docstring.

> A third burn can reduce total impulse for a finite radius ratio.

## i. Overview

> In normalized units the radii are 1, 64 and 16. Rational bounds on three square roots certify a
> strict margin greater than 9/1000 in the summed speed changes.

## ii. Key results

> - `Bielliptic.finite_bielliptic_saves_deltaV` gives the main result of this module.

## iv. References

> - [ref: hohmann\_weber\_bielliptic]. Weber describes the three-burn bielliptic transfer geometry.

## A. The three-burn cost and its strict margin

**`ClassicalMechanics.HohmannOptimality.Bielliptic.Parameters`**, a structure, [line 45](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L45).

> Normalized radii: departure 1, target R, common apocentre B.

```lean
structure Parameters where
  /-- The final circular radius in units of the initial radius. -/
  R : ℝ
  /-- The common apoapsis radius in units of the initial radius. -/
  B : ℝ
  /-- The final radius exceeds the initial radius. -/
  one_lt_R : 1 < R
  /-- The common apoapsis lies outside the final circle. -/
  R_lt_B : R < B
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.departureSpeed`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L56).

> First ellipse periapsis speed.

```lean
def departureSpeed (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.arrivalSpeed`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L58).

> Second ellipse periapsis speed at the final radius.

```lean
def arrivalSpeed (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.firstApoSpeed`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L60).

> The first ellipse speed at the common apoapsis.

```lean
def firstApoSpeed (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.secondApoSpeed`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L62).

> The second ellipse speed at the common apoapsis.

```lean
def secondApoSpeed (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.cost`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L64).

> Three actual speed-jump magnitudes; the final burn is retrograde.

```lean
def cost (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.hohmannPeri`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L69).

> The normalized periapsis speed of the direct Hohmann transfer.

```lean
def hohmannPeri (R : ℝ) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.hohmannCost`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L71).

> The normalized cost of a direct Hohmann transfer to radius `R`.

```lean
def hohmannCost (R : ℝ) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.time`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L75).

> The sum of the two bielliptic half-periods in normalized units.

```lean
def time (p : Parameters) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.hohmannTime`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L78).

> The direct Hohmann half-period in normalized units.

```lean
def hohmannTime (R : ℝ) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.cost_nonneg`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L80).

```lean
lemma cost_nonneg (p : Parameters) : 0 ≤ cost p
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.time_pos`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L83).

```lean
lemma time_pos (p : Parameters) : 0 < time p
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.«example»`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L90).

> Concrete finite-radius witness.

```lean
def «example» : Parameters
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.example_departure`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L92).

```lean
lemma example_departure : departureSpeed «example» = Real.sqrt (128/65 : ℝ)
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.example_arrival`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L94).

```lean
lemma example_arrival : arrivalSpeed «example» = Real.sqrt (1/10 : ℝ)
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.example_hohmann`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L96).

```lean
lemma example_hohmann : hohmannPeri 16 = Real.sqrt (32/17 : ℝ)
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.sqrt_rational_interval`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L100).

> Rational squared bounds; no floating-point/native evaluation is involved.

```lean
lemma sqrt_rational_interval {x l u : ℝ} (_hl : 0 ≤ l) (hu : 0 ≤ u)
    (hlo : l^2 ≤ x) (hhi : x ≤ u^2) : l ≤ Real.sqrt x ∧ Real.sqrt x ≤ u
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.example_root_H_bounds`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L107).

```lean
lemma example_root_H_bounds :
    (13719/10000 : ℝ) ≤ Real.sqrt (32/17 : ℝ) ∧
      Real.sqrt (32/17 : ℝ) ≤ (1372/1000 : ℝ)
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.example_root_A_bounds`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L111).

```lean
lemma example_root_A_bounds :
    (7/5 : ℝ) ≤ Real.sqrt (128/65 : ℝ) ∧
      Real.sqrt (128/65 : ℝ) ≤ (14033/10000 : ℝ)
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.example_root_D_bounds`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L115).

```lean
lemma example_root_D_bounds :
    (31/100 : ℝ) ≤ Real.sqrt (1/10 : ℝ) ∧
      Real.sqrt (1/10 : ℝ) ≤ (31623/100000 : ℝ)
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.example_cost_closed`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L120).

```lean
lemma example_cost_closed : cost «example» =
    (63/64 : ℝ)*Real.sqrt (128/65 : ℝ) +
      (5/4 : ℝ)*Real.sqrt (1/10 : ℝ) - (5/4 : ℝ)
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.example_hohmann_closed`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L138).

```lean
lemma example_hohmann_closed : hohmannCost 16 =
    (15/16 : ℝ)*Real.sqrt (32/17 : ℝ)-(3/4 : ℝ)
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.finite_bielliptic_saves_deltaV`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L149).

> Exact strict margin: over 0.009 times the departure circular speed.

```lean
lemma finite_bielliptic_saves_deltaV :
    (9/1000 : ℝ) < hohmannCost 16 - cost «example»
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.finite_bielliptic_beats_hohmann`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L157).

```lean
lemma finite_bielliptic_beats_hohmann : cost «example» < hohmannCost 16
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.not_universally_best_against_bielliptic`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L162).

> This refutes an unrestricted optimality claim already in a small subclass
> of three-burn transfers. It does not identify the all-impulse global optimum.

```lean
lemma not_universally_best_against_bielliptic :
    ¬ (∀ p : Parameters, hohmannCost p.R ≤ cost p)
```

**`ClassicalMechanics.HohmannOptimality.Bielliptic.scaled_counterexample`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean#L170).

```lean
lemma scaled_counterexample {v : ℝ} (hv : 0 < v) :
    v*cost «example» < v*hohmannCost 16
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Bielliptic.lean)

---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannOptimality.Shape, ClassicalMechanics.HohmannOptimality.Shape.circularOuter, ClassicalMechanics.HohmannOptimality.Shape.hH, ClassicalMechanics.HohmannOptimality.Shape.energyH, ClassicalMechanics.HohmannOptimality.Shape.burnH₁, ClassicalMechanics.HohmannOptimality.Shape.burnH₂, ClassicalMechanics.HohmannOptimality.Shape.costH, ClassicalMechanics.HohmannOptimality.Shape.sum_pos
statement: formalized
proof: formalized
---

# Dimensionless Hohmann parameters

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Optimality.Shape`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean): 31 declarations, 10 with a docstring.

> The reciprocal radius ratio determines the normalized Hohmann cost.

## i. Overview

> Use the inner radius and its circular speed as units. The Hohmann invariant pair lies at the
> intersection of two inequalities for the squared radial speeds.

## ii. Key results

> - `Shape.corner_feasible` gives the main result of this module.

## iv. References

> - [ref: hohmann\_prussing\_1992]. Prussing studies the two-impulse global comparison.

## A. Normalized invariants and feasibility

**`ClassicalMechanics.HohmannOptimality.Shape`**, a structure, [line 51](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L51).

> Reciprocal radius ratio. Length unit is r₁; speed unit is √(μ/r₁).

```lean
structure Shape where
  /-- The inner circular radius divided by the outer circular radius. -/
  alpha : ℝ
  /-- The radius ratio is positive. -/
  alpha_pos : 0 < alpha
  /-- The radius ratio is less than one. -/
  alpha_lt_one : alpha < 1
```

**`ClassicalMechanics.HohmannOptimality.Shape.circularOuter`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L62).

> The outer circular speed in units of the inner circular speed.

```lean
def circularOuter (s : Shape) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Shape.hH`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L64).

> The signed angular momentum of the normalized Hohmann coast.

```lean
def hH (s : Shape) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Shape.energyH`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L66).

> Twice the normalized specific energy of the Hohmann coast.

```lean
def energyH (s : Shape) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Shape.burnH₁`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L68).

> The conserved energy variable is twice specific energy in speed units.

```lean
def burnH₁ (s : Shape) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Shape.burnH₂`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L70).

> The normalized magnitude of the Hohmann arrival impulse.

```lean
def burnH₂ (s : Shape) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Shape.costH`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L72).

> The sum of the two normalized Hohmann impulse magnitudes.

```lean
def costH (s : Shape) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Shape.sum_pos`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L74).

```lean
lemma sum_pos (s : Shape) : 0 < 1 + s.alpha
```

**`ClassicalMechanics.HohmannOptimality.Shape.c_pos`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L75).

```lean
lemma c_pos (s : Shape) : 0 < s.circularOuter
```

**`ClassicalMechanics.HohmannOptimality.Shape.c_sq`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L76).

```lean
lemma c_sq (s : Shape) : s.circularOuter ^ 2 = s.alpha
```

**`ClassicalMechanics.HohmannOptimality.Shape.c_lt_one`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L78).

```lean
lemma c_lt_one (s : Shape) : s.circularOuter < 1
```

**`ClassicalMechanics.HohmannOptimality.Shape.h_pos`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L80).

```lean
lemma h_pos (s : Shape) : 0 < s.hH
```

**`ClassicalMechanics.HohmannOptimality.Shape.h_sq`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L82).

```lean
lemma h_sq (s : Shape) : s.hH ^ 2 = 2 / (1 + s.alpha)
```

**`ClassicalMechanics.HohmannOptimality.Shape.h_sq_mul`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L84).

```lean
lemma h_sq_mul (s : Shape) : s.hH ^ 2 * (1 + s.alpha) = 2
```

**`ClassicalMechanics.HohmannOptimality.Shape.one_lt_h_sq`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L87).

```lean
lemma one_lt_h_sq (s : Shape) : 1 < s.hH ^ 2
```

**`ClassicalMechanics.HohmannOptimality.Shape.one_lt_h`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L91).

```lean
lemma one_lt_h (s : Shape) : 1 < s.hH
```

**`ClassicalMechanics.HohmannOptimality.Shape.alpha_h_sq_lt_one`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L93).

```lean
lemma alpha_h_sq_lt_one (s : Shape) : s.alpha * s.hH ^ 2 < 1
```

**`ClassicalMechanics.HohmannOptimality.Shape.alpha_h_lt_c`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L95).

```lean
lemma alpha_h_lt_c (s : Shape) : s.alpha * s.hH < s.circularOuter
```

**`ClassicalMechanics.HohmannOptimality.Shape.alpha_c_lt_one`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L99).

```lean
lemma alpha_c_lt_one (s : Shape) : s.alpha * s.circularOuter < 1
```

**`ClassicalMechanics.HohmannOptimality.Shape.alpha_sq_h_lt_one`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L102).

```lean
lemma alpha_sq_h_lt_one (s : Shape) : s.alpha ^ 2 * s.hH < 1
```

**`ClassicalMechanics.HohmannOptimality.Shape.alpha_c_lt_h`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L105).

```lean
lemma alpha_c_lt_h (s : Shape) : s.alpha * s.circularOuter < s.hH
```

**`ClassicalMechanics.HohmannOptimality.Shape.corner_inner`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L107).

```lean
lemma corner_inner (s : Shape) : s.energyH + 2 = s.hH ^ 2
```

**`ClassicalMechanics.HohmannOptimality.Shape.corner_outer`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L110).

```lean
lemma corner_outer (s : Shape) : s.energyH + 2 * s.alpha = s.alpha ^ 2 * s.hH ^ 2
```

**`ClassicalMechanics.HohmannOptimality.Shape.corner_relation`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L114).

```lean
lemma corner_relation (s : Shape) :
    s.alpha ^ 2 * s.hH ^ 2 - 2 * s.alpha = s.hH ^ 2 - 2
```

**`ClassicalMechanics.HohmannOptimality.Shape.burnH₁_pos`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L119).

```lean
lemma burnH₁_pos (s : Shape) : 0 < s.burnH₁
```

**`ClassicalMechanics.HohmannOptimality.Shape.burnH₂_pos`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L120).

```lean
lemma burnH₂_pos (s : Shape) : 0 < s.burnH₂
```

**`ClassicalMechanics.HohmannOptimality.Shape.costH_pos`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L121).

```lean
lemma costH_pos (s : Shape) : 0 < s.costH
```

**`ClassicalMechanics.HohmannOptimality.Shape.Feasible`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L125).

> Both radial-speed squares must be nonnegative. h is signed: retrograde
> coasts are not silently excluded. This is a relaxation, not a trajectory.

```lean
def Feasible (s : Shape) (w h : ℝ) : Prop
```

**`ClassicalMechanics.HohmannOptimality.Shape.corner_feasible`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L128).

```lean
lemma corner_feasible (s : Shape) : s.Feasible s.energyH s.hH
```

**`ClassicalMechanics.HohmannOptimality.Shape.burnSquare₁`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L134).

> The first squared impulse expressed in the normalized invariant pair.

```lean
def burnSquare₁ (_s : Shape) (w h : ℝ) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.Shape.burnSquare₂`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean#L136).

> The second squared impulse expressed in the normalized invariant pair.

```lean
def burnSquare₂ (s : Shape) (w h : ℝ) : ℝ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Shape.lean)

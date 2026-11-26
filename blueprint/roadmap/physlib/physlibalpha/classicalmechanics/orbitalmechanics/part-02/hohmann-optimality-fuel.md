---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannOptimality.idealPropellantFraction, ClassicalMechanics.HohmannOptimality.idealPropellantFraction_mono, ClassicalMechanics.HohmannOptimality.idealPropellantFraction_strict, ClassicalMechanics.HohmannOptimality.remaining_fraction_two_burns, ClassicalMechanics.HohmannOptimality.newton_arc_ideal_fuel_lower_bound
statement: formalized
proof: formalized
---

# Hohmann optimality in the ideal rocket model

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Optimality.Fuel`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Fuel.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Fuel.lean): 5 declarations, 2 with a docstring.

> Fixed positive exhaust speed transfers the impulse bound to propellant fraction.

## i. Overview

> The ideal rocket equation gives the fraction consumed as a function of total delta-v at fixed
> exhaust speed. Monotonicity transfers the two-impulse bound to this model.

## ii. Key results

> - `newton_arc_ideal_fuel_lower_bound` gives the main result of this module.

## iv. References

> - [ref: hohmann\_nasa\_rocket]. NASA Glenn gives the ideal rocket equation.

## A. The ideal propellant fraction

**`ClassicalMechanics.HohmannOptimality.idealPropellantFraction`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Fuel.lean#L43).

> The fraction of initial mass consumed at fixed exhaust speed.

```lean
def idealPropellantFraction (exhaustSpeed deltaV : ℝ) : ℝ
```

**`ClassicalMechanics.HohmannOptimality.idealPropellantFraction_mono`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Fuel.lean#L46).

```lean
lemma idealPropellantFraction_mono {ve d₁ d₂ : ℝ} (hExhaustSpeed : 0 < ve) (hd : d₁ ≤ d₂) :
    idealPropellantFraction ve d₁ ≤ idealPropellantFraction ve d₂
```

**`ClassicalMechanics.HohmannOptimality.idealPropellantFraction_strict`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Fuel.lean#L54).

```lean
lemma idealPropellantFraction_strict {ve d₁ d₂ : ℝ} (hExhaustSpeed : 0 < ve) (hd : d₁ < d₂) :
    idealPropellantFraction ve d₁ < idealPropellantFraction ve d₂
```

**`ClassicalMechanics.HohmannOptimality.remaining_fraction_two_burns`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Fuel.lean#L64).

> Equal exhaust speed makes multiplying burn mass ratios equivalent to using
> sum delta-v; this is the ONLY fuel interpretation used here.

```lean
lemma remaining_fraction_two_burns (ve d₁ d₂ : ℝ) :
    Real.exp (-d₁/ve)*Real.exp (-d₂/ve) = Real.exp (-(d₁+d₂)/ve)
```

**`ClassicalMechanics.HohmannOptimality.newton_arc_ideal_fuel_lower_bound`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Fuel.lean#L70).

```lean
lemma newton_arc_ideal_fuel_lower_bound (p : Units) (a : KeplerArc p.mu)
    (h₀ : (a.state a.t₀).radius=p.r₁) (h₁ : (a.state a.t₁).radius=p.r₂)
    {ve : ℝ} (hExhaustSpeed : 0 < ve) :
    idealPropellantFraction ve p.bound ≤ idealPropellantFraction ve
      ((a.state a.t₀).impulse p.speed+(a.state a.t₁).impulse p.circular₂)
```

## Depends on

- [Kepler conservation and two-impulse bounds](hohmann-optimality-keplerconservation.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Fuel.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/Fuel.lean)

---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannOptimality.BiellipticWitness.first, ClassicalMechanics.HohmannOptimality.BiellipticWitness.second, ClassicalMechanics.HohmannOptimality.BiellipticWitness.direct, ClassicalMechanics.HohmannOptimality.BiellipticWitness.secondPosition, ClassicalMechanics.HohmannOptimality.BiellipticWitness.secondVelocity, ClassicalMechanics.HohmannOptimality.BiellipticWitness.totalTime, ClassicalMechanics.HohmannOptimality.BiellipticWitness.jump₁, ClassicalMechanics.HohmannOptimality.BiellipticWitness.jump₂
statement: formalized
proof: formalized
---

# A physical bielliptic counterexample

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Optimality.BiellipticWitness`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean): 31 declarations, 11 with a docstring.

> Two actual Newtonian coasts realize a cheaper three-impulse maneuver.

## i. Overview

> The first arc travels from radius 1 to the common apoapsis at 64. The second travels from that
> apoapsis to radius 16. The three actual velocity jumps give the strict cost comparison.

## ii. Key results

> - `BiellipticWitness.physical_three_impulse_counterexample` gives the main result of this module.

## iv. References

> - [ref: hohmann\_weber\_bielliptic]. Weber describes the three-burn bielliptic transfer geometry.

## A. The two coasts and the three velocity jumps

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.first`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L44).

> The first coast from radius 1 to the common apoapsis at radius 64.

```lean
def first : Parameters
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.second`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L46).

> The ellipse with periapsis at radius 16 and apoapsis at radius 64.

```lean
def second : Parameters
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.direct`**, a def, [line 48](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L48).

> The comparison Hohmann transfer from radius 1 to radius 16.

```lean
def direct : Parameters
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.secondPosition`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L50).

> The position along the second coast, timed from apoapsis.

```lean
def secondPosition (t : ℝ) : ℂ
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.secondVelocity`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L52).

> The velocity along the second coast, timed from apoapsis.

```lean
def secondVelocity (t : ℝ) : ℂ
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.totalTime`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L54).

> The combined duration of the two bielliptic coasts.

```lean
def totalTime : ℝ
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.jump₁`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L57).

> The velocity jump from the inner circle onto the first ellipse.

```lean
def jump₁ : ℂ
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.jump₂`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L59).

> The velocity jump between ellipses at the common apoapsis.

```lean
def jump₂ : ℂ
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.jump₃`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L61).

> The velocity jump from the second ellipse onto the final circle.

```lean
def jump₃ : ℂ
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.cost`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L63).

> The sum of the impulse magnitudes for the specified transfer.

```lean
def cost : ℝ
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.secondPosition_deriv`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L65).

```lean
lemma secondPosition_deriv (t : ℝ) : HasDerivAt secondPosition (secondVelocity t) t
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.secondVelocity_deriv`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L71).

```lean
lemma secondVelocity_deriv (t : ℝ) :
    HasDerivAt secondVelocity (-(1/‖secondPosition t‖^3) • secondPosition t) t
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.second_newton`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L78).

```lean
lemma second_newton (t : ℝ) :
    deriv (deriv secondPosition) t = -(1/‖secondPosition t‖^3) • secondPosition t
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.second_start`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L83).

```lean
lemma second_start : secondPosition 0=pack (-64) 0
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.second_end`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L85).

```lean
lemma second_end : secondPosition second.transferTime=pack 16 0
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.second_velocity_start`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L88).

```lean
lemma second_velocity_start : secondVelocity 0=pack 0 (-apoSpeed second)
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.second_velocity_end`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L90).

```lean
lemma second_velocity_end : secondVelocity second.transferTime=pack 0 (periSpeed second)
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.junction`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L93).

```lean
lemma junction : position first first.transferTime=secondPosition 0
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.time_pos`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L96).

```lean
lemma time_pos : 0 < totalTime
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.first_peri`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L98).

```lean
lemma first_peri : periSpeed first=Real.sqrt (128/65 : ℝ)
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.second_peri`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L101).

```lean
lemma second_peri : periSpeed second=Real.sqrt (1/10 : ℝ)
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.first_apo`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L104).

```lean
lemma first_apo : apoSpeed first=Real.sqrt (128/65 : ℝ)/64
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.second_apo`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L113).

```lean
lemma second_apo : apoSpeed second=Real.sqrt (1/10 : ℝ)/4
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.direct_peri`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L122).

```lean
lemma direct_peri : periSpeed direct=Real.sqrt (32/17 : ℝ)
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.direct_apo`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L125).

```lean
lemma direct_apo : apoSpeed direct=Real.sqrt (32/17 : ℝ)/16
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.direct_cost`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L134).

```lean
lemma direct_cost : totalDeltaV direct=Bielliptic.hohmannCost 16
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.jump₁_norm`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L141).

```lean
lemma jump₁_norm : ‖jump₁‖=|Real.sqrt (128/65 : ℝ)-1|
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.jump₂_norm`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L144).

```lean
lemma jump₂_norm : ‖jump₂‖=|Real.sqrt (1/10 : ℝ)/4-Real.sqrt (128/65 : ℝ)/64|
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.jump₃_norm`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L152).

```lean
lemma jump₃_norm : ‖jump₃‖=|Real.sqrt (1/10 : ℝ)-(1/4 : ℝ)|
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.cost_eq`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L157).

```lean
lemma cost_eq : cost=Bielliptic.cost Bielliptic.«example»
```

**`ClassicalMechanics.HohmannOptimality.BiellipticWitness.physical_three_impulse_counterexample`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean#L167).

> The numerical comparison is linked to actual finite-time coast arcs and
> actual vector jump norms. No arrival time or third burn is sent to infinity.

```lean
lemma physical_three_impulse_counterexample :
    0 < totalTime ∧
    (∀ t, deriv (deriv (position first)) t =
      -(1/‖position first t‖^3) • position first t) ∧
    (∀ t, deriv (deriv secondPosition) t =
      -(1/‖secondPosition t‖^3) • secondPosition t) ∧
    position first 0=pack 1 0 ∧
    position first first.transferTime=secondPosition 0 ∧
    secondPosition second.transferTime=pack 16 0 ∧
    (9/1000 : ℝ) < totalDeltaV direct-(‖jump₁‖+‖jump₂‖+‖jump₃‖)
```

## Depends on

- [The two Hohmann velocity impulses](hohmann-dynamics-impulses.md)
- [The cost of a finite bielliptic transfer](hohmann-optimality-bielliptic.md)

## Proof depends on

- [Newtonian dynamics of the Hohmann ellipse](hohmann-dynamics-dynamics.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/BiellipticWitness.lean)

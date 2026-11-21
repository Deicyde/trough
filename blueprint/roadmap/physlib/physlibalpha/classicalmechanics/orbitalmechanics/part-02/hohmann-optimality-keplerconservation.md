---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannOptimality.KeplerArc, ClassicalMechanics.HohmannOptimality.KeplerArc.state, ClassicalMechanics.HohmannOptimality.KeplerArc.left_mem, ClassicalMechanics.HohmannOptimality.KeplerArc.right_mem, ClassicalMechanics.HohmannOptimality.KeplerArc.radius_deriv, ClassicalMechanics.HohmannOptimality.KeplerArc.angular_deriv_zero, ClassicalMechanics.HohmannOptimality.KeplerArc.energy_deriv_zero, ClassicalMechanics.HohmannOptimality.KeplerArc.equal_endpoints_of_zero_deriv
statement: formalized
proof: formalized
---

# Kepler conservation and two-impulse bounds

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Optimality.KeplerConservation`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean): 13 declarations, 5 with a docstring.

> Newtonian coast arcs supply the endpoint invariants needed for the cost bound.

## i. Overview

> A comparison arc has differentiable position and velocity and avoids the centre throughout a
> finite interval. The Newtonian equation gives constant energy and angular momentum without
> restricting their signs.

## ii. Key results

> - `KeplerArc.newton_arc_lower_bound` gives the main result of this module.

## iv. References

> - [ref: hohmann\_prussing\_1992]. Prussing studies the two-impulse global comparison.

## A. Conservation along an arbitrary comparison arc

**`ClassicalMechanics.HohmannOptimality.KeplerArc`**, a structure, [line 44](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean#L44).

> A noncollision Newtonian coast over a positive finite time interval.

```lean
structure KeplerArc (mu : ℝ) where
  /-- The time of the departure impulse. -/
  t₀ : ℝ
  /-- The time of the arrival impulse. -/
  t₁ : ℝ
  /-- The coast takes positive time. -/
  time_order : t₀ < t₁
  /-- The first Cartesian position coordinate as a function of time. -/
  x : ℝ → ℝ
  /-- The second Cartesian position coordinate as a function of time. -/
  y : ℝ → ℝ
  /-- The first Cartesian velocity coordinate as a function of time. -/
  vx : ℝ → ℝ
  /-- The second Cartesian velocity coordinate as a function of time. -/
  vy : ℝ → ℝ
  /-- The coast stays away from the attracting centre. -/
  radius_pos : ∀ t ∈ Icc t₀ t₁, 0 < Real.sqrt (x t^2+y t^2)
  /-- The first position derivative is the first velocity component. -/
  dx : ∀ t ∈ Icc t₀ t₁, HasDerivAt x (vx t) t
  /-- The second position derivative is the second velocity component. -/
  dy : ∀ t ∈ Icc t₀ t₁, HasDerivAt y (vy t) t
  /-- The first velocity derivative obeys Newtonian central acceleration. -/
  dvx : ∀ t ∈ Icc t₀ t₁,
    HasDerivAt vx (-mu*x t/(Real.sqrt (x t^2+y t^2))^3) t
  /-- The second velocity derivative obeys Newtonian central acceleration. -/
  dvy : ∀ t ∈ Icc t₀ t₁,
    HasDerivAt vy (-mu*y t/(Real.sqrt (x t^2+y t^2))^3) t
```

**`ClassicalMechanics.HohmannOptimality.KeplerArc.state`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean#L75).

> The Cartesian state of the coast at the given time.

```lean
def state {mu : ℝ} (a : KeplerArc mu) (t : ℝ) : PlanarState
```

**`ClassicalMechanics.HohmannOptimality.KeplerArc.left_mem`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean#L77).

```lean
lemma left_mem {mu : ℝ} (a : KeplerArc mu) : a.t₀ ∈ Icc a.t₀ a.t₁
```

**`ClassicalMechanics.HohmannOptimality.KeplerArc.right_mem`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean#L79).

```lean
lemma right_mem {mu : ℝ} (a : KeplerArc mu) : a.t₁ ∈ Icc a.t₀ a.t₁
```

**`ClassicalMechanics.HohmannOptimality.KeplerArc.radius_deriv`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean#L82).

```lean
lemma radius_deriv {mu t : ℝ} (a : KeplerArc mu) (ht : t ∈ Icc a.t₀ a.t₁) :
    HasDerivAt (fun u => (a.state u).radius)
      ((a.x t*a.vx t+a.y t*a.vy t)/(a.state t).radius) t
```

**`ClassicalMechanics.HohmannOptimality.KeplerArc.angular_deriv_zero`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean#L97).

```lean
lemma angular_deriv_zero {mu t : ℝ} (a : KeplerArc mu) (ht : t ∈ Icc a.t₀ a.t₁) :
    HasDerivAt (fun u => (a.state u).angular) 0 t
```

**`ClassicalMechanics.HohmannOptimality.KeplerArc.energy_deriv_zero`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean#L105).

```lean
lemma energy_deriv_zero {mu t : ℝ} (a : KeplerArc mu) (ht : t ∈ Icc a.t₀ a.t₁) :
    HasDerivAt (fun u => (a.state u).energy mu) 0 t
```

**`ClassicalMechanics.HohmannOptimality.KeplerArc.equal_endpoints_of_zero_deriv`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean#L116).

```lean
lemma equal_endpoints_of_zero_deriv {f : ℝ → ℝ} {a b : ℝ} (hab : a ≤ b)
    (hd : ∀ t ∈ Icc a b, HasDerivAt f 0 t) : f b=f a
```

**`ClassicalMechanics.HohmannOptimality.KeplerArc.energy_conserved`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean#L126).

```lean
lemma energy_conserved {mu : ℝ} (a : KeplerArc mu) :
    (a.state a.t₀).energy mu = (a.state a.t₁).energy mu
```

**`ClassicalMechanics.HohmannOptimality.KeplerArc.angular_conserved`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean#L131).

```lean
lemma angular_conserved {mu : ℝ} (a : KeplerArc mu) :
    (a.state a.t₀).angular = (a.state a.t₁).angular
```

**`ClassicalMechanics.HohmannOptimality.KeplerArc.endpoints`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean#L138).

> Obtain endpoint constraints from the actual ODE; no conservation law is an
> input field of KeplerArc. Endpoint orientation and coast time are unrestricted.

```lean
def endpoints (p : Units) (a : KeplerArc p.mu)
    (h₀ : (a.state a.t₀).radius=p.r₁) (h₁ : (a.state a.t₁).radius=p.r₂) :
    PhysicalEndpoints p
```

**`ClassicalMechanics.HohmannOptimality.KeplerArc.newton_arc_lower_bound`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean#L156).

> Global two-impulse lower bound for every noncollision Newtonian coast arc.
> No tangency, ellipse, energy sign or positive angular momentum is assumed.

```lean
lemma newton_arc_lower_bound (p : Units) (a : KeplerArc p.mu)
    (h₀ : (a.state a.t₀).radius=p.r₁) (h₁ : (a.state a.t₁).radius=p.r₂) :
    p.bound ≤ (a.state a.t₀).impulse p.speed + (a.state a.t₁).impulse p.circular₂
```

**`ClassicalMechanics.HohmannOptimality.KeplerArc.newton_arc_equality_endpoints`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean#L164).

> Equality of the actual Cartesian cost forces the Hohmann endpoint velocities.

```lean
lemma newton_arc_equality_endpoints (p : Units) (a : KeplerArc p.mu)
    (h₀ : (a.state a.t₀).radius = p.r₁) (h₁ : (a.state a.t₁).radius = p.r₂)
    (he : (a.state a.t₀).impulse p.speed + (a.state a.t₁).impulse p.circular₂ = p.bound) :
    (a.state a.t₀).radial = 0 ∧ (a.state a.t₁).radial = 0 ∧
    (a.state a.t₀).tangent = p.speed * p.shape.hH ∧
    (a.state a.t₁).tangent = p.speed * (p.shape.alpha * p.shape.hH)
```

## Depends on

- [Restoring physical units to the Hohmann bounds](hohmann-optimality-physicalunits.md)
- [Planar states for the Hohmann comparison](hohmann-optimality-planarstate.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/KeplerConservation.lean)

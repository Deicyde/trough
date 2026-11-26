---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannOptimality.unitsOfH1, ClassicalMechanics.HohmannOptimality.h1_speed, ClassicalMechanics.HohmannOptimality.h1_outer_speed, ClassicalMechanics.HohmannOptimality.h1_peri_speed, ClassicalMechanics.HohmannOptimality.h1_apo_speed, ClassicalMechanics.HohmannOptimality.h1_bound_eq_totalDeltaV, ClassicalMechanics.HohmannOptimality.h1_global_two_impulse_minimum, ClassicalMechanics.HohmannOptimality.h1KeplerArc
statement: formalized
proof: formalized
---

# Attainment of the Hohmann lower bound

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Optimality.H1Bridge`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/H1Bridge.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/H1Bridge.lean): 10 declarations, 4 with a docstring; 2 private, not shown.

> The explicit Hohmann trajectory attains the lower bound within the comparison class.

## i. Overview

> The apsidal speeds in the explicit transfer match the normalized optimal speeds. Taking real and
> imaginary parts of the Newtonian coast gives a member of the very same comparison class used for
> the lower bound.

## ii. Key results

> - `h1_global_two_impulse_minimum` gives the main result of this module.

## iv. References

> - [ref: hohmann\_prussing\_1992]. Prussing studies the two-impulse global comparison.

## A. Physical attainment and the minimum

**`ClassicalMechanics.HohmannOptimality.unitsOfH1`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/H1Bridge.lean#L44).

> Data conversion only; no optimality assumption is added to H1.

```lean
def unitsOfH1 (p : HohmannTransfer.Parameters) : Units
```

**`ClassicalMechanics.HohmannOptimality.h1_speed`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/H1Bridge.lean#L47).

```lean
lemma h1_speed (p : HohmannTransfer.Parameters) :
    (unitsOfH1 p).speed=HohmannTransfer.circularSpeed p.mu p.r₁
```

**`ClassicalMechanics.HohmannOptimality.h1_outer_speed`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/H1Bridge.lean#L49).

```lean
lemma h1_outer_speed (p : HohmannTransfer.Parameters) :
    (unitsOfH1 p).circular₂=HohmannTransfer.circularSpeed p.mu p.r₂
```

**`ClassicalMechanics.HohmannOptimality.h1_peri_speed`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/H1Bridge.lean#L53).

```lean
lemma h1_peri_speed (p : HohmannTransfer.Parameters) :
    (unitsOfH1 p).speed*(unitsOfH1 p).shape.hH=HohmannTransfer.periSpeed p
```

**`ClassicalMechanics.HohmannOptimality.h1_apo_speed`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/H1Bridge.lean#L67).

```lean
lemma h1_apo_speed (p : HohmannTransfer.Parameters) :
    (unitsOfH1 p).speed*((unitsOfH1 p).shape.alpha*(unitsOfH1 p).shape.hH)=
      HohmannTransfer.apoSpeed p
```

**`ClassicalMechanics.HohmannOptimality.h1_bound_eq_totalDeltaV`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/H1Bridge.lean#L82).

```lean
lemma h1_bound_eq_totalDeltaV (p : HohmannTransfer.Parameters) :
    (unitsOfH1 p).bound=HohmannTransfer.totalDeltaV p
```

**`ClassicalMechanics.HohmannOptimality.h1_global_two_impulse_minimum`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/H1Bridge.lean#L97).

> Physical attainment from H1 plus a global lower bound against arbitrary
> smooth two-impulse competitors. Free time, free phase, fixed central field.

```lean
lemma h1_global_two_impulse_minimum (p : HohmannTransfer.Parameters) :
    (∀ t, deriv (deriv (HohmannTransfer.position p)) t =
      -(p.mu/‖HohmannTransfer.position p t‖^3) • HohmannTransfer.position p t) ∧
    HohmannTransfer.position p 0=HohmannTransfer.pack p.r₁ 0 ∧
    HohmannTransfer.position p p.transferTime=HohmannTransfer.pack (-p.r₂) 0 ∧
    (unitsOfH1 p).bound=
      ‖HohmannTransfer.entryImpulse p‖+‖HohmannTransfer.exitImpulse p‖ ∧
    (∀ a : KeplerArc p.mu,
      (a.state a.t₀).radius=p.r₁ → (a.state a.t₁).radius=p.r₂ →
      HohmannTransfer.totalDeltaV p ≤
        (a.state a.t₀).impulse (HohmannTransfer.circularSpeed p.mu p.r₁)+
        (a.state a.t₁).impulse (HohmannTransfer.circularSpeed p.mu p.r₂))
```

**`ClassicalMechanics.HohmannOptimality.h1KeplerArc`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/H1Bridge.lean#L118).

> The explicit H1 coast is a member of the same class used for the lower bound.

```lean
def h1KeplerArc (p : HohmannTransfer.Parameters) : KeplerArc p.mu
```

**`ClassicalMechanics.HohmannOptimality.h1_state_radius`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/H1Bridge.lean#L151).

```lean
lemma h1_state_radius (p : HohmannTransfer.Parameters) (t : ℝ) :
    ((h1KeplerArc p).state t).radius = ‖HohmannTransfer.position p t‖
```

**`ClassicalMechanics.HohmannOptimality.h1_attains_bound_in_kepler_class`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/H1Bridge.lean#L185).

> The lower bound is attained within the actual Newtonian comparison class.

```lean
lemma h1_attains_bound_in_kepler_class (p : HohmannTransfer.Parameters) :
    ∃ a : KeplerArc p.mu,
      (a.state a.t₀).radius = p.r₁ ∧ (a.state a.t₁).radius = p.r₂ ∧
      (a.state a.t₀).impulse (unitsOfH1 p).speed +
        (a.state a.t₁).impulse (unitsOfH1 p).circular₂ = (unitsOfH1 p).bound
```

## Depends on

- [The two Hohmann velocity impulses](../part-01/hohmann-dynamics-impulses.md)
- [Kepler conservation and two-impulse bounds](hohmann-optimality-keplerconservation.md)

## Proof depends on

- [Newtonian dynamics of the Hohmann ellipse](../part-01/hohmann-dynamics-dynamics.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/H1Bridge.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Optimality/H1Bridge.lean)

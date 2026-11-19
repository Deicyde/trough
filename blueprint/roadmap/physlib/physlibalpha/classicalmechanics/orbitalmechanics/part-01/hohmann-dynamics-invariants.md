---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannTransfer.specificEnergy, ClassicalMechanics.HohmannTransfer.velocity_numerator, ClassicalMechanics.HohmannTransfer.velocityAtAnomaly_norm_sq, ClassicalMechanics.HohmannTransfer.vis_viva_at_anomaly, ClassicalMechanics.HohmannTransfer.vis_viva, ClassicalMechanics.HohmannTransfer.coast_energy, ClassicalMechanics.HohmannTransfer.coast_energy_negative, ClassicalMechanics.HohmannTransfer.angular_momentum_at_anomaly
statement: formalized
proof: formalized
---

# Mechanical invariants of the Hohmann ellipse

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Dynamics.Invariants`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Invariants.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Invariants.lean): 10 declarations, 1 with a docstring.

> The elliptical coast has constant specific energy and angular momentum.

## i. Overview

> The squared speed follows the vis-viva identity. Together with the focus distance and the planar
> cross product this gives the conserved specific energy and signed angular momentum.

## ii. Key results

> - `coast_energy` gives the main result of this module.

## iv. References

> - [ref: hohmann\_jpl\_orbital\_mechanics] describes the Hohmann ellipse and its apses.

## A. Vis-viva and the two invariants

**`ClassicalMechanics.HohmannTransfer.specificEnergy`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Invariants.lean#L42).

> The sum of kinetic and gravitational potential energy per unit mass.

```lean
def specificEnergy (mu : ℝ) (q v : ℂ) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.velocity_numerator`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Invariants.lean#L44).

```lean
lemma velocity_numerator (p : Parameters) (u : ℝ) :
    p.a^2*Real.sin u^2 + p.b^2*Real.cos u^2 =
      p.a^2 * D p u * (1+p.e*Real.cos u)
```

**`ClassicalMechanics.HohmannTransfer.velocityAtAnomaly_norm_sq`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Invariants.lean#L53).

```lean
lemma velocityAtAnomaly_norm_sq (p : Parameters) (u : ℝ) :
    ‖velocityAtAnomaly p u‖^2 =
      p.n^2*p.a^2*(1+p.e*Real.cos u)/D p u
```

**`ClassicalMechanics.HohmannTransfer.vis_viva_at_anomaly`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Invariants.lean#L66).

```lean
lemma vis_viva_at_anomaly (p : Parameters) (u : ℝ) :
    ‖velocityAtAnomaly p u‖^2 = p.mu*(2/‖ellipse p u‖-1/p.a)
```

**`ClassicalMechanics.HohmannTransfer.vis_viva`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Invariants.lean#L73).

```lean
lemma vis_viva (p : Parameters) (t : ℝ) :
    ‖deriv (position p) t‖^2 = p.mu*(2/‖position p t‖-1/p.a)
```

**`ClassicalMechanics.HohmannTransfer.coast_energy`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Invariants.lean#L77).

```lean
lemma coast_energy (p : Parameters) (t : ℝ) :
    specificEnergy p.mu (position p t) (deriv (position p) t) = -p.mu/(2*p.a)
```

**`ClassicalMechanics.HohmannTransfer.coast_energy_negative`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Invariants.lean#L83).

```lean
lemma coast_energy_negative (p : Parameters) (t : ℝ) :
    specificEnergy p.mu (position p t) (deriv (position p) t) < 0
```

**`ClassicalMechanics.HohmannTransfer.angular_momentum_at_anomaly`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Invariants.lean#L87).

```lean
lemma angular_momentum_at_anomaly (p : Parameters) (u : ℝ) :
    cross (ellipse p u) (velocityAtAnomaly p u) = p.a*p.b*p.n
```

**`ClassicalMechanics.HohmannTransfer.coast_angular_momentum`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Invariants.lean#L96).

```lean
lemma coast_angular_momentum (p : Parameters) (t : ℝ) :
    cross (position p t) (deriv (position p) t) = p.a*p.b*p.n
```

**`ClassicalMechanics.HohmannTransfer.coast_angular_momentum_pos`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Invariants.lean#L100).

```lean
lemma coast_angular_momentum_pos (p : Parameters) (t : ℝ) :
    0 < cross (position p t) (deriv (position p) t)
```

## Depends on

- [Time derivatives of the Hohmann ellipse](hohmann-dynamics-differentiation.md)

## Proof depends on

- [Newtonian dynamics of the Hohmann ellipse](hohmann-dynamics-dynamics.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Invariants.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Invariants.lean)

---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannTransfer.lagrangianSystem, ClassicalMechanics.HohmannTransfer.lagrangianSystem_coord_eq, ClassicalMechanics.HohmannTransfer.eulerLagrange_position
statement: formalized
proof: formalized
---

# Lagrangian dynamics of the Hohmann transfer coast

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Dynamics.Lagrangian`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Lagrangian.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Lagrangian.lean): 3 declarations, 3 with a docstring; 7 private, not shown.

> The smooth coast satisfies the Euler–Lagrange equation for a Kepler Lagrangian on its radial range.

## i. Overview

> The inverse-radius term is singular at the centre. The normed-space constructor for
> `LagrangianSystem` requires a globally smooth Lagrangian. We smooth the inverse-radius term inside
> half the inner orbital radius. The entire transfer ellipse stays outside this region, where the
> Lagrangian is the usual kinetic term plus the gravitational parameter divided by the radius.

## ii. Key results

> - `lagrangianSystem` packages the smooth extension on the planar configuration space.
> - `lagrangianSystem_coord_eq` recovers the Kepler Lagrangian outside the modified region.
> - `eulerLagrange_position` proves that the Euler–Lagrange covector vanishes on the smooth coast.

## iv. References

> - [ref: hohmann\_jpl\_orbital\_mechanics] describes the Hohmann transfer coast.

## A. The Lagrangian on the plane

**`ClassicalMechanics.HohmannTransfer.lagrangianSystem`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Lagrangian.lean#L84).

> The Lagrangian system on the plane that agrees with the Kepler Lagrangian on the coast.

```lean
def lagrangianSystem (p : Parameters) : LagrangianSystem 𝓘(ℝ, ℂ) ⟨ℂ⟩
```

**`ClassicalMechanics.HohmannTransfer.lagrangianSystem_coord_eq`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Lagrangian.lean#L89).

> Outside the modified region the coordinate Lagrangian is the original Kepler Lagrangian.

```lean
lemma lagrangianSystem_coord_eq (p : Parameters) (t₀ : Time) (t : ℝ) {q : ℂ}
    (v : ℂ) (hq : p.r₁ / 2 ≤ ‖q‖) :
    (lagrangianSystem p).coord t₀ (t, q, v) = ‖v‖ ^ 2 / 2 + p.mu / ‖q‖
```

## B. The Euler–Lagrange equation along the coast

**`ClassicalMechanics.HohmannTransfer.eulerLagrange_position`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Lagrangian.lean#L131).

> The Hohmann transfer coast satisfies the Euler–Lagrange equation in the planar system.

```lean
lemma eulerLagrange_position (p : Parameters) (t₀ : Time) (t : ℝ) :
    eulerLagrange (lagrangianSystem p) t₀ (position p) t = 0
```

## Depends on

- [A. Euler–Lagrange equations](../../../../physlib/classicalmechanics/eulerlagrange.md)
- [Time derivatives of the Hohmann ellipse](hohmann-dynamics-differentiation.md)

## Proof depends on

- [Newtonian dynamics of the Hohmann ellipse](hohmann-dynamics-dynamics.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Lagrangian.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Lagrangian.lean)

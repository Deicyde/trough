---
declaration: module
origin: cited
lean: ClassicalMechanics.CentralForce.conservedQuantities, ClassicalMechanics.CentralForce.poissonBracket_conservedQuantities, ClassicalMechanics.CentralForce.gradient_conservedQuantities
statement: formalized
proof: formalized
---

# Conserved quantities for central forces

The module `PhyslibAlpha.ClassicalMechanics.CentralForce.ConservedQuantities`, [PhyslibAlpha/ClassicalMechanics/CentralForce/ConservedQuantities.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/ConservedQuantities.lean): 3 declarations, 3 with a docstring.

> The Hamiltonian, squared angular momentum, and axial angular momentum as a family of observables.

## i. Overview

> The central-force Hamiltonian and the squared magnitude and axial component of angular momentum
> form a family of three observables. Their Poisson brackets vanish away from the centre of force,
> and their phase-space gradients are given by the existing central-force results.

## ii. Key results

> - `CentralForce.conservedQuantities` : the three observables.
> - `CentralForce.poissonBracket_conservedQuantities` : the observables are pairwise in involution.
> - `CentralForce.gradient_conservedQuantities` : the phase-space gradients of the observables.

## iv. References

> See `PhyslibAlpha.ClassicalMechanics.CentralForce.AngularMomentum` for references.

## A. The conserved quantities

**`ClassicalMechanics.CentralForce.conservedQuantities`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/ConservedQuantities.lean#L54).

> The three conserved quantities in involution of a central-force system: the Hamiltonian `H`,
> the squared magnitude `L²` of the angular momentum, and its z-component `L_z`.

```lean
noncomputable def conservedQuantities :
    Fin 3 → EuclideanSpace ℝ (Fin 3) → EuclideanSpace ℝ (Fin 3) → ℝ
```

### A.1. Involution

**`ClassicalMechanics.CentralForce.poissonBracket_conservedQuantities`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/ConservedQuantities.lean#L66).

> Away from the centre of force, the conserved quantities of a central-force system are pairwise
> in involution.

```lean
lemma poissonBracket_conservedQuantities (i j : Fin 3) (p : EuclideanSpace ℝ (Fin 3))
    {q : EuclideanSpace ℝ (Fin 3)} (hq : q ≠ 0) :
    poissonBracket (S.conservedQuantities i) (S.conservedQuantities j) p q = 0
```

### A.2. Gradients

**`ClassicalMechanics.CentralForce.gradient_conservedQuantities`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/ConservedQuantities.lean#L88).

> Away from the centre of force, the phase-space gradients of the conserved quantities of a
> central-force system.

```lean
lemma gradient_conservedQuantities (p : EuclideanSpace ℝ (Fin 3)) {q : EuclideanSpace ℝ (Fin 3)}
    (hq : q ≠ 0) :
    (fun i => (gradient (fun p' => S.conservedQuantities i p' q) p,
      gradient (fun q' => S.conservedQuantities i p q') q)) =
    ![(S.m⁻¹ • p, (deriv S.V ‖q‖ / ‖q‖) • q),
      ((2 * ⟪q, q⟫_ℝ) • p - (2 * ⟪q, p⟫_ℝ) • q, (2 * ⟪p, p⟫_ℝ) • q - (2 * ⟪q, p⟫_ℝ) • p),
      (q 0 • EuclideanSpace.single 1 1 - q 1 • EuclideanSpace.single 0 1,
        p 1 • EuclideanSpace.single 0 1 - p 0 • EuclideanSpace.single 1 1)]
```

## Depends on

- [Angular-momentum observables under a central force](angularmomentum.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/CentralForce/ConservedQuantities.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/CentralForce/ConservedQuantities.lean)
